# Satoshium Suite — Standards

**Path:** `/suite/standards/`  
**Public page:** `index.html`  
**Status:** Active Suite-wide standards surface

## Purpose

The `/suite/standards/` directory defines the canonical rule layer used across the Satoshium Suite.

Standards establish the expectations and rules that govern what Suite institutions recognize, evaluate, record, publish, preserve, exchange, and interpret within their respective authorities.

This directory documents rule expectations.

It does not replace the institutional authority of Atlas, Navigator, Certifier, Registry, Chronicle, Anchor, Beacon, or Attestor.

## Public Page Relationship

`index.html` is the principal public representation of this directory.

The current page presents the following standards:

- Certification Standard
- Evidence Standard
- Trust Standard
- Scoring Standard
- Governance Standard
- Interoperability Standard
- Schema Standard
- Terminology Standard
- Versions Standard

These standards collectively define the rule framework that supports consistent Suite behavior across institutions and records.

## Standards Role

The current page establishes the following principle:

> Standards are the rule layer of the Satoshium Suite.

Standards define expectations.

Institutional implementations apply those expectations within their own bounded authority.

This distinction is important:

- Standards define what is expected.
- Methodology defines how expectations are implemented.
- Institutions perform their own governed operations.
- Canonical objects remain owned by their originating institutions.

## Standard Categories

### Certification Standard

Defines the canonical structure for certification determinations, including lifecycle, workflow, evidence, logic, schema, scoring, trust, and governance expectations.

### Evidence Standard

Defines what counts as evidence, how evidence is categorized, how evidence quality is assessed, and how evidence supports reviewable determinations.

### Trust Standard

Defines how trust signals are identified, interpreted, bounded, and communicated across Suite records and public verification surfaces.

### Scoring Standard

Defines how scores may be calculated, bounded, explained, and connected to certification outcomes without replacing human-readable evidence.

### Governance Standard

Defines how standards are maintained, changed, versioned, deprecated, and preserved as the Suite matures.

### Interoperability Standard

Defines how Suite institutions exchange, reference, and interpret records consistently across Certifier, Registry, Anchor, Beacon, Attestor, Navigator, Chronicle, and Atlas.

### Schema Standard

Defines expectations for machine-readable structures, shared objects, stable identifiers, metadata, and validation-ready Suite records.

### Terminology Standard

Defines canonical terms used across the Suite so that certification, attestation, registry, evidence, trust, and discovery language remains consistent.

### Versions Standard

Preserves the historical development of Satoshium Standards and identifies which version applies to a record, decision, or implementation.

## Relationship to Suite Institutions

Standards are Suite-wide.

They are not institutional records and do not inherit the authority of the institutions that implement them.

Likewise, an institution's use of a standard does not transfer institutional authority to the Standards layer.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

**Connection ≠ Identity.**  
**Reference ≠ Derivation.**  
**Reference ≠ Support.**  
**Reference ≠ Authority Transfer.**

## Canonical Boundaries

The Standards layer may define expectations that affect:

- certification;
- evidence;
- trust;
- scoring;
- governance;
- interoperability;
- schemas;
- terminology;
- versioning.

However, Standards do not themselves create the canonical outputs or exercise the operational authority of Suite institutions.

Examples include:

- Certifier Certification Packages;
- Satoshium Registry Records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals / Discovery Metadata;
- Attestor Attestations;
- Attestor Trust Statements;
- Navigator workflow definitions / orchestration; and
- Atlas Authoritative Intelligence.

Those responsibilities remain with their originating Suite institutions.

## Repository Convention

The current directory is expected to contain:

```text
/suite/standards/
├── index.html
├── README.md
├── certification/
├── evidence/
├── trust/
├── scoring/
├── governance/
├── interoperability/
├── schemas/
├── terminology/
└── versions/
```

Each subdirectory should document its own standard where appropriate.

## Maintenance

Repository maintenance for `/suite/standards/` should:

- keep the standards index aligned with the standards actually published;
- preserve clear separation between Suite-wide rules and institutional authority;
- version standards deliberately;
- preserve historical versions rather than silently overwriting them;
- keep terminology and schema expectations synchronized with adopted Suite architecture;
- avoid introducing implementation details into a standard unless the standard explicitly governs them;
- distinguish standards from methodology and operational evidence.

README reconciliation documents the Standards architecture that exists. It does not redesign it.
