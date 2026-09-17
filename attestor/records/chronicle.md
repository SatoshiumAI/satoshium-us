# Chronicle Reference Profile — Advanced Architecture

## Purpose
Defines how Attestor may reference a **Chronicle Entry** when preserved historical context is relevant and eligible for Attestor evaluation.

## Canonical Boundary
**Chronicle → Chronicle Entry**  
**Attestor → Trust Statement**

Chronicle remains authoritative for its canonical historical entry. Attestor does not rewrite Chronicle history.

## Governed Reference Context
Preserve, as applicable:
- Chronicle identifier/reference;
- relevant event/state;
- provenance;
- temporal context;
- version/state where applicable;
- scope and relevance;
- relationship to the Attestation/evaluation;
- material limitations; and
- Chronicle authority context (`Suite-source`).

## Historical State
Attestor must distinguish the source state evaluated at Time T from later source state where material.

`Source State at Evaluation ≠ Later Source State`

## Eligibility
Historical relevance does not automatically establish eligibility or Evaluation Outcome.

## Governing Principle
> **Reference does not transfer authority.**

## Status
Advanced governed Reference Profile.
