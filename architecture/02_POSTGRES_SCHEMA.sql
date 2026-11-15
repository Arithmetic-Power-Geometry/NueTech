-- NueTech QualityHub: Phase 2 PROPOSED PostgreSQL 15+ schema
-- Design draft, not executed. Requires PostgreSQL integration tests and security audit.
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE SCHEMA IF NOT EXISTS qualityhub;
SET search_path TO qualityhub,public;

CREATE TABLE tenants (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
 name text NOT NULL, institution_type text NOT NULL CHECK (institution_type IN ('university','college','school')),
 subtype text, board text, regulatory_id text, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE units (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 parent_id uuid REFERENCES units(id), name text NOT NULL, kind text NOT NULL,
 UNIQUE(tenant_id,id)
);
CREATE TABLE users (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), external_subject text UNIQUE NOT NULL,
 display_name text NOT NULL, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE memberships (
 tenant_id uuid NOT NULL REFERENCES tenants(id), user_id uuid NOT NULL REFERENCES users(id),
 role text NOT NULL CHECK (role IN ('owner','admin','iqac','nodal','department','reviewer','viewer')),
 PRIMARY KEY(tenant_id,user_id)
);
CREATE TABLE products (
 code text PRIMARY KEY CHECK (code IN ('university','college','school')),
 display_name text NOT NULL
);
INSERT INTO products VALUES ('university','QualityHub University'),('college','QualityHub College'),('school','QualityHub School');
CREATE TABLE licenses (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 product_code text NOT NULL REFERENCES products(code), valid_from date NOT NULL, valid_until date,
 status text NOT NULL CHECK(status IN ('trial','active','suspended','expired')),
 CHECK(valid_until IS NULL OR valid_until>=valid_from), UNIQUE(tenant_id,id)
);
CREATE TABLE framework_editions (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), issuer text NOT NULL, code text NOT NULL,
 edition text NOT NULL, status text NOT NULL CHECK(status IN ('verified_active','historical','proposed','unverified','retired')),
 source_url text NOT NULL, source_date date, effective_from date, effective_until date,
 institution_type text NOT NULL CHECK(institution_type IN ('university','college','school')),
 UNIQUE(issuer,code,edition)
);
CREATE TABLE framework_assignments (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 edition_id uuid NOT NULL REFERENCES framework_editions(id),
 scope_unit_id uuid, status text NOT NULL DEFAULT 'draft' CHECK(status IN ('draft','verified','disabled')),
 UNIQUE(tenant_id,edition_id,scope_unit_id)
);
CREATE TABLE periods (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 label text NOT NULL, kind text NOT NULL CHECK(kind IN ('academic','financial','calendar','cohort','custom')),
 starts_on date NOT NULL, ends_on date NOT NULL, CHECK(ends_on>=starts_on), UNIQUE(tenant_id,id)
);
CREATE TABLE metrics (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), edition_id uuid NOT NULL REFERENCES framework_editions(id),
 code text NOT NULL, title text NOT NULL, grain text NOT NULL, rule_spec jsonb NOT NULL DEFAULT '{}'::jsonb,
 verified_source_locator text, status text NOT NULL DEFAULT 'unverified',
 UNIQUE(edition_id,code)
);
CREATE TABLE metric_fields (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), metric_id uuid NOT NULL REFERENCES metrics(id),
 field_code text NOT NULL, data_type text NOT NULL, unit text, required boolean NOT NULL DEFAULT false,
 validation_spec jsonb NOT NULL DEFAULT '{}'::jsonb, UNIQUE(metric_id,field_code)
);
CREATE TABLE import_sources (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 name text NOT NULL, mode text NOT NULL CHECK(mode IN ('api_readonly','db_view_readonly','csv','xlsx','manual')),
 config_secret_ref text, enabled boolean NOT NULL DEFAULT true, UNIQUE(tenant_id,id)
);
CREATE TABLE import_batches (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 source_id uuid NOT NULL, content_sha256 text NOT NULL, mapping_version integer NOT NULL DEFAULT 1,
 status text NOT NULL CHECK(status IN ('staged','validated','rejected','applied','conflict')),
 created_at timestamptz NOT NULL DEFAULT now(), UNIQUE(tenant_id,source_id,content_sha256,mapping_version),
 FOREIGN KEY(tenant_id,source_id) REFERENCES import_sources(tenant_id,id), UNIQUE(tenant_id,id)
);
CREATE TABLE import_rows (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 batch_id uuid NOT NULL, source_key text NOT NULL, row_sha256 text NOT NULL,
 payload jsonb NOT NULL, validation_errors jsonb NOT NULL DEFAULT '[]'::jsonb,
 FOREIGN KEY(tenant_id,batch_id) REFERENCES import_batches(tenant_id,id), UNIQUE(batch_id,source_key), UNIQUE(tenant_id,id)
);
CREATE TABLE source_mappings (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 source_id uuid NOT NULL, domain text NOT NULL, source_column text NOT NULL,
 target_attribute text NOT NULL, transform_spec jsonb NOT NULL DEFAULT '{}'::jsonb,
 mapping_version integer NOT NULL, FOREIGN KEY(tenant_id,source_id) REFERENCES import_sources(tenant_id,id),
 UNIQUE(tenant_id,source_id,domain,source_column,mapping_version)
);
CREATE TABLE entity_crosswalks (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 source_id uuid NOT NULL, entity_type text NOT NULL, external_key text NOT NULL, canonical_id uuid NOT NULL,
 FOREIGN KEY(tenant_id,source_id) REFERENCES import_sources(tenant_id,id),
 UNIQUE(tenant_id,source_id,entity_type,external_key)
);
CREATE TABLE canonical_facts (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 entity_type text NOT NULL, entity_id uuid NOT NULL, attribute text NOT NULL,
 period_id uuid, value jsonb NOT NULL, source_row_id uuid,
 state text NOT NULL DEFAULT 'draft' CHECK(state IN ('draft','validated','disputed','superseded')),
 supersedes_id uuid, recorded_at timestamptz NOT NULL DEFAULT now(),
 FOREIGN KEY(tenant_id,period_id) REFERENCES periods(tenant_id,id),
 FOREIGN KEY(tenant_id,source_row_id) REFERENCES import_rows(tenant_id,id),
 UNIQUE(tenant_id,id)
);
CREATE TABLE metric_runs (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 metric_id uuid NOT NULL REFERENCES metrics(id), period_id uuid NOT NULL,
 rule_hash text NOT NULL, input_hash text NOT NULL, state text NOT NULL CHECK(state IN ('draft','validated','rejected','approved')),
 trace jsonb NOT NULL DEFAULT '{}'::jsonb, calculated_at timestamptz NOT NULL DEFAULT now(),
 FOREIGN KEY(tenant_id,period_id) REFERENCES periods(tenant_id,id), UNIQUE(tenant_id,id)
);
CREATE TABLE metric_values (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 run_id uuid NOT NULL, field_id uuid REFERENCES metric_fields(id), value jsonb NOT NULL,
 FOREIGN KEY(tenant_id,run_id) REFERENCES metric_runs(tenant_id,id), UNIQUE(tenant_id,id)
);
CREATE TABLE evidence_assets (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 storage_key text NOT NULL, sha256 text NOT NULL, mime_type text NOT NULL,
 classification text NOT NULL CHECK(classification IN ('public','internal','confidential','restricted')),
 version integer NOT NULL DEFAULT 1, created_at timestamptz NOT NULL DEFAULT now(),
 UNIQUE(tenant_id,id), UNIQUE(tenant_id,storage_key)
);
CREATE TABLE evidence_links (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 asset_id uuid NOT NULL, metric_value_id uuid NOT NULL, claim text,
 FOREIGN KEY(tenant_id,asset_id) REFERENCES evidence_assets(tenant_id,id),
 FOREIGN KEY(tenant_id,metric_value_id) REFERENCES metric_values(tenant_id,id)
);
CREATE TABLE reviews (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 metric_run_id uuid NOT NULL, reviewer_id uuid NOT NULL REFERENCES users(id),
 decision text NOT NULL CHECK(decision IN ('approve','reject','request_changes')),
 note text, reviewed_at timestamptz NOT NULL DEFAULT now(),
 FOREIGN KEY(tenant_id,metric_run_id) REFERENCES metric_runs(tenant_id,id)
);
CREATE TABLE snapshots (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 edition_id uuid NOT NULL REFERENCES framework_editions(id), period_id uuid NOT NULL,
 manifest_hash text NOT NULL, payload jsonb NOT NULL, approved_by uuid REFERENCES users(id),
 frozen_at timestamptz NOT NULL DEFAULT now(),
 FOREIGN KEY(tenant_id,period_id) REFERENCES periods(tenant_id,id), UNIQUE(tenant_id,id)
);
CREATE TABLE audit_events (
 id uuid PRIMARY KEY DEFAULT gen_random_uuid(), tenant_id uuid NOT NULL REFERENCES tenants(id),
 actor_id uuid REFERENCES users(id), action text NOT NULL, object_type text NOT NULL,
 object_id uuid, event_at timestamptz NOT NULL DEFAULT now(), details jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX idx_facts_tenant_entity_period ON canonical_facts(tenant_id,entity_type,entity_id,period_id);
CREATE INDEX idx_runs_tenant_period ON metric_runs(tenant_id,period_id);
CREATE INDEX idx_evidence_tenant_hash ON evidence_assets(tenant_id,sha256);
CREATE INDEX idx_audit_tenant_time ON audit_events(tenant_id,event_at DESC);
CREATE INDEX idx_rows_tenant_batch ON import_rows(tenant_id,batch_id);

-- Baseline RLS: production must add role-specific write policies and a secure
-- authenticated transaction-scoped tenant context; never let a client set tenant_id.
DO $$
DECLARE t text;
BEGIN
 FOREACH t IN ARRAY ARRAY['units','memberships','licenses','framework_assignments','periods','import_sources','import_batches','import_rows','source_mappings','entity_crosswalks','canonical_facts','metric_runs','metric_values','evidence_assets','evidence_links','reviews','snapshots','audit_events']
 LOOP
  EXECUTE format('ALTER TABLE qualityhub.%I ENABLE ROW LEVEL SECURITY',t);
  EXECUTE format('ALTER TABLE qualityhub.%I FORCE ROW LEVEL SECURITY',t);
  EXECUTE format('CREATE POLICY tenant_read ON qualityhub.%I FOR SELECT USING (tenant_id = nullif(current_setting(''qualityhub.tenant_id'',true),'''')::uuid)',t);
 END LOOP;
END $$;
-- NOTE: no INSERT/UPDATE/DELETE policies are provided; deny-by-default until
-- trusted service authorization and immutable audit triggers are implemented.
-- Additional composite foreign keys and unit tenant integrity require review
-- before this DDL can be used in production.
