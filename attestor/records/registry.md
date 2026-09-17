# Registry Reference Profile

## Purpose
Describes how Attestor may reference a **Satoshium Registry Record** when the registered object or its status is relevant and eligible for Attestor evaluation.

## Canonical Boundary
**Registry → Satoshium Registry Record**  
**Attestor → Trust Statement**

Attestor does not recreate, reclassify, register, or modify the Registry record.

## Reference Requirements
A Registry reference should preserve enough information to identify the SREG identifier or authoritative Registry reference, Registry-governed record type/classification, relevant status/state, provenance, scope and relevance, relationship to the Attestation/evaluation, and Registry authority.

## Change
If a Registry record changes, Attestor may need to review its own Attestation or Trust Statement. Attestor does not perform the Registry lifecycle operation.

## Governing Principle
> **Reference does not transfer authority.**

## Status
Foundational reference profile. Exact fields, source-state handling, change triggers, validation, and schemas remain advanced architecture.
