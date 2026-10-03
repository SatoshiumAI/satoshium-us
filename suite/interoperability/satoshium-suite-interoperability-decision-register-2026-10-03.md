# Satoshium Suite — Interoperability Decision Register

**Date:** October 3, 2026  
**Review:** Satoshium Suite Interoperability Review  
**Step:** 23 — Produce Interoperability Decision Register  
**Status:** COMPLETE — APPROVED

---

## Purpose

This register consolidates the clarifications and implementation decisions made during the Satoshium Suite Interoperability Review.

Each entry is classified as either:

- **INHERITED** — a governing rule already settled during Suite Reconciliation and carried forward unchanged; or
- **NEW INTEROPERABILITY MECHANIC** — an implementation, exchange, serialization, propagation, validation, or handoff decision made during Interoperability Review without changing settled architecture.

The governing boundary remains:

> **INTEROPERABILITY REVIEW EXAMINES EXCHANGE MECHANICS; IT DOES NOT REOPEN SETTLED SUITE ARCHITECTURE.**

No decision in this register changes the institutional roster, role, canonical object, authority boundary, or settled lifecycle/relationship semantics of the Suite.

---

# 1. Inherited Architecture Decisions

## IDR-001 — Formal Suite Roster

**Origin:** INHERITED — Suite Reconciliation  
**Decision:** The formal Satoshium Suite consists of exactly eight institutions:

```text
Atlas
Navigator
Certifier
Registry
Chronicle
Anchor
Beacon
Attestor
```

**Interoperability Consequence:** All cross-institution mechanics must preserve these institutional identities.

**Status:** COMPLETE — APPROVED

---

## IDR-002 — Institutional Roles

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

```text
Atlas → Authoritative Intelligence
Navigator → Workflow Definition / Orchestration
Certifier → Operational Certification
Registry → Canonical Registration / Public Catalog
Chronicle → Historical Preservation
Anchor → Integrity Preservation
Beacon → Discovery & Signals
Attestor → Governed Attestation & Rule-Constrained Evaluation
```

**Interoperability Consequence:** Technical exchange may connect roles but may not merge or transfer them.

**Status:** COMPLETE — APPROVED

---

## IDR-003 — Canonical Objects

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

```text
Atlas → Jurisdiction Intelligence Package
Navigator → Navigator Workflow Definition
Certifier → Certification Package
Registry → Satoshium Registry Entry (SREG)
Chronicle → Chronicle Entry
Anchor → Integrity Reference
Beacon → Discovery Signal
Attestor → Attestation; Trust Statement
```

**Interoperability Consequence:** References, payloads, metadata, handoffs, logs, and exchange envelopes must not be mistaken for new canonical Suite objects.

**Status:** COMPLETE — APPROVED

---

## IDR-004 — Reference Does Not Transfer Authority

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

**Interoperability Consequence:** Referencing, routing, displaying, caching, indexing, discovering, registering, preserving, anchoring, or evaluating an object does not transfer source authority.

**Status:** COMPLETE — APPROVED

---

## IDR-005 — Identifier Distinction

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **IDENTIFIER ≠ AUTHORITY ≠ STATUS ≠ RELATIONSHIP.**

Matching numeric suffixes do not establish identity or relationship.

**Interoperability Consequence:** Full identifier family, institution, object type, and explicit relationship must be preserved.

**Status:** COMPLETE — APPROVED

---

## IDR-006 — Lifecycle / Publication Separation

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **CANONICAL CREATION ≠ LIFECYCLE ACTIVATION ≠ PUBLICATION.**

And:

> **CREATION DEFINES EXISTENCE. ACTIVATION DEFINES OPERATIVE STATE. PUBLICATION DEFINES ACCESSIBILITY.**

**Interoperability Consequence:** Machine exchange must preserve lifecycle and publication as separate semantic dimensions.

**Status:** COMPLETE — APPROVED

---

## IDR-007 — Correction / Version / Supersession Semantics

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **CORRECTIONS REPAIR. VERSIONS PRESERVE CONTINUITY. SUPERSESSION PRESERVES HISTORY. MATERIAL CHANGE MAY REQUIRE NEW IDENTITY.**

**Interoperability Consequence:** Downstream references may observe later state but may not silently rewrite historical state.

**Status:** COMPLETE — APPROVED

---

## IDR-008 — Changed Trust Conclusion

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **CHANGED CONCLUSION = CHANGED CANONICAL STATEMENT.**

A materially changed Trust Statement conclusion requires a new Trust Statement identity.

**Interoperability Consequence:** A prior TRST record cannot be silently mutated to express a different conclusion.

**Status:** COMPLETE — APPROVED

---

## IDR-009 — Relationship Vocabulary

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

```text
references
derived-from
supports
evaluates
results-in
supersedes
corrects
related-to
```

**Interoperability Consequence:** Machine serialization must preserve these distinct semantics.

**Status:** COMPLETE — APPROVED

---

## IDR-010 — Weak Fallback Relationship

**Origin:** INHERITED — Suite Reconciliation  
**Decision:** `related-to` is a weak fallback and must not replace a stronger governed relationship.

**Interoperability Consequence:** Exact relationships must be preserved when known.

**Status:** COMPLETE — APPROVED

---

## IDR-011 — Unknown-State Guardrails

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

```text
UNKNOWN ≠ SUCCESS
NOT-TESTED ≠ PASS
```

**Interoperability Consequence:** Unknown/unavailable conditions must remain explicit.

**Status:** COMPLETE — APPROVED

---

## IDR-012 — Conceptual Sequence vs Mandatory Pipeline

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **CONCEPTUAL SEQUENCE ≠ MANDATORY PIPELINE.**

**Interoperability Consequence:** A workflow or exercised production sequence does not become universal Suite dependency architecture.

**Status:** COMPLETE — APPROVED

---

## IDR-013 — Navigator Authority Boundary

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **ORCHESTRATION ≠ AUTHORITY.**

Navigator coordinates institutional action but does not inherit the institutional authority of participating systems.

**Status:** COMPLETE — APPROVED

---

## IDR-014 — Registry Four-Layer Model

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

```text
Registry
→ Registry Entry (SREG)
→ Registry Record Type
→ Source Record
```

**Interoperability Consequence:** Registration never converts the Source Record into a Registry-owned source object.

**Status:** COMPLETE — APPROVED

---

## IDR-015 — Beacon Canonical Boundary

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

```text
Discovery Signal → canonical Beacon object
Discovery Metadata → supporting structure
```

**Status:** COMPLETE — APPROVED

---

## IDR-016 — Attestor Bounded Authority

**Origin:** INHERITED — Suite Reconciliation  
**Decision:**

> **ATTESTOR DOES NOT DETERMINE UNIVERSAL TRUTH OR ASSIGN UNIVERSAL TRUST.**

Attestor produces governed, bounded Trust Statements through rule-constrained evaluation.

**Status:** COMPLETE — APPROVED

---

## IDR-017 — Chronicle Historical Authority

**Origin:** INHERITED — Suite Reconciliation  
**Decision:** Chronicle remains the Suite's historical-preservation institution.

**Interoperability Consequence:** Logs, workflow traces, provenance records, and version histories in other institutions do not become Chronicle authority.

**Status:** COMPLETE — APPROVED

---

# 2. New Interoperability Mechanics — Reference & Serialization

## IDR-018 — Cross-Institution Reference Envelope

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 4  
**Decision:** Cross-institution references should preserve a minimum semantic envelope:

```text
identifier
source institution
object type
version where material
lifecycle state where declared
publication state where declared
provenance
relationship type
authority context
accessibility
```

**Status:** COMPLETE — APPROVED

---

## IDR-019 — Reference Envelope Is Non-Canonical

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 4  
**Decision:** The interoperability reference envelope is infrastructure, not a new canonical Suite object.

**Status:** COMPLETE — APPROVED

---

## IDR-020 — Semantic Compatibility Over Identical Serialization

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 5  
**Decision:**

> **SEMANTIC COMPATIBILITY ≠ IDENTICAL SERIALIZATION.**

Institutions may use different schemas, formats, nesting, and field names if shared concepts preserve compatible meaning.

**Status:** COMPLETE — APPROVED

---

## IDR-021 — Shared Semantic Field Set

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 5  
**Decision:** Cross-institution exchange should preserve compatible meaning for:

```text
identifier
source institution
object type
timestamp
version
lifecycle state
publication state
relationship type
provenance
source reference
authority context
controlled outcome
accessibility
```

**Status:** COMPLETE — APPROVED

---

## IDR-022 — Timestamp Event Meaning

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 5  
**Decision:** Timestamps must preserve event meaning.

Preferred semantic model:

```text
timestamp
+ event type
+ timezone/offset where available
```

or explicit fields such as `observed_at`, `published_at`, `evaluated_at`.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-023 — Controlled Outcome Namespacing

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 5  
**Decision:** Certification outcomes, verification results, validation results, review outcomes, evaluation outcomes, and Trust Statements must remain institutionally typed/namespaced.

A generic `status` field must not erase institutional meaning.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

# 3. New Interoperability Mechanics — Relationship Serialization

## IDR-024 — Explicit Relationship Direction

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 6  
**Decision:** Machine relationships use:

```text
SUBJECT
→ RELATIONSHIP
→ OBJECT
```

Direction must be preserved.

**Status:** COMPLETE — APPROVED

---

## IDR-025 — Strongest Correct Relationship

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 6  
**Decision:**

> **USE THE STRONGEST CORRECT GOVERNED RELATIONSHIP ACTUALLY SUPPORTED BY THE ARCHITECTURE AND EVIDENCE.**

**Status:** COMPLETE — APPROVED

---

## IDR-026 — `supports` Direction Convention

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 6  
**Decision:**

```text
supporting object
→ supports
→ supported object / assertion
```

**Classification:** CLARIFICATION  
**Status:** COMPLETE — APPROVED

---

## IDR-027 — Unsupported Relationship Handling

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 6  
**Decision:** Unknown/unsupported relationship tokens must be preserved explicitly and must not silently degrade to `related-to`.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-028 — Multiple Relationships Between Same Objects

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 6  
**Decision:** If multiple relationship types are independently true, each should be serialized separately.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

# 4. New Interoperability Mechanics — State, Version & Correction Propagation

## IDR-029 — State-at-Use vs Later State

**Origin:** NEW INTEROPERABILITY MECHANIC formalizing inherited distinction — Step 7  
**Decision:**

> **SOURCE STATE AT USE ≠ LATER SOURCE STATE.**

Both should remain reconstructable when material.

**Status:** COMPLETE — APPROVED

---

## IDR-030 — No Automatic Downstream Mutation

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 7  
**Decision:**

> **SOURCE CHANGE DOES NOT AUTOMATICALLY MUTATE DOWNSTREAM CANONICAL OBJECTS.**

The receiving institution independently determines its response.

**Status:** COMPLETE — APPROVED

---

## IDR-031 — Downstream Action Vocabulary

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 7  
**Decision:** Downstream source-change handling may be classified as:

```text
observe
store
refresh
republish
flag
ignore
```

with institution-specific governed consequences.

**Status:** COMPLETE — APPROVED

---

## IDR-032 — Current-State Refresh vs Historical Rewrite

**Origin:** NEW INTEROPERABILITY MECHANIC — Steps 7–8  
**Decision:**

> **CURRENT-STATE REFRESH ≠ HISTORICAL REFERENCE REWRITE.**

**Status:** COMPLETE — APPROVED

---

## IDR-033 — Historical Reference Mutation Prohibited

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 8  
**Decision:** Downstream institutions must not silently replace historical identifiers, versions, states, or conclusions with later values.

**Status:** COMPLETE — APPROVED

---

# 5. New Interoperability Mechanics — Navigator Handoffs

## IDR-034 — Navigator Handoff Contract

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 9  
**Decision:** Navigator handoffs should preserve:

```text
workflow definition
workflow execution context
handoff identifier
sending step
receiving institution
requested action
input references
input provenance
authority context
preconditions
expected output
completion criteria
failure model
retry policy
timeout/unavailable policy
unknown-state handling
timestamp
traceability context
```

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-035 — Workflow State Separation

**Origin:** INHERITED architecture, applied as interoperability mechanic — Step 9  
**Decision:**

> **WORKFLOW STATE ≠ CANONICAL INSTITUTIONAL STATE.**

**Status:** COMPLETE — APPROVED

---

## IDR-036 — Workflow Failure Separation

**Origin:** INHERITED architecture, applied as interoperability mechanic — Step 9  
**Decision:**

> **WORKFLOW FAILURE ≠ INSTITUTIONAL FAILURE.**

**Status:** COMPLETE — APPROVED

---

## IDR-037 — Retry Traceability

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 9  
**Decision:** Retries must preserve prior attempt, reason, input version/state, timestamps, and whether input changed.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

# 6. New Interoperability Mechanics — Registry & Beacon Exchange

## IDR-038 — Registry Source/Object Separation in Exchange

**Origin:** INHERITED architecture, confirmed operationally — Step 10  
**Decision:**

> **REGISTRY OWNS THE SREG. THE SOURCE INSTITUTION OWNS THE SOURCE RECORD.**

**Status:** COMPLETE — APPROVED

---

## IDR-039 — Source Version vs SREG Version

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 10  
**Decision:**

> **SOURCE VERSION ≠ REGISTRY VERSION.**

Each must be carried independently.

**Status:** COMPLETE — APPROVED

---

## IDR-040 — Registry Lifecycle/Publication Label Correction

**Origin:** NEW INTEROPERABILITY CLARIFICATION — Steps 3 and 10  
**Decision:** `SREG-2026-0001` currently exposes a field-label inconsistency where `Registry Lifecycle State` is shown as `Published`.

Under settled architecture, lifecycle and publication must remain distinct.

**Classification:** CLARIFICATION  
**Status:** OPEN FOR DOCUMENTATION CORRECTION; architecture unaffected.

---

## IDR-041 — Beacon Direct vs Contextual Provenance

**Origin:** NEW INTEROPERABILITY CLARIFICATION — Steps 11 and 19  
**Decision:** Beacon must distinguish:

```text
primary/direct observed source
from
related contextual Suite objects
```

For `BEAC-2026-0001`, `SC-CERT-2026-0001` is the direct source; SREG/CHR/ANCH are contextual references.

**Classification:** CLARIFICATION  
**Status:** COMPLETE — APPROVED

---

## IDR-042 — Re-Observation Does Not Rewrite Original Observation

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 11  
**Decision:** Later Beacon re-observation adds later state and may support versioning/supersession/resolution, but does not rewrite the original observation.

**Status:** COMPLETE — APPROVED

---

# 7. New Interoperability Mechanics — Attestor Ingestion

## IDR-043 — Governed Input Eligibility Standard

**Origin:** NEW INTEROPERABILITY MECHANIC refining Attestor architecture — Step 12  
**Decision:** A potential input becomes eligible only when Attestor can establish, as applicable:

```text
governed identity
material relevance
traceable provenance
authority context
scope compatibility
relevant time/state
sufficient integrity/resolvability/reviewability
rule admissibility
```

**Status:** COMPLETE — APPROVED

---

## IDR-044 — Availability / Authority / Reference Do Not Equal Eligibility

**Origin:** NEW INTEROPERABILITY CLARIFICATION — Step 12  
**Decision:**

```text
Availability ≠ Eligibility
Authority ≠ Eligibility
Reference ≠ Eligibility
Public ≠ Eligibility
```

**Status:** COMPLETE — APPROVED

---

## IDR-045 — Five-Layer Attestor Separation

**Origin:** INHERITED distinctions, operationally consolidated — Step 12  
**Decision:**

```text
Validation
≠ Eligibility
≠ Conformance
≠ Evaluation Outcome
≠ Trust Statement
```

**Status:** COMPLETE — APPROVED

---

# 8. New Interoperability Mechanics — Validation & Failure Handling

## IDR-046 — Five-Layer Cross-Boundary Validation Model

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 13  
**Decision:**

```text
Source-Object Validity
→ Reference Validity
→ Schema / Contract Conformity
→ Receiving-Institution Eligibility
→ Receiving-Institution Evaluation
```

Each is a separate question.

**Status:** COMPLETE — APPROVED

---

## IDR-047 — Invalidity Is Purpose-Bounded

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 13  
**Decision:** An object invalid for one operational purpose may still be usable for another bounded purpose, such as historical preservation.

**Status:** COMPLETE — APPROVED

---

## IDR-048 — Unsupported Is Not Invalid

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 13  
**Decision:** Unsupported schema/profile/value/relationship must not be reclassified as source-object invalidity.

**Status:** COMPLETE — APPROVED

---

## IDR-049 — Failure-State Vocabulary

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 14  
**Decision:** Interoperability implementations should support explicit failure/uncertainty categories including:

```text
missing-source
broken-reference
stale-version
unpublished
withdrawn
unresolved-identifier
malformed-payload
contradictory-metadata
institution-unavailable
unknown-relationship
unsupported
timeout
partial-response
unknown
```

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-050 — Last-Known-State Rule

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 14  
**Decision:** A prior known state may be preserved as `last_known_state`, but may not be relabeled as current when current state is unknown.

**Status:** COMPLETE — APPROVED

---

## IDR-051 — Contradictory Metadata Rule

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 14  
**Decision:** Conflicting material metadata must be preserved and flagged; a favorable value must not be selected silently.

**Status:** COMPLETE — APPROVED

---

# 9. New Interoperability Mechanics — Historical Traceability

## IDR-052 — Minimum Historical Reconstruction Model

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 15  
**Decision:** A material cross-institution exchange should remain reconstructable from:

```text
Referenced Object
Source
Version-at-Use
State-at-Use
Time
Relationship
Provenance
Receiving Context
Later Change
Downstream Response
```

**Status:** COMPLETE — APPROVED

---

## IDR-053 — Local Operational History vs Chronicle Authority

**Origin:** INHERITED Chronicle boundary, operationally clarified — Step 15  
**Decision:**

> **OPERATIONAL TRACEABILITY ≠ CHRONICLE AUTHORITY.**

And:

> **HISTORY PRESERVED LOCALLY ≠ CANONICAL HISTORICAL PRESERVATION.**

**Status:** COMPLETE — APPROVED

---

# 10. New Interoperability Mechanics — Compatibility Versioning

## IDR-054 — Separate Version Domains

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 16  
**Decision:**

```text
Canonical Object Version
≠ Schema Version
≠ Interface Version
≠ Interoperability Contract Version
≠ Profile Version
```

**Status:** COMPLETE — APPROVED

---

## IDR-055 — Compatibility Range Declaration

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 16  
**Decision:** Institutions should explicitly declare supported, deprecated, and incompatible schema/interface/contract versions.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-056 — Backward Compatibility Principle

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 16  
**Decision:** Non-breaking interface/schema evolution should preserve backward compatibility where practical.

**Status:** COMPLETE — APPROVED

---

## IDR-057 — Version Negotiation

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 16  
**Decision:** Where automated exchange exists, producer and consumer should negotiate the highest mutually supported compatible version.

No overlap means the exchange is unsupported, not silently coerced.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-058 — Unknown Version

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 16  
**Decision:**

> **UNKNOWN VERSION ≠ COMPATIBLE.**

**Status:** COMPLETE — APPROVED

---

# 11. New Interoperability Mechanics — Security, Authority & Trust

## IDR-059 — Technical Connectivity Boundary

**Origin:** NEW INTEROPERABILITY CONSOLIDATION — Step 17  
**Decision:**

> **TECHNICAL CONNECTIVITY DOES NOT OVERRIDE INSTITUTIONAL GOVERNANCE.**

**Status:** COMPLETE — APPROVED

---

## IDR-060 — Authorization vs Authority

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 17  
**Decision:**

> **AUTHORIZATION ≠ AUTHORITY.**

Technical permission to invoke or write does not grant substantive institutional authority.

**Status:** COMPLETE — APPROVED

---

## IDR-061 — Write-Capable Interface Controls

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 17  
**Decision:** Write-capable interfaces should preserve caller identity, requested action, authority context, target, resulting object, timestamp, and auditable approval/governance context where applicable.

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-062 — Trust Does Not Propagate by Reference

**Origin:** INHERITED trust boundary, applied to interoperability — Step 17  
**Decision:**

> **TRUST DOES NOT PROPAGATE BY REFERENCE.**

**Status:** COMPLETE — APPROVED

---

# 12. New Interoperability Mechanics — External Systems

## IDR-063 — External / Reference / Canonical Distinction

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 18  
**Decision:**

```text
External Source
≠ Suite Reference
≠ Suite Canonical Object
```

**Status:** COMPLETE — APPROVED

---

## IDR-064 — External Attribution Profile

**Origin:** NEW INTEROPERABILITY MECHANIC — Step 18  
**Decision:** External references should preserve, where applicable:

```text
external source name
external identifier
source organization
object type
version
state
canonical external reference
retrieved/observed time
provenance
relationship
authority context
limitations
accessibility
```

**Classification:** IMPLEMENTATION GAP  
**Status:** COMPLETE — APPROVED

---

## IDR-065 — Ingestion Does Not Canonicalize

**Origin:** NEW INTEROPERABILITY CLARIFICATION — Step 18  
**Decision:**

```text
INGESTION ≠ CANONICALIZATION
INDEXING ≠ CANONICALIZATION
CACHING ≠ CANONICALIZATION
REFERENCE ≠ CANONICALIZATION
```

**Status:** COMPLETE — APPROVED

---

# 13. New Interoperability Mechanics — Exercised Lineage

## IDR-066 — Exercised Sequence vs Provenance Graph

**Origin:** NEW INTEROPERABILITY CLARIFICATION — Step 19  
**Decision:** The shorthand:

```text
SC-CERT
→ SREG
→ CHR
→ ANCH
→ BEAC
→ ATT
→ TRST
```

is an **exercised production lineage / sequence**, not a literal serial provenance graph.

**Classification:** CLARIFICATION  
**Status:** COMPLETE — APPROVED

---

## IDR-067 — Production Provenance Precision

**Origin:** NEW INTEROPERABILITY CLARIFICATION — Step 19  
**Decision:**

```text
SC-CERT → SREG
= direct source/registration handoff

SREG → CHR
= relational/contextual; Certifier remains primary authoritative source

CHR → ANCH
= chronological sequence, not direct provenance

ANCH → BEAC
= contextual; Beacon directly observed Certifier

BEAC → ATT
= direct governed input, non-exclusive

ATT → TRST
= direct derivation
```

**Classification:** CLARIFICATION  
**Status:** COMPLETE — APPROVED

---

# 14. New Interoperability Mechanics — Adversarial Rules

## IDR-068 — Safe Degradation Under Ambiguity

**Origin:** NEW INTEROPERABILITY DETERMINATION — Step 20  
**Decision:** Composite ambiguity must degrade into explicit uncertainty rather than inferred identity, authority, validity, support, trust, or currentness.

**Status:** COMPLETE — APPROVED

---

## IDR-069 — Favorable-State Coercion Prohibited

**Origin:** NEW INTEROPERABILITY CONSOLIDATION — Step 20  
**Decision:** The following coercions are prohibited:

```text
unknown → PASS
unknown → VALID
unknown → SUPPORTED
unknown → TRUSTED
unknown → CURRENT
unavailable → invalid
superseded → deleted
published → active
active → published
valid reference → eligible
eligible → supported
conformant → trusted
```

**Status:** COMPLETE — APPROVED

---

# 15. Classification Decisions

## IDR-070 — PASS Is Dominant

**Origin:** NEW INTEROPERABILITY REVIEW DETERMINATION — Step 21  
**Decision:** Core interoperability architecture is sound.

**Status:** COMPLETE — APPROVED

---

## IDR-071 — Clarifications Are Non-Architectural

**Origin:** NEW INTEROPERABILITY REVIEW DETERMINATION — Step 21  
**Decision:** Clarifications identified during review are documentation/contract precision issues and do not reopen architecture.

**Status:** COMPLETE — APPROVED

---

## IDR-072 — Implementation Gaps Belong in Implementation Queue

**Origin:** NEW INTEROPERABILITY REVIEW DETERMINATION — Step 21  
**Decision:** Missing technical standardization/enforcement must be tracked as implementation work rather than architectural defects.

**Status:** COMPLETE — APPROVED

---

## IDR-073 — No Current Compatibility Issue

**Origin:** NEW INTEROPERABILITY REVIEW DETERMINATION — Step 21  
**Decision:**

> **NO CURRENT COMPATIBILITY ISSUE IDENTIFIED.**

Different schemas/formats do not constitute incompatibility where semantic mapping remains possible.

**Status:** COMPLETE — APPROVED

---

## IDR-074 — No Architectural Conflict

**Origin:** NEW INTEROPERABILITY REVIEW DETERMINATION — Step 21  
**Decision:**

> **NO ARCHITECTURAL CONFLICT IDENTIFIED.**

No settled Suite architecture decision requires reopening.

**Status:** COMPLETE — APPROVED

---

# 16. Consolidated Inheritance vs New-Mechanic Summary

## Inherited from Suite Reconciliation

The Interoperability Review inherits and does not redefine:

```text
formal institutional roster
institutional roles
canonical objects
identifier families
authority boundaries
REFERENCE DOES NOT TRANSFER AUTHORITY
relationship vocabulary
lifecycle/publication distinction
correction/version/supersession semantics
Changed Conclusion = Changed Canonical Statement
Navigator orchestration boundary
Registry four-layer model
Beacon canonical-object boundary
Attestor bounded trust authority
Chronicle historical-preservation authority
Conceptual Sequence ≠ Mandatory Pipeline
UNKNOWN ≠ SUCCESS
NOT-TESTED ≠ PASS
```

## Newly Decided Interoperability Mechanics

The review newly establishes or formalizes:

```text
cross-institution reference envelope
shared semantic field model
timestamp event semantics
controlled-outcome namespacing
relationship direction encoding
strongest-correct-relationship rule
unsupported relationship handling
source-state propagation model
no automatic downstream mutation
current-state refresh vs historical rewrite
Navigator handoff contract
retry / idempotency traceability
Registry source/version exchange behavior
Beacon direct vs contextual provenance handling
Attestor governed-input eligibility mechanics
cross-boundary validation sequence
failure-state vocabulary
last-known-state rule
historical reconstruction envelope
compatibility version domains/ranges
version negotiation
authorization vs authority
write-interface controls
external-source reference profile
external/source/reference/canonical separation
exercised-lineage vs provenance-graph distinction
safe degradation under ambiguity
finding classification discipline
```

---

# 17. Items Carried Forward

The following decisions are settled but require implementation or documentation work:

```text
1. Reference-resolution behavior for stale/unavailable/unresolved/superseded sources.
2. Reference-envelope required-field enforcement.
3. Timestamp normalization.
4. Lifecycle-state mapping.
5. Exact relationship predicate serialization.
6. Controlled-outcome namespacing.
7. `evaluates` and `results-in` machine profiles.
8. Unsupported and multi-relationship serialization.
9. Navigator handoff/retry/idempotency implementation.
10. Beacon exact machine property/predicate serialization.
11. Compatibility declarations and version negotiation.
12. Version-at-use pinning for contracts/schemas/profiles.
13. Technical authorization and write-audit controls.
14. External-source reference profile.
15. Registry `SREG-2026-0001` lifecycle/publication field-label correction.
16. Production expansion of deferred interaction families.
```

These should feed directly into the **Interoperability Implementation Queue**.

---

# Final Determination

The Interoperability Review did not redesign the Satoshium Suite.

It inherited the Suite's settled architecture and added the exchange mechanics necessary to preserve that architecture across institutional boundaries.

The decision hierarchy is therefore:

```text
Suite Reconciliation
→ defines institutional architecture

Interoperability Review
→ defines how that architecture exchanges, resolves, propagates, validates,
   fails, versions, traces, and interoperates
```

No interoperability mechanic in this register supersedes a Suite Reconciliation decision.

---

# FINAL DISPOSITION

# SATOSHIUM SUITE INTEROPERABILITY DECISION REGISTER — COMPLETE — APPROVED

Governing rule:

> **INHERITED ARCHITECTURE DEFINES WHAT THE INSTITUTIONS ARE. INTEROPERABILITY DECISIONS DEFINE HOW THOSE INSTITUTIONS EXCHANGE WITHOUT CHANGING WHAT THEY ARE.**
