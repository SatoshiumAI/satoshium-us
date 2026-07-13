#!/usr/bin/env python3
"""
validate_certification.py — Validate required fields in a Certification Package JSON.

Usage:
    python scripts/validate_certification.py output/SC-CERT-2026-0001
"""
import sys
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLKIT_ROOT))

from src.models import load_certification_package
from src.validator import validate_certification_package


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_certification.py <CERT_DIR>")
        print("Example: python scripts/validate_certification.py output/SC-CERT-2026-0001")
        sys.exit(1)

    cert_dir = sys.argv[1].strip()
    path = Path(cert_dir)

    if not path.exists():
        print(f"Error: directory not found: {path}")
        sys.exit(1)

    print(f"\nValidating: {path / 'certification_package.json'}\n")

    try:
        pkg = load_certification_package(cert_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    result = validate_certification_package(pkg)
    print(result.summary())

    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
