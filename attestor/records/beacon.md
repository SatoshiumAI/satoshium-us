# Beacon Reference Profile

## Purpose
Describes how Attestor may reference **Beacon Discovery Signals and Discovery Metadata** when discovery context is relevant and eligible for evaluation.

## Canonical Boundary
**Beacon → Discovery Signal / Discovery Metadata**  
**Attestor → Trust Statement**

Attestor does not create or redefine Beacon Discovery Signals.

## Discovery Is Not Trust
A Beacon signal may identify or surface governed information. Discovery does not automatically establish evidence sufficiency, an Attestation, or a Trust Statement.

## Reference Requirements
A Beacon reference should preserve enough information to identify the Beacon signal or discovery object, Beacon identifier, source/provenance relationship, relevant status/state, scope and relevance, relationship to the Attestation/evaluation, and Beacon authority.

## Terminology Boundary
Attestor's earlier descriptive phrase **trust signal** must not be confused with Beacon's canonical **Discovery Signal**.

## Governing Principle
> **Reference does not transfer authority.**

## Status
Foundational reference profile. Exact eligibility, discovery-reference schemas, validation, and source-state handling remain advanced architecture.
