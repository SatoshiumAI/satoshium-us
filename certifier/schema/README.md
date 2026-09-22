# Satoshium Certifier — Schema

**Path:** `/certifier/schema/`  
**Institution:** Satoshium Certifier  
**Surface:** Schema  
**Status:** Current repository documentation

## Purpose

This directory documents the structured formats used by **Satoshium Certifier** to represent Certification Packages, evidence inventories, generated artifacts, Certified Records, and governed Suite references.

The public page for this directory is:

- `index.html`

This README documents the schema role, canonical record hierarchy, representation model, portability expectations, and Suite boundaries of Certifier schema.

## Schema Role

Schema is Certifier's structural record layer.

It defines how Certifier records are represented so they can remain:

- consistent;
- reviewable;
- machine-readable;
- portable;
- versioned; and
- interoperable.

Schema does not certify by itself.

It preserves the structure of certification records produced through Suite Standards, Suite Methodology, evidence review, evaluation, and Certifier decision-making.

## Governing Relationship

The enduring relationship is:

```text
Suite Standards
        ↓
Suite Methodology
        ↓
Certifier
        ↓
Certification Package
        ↓
Generated Certifier Artifacts
        ↓
Governed Suite Relationships
```

The Certification Package remains Certifier's canonical operational record.

## Certification Package Schema

The Certification Package schema defines the structure of Certifier's canonical operational record.

It may include:

- Certification Subject;
- Profile;
- Scope;
- applicable Suite Standards;
- applicable Suite Methodology;
- Evidence Inventory;
- evaluation;
- certification decision;
- generated artifacts;
- lifecycle state; and
- certification history.

The schema preserves structure.

It does not independently create the certification decision.

## SCRD JSON Schema

The SCRD JSON schema defines the machine-readable representation of the Certified Record.

The SCRD HTML and SCRD JSON are two representations of the same Certified Record.

The JSON representation may support:

- public indexing;
- structured exchange;
- Registry integration;
- future APIs;
- machine validation; and
- long-term interoperability.

It does not create a separate certification object.

## Evidence Inventory Schema

The Evidence Inventory schema organizes factual materials associated with the Certification Package.

It may include:

- Evidence Record identifiers;
- source references;
- evidence types;
- traceability notes;
- review status;
- integrity-reference material; and
- mapped Suite Standards requirements.

Evidence structure supports traceability.

It does not replace evaluation or the certification decision.

## Generated Artifact Fields

Schema conventions may define fields used by generated Certifier artifacts including:

- Certification Process Report (SCPR);
- Certification Receipt (SCR);
- Certified Record HTML;
- Certified Record JSON;
- Evidence Maps; and
- governed Suite references.

Generated artifacts remain downstream from the Certification Package.

## Suite Reference Stubs

Certifier schema may prepare structured references for interoperability with other Suite institutions.

Examples include relationships to:

- **Registry** — SREG
- **Chronicle** — CHR
- **Anchor** — ANCH
- **Beacon** — Discovery Signal / Discovery Metadata
- **Attestor** — ATT / TRST
- **Navigator** — workflow definition / orchestration

These references do not make Certifier the owner of those downstream institutional objects.

## Schema Flow

The current schema relationship is:

```text
Certification Package Schema
        ↓
Evidence Inventory · Evidence Map
        ↓
SCPR · SCR · SCRD
        ↓
SCRD HTML · SCRD JSON
        ↓
Governed Suite Relationships
```

The Certifier artifacts remain Certifier-owned.

Downstream Suite objects remain owned by their respective institutions.

## Relationship to Suite Standards

Suite Standards define the expectations and schema requirements applicable across certification activity.

Certifier schema should remain aligned with those expectations without becoming a competing Suite-wide standards authority.

## Relationship to Suite Methodology

Suite Methodology defines implementation and repeatable process.

Certifier schema preserves records produced by that process.

Schema does not replace Methodology.

## Relationship to Registry

Registry owns the Satoshium Registry Entry / SREG.

Certifier schema may expose structured references suitable for Registry consumption, but Certifier does not own the Registry Entry.

## Relationship to Chronicle

Chronicle owns Chronicle Entries.

Certifier schema may preserve references or metadata supporting Chronicle chronology, but Certifier does not create Chronicle Entries merely by defining a schema field.

## Relationship to Anchor

Anchor owns Integrity References.

Hashes, timestamps, or integrity fields inside Certifier records may support Anchor operations, but they are not themselves an Anchor Integrity Reference unless Anchor establishes one.

## Relationship to Beacon

Beacon owns Discovery Signals / Discovery Metadata.

Certifier schema may expose metadata useful for discovery, but Certifier does not own Beacon discovery objects.

## Relationship to Attestor

Attestor is operational and institutionally distinct from Certifier.

The current Attestor architecture is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Certifier schema may support governed interoperability with Attestor.

It should not treat legacy `SATR` terminology as the current Attestor object model.

A schema field or Certifier record is not automatically an Attestation or Trust Statement.

## Relationship to Navigator

Navigator defines and orchestrates workflows.

Certifier schema may support machine-readable workflow integration while preserving Certifier ownership of certification records.

## Versioning and Portability

Schemas should be versioned so historical certification records remain understandable as newer schema versions or validation rules are introduced.

Versioning should preserve:

- historical interpretability;
- object identity;
- representation compatibility;
- migration clarity; and
- provenance.

A schema revision should not silently redefine the meaning of previously issued certification records.

## Operations Toolkit

The Operations Toolkit may generate or validate repository-based artifact sets using Certifier schema.

The toolkit supports implementation.

It does not replace certification judgment or operate as an independent certification authority.

## Authority Discipline

This directory should preserve the following distinctions:

- Schema ≠ Certification Decision
- Certification Package Schema ≠ Certification Package instance
- SCRD HTML ≠ separate canonical object from SCRD JSON
- Evidence structure ≠ Evaluation
- Reference stub ≠ downstream canonical object
- Hash field ≠ Anchor Integrity Reference
- Discovery metadata field ≠ Beacon Discovery Signal
- Certifier record ≠ Attestation
- Certifier record ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Considerations

The following should be reviewed during Suite Reconciliation rather than redesigned in this README pass:

1. whether the phrase **Suite Reference Stubs** remains the preferred terminology;
2. how Certifier schema should distinguish references from downstream canonical object identifiers;
3. whether any schema fields should be formally governed by Suite Standards rather than Certifier alone; and
4. how versioning and validation rules should be coordinated across Suite institutions.

## Repository Expectations

Changes to this directory should preserve:

1. the Certification Package as Certifier's canonical operational record;
2. schema as representation structure rather than decision authority;
3. parity between SCRD HTML and SCRD JSON;
4. evidence/evaluation distinctions;
5. current Suite object terminology;
6. downstream institutional ownership;
7. schema versioning and historical portability; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Schema preserves the structure of certification records; it does not create certification authority or collapse downstream Suite objects into Certifier-owned records.**
