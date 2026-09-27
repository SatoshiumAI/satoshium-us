# Satoshium Suite Reconciliation — Institutional Architecture Matrix

**Date:** September 25, 2026  
**Phase:** Phase I — Baseline & Institutional Architecture  
**Decision Class:** RECONCILE / CONSOLIDATE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record establishes the first Suite-wide institutional architecture matrix for the completed Satoshium Suite.

The matrix reconciles, side-by-side, each institution's:

- institutional role;
- authority domain;
- canonical object responsibility;
- principal inputs;
- principal outputs;
- operational status.

The purpose is to create one agreed architectural baseline from which all later reconciliation work proceeds.

The governing rule is:

> **Each institution must retain a distinct role, distinct authority boundary, and distinct canonical responsibility.**

---

## Formal Suite Roster

The formal Satoshium Suite consists of exactly eight institutions:

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

All eight are:

> **Operational**

Aegis remains:

> **External / Pre-Suite**

---

# Institutional Architecture Matrix

| Institution | Role | Authority | Canonical Object | Principal Inputs | Principal Outputs | Status |
|---|---|---|---|---|---|---|
| **Atlas** | Authoritative Intelligence | Governs authoritative jurisdiction intelligence within its defined scope | Jurisdiction Intelligence Package | Evidence, authoritative sources, jurisdiction data, governed signals and source material | Jurisdiction Intelligence Package and approved representations/serializations | Operational |
| **Navigator** | Workflow Definition / Orchestration | Governs workflow definition, routing, coordination, and workflow state; does not inherit participating institutions' substantive authority | Navigator Workflow Definition | Workflow triggers, references, governed inputs, institutional endpoints, workflow rules | Workflow coordination, routing, state, completion reporting, references to institutional outputs | Operational |
| **Certifier** | Operational Certification | Governs certification process, certification evidence, Certification Decision, and Certification Package | Certification Package | Applicable Standards, Methodology, evidence, jurisdiction/source intelligence, governed subject matter | Certification Package and subordinate certification artifacts | Operational |
| **Registry** | Canonical Registration / Public Catalog | Governs canonical registration, Registry identity, Registry classification, and Registry publication | Satoshium Registry Entry (SREG) | Qualifying source object, source identity, source institution, provenance, registration metadata | SREG, Registry metadata, catalog representation | Operational |
| **Chronicle** | Historical Preservation | Governs preservation eligibility, historical representation, event classification, and Chronicle Entry lifecycle | Chronicle Entry | Qualifying occurrence, source references, temporal evidence, provenance | Chronicle Entry and historical record | Operational |
| **Anchor** | Integrity Preservation | Governs Integrity Subjects, canonical representations, representation boundaries, integrity records, and verification of protected representations | Integrity Reference | Source artifact, canonical representation, representation boundary, integrity metadata | Integrity Reference and verification result | Operational |
| **Beacon** | Discovery & Signals | Governs discovery, Discovery Signals, Discovery Metadata, discovery provenance, and Beacon lifecycle/publication | Discovery Signal | Observable source object, relevant condition/change/state, source provenance | Discovery Signal and Discovery Metadata | Operational |
| **Attestor** | Governed Attestation & Rule-Constrained Evaluation | Governs eligibility under Attestor rules, Attestations, Evaluation Basis, Rule-Constrained Evaluation, Evaluation Outcomes, and Trust Statements | Attestation; Trust Statement | Eligible governed inputs, attributable assertion, applicable rules, evidence, provenance | Evaluation Outcome and Trust Statement | Operational |

---

# Institution-by-Institution Architectural Position

## Atlas

### Role

> **Authoritative Intelligence**

### Authority Boundary

Atlas is authoritative for the governed jurisdiction intelligence it produces.

It does not become:

- certification authority;
- registration authority;
- historical authority;
- integrity authority;
- discovery authority;
- Attestor evaluation authority.

### Canonical Responsibility

> **Jurisdiction Intelligence Package**

### Principal Inputs

```text
Authoritative sources
Evidence
Jurisdiction data
Governed signals
Source material
```

### Principal Outputs

```text
Jurisdiction Intelligence Package
Approved public representation
Derived JSON serialization where applicable
Supporting evidence / signals / profile structures
```

### Architectural Boundary

> **Atlas provides authoritative intelligence where applicable; it is not a universal prerequisite or Suite-wide superior authority.**

---

## Navigator

### Role

> **Workflow Definition / Orchestration**

### Authority Boundary

Navigator governs workflow structure and coordination.

It does not inherit the authority of any participating institution.

### Canonical Responsibility

> **Navigator Workflow Definition**

### Principal Inputs

```text
Workflow trigger
Institutional references
Governed inputs
Workflow rules
Schemas
Templates
Queries
Filters
```

### Principal Outputs

```text
Workflow routing
Workflow state
Institutional handoffs
Completion reporting
References to institutional outputs
```

### Architectural Boundary

> **Navigator coordinates. Participating institutions decide and act.**

And:

> **Workflow State ≠ Canonical Institutional State.**

---

## Certifier

### Role

> **Operational Certification**

### Authority Boundary

Certifier governs certification.

It owns:

- certification evidence handling;
- certification process;
- Certification Decision;
- Certification Package.

It does not own Suite Standards or Suite Methodology.

### Canonical Responsibility

> **Certification Package**

### Principal Inputs

```text
Suite Standards
Suite Methodology
Evidence
Governed subject matter
Atlas intelligence where applicable
```

### Principal Outputs

```text
Certification Package
Certification Decision
Supporting certification records
SCPR / SCR / SCRD representations
```

### Architectural Boundary

```text
Suite Standards define expectations.
Suite Methodology defines implementation.
Certifier performs certification.
```

---

## Registry

### Role

> **Canonical Registration / Public Catalog**

### Authority Boundary

Registry governs registration of qualifying source objects.

It does not absorb source authority.

### Canonical Responsibility

> **Satoshium Registry Entry (SREG)**

### Principal Inputs

```text
Qualifying source object
Source identifier
Source institution
Registry Record Type
Provenance
Registration metadata
```

### Principal Outputs

```text
SREG
Registry metadata
Catalog representation
Registry lifecycle and publication state
```

### Architectural Boundary

> **Registration does not transfer source authority.**

---

## Chronicle

### Role

> **Historical Preservation**

### Authority Boundary

Chronicle governs the historical record it creates.

It does not become authoritative for another institution's substantive source object.

### Canonical Responsibility

> **Chronicle Entry**

### Principal Inputs

```text
Qualifying occurrence
Temporal evidence
Source references
Historical provenance
Event classification
```

### Principal Outputs

```text
Chronicle Entry
Historical representation
Preserved occurrence record
```

### Architectural Boundary

> **Chronicle records when.**

And:

> **Historical authority ≠ source authority.**

---

## Anchor

### Role

> **Integrity Preservation**

### Authority Boundary

Anchor governs the integrity of the exact protected representation within the declared representation boundary.

It does not establish:

- truth;
- certification;
- package completeness;
- whole-package integrity unless explicitly defined.

### Canonical Responsibility

> **Integrity Reference**

### Principal Inputs

```text
Source Artifact Identity
Canonical Representation
Representation Boundary
Integrity metadata
```

### Principal Outputs

```text
Integrity Reference
Integrity verification result
Integrity provenance
```

### Architectural Boundary

> **Integrity is bounded to the representation actually protected.**

---

## Beacon

### Role

> **Discovery & Signals**

### Authority Boundary

Beacon governs discovery and signaling.

It does not become:

- verifier;
- Certifier;
- Registry;
- historical authority;
- Attestor trust authority.

### Canonical Responsibility

> **Discovery Signal**

### Principal Inputs

```text
Observable source object
Relevant condition
State
Change
Source provenance
```

### Principal Outputs

```text
Discovery Signal
Discovery Metadata
Discovery provenance
Beacon lifecycle / publication state
```

### Architectural Boundary

> **Discovery ≠ Determination.**

---

## Attestor

### Role

> **Governed Attestation & Rule-Constrained Evaluation**

### Authority Boundary

Attestor governs:

- input eligibility under Attestor rules;
- Attestations;
- Evaluation Basis;
- Rule-Constrained Evaluation;
- Evaluation Outcomes;
- Trust Statements.

It does not gain universal truth, certification, registration, source, or scoring authority.

### Canonical Responsibility

```text
Attestation
Trust Statement
```

### Principal Inputs

```text
Eligible Governed Inputs
Attributable assertion
Applicable rules
Evidence
Provenance
```

### Principal Outputs

```text
Evaluation Outcome
Trust Statement
```

### Architectural Boundary

> **Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement.**

---

# Cross-Suite Authority Boundaries

The matrix establishes the following non-transfer rules:

```text
Atlas intelligence
≠ Certification

Navigator orchestration
≠ Institutional authority

Certification
≠ Registration

Registration
≠ Historical preservation

Historical preservation
≠ Integrity preservation

Integrity preservation
≠ Discovery

Discovery
≠ Trust determination

Evaluation
≠ Source authority
```

The two strongest governing principles are:

> **CONNECTION ≠ IDENTITY**

and:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# Canonical Object Ownership Matrix

```text
Atlas
→ Jurisdiction Intelligence Package

Navigator
→ Navigator Workflow Definition

Certifier
→ Certification Package

Registry
→ Satoshium Registry Entry

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Beacon
→ Discovery Signal

Attestor
→ Attestation
→ Trust Statement
```

Supporting structures do not become competing canonical objects merely because they are named.

Examples:

```text
Workflow Orchestration
→ function

Certification Decision
→ determination within Certifier architecture

Registry Record Type
→ classification

Occurrence
→ Chronicle subject

Integrity Subject
→ protected subject definition

Discovery Metadata
→ supporting Beacon layer

Evaluation Outcome
→ controlled Attestor result
```

---

# Inputs and Outputs Are Relationships, Not Transfers of Authority

An output from one institution may become an input to another.

That does not transfer ownership.

Example:

```text
Certification Package
        ↓ referenced by
Registry
        ↓
SREG
```

The Registry owns the SREG.

Certifier continues to own the Certification Package.

Likewise:

```text
Discovery Signal
        ↓ referenced by
Attestor
```

does not make Attestor the owner of the Discovery Signal.

Therefore:

> **Input use ≠ authority transfer.**

---

# Operational Status

All eight formal institutions are:

```text
Operational
```

The completed Suite is therefore:

```text
8 formal institutions
8 operational institutions
```

No institution is currently classified as Development.

---

# Aegis Boundary

Aegis is deliberately excluded from the formal institutional matrix.

Its reconciled position is:

```text
Aegis
→ External / Pre-Suite
```

Aegis may remain historically important and architecturally relevant to the broader Satoshium ecosystem.

It is not one of the eight formal Suite institutions.

---

# Relationship to the Legacy System Registry

The legacy `SYS-*` System Registry is not a ninth institution and is not the formal Registry.

Its reconciled position is:

```text
SYS-*
→ Legacy / Pre-Suite Platform System Index

SREG-*
→ Formal Satoshium Registry object family
```

Therefore:

> **SYS ≠ SREG**

---

# Relationship to Legacy Layer Models

Legacy architecture such as:

```text
Trust Layer
Knowledge Layer
Intelligence Layer
Signal Layer
Agent Layer
Simulation Layer
Interface Layer
AI Platform Layer
```

may remain historically or conceptually useful.

These are not the current formal institutional architecture.

The institutional matrix takes precedence for current Suite descriptions.

---

# Baseline Architectural Rules

The matrix establishes the following Phase I baseline:

1. The formal Suite consists of eight institutions.
2. All eight are Operational.
3. Aegis remains external / pre-Suite.
4. Each institution has one distinct institutional role.
5. Each institution has a bounded authority domain.
6. Each institution owns a defined canonical object or object family.
7. Supporting structures do not become competing canonical objects.
8. Inputs and outputs may cross institutions without transferring authority.
9. Registration does not transfer source authority.
10. Historical preservation does not transfer source authority.
11. Integrity preservation does not create content authority.
12. Discovery does not create source or trust authority.
13. Attestor evaluation does not rewrite source authority.
14. Navigator coordination does not create institutional authority.
15. Legacy capability layers do not replace the formal institutional model.
16. `SYS-*` remains distinct from formal Registry `SREG-*`.

---

## Day-Close Use

This matrix serves as the agreed institutional baseline for subsequent reconciliation.

All later work should test terminology, lifecycle, relationships, dependencies, and whole-Suite architecture against this institutional model rather than against older platform or layer descriptions.

---

## Final Disposition

# INSTITUTIONAL ARCHITECTURE MATRIX — COMPLETE — APPROVED

The Satoshium Suite baseline is reconciled as eight operational institutions with distinct roles, authority boundaries, canonical responsibilities, inputs, outputs, and operational status.

This matrix establishes the Phase I institutional model from which later Suite Reconciliation proceeds.
