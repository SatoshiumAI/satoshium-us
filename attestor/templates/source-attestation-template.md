# Source / Provenance Attestation Template — Advanced Profile

## Purpose
Specialized authoring profile for the adopted Attestation Type:

`source-provenance`

It expresses a bounded assertion concerning source identity, origin, provenance, state, or relationship to a subject.

## Template
```yaml
attestation_identifier: ATT-YYYY-NNNN
attestation_type: source-provenance
lifecycle_state: draft
publication_state: unpublished

attesting_authority:
  identifier:
  authority_context:

subject:
  identifier:
  type:

assertion:
scope:

source_reference:
source_authority_context:
source_state_at_evaluation:

evidence_references: []
governed_references: []

provenance:
  mode:
  source_or_origin:
  relevant_time_or_state:
  acquisition_or_reference_context:
  derivation_basis:
  material_limitations:

relationships: []

created_at:
updated_at:
version_identity:

limitations: []
uncertainty: []
notes:
```

## Provenance Modes
`direct` · `referenced` · `derived`

## Authority Context
`Attestor` · `Suite-source` · `external-source`

## Boundary
Source existence, publicity, accessibility, or authority does not automatically establish eligibility or evaluation outcome.

`Availability ≠ Eligibility`

**Reference does not transfer authority.**

## Status
Advanced specialized Attestation profile.
