# Satoshium Attestor — Executable Validator v0.2

## Step 7 Purpose
Validator v0.2 closes an initial set of rule-coverage gaps identified by the Step 6 reconciliation, normalizes executable checks toward canonical `VAL-*` identifiers, and exercises the full Validation Result state model.

## Important Boundary
Review-dependent rules are never silently machine-passed. They are emitted as `not-tested` when applicable to the base validation profile.

A report may therefore be structurally successful yet aggregate to `incomplete` when mandatory governed review or external context has not been supplied.

## Files
- `attestation.schema.json`
- `trust-statement.schema.json`
- `attestor_validator.py`
- `registry-context.yaml`
- positive, negative, incomplete, and error fixtures
- generated validation reports
- `step7-test-matrix.json`

## Aggregate Result Semantics
- `valid` — all applicable mandatory machine tests pass and no mandatory test remains unresolved in the executed profile/context.
- `invalid` — at least one applicable mandatory rule fails.
- `incomplete` — no mandatory failure establishes invalidity, but at least one applicable mandatory rule remains `not-tested`.
- `error` — validator/runtime/representation failure prevents a governed determination.

## Status
Step 7 establishes expanded executable coverage and explicit result-state behavior. It does not yet claim complete coverage of all machine-testable catalog rules or production readiness.
