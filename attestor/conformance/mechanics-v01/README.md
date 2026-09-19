# Satoshium Attestor — Step 13: Conformance Mechanics

This directory establishes the initial governed mechanics that convert Validation Results and required Review/context evidence into a bounded Conformance Determination.

## Files

- `attestor-conformance-mechanics.md` — durable normative mechanics.
- `conformance-mechanics-v0.1.json` — machine-readable vocabulary and mapping contract.
- `representative-attestation-conformance-request.json` — representative object-conformance request.
- `representative-trust-statement-conformance-request.json` — representative object-conformance request.

## Key boundary

`Validation Result ≠ Conformance Determination`

The Step 12 representative objects are machine-valid, but the initial object-conformance profile also requires governed Review evidence for applicable Review-bound requirements. Without those records, a complete conformance determination must remain `undetermined`.

## Next implementation task

Build the executable conformance evaluator and governed Review-record contract, then run these representative requests through it.
