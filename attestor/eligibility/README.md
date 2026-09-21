# Satoshium Attestor — Eligibility

**Path:** `/attestor/eligibility/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Eligibility  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Eligibility determines what may legitimately enter Attestor evaluation.

It formalizes **eligible** in:

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

Eligibility is a governed admission determination for a particular evaluation. It is not a permanent quality of a source.

## Governing Principle

`Availability ≠ Eligibility`

`Authority ≠ Eligibility`

`Reference ≠ Eligibility`

An input is eligible because it satisfies the requirements of the particular Attestor evaluation—not merely because it exists, is public, is authoritative, or can be technically retrieved.

## Eligibility Requirements

A proposed input is eligible when Attestor can responsibly admit it under the applicable evaluation context.

Conceptually, the input must be:

- identifiable or sufficiently distinguishable;
- materially relevant;
- supported by traceable provenance;
- accompanied by authority context where material;
- compatible with evaluation scope;
- interpretable in its relevant time/state where material;
- sufficiently intact, resolvable, or reviewable; and
- not prohibited by applicable Attestor rules.

Eligibility requirements are represented through governed production Eligibility records and remain subject to applicable Schema and Validation controls.

## Evaluation-Specific Eligibility

Eligibility belongs to the relationship between an input and a particular evaluation.

`Input + Evaluation Purpose + Scope + Provenance + Authority Context + State + Relationship + Rules → Eligibility Determination`

Therefore:

`Eligible Here ≠ Eligible Everywhere`

The same source may be eligible for one purpose, ineligible for another, or eligible only for a bounded historical/contextual purpose.

## Eligible Does Not Mean Favorable

Eligibility permits consideration.

It does not establish:

- support for the assertion;
- correctness;
- sufficiency;
- evidence weight;
- a favorable outcome; or
- trustworthiness.

Eligible inputs may support, weaken, contradict, complicate, or leave unresolved the assertion under review.

## Ineligible Inputs

An input should be excluded from the governed evaluation basis when, materially:

- provenance is inadequate;
- identity is too ambiguous;
- the input is irrelevant;
- scope is incompatible;
- relevant state cannot be responsibly interpreted;
- the material is unusable for the evaluation purpose; or
- applicable Attestor rules prohibit its use.

An input must **not** be excluded merely because it is unfavorable to the assertion.

## Reviewable Exclusion

Where Attestor considers an input for eligibility but excludes it, and that exclusion is material to understanding the evaluation, enough context should be preserved to make the eligibility decision reviewable.

Evaluation and Methodology govern how material eligibility treatment is carried forward into the evaluation basis and later review.

## Suite Sources

Canonical Suite objects are potential governed inputs, not automatically eligible inputs.

Examples include:

- Atlas Authoritative Intelligence;
- Navigator Workflow Definition / Orchestration context;
- Certifier Certification Packages;
- Satoshium Registry Records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals / Discovery Metadata.

Their source authority remains intact while Attestor separately determines eligibility.

**Reference does not transfer authority.**

## External Sources

External origin neither disqualifies nor privileges an input.

An external source may be eligible when it can be governed sufficiently for the evaluation purpose, including adequate attribution, provenance, authority context, scope, relevant state, and limitations.

Likewise, a Suite source is not automatically eligible merely because it belongs to the Suite.

## Eligibility and Attestations

An Attestation presents the governed assertion for evaluation.

Its referenced evidence, source objects, and other inputs must satisfy applicable eligibility requirements before becoming part of the evaluation basis.

`Attestation → Referenced Inputs → Eligibility Determination → Evaluation Basis`

The existence of an Attestation does not make all references eligible.

## First Production Eligibility Demonstration

The first controlled production operation exercised Eligibility as a distinct governed admission decision before Rule-Constrained Evaluation.

Six source objects were separately assessed and admitted as eligible governed inputs for the bounded evaluation concerning `SC-CERT-2026-0001`:

- `SC-CERT-2026-0001` → eligible
- Atlas El Salvador source → eligible
- `SREG-2026-0001` → eligible
- `CHR-2026-0001` → eligible
- `ANCH-2026-0001` → eligible
- `BEAC-2026-0001` → eligible

A separate Eligibility record was preserved for each determination.

No independent Eligibility identifier family was required; the production records intentionally preserved `record_identifier: null`.

The operation demonstrated:

- Eligibility before Rule-Constrained Evaluation;
- evaluation-specific admission rather than source-wide status;
- preservation of source identity, provenance, authority context, relevant state, and relationships;
- no automatic eligibility merely because an object belonged to the Suite;
- no transfer of source authority;
- no conversion of Eligibility into evidence weight; and
- no predetermination of the later Evaluation Outcome.

The later Evaluation Outcome of `supported` was reached through Rule-Constrained Evaluation, not through the Eligibility decisions themselves.

## What Eligibility Does Not Establish

`Eligibility ≠ Truth`

`Eligibility ≠ Authority Ranking`

`Eligibility ≠ Evidence Weight`

`Eligibility ≠ Validation`

`Eligibility ≠ Conformance`

`Eligibility ≠ Publication`

`Eligibility ≠ Trust Statement Outcome`

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Eligibility → Established and Production-Proven**

- evaluation-specific governed admission → established
- availability → insufficient by itself
- authority → insufficient by itself
- reference → insufficient by itself
- provenance → required where material, not sufficient by itself
- unfavorable evidence → not excludable merely because unfavorable
- material exclusions → reviewable where required
- governed Eligibility records → exercised in production
- six first-production source determinations → **eligible**
- Eligibility / Evaluation Outcome separation → demonstrated
- source authority preservation → demonstrated
- independent Eligibility identifier family → not required
- production proof → **ESTABLISHED**

## Continuing Eligibility Governance

The first production operation establishes that Eligibility can function as a real governed admission boundary.

It does not make any source automatically eligible for a future evaluation.

Eligibility remains evaluation-specific. A source must be assessed again where the purpose, scope, provenance, authority context, relevant state, relationship, reviewability, or applicable rules materially differ.

`Eligible Here ≠ Eligible Everywhere`
