# Satoshium Suite Reconciliation — Documentation Correction Register

**Date:** September 28, 2026  
**Phase:** IV-A — Documentation Conformance Audit  
**Register Status:** ACTIVE  
**Scope:** Current-state Suite documentation corrections identified during reconciliation

---

## Purpose

This register records documentation discrepancies identified while comparing current Suite documentation against the reconciled Friday–Sunday architecture.

The purpose is to avoid an unnecessary repository-wide rewrite.

Only documentation issues that are:

- current-state;
- materially stale, contradictory, or misleading; and
- relevant to the reconciled Suite architecture

are entered here.

Historical material remains preserved when historically accurate.

---

## Classification

Each discrepancy is assigned one of four dispositions:

- **CORRECT NOW** — straightforward documentation correction supported by settled architecture;
- **INTEROPERABILITY REVIEW** — cross-institution issue requiring later dedicated interoperability review;
- **LATER DOCUMENTATION RECONCILIATION** — valid documentation issue outside the current light-day scope;
- **HISTORICAL — PRESERVE** — historically accurate material that should not be rewritten merely because the architecture later matured.

---

## Correction Register

| ID | Surface | Issue | Classification | Disposition |
|---|---|---|---|---|
| DCR-001 | `/suite/` / U.S. operational entry surface | Current-state Atlas wording used “jurisdiction record” / “jurisdiction intelligence record” in places where the formal Atlas canonical object is now the **Jurisdiction Intelligence Package**. | CORRECT NOW | Correct current-state terminology; preserve historical references where accurate. |
| DCR-002 | `/suite/status/` | Status documentation counted **Aegis** within the formal Suite roster and reported nine operational institutions. Reconciled architecture establishes exactly **8 formal Suite institutions**, all Operational; Aegis remains **external / pre-Suite**. | CORRECT NOW | Corrected. |
| DCR-003 | `/suite/methodology/` | Methodology documentation used generalized **scoring** language that could imply Suite-wide scoring authority. No generalized Suite-wide scoring authority exists under the reconciled architecture. | CORRECT NOW | Corrected. |
| DCR-004 | `/suite/methodology/` | Wording implied Certifier retained authority over “certification methodology” in a way that could conflict with Suite Methodology ownership. | CORRECT NOW | Corrected to distinguish shared Suite Methodology from Certifier's institution-specific certification procedures and decisions. |
| DCR-005 | `/atlas/` | Landing documentation described Atlas primarily as a “jurisdiction intelligence layer” / repository and continued to use record-centric terminology inconsistent with the reconciled canonical object model. | CORRECT NOW | Corrected to **Authoritative Intelligence** and **Jurisdiction Intelligence Package** framing. |
| DCR-006 | `/atlas/` | Relationship text used role shorthand such as “Certifier verifies,” “Anchor preserves trust references,” and “Attestor proves,” which conflicted with reconciled institutional roles and authority boundaries. | CORRECT NOW | Corrected to the formal eight-institution role model. |
| DCR-007 | `/navigator/` | Landing and README documentation still framed Navigator primarily as a query/exploration layer rather than the formal institution for **Workflow Definition / Orchestration**. | CORRECT NOW | Corrected. |
| DCR-008 | `/navigator/` | README displayed the institutions as a linear Atlas → Navigator → Certifier → Registry → Chronicle → Anchor → Beacon → Attestor sequence, risking interpretation as a mandatory Suite pipeline. | CORRECT NOW | Corrected to role-based institutional relationships and explicit non-mandatory pipeline language. |
| DCR-009 | `/navigator/` | Canonical object ownership was not clearly stated on principal documentation. | CORRECT NOW | Corrected to identify **Navigator Workflow Definition** as canonical object and **Workflow Orchestration** as function. |
| DCR-010 | `/registry/` | Current examples still referred to an “Atlas canonical jurisdiction record” and a “Chronicle historical event” rather than the reconciled canonical object terminology. | CORRECT NOW | Corrected to **Atlas Jurisdiction Intelligence Package** and **Chronicle Entry**. |
| DCR-011 | `/registry/` | Suite relationship descriptions said Chronicle “creates historical events,” Beacon “creates signals and discovery metadata,” and Navigator merely “coordinates workflows,” which did not match reconciled object ownership and role language. | CORRECT NOW | Corrected. |
| DCR-012 | `/registry/README.md` | README retained stale development priorities and language describing Registry as preparing for operational completion, despite Registry already being Operational. | CORRECT NOW | Corrected to current operational posture. |
| DCR-013 | `/beacon/` | Landing and README still stated **Continuing Development**, **Operational → No**, and pending production proof after Beacon had already achieved Operational status. | CORRECT NOW | Corrected to **Operational · September 2026** and completed production proof / post-operation review. |
| DCR-014 | `/beacon/` | Current-state documentation treated Discovery Metadata too closely to canonical responsibility in some wording. Reconciled architecture defines **Discovery Signal** as the canonical Beacon object; Discovery Metadata is supporting structure. | CORRECT NOW | Principal landing documentation aligned; deeper residual usage to be corrected only where it creates current-state ambiguity. |
| DCR-015 | Historical Updates / journals / production narratives | Earlier references to Beacon or Attestor as Continuing Development, earlier Suite operational counts, and historical Atlas “Jurisdiction Record” naming accurately describe the state at that time. | HISTORICAL — PRESERVE | Do not rewrite merely to match later architecture. |
| DCR-016 | Historical Suite formation material | Earlier June-era text that grouped Aegis with emerging Suite architecture reflects pre-reconciliation history. | HISTORICAL — PRESERVE | Preserve historical record; current-state surfaces must keep Aegis external / pre-Suite. |
| DCR-017 | Cross-institution relationship pages | Some deeper pages may still use legacy relationship shorthand, broad “trust signal” terminology, or role descriptions predating the final relationship vocabulary. | INTEROPERABILITY REVIEW | Defer to dedicated Interoperability Review unless a current-state contradiction is discovered during present reconciliation. |
| DCR-018 | Remaining non-principal repository documentation | Additional stale wording may remain in lower-level docs that was not necessary to inspect during the principal landing/status/methodology review. | LATER DOCUMENTATION RECONCILIATION | Do not perform a giant repository rewrite during Phase IV-A. |

---

## Corrections Completed During Phase IV-A

The following current-state documentation surfaces were corrected during this audit:

```text
/suite/status/index.html
/suite/status/README.md

/suite/methodology/index.html
/suite/methodology/README.md

/atlas/index.html
/atlas/README.md

/navigator/index.html
/navigator/README.md

/registry/index.html
/registry/README.md

/beacon/index.html
/beacon/README.md
```

Principal landing documentation for:

```text
Certifier
Chronicle
Anchor
Attestor
```

passed the current reconciliation review without requiring correction.

---

## Governing Documentation Rule

```text
Correct stale current-state documentation.
Preserve accurate historical documentation.
Do not redesign architecture through documentation cleanup.
Do not rewrite the entire repository merely because terminology matured.
```

The Documentation Correction Register is the control mechanism for remaining discrepancies.

---

## Current Disposition

```text
Documentation Correction Register
→ CREATED

Straightforward current-state corrections identified to date
→ RECORDED

Principal corrections completed during Phase IV-A
→ COMPLETE

Repository-wide rewrite
→ NOT AUTHORIZED / NOT REQUIRED

Historical preservation discipline
→ MAINTAIN

Interoperability issues
→ DEFER TO INTEROPERABILITY REVIEW

Remaining lower-level documentation drift
→ TRACK, DO NOT EXPAND SCOPE
```

**Disposition:** COMPLETE — APPROVED
