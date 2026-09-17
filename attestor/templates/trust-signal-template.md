# Trust Signal Template — Legacy Candidate (Not Canonical)

## Architectural Notice
This June-era template is retained as part of Attestor's design history.

**Trust Signal is not currently adopted as a canonical Attestor object.**

**Attestor → Trust Statement**

Beacon separately owns:

**Beacon → Discovery Signal / Discovery Metadata**

## Historical Candidate Structure
The June template proposed fields for:
- Trust Signal identifier;
- signal type;
- subject;
- signal source;
- direction;
- strength;
- Evidence/source references;
- status;
- confidence;
- notes.

It also proposed reputation as an accumulation of Trust Signals.

Those structures are **not adopted**.

## Reconciled Interpretation
The useful concept is **trust-relevant evaluation context**:

`Governed Inputs → Trust-Relevant Context → Rule-Constrained Evaluation → Trust Statement`

Advanced architecture may determine whether any legacy fields are useful for evaluation context, Evidence/source relationships, uncertainty, limitations, or Trust Statement support metadata.

## Not Adopted
No `TS-*` identifier family, direction scale, strength scale, confidence scale, Reputation accumulation model, or automatic Trust Signal generation is established.

## Status
Legacy candidate retained for architectural review; not an operational template.
