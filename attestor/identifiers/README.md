# Satoshium Attestor — Identifiers

**Path:** `/attestor/identifiers/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Identifiers  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

The Identifiers architecture establishes canonical identity for Attestor-owned objects while preserving the identifiers and authority of referenced source objects.

## Canonical Identifier Families

### Attestation

`ATT-YYYY-NNNN`

- `ATT` → Attestation
- `YYYY` → canonical creation year
- `NNNN` → four-digit sequence

### Trust Statement

`TRST-YYYY-NNNN`

- `TRST` → Trust Statement
- `YYYY` → canonical creation year
- `NNNN` → four-digit sequence

## Governing Relationship

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

The identifier model preserves the Entry Model distinction between assertion and conclusion. Attestations and Trust Statements are distinct governed objects and therefore have distinct canonical identities.

## Assignment

A canonical Attestor identifier is assigned at **canonical Creation**.

Candidate preparation, source review, drafting, or other pre-creation work does not consume or imply a canonical identifier.

`Candidate / Preparation → No canonical identifier`

`Canonical Creation → Identifier assigned`

## Persistence and Uniqueness

Once assigned:

- the identifier remains attached to its canonical object;
- it is not reused for another object;
- lifecycle or publication changes do not replace the identifier;
- versioning does not silently transfer the identifier to a different canonical object;
- a new canonical object receives a new identifier.

Detailed version behavior is governed by the later Versioning architecture.

## Source Identifiers

Source identifiers remain source-owned.

Examples include:

- `SC-CERT-*` → Certifier
- `SREG-*` → Registry
- `CHR-*` → Chronicle
- `ANCH-*` → Anchor
- `BEAC-*` → Beacon
- `ATT-*` → Attestor Attestation
- `TRST-*` → Attestor Trust Statement

**Reference does not transfer authority.**

Attestor preserves source identifiers as governed references rather than reissuing them inside an Attestor namespace.

## Identifier Semantics

An identifier establishes identity. It does not by itself establish:

- validation;
- conformance;
- lifecycle state;
- publication state;
- evidence sufficiency;
- currency;
- a favorable evaluation;
- trustworthiness; or
- a Trust Statement conclusion.

## Implementation Boundary

The first production operation has exercised canonical identifier assignment, persistence, source-identifier preservation, machine validation of the production representations, and public class-specific URI representation.

Implementation details remain subordinate to the established architecture, including:

- allocation and sequence-registry mechanics not otherwise fixed by Production;
- collision-prevention mechanics;
- future identifier-pattern changes, if ever governed;
- version-addressing conventions beyond the production paths exercised; and
- future operational allocation procedures.

Schemas, Validation, Versioning, Publication, and Production govern their respective implementation responsibilities.

## First Production Identifier Demonstration

The first controlled production operation exercised both canonical Attestor identifier families:

- `ATT-2026-0001` → first canonical production Attestation;
- `TRST-2026-0001` → first canonical production Trust Statement.

The operation demonstrated the assignment boundary:

`Pre-Creation Preparation → No canonical production identifier`

`Canonical Creation → ATT-2026-0001 / TRST-2026-0001 assigned`

The identifiers were not used for representative fixtures or preallocated production placeholders. Representative validation fixtures remained in the separate `9001` range and were explicitly non-production.

After canonical Creation, both identifiers persisted through:

- relationship correction;
- Validation;
- Governed Review;
- Conformance;
- lifecycle activation;
- Publication; and
- final published-state revalidation.

Neither identifier was replaced when lifecycle or publication state changed.

The bounded relationship-serialization correction also preserved both canonical identifiers because the governed materiality determination did not require a new canonical object.

**Identifier Architecture → DEMONSTRATED IN PRODUCTION**

## Production Namespace and Publication Demonstration

Production preserved source-owned identifiers including:

- `SC-CERT-2026-0001`;
- `SREG-2026-0001`;
- `CHR-2026-0001`;
- `ANCH-2026-0001`; and
- `BEAC-2026-0001`.

Those identifiers remained references to their originating Suite objects and were not reissued as ATT/TRST identifiers.

The canonical Attestor objects were publicly represented through class-specific paths:

- `/attestor/attestations/ATT-2026-0001/`
- `/attestor/trust-statements/TRST-2026-0001/`

This demonstrates public addressability without creating a generic Attestor record namespace for canonical ATT/TRST objects.

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Identifiers → Established and Production-Proven**

- Attestation identifier → `ATT-YYYY-NNNN` → production-exercised
- Trust Statement identifier → `TRST-YYYY-NNNN` → production-exercised
- first production identities → `ATT-2026-0001` and `TRST-2026-0001`
- assignment → canonical Creation → demonstrated
- pre-creation non-allocation → demonstrated
- representative / production separation → demonstrated
- reuse → prohibited and avoided
- persistence through correction → demonstrated
- persistence through lifecycle activation → demonstrated
- persistence through Publication → demonstrated
- source identifiers → preserved as source-owned references
- class-specific public addressability → demonstrated
- production proof → **ESTABLISHED**

## Continuing Identifier Governance

Production proof does not establish that every future sequence-allocation or collision-handling implementation has been exercised.

The standing boundaries remain:

`Identifier ≠ Validation`

`Identifier ≠ Conformance`

`Identifier ≠ Lifecycle State`

`Identifier ≠ Publication`

`Identifier ≠ Evidence Sufficiency`

`Identifier ≠ Evaluation Outcome`

`Identifier ≠ Trustworthiness`

A material change requiring a new canonical object requires a new canonical identifier.

**Reference does not transfer authority.**
