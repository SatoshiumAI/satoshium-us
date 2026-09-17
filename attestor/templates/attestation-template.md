# Attestation Template — Foundational Candidate

## Purpose
This candidate template shows the information a future Attestor Attestation may need to capture while preserving attribution, scope, provenance, evidence/source relationships, limitations, and traceability.

An Attestation is a governed, attributable assertion. It is not the final Trust Statement.

## Candidate Template
```yaml
attestation_identifier:
attestation_type:
status:

attesting_authority:
  identifier:
  type:

subject:
  identifier:
  type:

assertion:
scope:

evidence_references:
  -

source_references:
  -

governed_references:
  -

provenance:

created_at:
updated_at:

limitations:
notes:
```

## Architectural Notes
The exact field names, identifiers, required/optional status, controlled Attestation Types, authority types, timestamp requirements, and lifecycle states are not yet adopted.

The June template used `ATT-*`, fixed status values, a confidence indicator, and identity/qualification/ownership/participation/verification/reputation categories. Those remain historical candidates rather than current normative values.

## Foundational Relationship
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Governing Principle
> **Reference does not transfer authority.**

## Status
Foundational candidate template. Final operational format remains Advanced Architecture.
