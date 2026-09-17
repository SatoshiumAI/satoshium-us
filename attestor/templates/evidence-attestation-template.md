# Evidence Attestation Template — Advanced Profile

## Purpose
Specialized authoring profile for the adopted Attestation Type:

`evidence`

It expresses a bounded assertion concerning Evidence or its relationship to a subject, assertion, or evaluation context.

## Template
```yaml
attestation_identifier: ATT-YYYY-NNNN
attestation_type: evidence
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

evidence_reference:
source_references: []
governed_references: []

provenance:
  mode:
  source_or_origin:
  relevant_time_or_state:
  acquisition_or_reference_context:
  material_limitations:

relationships: []

created_at:
updated_at:
version_identity:

limitations: []
uncertainty: []
notes:
```

## Relationship Rule
Use adopted Attestor relationship vocabulary where applicable:

`supports` · `references` · `derived-from` · `evaluates` · `results-in` · `supersedes` · `corrects` · `related-to`

The June-only values `partially_supports`, `contradicts`, `neutral`, and `unclear` are not promoted here as canonical relationship types.

## Boundary
Evidence informs evaluation. An Evidence Attestation does not automatically establish truth, sufficiency, certification, verification, or a favorable Trust Statement.

`supports` as a relationship is not the same as `supported` as an Evaluation Outcome.

**Reference does not transfer authority.**

## Status
Advanced specialized Attestation profile.
