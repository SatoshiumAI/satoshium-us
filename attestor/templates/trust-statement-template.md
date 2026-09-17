# Trust Statement Template — Advanced Architecture

## Purpose
Authoring template for a canonical **Trust Statement**, Attestor's institutional output.

Canonical identifier family: `TRST-YYYY-NNNN`

A Trust Statement is a governed, attributable, bounded Attestor conclusion produced through Rule-Constrained Evaluation of an Attestation against eligible governed inputs.

## Template
```yaml
trust_statement_identifier: TRST-YYYY-NNNN
lifecycle_state: draft
publication_state: unpublished

subject:
  identifier:
  type:

bounded_conclusion:
scope:

attestor_attribution:
  identifier:
  authority_context: Attestor

supporting_attestations: []

evaluation:
  outcome:
  basis_references: []
  applicable_rules: []
  relevant_time_or_state:
  material_conflicts: []
  material_exclusions: []

provenance:
  mode: derived
  source_or_origin:
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

## Evaluation Outcomes
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

## Boundary
`Outcome ≠ Conclusion ≠ Trust Statement Identity`

A Trust Statement is not a universal truth declaration, reputation score, confidence percentage, certification, or inherited source authority.

**Reference does not transfer authority.**

## Status
Advanced authoring template. Exact machine-required fields/cardinality remain governed by the normative Trust Statement schema and Validation specification.
