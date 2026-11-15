# NueTech QualityHub — Integration Manual and Field Dictionary
**Design and Developed by Dr. Mohammad Amir Khusru Akhtar**
Version: 2026-11-15 — architecture specification, **not verified production integration**.

## What the supplied NueTech materials establish
The 2026 module plan advertises Institute Setup, Admission Management, Student Information System, Fees Management, Examinations & Marksheet Management, Document Management and Course Management from Starter; Employee Management, Program Management, Library, Timetable and Attendance from Pro; Placement, File, Committee and Task Management from Premium; accounting-package integration, Payroll and Scholarship from Enterprise. The brochure describes a Comprehensive Management System for universities, colleges and schools. **Neither document supplies actual database names, field types, APIs or export guarantees.**

## Commercial and technical boundaries
Three separately licensable products share a QualityHub engine. Each institution is a tenant. The source CMS stays unchanged; read-only API / read-only DB view / authorized CSV-XLSX / manual entry. A QualityHub tenant must be bound to its licensed product and applicable regulatory edition. All suggested fields below are **proposed canonical mapping names**, not confirmed CMS columns or official submission field dictionaries.

## Database architecture
- Core: `tenants`, `units`, `users`, `memberships`, `products`, `licenses`.
- Regulatory: `framework_editions`, `framework_assignments`, `periods`, `metrics`, `metric_fields`.
- Ingestion: `import_sources`, `import_batches`, `import_rows`, `source_mappings`, `entity_crosswalks`, `canonical_facts`.
- Evidence and workflow: `evidence_assets`, `evidence_links`, `metric_runs`, `metric_values`, `reviews`, `snapshots`, `audit_events`.
- These are draft PostgreSQL tables; migrations and RLS are not production validated. Refer to `architecture/02_POSTGRES_SCHEMA.sql` and `architecture/03_HARDENING_MIGRATION.sql`.
- Future typed tables after CMS export confirmation: institution, campus, programme, enrolment, staff appointment, examination result, placement, research output, finance transaction, school facility and school disclosure.

## Module-by-module field dictionary
The machine-readable companion is `06_MODULE_FIELD_DICTIONARY.csv` and has **27 proposed module-domain mappings**. Each record specifies product, domain, existing CMS module, proposed source fields, additional QualityHub fields, target workspaces and advertised minimum plan. The minimum-plan label may include a combination of modules from different plans; actual exports must be checked.

### 1. University — Institution
**Existing CMS:** Institute Setup (advertised Starter).
**Candidate import fields:** `institution_id; name; campus_id; address; ownership; established_year`.
**Additional QualityHub fields:** `AISHE_code; NAAC_cycle; recognition_order; regulator_category`.
**Potential reporting workspaces:** NAAC;NIRF;IQAC;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 2. University — Admissions and cohorts
**Existing CMS:** Admission Management;Student Information System (advertised Starter).
**Candidate import fields:** `student_id; programme_id; admission_date; academic_year; enrolment_status`.
**Additional QualityHub fields:** `cohort_eligibility; category_validation; exclusion_reason; source_snapshot`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 3. University — Programme and intake
**Existing CMS:** Course Management;Program Management (advertised Pro).
**Candidate import fields:** `programme_id; level; duration; approved_intake; department_id`.
**Additional QualityHub fields:** `approval_document; discipline_mapping; programme_period`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 4. University — Faculty
**Existing CMS:** Employee Management (advertised Pro).
**Candidate import fields:** `employee_id; appointment_date; designation; qualification; department_id; employment_status`.
**Additional QualityHub fields:** `fte_basis; faculty_eligibility; researcher_id; verification_document`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 5. University — Examinations and graduation
**Existing CMS:** Examinations & Marksheet Management (advertised Starter).
**Candidate import fields:** `student_id; programme_id; exam_year; result; award_date`.
**Additional QualityHub fields:** `graduation_cohort; late_result_flag; eligibility_reason`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 6. University — Placement and progression
**Existing CMS:** Placement Management (advertised Premium).
**Candidate import fields:** `student_id; employer; offer_date; joining_date; salary`.
**Additional QualityHub fields:** `verified_unique_outcome; higher_studies_proof; cohort_link`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 7. University — Research
**Existing CMS:** Document Management;Employee Management (advertised Starter/Pro).
**Candidate import fields:** `employee_id; publication_reference; document_uri`.
**Additional QualityHub fields:** `doi; indexing_proof; grant_order; patent_status; research_period`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 8. University — Finance
**Existing CMS:** Integration with Accounting Package;Payroll Management (advertised Enterprise).
**Candidate import fields:** `ledger_code; amount; date; cost_centre; payroll_category`.
**Additional QualityHub fields:** `audited_mapping; eligible_expense; financial_year; reconciliation`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 9. University — IQAC and governance
**Existing CMS:** Committee Management;Task Management (advertised Premium).
**Candidate import fields:** `committee_id; meeting_date; minutes_uri; action_owner; due_date`.
**Additional QualityHub fields:** `iqac_resolution; action_taken_evidence; aq ar_cycle`.
**Potential reporting workspaces:** IQAC;AQAR;NAAC. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 10. University — Evidence and submission
**Existing CMS:** Document Management;File Management (advertised Starter/Premium).
**Candidate import fields:** `document_id; file_name; category; uploaded_at`.
**Additional QualityHub fields:** `sha256; storage_key; claim_id; reviewer; edition; freeze_hash`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 11. College — Institution and affiliation
**Existing CMS:** Institute Setup (advertised Starter).
**Candidate import fields:** `institution_id; name; address; affiliating_university; status`.
**Additional QualityHub fields:** `autonomy_order; affiliation_validity; college_category; AISHE_code`.
**Potential reporting workspaces:** NAAC;NIRF;IQAC. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 12. College — Students and enrolment
**Existing CMS:** Admission Management;Student Information System (advertised Starter).
**Candidate import fields:** `student_id; programme_id; admission_year; status`.
**Additional QualityHub fields:** `eligible_cohort; category_proof; period; exclusion_reason`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 13. College — Programmes
**Existing CMS:** Course Management;Program Management (advertised Pro).
**Candidate import fields:** `programme_id; programme_name; duration; intake`.
**Additional QualityHub fields:** `affiliation_approval; autonomous_curriculum_flag; discipline`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 14. College — Faculty and teaching
**Existing CMS:** Employee Management;Timetable Management (advertised Pro).
**Candidate import fields:** `employee_id; qualification; designation; workload; department_id`.
**Additional QualityHub fields:** `fte_basis; appointment_proof; eligibility`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 15. College — Assessment and results
**Existing CMS:** Examinations & Marksheet Management (advertised Starter).
**Candidate import fields:** `student_id; programme_id; exam_date; result; award_date`.
**Additional QualityHub fields:** `university_exam_source; cohort_definition; result_verification`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 16. College — Progression
**Existing CMS:** Placement Management (advertised Premium).
**Candidate import fields:** `student_id; employer; salary; joining_date`.
**Additional QualityHub fields:** `higher_study_confirmation; duplicate_outcome_check; cohort_link`.
**Potential reporting workspaces:** NAAC;NIRF;AQAR. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 17. College — IQAC, outreach and evidence
**Existing CMS:** Committee Management;Task Management;Document Management (advertised Premium).
**Candidate import fields:** `meeting_id; minutes_uri; event_id; document_id`.
**Additional QualityHub fields:** `iqac_action_log; outreach_proof; metric_claim; approval`.
**Potential reporting workspaces:** IQAC;AQAR;NAAC. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 18. College — Finance and resources
**Existing CMS:** Integration with Accounting Package;Library Management (advertised Enterprise).
**Candidate import fields:** `ledger_code; amount; subscription_id; period`.
**Additional QualityHub fields:** `audited_category; resource_evidence; exclusion_reason`.
**Potential reporting workspaces:** NAAC;NIRF. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 19. School — Identity and affiliation
**Existing CMS:** Institute Setup (advertised Starter).
**Candidate import fields:** `school_id; name; address; board; principal`.
**Additional QualityHub fields:** `affiliation_number; validity; school_code; UDISE_code; SARAS_cycle`.
**Potential reporting workspaces:** CBSE SARAS;OASIS;UDISE+. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 20. School — Admissions and enrolment
**Existing CMS:** Admission Management;Student Information System (advertised Starter).
**Candidate import fields:** `student_id; class; section; gender; admission_date; status`.
**Additional QualityHub fields:** `udise_reporting_category; age_validation; reporting_year; privacy_basis`.
**Potential reporting workspaces:** UDISE+;OASIS;SQAAF. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 21. School — Teachers and staff
**Existing CMS:** Employee Management (advertised Pro).
**Candidate import fields:** `employee_id; designation; qualification; appointment_date; status`.
**Additional QualityHub fields:** `trained_status; teacher_category; compliance_documents`.
**Potential reporting workspaces:** OASIS;UDISE+;SQAAF. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 22. School — Classes, curriculum and learning
**Existing CMS:** Course Management;Program Management;Assignment Management (advertised Pro).
**Candidate import fields:** `class; subject; teacher_id; course_code`.
**Additional QualityHub fields:** `curriculum_evidence; self_assessment_indicator; improvement_action`.
**Potential reporting workspaces:** SQAAF;UDISE+. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 23. School — Attendance and results
**Existing CMS:** Attendance Management;Examinations & Marksheet Management (advertised Pro).
**Candidate import fields:** `student_id; date; attendance_status; assessment_result`.
**Additional QualityHub fields:** `aggregate_window; validated_reporting_population; quality_indicator`.
**Potential reporting workspaces:** SQAAF;UDISE+. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 24. School — Infrastructure and safety
**Existing CMS:** Institute Setup;Document Management;Transport Management (advertised Starter/Premium).
**Candidate import fields:** `building_id; facility_type; document_id; transport_route`.
**Additional QualityHub fields:** `fire_certificate; building_safety; water_sanitation; accessibility; valid_until`.
**Potential reporting workspaces:** CBSE SARAS;SQAAF;UDISE+. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 25. School — Disclosure and affiliation documents
**Existing CMS:** Document Management;File Management (advertised Starter/Premium).
**Candidate import fields:** `document_id; document_type; file_uri; uploaded_at`.
**Additional QualityHub fields:** `public_disclosure_field; publication_url; approval_status; sha256`.
**Potential reporting workspaces:** CBSE SARAS;OASIS. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 26. School — School governance and improvement
**Existing CMS:** Committee Management;Task Management;Grievance Management (advertised Premium).
**Candidate import fields:** `committee_id; meeting_date; action_id; grievance_id`.
**Additional QualityHub fields:** `sqaaf_self_review; improvement_plan; closure_proof`.
**Potential reporting workspaces:** SQAAF;OASIS. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

### 27. School — Financial and fee disclosures
**Existing CMS:** Fees Management;Integration with Accounting Package (advertised Starter/Enterprise).
**Candidate import fields:** `fee_head; fee_amount; period; ledger_code`.
**Additional QualityHub fields:** `board_required_disclosure; audited_reconciliation`.
**Potential reporting workspaces:** CBSE SARAS;OASIS. **Verification:** obtain source header/type and stable key, verify official metric/edition eligibility and attach dated evidence before calculation.

## Integration implementation contract
1. Gautam supplies actual stack, authorized read-only integration mechanism, per-plan export availability, **synthetic/redacted** column headers and stable keys.
2. Register tenant, institutional category, academic/financial period, purchased pack and official edition.
3. Configure connector with scoped read-only credentials in secrets manager; never store credentials in GitHub or reports.
4. Record exact source-to-canonical mapping, type, unit, null policy, transformation version and source column provenance.
5. Stage each import; hash file/rows; reject malformed, cross-tenant and duplicate identifiers; flag conflicting updates.
6. Map only to verified metric definitions for the correct regulator/category/edition; do not invent scores.
7. Upload evidence to encrypted private object storage; store hash and claim linkage; route for reviewer approval.
8. Freeze approved report and export evidence index, discrepancy report and worksheets. Never assert automatic portal submission without regulator-authorized API.
9. Log each import, validation, review and export; enforce tenant isolation and retention.
10. Run integration tests with synthetic university, college and school tenants before any live use.

## Required official verification
- University/College: operative NAAC manual and edition; NAAC/AQAR field definitions; each NIRF year/category DCS schema, eligibility and formula.
- School: CBSE SARAS, OASIS, SQAAF, mandatory public disclosure and current UDISE+ DCF; applicability differs by board and year.
- Official portal export formats and permission to submit are **not confirmed**.
- This manual is a development mapping, **not an official regulator manual**.

## Acceptance criteria
- Tenant isolation; licence enforcement; read-only CMS integration; versioned source mapping; deterministic import and conflict review; date- and edition-specific calculation; secure evidence; reviewer approval; immutable exports; accessible front page; printable full integration manual; backup/recovery; security testing.
- No complete production implementation or live CMS integration is claimed.

## Supporting source locations
- User-provided *Modules For School & Colleges* (2026), module matrix page 1.
- User-provided *New Brochure 2026*, CMS module descriptions pages 1–3.
- Official verification references retained in `research/01_OFFICIAL_EVIDENCE.md` and `architecture/02_DESIGN_AND_IMPORT_MAPPING.md`.
