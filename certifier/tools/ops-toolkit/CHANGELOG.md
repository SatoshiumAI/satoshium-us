# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-07-13

### Added

- Initial release of `satoshium-certifier-ops-toolkit`.
- `scripts/new_certification.py` — initialize a new certification folder from a certification ID.
- `scripts/validate_certification.py` — validate required fields in a Certification Package JSON.
- `scripts/generate_artifacts.py` — generate all 12 derived artifacts from the canonical package.
- `scripts/check_release.py` — check release readiness: missing files and unfilled placeholders.
- `src/models.py` — shared data model, field definitions, and utility functions.
- `src/validator.py` — field validation logic with structured `ValidationResult`.
- `src/generator.py` — all 12 artifact generators with HTML escaping for SCRD HTML output.
- `src/checklist.py` — release checklist logic with placeholder scanning.
- `package-templates/` — JSON templates for all artifact types with `PLACEHOLDER` fields.
- `schema/` — JSON Schema definitions for `certification_package` and `evidence_inventory`.
- `examples/SC-CERT-2026-0001/` — fully populated sample certification with all 13 artifacts.
- `tests/` — `unittest`-based test suite covering new-certification, validation, generation, and checklist.
- `tests/fixtures/complete-certification/` — committed fixture with all 13 artifact files and no placeholder markers; used to assert `check_release.py` exits 0 in CI.
- `tests/fixtures/incomplete-certification/` — committed fixture with 2 of 13 artifact files, both containing placeholder markers; used to assert `check_release.py` exits 1 in CI.
- `.github/workflows/validate-toolkit.yml` — 10-step GitHub Actions CI workflow (Python 3.11):
  - Steps 1–2: `py_compile` syntax check and import validation.
  - Step 3: full `unittest` suite including fixture-based integration tests.
  - Steps 4–6: end-to-end smoke tests (validate, generate, new-certification).
  - Step 7: release check on complete fixture — asserts exit 0; fails CI if it exits 1.
  - Step 8: release check on incomplete fixture — asserts exit 1; fails CI if it exits 0. No `|| true` masking.
  - Steps 9–10: Replit lock-in file check and stdlib-only assertion.
- `docs/artifacts.md` — artifact field reference.
- `docs/workflow.md` — end-to-end workflow guide.
- `MANIFEST.md` — complete file listing with purpose descriptions.
- `VERSION` — semantic version file.
- `CHANGELOG.md` — this file.

### Technical notes

- stdlib-only: no external dependencies required.
- Python 3.8+ compatible; tested in CI on Python 3.11.
- HTML output uses `html.escape()` for all user-supplied field values.
- `datetime.now(timezone.utc)` used throughout (avoids deprecated `utcnow()`).
- No `|| true` in CI: expected pass and expected fail are both asserted explicitly via committed fixtures.
