# Beacon Reference Profile — Advanced Architecture

## Purpose
Defines how Attestor may reference **Beacon Discovery Signals and Discovery Metadata** when discovery context is relevant and eligible for evaluation.

## Canonical Boundary
**Beacon → Discovery Signal / Discovery Metadata**  
**Attestor → Trust Statement**

Attestor does not create, redefine, or absorb Beacon Discovery Signals.

## Discovery Is Not Trust
Discovery may surface governed information. It does not automatically establish eligibility, evidence sufficiency, an Attestation, Evaluation Outcome, or Trust Statement.

## Governed Reference Context
Preserve, as applicable:
- BEAC identifier or discovery-object reference;
- source/provenance relationship;
- relevant status/state and version;
- relevant time/state at evaluation;
- scope and relevance;
- relationship to the Attestation/evaluation;
- material limitations; and
- Beacon authority context (`Suite-source`).

## Terminology Boundary
Beacon's canonical **Discovery Signal** must not be confused with the legacy Attestor phrase **Trust Signal**, which is not a canonical Attestor object.

## Change
Material Beacon/source-state change may trigger Attestor review.

## Governing Principle
> **Reference does not transfer authority.**

## Status
Advanced governed Reference Profile.
