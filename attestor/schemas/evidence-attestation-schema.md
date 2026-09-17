# Evidence Attestation Schema — Foundational Candidate Profile

## Purpose
This document preserves the early concept of a specialized Attestation concerning Evidence.

It may eventually become an Attestation Type profile if advanced architecture determines that evidence-related assertions require a formal specialization.

It does not determine whether Evidence is correct or automatically sufficient.

## Foundational Meaning
An evidence-related Attestation may express a bounded assertion concerning:
- existence of Evidence;
- review of Evidence;
- relationship between Evidence and a subject/assertion;
- conflicting Evidence;
- incomplete or unavailable Evidence;
- relevant Evidence state or provenance.

## Candidate Structural Concepts
```yaml
attestation_identifier:
attestation_type:

attesting_authority:
subject:
assertion:
scope:

evidence_reference:
evidence_relationship:
source_references:
governed_references:
provenance:

status:
created_at:
updated_at:

limitations:
notes:
```

Exact field names and values are provisional.

## Evidence Relationship
The June schema proposed values such as `supports`, `partially_supports`, `contradicts`, `neutral`, and `unclear`.

These remain useful **candidate semantics**, but they are not adopted controlled values.

## Evidence Is Not Proof
Evidence informs Attestor evaluation.

An evidence-related Attestation does not automatically establish:
- truth;
- certification;
- verification;
- a favorable conclusion;
- a Trust Statement.

## Authority
Evidence and referenced source objects retain their originating authority.

> **Reference does not transfer authority.**

## Deferred
Advanced architecture must determine:
- whether this is a formal Attestation Type profile;
- eligibility rules;
- Evidence reference model;
- controlled relationship values;
- provenance requirements;
- uncertainty representation;
- validation and conformance.

## Status
Foundational candidate profile only.
