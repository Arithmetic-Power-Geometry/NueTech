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
    """Print-ready product and integration overview for commercial discussions."""
    sections=[
      ("Product Overview",f"{NAME} — {product}. Quality-assurance workspaces: {PACKS[product]['frameworks']}."),
      ("Product Modules","\n".join("• "+m for m in PACKS[product]["modules"])),
      ("CMS Integration Matrix","\n".join(f"• {source} → {destination}; additional information: {extra}" for source,destination,extra in SOURCES)),
      ("Integration Approach","\n".join(f"{title}: {description}" for title,description in STEPS[:5])),
      ("Data and Reporting Flow","Existing CMS → Authorized read-only transfer → Field mapping and validation → QualityHub reporting workspace → Evidence review → Report export."),
      ("Implementation Scope","The integration matrix presents the proposed configuration. Actual CMS columns, access permissions, and applicable regulatory editions are confirmed during implementation.")
    ]
    body="".join(f"<section><h2>{html.escape(title)}</h2><p>{html.escape(value).replace(chr(10),'<br>')}</p></section>" for title,value in sections)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{NAME} — {product} Product Overview</title>
<style>body{{font-family:Arial,sans-serif;color:#15253b;max-width:850px;margin:35px auto;line-height:1.5}}h1{{color:#0c4265}}h2{{border-bottom:1px solid #cad6df;padding-bottom:5px;margin-top:25px}}section{{break-inside:avoid}}p{{white-space:normal}}.small{{color:#536576}}@media print{{body{{margin:12mm}}section{{break-inside:auto}}}}</style></head><body>
<h1>{NAME}</h1><p><strong>{html.escape(CREDIT)}</strong></p><p class="small">{html.escape(product)} | Product and Integration Overview | {date.today().isoformat()}</p>
{body}<footer><hr><p class="small">{NAME} · {html.escape(CREDIT)}</p></footer></body></html>"""

st.set_page_config(page_title=NAME,layout="wide")
st.title(NAME)
st.caption(CREDIT)
st.caption("University • College • School | Quality assurance, institutional reporting and evidence management")

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

st.subheader("Connected Quality Management")
st.caption("A unified view of institutional information and quality-assurance workflows.")
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
st.caption("Integration pathways are configurable to match each institution’s available CMS modules.")

product=st.selectbox("Select separately licensed product",list(PACKS))
st.subheader(product+" product")
st.write("**Reporting frameworks:** "+PACKS[product]["frameworks"])
st.write("**Components included:**")
for item in PACKS[product]["modules"]: st.write("• "+item)
tab1,tab2,tab3,tab4=st.tabs(["CMS Mapping","Integration Architecture","Included Modules","Print / Export"])
with tab1:
 st.table([{"Advertised CMS component":a,"QualityHub import":b,"QualityHub additions":c} for a,b,c in SOURCES])
 st.caption("Field mapping is configurable for each CMS installation.")
with tab2:
 st.code("Existing CMS (read-only) → Import adapter → Validation & provenance → Isolated PostgreSQL → Edition-specific metrics → Evidence & approvals → Frozen report",language="text")
 for a,b in STEPS:
  with st.expander(a): st.write(b)
with tab3:
 for item in PACKS[product]["modules"]:
  st.write("✓ "+item)
 st.caption("Module configuration and availability depend on the institution’s selected package.")
with tab4:
 st.write("Download the integration guide and print it or save it as PDF.")
 st.download_button("Download printable product overview (HTML)",printable(product),file_name=f"NueTech_QualityHub_{product}_Integration_Blueprint.html",mime="text/html")
 
st.divider()
st.subheader("Product Resources")
st.write("Download the product integration overview and module field dictionary.")
base="https://github.com/Arithmetic-Power-Geometry/NueTech/blob/main/"
for title,relative in [
    ("Full module-by-module integration manual","manual/06_COMPLETE_INTEGRATION_MANUAL.md"),
    ("Module field dictionary (CSV)","manual/06_MODULE_FIELD_DICTIONARY.csv"),
]:
    st.markdown(f"- [{title}]({base}{relative})")


st.markdown("**Downloads**")
project_root=Path(__file__).resolve().parent.parent
for title,relative in [
    ("Integration manual (Markdown)","manual/06_COMPLETE_INTEGRATION_MANUAL.md"),
    ("All three products: field dictionary (CSV)","manual/06_MODULE_FIELD_DICTIONARY.csv"),
]:
    candidate=(project_root/relative).resolve()
    if candidate.is_relative_to(project_root) and candidate.is_file():
        st.download_button("Download "+title,candidate.read_bytes(),file_name=candidate.name,mime="text/plain",key="download_"+candidate.name)
    else:
        st.caption(title+": file not present in this deployment; use the public repository link above.")

st.divider()
st.subheader("CMS Module Integration")
st.caption("Explore modules, field mapping and reporting destinations for the selected product.")
from assumed_cms import build_demo
assumed=build_demo(product,st.selectbox("Existing CMS subscription for assumed mapping",["Starter","Basic","Pro","Premium","Enterprise"],index=4,key="assumed_plan"))
st.write("**Sample institution:** "+assumed["synthetic_institution"]["name"])
st.write("**Reporting workspaces:** "+", ".join(assumed["frameworks"]))
st.dataframe(assumed["mapping"],width="stretch",hide_index=True)
import json as _json
st.download_button("Download module mapping (JSON)",_json.dumps(assumed,indent=2),file_name="qualityhub_"+product.lower()+"_assumed_mapping.json",mime="application/json")
st.caption("Modules outside the selected CMS plan can be supplied through authorized import or manual entry.")
st.divider()
st.subheader("Data Import & Field Mapping")
st.caption("Preview field matching and validation using sample CSV files. This screen does not save uploaded records.")
from csv_preview import inspect_csv
from demo_fields import FIELDS
domain=st.selectbox("Data domain",list(FIELDS),key="preview_domain")
uploaded=st.file_uploader("Sample CSV (maximum 2 MB)",type=["csv"],key="cms_preview")
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
st.subheader("Evidence Readiness")
st.caption("Review sample evidence checkpoints for the selected reporting workspace.")
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
st.caption(CREDIT+" · NueTech QualityHub · Sample-data demonstration")
