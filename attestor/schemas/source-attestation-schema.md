# Source Attestation Schema — Foundational Candidate Profile

## Purpose
This document preserves the early concept of a specialized Attestation concerning a source or provenance relationship.

It may eventually become a Source / Provenance Attestation Type profile if advanced architecture adopts that specialization.

It does not determine that a source is correct, trustworthy, authoritative, or eligible merely because it exists.

## Foundational Meaning
A source-related Attestation may express a bounded assertion concerning:
- source existence;
- authorship or origin;
- provenance;
- relevance;
- relationship to a subject;
- known limitations;
- whether the source supports, conflicts with, documents, references, or mentions something.

## Candidate Structural Concepts
```yaml
attestation_identifier:
attestation_type:

attesting_authority:
subject:
assertion:
scope:

source_reference:
source_relationship:
evidence_references:
governed_references:
provenance:

status:
created_at:
updated_at:

limitations:
notes:
```

Exact field names and controlled values are provisional.

## Source Relationships
The June schema proposed values such as `supports`, `partially_supports`, `contradicts`, `references`, `documents`, `mentions`, and `unclear`.

These remain candidate semantics only.

## Source Authority
A source-related Attestation does not transfer source authority to Attestor.

> **Reference does not transfer authority.**

## Availability Is Not Eligibility
A source being public, technically accessible, or referenced elsewhere does not automatically make it eligible for Attestor evaluation.

## Deferred
Advanced architecture must determine:
- whether this becomes a formal Attestation Type profile;
- source eligibility;
- source classification;
- provenance requirements;
- controlled relationship values;
- validation;
- external-source handling;
- source-state change behavior.

## Status
Foundational candidate profile only.
