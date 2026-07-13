# satoshium-certifier-ops-toolkit

A command-line toolkit for generating, validating, and organizing certification artifacts for the **Satoshium Suite**.

---

## Overview

The **Certification Package JSON** is the canonical certification object. All other artifacts are generated representations or references derived from it.

This toolkit helps you:
- Initialize a new certification folder from a certification ID
- Generate all 13 artifact types from the canonical package
- Validate required fields
- Check release readiness

---

## Supported Artifacts

| Artifact | File | Description |
|---|---|---|
| Certification Package JSON | `certification_package.json` | Canonical certification object |
| Certification Package Markdown | `certification_package.md` | Human-readable certification summary |
| SCPR Markdown | `scpr.md` | Satoshium Certification Progress Report |
| SCR Markdown | `scr.md` | Satoshium Certification Record |
| SCRD HTML | `scrd.html` | Satoshium Certification Record Document (HTML) |
| SCRD JSON | `scrd.json` | Satoshium Certification Record Document (JSON) |
| Evidence Inventory JSON | `evidence_inventory.json` | Structured evidence inventory |
| Evidence Map Markdown | `evidence_map.md` | Evidence map narrative |
| SREG Registry Entry JSON stub | `sreg_stub.json` | Registry Entry reference stub |
| SCHR Chronicle Record JSON stub | `schr_stub.json` | Chronicle Record reference stub |
| ANCH Anchor Reference JSON stub | `anch_stub.json` | Anchor Reference stub |
| SATR Attestation Record JSON stub | `satr_stub.json` | Attestation Record reference stub |
| Release Checklist Markdown | `release_checklist.md` | Pre-release artifact completeness checklist |

---

## Requirements

- **Python 3.8+** (no external packages required — stdlib only)
- Git (for pushing to GitHub)

---

## Quick Start

### 1. Clone or download the repository

```bash
git clone https://github.com/YOUR_USERNAME/satoshium-certifier-ops-toolkit.git
cd satoshium-certifier-ops-toolkit
```

### 2. Initialize a new certification folder

```bash
python scripts/new_certification.py SC-CERT-2026-0001
```

This creates `output/SC-CERT-2026-0001/` with a pre-filled `certification_package.json` template. Open it and fill in all `PLACEHOLDER` fields before proceeding.

### 3. Generate all artifacts

```bash
python scripts/generate_artifacts.py output/SC-CERT-2026-0001
```

This reads `certification_package.json` and produces all other artifact files in the same folder.

### 4. Validate the certification package

```bash
python scripts/validate_certification.py output/SC-CERT-2026-0001
```

Reports any missing or incomplete required fields.

### 5. Check release readiness

```bash
python scripts/check_release.py output/SC-CERT-2026-0001
```

Reports which artifact files are present, missing, or contain unfilled placeholders.

---

## Directory Structure

```
satoshium-certifier-ops-toolkit/
├── README.md
├── LICENSE
├── .gitignore
├── package-templates/          # JSON/Markdown templates with placeholder fields
│   ├── certification_package.json
│   ├── scrd.json
│   ├── evidence_inventory.json
│   ├── sreg_stub.json
│   ├── schr_stub.json
│   ├── anch_stub.json
│   └── satr_stub.json
├── schema/                     # JSON Schema definitions for validation
│   ├── certification_package.schema.json
│   └── evidence_inventory.schema.json
├── src/                        # Shared Python library modules
│   ├── __init__.py
│   ├── models.py               # Data loading and field definitions
│   ├── generator.py            # Artifact generation logic
│   ├── validator.py            # Field validation logic
│   └── checklist.py            # Release checklist logic
├── scripts/                    # CLI entry points
│   ├── new_certification.py
│   ├── validate_certification.py
│   ├── generate_artifacts.py
│   └── check_release.py
├── examples/
│   └── SC-CERT-2026-0001/      # Sample certification (fully filled)
│       ├── certification_package.json
│       ├── certification_package.md
│       ├── scpr.md
│       ├── scr.md
│       ├── scrd.html
│       ├── scrd.json
│       ├── evidence_inventory.json
│       ├── evidence_map.md
│       ├── sreg_stub.json
│       ├── schr_stub.json
│       ├── anch_stub.json
│       ├── satr_stub.json
│       └── release_checklist.md
├── output/                     # Your generated certifications (git-ignored)
└── docs/
    ├── artifacts.md            # Artifact descriptions and field reference
    └── workflow.md             # End-to-end workflow guide
```

---

## Pushing to GitHub

### First time

```bash
# Inside the repo directory
git init
git add .
git commit -m "Initial commit: satoshium-certifier-ops-toolkit"
git remote add origin https://github.com/YOUR_USERNAME/satoshium-certifier-ops-toolkit.git
git push -u origin main
```

### Subsequent pushes

```bash
git add output/SC-CERT-2026-XXXX
git commit -m "Add certification SC-CERT-2026-XXXX artifacts"
git push
```

> **Note:** The `output/` folder is git-ignored by default. Remove the `output/` line from `.gitignore` if you want to commit generated artifacts, or copy finished certifications into a separate versioned folder.

---

## Running Completely Outside Replit

This toolkit has **no Replit dependencies**. To use it anywhere:

1. Copy or clone the repo to any machine with Python 3.8+.
2. Run scripts directly with `python scripts/<script>.py ...`
3. No `pip install` step is required — only the Python standard library is used.

---

## License

MIT License. See [LICENSE](LICENSE).
