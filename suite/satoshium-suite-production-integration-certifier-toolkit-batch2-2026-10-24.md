# Satoshium Suite — Phase 2 Certifier Toolkit Reliability and Migration Gate

**Date:** October 24, 2026  
**Scope:** PI-03 (toolkit migration classification) and PI-04 (unreadable artifact fail-closed behavior)  
**Branch:** `phase004`  
**Baseline:** `b9e2570dcbc54e6bd62085351d0796907f1d880f`  
**Review disposition:** **COMPLETE — APPROVED (source correction + regression-test coverage)**  
**Executable test status:** **NOT RUN IN THIS ENVIRONMENT** — no repository checkout/Python runtime from connected GitHub is available, and GitHub Pages deployment is not a Python test runner.  
**Phase 2 overall:** ACTIVE.

## PI-04 — Proven static failure mode and bounded correction

Prior `src/checklist.py` caught `Exception` when scanning each present artifact and silently suppressed read failures, allowing `is_complete` to return true if all expected paths existed and none of the *readable* files contained placeholders. This is a false-positive risk, not proof any real production artifact was unreadable.

The correction:
- propagates errors from `check_for_placeholders()` instead of swallowing all exceptions;
- catches expected `OSError` and `UnicodeError` at the per-artifact `run_checklist()` boundary and records a distinct `read_errors` entry with artifact and exception type/message;
- includes `read_errors` in the release completeness predicate and human-readable FAILED summary;
- retains all historic `EXPECTED_ARTIFACTS` names and the 13-artifact contract, so this patch cannot be construed as protocol migration;
- keeps `scripts/check_release.py` existing `exit 0` for complete and `exit 1` for incomplete; the new error classification feeds that existing exit logic.

Added tests to `tests/test_checklist.py`: simulated PermissionError for a present artifact with all other artifacts clean, genuinely invalid UTF-8 content, and command-line invocation expecting exit code 1, explicit error information and FAILED text. Updated `tests/README.md` to clarify the simulated-permission and encoding-failure coverage.

**Test run evidence:** Test source has been added but no assertion is made that these tests ran successfully against the repository in an executable environment. Required next acceptance: run `python -m unittest discover tests -v` and `python -m unittest tests.test_checklist -v` from `certifier/tools/ops-toolkit/` with Python 3.8+, verify all passes including fixture tests and new negative cases. Check CLI exit code independently. Until then **PI-04 = SOURCE CORRECTED / RUNTIME VERIFICATION OPEN**, not implementation certified.

## PI-03 — Legacy cross-institution migration remains deferred

Inspected `src/models.py`, `src/checklist.py`, `scripts/check_release.py` and the existing October 23 migration assessment alongside historic tests. `EXPECTED_ARTIFACTS` continues to require 13 names, including `sreg_stub.json`, `schr_stub.json`, `anch_stub.json`, `satr_stub.json`. This legacy self-contained artifact check is not a governed current CHR/ATT/TRST creation contract. The checklist's PASS, even after reliability correction, is not Certifier institutional approval, Registry registration, Chronicle preservation, Anchor integrity issuance or Attestor publication.

Do **not** rename downstream stubs, make handoffs automatic or remove fixture requirements by incidental patch. A separately versioned migration remains necessary once institution-owned optional request interfaces and desired local-only completeness policy are formally specified. The existing assessment and `PR-OPEN-001` remain authoritative. No institution's canonical object ownership or authority was modified.

## Acceptance / handoff

| Item | State | Required remaining proof |
|---|---|---|
| PI-04 present-but-unreadable artifact detection | Source corrected and tests authored; **not yet executed** | Run tests in actual Python environment, verify CLI exit, ensure no regressions |
| PI-03 legacy toolkit migration | DEFERRED — unchanged | Versioned current contract, optional receiving interfaces, fixtures/docs/CI migration and runtime tests |
| PR-OPEN-001 | OPEN / DEFERRED | Current-protocol interfaces and migrated toolkit |
| PR-OPEN-002 | PENDING EXECUTION VERIFICATION | Negative test and CLI evidence, then change disposition in existing register |
| General IQ-001–023 | OPEN as applicable | Their existing specific machine-contract acceptance criteria |

> **Authority follows the governed subject. Reference does not transfer authority.**

**This bounded Phase 2 source and regression design review is COMPLETE — APPROVED; Phase 2 overall remains ACTIVE.**
