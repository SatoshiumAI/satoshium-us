# Satoshium Atlas — Certification Scope

**Path:** `/atlas/certification/atlas-certification-scope/`  
**Institution:** Satoshium Atlas  
**Surface:** Atlas Certification Scope  
**Status:** Current repository documentation

## Purpose

This directory documents the **Atlas Certification Scope**.

The Scope defines the certification boundary for Satoshium Atlas by identifying which Atlas artifacts participate in certification under the Satoshium Suite and which institutional records remain outside the Atlas certification process.

The public page for this directory is:

- `index.html`

This README documents the repository role, certification boundary, included and excluded surfaces, and institutional relationships of the Scope. It does not replace the public presentation in `index.html`.

## Scope Role

The Atlas Certification Scope operates alongside the Atlas Certification Framework and Atlas Certification Profile.

Conceptually:

```text
Atlas Certification Framework
        ↓
Atlas Certification Profile
        ↓
Atlas Certification Scope
        ↓
Certification Boundary
```

The Framework defines how Atlas participates in certification.

The Profile defines which Atlas characteristics are evaluated.

The Scope defines which Atlas artifacts are included or excluded from the certification boundary.

## Boundary Principle

Atlas certification evaluates Atlas-owned records and formally defined Atlas certification subjects.

Operational records produced by other Suite institutions remain outside Atlas certification scope unless explicitly governed otherwise.

The governing principle is:

> **Institutional responsibility remains with the system that owns the record.**

Reference does not transfer authority.

## Included Within Scope

The current Scope identifies the following Atlas materials as included within the certification boundary:

- Jurisdiction Intelligence Engine outputs;
- Country and State records;
- Atlas evidence;
- Atlas metadata;
- Atlas signals;
- Atlas trust-related dimensions;
- change logs; and
- canonical Atlas artifacts.

Inclusion within scope means these materials may be examined as part of the Atlas certification subject or certification evaluation.

It does not mean that every included component becomes an independent certification subject.

## Outside Scope

The current Scope identifies the following as outside the Atlas certification boundary:

- Registry Entries / SREG;
- Chronicle records;
- Anchor Integrity References;
- Beacon Discovery Signals / Discovery Metadata;
- Attestor Trust Statements;
- Navigator workflows;
- certification scoring; and
- Suite governance documents.

These surfaces remain governed by their respective institutions or Suite layers.

## Certification Package Boundary

The Atlas certification process leads to a Certifier-owned Certification Package.

Conceptually:

```text
Atlas Record
        ↓
Within Scope
        ↓
Certification Evaluation
        ↓
Certification Package
        ↓
Possible downstream Suite references or operations
```

The Certification Package is not an Atlas-owned canonical object.

Atlas remains authoritative for the Atlas record being certified.

Certifier remains authoritative for the certification operation and resulting Certification Package.

## Relationship to Certifier

Certifier performs certification.

The Atlas Certification Scope identifies what Atlas material falls within the certification boundary.

The Scope does not issue certification decisions or control certification lifecycle state.

## Relationship to Registry

Registry may create a Registry Entry / SREG that references a certified Atlas result.

Registry remains authoritative for its own Registry object.

Registry does not become authoritative for the underlying Atlas record or Certification Package.

## Relationship to Chronicle

Chronicle may preserve governed chronology associated with certification-related events.

Chronicle remains distinct from Atlas record authority.

The exact canonical naming of Chronicle outputs should follow Chronicle's governing architecture.

## Relationship to Anchor

Anchor may preserve an Integrity Reference for a defined representation associated with an Atlas or certification artifact.

Anchor preserves integrity context and does not inherit Atlas or Certifier authority.

## Relationship to Beacon

Beacon provides Discovery Signals / Discovery Metadata.

Discovery remains outside the Atlas certification scope and does not itself establish certification, validity, support, or trust.

## Relationship to Attestor

Attestor operates under the canonical flow:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Attestor Trust Statements remain outside Atlas certification scope.

Atlas trust-related dimensions or signals are not Attestor Trust Statements.

## Relationship to Navigator

Navigator defines and orchestrates workflows.

Navigator workflow activity remains outside Atlas certification scope and does not become part of the Atlas certification subject merely through orchestration.

## Authority and Relationship Discipline

The Scope must preserve these distinctions:

- Atlas Record ≠ Certification Package
- Certification Package ≠ Registry Entry
- Certification Package ≠ Chronicle record
- Certification Package ≠ Integrity Reference
- Certification Package ≠ Discovery Signal
- Certification Package ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Scope Philosophy

Clear certification boundaries allow Atlas to participate in Suite certification while preserving institutional separation.

A useful conceptual summary is:

```text
Atlas → owns Atlas intelligence records
Certifier → performs certification
Registry → governs Registry records
Chronicle → governs chronology
Anchor → governs Integrity References
Beacon → governs discovery
Attestor → governs Attestations and Trust Statements
Navigator → governs workflow definition / orchestration
```

This summary describes institutional responsibilities rather than an automatic downstream sequence.

## Repository Expectations

Changes to this directory should preserve:

1. a clear Atlas certification boundary;
2. Atlas authority over Atlas records;
3. Certifier authority over certification;
4. explicit included and excluded surfaces;
5. downstream institutional independence;
6. separation between Atlas trust terminology and Attestor Trust Statements;
7. provenance and reference boundaries; and
8. consistency with Suite Standards, Suite Methodology, and the Atlas Certification Framework.

Changes that would redefine institutional scope, downstream authority, certification ownership, or trust semantics require governed Suite Reconciliation rather than a documentation-only edit.

## Governing Principle

**Atlas certification should define exactly what is being certified while leaving every other Suite institution authoritative for its own records and operations.**
