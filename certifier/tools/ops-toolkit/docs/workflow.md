# End-to-End Workflow Guide

This guide walks through the complete lifecycle of a Satoshium certification using the `satoshium-certifier-ops-toolkit`.

---

## Prerequisites

- Python 3.8 or later
- No external packages required (stdlib only)

Verify your Python version:

```bash
python --version
# or
python3 --version
```

---

## Step 1 — Initialize a New Certification

```bash
python scripts/new_certification.py SC-CERT-2026-0000
```

**What it does:**
- Creates `output/SC-CERT-2026-0000/`
- Copies the `package-templates/certification_package.json` template into the folder
- Sets `certification_id` to `SC-CERT-2026-0000`

**Expected output:**

```
✅  Initialized certification folder: output/SC-CERT-2026-0000
```

---

## Step 2 — Fill In the Certification Package

Open `output/SC-CERT-2026-0000/certification_package.json` in any text editor and replace every value marked `PLACEHOLDER` or `YYYY-MM-DD` with real data.

Refer to `docs/artifacts.md` for a full field reference.

**Key sections to complete:**

| Section | Fields to fill |
|---|---|
| Top-level | `issued_date`, `effective_date`, `status` |
| `certifier` | `id`, `name`, `role`, `contact` |
| `subject` | `id`, `name`, `type`, `description`, `version`, `repository` |
| `standard` | `id`, `name`, `version`, `reference_url` |
| `methodology` | `id`, `name`, `version`, `description` |
| `scope` | `summary`, `inclusions`, `exclusions` |
| `outcome` | `status`, `summary`, `determination_date` |
| `evidence_references` | At least one complete evidence item |
| `metadata` | `created_by`, `created_at` |

Also remove the `_instructions` key when you are done.

See `examples/SC-CERT-2026-0000/certification_package.json` for a fully completed reference.

---

## Step 3 — Validate the Certification Package

```bash
python scripts/validate_certification.py output/SC-CERT-2026-0000
```

**What it checks:**
- All required fields are present
- No placeholder values remain in required fields
- `status` and `outcome.status` are valid enum values
- `evidence_references` is non-empty and complete

**Pass output:**

```
✅  Validation passed.
```

**Fail output:**

```
❌  Validation failed with 3 error(s).

Errors:
  • Field 'certifier.name' still contains a placeholder value: 'CERTIFIER-NAME-PLACEHOLDER'
  • Field 'issued_date' still contains a placeholder value: 'YYYY-MM-DD'
  • evidence_references[0].location is missing or contains a placeholder.
```

Fix all errors before proceeding to artifact generation.

---

## Step 4 — Generate All Artifacts

```bash
python scripts/generate_artifacts.py output/SC-CERT-2026-0000
```

**What it generates** (12 derived artifacts):

```
  Generated: certification_package.md
  Generated: scpr.md
  Generated: scr.md
  Generated: scrd.json
  Generated: scrd.html
  Generated: evidence_inventory.json
  Generated: evidence_map.md
  Generated: sreg_stub.json
  Generated: schr_stub.json
  Generated: anch_stub.json
  Generated: satr_stub.json
  Generated: release_checklist.md

Done. 12 artifacts generated.
```

> **Note:** Generation proceeds even if validation warnings are present, but outputs may contain placeholder values. Always validate first.

---

## Step 5 — Complete the Stub Artifacts

The four stub files (`sreg_stub.json`, `schr_stub.json`, `anch_stub.json`, `satr_stub.json`) are pre-filled with known values from the package but contain placeholders that must be completed before submission:

| Stub | Fields to complete |
|---|---|
| `sreg_stub.json` | `entry_type`, `registry_submission_date`, `registry_reference` |
| `schr_stub.json` | `chronicle_type`, `event_description`, `preceding_record_id` |
| `anch_stub.json` | `anchor_type`, `anchor_target`, `anchor_hash`, `anchor_timestamp`, `anchor_reference_url` |
| `satr_stub.json` | `attestor_id`, `attestor_name`, `attestation_date`, `attestation_statement`, `attestation_signature` |

---

## Step 6 — Check Release Readiness

```bash
python scripts/check_release.py output/SC-CERT-2026-0000
```

**What it checks:**
- All 13 expected artifact files are present
- No placeholder markers remain in any file

**Pass output:**

```
Release Checklist — 13/13 artifacts present
==================================================

✅  Present artifacts:
  [x] certification_package.json
  [x] certification_package.md
  ...

🟢  Release check PASSED — all artifacts present and no placeholders found.
```

**Fail output:**

```
❌  Missing artifacts:
  [ ] anch_stub.json

⚠   Artifacts with unfilled placeholders:
  satr_stub.json:
    • 'PLACEHOLDER' appears 5x

🔴  Release check FAILED — address the items above before release.
```

---

## Reference: All Commands

```bash
# Initialize a new certification folder
python scripts/new_certification.py SC-CERT-2026-XXXX

# Validate the canonical package
python scripts/validate_certification.py output/SC-CERT-2026-XXXX

# Generate all derived artifacts
python scripts/generate_artifacts.py output/SC-CERT-2026-XXXX

# Check release readiness
python scripts/check_release.py output/SC-CERT-2026-XXXX
```

---

## Pushing to GitHub

See [README.md](../README.md#pushing-to-github) for the full push workflow.

```bash
git add output/SC-CERT-2026-0000
git commit -m "Add certification artifacts: SC-CERT-2026-0000"
git push
```
