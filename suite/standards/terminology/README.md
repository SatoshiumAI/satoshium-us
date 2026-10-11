# Satoshium Terminology Standard

**Path:** `/suite/standards/terminology/`  
**Surface:** Satoshium Suite · Standards · Terminology  
**Status:** Current repository documentation

## Purpose

This directory documents the **Satoshium Terminology Standard**, the Suite-wide standards layer governing official vocabulary, naming conventions, controlled terminology, governance vocabulary, and cross-reference semantics.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Standard Role

The Terminology Standard establishes the common language used throughout the Satoshium Suite.

Its purpose is to reduce ambiguity across:

- documentation;
- standards;
- methodology;
- schemas;
- identifiers;
- public interfaces;
- canonical records; and
- cross-institution relationships.

Within the Suite architecture:

- **Standards define expectations.**
- **Methodology defines implementation.**
- **Terminology defines the governed meaning of the language used to describe both.**

Terminology does not transfer institutional authority merely by defining a term.

## Official Definitions

Official Definitions establish the canonical meaning of Suite terms.

Definitions should preserve clear distinctions between concepts such as:

- certification;
- evidence;
- validation;
- eligibility;
- evaluation;
- conformance;
- publication;
- attestation;
- Trust Statement;
- Integrity Reference;
- Registry Entry;
- Discovery Signal;
- lifecycle state;
- correction;
- supersession;
- provenance;
- Suite Governance;
- Institutional Governance;
- Institutional Sovereignty;
- Routine Change;
- Material Change;
- Constitutional Change;
- Governed Subject;
- Canonical Ownership;
- Authority Transfer;
- Governance Decision Record (GDR);
- Governance Decision Register;
- Architecture Reconciliation; and
- Constitutional Admission.

Where a term has a governed institutional meaning, documentation should not casually broaden or weaken that meaning.

## Governance Vocabulary

The October 11, 2026 Satoshium Suite Governance Review established the following governed vocabulary.

### Suite Governance

**Suite Governance** protects the constitutional whole.

It governs shared constitutional boundaries, including:

- formal Suite membership;
- institutional role assignment;
- canonical ownership assignment;
- authority allocation;
- constitutional dependencies;
- institutional structural change; and
- other matters whose governed subject is the Suite itself.

Suite Governance does not become routine operational authority over institution-owned work.

### Institutional Governance

**Institutional Governance** governs the work and decisions that belong to an institution within its settled authority.

It includes institution-owned responsibilities such as:

- canonical object stewardship;
- lifecycle decisions;
- Corrections;
- Versioning;
- institution-specific Rules;
- institution-specific Policies;
- institution-specific Procedures; and
- institution-specific determinations.

### Institutional Sovereignty

**Institutional Sovereignty** means that each formal Suite institution retains distinct authority over its settled operational domain and canonical responsibilities, subject to applicable Suite-level constitutional constraints.

```text
INSTITUTIONAL SOVEREIGNTY
≠ UNLIMITED AUTHORITY

SUITE CONSTRAINT
≠ SUITE OWNERSHIP
```

### Governed Subject

The **Governed Subject** is the thing whose authority, state, rule, object, process, or constitutional condition is being governed.

The controlling rule is:

> **Authority follows the governed subject.**

### Routine Change

A **Routine Change** is a change that remains within settled authority and does not materially alter shared architecture, canonical ownership, institutional role, or constitutional boundaries.

Routine change may remain within the owning institution or standards-maintenance authority.

### Material Change

A **Material Change** affects a governed subject in a way that requires broader review because of meaningful shared impact, compatibility consequences, or cross-institution effects.

For institution-owned Material change:

```text
Institution
→ retains determination / approval authority

Suite
→ performs coherence / shared-impact review
```

Suite review does not automatically create co-ownership or co-approval authority.

### Constitutional Change

A **Constitutional Change** alters the formal Suite architecture, including matters such as:

- institutional membership;
- institutional role;
- canonical ownership;
- authority allocation;
- institutional merger, division, retirement, removal, or successor status; or
- other changes to settled constitutional boundaries.

Constitutional Change requires Formal Suite Governance.

### Canonical Ownership

**Canonical Ownership** is the governed authority over a canonical object's identity, lifecycle, correction, Versioning, publication, and substantive canonical state.

```text
SHARED CUSTODY
≠ SHARED OWNERSHIP

MULTIPLE REPRESENTATIONS
≠ MULTIPLE AUTHORITIES
```

Canonical ownership may change only through explicit Constitutional Governance.

### Authority Transfer

**Authority Transfer** is an explicit governed reassignment of authority from one constitutional or institutional owner to another.

Authority transfer does not arise merely from:

- reference;
- registration;
- workflow participation;
- orchestration;
- interoperability;
- technical dependency;
- Suite membership;
- review participation; or
- repeated practice.

### Governance Decision Record (GDR)

A **Governance Decision Record (GDR)** is the formal record of a governed governance decision.

A GDR preserves:

- decision identity;
- governed subject;
- classification;
- determination;
- approval;
- effective standing;
- affected institutions or objects where applicable;
- supersession / correction relationships; and
- historical traceability.

```text
GDR IDENTITY
≠ DOCUMENT VERSION
```

### Governance Decision Register

The **Governance Decision Register** is the authoritative index of formal governance decisions.

It provides both:

```text
CURRENT-STATE INDEX
+
HISTORICAL-LINEAGE INDEX
```

The current controlling Suite Governance decision is:

```text
GDR-2026-0026
→ Satoshium Suite Governance Model
→ APPROVED
→ EFFECTIVE
```

### Architecture Reconciliation

**Architecture Reconciliation** is the governed review used when a material contradiction, ambiguity, or proposed change may affect settled Suite architecture.

It may resolve or escalate questions involving:

- institutional role;
- canonical ownership;
- authority boundaries;
- relationship semantics;
- lifecycle semantics;
- constitutional dependency; or
- Suite membership.

Architecture Reconciliation is not ordinary documentation cleanup.

### Constitutional Admission

**Constitutional Admission** is the formal Suite Governance act by which a new institution becomes a formal member of the Satoshium Suite.

Operational maturity, public visibility, integration, branding, repeated use, or technical importance do not create Suite membership by themselves.

```text
NEW CAPABILITY
≠ NEW INSTITUTION

DE FACTO MEMBERSHIP
→ NOT RECOGNIZED
```

## Naming Conventions

Naming Conventions establish consistent treatment of:

- page names;
- directory names;
- schema names;
- identifiers;
- standards;
- methodology surfaces;
- canonical object names; and
- public interfaces.

Naming consistency should support discovery and interoperability without overriding established architecture.

A filename or label should not be normalized merely for cosmetic consistency when an existing governed architecture requires a different form.

## Controlled Vocabulary

Controlled Vocabulary identifies preferred, deprecated, ambiguous, synonymous, or context-sensitive terms.

Where terminology changes:

- deprecated language should be identified;
- historical usage should remain historically accurate;
- current documentation should use the current governed term;
- synonyms should not silently collapse distinct concepts; and
- a terminology change should not be treated as an architectural change unless meaning is actually being altered.

## Cross-Reference Terms

Cross-reference terminology defines how concepts relate across Suite institutions and governed records.

Relationship terms should preserve their exact meaning.

In particular:

- reference does not mean derivation;
- reference does not mean support;
- connection does not mean identity; and
- reference does not transfer authority.

Cross-reference language should not imply stronger relationships than the architecture actually establishes.

## Core Distinction Discipline

Terminology throughout the Suite should preserve these established distinctions:

- Authority ≠ Eligibility
- Eligibility ≠ Evaluation Outcome
- Evaluation Outcome ≠ Trust Statement
- Validation ≠ Evaluation
- Validation ≠ Eligibility
- Validation ≠ Conformance
- Valid ≠ Published
- Valid ≠ True
- Valid ≠ Supported
- Conformant ≠ Published
- Canonical Creation ≠ Lifecycle Activation
- Lifecycle Activation ≠ Publication
- Correction ≠ Deletion
- Correction ≠ Version
- Correction ≠ Versioning Decision
- Supersession ≠ Mutation
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity
- Changed Conclusion = Changed Canonical Statement
- Review ≠ Approval
- Suite Review ≠ Suite Ownership
- Version ≠ Decision
- GDR Identity ≠ Document Version
- Interoperability Failure ≠ Source Invalidity
- Compatibility Review ≠ Governance Veto
- New Capability ≠ New Institution
- Shared Custody ≠ Shared Ownership
- Multiple Representations ≠ Multiple Authorities
- NOT-TESTED NEVER EQUALS PASS

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Relationship to Suite Institutions

The Terminology Standard applies across the formal Suite while preserving each institution's distinct canonical responsibility.

### Atlas

Uses terminology appropriate to authoritative intelligence and structural context.

### Navigator

Uses terminology appropriate to workflow definition and orchestration.

### Certifier

Uses terminology appropriate to certification operations and the Certification Package.

### Registry

Uses terminology appropriate to Registry objects and their relationships to source records.

### Chronicle

Uses terminology appropriate to governed chronology.

### Anchor

Uses terminology appropriate to integrity references.

### Beacon

Uses terminology appropriate to discovery signals and discovery metadata.

### Attestor

Uses terminology appropriate to the canonical flow:

Eligible Governed Inputs  
→ Attestation  
→ Rule-Constrained Evaluation  
→ Trust Statement

Attestor terminology must not imply universal truth, source-authority transfer, or substitution for another Suite institution.

## Relationship to Suite Governance

The Terminology Standard records and preserves the vocabulary established by the ratified Satoshium Suite Governance Model.

It does not independently create governance authority.

```text
Terminology
→ defines governed meaning

Governance
→ establishes governed authority / decisions
```

A terminology edit may clarify language.

It may not silently create:

- a new institution;
- new canonical ownership;
- new approval authority;
- a new constitutional dependency; or
- a new Governance Decision.

## Historical Discipline

Historical terminology should remain accurate to the period in which it was used where the historical record itself is being preserved.

Current documentation should use current terminology.

A later terminology standard should not retroactively rewrite historical facts merely to make older records appear uniform.

## Repository Expectations

Changes to this directory should preserve:

1. canonical terminology;
2. consistent naming conventions;
3. controlled vocabulary discipline;
4. exact relationship semantics;
5. institutional authority boundaries;
6. historical terminology accuracy; and
7. consistency with the governing Suite standards and architecture;
8. current Governance Review vocabulary;
9. separation of Suite Governance from Institutional Governance;
10. explicit change-classification terminology;
11. GDR and Governance Decision Register terminology; and
12. constitutional terminology for ownership, membership, and architecture reconciliation.

Changes that would redefine institutional meaning, canonical object identity, relationship semantics, or authority allocation require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Consistent language supports consistent governance and understanding, but terminology must preserve the architecture and authority model rather than redefine them.**
