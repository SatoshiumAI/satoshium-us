# Tests — satoshium-certifier-ops-toolkit

Unit tests for the toolkit's Python library (`src/`) and CLI scripts (`scripts/`).

## Requirements

- Python 3.8+
- No external packages — uses `unittest` from the standard library only

## Running the Tests

From the **repository root** (`satoshium-certifier-ops-toolkit/`):

```bash
# Run the full suite
python -m unittest discover tests -v

# Run a specific test module
python -m unittest tests.test_validator -v
python -m unittest tests.test_generator -v
python -m unittest tests.test_checklist -v
python -m unittest tests.test_new_certification -v
```

## Test Coverage

| Module | Test File | What is tested |
|---|---|---|
| `scripts/new_certification.py` | `test_new_certification.py` | Folder creation, certification_id propagation, valid JSON output, duplicate prevention |
| `src/validator.py` | `test_validator.py` | Clean package passes, placeholder detection, missing field detection, invalid status detection, warning vs error distinction |
| `src/generator.py` | `test_generator.py` | All 12 artifacts created, Markdown content accuracy, JSON validity and field accuracy, HTML escaping, edge cases (empty evidence, missing optional fields) |
| `src/checklist.py` | `test_checklist.py` | Empty dir detection, all-present pass, partial-present report, placeholder scanning, occurrence counts, summary text |

## What the Tests Do Not Cover

- End-to-end CLI execution via `subprocess` (this is verified by the GitHub Actions workflow)
- Network access (there is none — stdlib only)
- Schema validation against `schema/*.schema.json` (JSON Schema validation requires `jsonschema`; the schema files are reference-only and are not enforced at runtime)
- File permission errors on unusual OS configurations

## Smoke Test (Manual)

To manually verify the full CLI flow:

```bash
python scripts/new_certification.py SC-CERT-SMOKE-0000
# Edit output/SC-CERT-SMOKE-0000/certification_package.json — replace all PLACEHOLDER values
python scripts/validate_certification.py output/SC-CERT-SMOKE-0000
python scripts/generate_artifacts.py output/SC-CERT-SMOKE-0000
python scripts/check_release.py output/SC-CERT-SMOKE-0000
```

The example package can be used as a reference:

```bash
# Validate and run checklist against the pre-generated example
python scripts/validate_certification.py examples/SC-CERT-2026-0000
python scripts/generate_artifacts.py examples/SC-CERT-2026-0000
python scripts/check_release.py examples/SC-CERT-2026-0000
```
