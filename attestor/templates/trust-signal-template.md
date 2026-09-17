# Trust Signal Template — Legacy Historical Artifact

## Architectural Notice
This file is retained only as part of Attestor's design history.

**Trust Signal is not a canonical Attestor object and this is not an operational template.**

Canonical responsibility:

`Attestor → Trust Statement`

Beacon separately owns:

`Beacon → Discovery Signal / Discovery Metadata`

## Historical Interpretation
The useful concept beneath the June-era Trust Signal proposal is **trust-relevant evaluation context**.

That context is now handled through governed inputs, Evidence/Source relationships, evaluation basis, provenance, limitations, uncertainty, and Trust Statement support metadata.

## Not Adopted
No:
- `TS-*` identifier family;
- Trust Signal object;
- direction scale;
- strength scale;
- confidence scale;
- Reputation accumulation model; or
- automatic Trust Signal generation.

## Governing Model
`Attestation + Eligible Governed Inputs → Rule-Constrained Evaluation → Trust Statement`

## Status
**Legacy / historical only. Do not use for production authoring.**
