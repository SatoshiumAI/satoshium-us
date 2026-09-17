# Attestation Template — Advanced Architecture

## Purpose
Authoring template for a canonical Satoshium Attestor **Attestation**: a governed, attributable assertion.

Canonical identifier family: `ATT-YYYY-NNNN`

## Template
```yaml
attestation_identifier: ATT-YYYY-NNNN
attestation_type:
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

evidence_references: []
source_references: []
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

## Controlled Attestation Types
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

## Lifecycle
`draft` · `active` · `superseded` · `withdrawn` · `retired`

Publication is separately represented as `unpublished` or `published`.

## Boundary
An Attestation is not a Trust Statement and does not itself establish an Evaluation Outcome.

**Reference does not transfer authority.**

## Status
Advanced authoring template. Exact machine-required fields/cardinality remain governed by the normative Attestation schema and Validation specification.
