# NueTech QualityHub

**Design and Developed by Dr. Mohammad Amir Khusru Akhtar**

A public **synthetic-data demonstration** of an optional, read-only quality-assurance add-on to an existing educational management system. This repository does not contain the vendor's core CMS, institutional records, passwords, production connectors, or regulatory submissions.

## Independently licensed product configurations

| Product | Illustrative regulatory workspaces |
| --- | --- |
| University | NAAC, applicable NIRF categories, IQAC and AQAR |
| College | Applicable NAAC, NIRF, IQAC and AQAR |
| School | CBSE SARAS, SQAAF, OASIS, UDISE+ and public disclosure preparation |

Selections represent **workspace design**, not proof of accreditation eligibility or compatibility with the current version of an official submission portal.

## Streamlit demo

Entry point: `prototype/qualityhub_app.py`

Run locally:

```bash
python -m pip install -r prototype/requirements.txt
python -m streamlit run prototype/qualityhub_app.py
```

Streamlit Community Cloud: select GitHub repo `Arithmetic-Power-Geometry/NueTech`, branch `main`, main-file path `prototype/qualityhub_app.py`, Python 3.12. Cloud deployment must be initiated by the authorized Streamlit account holder.

## What the demo illustrates

- Three selectable product packs and the assumed CMS-to-QualityHub relationship diagram.
- Plan-based module availability with **unverified**, brochure-derived mappings.
- Read-only preview of **synthetic or redacted** CSV headers and rows (2 MB limit; no import or persistence).
- JSON mapping export, integration-document download and printable developer blueprint.
- Evidence-readiness illustration with no official score or accreditation claim.

## Public handover documents

- [Integration manual](manual/06_COMPLETE_INTEGRATION_MANUAL.md)
- [CMS field dictionary](manual/06_MODULE_FIELD_DICTIONARY.csv)
- [Proposed PostgreSQL schema](architecture/02_POSTGRES_SCHEMA.sql)
- [Proposed hardening migration](architecture/03_HARDENING_MIGRATION.sql)

These are **proposed designs**. The existing CMS vendor must verify field names, API or export capabilities, permission boundaries and subscription entitlements. Regulatory editions, formulae and reporting templates must be verified against current official sources before any operational use.

## Security and release boundary

**Demonstration only.** Do not upload real student, employee, financial, personally identifiable or confidential institutional data. There is no production authentication, database tenant isolation, encrypted evidence repository, official regulator API connection, or regulator-endorsed submission output. The application does not modify the source CMS.

This release is appropriate for architectural review and sales discussions using synthetic examples, not live institutional onboarding.
