#!/usr/bin/env python3
"""
new_certification.py — Initialize a new certification folder from a certification ID.

Usage:
    python scripts/new_certification.py SC-CERT-2026-0001
"""
import json
import sys
from pathlib import Path


TOOLKIT_ROOT  = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = TOOLKIT_ROOT / "package-templates" / "certification_package.json"
OUTPUT_ROOT   = TOOLKIT_ROOT / "output"


def init_certification(cert_id: str) -> None:
    cert_dir = OUTPUT_ROOT / cert_id

    if cert_dir.exists():
        print(f"Error: '{cert_dir}' already exists. Delete it first if you want to reinitialize.")
        sys.exit(1)

    if not TEMPLATE_PATH.exists():
        print(f"Error: template not found at {TEMPLATE_PATH}")
        sys.exit(1)

    cert_dir.mkdir(parents=True)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = json.load(f)

    template["certification_id"] = cert_id

    pkg_path = cert_dir / "certification_package.json"
    with open(pkg_path, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2)
        f.write("\n")

    print(f"\n✅  Initialized certification folder: {cert_dir}")
    print(f"\nNext steps:")
    print(f"  1. Open and fill in all PLACEHOLDER fields in:")
    print(f"       {pkg_path}")
    print(f"  2. Run validation:")
    print(f"       python scripts/validate_certification.py output/{cert_id}")
    print(f"  3. Generate all artifacts:")
    print(f"       python scripts/generate_artifacts.py output/{cert_id}")
    print(f"  4. Check release readiness:")
    print(f"       python scripts/check_release.py output/{cert_id}")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/new_certification.py <CERTIFICATION_ID>")
        print("Example: python scripts/new_certification.py SC-CERT-2026-0001")
        sys.exit(1)

    cert_id = sys.argv[1].strip()
    init_certification(cert_id)
