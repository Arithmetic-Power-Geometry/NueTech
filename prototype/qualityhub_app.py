"""NueTech QualityHub — synthetic public demonstration and integration blueprint."""
import html
from datetime import date
from pathlib import Path
import streamlit as st

NAME="NueTech QualityHub"
CREDIT="Design and Developed by Dr. Mohammad Amir Khusru Akhtar"
PACKS={
 "University":{"modules":["Institution Profile","NAAC Preparation","NIRF Category Workspace","IQAC and AQAR","Research and Outcomes","Evidence and Review","Submission Readiness"],"frameworks":"NAAC / NIRF / IQAC / AQAR (applicable verified editions only)"},
 "College":{"modules":["College Profile","NAAC Preparation","NIRF Eligibility and Category","IQAC and AQAR","Programme and Faculty","Evidence and Review","Submission Readiness"],"frameworks":"NAAC / eligible NIRF categories / IQAC / AQAR"},
 "School":{"modules":["School Profile","CBSE SARAS","OASIS","SQAAF","Mandatory Public Disclosure","UDISE+","Evidence and Review"],"frameworks":"CBSE / UDISE+ (board and current edition must be verified)"}
}
SOURCES=[
 ("Institute Setup","Institution identity and campuses","Regulatory IDs, institution type, scope"),
 ("Admission / Student Information","Students, enrolments and cohorts","Verified cohort definitions and unique identifiers"),
 ("Course / Programme","Programmes, courses and approved intake","Approval documents and regulator classification"),
 ("Employee Management","Faculty and staff","Eligibility, full-time equivalent and appointment evidence"),
 ("Examination","Results, graduation and progression","Period alignment, exclusions and delayed results"),
 ("Placement","Graduate outcomes and employer records","Unique student outcome and higher education verification"),
 ("Accounting / Payroll","Audited expenditure and resources","Category mapping, reconciliation and audit"),
 ("Documents / File","Evidence inventory","Checksums, controlled storage and claim linkage"),
 ("Committees / Tasks","Governance meetings and action tracking","IQAC review and approval trail"),
 ("Library / Attendance","Learning resources and attendance","Edition-specific eligibility and reporting rules")
]
STEPS=[
 ("01. Select institution and licence","Register University, College or School tenant; activate only its purchased product; do not infer regulatory eligibility from a licence."),
 ("02. Confirm the regulatory edition","Choose regulator, category, year and source URL; mark unverified editions as draft and block final compliance claims."),
 ("03. Inventory CMS capabilities","Gautam confirms actual tables/API/export headers, stable IDs, supported plans, authentication and data owner permissions."),
 ("04. Connect without modifying CMS","Prefer authenticated read-only API; otherwise read-only database view, CSV/XLSX export or manual upload. Never write to the source CMS."),
 ("05. Map and validate","Preview source columns, mapping versions, reporting periods, duplicates, units, missing fields and conflicts; retain provenance."),
 ("06. Store in isolated QualityHub","Separate PostgreSQL tenant data, source batches, canonical facts and evidence metadata; keep documents in private encrypted object storage."),
 ("07. Calculate verified metrics","Use edition-specific documented formulas only; show inputs, exclusions, denominator, source records and calculation trace."),
 ("08. Review and approve","Department owner validates, IQAC/nodal reviewer approves, unresolved evidence gaps block readiness, and approved snapshots are immutable."),
 ("09. Export preparation package","Generate metric worksheets, evidence index, discrepancy list, approval history and submission-ready documents when the regulator's format is verified."),
 ("10. Maintain and synchronize","Schedule authorized read-only sync; changed facts create reviewable differences, never silently replace approved submissions.")
]
CHECKS=[
 "Obtain authorized sample export headers from every relevant CMS plan",
 "Identify stable institution, student, employee, programme and outcome keys",
 "Confirm PostgreSQL 15+ deployment, database role model and tenant RLS",
 "Validate all framework edition/source references and category eligibility",
 "Test duplicate imports, cross-tenant access and versioned evidence",
 "Implement encrypted evidence storage, retention and access logs",
 "Verify approval separation and immutable frozen exports",
 "Run integration tests using synthetic data before live data",
 "Conduct privacy, security and accessibility reviews",
 "Approve commercial packaging, branding and deployment boundaries"
]
def printable(product):
    sections=[
      ("Product and applicability",f"{NAME} — {product} Pack. {PACKS[product]['frameworks']}. Product entitlement does not establish regulatory eligibility."),
      ("Modules", "\n".join("• "+m for m in PACKS[product]["modules"])),
      ("Existing CMS mapping","\n".join(f"• {a} → {b}; addon: {c}" for a,b,c in SOURCES)),
      ("Integration sequence","\n".join(f"{a}: {b}" for a,b in STEPS)),
      ("Implementation acceptance checklist","\n".join("☐ "+x for x in CHECKS)),
      ("Delivery boundary","Synthetic public demonstration only. Actual CMS interfaces and current official templates require verification. No automatic portal submission, no certified accreditation/ranking claim, and no production deployment until tested.")
    ]
    body="".join(f"<section><h2>{html.escape(title)}</h2><p>{html.escape(value).replace(chr(10),'<br>')}</p></section>" for title,value in sections)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{NAME} — {product} Integration Blueprint</title>
<style>body{{font-family:Arial,sans-serif;color:#15253b;max-width:850px;margin:35px auto;line-height:1.5}}h1{{color:#0c4265}}h2{{border-bottom:1px solid #cad6df;padding-bottom:5px;margin-top:25px}}section{{break-inside:avoid}}p{{white-space:normal}}.small{{color:#536576}}@media print{{body{{margin:12mm}}section{{break-inside:auto}}}}</style></head><body>
<h1>{NAME}</h1><p><strong>{html.escape(CREDIT)}</strong></p><p class="small">Integration and implementation blueprint | {html.escape(product)} | Generated {date.today().isoformat()} | Proposed architecture, not a certification</p>
{body}<footer><hr><p class="small">{NAME} · {html.escape(CREDIT)}</p></footer></body></html>"""

st.set_page_config(page_title=NAME,layout="wide")
st.title(NAME)
st.caption(CREDIT)
st.info("Synthetic public architecture demonstration. No real CMS or regulatory portal connection. Do not upload personal, confidential or institutional data.")

# Front-page architecture: brochure-derived module availability, not verified API connections.
PLAN_LEVEL={"Institute Setup":"Starter","Admission Management":"Starter","Student Information System":"Starter","Examinations & Marksheet Management":"Starter","Document Management":"Starter","Course Management":"Starter","Employee Management":"Pro","Program Management":"Pro","Attendance Management":"Pro","Library Management":"Pro","Placement Management":"Premium","Committee Management":"Premium","File Management":"Premium","Integration with Accounting Package":"Enterprise"}
PLAN_ORDER={"Starter":0,"Basic":1,"Pro":2,"Premium":3,"Enterprise":4}
PRODUCT_TARGETS={
 "University":["NAAC","NIRF","IQAC","AQAR"],
 "College":["NAAC","NIRF (eligible)","IQAC","AQAR"],
 "School":["CBSE SARAS","SQAAF","OASIS","UDISE+"]
}
MODULE_RELATIONS={
 "Institute Setup":["NAAC","NIRF","IQAC","AQAR","CBSE SARAS","OASIS","UDISE+"],
 "Admission Management":["NAAC","NIRF","CBSE SARAS","UDISE+"],
 "Student Information System":["NAAC","NIRF","AQAR","OASIS","UDISE+"],
 "Examinations & Marksheet Management":["NAAC","NIRF","AQAR","SQAAF","UDISE+"],
 "Document Management":["NAAC","NIRF","IQAC","AQAR","CBSE SARAS","SQAAF","OASIS","UDISE+"],
 "Course Management":["NAAC","NIRF","AQAR","SQAAF","UDISE+"],
 "Employee Management":["NAAC","NIRF","AQAR","OASIS","SQAAF"],
 "Program Management":["NAAC","NIRF","AQAR","SQAAF"],
 "Attendance Management":["AQAR","SQAAF","UDISE+"],
 "Library Management":["NAAC","AQAR","SQAAF"],
 "Placement Management":["NAAC","NIRF","AQAR"],
 "Committee Management":["IQAC","AQAR","SQAAF"],
 "File Management":["NAAC","NIRF","AQAR","CBSE SARAS"],
 "Integration with Accounting Package":["NAAC","NIRF","AQAR","CBSE SARAS"]
}
def architecture_dot(product,plan):
    # Only illustrative mapping; never a claim of regulator-approved field correspondence.
    import json
    q=lambda value:json.dumps(value)
    targets=PRODUCT_TARGETS[product]
    relevant=[m for m,ts in MODULE_RELATIONS.items() if any(t in ts or (t=="NIRF (eligible)" and "NIRF" in ts) for t in targets)]
    available=[m for m in relevant if PLAN_ORDER[PLAN_LEVEL[m]]<=PLAN_ORDER[plan]]
    absent=[m for m in relevant if m not in available]
    lines=['digraph Q {','graph [rankdir=LR, bgcolor="transparent", pad="0.3", nodesep="0.24", ranksep="0.75", splines=polyline, fontname="Arial"];',
    'node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10, color="#C9D8E8", fontcolor="#102B46"];',
    'edge [color="#8AA4B7", arrowsize=0.6];',
    'subgraph cluster_cms { label="EXISTING NUETECH CMS (advertised modules)"; style="rounded"; color="#B9C9D8";']
    for i,m in enumerate(available):
        module_label=m+"\\n"+PLAN_LEVEL[m]+"+"
        lines.append(f'm{i} [label={q(module_label)}, fillcolor="#E5F2FB"];')
    lines.append('}')
    lines.append('adapter [label="READ-ONLY ADAPTER\\nAPI / DB view / CSV / XLSX", fillcolor="#FFF0D7", color="#E9B45E"];')
    lines.append('core [label="QUALITYHUB SIDECAR\\nMapping • validation • provenance\\nPostgreSQL • evidence • approvals", fillcolor="#DFF4EB", color="#55A486"];')
    lines.append('subgraph cluster_products { label="SEPARATELY LICENSED '+product.upper()+' PACK"; style="rounded"; color="#A5C4B8";')
    for i,t in enumerate(targets):lines.append(f't{i} [label={q(t)}, fillcolor="#E7F5EF"];')
    lines.append('}')
    for i in range(len(available)):lines.append(f'm{i} -> adapter;')
    lines.append('adapter -> core [label="no CMS writes"];')
    for i in range(len(targets)):lines.append(f'core -> t{i};')
    lines.append('}')
    return "\n".join(lines),absent

st.subheader("How existing NueTech CMS connects to three QualityHub products")
st.caption("Architecture illustration based on the supplied CMS plan sheet. Connections and field mappings are proposed, not verified live integrations.")
overview=st.columns(3)
for col,(kind,description) in zip(overview,[("University","NAAC · NIRF · IQAC · AQAR"),("College","Applicable NAAC · NIRF · IQAC · AQAR"),("School","CBSE SARAS · SQAAF · OASIS · UDISE+")]):
    with col:
        with st.container(border=True):
            st.markdown("#### "+kind)
            st.caption(description)
            st.write("Independently licensed")
st.markdown("**Existing CMS → read-only adapter → QualityHub sidecar → selected regulatory workspace**")
cms_plan=st.select_slider("Existing CMS plan (illustrative module availability)",options=list(PLAN_ORDER),value="Pro")
overview_product=st.radio("Graph view",list(PACKS),horizontal=True)
dot,missing=architecture_dot(overview_product,cms_plan)
st.graphviz_chart(dot,width="stretch")
if missing:
    st.warning("Not advertised in this CMS plan: "+", ".join(missing)+". QualityHub needs a separate authorized import or manual entry for those domains.")
st.caption("The graph shows module-level candidate relationships only. It does not assert current regulatory eligibility, completeness of fields, API availability or official template compliance.")

product=st.selectbox("Select separately licensed product",list(PACKS))
st.subheader(product+" product")
st.write("**Applicable frameworks:** "+PACKS[product]["frameworks"])
st.write("**Components included:**")
for item in PACKS[product]["modules"]: st.write("• "+item)
tab1,tab2,tab3,tab4=st.tabs(["CMS Mapping","Integration Architecture","Readiness Checklist","Final Print / Export"])
with tab1:
 st.table([{"Advertised CMS component":a,"QualityHub import":b,"QualityHub additions":c} for a,b,c in SOURCES])
 st.warning("CMS modules are brochure-advertised only. Export/API availability and actual field names have not been verified.")
with tab2:
 st.code("Existing CMS (read-only) → Import adapter → Validation & provenance → Isolated PostgreSQL → Edition-specific metrics → Evidence & approvals → Frozen report",language="text")
 for a,b in STEPS:
  with st.expander(a): st.write(b)
with tab3:
 for i,item in enumerate(CHECKS): st.checkbox(item,key=f"{product}-{i}")
 st.caption("Checklist selections are session-only and do not certify completion.")
with tab4:
 st.write("Download a complete, print-ready implementation blueprint. Open the HTML file in a browser and select Print / Save as PDF.")
 st.download_button("Download printable integration blueprint (HTML)",printable(product),file_name=f"NueTech_QualityHub_{product}_Integration_Blueprint.html",mime="text/html")
 st.markdown("**Required final report sections:** Product scope, framework applicability, CMS-to-addon mapping, ten-step integration sequence, implementation checklist and deployment boundaries.")
st.divider()
st.subheader("Download full integration manual, field dictionary and database schema")
st.write("Developer handover files: proposed CMS source fields, QualityHub-specific fields, University/College/School applicability, and PostgreSQL schema.")
base="https://github.com/Arithmetic-Power-Geometry/NueTech/blob/main/"
for title,relative in [
    ("Full module-by-module integration manual","manual/06_COMPLETE_INTEGRATION_MANUAL.md"),
    ("Module field dictionary (CSV)","manual/06_MODULE_FIELD_DICTIONARY.csv"),
    ("PostgreSQL base schema (SQL)","architecture/02_POSTGRES_SCHEMA.sql"),
    ("Database hardening migration (SQL)","architecture/03_HARDENING_MIGRATION.sql"),
]:
    st.markdown(f"- [{title}]({base}{relative})")
st.caption("Public demo reference files. These are proposed specifications, not verified CMS field exports or complete official regulator templates.")

st.markdown("**Direct file downloads (when running from a complete repository checkout)**")
project_root=Path(__file__).resolve().parent.parent
for title,relative in [
    ("Integration manual (Markdown)","manual/06_COMPLETE_INTEGRATION_MANUAL.md"),
    ("All three products: field dictionary (CSV)","manual/06_MODULE_FIELD_DICTIONARY.csv"),
    ("PostgreSQL schema (SQL)","architecture/02_POSTGRES_SCHEMA.sql"),
    ("PostgreSQL hardening (SQL)","architecture/03_HARDENING_MIGRATION.sql"),
]:
    candidate=(project_root/relative).resolve()
    if candidate.is_relative_to(project_root) and candidate.is_file():
        st.download_button("Download "+title,candidate.read_bytes(),file_name=candidate.name,mime="text/plain",key="download_"+candidate.name)
    else:
        st.caption(title+": file not present in this deployment; use the public repository link above.")

st.subheader("Delivery status — what remains")
st.table([
 {"Component":"University / College / School product selection","Status":"Prototype source implemented","Next requirement":"Entitlement enforcement and user acceptance tests"},
 {"Component":"CMS integration","Status":"Proposed field mappings","Next requirement":"Actual CMS API/export samples and read-only connector"},
 {"Component":"PostgreSQL database","Status":"Schema and migration drafted","Next requirement":"Execute tests; implement trusted RLS and access control"},
 {"Component":"Regulatory frameworks","Status":"Partial official-source research","Next requirement":"Verify all current edition-specific field templates and rules"},
 {"Component":"Evidence and review","Status":"Synthetic readiness checks","Next requirement":"Secure evidence storage, audit and real approval workflow"},
 {"Component":"Reports and print","Status":"Integration blueprint export implemented","Next requirement":"Official format exports and rendered output testing"},
 {"Component":"Security and deployment","Status":"Not production validated","Next requirement":"Authentication, backups, monitoring, penetration tests"}
])
st.warning("QualityHub is a development prototype. Do not use it as an official accreditation submission system until the listed gates are completed.")

st.divider()
st.subheader("Assumed full CMS integration — University, College and School")
st.caption("Based on the supplied 2026 NueTech module matrix. All field names and institutional records below are synthetic assumptions, not confirmed CMS columns.")
from assumed_cms import build_demo
assumed=build_demo(product,st.selectbox("Existing CMS subscription for assumed mapping",["Starter","Basic","Pro","Premium","Enterprise"],index=4,key="assumed_plan"))
st.write("**Synthetic institution:** "+assumed["synthetic_institution"]["name"])
st.write("**Potential reporting workspaces:** "+", ".join(assumed["frameworks"]))
st.dataframe(assumed["mapping"],width="stretch",hide_index=True)
import json as _json
st.download_button("Download assumed mapping JSON",_json.dumps(assumed,indent=2),file_name="qualityhub_"+product.lower()+"_assumed_mapping.json",mime="application/json")
st.warning("Unavailable CMS modules require a higher plan, authorized external import, or manual QualityHub input. The listed regulator mappings are indicative only.")
st.divider()
st.subheader("CMS CSV mapping preview — no database writes")
st.caption("Upload a synthetic or redacted UTF-8 CSV to inspect required columns, mapping and duplicate identifiers. No source CMS modification and no storage.")
from csv_preview import inspect_csv
from demo_fields import FIELDS
domain=st.selectbox("Data domain",list(FIELDS),key="preview_domain")
uploaded=st.file_uploader("CSV export (synthetic/redacted data only, maximum 2 MB)",type=["csv"],key="cms_preview")
if uploaded is not None:
    raw=uploaded.getvalue()
    if len(raw)>2_000_000:
        st.error("CSV exceeds 2 MB limit.")
    else:
        import csv as _csv
        import io as _io
        try:
            headers=next(_csv.reader(_io.StringIO(raw.decode("utf-8-sig"))))
            st.caption("Map each required canonical field to the corresponding CMS export column.")
            mapping={}
            for field in FIELDS[domain]:
                selected=st.selectbox(field,["(not mapped)"]+headers,index=(headers.index(field)+1 if field in headers else 0),key="map_"+domain+"_"+field)
                if selected!="(not mapped)":
                    mapping[selected]=field
            result=inspect_csv(raw,domain,mapping)
            st.json(result,expanded=False)
            if result["ready_to_stage"]:
                st.success("Structure passes preliminary checks; no data imported.")
            else:
                st.warning("Resolve missing fields or validation issues before import.")
        except (ValueError,UnicodeError,StopIteration) as exc:
            st.error("Invalid CSV: "+str(exc))
st.divider()
st.subheader("Evidence readiness — interactive demonstration")
st.caption("Synthetic sample requirements only. No official metric codes or regulatory scores are asserted.")
from readiness import Requirement, evaluate, PRODUCTS
sample=[]
for framework in PRODUCTS[product]:
    with st.expander(framework+" — sample evidence checkpoint"):
        status=st.selectbox("Evidence state",["missing","uploaded","verified","rejected"],key="evidence_"+product+framework)
        official=st.checkbox("Official template edition verified",key="official_"+product+framework)
        approved=st.checkbox("Reviewed and approved",key="approved_"+product+framework)
        sample.append(Requirement(code="DEMO_"+framework.replace(" ","_"),framework=framework,title="Illustrative checkpoint",evidence_status=status,template_verified=official,reviewer_approved=approved))
result=evaluate(product,sample)
c1,c2,c3=st.columns(3)
c1.metric("Checkpoints",result["requirements"])
c2.metric("Internally ready",result["ready"])
c3.metric("Outstanding",len(result["gaps"]))
st.write("**Internal status:** "+result["status"])
st.caption(result["disclaimer"])

st.divider()
st.caption(CREDIT+" · No source CMS modifications · Public synthetic demo only")
