"""NueTech QualityHub assumed CMS integration fixture.
Synthetic demonstration data only; no claim about actual CMS schema or official regulator forms.
Design and Developed by Dr. Mohammad Amir Khusru Akhtar.
"""
from dataclasses import dataclass
from typing import Tuple

PLAN_ORDER = ("Starter", "Basic", "Pro", "Premium", "Enterprise")
PRODUCT_FRAMEWORKS = {
    "University": ("NAAC", "NIRF", "IQAC", "AQAR"),
    "College": ("NAAC", "NIRF (if eligible)", "IQAC", "AQAR"),
    "School": ("CBSE SARAS", "SQAAF", "OASIS", "UDISE+"),
}
# Transcribed from the user-supplied NueTech 2026 CMS module plan.
CMS_MODULES = {
    "PC-UCMIS Framework":"Starter", "Institute Setup":"Starter",
    "Admission Management":"Starter", "Student Information System":"Starter",
    "Fees Management":"Starter", "Examinations & Marksheet Management":"Starter",
    "Document Management":"Starter", "Course Management":"Starter",
    "Institute Portal":"Basic", "Student Portal":"Basic",
    "Faculty Portal":"Basic", "Applicant Portal":"Basic",
    "Completion Certificate Management":"Pro", "Employee Management":"Pro",
    "User & Roles Management":"Pro", "Messaging engine for notifications, SMS and Email":"Pro",
    "ID Card Management (RFID/QR/BarCode)":"Pro", "Library Management":"Pro",
    "Program Management":"Pro", "Calendar Management":"Pro",
    "Enquiries Management":"Pro", "Timetable Management":"Pro",
    "Attendance Management":"Pro", "Assignment Management":"Pro",
    "Student Mobile Application":"Premium", "Faculty Mobile Application":"Premium",
    "File Management":"Premium", "Grievance Management":"Premium",
    "Placement Management":"Premium", "Disciplinary Management":"Premium",
    "Transport Management":"Premium", "Task Management":"Premium",
    "Hostel Management":"Premium", "Committee Management":"Premium",
    "Front Desk Management":"Premium", "Analytics Module":"Premium",
    "Integration with Accounting Package":"Enterprise", "Payroll Management":"Enterprise",
    "Scholarship Management":"Enterprise",
    "Security Gate Management (RFID/BarCode Enabled)":"Enterprise",
    "Campaign Management":"Enterprise", "Event Management":"Enterprise",
}
@dataclass(frozen=True)
class Mapping:
    domain: str
    source_module: str
    fields: Tuple[str, ...]
    targets: Tuple[str, ...]
    extra_fields: Tuple[str, ...] = ()

MAPPINGS = {
 "University": (
  Mapping("Institution","Institute Setup",("institution_id","name","aishe_code","campus_id"),("NAAC","NIRF","IQAC","AQAR"),("approval_document","reporting_period")),
  Mapping("Admissions","Admission Management",("student_id","program_code","admission_year","category"),("NAAC","NIRF","AQAR"),("cohort_eligibility","source_evidence")),
  Mapping("Students","Student Information System",("student_id","program_code","status","gender"),("NAAC","NIRF","AQAR"),("verified_reporting_population",)),
  Mapping("Programmes","Program Management",("program_code","level","approved_intake","duration"),("NAAC","NIRF"),("programme_approval",)),
  Mapping("Faculty","Employee Management",("employee_id","department","qualification","appointment_date"),("NAAC","NIRF","AQAR"),("fte_basis","appointment_proof")),
  Mapping("Examinations","Examinations & Marksheet Management",("student_id","program_code","result_year","result"),("NAAC","NIRF","AQAR"),("graduation_cohort",)),
  Mapping("Placements","Placement Management",("student_id","employer","joining_date","salary"),("NAAC","NIRF","AQAR"),("offer_evidence",)),
  Mapping("IQAC","Committee Management",("meeting_id","meeting_date","minutes_uri"),("IQAC","AQAR","NAAC"),("action_taken_report",)),
  Mapping("Finance","Integration with Accounting Package",("ledger_code","amount","financial_year"),("NAAC","NIRF","AQAR"),("audited_mapping",)),
  Mapping("Research","Document Management",("document_id","employee_id","publication_reference"),("NAAC","NIRF"),("doi","indexing_proof")),
 ),
 "College": (
  Mapping("Institution","Institute Setup",("institution_id","name","affiliating_university"),("NAAC","IQAC","AQAR"),("affiliation_order","autonomy_status")),
  Mapping("Students","Student Information System",("student_id","program_code","admission_year"),("NAAC","NIRF (if eligible)","AQAR"),("cohort_eligibility",)),
  Mapping("Programmes","Course Management",("course_code","programme_name","duration"),("NAAC","AQAR"),("affiliation_approval",)),
  Mapping("Faculty","Employee Management",("employee_id","department","qualification"),("NAAC","NIRF (if eligible)"),("appointment_proof",)),
  Mapping("Examinations","Examinations & Marksheet Management",("student_id","result_year","result"),("NAAC","AQAR"),("result_source",)),
  Mapping("Placements","Placement Management",("student_id","employer","joining_date"),("NAAC","NIRF (if eligible)"),("higher_study_proof",)),
  Mapping("IQAC","Committee Management",("meeting_id","meeting_date","minutes_uri"),("IQAC","AQAR"),("action_taken_report",)),
  Mapping("Finance","Integration with Accounting Package",("ledger_code","amount","financial_year"),("NAAC","NIRF (if eligible)"),("audited_mapping",)),
 ),
 "School": (
  Mapping("Identity","Institute Setup",("school_id","name","affiliation_number","udise_code"),("CBSE SARAS","OASIS","UDISE+"),("recognition_order",)),
  Mapping("Students","Student Information System",("student_id","class","section","admission_year"),("OASIS","UDISE+","SQAAF"),("reporting_population",)),
  Mapping("Teachers","Employee Management",("employee_id","designation","qualification"),("OASIS","UDISE+","SQAAF"),("teacher_eligibility_proof",)),
  Mapping("Curriculum","Course Management",("class","subject","course_code"),("SQAAF",),("self_assessment_evidence",)),
  Mapping("Attendance","Attendance Management",("student_id","date","attendance_status"),("SQAAF","UDISE+"),("aggregation_period",)),
  Mapping("Examinations","Examinations & Marksheet Management",("student_id","class","result"),("SQAAF",),("learning_outcome_evidence",)),
  Mapping("Infrastructure","Document Management",("document_id","document_type","valid_until"),("CBSE SARAS","SQAAF","UDISE+"),("fire_safety_certificate","building_safety_certificate")),
  Mapping("Disclosures","File Management",("document_id","publication_url","document_type"),("CBSE SARAS","OASIS"),("mandatory_disclosure_check",)),
  Mapping("Governance","Committee Management",("meeting_id","meeting_date","minutes_uri"),("SQAAF",),("improvement_action",)),
  Mapping("Fees","Fees Management",("fee_head","amount","academic_year"),("CBSE SARAS",),("disclosure_verification",)),
 ),
}
SYNTHETIC_INSTITUTIONS = {
 "University":{"institution_id":"DEMO-UNI-001","name":"Sample Valley University","aishe_code":"DEMO-ONLY","campus_id":"MAIN"},
 "College":{"institution_id":"DEMO-COL-001","name":"Sample Valley College","affiliating_university":"Example State University"},
 "School":{"school_id":"DEMO-SCH-001","name":"Sample Valley School","affiliation_number":"DEMO-ONLY","udise_code":"DEMO-ONLY"},
}
def build_demo(product, plan):
    if product not in MAPPINGS or plan not in PLAN_ORDER:
        raise ValueError("Unknown product or plan")
    output=[]
    for m in MAPPINGS[product]:
        minimum=CMS_MODULES[m.source_module]
        output.append({
          "domain":m.domain,"cms_module":m.source_module,"minimum_cms_plan":minimum,
          "available_in_selected_plan":PLAN_ORDER.index(plan)>=PLAN_ORDER.index(minimum),
          "assumed_source_fields":list(m.fields),"qualityhub_extra_fields":list(m.extra_fields),
          "possible_workspaces":list(m.targets),"connection_status":"ASSUMED — NOT CONNECTED",
        })
    return {"product":product,"plan":plan,"frameworks":list(PRODUCT_FRAMEWORKS[product]),
            "synthetic_institution":SYNTHETIC_INSTITUTIONS[product],
            "mapping":output,"assumptions":"CMS columns, APIs and regulatory applicability are not verified."}
