# Satoshium Attestor — Trust Signals

## Page
`/attestor/trust-signals/`

## Purpose
This page preserves the historical **Trust Signals** concept while recording its final place in the operational Satoshium Attestor architecture.

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

## Production Confirmation
The first controlled production operation confirms the architectural determination that a separate Trust Signal layer is unnecessary.

The production path was:

`Eligible Governed Inputs → ATT-2026-0001 → Rule-Constrained Evaluation → supported → TRST-2026-0001`

No canonical Trust Signal object was created between the governed inputs, Attestation, Evaluation, and Trust Statement.

No Trust Signal identifier was assigned.

No Trust Signal lifecycle or publication state was required.

No Trust Signal schema or production template was invoked.

No confidence percentage, reputation score, directional signal, weighting mechanism, or signal aggregation was used.

Trust-relevant context was represented through the canonical architecture already governing Eligibility, Evidence, Provenance, Authority, Relationships, Evaluation, limitations, and the bounded Trust Statement.

**Trust Signal noncanonical boundary → CONFIRMED IN PRODUCTION**

The production operation also used `BEAC-2026-0001` as a governed reference while preserving Beacon's ownership of its Discovery Signal / Discovery Metadata. This operationally demonstrated that an Attestor historical “trust signal” concept is not a Beacon Discovery Signal and that reference does not transfer authority.

## Reconciliation Notes
The architecture resolves the question that the foundational page deliberately left open.

The adopted determination is:
- retain the route `/attestor/trust-signals/` as explanatory and historical documentation;
- retain “trust signal” only as descriptive language where useful;
- do not establish a Trust Signal canonical object;
- do not establish Trust Signal identifiers, lifecycle states, schemas, controlled values, scoring, directionality, weighting, or aggregation;
- use the established Evidence, Provenance, Relationships, Evaluation, uncertainty, limitations, and Trust Statement architecture instead;
- preserve a strict namespace boundary from Beacon Discovery Signals.

## Status
**Trust Signals → Legacy / Descriptive Boundary Established and Production-Confirmed**

- canonical Attestor Trust Signal object → not adopted
- Trust Signal identifier family → not adopted
- Trust Signal lifecycle / publication state → not adopted
- Trust Signal controlled machine vocabulary → not adopted
- Trust Signal production schema / template → not adopted
- confidence / reputation scoring → not adopted
- directional positive / negative / neutral / mixed / uncertain vocabulary → not adopted
- weighting / aggregation model → not adopted
- canonical Attestor output → Trust Statement
- Beacon Discovery Signal namespace → preserved as Beacon-owned
- `BEAC-2026-0001` reference boundary → production-demonstrated
- first production operation → completed without a Trust Signal object layer
- production confirmation → **ESTABLISHED**

No further Trust Signal architecture is required for Attestor production.

Historical `trust-signal-schema.md` and `trust-signal-template.md` artifacts may remain for provenance, but they are legacy/non-operational and must not be presented as current production contracts.

## Continuing Governance

`Trust Signal ≠ Trust Statement`

`Trust Signal ≠ Evaluation Outcome`

`Trust Signal ≠ Beacon Discovery Signal`

`Evidence ≠ Trust Signal ≠ Evaluation Outcome`

`supports ≠ supported`

**Reference does not transfer authority.**

## Files
- `index.html` — public Trust Signals page.
- `README.md` — repository documentation.
