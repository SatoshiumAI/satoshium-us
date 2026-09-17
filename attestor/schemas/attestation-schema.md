# Attestation Schema — Foundational Candidate Profile

## Purpose
This document preserves and reconciles the early structural work for representing an **Attestation** within Satoshium Attestor.

An Attestation is a governed, attributable assertion about a subject, record, relationship, condition, event, or other trust-relevant matter.

This document is **not yet a normative machine schema**.

## Canonical Context
**Attestor → Trust Statement**

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

An Attestation is not the final Trust Statement.

## Candidate Structural Model
The reconciled foundation indicates that an Attestation will need to represent concepts such as:

```yaml
attestation_identifier:
attestation_type:
status:

attesting_authority:
subject:
assertion:
scope:

evidence_references:
source_references:
governed_references:
provenance:

created_at:
updated_at:

limitations:
notes:
```

Field names and cardinality are provisional.

## Foundational Requirements
A future normative Attestation schema should be capable of preserving:
- identity of the Attestation;
- Attestation Type;
- responsible Attesting Authority;
- subject;
- assertion;
- scope;
- Evidence relationships;
- authoritative/source references;
- provenance;
- relevant status/state;
- limitations and uncertainty where material;
- traceability to related governed objects.

## Not Yet Adopted
The June schema proposed identifiers such as `ATT-000001`, fixed status values, identity-oriented examples, confidence indicators, and several Attestation Types.

Those examples are not carried forward as normative values.

In particular, no final decision has been made on:
- identifier format;
- exact required fields;
- status vocabulary;
- confidence representation;
- controlled Attestation Types;
- timestamp rules;
- machine serialization.

## Authority Boundary
References to Registry, Chronicle, Anchor, Beacon, Certifier, Atlas, Navigator, or external sources remain references to objects governed by their respective authorities.

> **Reference does not transfer authority.**

## Status
Foundational candidate profile. Normative schema design, validation, controlled values, and conformance remain Advanced Architecture.
