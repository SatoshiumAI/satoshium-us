"""
validator.py — Field validation for Satoshium Certification Package JSON.
"""
from typing import Any, Dict, List

from .models import (
    REQUIRED_CERT_FIELDS,
    get_nested,
    contains_placeholder,
)


class ValidationResult:
    def __init__(self) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    def summary(self) -> str:
        lines = []
        if self.is_valid:
            lines.append("✅  Validation passed.")
        else:
            lines.append(f"❌  Validation failed with {len(self.errors)} error(s).")
        if self.errors:
            lines.append("\nErrors:")
            for e in self.errors:
                lines.append(f"  • {e}")
        if self.warnings:
            lines.append("\nWarnings:")
            for w in self.warnings:
                lines.append(f"  ⚠  {w}")
        return "\n".join(lines)


def validate_certification_package(pkg: Dict[str, Any]) -> ValidationResult:
    result = ValidationResult()

    # Check for template instruction key
    if "_instructions" in pkg:
        result.add_warning(
            "The '_instructions' key is still present. Remove it before generating artifacts."
        )

    # Required field presence and placeholder check
    for dotted_key, section in REQUIRED_CERT_FIELDS:
        value = get_nested(pkg, dotted_key)
        if value is None:
            result.add_error(f"Missing required field: '{dotted_key}' (section: {section})")
        elif contains_placeholder(value):
            result.add_error(
                f"Field '{dotted_key}' still contains a placeholder value: {value!r}"
            )

    # evidence_references must be a list
    refs = pkg.get("evidence_references")
    if not isinstance(refs, list):
        result.add_error("'evidence_references' must be an array.")
    elif len(refs) == 0:
        result.add_warning("'evidence_references' is empty — no evidence items listed.")
    else:
        for i, ref in enumerate(refs):
            for field in ("evidence_id", "title", "type", "location"):
                val = ref.get(field)
                if not val or contains_placeholder(val):
                    result.add_error(
                        f"evidence_references[{i}].{field} is missing or contains a placeholder."
                    )

    # Status must be a known value
    valid_statuses = {"PENDING", "CERTIFIED", "REJECTED", "SUSPENDED", "WITHDRAWN"}
    status = pkg.get("status")
    if status and status not in valid_statuses:
        result.add_error(
            f"'status' must be one of {sorted(valid_statuses)}, got: {status!r}"
        )

    outcome_status = get_nested(pkg, "outcome.status")
    if outcome_status and outcome_status not in valid_statuses:
        result.add_error(
            f"'outcome.status' must be one of {sorted(valid_statuses)}, got: {outcome_status!r}"
        )

    return result
