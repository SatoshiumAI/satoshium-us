# Satoshium Attestor — Records / Reference Profiles

**Path:** `/attestor/records/`  
**Current Stage:** Operational Reference Profiles  
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

## First Production Reference-Profile Demonstration

The first controlled production operation exercised governed references to six source objects or source contexts:

- `SC-CERT-2026-0001` → Certifier authority preserved;
- Atlas Jurisdiction Record — El Salvador → Atlas authority preserved;
- `SREG-2026-0001` → Registry authority preserved;
- `CHR-2026-0001` → Chronicle authority preserved;
- `ANCH-2026-0001` → Anchor authority preserved within its defined SCRD integrity scope; and
- `BEAC-2026-0001` → Beacon authority preserved.

All six source inputs received governed Eligibility determinations before use.

They remained distinct from:

- `ATT-2026-0001` → Attestor-owned canonical Attestation; and
- `TRST-2026-0001` → Attestor-owned canonical Trust Statement.

The operation demonstrated that governed reference can preserve source identity, provenance, state/scope context, and authority without creating duplicate Attestor-owned source records.

**Reference-Profile Architecture → DEMONSTRATED IN PRODUCTION**

## Records Namespace Boundary

The route `/attestor/records/` is retained as the documentation namespace for governed Reference Profiles.

It is **not** the canonical publication namespace for ATT/TRST objects.

Canonical production object paths are class-specific:

- `/attestor/attestations/ATT-YYYY-NNNN/`
- `/attestor/trust-statements/TRST-YYYY-NNNN/`

Therefore:

`Records Route ≠ Canonical ATT/TRST Object Namespace`

`Reference Profile ≠ Source Object Copy`

`Reference ≠ Authority Transfer`

## Status

**Reference Profiles → Established and Production-Proven**

- Suite-source reference model → production-exercised
- Eligibility-before-use → production-exercised
- source authority preservation → demonstrated
- source provenance / state context → demonstrated
- cross-institution relationships → demonstrated
- Records namespace boundary → explicit
- external-source profile → established but not exercised by first production operation
- canonical ATT/TRST publication → separate object-class namespaces
- production proof → **ESTABLISHED for Suite-source reference profiles exercised**

## Continuing Reference Governance

Production proof is bounded to the source classes and relationships actually exercised.

It does not establish that:

- every future source is eligible;
- every external source profile has been production-tested;
- reference establishes support;
- reference transfers authority;
- a referenced source becomes an Attestor-owned object; or
- a source-state change predetermines the Attestor response.

`Availability ≠ Eligibility`

`Reference ≠ Eligibility`

`Reference ≠ Support`

`Connection ≠ Identity`

**Reference does not transfer authority.**

Exact machine representation and profile-specific validation requirements remain subordinate to normative Schemas and Validation.

