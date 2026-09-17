# Governed Correction / Change Template — Advanced Architecture

## Purpose
Operational worksheet for documenting governed change to an Attestor-owned Attestation or Trust Statement.

**Correction is not established as a separate canonical Attestor object class.**

Correction explains why a governed change occurs. Versioning determines how canonical identity behaves across that change.

`Correction ≠ Version`

## Template
```yaml
target_object:
  canonical_identifier:
  object_type:
  current_version_identity:
  current_lifecycle_state:

change:
  reason:
  summary:
  requested_or_identified_at:
  responsible_attestor_context:

materiality_review:
  essential_meaning_changed:
  scope_materially_changed:
  assertion_or_conclusion_materially_changed:
  evaluation_basis_materially_changed:
  determination:

prior_state_reference:
proposed_state_reference:

provenance:
relationships: []

result:
  action:
  resulting_canonical_identifier:
  resulting_version_identity:
  resulting_lifecycle_state:
  supersedes_reference:
  corrects_reference:

limitations: []
notes:
```

## Governing Decision
Bounded/non-substantive correction may preserve canonical identity through a governed version.

Material change to essential institutional meaning requires a new canonical object.

For a Trust Statement, a materially different conclusion requires a new `TRST-YYYY-NNNN`.

For an Attestation, a materially different assertion requires a new `ATT-YYYY-NNNN`.

## Historical Integrity
`Prior State → Governed Change → Current State`

No silent overwrite.

## Authority Boundary
Attestor corrects Attestor-owned objects only. Another Suite institution governs correction of its own canonical objects.

**Reference does not transfer authority.**

## Status
Advanced governed-change worksheet; not an independent canonical object schema.
