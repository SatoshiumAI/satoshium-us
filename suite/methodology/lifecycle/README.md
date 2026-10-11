# Certification Lifecycle

**Path:** `/suite/methodology/lifecycle/`  
**Surface:** Satoshium Suite · Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents the Satoshium Suite **Certification Lifecycle** methodology surface.

The Certification Lifecycle defines the temporal progression of **Certifier / certification-domain activity** from initial submission through evaluation, decision, issuance, publication-related handling, monitoring, renewal, retirement, and archival preservation.

It is not the lifecycle model for every Satoshium Suite institution or canonical object.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Methodology Role

The Certification Lifecycle is part of the Satoshium Suite Methodology as a **certification-specific methodology surface**.

Its role is to describe the chronological framework through which certification activity progresses while preserving clear distinctions between:

- canonical creation;
- validation;
- eligibility;
- evaluation;
- certification determination;
- lifecycle activation;
- publication;
- correction;
- supersession;
- retirement; and
- archival preservation.

The lifecycle provides temporal structure for certification activity. It does not transfer authority between Suite institutions and does not import Certifier lifecycle semantics into another institution's canonical objects.

## Scope Boundary

The Certification Lifecycle governs certification-domain progression.

It does **not** govern the canonical lifecycle of:

- Satoshium Registry Entries (SREGs);
- Chronicle Entries;
- Integrity References;
- Discovery Signals;
- Navigator Workflow Definitions;
- Atlas Jurisdiction Intelligence Packages;
- Attestations; or
- Trust Statements.

Each institution retains lifecycle authority over its own canonical objects.

```text
Certification Lifecycle
→ Certifier / certification-domain methodology

Institutional Lifecycle
→ owned by the institution governing the canonical object
```

A downstream institution may reference, register, preserve, anchor, discover, evaluate, or otherwise interact with a certification object without inheriting the Certification Lifecycle.

```text
REFERENCE
≠ LIFECYCLE IMPORT

HANDOFF
≠ LIFECYCLE TRANSFER

INTEROPERABILITY
≠ LIFECYCLE OWNERSHIP
```

## Lifecycle Stages

The current lifecycle surface identifies the following stages.

### Submission

A certification target is identified, submitted, or selected for review.

Initial metadata, scope, and the intended certification standard may be recorded.

Submission does not itself establish eligibility or certification status.

### Validation

The submission is checked for required structural and procedural conditions before formal evaluation.

Validation must remain distinct from eligibility, evaluation, conformance, certification outcome, and publication.

A VALID result does not mean true, supported, published, or certified.

### Evidence Collection

Required evidence is gathered, organized, referenced, and prepared for review according to the applicable evidence requirements.

Evidence collection must preserve provenance and source authority.

Reference does not transfer authority.

### Evaluation

Governed evidence is evaluated under the applicable criteria, methodology, scoring rules, and certification standard.

Evaluation remains distinct from validation and from any later Attestor trust conclusion.

### Decision

A governed certification determination is reached under the applicable standards and methodology.

The certification determination must remain conceptually distinct from later lifecycle states such as suspension, revocation, expiration, renewal, retirement, or archival treatment unless the governing architecture explicitly defines otherwise.

### Issuance

Where the certification determination permits issuance, the certification object and associated structured records may be created with applicable identifiers, metadata, evidence references, and verification-ready fields.

Canonical creation is not the same as lifecycle activation or publication.

### Publication

Certification information may become available through governed publication and may later be referenced by independently governed registration, integrity-preservation, discovery, indexing, or public-verification mechanisms.

Publication is distinct from validity, conformance, certification determination, and canonical creation.

Publication through or reference by another Suite institution does not transfer Certifier authority.

### Monitoring

Active certifications may be monitored for relevant changes, expiration conditions, corrections, disputes, updated evidence, or review triggers.

Monitoring should preserve historical accuracy and should not silently mutate canonical records.

### Renewal

A certification may enter a governed renewal process when updated evidence, periodic review, or other applicable conditions require renewed consideration.

Renewal should preserve the distinction between the existing historical certification record and any newly governed certification statement or lifecycle action.

### Retirement and Archive

Certifications that are no longer active may be retired while remaining preserved as part of the institutional record.

Retirement and archival preservation do not erase historical facts.

Correction is not deletion.

Supersession is not mutation.

## Institutional Relationships

The Certification Lifecycle may be referenced by multiple Suite institutions, but it does not become their lifecycle model. Each institution retains its own canonical responsibility and lifecycle authority.

### Certifier

Certifier owns certification operations and the Certification Package.

The lifecycle describes the temporal progression of certification activity without replacing Certifier authority.

### Registry

Registry may record governed Registry objects associated with certification activity.

Registration does not create certification authority, and the Certification Lifecycle does not govern the SREG lifecycle.

### Chronicle

Chronicle records governed chronology and historical events.

Chronicle reference does not itself create or modify certification state, and the Certification Lifecycle does not govern Chronicle Entry lifecycle state.

### Anchor

Anchor establishes integrity references.

Integrity reference does not equal certification determination or lifecycle activation, and Anchor retains authority over Integrity Reference lifecycle.

### Beacon

Beacon provides discovery signals and discovery metadata.

Discovery does not equal publication authority or certification authority, and Beacon retains authority over Discovery Signal lifecycle.

### Attestor

Attestor may consume eligible governed certification-related inputs within its own canonical flow.

Attestor does not replace Certifier, and Attestor's Attestation / Trust Statement lifecycle remains independent from the Certification Lifecycle.

### Navigator and Atlas

Navigator may support governed workflow or orchestration, while Atlas may provide authoritative intelligence or structural context according to their established institutional roles.

Neither inherits certification authority or Certifier lifecycle authority through participation in a workflow or reference relationship.

## Lifecycle Boundaries

The lifecycle must preserve these distinctions:

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
- correction is not automatically a new version;
- supersession is not mutation; and
- reference does not transfer authority.

## Methodology Boundary

The Certification Lifecycle is not a universal Suite pipeline.

```text
Certification Lifecycle
≠ Registry Lifecycle

Certification Lifecycle
≠ Chronicle Lifecycle

Certification Lifecycle
≠ Anchor Lifecycle

Certification Lifecycle
≠ Beacon Lifecycle

Certification Lifecycle
≠ Attestor Lifecycle

Certification Lifecycle
≠ Navigator Workflow Lifecycle

Certification Lifecycle
≠ Atlas Intelligence Lifecycle
```

The broader Suite may exercise workflows in which certification activity is followed by registration, preservation, anchoring, discovery, or attestation.

That sequence is an exercised or conceptual relationship only.

> **Conceptual Sequence ≠ Mandatory Pipeline**

> **Exercised Lineage ≠ Mandatory Architecture**

## Historical Discipline

Lifecycle progression must remain historically traceable.

Earlier states should not be rewritten merely because a certification later changes status.

Where the architecture requires correction, supersession, renewal, retirement, or other lifecycle treatment, the historical record should remain preserved according to the applicable governed process.

## Repository Expectations

Changes to this directory should preserve:

1. clear temporal ordering of certification activity;
2. distinctions between validation, evaluation, determination, lifecycle state, and publication;
3. Certifier authority over certification operations;
4. provenance and authority boundaries across Suite institutions;
5. historical accuracy;
6. non-destructive correction and supersession semantics; and
7. consistency with the governing Suite standards, methodology, and institutional architecture;
8. explicit certification-domain scope;
9. preservation of institution-specific lifecycle authority; and
10. the distinction between certification progression and downstream institutional lifecycles.

Changes that would redefine lifecycle state semantics, trust relationships, or authority allocation require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**The Certification Lifecycle governs certification-domain progression only; downstream interaction does not import Certifier lifecycle authority into another institution.**
