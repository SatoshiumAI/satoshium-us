# Satoshium Suite Reconciliation — Terminology Collision Resolution

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record documents the formal resolution of terminology collisions identified during the September 26, 2026 phase of the Satoshium Suite Reconciliation.

The review focused on areas where mature Suite terminology could be confused, collapsed, or interpreted as implying authority, validation, outcome, trust, lifecycle, or identity beyond its intended scope.

The following collisions were reviewed and resolved:

1. Validation vs Eligibility
2. Validation vs Conformance
3. Verification vs Certification
4. Trust Signal vs Trust Statement
5. Beacon Discovery Signal vs legacy “trust signal”
6. Decision/Outcome vs Lifecycle State
7. Record vs Object vs Entry
8. Authority vs Provenance

The governing principles remain:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

> **CONNECTION ≠ IDENTITY.**

> **REFERENCE ≠ DERIVATION ≠ SUPPORT.**

> **STATUS DESCRIBES CONDITION; IT DOES NOT DEFINE AUTHORITY OR SUBSTANTIVE OUTCOME.**

---

# 1. Validation vs Eligibility

## Resolution
**DISTINCT TERMS — DO NOT INTERCHANGE**

## Controlled Meaning

### Eligibility
Eligibility determines whether a subject, object, assertion, event, or request satisfies the threshold conditions required to enter a governed process.

It answers:

> **May this candidate proceed into the process?**

### Validation
Validation determines whether a governed object or process satisfies the structural, formal, or procedural requirements applicable to it.

It answers:

> **Does this object/process meet its governing requirements?**

## Semantic Order

```text
Candidate
    ↓
Eligibility Determination
    ↓
Eligible
    ↓
Governed Process / Object Creation
    ↓
Validation
    ↓
Valid / Invalid
```

## Controlled Distinctions

- Eligible ≠ Valid
- Valid ≠ Eligible
- Eligible ≠ Supported
- Valid ≠ Supported
- Preservation Eligibility ≠ Chronicle Validation

## Final Rule

> **ELIGIBILITY DETERMINES WHETHER SOMETHING MAY ENTER THE PROCESS.**

> **VALIDATION DETERMINES WHETHER THE GOVERNED OBJECT OR PROCESS MEETS ITS REQUIREMENTS.**

---

# 2. Validation vs Conformance

## Resolution
**DISTINCT BUT RELATED TERMS**

## Controlled Meaning

### Validation
Validation determines whether a governed object or process satisfies institutional requirements.

### Conformance
Conformance determines whether a governed object, process, implementation, or artifact satisfies an explicitly identified specification, framework, profile, rule set, or requirement set.

## Relationship

```text
Object / Process
    ↓
Conformance Testing
    ↓
Conformance Result
    ↓ may inform
Validation
    ↓
Validation Result
```

This relationship is not necessarily procedural in every institution, but it preserves the semantic distinction.

## Controlled Distinctions

- Conformance ≠ Validation
- Conformant ≠ Valid by definition
- Valid ≠ Conformant by definition
- Conformant ≠ Certified
- Conformant ≠ Supported
- NOT-TESTED ≠ PASS
- NOT-TESTED ≠ FAIL

## Final Rule

> **VALIDATION DETERMINES WHETHER THE GOVERNED OBJECT OR PROCESS MEETS ITS INSTITUTIONAL REQUIREMENTS.**

> **CONFORMANCE DETERMINES WHETHER IT SATISFIES A SPECIFIC, EXPLICITLY IDENTIFIED REQUIREMENT SET.**

---

# 3. Verification vs Certification

## Resolution
**DISTINCT TERMS — DO NOT INTERCHANGE**

## Controlled Meaning

### Verification
Verification is the process of checking whether a representation, claim, condition, or record matches a defined evidentiary or factual basis.

It asks:

> **Does this thing match what the evidence or reference basis says it should match?**

### Certification
Certification is Certifier’s governed institutional act of reviewing a subject against applicable certification requirements and issuing a Certification Decision within a Certification Package.

It asks:

> **Does this subject satisfy the requirements necessary for Certifier to issue its governed certification determination?**

## Controlled Distinctions

- Verification ≠ Certification
- Verified ≠ Certified
- Integrity Verification ≠ Certification
- Historical Verification ≠ Certification
- Verification Step ≠ Certification Decision
- Verification ≠ Validation
- Verification ≠ Conformance
- VERIFIED ≠ TRUE

## Final Rule

> **VERIFICATION DETERMINES WHETHER SOMETHING MATCHES A DEFINED EVIDENTIARY OR REFERENCE BASIS.**

> **CERTIFICATION IS CERTIFIER’S GOVERNED INSTITUTIONAL DETERMINATION UNDER APPLICABLE CERTIFICATION REQUIREMENTS.**

---

# 4. Trust Signal vs Trust Statement

## Resolution
**DISTINCT TERMS — “TRUST SIGNAL” MUST NOT SUBSTITUTE FOR TRUST STATEMENT**

## Trust Statement

A **Trust Statement** is Attestor’s canonical governed conclusion produced from an Attestation through Rule-Constrained Evaluation.

It has:

- canonical identity;
- TRST identifier;
- bounded scope;
- provenance;
- lifecycle;
- publication state;
- an Attestor authority domain.

```text
Attestation
    ↓
Rule-Constrained Evaluation
    ↓
Evaluation Outcome
    ↓
Trust Statement
```

## Trust Signal

A legacy or descriptive **trust signal** may refer only to a non-canonical indicator, contextual clue, heuristic, or observation that could inform trust-related analysis.

It does not possess the same institutional identity, governance, lifecycle, or authority as a Trust Statement.

## Controlled Distinctions

- Trust Signal ≠ Trust Statement
- Atlas Signal ≠ Trust Statement
- Beacon Discovery Signal ≠ Trust Statement
- Legacy Trust Signal ≠ Trust Statement

## Final Rule

> **TRUST SIGNAL IS AN INDICATOR.**

> **TRUST STATEMENT IS A CANONICAL GOVERNED CONCLUSION.**

---

# 5. Beacon Discovery Signal vs Legacy “Trust Signal”

## Resolution
**DISTINCT TERMS — LEGACY “TRUST SIGNAL” MUST NOT NAME BEACON’S CANONICAL OBJECT**

## Discovery Signal

A **Discovery Signal** is Beacon’s canonical governed representation of a relevant discovery, observation, change, or externally sourced condition admitted into Beacon.

Beacon owns:

- Discovery Signal identity;
- Discovery Metadata;
- provenance;
- Signal Type;
- lifecycle;
- versioning;
- publication state;
- Beacon relationships.

## Legacy “Trust Signal”

The legacy phrase **trust signal** is non-canonical descriptive terminology only.

It does not represent:

- a Beacon canonical object;
- an Attestor Trust Statement;
- a formal Evaluation Outcome;
- an authority-bearing Suite object.

## Controlled Distinctions

```text
Atlas Signal
    ≠
Beacon Discovery Signal
    ≠
legacy trust signal
    ≠
Attestor Trust Statement
```

## Final Rule

> **BEACON DISCOVERY SIGNAL IS A CANONICAL DISCOVERY OBJECT.**

> **LEGACY “TRUST SIGNAL” IS NOT A CANONICAL BEACON OBJECT AND MUST NOT IMPLY TRUST AUTHORITY.**

Historical use may remain preserved where historically accurate, but current-state documentation should use mature terminology.

---

# 6. Decision / Outcome vs Lifecycle State

## Resolution
**DISTINCT SEMANTIC DOMAINS — DO NOT INTERCHANGE**

## Decision / Outcome

A Decision or Outcome is a substantive institutional determination produced by a governed process.

Examples include:

- Certification Decision
- Certification Outcome
- Evaluation Outcome
- Conformance Result
- Validation Result
- Eligibility Determination

It answers:

> **What did the governed process conclude?**

## Lifecycle State

Lifecycle State describes the current governed condition of the canonical object.

Examples include:

- Active
- Inactive
- Superseded
- Withdrawn
- Archived

It answers:

> **What is the current operative condition of the object?**

## Controlled Examples

```text
Certification Outcome: Approved
Lifecycle State: Active
```

Later:

```text
Certification Outcome: Approved
Lifecycle State: Superseded
```

The substantive conclusion can remain historically unchanged while lifecycle state changes.

## Controlled Distinctions

- Outcome ≠ Lifecycle State
- Certified ≠ Active
- Failed Certification ≠ Inactive
- Supported ≠ Active
- Contradicted ≠ Withdrawn
- Evaluation Outcome ≠ Lifecycle Status
- Validation Result ≠ Lifecycle State
- Conformance Result ≠ Lifecycle State

## Preferred Labels

Use explicit labels rather than generic “Status”:

- Lifecycle State
- Certification Outcome
- Validation Result
- Conformance Result
- Evaluation Outcome
- Eligibility Determination
- Publication State

## Final Rule

> **DECISION / OUTCOME = SUBSTANTIVE INSTITUTIONAL CONCLUSION.**

> **LIFECYCLE STATE = CURRENT GOVERNED CONDITION OF THE CANONICAL OBJECT.**

---

# 7. Record vs Object vs Entry

## Resolution
**DISTINCT TERMS WITH DIFFERENT LEVELS OF SPECIFICITY**

## Object

**Object** is the broad Suite-wide architectural term.

A canonical object is a distinct governed entity with identity, ownership, lifecycle, and institutional meaning.

Examples:

- Certification Package
- Satoshium Registry Entry
- Chronicle Entry
- Integrity Reference
- Discovery Signal
- Attestation
- Trust Statement
- Jurisdiction Intelligence Package
- Navigator Workflow Definition

> **Canonical Object** is the preferred Suite-wide umbrella term.

## Record

**Record** is a governed informational representation or a contextual role.

It should be used where the thing is genuinely modeled as a record, including:

- Source Record
- Supporting Record
- Historical Record
- Provenance Record
- Evaluation Record, where such a distinct record exists

Not every canonical object should be renamed a “record.”

## Entry

**Entry** is an institution-specific formal object label.

Current formal examples:

- Satoshium Registry Entry (SREG)
- Chronicle Entry

## Controlled Distinctions

- Record ≠ universal replacement for Object
- Entry ≠ generic synonym for Object
- Registry Record ≠ preferred formal name for SREG
- Source Record = contextual role, not canonical object class
- Supporting Record = contextual role, not canonical status
- Representation ≠ Canonical Object by default
- Entry ≠ Version
- Record ≠ Authoritative by definition

## Canonical Hierarchy

```text
Canonical Object
    ├── Package
    ├── Entry
    ├── Reference
    ├── Signal
    ├── Attestation
    ├── Statement
    └── Workflow Definition
```

## Final Rule

> **OBJECT = ARCHITECTURAL UMBRELLA TERM.**

> **RECORD = GOVERNED INFORMATIONAL REPRESENTATION OR CONTEXTUAL RECORD ROLE.**

> **ENTRY = INSTITUTION-SPECIFIC FORMAL OBJECT LABEL WHERE EXPLICITLY DEFINED.**

---

# 8. Authority vs Provenance

## Resolution
**DISTINCT TERMS — DO NOT INTERCHANGE**

## Authority

Authority identifies the institution responsible for governing a defined object, process, or decision domain.

It answers:

> **Who governs this?**

## Provenance

Provenance identifies where information, records, evidence, or representations came from and how they reached their current form.

It answers:

> **Where did this come from?**

## Controlled Example

```text
SREG-2026-0001
    provenance → SC-CERT-2026-0001
```

This means the Registry Entry can trace its source to the Certifier object.

It does not transfer certification authority to Registry.

## Controlled Distinctions

- Authority ≠ Provenance
- Provenance may identify authority
- Provenance does not create authority
- Provenance does not transfer authority
- Object Authority ≠ Complete Source Provenance
- Historical Provenance ≠ Source Authority
- Beacon Provenance ≠ Source Authority
- Attestor Provenance ≠ Ownership of Source Records

## Final Rule

> **AUTHORITY ANSWERS WHO GOVERNS.**

> **PROVENANCE ANSWERS WHERE IT CAME FROM.**

and:

> **PROVENANCE MAY LOCATE AUTHORITY, BUT IT DOES NOT CREATE OR TRANSFER AUTHORITY.**

---

# Terminology Collision Resolution Matrix

| Collision | Final Resolution |
|---|---|
| Validation vs Eligibility | Eligibility governs admission; Validation governs object/process compliance |
| Validation vs Conformance | Validation determines institutional acceptability; Conformance tests explicit requirements |
| Verification vs Certification | Verification checks correspondence; Certification is Certifier’s governed determination |
| Trust Signal vs Trust Statement | Trust Signal is non-canonical indicator terminology; Trust Statement is canonical Attestor conclusion |
| Beacon Discovery Signal vs legacy “trust signal” | Discovery Signal is Beacon’s canonical object; legacy trust signal is non-canonical |
| Decision/Outcome vs Lifecycle State | Decision/Outcome is substantive conclusion; Lifecycle State is current object condition |
| Record vs Object vs Entry | Object is umbrella term; Record is informational/contextual; Entry is institution-specific formal label |
| Authority vs Provenance | Authority identifies who governs; Provenance identifies origin and lineage |

---

# Suite-Wide Collision Rules

The terminology-collision review establishes the following governing rules:

1. Eligibility determines admission; Validation determines compliance with institutional requirements.
2. Conformance tests explicitly defined requirement sets and is not synonymous with Validation.
3. Verification checks correspondence and is not Certification.
4. A Trust Statement is a formal Attestor canonical object.
5. “Trust signal” is not a substitute for Trust Statement.
6. Beacon’s canonical object is Discovery Signal.
7. Legacy “trust signal” does not carry Beacon or Attestor authority.
8. Decision and Outcome terminology must remain distinct from Lifecycle State.
9. Canonical Object is the Suite-wide architectural umbrella term.
10. Record should be used only where informational or contextual record semantics actually apply.
11. Entry is reserved for institutions whose formal object name uses Entry.
12. Authority and Provenance are separate semantic dimensions.
13. Provenance may identify an authority source but does not transfer that authority.
14. Connection ≠ Identity.
15. Reference ≠ Derivation ≠ Support.
16. Supersession ≠ Mutation.
17. **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# Final Disposition

**Terminology Collision Resolution — COMPLETE — APPROVED**

All eight terminology collisions identified for the September 26, 2026 Phase II reconciliation have been resolved.

This record should govern subsequent lifecycle-semantic reconciliation, correction/versioning reconciliation, relationship-semantics reconciliation, authority-semantics reconciliation, and documentation conformance work.
