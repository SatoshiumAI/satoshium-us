# Satoshium Suite Reconciliation — Canonical Object Audit

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record documents the Suite-wide Canonical Object Audit conducted during the September 26, 2026 phase of the Satoshium Suite Reconciliation.

The audit tested the mature operational object model of each formal Suite institution and clarified the distinction between:

- canonical institutional objects;
- contained determinations or classifications;
- supporting records and metadata;
- operational functions and processes;
- lifecycle or workflow state;
- derived or public representations;
- source records owned by other institutions.

The governing principles remain:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

> **COORDINATION DOES NOT TRANSFER AUTHORITY.**

> **Institutional role ≠ canonical object.**

---

## 1. Certifier

### Canonical Object
**Certification Package**

### Institutional Role
Operational Certification

### Determination
**CONFIRMED**

The Certification Package is the single canonical Certifier object representing one governed certification action.

The Certification Decision is contained within the Certification Package and is not a competing canonical object.

Supporting or derived artifacts include:

- Evidence Records / SEV
- Evidence Inventory
- Evidence Mapping
- SCPR
- SCR
- SCRD HTML
- SCRD JSON

Suite Standards and Suite Methodology are governing inputs to certification and are not Certifier-owned canonical objects.

### Authority Boundary
Certifier is authoritative for the certification action and Certification Decision. The originating institution retains authority over the source object being certified.

---

## 2. Registry

### Canonical Object
**Satoshium Registry Entry (SREG)**

### Institutional Role
Canonical Registration / Public Catalog

### Determination
**RECONCILED**

The preferred formal canonical term is **Satoshium Registry Entry (SREG)**.

“Registry Record” may remain as legacy or generic descriptive language, but it should not be used as the preferred canonical object name.

The mature hierarchy is:

```text
Satoshium Registry
        ↓
Satoshium Registry Entry (SREG)
        ↓
Registry Record Type
        ↓
Authoritative Source Record
```

Registry Record Type is a classification, not a canonical object.

The public Catalog / Registered Items surface is a presentation and discovery layer around SREGs, not a separate object family.

### Authority Boundary
Registry owns registration identity, Registry metadata, Registry relationships, Registry lifecycle, versioning, correction, and publication.

The originating institution retains authority over the underlying Source Record.

> **REGISTRATION DOES NOT TRANSFER SOURCE AUTHORITY.**

---

## 3. Chronicle

### Canonical Object
**Chronicle Entry**

### Identifier Family
**CHR-YYYY-NNNN**

### Institutional Role
Historical Preservation

### Determination
**CONFIRMED**

The Chronicle Entry is Chronicle’s governed historical-preservation representation of a qualifying Occurrence.

The Occurrence itself is the represented subject and is not the Chronicle-owned canonical object.

Supporting concepts include:

- Preservation Eligibility
- Event Type
- Sources
- Evidence
- Provenance
- Relationships
- Verification
- Validation
- Lifecycle State
- Publication State

### Authority Boundary
Chronicle is authoritative for its historical representation and preservation lifecycle.

It does not inherit authority over the source object involved in the historical occurrence.

> **Historical authority ≠ source authority.**

---

## 4. Anchor

### Canonical Object
**Integrity Reference**

### Institutional Role
Integrity Preservation

### Determination
**CONFIRMED**

An Integrity Reference is Anchor’s governed record for the integrity-preservation state of a specifically defined representation of a source artifact.

The Integrity Subject is defined by:

```text
Source Artifact identity
        +
Canonical Representation
        +
Representation Boundary
```

Supporting integrity materials may include:

- hashes;
- algorithms;
- signatures;
- timestamps;
- canonicalization methods;
- external commitments;
- provenance;
- verification material.

These are supporting components and are not separate canonical objects.

### Verification and Validation
Verification compares a representation against preserved integrity evidence.

Validation determines whether the Integrity Reference satisfies Anchor requirements.

> **Verification ≠ Validation**

### Authority Boundary
Anchor is authoritative for integrity preservation and Anchor-controlled integrity metadata.

It is not authoritative for the substantive meaning, truth, certification, or trustworthiness of the source object.

> **INTEGRITY ≠ TRUTH**  
> **INTEGRITY ≠ CERTIFICATION**  
> **INTEGRITY ≠ TRUST**

---

## 5. Beacon

### Canonical Object
**Discovery Signal**

### Supporting Layer
**Discovery Metadata**

### Institutional Role
Discovery & Signals

### Determination
**CONFIRMED / CLARIFIED**

The Discovery Signal is the single canonical Beacon object.

Discovery Metadata is a governed supporting metadata layer and is not an independent canonical object.

Supporting structures may include:

- source references;
- provenance;
- subject;
- Signal Type;
- relevance context;
- timestamps;
- status;
- version information;
- relationships;
- publication information;
- indexing fields.

Signal Type is classification.

Indexes, Queries, Results, and public Records surfaces are operational or presentation structures, not canonical Beacon object families.

### Authority Boundary
Beacon owns the Discovery Signal and Beacon-created Discovery Metadata.

The source institution or external source retains source authority.

> **DISCOVERY DOES NOT TRANSFER SOURCE AUTHORITY.**

---

## 6. Attestor — Attestation

### Canonical Object
**Attestation**

### Identifier Family
**ATT-YYYY-NNNN**

### Determination
**CONFIRMED**

An Attestation is a governed, attributable assertion admitted into Attestor for evaluation.

The Attestation is distinct from:

- the source object;
- the asserted proposition considered in isolation;
- eligibility;
- Rule-Constrained Evaluation;
- Evaluation Outcome;
- Trust Statement.

The canonical flow is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
```

### Identity Rule
A materially changed assertion requires a new Attestation.

---

## 7. Attestor — Evaluation Outcome

### Object Type
**Controlled Evaluation Result**

### Canonical Object
**No**

### Determination
**CLARIFIED**

Evaluation Outcome is the controlled result produced by Rule-Constrained Evaluation.

It is not a third canonical Attestor object.

The architecture is:

```text
Attestation
    ↓
Rule-Constrained Evaluation
    ↓
Evaluation Outcome
    ↓
Trust Statement
```

Key distinctions:

> **Evaluation Outcome ≠ Trust Statement**  
> **Evaluation Outcome ≠ Validation Result**  
> **Eligibility ≠ Evaluation Outcome**  
> **Evaluation Outcome ≠ Conformance Determination**

---

## 8. Attestor — Trust Statement

### Canonical Object
**Trust Statement**

### Identifier Family
**TRST-YYYY-NNNN**

### Primary Institutional Output
**Yes**

### Determination
**CONFIRMED**

A Trust Statement is Attestor’s governed, attributable, bounded conclusion produced after Rule-Constrained Evaluation of an Attestation.

The Trust Statement is distinct from the Evaluation Outcome.

The Evaluation Outcome is a controlled classification. The Trust Statement is the canonical institutional object expressing the bounded conclusion.

### Derivation
```text
Trust Statement
    derived-from
Attestation
```

Derivation does not collapse identity.

### Identity Rule
> **Changed Conclusion = Changed Canonical Statement**

A materially changed conclusion requires a new Trust Statement and new TRST identifier.

### Authority Boundary
Attestor owns the bounded evaluative conclusion expressed by the Trust Statement.

It does not acquire authority over referenced source objects.

---

## 9. Atlas

### Canonical Object
**Jurisdiction Intelligence Package**

### Institutional Role
Authoritative Intelligence

### Determination
**RECONCILED**

Representative review of the El Salvador country package and California state package confirmed a common Atlas package architecture.

The Jurisdiction Intelligence Package is the canonical governed Atlas object.

The phrase **Jurisdiction Intelligence Record** may remain as a conceptual description of the information embodied by the package, but it is not treated as a separate co-equal canonical object.

### Canonical Package Components

A Jurisdiction Intelligence Package may include governed component layers such as:

- Evidence Layer
- Signal Layer
- Trust Dimensions
- Profile
- Builder Mode
- Topology Metadata
- Change Log

Representative package derivation follows the general pattern:

```text
Evidence
   ↓
Signals
   ↓
Trust Dimensions
   ↓
Profile / Builder Mode
```

Metadata and Change Log provide structural and provenance support.

These component files are governed internal package components, not separate institutional canonical object families.

### Derived Representations

Public HTML renderings and JSON serializations are derived representations of the package.

They are not separate canonical Atlas objects.

### Cross-Institution Terminology Boundary

> **Atlas Signal ≠ Beacon Discovery Signal**

> **Atlas Trust Dimension ≠ Attestor Trust Statement**

### Audit Coverage

Representative review of one country package and one state package was sufficient to confirm the shared object architecture for the current Canonical Object Audit.

The remaining Atlas packages do not require individual audit unless a materially different package family is later identified.

---

## 10. Navigator

### Canonical Object
**Navigator Workflow Definition**

### Institutional Role
Workflow Definition / Orchestration

### Operational Function
**Workflow Orchestration**

### Determination
**RECONCILED**

The Navigator Workflow Definition is the canonical Navigator object.

Workflow Orchestration is the operational function that executes or coordinates the workflow definition.

The mature model is:

```text
Trigger / Query
      ↓
Navigator Workflow Definition
      ↓
Workflow Orchestration
      ↓
Participating Institutions
      ↓
Institution-owned canonical outputs
```

### Supporting Structures

The following are supporting frameworks, inputs, state, or derived outputs rather than co-equal canonical Navigator objects:

- Queries
- Triggers
- Schemas
- Templates
- Rules
- Filters
- Definitions
- Workflow State
- Status
- Outputs
- Completion Reporting

Schemas define structure.

Templates implement reusable structure.

Outputs are structured presentation products.

Workflow State is operational execution state and remains distinct from canonical institutional state.

### Authority Boundary

Navigator may:

- select or initiate workflows;
- determine participating institutions;
- coordinate execution order;
- pass references and workflow context;
- monitor progress;
- identify incomplete activities;
- track workflow state;
- report completion.

Navigator does not own the canonical objects created by participating institutions.

> **COORDINATION DOES NOT TRANSFER AUTHORITY.**

---

# Reconciled Suite Canonical Object Model

| Institution | Canonical Object(s) | Primary Function |
|---|---|---|
| Atlas | Jurisdiction Intelligence Package | Authoritative Intelligence |
| Navigator | Navigator Workflow Definition | Workflow Orchestration |
| Certifier | Certification Package | Operational Certification |
| Registry | Satoshium Registry Entry (SREG) | Canonical Registration / Public Catalog |
| Chronicle | Chronicle Entry | Historical Preservation |
| Anchor | Integrity Reference | Integrity Preservation |
| Beacon | Discovery Signal | Discovery & Signals |
| Attestor | Attestation; Trust Statement | Governed Attestation & Rule-Constrained Evaluation |

---

# Non-Canonical but Governed / Supporting Constructs

The following were explicitly reviewed and should not be treated as competing canonical Suite objects:

- Certification Decision
- Registry Record Type
- Occurrence
- Preservation Eligibility
- Event Type
- hashes / signatures / timestamps
- Discovery Metadata
- Signal Type
- Eligibility
- Evaluation Outcome
- Rule-Constrained Evaluation
- Atlas Evidence / Signals / Trust Dimensions / Profile / Builder Mode / Metadata / Change Log
- Navigator Schemas / Templates / Definitions / Workflow State / Outputs

---

# Suite-Wide Canonical Object Rules

1. Each formal Suite institution owns its own canonical objects.
2. A referenced object remains authoritative in its originating institution.
3. Supporting records do not become canonical merely because they are governed.
4. Classifications do not become canonical objects.
5. Operational functions do not become canonical objects.
6. Lifecycle or workflow state does not become a canonical object.
7. Derived renderings and serializations do not become canonical objects.
8. Reference does not transfer authority.
9. Coordination does not transfer authority.
10. Connection does not create identity.
11. Derivation does not collapse identity.
12. Changed canonical meaning may require a new canonical object identity according to institution-specific rules.

---

# Final Disposition

**Canonical Object Audit — COMPLETE — APPROVED**

This record closes the September 26, 2026 Canonical Object Audit portion of Phase II of the Satoshium Suite Reconciliation.

The next Phase II task is the **Identifier-Family Audit**.
