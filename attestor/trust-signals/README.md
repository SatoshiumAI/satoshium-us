# Satoshium Attestor — Trust Signals

## Page
`/attestor/trust-signals/`

## Purpose
This page preserves the historical **Trust Signals** concept while recording its final place in the established Satoshium Attestor architecture.

## Architectural Determination
> **Trust Signal is legacy / descriptive Attestor terminology only.**

Attestor does **not** establish Trust Signal as:
- a canonical object;
- a controlled record type;
- an Evaluation Outcome;
- a reputation object;
- a confidence percentage;
- a score;
- a weighting mechanism;
- a directional machine vocabulary.

Trust-relevant considerations are represented through the architecture that already governs Attestations, eligible governed inputs, Evidence, Provenance, Relationships, Evaluation, limitations, uncertainty, Lifecycle, and Trust Statements.

A parallel Trust Signal object model is not required.

## Critical Namespace Boundary
> **Attestor trust signals are not Beacon Discovery Signals.**

**Beacon → Discovery Signal / Discovery Metadata**

**Attestor → Trust Statement**

Beacon Discovery Signals are canonical Beacon outputs.

Attestor “trust signal” is historical/descriptive language only.

## Canonical Attestor Model
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

Trust-relevant context may inform this process, but it is not an intervening canonical object.

## Historical / Descriptive Context
The phrase “trust signal” may still be useful in historical material or explanatory prose to describe information relevant to evaluation.

Examples may include:
- Attestation context;
- Evidence context;
- authoritative outcome context;
- historical and relationship context;
- accountability context;
- conflicting or uncertain context.

These are descriptive categories, not controlled Attestor values.

## Evidence Boundary
Evidence remains distinct from any interpretation made during evaluation.

> **Evidence ≠ Trust Signal ≠ Evaluation Outcome**

Evidence preserves its source, provenance, relevant state, authority, relevance, scope, and limitations.

## Relationship Boundary
The adopted relationship vocabulary includes:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

These relationships provide governed semantic structure without requiring a separate Trust Signal layer.

> **supports ≠ supported**

## Evaluation Boundary
Adopted Evaluation Outcomes are:
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

These outcomes replace any need to interpret historical positive / negative / neutral / mixed / uncertain signal direction as formal Attestor vocabulary.

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## No Reputation or Scoring Model
Attestor does not establish:
- generic reputation;
- a canonical reputation object;
- reputation scoring;
- trust scoring;
- confidence percentages;
- universal evidence weighting;
- majority-source rules;
- directional signal aggregation.

The canonical institutional output remains the bounded **Trust Statement**.

## Schema and Template Treatment
Historical `trust-signal-schema.md` and `trust-signal-template.md` artifacts may be preserved for provenance and architectural history, but they are **legacy / historical only** and are not production Attestor schemas or templates.

They must not be interpreted as evidence that Trust Signal remains a canonical object.

## Governing Principle
> **Reference does not transfer authority.**

## Reconciliation Notes
This Advanced Architecture reconciliation resolves the question that the foundational page deliberately left open.

The adopted determination is:
- retain the route `/attestor/trust-signals/` as explanatory and historical documentation;
- retain “trust signal” only as descriptive language where useful;
- do not establish a Trust Signal canonical object;
- do not establish Trust Signal identifiers, lifecycle states, schemas, controlled values, scoring, directionality, weighting, or aggregation;
- use the established Evidence, Provenance, Relationships, Evaluation, uncertainty, limitations, and Trust Statement architecture instead;
- preserve a strict namespace boundary from Beacon Discovery Signals.

## Status
**Trust Signals → Advanced Architecture reconciled.**

No further Trust Signal architecture is required for Attestor production readiness.

Remaining Attestor implementation work belongs to the canonical architecture, not to a separate Trust Signal system.

## Files
- `index.html` — public Trust Signals page.
- `README.md` — repository documentation.
