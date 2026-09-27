# Satoshium Suite Reconciliation — Suite Canonical Vocabulary & Object Matrix

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record consolidates the results of the September 26, 2026 Phase II reconciliation into one Suite-level reference covering:

- canonical objects;
- canonical identifiers;
- lifecycle terminology;
- correction and versioning semantics;
- relationship vocabulary;
- authority terminology;
- validation, eligibility, conformance, and verification distinctions;
- outcome and status semantics;
- legacy truth, trust, and scoring terminology.

This record does not redesign the Satoshium Suite.

It documents the mature architecture established across the eight formal Suite institutions.

---

# I. Canonical Institutional Object Matrix

| Institution | Institutional Role | Canonical Object(s) | Canonical Identifier | Primary Authority | Key Supporting Constructs |
|---|---|---|---|---|---|
| **Atlas** | Authoritative Intelligence | **Jurisdiction Intelligence Package** | Package-specific / existing Atlas identity | Governing jurisdiction intelligence packages | Evidence Layer, Signal Layer, Trust Dimensions, Profile, Builder Mode, Topology Metadata, Change Log |
| **Navigator** | Workflow Definition / Orchestration | **Navigator Workflow Definition** | No invented NAV family established | Workflow definition and orchestration | Queries, Triggers, Schemas, Templates, Rules, Filters, Workflow State, Outputs |
| **Certifier** | Operational Certification | **Certification Package** | **SC-CERT-YYYY-NNNN** | Certification action and Certification Decision | Evidence Records, Evidence Inventory, Evidence Mapping, SCPR, SCR, SCRD |
| **Registry** | Canonical Registration / Public Catalog | **Satoshium Registry Entry** | **SREG-YYYY-NNNN** | Registration identity, Registry metadata, catalog governance | Registry Record Type, source-reference metadata, catalog representation |
| **Chronicle** | Historical Preservation | **Chronicle Entry** | **CHR-YYYY-NNNN** | Historical preservation and Chronicle Entry governance | Occurrence, Event Type, Preservation Eligibility, historical verification, entry versions |
| **Anchor** | Integrity Preservation | **Integrity Reference** | **ANCH-YYYY-NNNN** | Integrity preservation and Integrity Reference governance | Integrity Subject, hash, signature, timestamp, representation boundary, verification |
| **Beacon** | Discovery & Signals | **Discovery Signal** | **BEAC-YYYY-NNNN** | Discovery Signal and Discovery Metadata governance | Discovery Metadata, Signal Type, indexing/query/presentation |
| **Attestor** | Governed Attestation & Rule-Constrained Evaluation | **Attestation**; **Trust Statement** | **ATT-YYYY-NNNN**; **TRST-YYYY-NNNN** | Attestation, evaluation, Evaluation Outcome, Trust Statement | Eligibility, Validation, Rule-Constrained Evaluation, Evaluation Outcome |

---

# II. Canonical Object Rules

## Atlas

**Canonical Object:** Jurisdiction Intelligence Package

The term **Jurisdiction Intelligence Record** may remain useful conceptually, but it is not a separate co-equal canonical object.

The package is the governed whole.

```text
Jurisdiction Intelligence Package
    ├── Evidence Layer
    ├── Signal Layer
    ├── Trust Dimensions
    ├── Profile
    ├── Builder Mode
    ├── Topology Metadata
    └── Change Log
```

HTML and JSON are representations or serializations, not separate canonical objects.

> **Atlas Signal ≠ Beacon Discovery Signal**

> **Atlas Trust Dimension ≠ Attestor Trust Statement**

## Navigator

**Canonical Object:** Navigator Workflow Definition

**Workflow Orchestration** is the institution’s operational function, not a competing canonical object.

```text
Navigator Workflow Definition
        ↓ governs
Workflow Orchestration
```

Queries, triggers, schemas, templates, rules, filters, workflow state, and outputs support execution but are not co-equal canonical objects.

> **Workflow State ≠ Canonical Institutional State**

> **Coordination does not transfer authority.**

## Certifier

**Canonical Object:** Certification Package

The Certification Decision is a governed determination contained within the Package.

```text
Certification Package
    ├── governed subject
    ├── evidence
    ├── certification process
    └── Certification Decision / Outcome
```

> **Certification Decision ≠ Lifecycle State**

> **Certification Outcome ≠ Publication State**

## Registry

**Canonical Object:** Satoshium Registry Entry

Preferred name:

> **Satoshium Registry Entry (SREG)**

“Registry Record” may remain general or legacy shorthand, but it is not the preferred canonical name.

Architecture:

```text
Registry
    ↓
SREG
    ↓
Registry Record Type
    ↓
Authoritative Source Record
```

The final line represents relationship, not ownership.

> **Registration does not transfer source authority.**

## Chronicle

**Canonical Object:** Chronicle Entry

The **Occurrence** is the represented historical subject, not the canonical object.

```text
Occurrence
    ↓ represented by
Chronicle Entry
```

> **Historical authority ≠ source authority**

> **Chronicle records when; it does not become authoritative for what another institution owns.**

## Anchor

**Canonical Object:** Integrity Reference

The Integrity Subject is defined through:

- Source Artifact identity;
- Canonical Representation;
- Representation Boundary.

> **Integrity ≠ Truth**

> **Integrity ≠ Certification**

> **Integrity ≠ Trust**

## Beacon

**Canonical Object:** Discovery Signal

**Discovery Metadata** is a governed supporting layer, not a second canonical object.

> **Discovery Signal ≠ legacy trust signal**

> **Discovery Signal ≠ Trust Statement**

> **Discovery does not transfer source authority.**

## Attestor

**Canonical Objects:**

1. **Attestation**
2. **Trust Statement**

Supporting governed result:

> **Evaluation Outcome**

Evaluation Outcome is not a third canonical object.

Canonical flow:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Validation
        ↓
Rule-Constrained Evaluation
        ↓
Evaluation Outcome
        ↓
Trust Statement
```

> **Attestation ≠ Evaluation**

> **Evaluation ≠ Evaluation Outcome**

> **Evaluation Outcome ≠ Trust Statement**

> **Changed Conclusion = Changed Canonical Statement**

---

# III. Canonical Vocabulary Matrix

| Term | Controlled Meaning | Must Not Be Confused With |
|---|---|---|
| **Canonical Object** | Governed entity with institutional identity, ownership, and lifecycle | Representation, supporting record |
| **Canonical Creation** | Establishes existence and identity | Activation, Publication |
| **Lifecycle Activation** | Establishes operative standing | Creation, Publication |
| **Publication** | Establishes public accessibility | Creation, Authority, Validation |
| **Lifecycle State** | Current governed condition of object | Outcome, Validation Result |
| **Version** | Governed edition/state of same continuing identity | Correction, new object automatically |
| **Correction** | Repairs an error or defect | Version, Deletion |
| **Supersession** | Replaces operative standing while preserving history | Mutation, Deletion |
| **Eligibility** | Threshold determination for entering a process | Validation, Outcome |
| **Validation** | Determines whether governed object/process meets applicable institutional requirements | Eligibility, Conformance, Truth |
| **Conformance** | Tests against explicitly identified requirements | Validation, Certification |
| **Verification** | Checks correspondence against defined evidence/reference basis | Certification, Validation |
| **Certification** | Certifier-governed institutional determination | Verification |
| **Evaluation** | Governed application of criteria/evidence to a subject | Validation, Outcome |
| **Evaluation Outcome** | Result produced by Evaluation | Trust Statement, Lifecycle State |
| **Trust Statement** | Canonical bounded Attestor conclusion | Truth declaration, score, certification |
| **Provenance** | Origin, lineage, custody, and transformation history | Authority |
| **Authority** | Institutionally assigned governance responsibility | Provenance, reference |
| **Status** | Domain-specific current condition | Identity, authority |
| **Record** | Governed informational representation or contextual role | Universal synonym for Object |
| **Entry** | Formal object label where institution explicitly defines one | Generic object term |
| **Representation** | Rendering/serialization/display of object | Canonical object by default |

---

# IV. Lifecycle Vocabulary

The Suite formally preserves:

```text
Canonical Creation
        ↓
Lifecycle Activation
        ↓
Publication
```

These answer different questions:

| Concept | Question |
|---|---|
| Canonical Creation | Does the object exist? |
| Lifecycle Activation | Is it operative? |
| Publication | Is it publicly accessible? |

Therefore:

> **Created ≠ Active**

> **Active ≠ Published**

> **Published ≠ Current**

> **Published ≠ Valid**

> **Published ≠ Certified**

---

# V. Correction & Versioning Vocabulary

The controlling rules are:

> **Correction ≠ Version**

> **Correction ≠ Deletion**

> **Supersession ≠ Mutation**

> **Changed Conclusion = Changed Canonical Statement**

Suite-wide decision logic:

```text
Change Identified
      ↓
Canonical meaning unchanged?
      ↓
YES
→ Correction
→ same canonical identity
→ new version where appropriate

NO
→ new canonical object
→ explicit relationship to predecessor
→ predecessor preserved
```

Special Attestor rules:

> **Materially changed assertion = new Attestation**

> **Changed conclusion = new Trust Statement**

---

# VI. Relationship Vocabulary Matrix

| Relationship | Controlled Meaning |
|---|---|
| **references** | Points to or identifies another object |
| **derived-from** | Originates from or was generated from another object |
| **supports** | Provides substantive evidentiary or logical support |
| **evaluates** | Process acts upon a subject/object |
| **results-in** | Process produces an outcome, state, or output |
| **supersedes** | Replaces another object/version in operative standing |
| **corrects** | Repairs an error or defect in an earlier object/version |
| **related-to** | Generic association where no stronger relationship applies |

Core distinctions:

> **REFERENCE ≠ DERIVATION ≠ SUPPORT**

> **EVALUATES ≠ RESULTS-IN**

> **SUPERSEDES ≠ CORRECTS**

> **RELATED-TO is a fallback, not the default.**

---

# VII. Authority Vocabulary Matrix

| Context | Authority Rule |
|---|---|
| Reference | Does not transfer authority |
| Registration | Does not transfer source authority |
| Chronicle preservation | Historical authority ≠ source authority |
| Anchor integrity | Integrity authority ≠ content authority |
| Beacon discovery | Discovery authority ≠ source authority |
| Derivation | Does not transfer source authority |
| Support | Does not transfer source authority |
| Evaluation | Evaluation authority ≠ source authority |
| Navigator coordination | Coordination does not transfer institutional authority |
| Publication | Does not transfer authority |
| Provenance | May locate authority, but does not create it |
| Representation | Does not replace source identity |
| Version | Does not transfer authority |
| Identifier | Does not independently establish authority |

The two primary Suite rules are:

> **CONNECTION ≠ IDENTITY**

> **REFERENCE DOES NOT TRANSFER AUTHORITY**

---

# VIII. Validation / Eligibility / Conformance / Verification Matrix

| Term | Core Question |
|---|---|
| **Eligibility** | May this enter the governed process? |
| **Validation** | Does this object/process meet its institutional requirements? |
| **Conformance** | Does it satisfy this explicitly identified requirement set? |
| **Verification** | Does it match the defined evidence/reference basis? |
| **Certification** | What governed certification determination does Certifier issue? |
| **Evaluation** | What conclusion follows from applying the defined evaluation rules? |

These terms remain distinct.

Especially:

> **Eligible ≠ Valid**

> **Valid ≠ Conformant by definition**

> **Verified ≠ Certified**

> **NOT-TESTED ≠ PASS**

---

# IX. Outcome / Status Matrix

Substantive result and object condition must remain separate.

Example:

```text
Evaluation Outcome: Supported
Lifecycle State: Active
Publication State: Published
```

These describe three different dimensions.

Preferred labels include:

- Lifecycle State
- Publication State
- Validation Result
- Conformance Result
- Certification Outcome
- Evaluation Outcome
- Eligibility Determination
- Workflow Status
- Institutional Status

Avoid unqualified generic **Status** where ambiguity exists.

---

# X. Truth / Trust / Scoring Vocabulary

## Truth Before Trust

May remain as historical or philosophical doctrine.

It should mean:

> governed evidence and evaluation should precede trust conclusions.

It does **not** establish universal truth authority.

## Trust Standard

May remain if it is the proper historical title of a specific artifact.

Current generic usage should not imply one omnibus Suite-wide trust authority.

## Trust Statement

Attestor canonical object representing a bounded governed conclusion.

> **Trust Statement ≠ Truth Declaration**

> **Trust Statement ≠ Universal Trust Rating**

## Trust Score

No generalized Suite-wide scoring authority currently exists.

> **Evaluation authority ≠ scoring authority**

Any future scoring model requires explicit architecture.

## Trusted

Should not be used as an unqualified universal Suite status.

Prefer the actual governed result and statement.

---

# XI. Legacy-to-Mature Terminology Mapping

| Legacy / Ambiguous Term | Mature Treatment |
|---|---|
| Registry Record | Prefer **Satoshium Registry Entry (SREG)** |
| Jurisdiction Intelligence Record | Conceptual only; canonical object is **Jurisdiction Intelligence Package** |
| Trust Signal | Non-canonical indicator terminology |
| Beacon trust signal | Correct to **Discovery Signal** where Beacon object is intended |
| Trust Statement | Preserve as formal Attestor canonical object |
| Trust Layer | Historical/capability taxonomy, not current formal Suite authority layer |
| Trust Standard | Preserve named historical artifact; otherwise use precise governing-standard terminology |
| Trusted | Avoid as generic universal status |
| Trust Score | No generalized scoring authority unless explicitly defined |
| Truth Authority | No current Suite institution holds universal truth authority |
| Registry authority over source | Not valid |
| Chronicle source authority | Not valid |
| Beacon source authority | Not valid |
| Attestor universal trust authority | Not valid |

---

# XII. Canonical Identifier Principles

Known formal families:

| Institution | Identifier |
|---|---|
| Certifier | `SC-CERT-YYYY-NNNN` |
| Registry | `SREG-YYYY-NNNN` |
| Chronicle | `CHR-YYYY-NNNN` |
| Anchor | `ANCH-YYYY-NNNN` |
| Beacon | `BEAC-YYYY-NNNN` |
| Attestor — Attestation | `ATT-YYYY-NNNN` |
| Attestor — Trust Statement | `TRST-YYYY-NNNN` |

No identifier should independently imply:

- authority beyond its namespace;
- lifecycle state;
- publication;
- validity;
- conformance;
- evaluation outcome;
- relationship;
- version.

Matching numeric sequences across institutions do not create a relationship.

For example:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
```

are separate canonical identities.

The shared `0001` does not establish lineage.

---

# XIII. Suite Canonical Object Hierarchy

```text
Satoshium Suite
│
├── Atlas
│   └── Jurisdiction Intelligence Package
│
├── Navigator
│   └── Navigator Workflow Definition
│
├── Certifier
│   └── Certification Package
│
├── Registry
│   └── Satoshium Registry Entry
│
├── Chronicle
│   └── Chronicle Entry
│
├── Anchor
│   └── Integrity Reference
│
├── Beacon
│   └── Discovery Signal
│
└── Attestor
    ├── Attestation
    └── Trust Statement
```

This is the reconciled canonical object model for the eight formal Suite institutions.

---

# XIV. Suite-Wide Governing Semantic Rules

The reconciliation establishes the following consolidated rules:

1. **Canonical Object** is the Suite-wide architectural umbrella term.
2. Each canonical object remains owned by its governing institution.
3. **Canonical Creation ≠ Lifecycle Activation ≠ Publication.**
4. **Eligibility ≠ Validation.**
5. **Validation ≠ Conformance.**
6. **Verification ≠ Certification.**
7. **Evaluation ≠ Evaluation Outcome.**
8. **Evaluation Outcome ≠ Trust Statement.**
9. **Outcome ≠ Lifecycle State.**
10. **Correction ≠ Version.**
11. **Correction ≠ Deletion.**
12. **Supersession ≠ Mutation.**
13. **Changed Conclusion = Changed Canonical Statement.**
14. **Reference ≠ Derivation ≠ Support.**
15. **Evaluates ≠ Results-In.**
16. **Supersedes ≠ Corrects.**
17. **Connection ≠ Identity.**
18. **Reference does not transfer authority.**
19. Registration does not transfer source authority.
20. Historical preservation does not transfer source authority.
21. Integrity preservation does not transfer content authority.
22. Discovery does not transfer source authority.
23. Derivation does not transfer source authority.
24. Evaluation does not transfer source authority.
25. Coordination does not transfer institutional authority.
26. Publication does not transfer authority.
27. Provenance may identify authority but does not create it.
28. Representation does not replace canonical source identity.
29. Identifier does not independently establish authority, status, outcome, or relationship.
30. **NOT-TESTED ≠ PASS.**
31. Trust Statement is a bounded Attestor conclusion, not universal truth.
32. Evaluation authority does not imply scoring authority.
33. No formal current Suite institution possesses universal truth authority.
34. Legacy terminology should be preserved historically where accurate, but current-state documentation should use mature terms.
35. **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# XV. Final Reconciled Suite Matrix

| Institution | Canonical Object | Institutional Authority | Must Not Be Mistaken For |
|---|---|---|---|
| Atlas | Jurisdiction Intelligence Package | Authoritative Intelligence | Beacon Discovery Signal; Attestor Trust Statement |
| Navigator | Navigator Workflow Definition | Workflow Definition / Orchestration | Authority over participating institutions |
| Certifier | Certification Package | Operational Certification | Verification alone; lifecycle status |
| Registry | Satoshium Registry Entry | Canonical Registration | Source-record ownership |
| Chronicle | Chronicle Entry | Historical Preservation | Authority over source object |
| Anchor | Integrity Reference | Integrity Preservation | Truth, certification, trust |
| Beacon | Discovery Signal | Discovery & Signals | Trust Statement; source authority |
| Attestor | Attestation; Trust Statement | Governed Attestation & Rule-Constrained Evaluation | Universal truth authority; universal trust authority; generalized scoring authority |

---

# Final Disposition

**SUITE CANONICAL VOCABULARY & OBJECT MATRIX — COMPLETE — APPROVED**

The mature Suite now has a single reconciled vocabulary and canonical-object model across all eight formal institutions.

The central architectural principle is:

> **Each institution governs its own canonical objects and determinations. Relationships establish traceability and interoperability without collapsing identity or transferring authority.**

The shortest governing pair remains:

> **CONNECTION ≠ IDENTITY.**

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

This record completes the **Suite Canonical Vocabulary & Object Matrix** deliverable and completes the substantive **Saturday Phase II — Objects, Terminology & Semantics** reconciliation work.
