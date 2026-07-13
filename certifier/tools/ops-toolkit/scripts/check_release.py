#!/usr/bin/env python3
"""
check_release.py — Report missing artifact files and incomplete artifact groups.

Usage:
    python scripts/check_release.py output/SC-CERT-2026-0001
"""
import sys
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLKIT_ROOT))

from src.checklist import run_checklist


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/check_release.py <CERT_DIR>")
        print("Example: python scripts/check_release.py output/SC-CERT-2026-0001")
        sys.exit(1)

    cert_dir = sys.argv[1].strip()
    path = Path(cert_dir)

    if not path.exists():
        print(f"Error: directory not found: {path}")
        sys.exit(1)

    print(f"\nChecking release readiness: {path}\n")

    result = run_checklist(cert_dir)
    print(result.summary())

    sys.exit(0 if result.is_complete else 1)


if __name__ == "__main__":
    main()
