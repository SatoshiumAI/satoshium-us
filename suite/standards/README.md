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


The broader Governance Review adds an additional governing distinction:

```text
Suite Governance
→ protects constitutional boundaries and shared governance controls

Institutional Governance
→ governs institution-owned responsibilities and canonical authority
```

The current controlling governance decision is:

```text
GDR-2026-0026
→ Satoshium Suite Governance Model
→ APPROVED
→ EFFECTIVE
```

## Standard Categories

### Certification Standard

Defines the canonical structure for certification determinations, including lifecycle, workflow, evidence, logic, schema, scoring, trust, and governance expectations.

### Evidence Standard

Defines what counts as evidence, how evidence is categorized, how evidence quality is assessed, and how evidence supports reviewable determinations.

### Trust Standard

Defines shared trust-related expectations, terminology, scope, and communication boundaries without creating generalized Suite-wide trust authority.

The Trust Standard does **not** create:

- a universal Suite-wide trust authority;
- a canonical Suite-wide `Trust Signal` object;
- a generic `trusted` status;
- authority over Attestor-owned Trust Statements; or
- authority over Beacon-owned Discovery Signals.

Canonical institutional boundaries remain:

```text
Attestor
→ Trust Statement

Beacon
→ Discovery Signal
```

### Scoring Standard

Defines how scores may be calculated, bounded, explained, and connected to governed outcomes in contexts that explicitly adopt scoring.

It does **not** create generalized Suite-wide scoring authority.

```text
Score
≠ Trust Statement

Score
≠ universal trust status
```

Institutional adoption of scoring remains explicit and subject to the authority of the institution applying it.

### Governance Standard

Defines how official Suite Standards are maintained, changed, versioned, deprecated, superseded, and preserved.

The Governance Standard is a **standards-governance instrument**. It is distinct from the broader **Satoshium Suite Governance Model**, which governs constitutional authority, institutional sovereignty, canonical ownership, governance decisions, change control, constitutional admission, accountability, and historical preservation across the Suite.

```text
Governance Standard
→ governs maintenance and evolution of Suite Standards

Suite Governance Model
→ governs constitutional authority and change across the Suite
```

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
- Beacon Discovery Signals; Discovery Metadata remains supporting structure;
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
- distinguish standards from methodology and operational evidence;
- distinguish the Governance Standard from the broader Suite Governance Model;
- avoid language implying generalized Suite-wide trust or scoring authority.

README reconciliation documents the Standards architecture that exists. It does not redesign it.
