# Satoshium Certification Standard

**Path:** `/suite/standards/certification/`  
**Surface:** Satoshium Suite · Standards · Certification  
**Status:** Current repository documentation

## Purpose

This directory documents the **Satoshium Certification Standard**, the Suite-wide standards layer governing certification expectations.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Standard Role

The Satoshium Certification Standard defines the governed expectations that certification methodology and Certifier operations implement.

Within the Suite architecture:

- **Standards define expectations.**
- **Methodology defines implementation.**
- **Certifier performs certification.**

The Certification Standard therefore does not replace Certifier and does not itself execute certification operations.

## Relationship to Certifier

Satoshium Certifier is the formal Suite institution responsible for certification operations and the Certification Package.

Certifier implements the governing certification standards and methodology.

The Standard defines the rule layer under which Certifier operates; Certifier remains responsible for the operational certification outputs it creates.

The Standard does not independently issue certifications.

## Related Methodology Surfaces

The current Certification Standard surface links to the following methodology areas:

### Certification Lifecycle

Defines the temporal progression of certification activity.

Path:

- `/suite/methodology/lifecycle/`

Lifecycle must preserve the distinctions between canonical creation, activation, publication, correction, supersession, retirement, and archival preservation.

### Certification Workflow

Defines how certification work is operationally performed within lifecycle stages.

Path:

- `/suite/methodology/workflow/`

Workflow remains distinct from lifecycle and does not transfer Certifier authority to orchestration systems.

### Evaluation Criteria

Defines the objective criteria applied during certification evaluation.

Path:

- `/suite/methodology/evaluation-criteria/`

Evaluation criteria support evaluation but do not independently determine certification status.

### Evidence Requirements

Defines the evidentiary foundation required for certification activity.

Path:

- `/suite/methodology/evidence-requirements/`

Evidence must preserve provenance and source authority.

### Certification Logic

Defines governed decision logic used within the certification methodology.

Path:

- `/suite/methodology/certification-logic/`

Certification logic supports repeatable decision-making but does not independently create institutional authority.

### Certification Schema

Defines structured representation requirements for certification records.

Path:

- `/suite/methodology/certification-schema/`

Schema validation is distinct from substantive certification evaluation, lifecycle state, and publication.

## Related Standards

The current public surface also identifies supporting standards areas for:

- scoring;
- trust-related rules; and
- governance.

Those standards must remain consistent with the mature Suite architecture and with the authority boundaries of Certifier and Attestor.

Where trust terminology overlaps with Attestor's governed Trust Statement semantics, the meaning should be reconciled through the appropriate Suite-level architectural review rather than inferred from terminology alone.

## Institutional Boundaries

The Certification Standard may be referenced or consumed by multiple Suite institutions, but each institution retains its own canonical responsibility.

### Certifier

Implements certification standards and methodology operationally and produces certification outputs.

### Registry

Creates and maintains canonical Registry objects, including Satoshium Registry Entries, that may reference certification source records.

Registry does not become the certification authority merely by recording or referencing a certification object.

### Chronicle

Records governed chronology.

Chronicle does not own certification authority.

### Anchor

Establishes integrity references.

Integrity reference does not equal certification authority, certification determination, or evidence ownership.

### Beacon

Provides discovery signals and discovery metadata.

Discovery does not equal derivation, publication authority, or certification authority.

### Attestor

Consumes eligible governed inputs within its own canonical flow:

Eligible Governed Inputs  
→ Attestation  
→ Rule-Constrained Evaluation  
→ Trust Statement

Attestor does not replace Certifier and does not become authoritative source for referenced certification objects.

### Navigator

Owns workflow definition and orchestration.

Navigator may coordinate or query governed workflow information where the architecture permits, but orchestration does not transfer certification authority.

### Atlas

Provides authoritative intelligence according to its own institutional role.

Reference to standards or certification objects does not transfer Certifier authority.

## Authority and Relationship Discipline

This directory must preserve the Suite's established distinctions:

- authority is not eligibility;
- eligibility is not evaluation outcome;
- validation is not evaluation;
- validation is not eligibility;
- validation is not conformance;
- valid does not mean published;
- valid does not mean true;
- valid does not mean supported;
- evaluation outcome is not a Trust Statement;
- canonical creation is not lifecycle activation;
- lifecycle activation is not publication;
- correction is not deletion;
- supersession is not mutation;
- reference does not equal derivation;
- reference does not equal support; and
- reference does not transfer authority.

## Historical Discipline

Changes to standards should preserve historical accuracy.

Earlier records created under earlier versions of a standard should not be rewritten merely because the standard later changes.

Versioning, deprecation, supersession, correction, and preservation should follow the applicable governed process.

## Repository Expectations

Changes to this directory should preserve:

1. the distinction between standards, methodology, and Certifier operations;
2. Certifier's responsibility for certification outputs;
3. institutional authority boundaries;
4. provenance and relationship semantics;
5. the distinction between certification and Attestor trust conclusions;
6. historical accuracy and version discipline; and
7. consistency with the governing Suite architecture.

Changes that would redefine institutional roles, trust semantics, canonical objects, publication authority, or cross-institution responsibilities require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Standards define expectations. Methodology defines implementation. Certifier performs certification.**

