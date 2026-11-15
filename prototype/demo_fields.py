"""Public demo-only CSV field contracts. No persistence or institutional data."""

FIELDS = {
    "students": ("student_id", "program_code", "admission_year"),
    "staff": ("employee_id", "designation", "appointment_date"),
    "examinations": ("student_id", "program_code", "result_year", "result"),
    "placements": ("student_id", "employer", "offer_date"),
}
