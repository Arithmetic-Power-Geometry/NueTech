-- QualityHub Phase 3: additive hardening migration against 02_POSTGRES_SCHEMA.sql
-- PostgreSQL 15+; NOT executed in this environment. Apply only to an empty
-- development database, then run real integration tests. NOT production-ready.
BEGIN;
SET search_path TO qualityhub,public;

-- Tenant-scoped structural references.
ALTER TABLE units DROP CONSTRAINT IF EXISTS units_parent_id_fkey;
ALTER TABLE units ADD CONSTRAINT units_parent_tenant_fk
  FOREIGN KEY (tenant_id,parent_id) REFERENCES units(tenant_id,id);
ALTER TABLE framework_assignments ADD CONSTRAINT assignment_scope_tenant_fk
  FOREIGN KEY (tenant_id,scope_unit_id) REFERENCES units(tenant_id,id);
ALTER TABLE canonical_facts ADD CONSTRAINT facts_supersedes_tenant_fk
  FOREIGN KEY (tenant_id,supersedes_id) REFERENCES canonical_facts(tenant_id,id);
CREATE UNIQUE INDEX IF NOT EXISTS uq_assignment_root
  ON framework_assignments(tenant_id,edition_id) WHERE scope_unit_id IS NULL;

-- Schema-level product and framework type restrictions, not a substitute
-- for actual institution eligibility under the official rulebook.
CREATE OR REPLACE FUNCTION enforce_qualityhub_product_type() RETURNS trigger
LANGUAGE plpgsql SET search_path=qualityhub,pg_temp AS $$
DECLARE actual_type text;
BEGIN
 SELECT institution_type INTO actual_type FROM tenants WHERE id=NEW.tenant_id;
 IF actual_type IS NULL OR NEW.product_code IS DISTINCT FROM actual_type THEN
   RAISE EXCEPTION 'Product type incompatible with institution';
 END IF;
 RETURN NEW;
END $$;
CREATE TRIGGER licenses_type_guard BEFORE INSERT OR UPDATE OF tenant_id,product_code
 ON licenses FOR EACH ROW EXECUTE FUNCTION enforce_qualityhub_product_type();

CREATE OR REPLACE FUNCTION enforce_qualityhub_framework_type() RETURNS trigger
LANGUAGE plpgsql SET search_path=qualityhub,pg_temp AS $$
DECLARE actual_type text; edition_type text; edition_status text;
BEGIN
 SELECT institution_type INTO actual_type FROM tenants WHERE id=NEW.tenant_id;
 SELECT institution_type,status INTO edition_type,edition_status
   FROM framework_editions WHERE id=NEW.edition_id;
 IF actual_type IS NULL OR edition_type IS DISTINCT FROM actual_type THEN
   RAISE EXCEPTION 'Framework incompatible with institution';
 END IF;
 IF NEW.status='verified' AND edition_status <> 'verified_active' THEN
   RAISE EXCEPTION 'Cannot verify assignment to non-active framework edition';
 END IF;
 RETURN NEW;
END $$;
CREATE TRIGGER framework_type_guard BEFORE INSERT OR UPDATE
 ON framework_assignments FOR EACH ROW EXECUTE FUNCTION enforce_qualityhub_framework_type();

-- Ensure value field belongs to the metric that was actually calculated.
CREATE OR REPLACE FUNCTION enforce_qualityhub_metric_field() RETURNS trigger
LANGUAGE plpgsql SET search_path=qualityhub,pg_temp AS $$
DECLARE run_metric uuid; field_metric uuid;
BEGIN
 IF NEW.field_id IS NULL THEN RETURN NEW; END IF;
 SELECT metric_id INTO run_metric FROM metric_runs
   WHERE tenant_id=NEW.tenant_id AND id=NEW.run_id;
 SELECT metric_id INTO field_metric FROM metric_fields WHERE id=NEW.field_id;
 IF run_metric IS NULL OR field_metric IS DISTINCT FROM run_metric THEN
   RAISE EXCEPTION 'Metric field does not belong to calculation';
 END IF;
 RETURN NEW;
END $$;
CREATE TRIGGER metric_field_guard BEFORE INSERT OR UPDATE
 ON metric_values FOR EACH ROW EXECUTE FUNCTION enforce_qualityhub_metric_field();

-- Disallow edits to frozen snapshots. Append a new snapshot instead.
CREATE OR REPLACE FUNCTION deny_qualityhub_snapshot_mutation() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
 RAISE EXCEPTION 'Frozen snapshot is immutable';
END $$;
CREATE TRIGGER snapshot_immutable BEFORE UPDATE OR DELETE ON snapshots
 FOR EACH ROW EXECUTE FUNCTION deny_qualityhub_snapshot_mutation();

-- Audit records are append-only. Do not grant untrusted actors direct insert.
CREATE OR REPLACE FUNCTION deny_qualityhub_audit_mutation() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
 RAISE EXCEPTION 'Audit history is append-only';
END $$;
CREATE TRIGGER audit_immutable BEFORE UPDATE OR DELETE ON audit_events
 FOR EACH ROW EXECUTE FUNCTION deny_qualityhub_audit_mutation();

-- Additional source integrity constraints.
ALTER TABLE import_rows ADD CONSTRAINT import_rows_source_key_nonempty CHECK(length(trim(source_key))>0);
ALTER TABLE import_batches ADD CONSTRAINT import_batches_sha256_format
 CHECK(content_sha256 ~ '^[0-9a-f]{64}$');
ALTER TABLE evidence_assets ADD CONSTRAINT evidence_sha256_format
 CHECK(sha256 ~ '^[0-9a-f]{64}$');

COMMIT;

-- Remaining blockers: secure authentication and database GRANT model,
-- RLS write policies, full entity/metric-to-edition applicability,
-- tenant-isolated evidence object storage, approved metric run immutability,
-- real CMS exports, official template coverage, and PostgreSQL execution tests.
