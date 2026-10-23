# Satoshium Certifier Operations Toolkit — Protocol Migration Assessment

**Date:** October 23, 2026  
**Review Classification:** RECONCILE / DEFER IMPLEMENTATION  
**Status:** COMPLETE — APPROVED (assessment only); executable migration NOT PERFORMED  
**Institution:** Satoshium Certifier  
**Scope:** `certifier/tools/ops-toolkit/` legacy generator, field validator, release checker, templates, fixtures, and tests

## Governing boundary

Certifier owns the canonical **Certification Package** and its certification decisions. The toolkit's `certification_package.json` is an input representation for mechanically generated artifacts, not a substitute for institutional creation or approval. Registry governs **SREG**, Chronicle governs **CHR**, Anchor governs **ANCH**, Beacon governs **BEAC**, and Attestor governs **ATT** and **TRST** with Rule-Constrained Evaluation.

**Reference does not transfer authority.** No downstream object is created or approved merely by generating a local request stub, passing a field check, or assembling a file set.

The exercised inaugural Suite lineage is evidence of one production case, **not a mandatory inter-institutional pipeline**.

## Confirmed current executable contract

| Area | Observed implementation | Migration consequence |
|---|---|---|
| `src/generator.py` | Emits `sreg_stub.json`, `schr_stub.json`, `anch_stub.json`, `satr_stub.json` plus Certification Package-derived artifacts | `SCHR` and `SATR` are historical toolkit request formats, **not** current CHR, ATT or TRST contracts; generated files cannot be renamed and represented as valid institution-issued objects |
| `src/models.py` | `EXPECTED_ARTIFACTS` hardcodes 13 artifacts, including all four downstream stubs | Makes otherwise optional cross-institution preparation look compulsory for local completeness |
| `src/checklist.py`, `scripts/check_release.py` | Completeness succeeds only when all 13 expected files exist and placeholder markers are absent; success is printed as a release-check PASS | PASS proves neither governed Certifier approval nor Registry/Chronicle/Anchor/Attestor authorization or publication |
| `src/validator.py` | Checks required fields, placeholder markers, select statuses, and evidence-list shape | Not comprehensive current Schema, Validation, Conformance, or institutional decision verification |
| `schema/*.schema.json` | Reference schemas; the tests README states JSON Schema is not enforced by runtime validator | An implementation migration must decide separately whether/how to add explicit versioned schema validation |
| `tests/test_generator.py`, `tests/test_checklist.py`, `tests/test_validator.py`, `tests/test_new_certification.py` | Tests encode the historical filenames, 13-file checklist, statuses, and generated shapes | Any change needs matching baseline and migration tests; historical fixtures should not be silently relabeled |
| `tests/fixtures/`, `MANIFEST.md` and CI workflow | Complete/incomplete fixtures intentionally assert 13-file PASS/FAIL | CI fixture and documentation changes must be coordinated with new behavior |

**Additional implementation concern:** `check_for_placeholders()` catches and silently ignores file-read exceptions. A present but unreadable artifact could therefore avoid a placeholder warning. A future reliability patch should fail closed on read errors, with a regression test, independently of any institutional protocol migration. This is a source-inspection finding, **not** evidence that such an unreadable production artifact has occurred.

## Decision — no untested replacement of downstream records

Do **not** mechanically rename `schr_stub.json` to `chr_stub.json` or `satr_stub.json` to `att_stub.json`; do **not** claim that generating either proves CHR, ATT, or TRST creation. A real replacement must be a clearly labeled **optional preparation/handoff request**, subject to each receiving institution's separately specified interface, eligibility, decision, and publication process. If the receiving institution has no formally governed request interface, **do not invent one**.

Similarly, `sreg_stub.json` and `anch_stub.json` remain local preparation artifacts. Beacon publication and Attestor's bounded Evaluation/Trust Statement path are not automatically required of every Certification Package.

## Proposed bounded implementation sequence — future work, not authorized as complete

1. **Freeze historical behavior.** Preserve the v0.1 toolkit contract, 13-file fixtures, and historical changelog so old outputs remain interpretable.
2. **Define the current contract.** Identify Certifier-owned required output artifacts separately from optional institution-specific requests. Record which external interfaces actually exist before writing adapters.
3. **Separate result types.** Report `local_artifact_completeness` and `field_validation` independently of `institutional_approval`, `publication`, and `external_handoff`. An unknown or unverified external status must not be shown as PASS.
4. **Make conditional outputs opt-in.** If supported by governing interfaces, allow explicit user/workflow selection of appropriate handoff requests; default to no implied downstream publication.
5. **Migrate schemas and validators only against adopted contracts.** Maintain canonical Package identity and clear validation/decision boundaries; do not silently redefine Certifier status or outcome vocabulary.
6. **Update fixtures, tests, generated checklist, CLI messages, README, public page, manifest, and CI as one coherent versioned release.** Historical examples remain labeled.
7. **Run regression suite and new negative-path tests before declaring migration complete.** Require explicit authorization from each institution for any actual creation or publication call.

## Minimum migration acceptance tests

- **Certifier only:** A valid local Certification Package with **no** downstream request stubs is not incorrectly rejected for missing optional institutional handoffs.
- **No false authority:** A generator/checklist PASS never asserts certification approval, SREG registration, CHR preservation, ANCH integrity, ATT evaluation, TRST publication, or Beacon signaling.
- **Canonical identity:** Source identifier, Certifier Package identity, and optional downstream request identifiers are not conflated; a request file is not represented as a canonical institution-issued record.
- **Conditional operations:** No external request is emitted or mandatory unless expressly selected and a governed interface exists.
- **Validation limits:** Schema-only success and field-only success do not become institutional Validation or Conformance results.
- **Negative paths:** Missing mandatory local files, placeholders, invalid JSON, stale source versions, inconsistent identifiers, and unreadable files fail or report explicit errors; no unexpected PASS.
- **History/compatibility:** Legacy fixtures remain interpretable; former scripts and examples do not silently change meaning.
- **Regression/CI:** Generator, validator, checklist, CLI smoke checks, complete/incomplete fixtures, and end-to-end run pass for the new version in an executable test environment.
- **Version and publication discipline:** Implementation migration receives a new documented toolkit version, and publication remains a distinct institution-controlled action.

## Review result

**Architecture:** CONFIRM — no Suite constitutional CHANGE required.  
**Legacy tool semantics:** RECONCILE — meaningful migration required before current-protocol executable claims.  
**Current documentation warnings:** CORRECT — existing README, workflow, artifacts documentation and public page already mark historical behavior.  
**Executable migration:** DEFER — intentionally not performed or asserted tested in this review.  
**Outstanding reliability test:** unreadable-file / swallowed-exception case.

The Protocol Review documents architecture and discrepancies; it does not authorize a new cross-institution workflow or claim unexecuted implementation as operational.
