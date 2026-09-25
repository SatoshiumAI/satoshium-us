# Satoshium Suite Reconciliation — Deferred Issues Register

**Date:** September 25, 2026  
**Phase:** Phase I — Establish the Reconciliation Baseline  
**Step:** 4  
**Status:** Proposed for Approval  
**Purpose:** Assemble previously reserved Suite-level issues before institutional reconciliation begins.

---

## 1. Purpose of This Register

This register collects previously reserved or explicitly deferred questions that may require resolution during the September 25–30, 2026 Satoshium Suite Reconciliation.

It does **not** resolve those questions.

It exists to ensure that no known Suite-level issue is silently lost, prematurely answered, or allowed to drift into the later Interoperability Review or broader Satoshium Universe Documentation Reconciliation.

Each item is therefore recorded as an issue to be examined at the appropriate scheduled phase.

---

## 2. Governing Scope Rule

An issue belongs in this register when it concerns one or more of the following:

- formal Suite institutional roles;
- canonical responsibility;
- authority boundaries;
- canonical object ownership;
- Suite terminology;
- lifecycle or publication semantics;
- relationship semantics;
- Suite conceptual architecture;
- legacy architecture that conflicts with the current operational institutional architecture.

Issues primarily concerning interfaces, exchange mechanics, implementation handoffs, compatibility, or detailed cross-institution technical behavior belong to the later **Interoperability Review**.

Issues that concern the broader Satoshium Universe rather than the formal Suite belong to the later **Satoshium Universe Documentation Reconciliation**.

---

# ACTIVE DEFERRED ISSUES

## DI-001 — `SYS-*` System Registry vs Formal Satoshium Registry

**Issue:**  
Determine the enduring relationship, if any, between the legacy `SYS-*` System Registry architecture and the formal Satoshium Registry / Satoshium Registry Record architecture.

**Known Background:**  
Earlier Satoshium architecture used `SYS-*` identifiers as a System Registry mechanism for systems, layers, deployment status, namespace stability, and related architectural classification.

The mature Suite now has a formal Registry institution whose canonical responsibility is the **Satoshium Registry Record**.

**Question to Reconcile:**  
Are these:

- the same architecture under different maturity stages;
- separate registries with different jurisdictions;
- a legacy architecture that should be retired from current-state usage;
- or another explicitly defined relationship?

**Do Not Assume:**  
Do not merge `SYS-*` into the formal Registry merely because both use the word “Registry.”

**Scheduled Review:** Friday — Phase I

**Status:** OPEN

---

## DI-002 — Legacy Suite Layer Models vs Operational Institutional Architecture

**Issue:**  
Determine whether older Satoshium layer models remain current architecture, historical explanatory models, partial conceptual models, or obsolete current-state descriptions.

**Known Legacy Models Include:**  

- Trust → Knowledge → Intelligence → Signal → Simulation
- variants including Interface
- variants using Canon / Trust / Signal / Agent / Interface
- other fixed-domain or layer-based descriptions predating the mature eight-institution Suite

**Question to Reconcile:**  
Do these models describe the current Suite, describe only an earlier architecture, or remain valid only for a narrower conceptual purpose?

**Scheduled Review:** Friday — Phase I

**Status:** OPEN

---

## DI-003 — Institutional Role and Authority Overlap

**Issue:**  
Determine whether any two Suite institutions appear to own the same authority or canonical responsibility.

**Institutions Requiring Explicit Boundary Review Include:**

- Atlas
- Navigator
- Certifier
- Registry
- Chronicle
- Anchor
- Beacon
- Attestor

**Core Test:**  
No institution should gain authority over another institution’s canonical object merely because it references, consumes, publishes, discovers, evaluates, or records it.

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-004 — Canonical Object Ownership

**Issue:**  
Reconcile ownership boundaries among institutional canonical objects and distinguish the object owned by an institution from records that reference or catalog that object.

**Known Example:**  
A Registry-owned Satoshium Registry Record may catalog or reference a source object owned by Atlas, Certifier, Attestor, or another institution without transferring ownership.

**Questions to Reconcile:**

- What does each institution canonically create?
- What does each institution merely reference?
- What does Registry register versus create?
- What is the distinction between a Registry identifier and a source-system identifier?
- Does any legacy documentation blur object ownership?

**Scheduled Review:** Friday–Saturday

**Status:** OPEN

---

## DI-005 — Registry Authority vs Source-Institution Authority

**Issue:**  
Clarify the authority relationship between Registry and the institutions that own source records.

**Core Question:**  
Can Registry appear to become authoritative for the content, state, or meaning of the object it registers?

**Constraint:**  
Registration must not silently transfer source authority.

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-006 — Chronicle Record Authority vs State Authority

**Issue:**  
Clarify whether Chronicle documentation ever implies that recording an event gives Chronicle authority over the state or lifecycle of the object being recorded.

**Core Question:**  
Can Chronicle appear to control the state it records?

**Constraint:**  
Recording an event and controlling the underlying institutional state must remain distinct.

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-007 — Anchor Integrity Authority vs Certification / Verification Authority

**Issue:**  
Clarify whether any current or legacy documentation makes Anchor appear to certify, verify, validate, or otherwise determine institutional truth beyond its integrity responsibility.

**Core Question:**  
Can Anchor appear to certify something merely because it establishes or preserves an integrity reference?

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-008 — Beacon Discovery Authority vs Verification Authority

**Issue:**  
Clarify whether Beacon’s discovery and signaling language ever implies verification, validation, certification, truth determination, or source authority.

**Core Question:**  
Can Beacon appear to verify something merely because it exposes a discovery signal or discovery metadata?

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-009 — Navigator Orchestration vs Outcome Ownership

**Issue:**  
Clarify the boundary between workflow definition/orchestration and ownership of institutional outcomes.

**Core Question:**  
Can Navigator appear to own, determine, or authorize the substantive outcomes produced by other institutions?

**Constraint:**  
Orchestration must not silently become institutional outcome authority.

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-010 — Certifier Trust / Confidence Language vs Attestor Trust Statements

**Issue:**  
Reconcile legacy Certifier language involving “trust,” “reviewable trust,” Trust Model, Trust pages, confidence concepts, or similar terms with mature Attestor architecture.

**Questions to Reconcile:**

- What remains valid Certifier terminology?
- What belongs specifically to Attestor?
- Does any “Trust Standard” terminology conflict with Attestor Trust Statements?
- Does Certifier language imply authority now owned by Attestor?
- Are Atlas “trust dimensions” conceptually distinct or terminologically colliding?

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-011 — Truth / Trust / Trust Standard / Scoring Terminology

**Issue:**  
Review legacy Truth, Trust, Trust Standard, trust-assessment, trust-signal, and scoring terminology where it intersects the mature Suite.

**Questions to Reconcile:**

- Does “truth” imply authority the Suite does not claim?
- Does “trust” refer to confidence, evidence, evaluation, attestation, or a governed Trust Statement?
- Are trust scores still architecturally valid?
- Are “trust signals” confused with Beacon discovery signals?
- Are legacy terms historical, current, or obsolete?

**Constraint:**  
Attestor does not determine universal truth.

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-012 — Lifecycle, Status, Outcome, and Publication Semantics

**Issue:**  
Reconcile legacy documentation that may mix:

- lifecycle states;
- evaluation outcomes;
- certification outcomes;
- publication states;
- operational status;
- suspension/revocation/expiration concepts.

**Known Collision Pattern:**  
Terms such as Certified, Suspended, Revoked, Expired, Active, Published, Valid, Supported, and related states may be used across different semantic categories.

**Questions to Reconcile:**

- Which terms describe lifecycle?
- Which describe publication?
- Which describe evaluation outcome?
- Which describe certification disposition?
- Which belong only to particular institutions?

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-013 — Validation, Eligibility, Evaluation, and Conformance Boundaries

**Issue:**  
Confirm or reconcile any current or legacy documentation that blurs:

- Validation;
- Eligibility;
- Evaluation;
- Conformance.

**Existing Distinctions to Preserve Unless Contradicted by Stronger Evidence:**

- Validation ≠ Eligibility
- Validation ≠ Evaluation
- Validation ≠ Conformance
- Eligibility ≠ Evaluation Outcome

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-014 — Relationship Semantics

**Issue:**  
Reconcile the meaning of key Suite relationships and ensure that legacy or current documentation does not collapse distinct relationships.

**Existing Distinctions Include:**

- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

**Relationship Terms Requiring Review May Include:**

- supports
- references
- derived-from
- evaluates
- results-in
- supersedes
- corrects
- related-to

**Question to Reconcile:**  
Which relationship terms are Attestor-specific and which, if any, are genuinely Suite-wide?

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-015 — Correction, Versioning, Supersession, and Mutation

**Issue:**  
Reconcile documentation and object semantics involving corrections, versions, supersession, mutation, and changed canonical statements.

**Existing Distinctions Include:**

- Correction ≠ Deletion
- Correction ≠ Version
- Correction ≠ Versioning Decision
- Supersession ≠ Mutation
- Changed Conclusion = Changed Canonical Statement

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-016 — Authority and Provenance Terminology

**Issue:**  
Determine whether authority and provenance terms are consistently defined across the Suite.

**Known Attestor Authority Contexts:**

- Attestor
- Suite-source
- external-source

**Known Attestor Provenance Values:**

- direct
- referenced
- derived

**Question to Reconcile:**  
Are these Attestor-specific values, or do any represent a broader Suite-level vocabulary?

**Constraint:**  
Do not generalize Attestor-specific controlled values into universal Suite vocabulary without explicit reconciliation.

**Scheduled Review:** Saturday — Phase II

**Status:** OPEN

---

## DI-017 — First Production Lineage vs Universal Suite Pipeline

**Issue:**  
Determine how the first exercised production lineage should inform the Suite’s architectural model.

**Known Production Lineage Includes References To:**

- `SC-CERT-2026-0001`
- `SREG-2026-0001`
- `CHR-2026-0001`
- `ANCH-2026-0001`
- `BEAC-2026-0001`

with:

- `ATT-2026-0001`
- `TRST-2026-0001`

**Core Question:**  
How should the lineage demonstrate real institutional relationships without becoming an incorrectly mandatory universal sequence?

**Scheduled Review:** Sunday — Phase III

**Status:** OPEN

---

## DI-018 — Conceptual Sequence vs Dependency

**Issue:**  
Determine the Suite’s conceptual sequence without converting explanatory order into technical dependency or mandatory execution order.

**Core Questions:**

- What is the most coherent Suite-level architectural sequence?
- Which relationships are conceptual rather than required dependencies?
- Which institutions can operate independently?
- Which sequencing language is explanatory only?

**Scheduled Review:** Sunday — Phase III

**Status:** OPEN

---

## DI-019 — Atlas Position Within the Mature Suite

**Issue:**  
Confirm Atlas’s architectural position as the Suite’s Authoritative Intelligence institution in light of later domain-intelligence or specialized intelligence concepts.

**Question to Reconcile:**  
Does any newer intelligence architecture create ambiguity about Atlas’s formal place in the Suite?

**Constraint:**  
Do not remove Atlas from the Suite or redefine its role without a genuine architectural contradiction.

**Scheduled Review:** Friday–Sunday

**Status:** OPEN

---

## DI-020 — Legacy Canon / Governance / Verification Tooling Placement

**Issue:**  
Review legacy references to Canon, governance tooling, verification tooling, or similar architectural components where they appear to function as Suite institutions, layers, or authorities.

**Question to Reconcile:**  
Are these:

- historical architectural labels;
- tools subordinate to existing institutions;
- cross-Suite concepts;
- or current architectural elements requiring explicit placement?

**Scheduled Review:** Friday–Saturday

**Status:** OPEN

---

# EXCLUDED / HANDED-FORWARD CATEGORIES

The following categories are intentionally **not** active Suite Reconciliation issues unless a specific Suite-level contradiction requires them.

## IR-HANDOFF — Interoperability Review

Examples include:

- detailed technical handoffs between institutions;
- API or interface compatibility;
- exchange mechanics;
- implementation-specific cross-institution behavior;
- detailed input/output schemas between institutions;
- technical compatibility of identifiers across implementations.

These shall be captured later in the **Interoperability Review Handoff Register**.

---

## UDR-HANDOFF — Satoshium Universe Documentation Reconciliation

Examples include:

- broad cleanup across Satoshium domains;
- unrelated stale website language;
- general README cleanup outside Suite-level relevance;
- Universe-level umbrella language not necessary to settle Suite architecture;
- broader presentation questions involving non-Suite applications, domains, or services.

These shall be captured later in the **Universe Documentation Reconciliation Handoff Register**.

---

# PREVIOUSLY RESOLVED BEFORE STEP 4

The following issue was historically unresolved but is no longer open entering this register:

## Aegis Suite Membership

**Current Determination:**  
Aegis is external/pre-Suite.

It is not one of the eight formal Suite institutions.

This register therefore does not reopen Aegis membership as an active reconciliation question.

**Status:** CLOSED BY BASELINE

---

# Step 4 Determination

The known previously reserved Suite-level issues have been assembled into one working register.

No listed issue is resolved merely by appearing in this document.

Additional issues may be added later only when supported by repository evidence or reconciliation findings.

**Recommended Classification:** CONFIRMED

**Step 4 Status:** PENDING APPROVAL

---

## Recommended GitHub Placement

`suite/reconciliation/satoshium-suite-reconciliation-deferred-issues-register-2026-09-25.md`
