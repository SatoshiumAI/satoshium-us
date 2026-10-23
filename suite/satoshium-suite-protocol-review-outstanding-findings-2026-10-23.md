# Satoshium Suite — Protocol Review Outstanding Findings & Disposition Register

**Date:** October 23, 2026  
**Branch reviewed:** `phase004`  
**Review:** Suite Protocol Review — cross-repository outstanding-findings reconciliation  
**Status:** COMPLETE — APPROVED (this register only); **Suite Protocol Review remains ACTIVE**  
**Governance baseline:** Satoshium Suite Reconciliation — COMPLETE — APPROVED (September 30, 2026); Suite Governance Review — COMPLETE — APPROVED (October 11, 2026; `GDR-2026-0026`)  
**Scope boundary:** Classify observed documentation, implementation, test, and deployment gaps without reopening the settled eight-institution architecture.

## Governing constraints

> **Authority follows the governed subject. Reference does not transfer authority.**

- The eight current formal Suite institutions remain Operational: Atlas, Navigator, Certifier, Registry, Chronicle, Anchor, Beacon, Attestor.
- Their independently governed canonical responsibilities are unchanged. Attestor owns **Attestation** and **Trust Statement**; Rule-Constrained Evaluation is a governed act, not a third canonical object.
- The inaugural exercised production lineage is production evidence, **not** a required sequence for future operations.
- Schema/field checks, Validation, Eligibility, substantive Evaluation, Conformance, lifecycle activation, and Publication are not interchangeable.
- Historical repository documents may be preserved with dated notices; they must not be rewritten to misrepresent the historical state.
- Do not treat a successful documentation correction or a repository entry-point addition as evidence of a successful deployed route or runtime test.

## 1. Disposition definitions

| Disposition | Meaning |
|---|---|
| **RESOLVED — VERIFIED** | Corrected in `phase004` and re-fetched; repository-level proof only |
| **CONFIRM — PASS** | Reviewed material preserves the approved boundaries; no modification required |
| **DEFERRED — IMPLEMENTATION** | Requires separately specified/tested executable work |
| **OPEN — DEPLOYMENT VERIFICATION** | Repository-level change exists; live route/hosting behavior not proven |
| **OPEN — COVERAGE** | Additional review or implementation coverage must be explicitly assessed |
| **NOT AN ARCHITECTURAL CHANGE** | Within settled institutional roles, canonical ownership, and constitutional boundaries |

A status listed here is not a substitute for each source artifact's own verification and approvals.

## 2. Repository-level corrections verified during this Protocol Review

The October 23 review made bounded, individually committed corrections to reviewed Certifier, Registry, Chronicle, Anchor, Beacon, Attestor, and Suite Standards surfaces. Major verified classes included:

1. **Production-state alignment:** Older Chronicle and Anchor documentation still described completed first production as prospective.
2. **Canonical responsibility:** Some Attestor status, schemas, validation, lifecycle, publication, production, and related standards documents named only `Trust Statement`; they were aligned to **Attestation + Trust Statement**.
3. **Source vs Evidence:** Chronicle's `source-record-schema.md` was an accidental duplicate of the Evidence Record Schema; its distinct historical source version was restored with a provenance notice.
4. **Standards vs institutional decisions:** Registry Validation/Publication and Suite Evidence/Scoring standards language was bounded to avoid false authorization or trust claims.
5. **Relationship meaning:** Registry derived relationship assertions were clarified so they do not imply canonical derivation, substantive support, or authority transfer.
6. **Historical candidate profiles:** Attestor `evidence` and `source-provenance` Type adoption was distinguished from the provisional state of old specialized profile documents.
7. **Repository HTML entry points:** `attestor/publication/index.html` added alongside existing `index.htm`; `attestor/generation/index.html` added matching the established canonical Generation URL while retaining `attestor/attestation-generation/index.html`.
8. **Legacy Certifier toolkit disclosure:** The executable toolkit's `SCHR`, `SATR`, mandatory-stub-looking local checklist, public page, and v0.1 manifest were explicitly labeled as historical/local support contracts rather than current Suite-issued downstream records.
9. **Toolkit migration assessment:** `certifier/tools/ops-toolkit/docs/protocol-migration-assessment-2026-10-23.md` created and cross-linked. Its assessment is COMPLETE — APPROVED; executable migration is **not performed**.

Individual commits and modified-file verification are preserved in the repository's `phase004` commit history. This register does not reclassify any previously approved governance or reconciliation decision.

## 3. Outstanding Protocol Review items

### PR-OPEN-001 — Certifier toolkit protocol migration

**Disposition:** DEFERRED — IMPLEMENTATION.  
**Evidence:** `certifier/tools/ops-toolkit/src/generator.py`, `src/models.py`, `src/checklist.py`, tests, fixtures, and the October 23 migration assessment.  
**Problem:** Legacy `SCHR`/`SATR` request formats and a 13-file completeness contract cannot be treated as current CHR/ATT/TRST creation or mandatory downstream publication.  
**Gate:** Define adopted, institution-owned request interfaces where they exist; explicitly separate local artifact completeness from certification/publication and optional inter-institutional handoffs; version and regression-test the migrated implementation.  
**Current production impact:** Does **not** revoke the distinct production proof already established by institutions.

### PR-OPEN-002 — Certifier checklist unreadable-file path

**Disposition:** DEFERRED — IMPLEMENTATION / TEST.  
**Evidence:** `certifier/tools/ops-toolkit/src/checklist.py` catches and ignores file-read exceptions inside `check_for_placeholders()`.  
**Problem:** A present but unreadable file can fail to produce a placeholder warning without an explicit read error.  
**Gate:** Fail closed with a regression test; preserve accurate CLI exit and summary behavior.  
**Status limitation:** Static-code finding; no assertion that a production file was unreadable.

### PR-OPEN-003 — Attestor canonical Generation URL deployment

**Disposition:** OPEN — DEPLOYMENT VERIFICATION.  
**Evidence:** `attestor/generation/index.html` now matches the canonical URL declared by the existing page; legacy `attestor/attestation-generation/index.html` remains.  
**Gate:** Independently verify served HTTPS status, canonical URL, page content, and any necessary legacy-route behavior after deployment.  
**Do not assume:** Creating a repository entry point proves successful deployment, redirect, or Cloudflare routing.

### PR-OPEN-004 — Attestor Publication route deployment

**Disposition:** OPEN — DEPLOYMENT VERIFICATION.  
**Evidence:** `attestor/publication/index.html` was added as an identical copy of the former `index.htm`.  
**Gate:** Verify the directory URL resolves to the governed public page after deployment.  
**Do not assume:** Repository file parity guarantees publicly served response behavior.

### PR-OPEN-005 — Specialized Attestor Attestation Type profiles

**Disposition:** OPEN — COVERAGE / FUTURE PROFILE IMPLEMENTATION.  
**Evidence:** `attestor/schemas/source-attestation-schema.md` and `evidence-attestation-schema.md` retain their foundational candidate field/semantic designs with October 23 notices.  
**Gate:** Profile-specific normative reconciliation, adopted controlled values, machine contract, validation, conformance, and production tests before specialized executable profile claims.  
**Boundary:** `evidence` and `source-provenance` Attestation Types are adopted, but Type adoption is **not** proof of every specialized candidate profile.

### PR-OPEN-006 — Generalized automated Suite interoperability

**Disposition:** DEFERRED — IMPLEMENTATION; retain the existing approved queue **without duplicating or falsely closing it**.  
**Authoritative source:** `suite/interoperability/satoshium-suite-interoperability-implementation-queue-2026-10-03.md`.  
**Existing queue:** **23 items**: **11 P0**, **8 P1**, **4 P2**.  
**P0 meaning:** Controls required **before relying on generalized automated cross-institution production exchange**; not retrospective failures of the limited exercised production lineage.  
**Gate:** Implement and test the relevant queued identity, reference, state, relationship, failure, handoff, authorization, and write-audit controls before general automated reliance.  
**Boundary:** Implementation executes settled architecture; it does not redefine it.

## 4. Suite 1.0 readiness — carefully scoped

**Already established:** all eight institutions Operational; documented and production-exercised canonical object responsibilities; completed September 30 Suite Reconciliation and October 11 Suite Governance Review; bounded first-production evidence.

**Not established by this Protocol Review alone:** that all generalized automated interoperability P0 controls are implemented, all optional profile combinations exercised, both newly supplied repository routes actually live, or the Certifier toolkit migrated.

**Release decision:** Do **not** pronounce all implementation or deployment gaps closed. Whether a particular gap blocks the intended *Suite 1.0 release* depends on the release's explicitly approved functional scope and acceptance criteria. The October 3 P0 classification specifically blocks **generalized automated cross-institution reliance**, not necessarily a release limited to the already exercised institutional scope.

## 5. Recommended next review gates

1. **Verify deployment** for Attestor Generation and Publication routes, without rewriting canonical records.
2. **Compare any further Protocol Review findings against existing IQ-001–IQ-023** before opening an additional implementation work item.
3. **Run bounded consistency sweep** over remaining current-state route, identifier, canonical ownership, and production assertion surfaces; preserve historical materials.
4. **Separate release scope from future platform aspirations.** Define which capabilities Suite 1.0 promises and test those specific gates.
5. **Carry PR-OPEN-001–006 forward** with owner, evidence, actual test results, and disposition changes only when supported.

## Final disposition of this register

**OUTSTANDING-FINDINGS RECONCILIATION REGISTER — COMPLETE — APPROVED (October 23, 2026).**  
**SUITE PROTOCOL REVIEW — ACTIVE.**  
**ARCHITECTURAL CHANGE FOUND IN THESE REVIEWED ITEMS — NONE.**  
**OPEN IMPLEMENTATION / DEPLOYMENT / COVERAGE ITEMS — EXPLICITLY PRESERVED, NOT CLAIMED COMPLETE.**

> **Implement what the architecture requires. Do not redesign the architecture while implementing it.**
