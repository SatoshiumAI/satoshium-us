# Satoshium Attestor — Entry Model

**Path:** `/attestor/entry-model/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

The Entry Model defines the complete conceptual structure of an Attestation and a Trust Statement and establishes the governed relationship between them.

It is the first dependency in Attestor Advanced Architecture. It defines the conceptual object boundary before identifiers, controlled values, schemas, lifecycle rules, validation, conformance, publication, or production behavior are finalized.

## Governing Relationship

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Governing Principle

**Reference does not transfer authority.**

Referenced objects retain the authority of their source institutions. Attestor owns its governed Attestor objects and the Trust Statements it produces; it does not acquire source authority merely by referencing or evaluating source material.

## Core Distinction

### Attestation

An **Attestation** is a governed, attributable assertion presented for an Attestor purpose and evaluation.

Conceptually it preserves:

- Attestation identity
- Attestation type / classification context
- Attesting Authority
- Subject
- Assertion
- Scope
- Evidence references
- Source / governed references
- Provenance
- Relevant time / state
- Status / lifecycle context
- Limitations / uncertainty
- Relationships

### Trust Statement

A **Trust Statement** is Attestor's canonical output: a governed, attributable, bounded conclusion produced through rule-constrained evaluation.

Conceptually it preserves:

- Trust Statement identity
- Subject
- Bounded conclusion
- Scope
- Attestor attribution
- Supporting Attestation(s)
- Evidence / authoritative references
- Evaluation basis
- Provenance
- Relevant time / state
- Status / lifecycle context
- Limitations / uncertainty
- Relationships

## Assertion vs. Conclusion

`Attestation → Rule-Constrained Evaluation → Trust Statement`

An Attestation is not automatically a Trust Statement, and evidence or authoritative references do not automatically determine the outcome.

## Authority Boundary

- Atlas → Authoritative Intelligence
- Navigator → Workflow Definition / Orchestration
- Certifier → Certification Package
- Registry → Satoshium Registry Record
- Chronicle → Chronicle Entry
- Anchor → Integrity Reference
- Beacon → Discovery Signal / Discovery Metadata
- Attestor → Trust Statement

## What This Page Does Not Yet Establish

The Entry Model does not yet establish exact identifier syntax, normative machine field names, required/optional cardinality, final controlled values, final Attestation Types, lifecycle states, versioning rules, validation rules, conformance requirements, publication states, or serialization formats.

Those are resolved through the remaining Advanced Architecture pages.

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Entry Model → Established**

The conceptual distinction and relationship between Attestation and Trust Statement are established. Normative machine architecture and production proof remain pending.
