# Satoshium Atlas — Certification Profile

**Path:** `/atlas/certification/certification-profile/`  
**Institution:** Satoshium Atlas  
**Surface:** Atlas Certification Profile  
**Status:** Current repository documentation

## Purpose

This directory documents the **Atlas Certification Profile**.

The Profile defines the characteristics of Satoshium Atlas records that are examined during certification under the Satoshium Suite.

The public page for this directory is:

- `index.html`

This README documents the repository role, evaluation domains, boundaries, and institutional relationships of the Profile. It does not replace the public presentation in `index.html`.

## Profile Role

The Atlas Certification Profile operates beneath the Atlas Certification Framework.

The relationship is:

```text
Atlas Certification Framework
        ↓
Atlas Certification Profile
        ↓
Evaluated Atlas Record Characteristics
```

The Framework defines how Atlas participates in certification.

The Profile defines what characteristics of an Atlas record are reviewed.

The Profile does not replace Suite Standards, Suite Methodology, or Certifier authority.

## Profile Boundary

The Profile is not:

- a scoring rubric;
- an evidence rulebook;
- a Registry model;
- a certification decision;
- a Suite-wide standard; or
- a replacement for Suite Methodology.

Its role is limited to identifying the Atlas record attributes that certification review should examine.

The governing distinction is:

> **The Profile defines what is reviewed. The Methodology governs how review is performed.**

## Evaluation Domains

The current Profile identifies the following evaluation domains.

### Identity

Confirms canonical identity information such as:

- record name;
- jurisdiction;
- record type;
- repository path;
- public location;
- version reference; and
- relationship to the applicable Atlas record family.

### Structure

Evaluates whether required Atlas artifacts are present, organized consistently, and aligned with the expected record architecture.

### Metadata

Reviews identifiers, dates, record state, source references, classification fields, update history, and machine-readable descriptors.

### Evidence

Examines whether claims within the Atlas record are supported by documented evidence, source references, and preserved evaluation material.

### Traceability

Determines whether record conclusions can be traced to source material, evidence files, signal definitions, trust-related dimensions, and change history.

### Trust Dimensions

The current Profile uses **Trust Dimensions** to evaluate characteristics such as readiness, transparency, stability, and reliability within Atlas records.

This terminology should remain bounded to the Atlas record and certification context.

It should not be treated as equivalent to an Attestor Trust Statement or Attestor rule-constrained evaluation.

### Signals

Evaluates whether Atlas signals are documented, internally consistent, evidence-derived, and aligned with the relevant jurisdiction or record context.

### Currency

Reviews whether the record has an identifiable update state, preserved change history, and certification-relevant freshness context.

### Completeness

Assesses whether required Atlas files, references, explanations, and evaluation materials are present for meaningful certification review.

### Reproducibility

Determines whether another reviewer or authorized Suite process could reconstruct the certification evaluation from preserved Atlas materials and applicable certification outputs.

## Profile Evaluation Model

Conceptually:

```text
Atlas Record
        ↓
Profile Domains
        ↓
Evidence Review
        ↓
Methodology Application
        ↓
Certification Decision
        ↓
Certification Package
```

The Profile is the evaluation lens between the Atlas record and the certification process.

It does not itself issue the certification decision.

## Relationship to Suite Standards and Methodology

The Profile operates within the established Suite architecture:

- **Suite Standards define expectations.**
- **Suite Methodology defines implementation.**
- **The Atlas Certification Framework applies those layers to Atlas.**
- **The Atlas Certification Profile identifies Atlas-specific evaluation characteristics.**
- **Certifier performs certification.**

The Profile must not become a separate standards or methodology authority.

## Relationship to Atlas

Atlas remains authoritative for:

- Atlas intelligence records;
- Atlas-owned metadata;
- Atlas signals;
- Atlas record families;
- Atlas source relationships; and
- Atlas change history.

Certification review does not transfer ownership of those records to the Profile or Certifier.

## Relationship to Certifier

Certifier owns the certification process and the Certification Package.

The Profile provides the Atlas-specific evaluation lens used within that process.

The Profile does not issue, activate, publish, suspend, revoke, or otherwise govern certification status.

## Relationship to Registry

Registry may create a Registry Entry / SREG referencing a certified Atlas result.

Registry does not become authoritative for the underlying Atlas record.

Reference does not transfer authority.

## Relationship to Chronicle

Chronicle may preserve governed chronology associated with certification-related events.

Chronicle remains distinct from Atlas record authority.

## Relationship to Anchor

Anchor may preserve an Integrity Reference for a defined representation associated with an Atlas or certification artifact.

Anchor preserves integrity context, not Atlas meaning or certification authority.

## Relationship to Beacon

Beacon provides Discovery Signals / Discovery Metadata.

Discovery should remain distinct from certification, validity, support, or trust.

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

Atlas Trust Dimensions or trust-related signals are not Attestor Trust Statements.

A certification outcome may become an eligible governed Attestor input where applicable, but that later use does not alter the meaning of the Atlas Certification Profile.

## Relationship to Navigator

Navigator defines and orchestrates workflows.

Navigator may participate in certification-related workflows without inheriting Atlas or Certifier authority.

## Authority and Relationship Discipline

The Profile must preserve the following distinctions:

- Profile Domain ≠ Certification Outcome
- Evidence ≠ Certification Decision
- Atlas Trust Dimension ≠ Attestor Trust Statement
- Signal ≠ Trust Statement
- Validation ≠ Evaluation
- Eligibility ≠ Evaluation Outcome
- Evaluation Outcome ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Profile Versioning

The Atlas Certification Profile may evolve as Atlas record families mature.

Certifications should preserve the Profile version used during evaluation where governed.

Historical Profile versions should remain interpretable so later reviewers can understand the evaluation lens applied at the time.

A later Profile version should not silently rewrite the meaning of an earlier certification.

## Repository Expectations

Changes to this directory should preserve:

1. the Profile as an Atlas-specific evaluation lens;
2. separation from Suite Standards and Suite Methodology;
3. Certifier authority over certification;
4. Atlas authority over Atlas records;
5. clear evaluation-domain definitions;
6. separation between Atlas trust terminology and Attestor Trust Statements;
7. versioning and historical interpretability; and
8. downstream institutional boundaries.

Changes that would redefine trust semantics, certification authority, downstream institutional responsibilities, or the relationship between Profile domains and Suite Methodology require governed Suite Reconciliation rather than a documentation-only edit.

## Governing Principle

**The Atlas Certification Profile defines what characteristics are reviewed without becoming the authority that governs how certification is performed or decided.**
