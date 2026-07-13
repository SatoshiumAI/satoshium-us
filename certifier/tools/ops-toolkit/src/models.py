"""
models.py — Data loading and field definitions for Satoshium certification artifacts.
"""
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


PLACEHOLDER_MARKERS = [
    "PLACEHOLDER",
    "YYYY-MM-DD",
    "YYYY-MM-DDTHH:MM:SSZ",
]

REQUIRED_CERT_FIELDS: List[Tuple[str, str]] = [
    ("certification_id",          "top-level"),
    ("schema_version",            "top-level"),
    ("issued_date",               "top-level"),
    ("status",                    "top-level"),
    ("certifier.id",              "certifier"),
    ("certifier.name",            "certifier"),
    ("certifier.role",            "certifier"),
    ("subject.id",                "subject"),
    ("subject.name",              "subject"),
    ("subject.type",              "subject"),
    ("subject.description",       "subject"),
    ("standard.id",               "standard"),
    ("standard.name",             "standard"),
    ("standard.version",          "standard"),
    ("methodology.id",            "methodology"),
    ("methodology.name",          "methodology"),
    ("scope.summary",             "scope"),
    ("outcome.status",            "outcome"),
    ("outcome.summary",           "outcome"),
    ("metadata.created_by",       "metadata"),
    ("metadata.created_at",       "metadata"),
]

EXPECTED_ARTIFACTS = [
    "certification_package.json",
    "certification_package.md",
    "scpr.md",
    "scr.md",
    "scrd.html",
    "scrd.json",
    "evidence_inventory.json",
    "evidence_map.md",
    "sreg_stub.json",
    "schr_stub.json",
    "anch_stub.json",
    "satr_stub.json",
    "release_checklist.md",
]


def load_certification_package(cert_dir: str) -> Dict[str, Any]:
    """Load and return the certification_package.json from the given directory."""
    path = Path(cert_dir) / "certification_package.json"
    if not path.exists():
        raise FileNotFoundError(
            f"certification_package.json not found in {cert_dir}"
        )
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_nested(obj: Dict[str, Any], dotted_key: str) -> Any:
    """Retrieve a value from a nested dict using dot notation."""
    keys = dotted_key.split(".")
    current = obj
    for k in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(k)
    return current


def contains_placeholder(value: Any) -> bool:
    """Return True if a value contains any placeholder marker."""
    if value is None:
        return True
    s = str(value)
    return any(marker in s for marker in PLACEHOLDER_MARKERS)


def today_iso() -> str:
    return date.today().isoformat()


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
