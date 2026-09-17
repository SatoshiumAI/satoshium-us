# Satoshium Attestor — Identifiers

**Path:** `/attestor/identifiers/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
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

## Deferred Implementation Detail

This architecture establishes the canonical identifier families and governing semantics but leaves the following to later advanced architecture:

- allocation mechanics;
- sequence registry behavior;
- collision handling;
- machine validation patterns;
- URI representation;
- version-addressing conventions;
- operational assignment procedure.

These belong respectively to Schemas, Validation, Versioning, Publication, and Production.

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Identifiers → Established**

- Attestation identifier → `ATT-YYYY-NNNN`
- Trust Statement identifier → `TRST-YYYY-NNNN`
- Assignment → canonical Creation
- Reuse → prohibited
- Source identifiers → preserved as source-owned references
- Production proof → pending
