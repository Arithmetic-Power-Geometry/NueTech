"""NueTech QualityHub: conservative evidence readiness evaluator.
Design and Developed by Dr. Mohammad Amir Khusru Akhtar.
No official regulator score or submission eligibility is calculated.
"""
from dataclasses import dataclass
from typing import Iterable

PRODUCTS = {
    'University': ('NAAC', 'NIRF', 'IQAC', 'AQAR'),
    'College': ('NAAC', 'NIRF', 'IQAC', 'AQAR'),
    'School': ('CBSE SARAS', 'SQAAF', 'OASIS', 'UDISE+'),
}
STATES = {'missing', 'uploaded', 'verified', 'rejected'}

@dataclass(frozen=True)
class Requirement:
    code: str
    framework: str
    title: str
    evidence_status: str = 'missing'
    template_verified: bool = False
    reviewer_approved: bool = False

def evaluate(product: str, requirements: Iterable[Requirement]) -> dict:
    if product not in PRODUCTS:
        raise ValueError('Unknown licensed product')
    rows = list(requirements)
    if len({r.code for r in rows}) != len(rows):
        raise ValueError('Duplicate requirement code')
    for r in rows:
        if r.framework not in PRODUCTS[product]:
            raise ValueError('Framework incompatible with product')
        if r.evidence_status not in STATES:
            raise ValueError('Invalid evidence state')
    verified = sum(r.evidence_status == 'verified' and r.template_verified and r.reviewer_approved for r in rows)
    gaps = [r.code for r in rows if not (r.evidence_status == 'verified' and r.template_verified and r.reviewer_approved)]
    return {'product': product, 'requirements': len(rows), 'ready': verified,
            'gaps': gaps, 'status': 'PREPARATION COMPLETE (internal only)' if rows and not gaps else 'NOT READY',
            'disclaimer': 'Internal evidence checklist only; not a regulatory score or certification.'}
