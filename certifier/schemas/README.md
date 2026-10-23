# Satoshium Certifier — Schemas

**Path:** `/certifier/schemas/`  
**Institution:** Satoshium Certifier  
**Status:** Current documentation of a legacy draft schema and its governing boundaries  
**Reviewed:** October 23, 2026

## Purpose

This directory holds structured data-model materials associated with Satoshium Certifier. Schemas describe record structure and may support validation, machine exchange, portability, and interoperability. **A schema is not a canonical object, a certification determination, or an institutional authority.**

The **Certification Package** is Certifier's canonical operational object. The Package, its governed lifecycle and determination, and its generated artifacts must be interpreted under the current Suite Reconciliation, Interoperability Review, Governance Review, and Certifier documentation.

## Current Contents

- `certification-schema.json` — **July 1, 2026 draft legacy data-model specimen (v1.0)**. Its own metadata identifies it as `draft`. It records an earlier model; it is **not** declared here to be the controlling production schema or a machine-enforced JSON Schema validator.

No other schema filenames mentioned in historical planning are implied to exist merely by being proposed.

## Historical Draft Boundary

The July draft retains historical terms and assumptions such as `subsystem`, `certification_record`, `registry_entry`, `history.event_type`, and `determination_result` values that mix certification outcomes with later lifecycle states. These fields should **not** be treated as current governing definitions.

In particular:

- **Certification determination ≠ lifecycle state.** Revocation and expiration are not fresh certification determinations simply because the draft lists them among allowed results.
- **History/event fields ≠ Chronicle Entry.** Chronicle independently governs its canonical Chronicle Entries.
- **Registry reference fields ≠ SREG creation.** Registry alone creates and governs its Registry Entries.
- **Attestation fields or references ≠ Attestation or Trust Statement.** Attestor governs its Attestations and bounded Trust Statements through Rule-Constrained Evaluation.
- **Schema validation ≠ eligibility, evaluation, conformance, certification, or publication.**
- **Representation ≠ canonical identity.** SCRD HTML and JSON are representations of the same Certifier-controlled Certified Record, not separate certification authorities.

The JSON draft is preserved unaltered for historical continuity. Before it is used as an active production or interoperable validation contract, its fields, allowed values, semantics, implementation, and compatibility must be assessed against current controlling artifacts.

## Current Certification Record Model

```text
Certifier (institutional certification authority)
  → Certification Package (canonical operational object)
    → SCPR / SCR / SCRD and supporting evidence artifacts
    → governed references to other institution-owned objects
```

The Package is authoritative within Certifier's settled subject area. Schemas describe representations and constraints; they do not independently create that authority.

## Interoperability Boundaries

- **Atlas** retains authority over the source jurisdiction intelligence.
- **Registry** owns Satoshium Registry Entries (SREG).
- **Chronicle** owns Chronicle Entries.
- **Anchor** owns Integrity References (ANCH), limited to defined representations.
- **Beacon** owns Discovery Signals (BEAC).
- **Attestor** owns Attestations (ATT) and Trust Statements (TRST).
- **Navigator** owns Navigator Workflow Definitions and orchestrates workflows without taking institutional decisions.

Downstream references are conditional relationships, not a mandatory Suite-wide production pipeline.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Schema and Implementation Discipline

Any new or revised machine-readable schema should:

1. identify whether it is a template, historical draft, current specification, or production-enforced validator;
2. state the governed object and the institution responsible for it;
3. distinguish record identity, versions, lifecycle, evaluation outcomes, references, and publication;
4. preserve compatibility and historical interpretability rather than silently changing issued records;
5. distinguish structural validation from governed certification or trust evaluation;
6. be checked against actual production records and the operational toolkit before asserting production conformance.

No migration, replacement schema, or new canonical object is authorized by this README.

## Related Current Documentation

- `../schema/README.md` — broader Certifier schema/representation explanation
- `../interoperability/README.md` — current institutional relationships
- `../workflow/` — current certification workflow
- `../../suite/interoperability/` — Suite interoperability
- `../../suite/governance/` — Suite governance

The July 2026 files under `../docs/` are historical and non-controlling.

## Governing Principle

**Schemas structure and constrain representations. Certifier governs certification. Other institutions govern their own canonical objects.**
