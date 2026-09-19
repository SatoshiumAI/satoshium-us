# Satoshium Attestor — Executable Validator v0.1

This implementation package is the first executable realization of the Attestor Machine Contract.

## Files
- `attestation.schema.json` — JSON Schema 2020-12 representation of `attestor.attestation.base`.
- `trust-statement.schema.json` — JSON Schema 2020-12 representation of `attestor.trust-statement.base`.
- `attestor_validator.py` — first executable validator producing the governed Validation Report structure.
- `valid-attestation.yaml` — non-production positive ATT fixture.
- `valid-trust-statement.yaml` — non-production positive TRST fixture.
- `invalid-attestation.yaml` — deliberate negative ATT fixture.
- `attestation-validation-report.json` — first successful ATT validation report.
- `trust-statement-validation-report.json` — first successful TRST validation report.
- `invalid-attestation-validation-report.json` — negative validation report demonstrating failure detection.

## Architectural Boundary
These artifacts implement established architecture; they do not create or modify it.

The fixtures are not canonical production objects and do not constitute production proof.

## Runtime
Python 3.11+ recommended. YAML input requires PyYAML.

Example:

`python attestor_validator.py valid-attestation.yaml --output attestation-validation-report.json`

`python attestor_validator.py valid-trust-statement.yaml --output trust-statement-validation-report.json`

The validator currently executes the deterministic base-profile rules implemented in v0.1. Review-dependent institutional rules remain outside automatic pass/fail adjudication.

## Status
**Executable schema artifacts → created**

**Validator implementation v0.1 → created**

**Positive fixtures → executed successfully**

**Negative fixture → executed successfully**

The initial ATT fixture returned `valid`.  
The initial TRST fixture returned `valid`.  
The deliberate invalid ATT fixture returned `invalid` with two detected failures.

These are implementation fixtures only, not production proof.

Next: reconcile validator coverage against the complete `VAL-*` catalog, add broader negative/boundary fixtures, and close implementation gaps before representative or production validation.
