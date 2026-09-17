# Satoshium Attestor — Records / Reference Profiles

**Path:** `/attestor/records/`  
**Architecture Stage:** Advanced Architecture / Implementation Layer  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

This directory contains governed **Reference Profiles** describing how Attestor may use eligible source objects without creating a second Attestor record system.

The route `/attestor/records/` is retained. Architecturally, the contents are Reference Profiles.

## Governing Principle

> **Reference does not transfer authority.**

A referenced object remains governed by its originating Suite institution or external authority.

## Reference Model

`Source Object → Governed Reference → Eligibility Determination → Attestation / Evaluation Basis → Rule-Constrained Evaluation → Trust Statement`

Availability or reference alone does not establish eligibility.

## Profiles

- `atlas.md` — Atlas Authoritative Intelligence
- `certifier.md` — Certifier Certification Package
- `registry.md` — Satoshium Registry Record
- `chronicle.md` — Chronicle Entry
- `anchor.md` — Anchor Integrity Reference
- `beacon.md` — Beacon Discovery Signal / Discovery Metadata
- `external.md` — eligible external sources

## Common Reference Requirements

A governed reference should preserve, as applicable:

- source object identifier or stable/resolvable reference;
- source institution or originating authority;
- source object/type context;
- relevant version or state;
- provenance;
- relevant time/state at evaluation;
- scope and relevance;
- relationship to the Attestation/evaluation;
- material limitations; and
- authority context.

## Eligibility

`Availability ≠ Eligibility`

`Authority ≠ Eligibility`

`Reference ≠ Eligibility`

Eligibility is determined for the particular Attestor evaluation under the adopted Eligibility architecture.

## Source-State Change

Material later change to a referenced source may trigger Attestor review.

`Material Source-State Change → Review`

A trigger does not automatically determine correction, supersession, withdrawal, or a new Trust Statement.

## Status

**Reference Profiles → Advanced architecture reconciled.**

Exact machine serialization and profile-specific validation requirements remain subordinate to normative Schemas and Validation.
