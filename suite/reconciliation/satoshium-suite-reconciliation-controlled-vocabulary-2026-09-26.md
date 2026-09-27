# Satoshium Suite Reconciliation — Controlled Vocabulary Reconciliation

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record documents the Suite-wide Controlled Vocabulary Reconciliation conducted during the September 26, 2026 phase of the Satoshium Suite Reconciliation.

The review reconciled terminology across the formal Satoshium Suite for:

- Lifecycle
- Publication
- Provenance
- Authority
- Validation
- Conformance
- Evaluation
- Eligibility
- Relationships
- Status

The purpose of this record is to preserve clear semantic boundaries so that similar terms are not used as interchangeable substitutes across institutions.

The governing principle remains:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# 1. Lifecycle

## Controlled Definition

**Lifecycle** is the institution-governed progression of a canonical object through defined states from creation through subsequent operation, revision, supersession, withdrawal, archival, or other authorized lifecycle conditions.

Lifecycle describes the condition of an object over time.

It does not describe the substantive conclusion about that object.

## Controlled Distinctions

- Canonical Creation ≠ Lifecycle Activation
- Canonical Creation ≠ Publication
- Active ≠ Published
- Active ≠ Valid
- Active ≠ Conformant
- Active ≠ Certified
- Active ≠ Supported
- Active ≠ Eligible
- Version ≠ New Canonical Identity by default
- Correction ≠ New Canonical Object by default
- Supersession ≠ Mutation
- Superseded ≠ Invalid
- Withdrawn ≠ False
- Archived ≠ Rejected

## Recommended Lifecycle Vocabulary

- Canonical Creation
- Active
- Inactive
- Superseded
- Withdrawn
- Archived
- Version

## Governing Rule

> **LIFECYCLE STATE DESCRIBES THE CONDITION OF THE OBJECT — NOT THE SUBSTANTIVE CONCLUSION ABOUT THE OBJECT.**

---

# 2. Publication

## Controlled Definition

**Publication** is the institution-governed act of exposing an existing canonical object or approved representation to a public audience.

Publication changes accessibility.

It does not create identity, authority, validity, truth, certification, or substantive outcome.

## Controlled Distinctions

- Canonical Creation ≠ Publication
- Active ≠ Published
- Published ≠ Valid
- Published ≠ Conformant
- Published ≠ Certified
- Published ≠ Eligible
- Published ≠ Supported
- Published ≠ Current
- Publication ≠ Version
- Published Object ≠ New Canonical Object

## Derived Representations

A published HTML rendering, JSON serialization, catalog surface, or other approved representation does not become a second canonical object merely because it is public.

## Governing Rule

> **PUBLICATION EXPOSES AUTHORITY; IT DOES NOT CREATE AUTHORITY.**

and:

> **PUBLICATION CHANGES ACCESSIBILITY, NOT INSTITUTIONAL MEANING.**

---

# 3. Provenance

## Controlled Definition

**Provenance** is the documented origin, lineage, custody, derivation, and transformation history that allows information, records, and representations to be traced to their sources and prior states.

Provenance explains where something came from.

It does not determine whether that thing is true, valid, supported, certified, or authoritative.

## Controlled Distinctions

- Provenance ≠ Authority
- Provenance ≠ Evidence
- Provenance ≠ Derivation
- Provenance ≠ Relationship Type in general
- Provenance ≠ Validation
- Provenance ≠ Evaluation Outcome
- Provenance ≠ Support

## Provenance Vocabulary

- Source Provenance
- Object Provenance
- Representation Provenance
- Derivation Provenance
- Provenance Record, only where an explicit record exists

## Governing Rule

> **PROVENANCE IDENTIFIES ORIGIN; IT DOES NOT TRANSFER AUTHORITY.**

and:

> **PROVENANCE EXPLAINS WHERE SOMETHING CAME FROM — NOT WHETHER IT IS TRUE, VALID, OR AUTHORITATIVE.**

---

# 4. Authority

## Controlled Definition

**Authority** is the institutionally assigned responsibility to govern a defined object, process, or decision domain and to make determinations within that domain.

Authority belongs to the institution that owns the relevant governed domain.

## Institutional Authority Domains

- **Atlas** — Atlas intelligence packages
- **Navigator** — Navigator Workflow Definitions and orchestration state
- **Certifier** — Certification Packages, certification actions, and Certification Decisions
- **Registry** — SREG identity and Registry-controlled registration metadata
- **Chronicle** — Chronicle Entries and historical preservation
- **Anchor** — Integrity References and integrity-preservation determinations
- **Beacon** — Discovery Signals and Discovery Metadata
- **Attestor** — Attestations, Rule-Constrained Evaluation, Evaluation Outcomes, and Trust Statements

## Controlled Distinctions

- Authority ≠ Reference
- Authority ≠ Publication
- Authority ≠ Provenance
- Authority ≠ Validation
- Authority ≠ Conformance
- Authority ≠ Evaluation Outcome
- Authority ≠ Eligibility
- Historical Authority ≠ Source Authority
- Registration Authority ≠ Source Authority
- Evaluation Authority ≠ Source Authority

## Governing Rules

> **AUTHORITY IS OWNED BY DOMAIN — IT IS NOT INHERITED THROUGH REFERENCE, PUBLICATION, REGISTRATION, DISCOVERY, PRESERVATION, OR COORDINATION.**

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

> **COORDINATION DOES NOT TRANSFER AUTHORITY.**

---

# 5. Validation

## Controlled Definition

**Validation** is the institution-specific determination that a governed object or process satisfies the structural, formal, or procedural requirements applicable to that object or process.

Validation determines whether the object or process meets its institutional requirements.

It does not determine substantive truth.

## Controlled Distinctions

- VALID ≠ TRUE
- Valid ≠ Certified
- Validation ≠ Certification Decision
- Valid ≠ Supported
- Validation ≠ Evaluation
- Eligible ≠ Valid
- Validation ≠ Conformance
- Valid ≠ Published
- Validation ≠ Lifecycle
- Validation does not transfer authority

## Validation Vocabulary

- Valid
- Invalid
- Validation Result
- Validation Evidence
- Validation Rule / Requirement

## Governing Rule

> **VALIDATION DETERMINES WHETHER THE OBJECT OR PROCESS MEETS ITS RULES — NOT WHETHER ITS SUBSTANTIVE CONTENT IS TRUE.**

---

# 6. Conformance

## Controlled Definition

**Conformance** is the determination that a governed object, process, implementation, or artifact satisfies an explicitly identified specification, framework, profile, rule set, or requirement set.

Conformance measures alignment to declared requirements.

## Controlled Distinctions

- Conformance ≠ Validation
- Conformant ≠ Valid by definition
- Conformant ≠ Certified
- Conformance Determination ≠ Certification Decision
- Conformant ≠ Supported
- Eligible ≠ Conformant
- Conformant ≠ True
- Conformance ≠ Publication State
- Conformance ≠ Lifecycle State

## Conformance Vocabulary

- Conformant
- Non-Conformant
- Not Tested
- Not Applicable
- Conformance Basis
- Conformance Result
- Conformance Evidence

## Special Rule

> **NOT-TESTED ≠ PASS**

and:

> **NOT-TESTED ≠ FAIL**

## Governing Rule

> **CONFORMANCE MEASURES ALIGNMENT TO RULES; IT DOES NOT BY ITSELF ESTABLISH VALIDITY, CERTIFICATION, OR SUBSTANTIVE TRUTH.**

---

# 7. Evaluation

## Controlled Definition

**Evaluation** is the governed application of defined rules, criteria, and evidence to a subject, assertion, or object in order to produce a bounded substantive conclusion.

The clearest formal Suite implementation is Attestor's **Rule-Constrained Evaluation**.

## Attestor Flow

```text
Attestation
    ↓
Rule-Constrained Evaluation
    ↓
Evaluation Outcome
    ↓
Trust Statement
```

## Controlled Distinctions

- Evaluation ≠ Attestation
- Evaluation ≠ Evaluation Outcome
- Evaluation ≠ Trust Statement
- Evaluation ≠ Validation
- Evaluation ≠ Conformance
- Evaluation ≠ Eligibility
- Evaluation ≠ Certification
- Evaluation Outcome ≠ Certification Decision
- Evaluation Outcome ≠ Universal Truth
- Trust Statement ≠ Universal Truth
- Evidence ≠ Evaluation
- Evidence ≠ Evaluation Outcome

## Evaluation Vocabulary

- Evaluation
- Rule-Constrained Evaluation
- Evaluation Basis
- Evaluation Outcome
- Evaluation Record, only where an explicit record exists

## Governing Rule

> **EVALUATION IS THE PROCESS; EVALUATION OUTCOME IS THE RESULT; TRUST STATEMENT IS THE CANONICAL ATTESTOR EXPRESSION OF THAT RESULT.**

---

# 8. Eligibility

## Controlled Definition

**Eligibility** is the institution-governed determination that a candidate satisfies the threshold conditions required to enter a defined process.

Eligibility is an admission gate.

It does not predict the downstream result.

## Controlled Distinctions

- Eligibility ≠ Evaluation Outcome
- Eligibility ≠ Validation Result
- Eligibility ≠ Conformance Result
- Eligibility ≠ Certification Decision
- ELIGIBLE ≠ SUPPORTED
- Eligible ≠ Valid
- Eligible ≠ Conformant
- Eligible for Certification ≠ Certified
- Eligible ≠ Published
- Eligibility ≠ Authority
- Provenance ≠ Eligibility
- Eligibility ≠ Lifecycle

## Eligibility Vocabulary

- Eligible
- Ineligible
- Eligibility Criteria
- Eligibility Determination
- Preservation Eligibility
- Evaluation Eligibility

## Governing Rule

> **ELIGIBILITY DETERMINES ADMISSION — NOT OUTCOME.**

---

# 9. Relationships

## Controlled Definition

A **Relationship** is an explicitly typed semantic connection between distinct governed objects, records, representations, or institutional entities.

Relationships must preserve identity and authority boundaries.

## Core Controlled Relationship Terms

- references
- derived-from
- supports
- source-of / originates-from
- registered-as / registers
- preserved-as
- integrity-preserved-by / anchored-by
- represented-as
- attests-to
- evaluates
- produces
- supersedes / superseded-by
- version-of
- related-to, only as a weak fallback

## Controlled Distinctions

- Connection ≠ Identity
- Reference ≠ Derivation
- Reference ≠ Support
- Reference ≠ Ownership
- Derivation ≠ Identity
- Registration Relationship ≠ Identity
- Anchored ≠ Certified
- Anchored ≠ Trusted
- Discovery Relationship ≠ Source Ownership
- Discovery ≠ Verification
- Produces ≠ Derived-From
- Supersession ≠ Mutation
- Version-Of ≠ Supersedes

## Governing Rules

> **CONNECTION ≠ IDENTITY**

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

> **REFERENCE ≠ DERIVATION ≠ SUPPORT.**

> **SUPERSESSION ≠ MUTATION.**

---

# 10. Status

## Controlled Definition

**Status** is a domain-specific descriptor of the current condition of an object, process, workflow, publication, or institution.

The status domain should be explicit whenever ambiguity is possible.

## Recognized Status Domains

- Lifecycle Status
- Publication Status
- Validation Result
- Conformance Result
- Evaluation Outcome
- Workflow Status
- Institutional Status
- Operational Status

## Controlled Distinctions

- Active ≠ Valid
- Active ≠ Published
- Published ≠ Current
- Valid ≠ Active
- Invalid ≠ Withdrawn
- Evaluation Outcome ≠ Lifecycle Status
- Workflow Status ≠ Canonical Object Status
- Status ≠ Authority
- Status Change ≠ Identity Change
- Status ≠ Version

## Institutional Status

The reconciled formal Satoshium Suite contains exactly eight institutions, all **Operational**:

1. Atlas
2. Navigator
3. Certifier
4. Registry
5. Chronicle
6. Anchor
7. Beacon
8. Attestor

Institutional status does not determine the status of individual objects owned by those institutions.

## Governing Rule

> **STATUS DESCRIBES CONDITION; IT DOES NOT BY ITSELF DEFINE IDENTITY, AUTHORITY, VALIDITY, PUBLICATION, OR SUBSTANTIVE OUTCOME.**

---

# Reconciled Controlled Vocabulary Matrix

| Domain | Controlled Meaning | Must Not Be Treated As |
|---|---|---|
| Lifecycle | Governed progression of an object through institutional states | outcome, validation, publication, eligibility |
| Publication | Public exposure of an existing object or approved representation | creation, authority, validity, substantive outcome |
| Provenance | Origin, lineage, custody, derivation, and transformation history | authority, evidence, validation, support |
| Authority | Institutional responsibility over a defined object/process/decision domain | reference, publication, provenance, validation |
| Validation | Determination that an object/process satisfies institutional requirements | truth, certification, support, evaluation |
| Conformance | Determination of alignment to an explicit specification or rule set | validation, certification, truth, evaluation |
| Evaluation | Governed process applying evidence and criteria to reach a bounded conclusion | validation, conformance, eligibility, certification |
| Eligibility | Threshold determination for admission to a governed process | favorable outcome, validation, certification, support |
| Relationships | Explicit semantic connections between distinct objects/entities | identity, authority transfer |
| Status | Domain-specific description of current condition | identity, authority, validity, version |

---

# Suite-Wide Semantic Rules

The Controlled Vocabulary Reconciliation establishes the following Suite-wide rules:

1. Canonical Creation ≠ Lifecycle Activation.
2. Lifecycle Activation ≠ Publication.
3. Active ≠ Published.
4. Published ≠ Valid.
5. Published ≠ Current.
6. Valid ≠ True.
7. Valid ≠ Supported.
8. Conformant ≠ Valid by definition.
9. Conformant ≠ Certified.
10. NOT-TESTED ≠ PASS.
11. Eligibility ≠ Evaluation Outcome.
12. Eligible ≠ Supported.
13. Evaluation ≠ Evaluation Outcome.
14. Evaluation Outcome ≠ Trust Statement.
15. Evaluation Outcome ≠ Certification Decision.
16. Provenance ≠ Authority.
17. Evidence ≠ Provenance.
18. Reference ≠ Derivation.
19. Reference ≠ Support.
20. Connection ≠ Identity.
21. Supersession ≠ Mutation.
22. Status ≠ Version.
23. Workflow Status ≠ Canonical Object Status.
24. Historical Authority ≠ Source Authority.
25. Registration Authority ≠ Source Authority.
26. Evaluation Authority ≠ Source Authority.
27. Publication exposes authority; it does not create authority.
28. Validation does not transfer authority.
29. Eligibility does not transfer authority.
30. Coordination does not transfer authority.
31. **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# Final Disposition

**Controlled Vocabulary Reconciliation — COMPLETE — APPROVED**

The following vocabulary domains are now reconciled for Phase II:

- Lifecycle
- Publication
- Provenance
- Authority
- Validation
- Conformance
- Evaluation
- Eligibility
- Relationships
- Status

This record should govern subsequent terminology-collision review, lifecycle reconciliation, correction/versioning semantics, relationship semantics, authority semantics, and final Suite documentation conformance work.
