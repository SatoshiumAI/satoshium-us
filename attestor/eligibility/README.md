# Satoshium Attestor — Eligibility

**Path:** `/attestor/eligibility/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
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

Exact machine validation is deferred to Schemas and Validation.

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

Detailed recording requirements belong to Evaluation and Methodology.

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

**Eligibility → Established**

- eligibility → evaluation-specific governed admission
- availability → insufficient by itself
- authority → insufficient by itself
- provenance → necessary where material, not sufficient by itself
- unfavorable evidence → not excludable merely because unfavorable
- material exclusions → reviewable where required
- machine eligibility rules → deferred to Validation / Schemas
- production proof → pending
