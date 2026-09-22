# Satoshium Atlas — Certification Subjects

**Path:** `/atlas/certification/atlas-certification-subjects/`  
**Institution:** Satoshium Atlas  
**Surface:** Atlas Certification Subjects  
**Status:** Current repository documentation

## Purpose

This directory documents the **Atlas Certification Subjects** surface.

Its role is to identify which canonical Satoshium Atlas objects may become certification subjects under the Satoshium Suite certification architecture and to distinguish those subjects from supporting artifacts.

The public page for this directory is:

- `index.html`

This README documents the repository role, subject model, supporting-artifact boundary, and institutional relationships of this surface. It does not replace the public presentation in `index.html`.

## Subject Role

Atlas Certification Subjects operate beneath the Atlas Certification Framework, Profile, and Scope.

Conceptually:

```text
Atlas Certification Framework
        ↓
Atlas Certification Profile
        ↓
Atlas Certification Scope
        ↓
Atlas Certification Subjects
        ↓
Certification Candidate
```

The Framework defines how Atlas participates in certification.

The Profile identifies what characteristics are evaluated.

The Scope defines the certification boundary.

The Subjects surface identifies the actual Atlas objects eligible to become certification subjects.

## Subject Principle

Certification applies to a defined Atlas subject.

Supporting artifacts may provide:

- evidence;
- context;
- metadata;
- traceability;
- signal support;
- trust-related context; and
- change history.

Those supporting materials are not normally independent certification subjects.

The governing distinction is:

> **The certification subject is the record being evaluated. Supporting artifacts explain and substantiate that record.**

## Primary Certification Subjects

The current page identifies complete Atlas record objects as the primary certification subjects.

### Jurisdiction Intelligence Engine Records

Jurisdiction Intelligence Engine records are identified as primary Atlas certification subjects where they represent complete jurisdiction intelligence packages with the required supporting record context.

### Country Records

Country records may serve as certification subjects when they are complete, canonical Atlas jurisdiction records for a country-level jurisdiction.

### State Records

State records may serve as certification subjects when they are complete, canonical Atlas jurisdiction records for a U.S. state or comparable subnational jurisdiction.

### Future Atlas Record Families

Future Atlas record families may become certification subjects only when Atlas formally defines them as complete canonical record families and establishes the applicable certification treatment.

Potential future examples on the current public page include corridor, regional, institutional, and dataset records.

Their appearance as future possibilities does not itself establish them as current canonical subject families.

## Supporting Certification Artifacts

Supporting artifacts may be reviewed during certification without becoming the subject itself.

### Evidence

Evidence supports the subject by documenting source material, substantiating claims, and preserving the basis for review.

### Metadata

Metadata supports identification, classification, versioning, update state, repository structure, and machine-readable context.

### Signals

Signals support evaluation by identifying evidence-derived indicators used within the Atlas record.

### Trust Dimensions

The current Atlas architecture uses **Trust Dimensions** as supporting Atlas record context.

This terminology should remain bounded to Atlas.

Trust Dimensions are not Attestor Trust Statements and should not be treated as equivalent to Attestor rule-constrained evaluation.

### Change Logs

Change logs preserve update history, revision context, and certification-relevant changes.

### Builder Mode and Profile Files

Builder Mode, profile files, and related materials support record construction, organization, and review context.

They do not automatically become independent certification subjects.

## Certification Subject Matrix

The current subject model distinguishes:

```text
Complete Atlas Record
→ Primary Certification Subject

Supporting Artifact
→ Evaluated / Referenced Context

Other Suite Institutional Record
→ Outside Atlas Subject Ownership
```

This separation prevents the certification of isolated fragments when the governed subject is the complete Atlas record.

## Subject Flow

Conceptually:

```text
Atlas Certification Subject
        ↓
Supporting Artifacts
        ↓
Profile Evaluation
        ↓
Scope Boundary
        ↓
Certification Decision
        ↓
Certification Package
```

The Certification Package remains a Certifier-owned output.

Atlas remains authoritative for the underlying Atlas certification subject.

## Relationship to Certifier

Certifier performs certification.

Certifier evaluates the Atlas subject under the applicable Standards, Methodology, Atlas Certification Framework, Profile, and Scope.

The Subjects surface does not itself issue a certification decision.

## Relationship to Registry

Registry records remain outside the Atlas certification-subject boundary.

A Registry Entry / SREG may later reference a certified Atlas result.

That reference does not make Registry the authority for the underlying Atlas subject.

## Relationship to Chronicle

Chronicle records remain outside the Atlas certification-subject boundary.

Chronicle may preserve governed chronology related to certification activity, but it does not become the certification subject.

## Relationship to Anchor

Anchor Integrity References remain outside the Atlas certification-subject boundary.

Anchor may preserve integrity context for a defined representation without becoming authoritative for Atlas meaning or certification.

## Relationship to Beacon

Beacon Discovery Signals / Discovery Metadata remain outside the Atlas certification-subject boundary.

Discovery does not convert a Beacon object into an Atlas certification subject.

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

Attestor records remain outside the Atlas certification-subject boundary.

A certified Atlas subject or related certification artifact may become an eligible governed Attestor input where applicable, but that downstream use does not change the identity of the original Atlas subject.

## Relationship to Navigator

Navigator workflow definitions and orchestration remain outside the Atlas certification-subject boundary.

Workflow participation does not make a Navigator object part of the Atlas certification subject.

## Authority and Relationship Discipline

This surface should preserve these distinctions:

- Certification Subject ≠ Supporting Artifact
- Atlas Record ≠ Certification Package
- Atlas Trust Dimension ≠ Attestor Trust Statement
- Certification Package ≠ Registry Entry
- Certification Package ≠ Integrity Reference
- Certification Package ≠ Discovery Signal
- Certification Package ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Subject Versioning

Certification subject families may evolve over time.

New subject families should be formally defined before they become eligible for certification.

Certification records should preserve the subject type and applicable version context used at the time of evaluation.

A later Atlas subject-family model should not silently redefine an earlier certification subject.

## Repository Expectations

Changes to this directory should preserve:

1. the distinction between certification subjects and supporting artifacts;
2. Atlas authority over Atlas records;
3. Certifier authority over certification;
4. explicit subject-family definitions;
5. historical subject/version context;
6. separation between Atlas trust terminology and Attestor Trust Statements;
7. downstream institutional independence; and
8. consistency with the Atlas Certification Framework, Profile, and Scope.

Changes that would create new canonical Atlas subject families, redefine trust semantics, or alter downstream institutional authority require governed Suite or Atlas architectural review rather than a documentation-only edit.

## Governing Principle

**Certify the governed Atlas record, not the supporting fragments that explain it.**
