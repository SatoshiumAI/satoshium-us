# Trust Signal Schema — Legacy Candidate (Not Canonical)

## Architectural Notice
This June-era schema is retained because it is part of Attestor's early design work.

**Trust Signal is not currently adopted as a canonical Attestor object.**

Attestor's canonical institutional output is:

**Attestor → Trust Statement**

Beacon separately owns:

**Beacon → Discovery Signal / Discovery Metadata**

The terms must not be conflated.

## Historical Purpose
The early design proposed a structured object for observations, events, indicators, relationships, or information thought capable of influencing trust evaluation.

Candidate fields included:
- signal type;
- subject;
- source;
- description;
- direction;
- strength;
- Evidence references;
- source references;
- related records;
- timestamps;
- confidence;
- notes.

## Reconciled Interpretation
The useful idea beneath the old schema is **trust-relevant evaluation context**.

Such context may eventually inform Attestor evaluation, but the foundation does not currently require a separately persisted `Trust Signal` object.

Conceptually:

`Governed Inputs → Trust-Relevant Context → Rule-Constrained Evaluation → Trust Statement`

## Not Adopted
The following June concepts are not adopted:
- `TS-*` identifier family;
- Trust Signal as a canonical object;
- positive/negative/neutral/mixed direction;
- low/medium/high signal strength;
- confidence scale;
- Reputation as accumulation of Trust Signals;
- automatic conversion of Attestations, Evidence, or verification outcomes into Trust Signals.

## Potential Advanced-Architecture Value
The whole-foundation review may determine whether some old fields belong instead in:
- evaluation context;
- Evidence relationships;
- source relationships;
- uncertainty/limitations;
- evaluation result metadata;
- Trust Statement support metadata.

That decision should be made before any machine schema is created.

## Governing Principle
> **Reference does not transfer authority.**

## Status
**Legacy candidate retained for architectural review; not a canonical schema.**
