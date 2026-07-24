# MANIFEST — satoshium-certifier-ops-toolkit

Complete file listing for version 0.1.0. Every file in the repository and its purpose.

---

## Root

| File | Purpose |
|---|---|
| `README.md` | Primary documentation: overview, supported artifacts, quick-start, directory structure, GitHub push instructions, local usage guide |
| `LICENSE` | MIT License |
| `.gitignore` | Excludes `output/`, Python bytecode, OS files, editor files, and logs from git |
| `VERSION` | Semantic version string (currently `0.1.0`) |
| `CHANGELOG.md` | Version history following Keep a Changelog format |
| `MANIFEST.md` | This file — complete repository file listing with purpose descriptions |

---

## `.github/`

| File | Purpose |
|---|---|
| `.github/workflows/validate-toolkit.yml` | GitHub Actions CI workflow (10 steps, Python 3.11 on ubuntu-latest). Runs on every push and pull request. See "GitHub Actions Steps" section below for the full step breakdown. |

---

## `docs/`

| File | Purpose |
|---|---|
| `docs/artifacts.md` | Reference guide for all 13 artifact types: purpose, generation source, and field descriptions |
| `docs/workflow.md` | End-to-end workflow guide covering all four CLI commands with expected inputs, outputs, and error messages |

---

## `examples/`

Pre-generated, fully populated sample certification using ID `SC-CERT-2026-0000`. All 13 artifact files are present. Values are illustrative only.

| File | Purpose |
|---|---|
| `examples/SC-CERT-2026-0000/certification_package.json` | Canonical certification object — primary source for all other artifacts |
| `examples/SC-CERT-2026-0000/certification_package.md` | Human-readable Markdown summary of the certification package |
| `examples/SC-CERT-2026-0000/scpr.md` | Satoshium Certification Progress Report |
| `examples/SC-CERT-2026-0000/scr.md` | Satoshium Certification Record |
| `examples/SC-CERT-2026-0000/scrd.html` | Satoshium Certification Record Document (HTML, self-contained, no external dependencies) |
| `examples/SC-CERT-2026-0000/scrd.json` | Satoshium Certification Record Document (JSON) |
| `examples/SC-CERT-2026-0000/evidence_inventory.json` | Structured inventory of all evidence items |
| `examples/SC-CERT-2026-0000/evidence_map.md` | Narrative Markdown map of evidence items |
| `examples/SC-CERT-2026-0000/sreg_stub.json` | SREG Registry Entry stub — partially populated; fill before Registry submission |
| `examples/SC-CERT-2026-0000/schr_stub.json` | SCHR Chronicle Record stub — partially populated; fill before Chronicle submission |
| `examples/SC-CERT-2026-0000/anch_stub.json` | ANCH Anchor Reference stub — partially populated; fill before anchoring |
| `examples/SC-CERT-2026-0000/satr_stub.json` | SATR Attestation Record stub — partially populated; fill before Attestor submission |
| `examples/SC-CERT-2026-0000/release_checklist.md` | Release readiness checklist with checkboxes for all 13 artifacts and validation steps |

---

## `output/`

| File | Purpose |
|---|---|
| `output/.gitkeep` | Keeps the `output/` directory tracked by git. The `output/` directory itself is in `.gitignore` so generated certifications are not committed unless explicitly added. |

---

## `package-templates/`

Blank JSON templates with `PLACEHOLDER` fields. Used by `scripts/new_certification.py` to initialize new certification folders. Do not edit — these are the canonical starting points.

| File | Purpose |
|---|---|
| `package-templates/certification_package.json` | Primary template for the canonical certification object. Contains all required and optional fields. |
| `package-templates/evidence_inventory.json` | Template for the Evidence Inventory JSON artifact |
| `package-templates/scrd.json` | Template for the SCRD JSON artifact |
| `package-templates/sreg_stub.json` | Template for the SREG Registry Entry JSON stub |
| `package-templates/schr_stub.json` | Template for the SCHR Chronicle Record JSON stub |
| `package-templates/anch_stub.json` | Template for the ANCH Anchor Reference JSON stub |
| `package-templates/satr_stub.json` | Template for the SATR Attestation Record JSON stub |

---

## `schema/`

JSON Schema definitions (draft-07). Reference documents for understanding artifact structure. Not enforced at runtime (no `jsonschema` dependency).

| File | Purpose |
|---|---|
| `schema/certification_package.schema.json` | JSON Schema for the canonical Certification Package |
| `schema/evidence_inventory.schema.json` | JSON Schema for the Evidence Inventory artifact |

---

## `scripts/`

CLI entry points. Run from the repository root. Path resolution uses `Path(__file__).resolve().parent.parent` — no manual `PYTHONPATH` setup required.

| File | Purpose |
|---|---|
| `scripts/__init__.py` | Makes `scripts/` a Python package, enabling test imports |
| `scripts/new_certification.py` | Initialize a new certification folder. Usage: `python scripts/new_certification.py <CERT_ID>` |
| `scripts/validate_certification.py` | Validate required fields. Usage: `python scripts/validate_certification.py <CERT_DIR>` |
| `scripts/generate_artifacts.py` | Generate all 12 derived artifacts. Usage: `python scripts/generate_artifacts.py <CERT_DIR>` |
| `scripts/check_release.py` | Check release readiness. Exits 0 if all 13 artifacts are present and placeholder-free; exits 1 otherwise. Usage: `python scripts/check_release.py <CERT_DIR>` |

---

## `src/`

Shared Python library. Stdlib-only — no external dependencies.

| File | Purpose |
|---|---|
| `src/__init__.py` | Makes `src/` a Python package |
| `src/models.py` | Shared constants, data loading, field traversal, placeholder detection, date utilities |
| `src/validator.py` | `ValidationResult` class and `validate_certification_package()` — checks required fields, placeholder values, evidence completeness, status enum values |
| `src/generator.py` | All 12 artifact generator functions. Uses `html.escape()` for all user-supplied values in HTML output. |
| `src/checklist.py` | `ChecklistResult` class, `check_for_placeholders()` helper, and `run_checklist()` — scans for missing files and remaining placeholder markers |

---

## `tests/`

Unit and integration test suite. Uses Python `unittest` (stdlib only). Run with `python -m unittest discover tests -v` from the repository root.

| File | Purpose |
|---|---|
| `tests/__init__.py` | Makes `tests/` a Python package |
| `tests/README.md` | Test documentation: how to run, coverage table, what is and isn't tested, manual smoke test |
| `tests/test_new_certification.py` | 6 tests: folder creation, cert ID propagation, placeholder replacement, valid JSON output, duplicate prevention |
| `tests/test_validator.py` | 18 tests: clean pass, placeholder detection, missing fields, invalid status values, warning vs error distinction |
| `tests/test_generator.py` | 24 tests: all 12 artifacts created, Markdown content, JSON validity, HTML escaping, edge cases |
| `tests/test_checklist.py` | 26 tests: empty dir, all-present pass, partial-present, placeholder scanning, fixture-based integration (see below) |

### `tests/fixtures/`

Committed fixture directories used by both the test suite and the GitHub Actions workflow to assert explicit pass/fail outcomes from `check_release.py`. Neither fixture uses `|| true` — pass and fail are both asserted directly.

| Directory | File count | Purpose |
|---|---|---|
| `tests/fixtures/complete-certification/` | 13 | All 13 required artifact files present; no placeholder markers in any file. `check_release.py` must exit 0. |
| `tests/fixtures/incomplete-certification/` | 2 | Only 2 of 13 artifact files present; both contain placeholder markers. `check_release.py` must exit 1. |

#### `tests/fixtures/complete-certification/` (13 files)

| File | Notes |
|---|---|
| `certification_package.json` | Fully populated; no placeholder fields |
| `certification_package.md` | Clean content |
| `scpr.md` | Clean content |
| `scr.md` | Clean content |
| `scrd.html` | Clean content |
| `scrd.json` | Clean content |
| `evidence_inventory.json` | Clean content |
| `evidence_map.md` | Clean content |
| `sreg_stub.json` | All stub fields filled (entry_type, registry_submission_date, registry_reference populated) |
| `schr_stub.json` | All stub fields filled (chronicle_type, event_description, preceding_record_id populated) |
| `anch_stub.json` | All stub fields filled (anchor_type, anchor_target, anchor_hash, anchor_timestamp, anchor_reference_url populated) |
| `satr_stub.json` | All stub fields filled (attestor_id, attestor_name, attestation_date, attestation_statement, attestation_signature populated) |
| `release_checklist.md` | Clean content |

#### `tests/fixtures/incomplete-certification/` (2 files)

| File | Notes |
|---|---|
| `certification_package.json` | Present but contains placeholder markers (`CERTIFIER-NAME-PLACEHOLDER`, `YYYY-MM-DD`, etc.) |
| `scpr.md` | Present but contains placeholder markers (`YYYY-MM-DD`, `SUBJECT-NAME-PLACEHOLDER`, etc.) |
| *(11 other artifacts)* | Intentionally absent |

---

## GitHub Actions Steps

The workflow at `.github/workflows/validate-toolkit.yml` runs 10 steps:

| Step | Name | What it asserts |
|---|---|---|
| 1 | Syntax check — src/ | All `src/` Python files compile without `SyntaxError` |
| 2 | Syntax check — scripts/ | All `scripts/` Python files compile without `SyntaxError` |
| 3 | Syntax check — tests/ | All `tests/` Python files compile without `SyntaxError` |
| 4 | Import check — src modules | All `src/` modules import cleanly (catches broken relative imports, `ImportError`, load-time `NameError`) |
| 5 | Run unit tests | Full `unittest discover tests` suite passes (68+ assertions) |
| 6 | Smoke — validate example | `validate_certification.py examples/SC-CERT-2026-0000` exits 0 |
| 7 | Smoke — generate artifacts | `generate_artifacts.py examples/SC-CERT-2026-0000` exits 0 and produces files |
| 8 | Smoke — new certification | `new_certification.py SC-CERT-CI-0000` exits 0 and creates the expected folder |
| 9 | **Release check — complete fixture must PASS** | `check_release.py tests/fixtures/complete-certification` exits 0; CI fails if it exits 1 |
| 10 | **Release check — incomplete fixture must FAIL** | `check_release.py tests/fixtures/incomplete-certification` exits 1; CI fails if it exits 0 |
| 11 | Check for Replit-specific files | `.replit`, `replit.nix`, `.breakpoints` must be absent |
| 12 | Verify no requirements.txt | Absence of `requirements.txt` confirms stdlib-only constraint |

> Steps 9 and 10 use no `|| true`. Both outcomes are asserted explicitly.

---

## Summary

| Category | File count |
|---|---|
| Root (README, LICENSE, etc.) | 6 |
| `.github/workflows/` | 1 |
| `docs/` | 2 |
| `examples/SC-CERT-2026-0000/` | 13 |
| `output/` | 1 |
| `package-templates/` | 7 |
| `schema/` | 2 |
| `scripts/` | 5 |
| `src/` | 5 |
| `tests/` (root) | 6 |
| `tests/fixtures/complete-certification/` | 13 |
| `tests/fixtures/incomplete-certification/` | 2 |
| **Total** | **63** |
