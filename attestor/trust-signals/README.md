# Satoshium Attestor — Trust Signals

## Page

`/attestor/trust-signals/`

## Purpose

This page reconciles the pre-Suite **Trust Signals** concept with the current Satoshium Suite architecture.

Within Attestor, a **trust signal** is retained as a human-readable description for information or an indicator that may be relevant to evaluating an Attestation or supporting a Trust Statement.

This reconciliation does **not** establish a Trust Signal as a separate canonical Attestor object, controlled record type, score, or final conclusion.

## Critical Namespace Boundary

> **Attestor trust signals are not Beacon Discovery Signals.**

Beacon owns:

**Beacon → Discovery Signal / Discovery Metadata**

Attestor owns:

**Attestor → Trust Statement**

The shared word “signal” must not create institutional ambiguity.

Beacon Discovery Signals are canonical Beacon outputs used for discovery. Attestor trust signals, as presently understood, are descriptive trust-relevant evaluation context.

## Architectural Status

The term **trust signal** remains useful for explaining that certain governed facts, evidence, relationships, outcomes, or historical conditions may matter during trust evaluation.

However, advanced Attestor architecture must still determine whether “trust signal” needs formal machine representation at all.

Possible future outcomes include:

- retaining the term only as explanatory language;
- representing trust-relevant factors inside Attestation evaluation;
- defining a controlled evaluation-factor structure under another name;
- establishing a formal Attestor construct if a genuine architectural requirement emerges.

No option is adopted by this foundational reconciliation.

## Trust-Relevant Context

The page recognizes several conceptual sources of trust-relevant context:

- Attestation context;
- Evidence context;
- Authoritative outcome context;
- Historical and relationship context;
- Accountability context;
- Conflicting or uncertain context.

These are descriptive categories, not controlled machine values.

## No Reputation Model

The June-era page connected Trust Signals to reputation and included **Reputation Signals**.

That framing is not carried forward as established Attestor architecture.

Attestor currently owns Trust Statements, not a canonical reputation object, reputation score, or reputation system.

## No Directional Signal Vocabulary

The earlier page described signals as:

- positive;
- negative;
- neutral;
- mixed;
- uncertain.

Those values are not adopted here.

Attestor has not yet established a directional, scoring, weighting, or reputation model. Advanced architecture should not inherit those labels without first demonstrating that such a model is necessary and compatible with Attestor's bounded responsibility.

## Relationship to Evidence

A trust-relevant interpretation is not the same as the underlying evidence.

Evidence retains its own source, provenance, authority, relevance, and status.

The interpretation of that evidence during Attestor evaluation must not overwrite or redefine the evidence itself.

## Relationship to Trust Statements

Conceptually:

`Governed Inputs → Trust-Relevant Context → Attestor Evaluation → Trust Statement`

Trust-relevant context does not independently produce a Trust Statement.

The applicable Attestor rules, evidence, authoritative references, provenance, scope, status, limitations, and evaluation process govern the conclusion.

## Governing Principle

> **Reference does not transfer authority.**

This applies both to authoritative Suite objects and to any trust-relevant meaning Attestor derives from them.

## Reconciliation Notes

This revision makes a substantial change to the June-era page.

Major changes include:

- preserving “trust signal” only as a descriptive Attestor concept at this stage;
- explicitly separating Attestor trust signals from Beacon Discovery Signals;
- removing Attestation Signals, Evidence Signals, Verification Signals, Reputation Signals, Accountability Signals, and Correction Signals as implied formal categories;
- replacing those categories with broader descriptive evaluation-context areas;
- removing the pre-Suite `Signal → Context → Evaluation → Trust` model;
- replacing “Trust” as the endpoint with Attestor's canonical **Trust Statement**;
- removing the implied reputation architecture;
- removing positive/negative/neutral/mixed/uncertain as established directional values;
- adding conflicting and uncertain evidence treatment;
- preserving institutional authority boundaries;
- deferring the question of whether a formal trust-signal object should exist at all.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- whether “Trust Signal” should remain a formal Attestor term;
- whether a separate trust-signal object is necessary;
- whether trust-relevant factors require controlled machine representation;
- naming if a formal evaluation-factor structure is adopted;
- controlled values;
- directionality;
- weighting;
- scoring;
- aggregation;
- relationship to evidence sufficiency;
- relationship to Attestation Types;
- relationship to Trust Statement generation;
- lifecycle and versioning treatment;
- schemas and validation;
- conformance tests and reference vectors.

## Files

- `index.html` — public Trust Signals page.
- `README.md` — repository documentation for the Trust Signals page.
