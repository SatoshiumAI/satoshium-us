#!/usr/bin/env python3
"""
generate_artifacts.py — Generate all derived artifacts from a Certification Package JSON.

Usage:
    python scripts/generate_artifacts.py output/SC-CERT-2026-0001
"""
import sys
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLKIT_ROOT))

from src.models import load_certification_package
from src.validator import validate_certification_package
from src.generator import generate_all_artifacts


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_artifacts.py <CERT_DIR>")
        print("Example: python scripts/generate_artifacts.py output/SC-CERT-2026-0001")
        sys.exit(1)

    cert_dir = sys.argv[1].strip()
    path = Path(cert_dir)

    if not path.exists():
        print(f"Error: directory not found: {path}")
        sys.exit(1)

    print(f"\nLoading: {path / 'certification_package.json'}")

    try:
        pkg = load_certification_package(cert_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Warn if there are validation errors but don't block generation
    result = validate_certification_package(pkg)
    if not result.is_valid:
        print("\n⚠   Validation warnings detected — artifacts will still be generated,")
        print("    but output may contain placeholder values.\n")
        for err in result.errors:
            print(f"  • {err}")
        print()

    generate_all_artifacts(pkg, path)


if __name__ == "__main__":
    main()
