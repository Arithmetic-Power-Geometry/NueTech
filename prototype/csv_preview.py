"""Safe, read-only CSV header mapping preview for the QualityHub demonstration."""
import csv
import io
from demo_fields import FIELDS

MAX_BYTES = 2_000_000

def inspect_csv(content: bytes, domain: str, mapping: dict | None = None) -> dict:
    if domain not in FIELDS:
        raise ValueError("Unsupported import domain")
    if not isinstance(content, bytes) or len(content) > MAX_BYTES:
        raise ValueError("CSV must be bytes and no larger than 2 MB")
    try:
        decoded = content.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("Upload UTF-8 CSV") from exc
    mapping = mapping or {}
    reader = csv.DictReader(io.StringIO(decoded, newline=""))
    headers = reader.fieldnames or []
    if not headers or len(headers) != len(set(headers)) or any(not h for h in headers):
        raise ValueError("Invalid or duplicate CSV headers")
    if any(key not in headers for key in mapping):
        raise ValueError("Mapping references a missing source column")
    targets = [mapping.get(h, h) for h in headers]
    if len(targets) != len(set(targets)):
        raise ValueError("Two source columns map to the same target")
    required = set(FIELDS[domain])
    missing = sorted(required - set(targets))
    count = 0
    seen = set()
    issues = []
    for row_number, row in enumerate(reader, start=2):
        count += 1
        if None in row or any(value is None for value in row.values()):
            issues.append(f"Row {row_number}: inconsistent column count")
            continue
        data = {mapping.get(key, key): value.strip() for key, value in row.items()}
        if not missing:
            key = data[FIELDS[domain][0]]
            if not key:
                issues.append(f"Row {row_number}: empty record identifier")
            elif key in seen:
                issues.append(f"Row {row_number}: duplicate record identifier")
            seen.add(key)
    return {
        "domain": domain,
        "source_columns": headers,
        "mapped_columns": targets,
        "required_columns": list(FIELDS[domain]),
        "missing_required": missing,
        "row_count": count,
        "issues": issues[:100],
        "truncated_issues": len(issues) > 100,
        "ready_to_stage": not missing and not issues,
        "note": "Header and row-shape preview only; no persistence or official regulator validation."
    }
