# End-to-End Workflow Guide

> **PROTOCOL REVIEW NOTICE — October 23, 2026: LEGACY TOOLKIT CONTRACT**  
> This toolkit is a runnable artifact-generation and field-checking utility, **not** an independent certification authority or an implementation of every current Suite protocol. Several existing outputs and checks retain historical labels (`SCHR`, `SATR`) and an all-artifacts release checklist. These do **not** create Chronicle Entries, Anchor Integrity References, Registry Entries, Attestations, or Trust Statements, and do not make downstream institutional actions mandatory. Current Suite and institutional documentation controls. **Validation pass ≠ eligibility, conformance, certification, publication, or cross-institutional approval.** The code and generated formats remain unchanged pending a separately tested migration.


This guide walks through the toolkit's **legacy local generation workflow**, not the complete governed certification lifecycle or a required Suite-wide workflow.

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

## Step 5 — Review Legacy Stub Artifacts (Conditional Only)

The four generated stub files (`sreg_stub.json`, `schr_stub.json`, `anch_stub.json`, `satr_stub.json`) are **historical toolkit placeholders**. Do not interpret their presence or the table below as instructions to create downstream records or as a required submission sequence. These stub formats have **not** been migrated to the current Chronicle (`CHR`) and Attestor (`ATT` / `TRST`) contracts. Only the relevant institution may create/govern its canonical objects. The table describes fields expected by the existing utility, **not** required current institution fields:

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

**What it checks (legacy implementation only):**
- All 13 legacy toolkit-expected artifact files are present
- No placeholder markers remain in any file

**Not checked:** independent institutional approvals, all current schema/contract semantics, eligibility, conformance, certification, Attestor evaluation, or publication authorization. A release-check PASS is **not** an authorization to publish and may fail merely because a non-required downstream stub remains uncompleted.

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

The following Git commands are illustrative only. Generated `output/` is git-ignored in this toolkit; confirm the intended location and artifact governance before committing or publishing. See the repository's applicable deployment procedures.

```bash
git add output/SC-CERT-2026-0000
git commit -m "Add certification artifacts: SC-CERT-2026-0000"
git push
```
