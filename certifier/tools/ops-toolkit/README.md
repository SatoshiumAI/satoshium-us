# satoshium-certifier-ops-toolkit

> **PROTOCOL REVIEW NOTICE — October 23, 2026: LEGACY TOOLKIT CONTRACT**  
> This toolkit is a runnable artifact-generation and field-checking utility, **not** an independent certification authority or an implementation of every current Suite protocol. Several existing outputs and checks retain historical labels (`SCHR`, `SATR`) and an all-artifacts release checklist. These do **not** create Chronicle Entries, Anchor Integrity References, Registry Entries, Attestations, or Trust Statements, and do not make downstream institutional actions mandatory. Current Suite and institutional documentation controls. **Validation pass ≠ eligibility, conformance, certification, publication, or cross-institutional approval.** The code and generated formats remain unchanged pending a separately tested migration.


A command-line toolkit for generating, validating, and organizing certification artifacts for the **Satoshium Suite**.

---

## Overview

The **Certification Package** is Certifier's canonical operational object. Within this toolkit, `certification_package.json` is its source representation for generating derivative files; use of this JSON format does not itself create or approve a certification.

This toolkit helps you:
- Initialize a new certification folder from a certification ID
- Generate all certification artifacts from the canonical Certification Package
- Validate the Certification Package against required operational fields
- Run a legacy file-completeness and placeholder release check (not a publication authorization)

---

## Supported Artifacts

| Artifact | File | Description |
|---|---|---|
| Certification Package JSON | `certification_package.json` | Canonical operational certification object |
| Certification Package Markdown | `certification_package.md` | Human-readable representation of the canonical Certification Package |
| SCPR Markdown | `scpr.md` | Satoshium Certification Process Report |
| SCR Markdown | `scr.md` | Satoshium Certification Receipt |
| SCRD HTML | `scrd.html` | Satoshium Certified Record (HTML) |
| SCRD JSON | `scrd.json` | Satoshium Certified Record (JSON) |
| Evidence Inventory JSON | `evidence_inventory.json` | Structured evidence inventory |
| Evidence Map Markdown | `evidence_map.md` | Evidence map narrative |
| SREG Registry Entry JSON stub | `sreg_stub.json` | Registry Entry reference stub |
| SCHR Chronicle Record JSON stub | `schr_stub.json` | Chronicle Record reference stub |
| ANCH Anchor Reference JSON stub | `anch_stub.json` | Anchor Reference stub |
| SATR Attestation Record JSON stub | `satr_stub.json` | Attestation Record reference stub |
| Release Checklist Markdown | `release_checklist.md` | Pre-release artifact completeness checklist |

---

## Current interoperability boundary

The current production identifier families are **SREG**, **CHR**, **ANCH**, **BEAC**, **ATT**, and **TRST**, each governed by its originating institution. The toolkit's `schr_stub.json` and `satr_stub.json` are historical request/placeholder formats, **not** current canonical identifiers. Its `sreg_stub.json` and `anch_stub.json` are likewise only prospective preparation artifacts, not institution-issued records. The 13-file checklist is the legacy toolkit's local completeness rule, not a Suite-wide publication requirement. Use current institution-controlled records, validation procedures, and decisions for actual interoperability.

## Requirements

- **Python 3.8+** (no external packages required — stdlib only)
- Git (for pushing to GitHub)

---

## Quick Start

### 1. Clone or download the repository

Clone or download the repository from its official GitHub location, then open a terminal in the repository root:

```bash
cd satoshium-certifier-ops-toolkit
```

### 2. Initialize a new certification folder

```bash
python scripts/new_certification.py SC-CERT-2026-0000
```

This creates `output/SC-CERT-2026-0000/` with a pre-filled `certification_package.json` template. Open it and fill in all `PLACEHOLDER` fields before proceeding.

### 3. Generate all artifacts

```bash
python scripts/generate_artifacts.py output/SC-CERT-2026-0000
```

This reads `certification_package.json` and produces all other artifact files in the same folder.

### 4. Validate the certification package

```bash
python scripts/validate_certification.py output/SC-CERT-2026-0000
```

Reports missing or incomplete operational fields in the canonical Certification Package.

### 5. Check release readiness

```bash
python scripts/check_release.py output/SC-CERT-2026-0000
```

Reports which certification artifacts are present, missing, or contain unfilled placeholders before publication.

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
│   └── SC-CERT-2026-0000/      # Sample certification (fully filled)
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

## Platform Compatibility

This toolkit runs on any system with **Python 3.8+** and requires no external Python packages.

1. Copy or clone the repository to a compatible system.
2. Run scripts directly with `python scripts/<script>.py ...`.
3. No `pip install` step is required because the toolkit uses only the Python standard library.

---

## License

MIT License. See [LICENSE](LICENSE).
