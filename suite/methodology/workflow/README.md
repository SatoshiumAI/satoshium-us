# Certification Workflow

**Path:** `/suite/methodology/workflow/`  
**Surface:** Satoshium Suite · Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents the Satoshium Suite **Certification Workflow** methodology surface.

The Certification Workflow defines the repeatable operational sequence used to perform certification work consistently, transparently, and reviewably across the Suite.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Methodology Role

The Certification Workflow is part of the Satoshium Suite Methodology.

Its role is to define how certification work is performed within the broader stages described by the Certification Lifecycle.

The lifecycle describes when governed stages occur.

The workflow describes the operational work performed within those stages.

Workflow does not independently create institutional authority, certification outcomes, lifecycle activation, publication state, or trust statements.

## Workflow Stages

The current workflow surface identifies the following operational stages.

### Submission Processing

Receive the certification request, establish scope, assign applicable identifiers, and prepare the record for the next governed step.

Submission processing does not itself establish eligibility or certification status.

### Validation

Verify the required structural, identity, and procedural conditions needed before formal evaluation.

Validation must remain distinct from:

- eligibility;
- evaluation;
- conformance;
- certification outcome;
- publication; and
- trust conclusions.

A VALID result does not mean true, supported, conformant, published, or certified.

### Evidence Processing

Collect, organize, classify, reference, and prepare evidence for formal evaluation under the applicable evidence requirements.

Evidence processing must preserve provenance and source authority.

Reference does not transfer authority.

### Evaluation

Apply the applicable evaluation criteria, scoring methodology, and certification logic to governed evidence.

Evaluation remains distinct from validation and from any later Attestor Trust Statement.

### Decision

Determine the governed certification outcome under the applicable standards and methodology.

The decision should be documented sufficiently to support independent review and reproducibility.

### Record Generation

Create the structured certification records, metadata, identifiers, and supporting documentation required by the certification process.

Canonical creation must remain distinct from lifecycle activation and publication.

### Publication

Where governed publication is appropriate, certification information may be made available through the applicable publication, registration, integrity-reference, discovery, or repository surfaces.

Publication does not transfer Certifier authority to another Suite institution.

Publication is distinct from validity, conformance, canonical creation, and lifecycle activation.

### Ongoing Maintenance

Monitor governed certification records for events such as renewal, correction, suspension, revocation, expiration, retirement, or archival treatment.

Maintenance must preserve historical accuracy and must not silently mutate canonical records.

## Relationship to the Certification Lifecycle

The Certification Workflow and Certification Lifecycle are complementary but distinct.

The Lifecycle defines the temporal progression of certification activity.

The Workflow defines the operational sequence of actions performed within that progression.

Neither should collapse distinct concepts such as validation, evaluation, certification determination, lifecycle state, or publication.

## Relationship to Certifier

Satoshium Certifier is the Suite institution responsible for certification operations and the Certification Package.

The Certification Workflow supports Certifier by defining the repeatable operational process through which certification work is performed.

The workflow does not independently issue certification objects or become the source authority for certification merely because it describes the process.

## Relationship to Navigator

Navigator owns workflow definition and orchestration within the formal Suite architecture.

Certification Workflow methodology may therefore be implemented or orchestrated through Navigator according to the governed Suite design.

That operational relationship does not transfer Certifier's certification authority to Navigator.

Navigator coordinates work.

Certifier remains responsible for certification operations and certification outputs.

## Relationship to Other Suite Institutions

Other Suite institutions may participate in or receive outputs from the certification workflow according to their own canonical responsibilities.

For example:

- Registry may create or maintain governed Registry records associated with certification objects.
- Chronicle may record governed chronology.
- Anchor may establish integrity references.
- Beacon may provide discovery signals or discovery metadata.
- Attestor may consume eligible governed certification-related inputs within its own canonical flow.
- Atlas may provide authoritative intelligence or structural context.

Participation, reference, registration, anchoring, discovery, or attestation does not transfer certification authority.

## Workflow Boundaries

The workflow must preserve these established distinctions:

- authority is not eligibility;
- eligibility is not an evaluation outcome;
- validation is not evaluation;
- validation is not eligibility;
- validation is not conformance;
- valid does not mean true;
- valid does not mean supported;
- valid does not mean published;
- evaluation outcome is not a Trust Statement;
- canonical creation is not lifecycle activation;
- lifecycle activation is not publication;
- correction is not deletion;
- correction is not automatically a new version;
- supersession is not mutation;
- reference does not equal derivation;
- reference does not equal support; and
- reference does not transfer authority.

## Historical Discipline

Workflow execution should preserve the history of governed certification activity.

Corrections, renewals, suspensions, revocations, expirations, retirement, and archival treatment should follow the applicable governed process rather than rewriting earlier historical states.

Historical records should remain historically accurate.

## Repository Expectations

Changes to this directory should preserve:

1. the distinction between workflow and lifecycle;
2. the distinction between validation, eligibility, conformance, and evaluation;
3. Certifier authority over certification operations;
4. Navigator's orchestration role without authority transfer;
5. evidence provenance and source authority;
6. separation between canonical creation, lifecycle activation, and publication;
7. historical accuracy; and
8. consistency with the governing Suite standards, methodology, and institutional architecture.

Changes that would redefine certification authority, validation semantics, trust relationships, publication semantics, or cross-institution workflow responsibilities require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**A lifecycle defines when certification stages occur. A workflow defines how governed work is performed within those stages.**
