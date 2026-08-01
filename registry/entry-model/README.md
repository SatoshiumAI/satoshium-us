# Satoshium Registry Entry Model

**Canonical operational model for the Satoshium Registry Entry (SREG)**

This directory contains the public documentation and supporting materials for the Satoshium Registry Entry Model.

The Entry Model defines the **Satoshium Registry Entry**, or **SREG**, as the canonical operational object of Satoshium Registry.

A SREG identifies, classifies, references, connects, versions, and preserves the discoverability of an Authoritative Source Record without transferring authority away from the institution that created it.

---

## Purpose

The purpose of the Entry Model is to establish a single canonical Registry object that can be applied consistently across all supported Registry Record Types.

The Entry Model answers the question:

> How should Registry catalog an authoritative record while preserving institutional ownership, source authority, interoperability, version history, and long-term discoverability?

The answer is the SREG.

---

## Constitutional Position

The SREG implements the Satoshium Suite constitutional hierarchy at the Registry institutional layer:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Institutional Implementation
  ↓
Satoshium Registry Entry (SREG)
```

### Suite Standards

Define shared expectations for terminology, schemas, versions, governance, evidence references, trust references, interoperability, and public accountability.

### Suite Methodology

Defines repeatable, reviewable, documented, and maintainable implementation principles.

### Suite Interoperability

Defines how Registry exchanges identifiers, references, relationships, and metadata with other Suite institutions without merging institutional responsibilities.

### Registry Institutional Implementation

Applies those Suite-wide foundations through Registry Rules, Policies, Procedures, schemas, Record Types, lifecycle controls, versions, corrections, relationships, and public publication.

---

## Canonical Operational Hierarchy

Registry is organized through four distinct layers:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

### Satoshium Registry

The institution responsible for the public catalog and Registry operations.

### Registry Entry (SREG)

The canonical Registry operational object.

A SREG is an independently maintained Registry record that identifies, classifies, references, and connects an Authoritative Source Record.

### Registry Record Type

The controlled primary classification assigned to the SREG.

The Record Type governs organization, validation, discoverability, profile application, and relationship behavior.

### Authoritative Source Record

The record created and maintained by the originating institution.

Registry catalogs the Authoritative Source Record.

Registry does not replace it.

---

## What a SREG Is

A SREG is:

- a Registry-owned operational object;
- a stable public catalog entry;
- a structured reference to an authoritative record;
- a version-aware Registry record;
- a relationship-bearing object;
- a human-readable and machine-readable publication;
- a durable path back to source authority.

A SREG is not:

- the Authoritative Source Record;
- a substitute certification;
- an attestation;
- a historical event;
- an integrity anchor;
- a discovery signal;
- a workflow definition;
- a transfer of ownership or authority.

---

## Registry Authority

Registry is authoritative for the SREG and its Registry-owned information, including:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry correction history;
- Registry publication history;
- Registry catalog presentation.

Registry authority applies to the Registry Entry.

It does not extend to the underlying Source Record.

---

## Source Authority

The Source Institution remains authoritative for:

- source-record content;
- Source-System Identifier;
- source-record version;
- source-record status;
- certification outcomes;
- attestation conclusions;
- historical event content;
- integrity references;
- discovery signals;
- jurisdiction intelligence;
- workflow definitions.

Registry may report or reference those source-controlled values.

Registry does not redefine them.

---

## Source Institutions

A SREG may catalog records created by:

- Atlas;
- Certifier;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- another approved Satoshium Suite institution;
- an approved external source.

The Entry Model preserves the distinction between Registry authority and Source Institution authority.

---

## Certification Relationship

The first operational Certifier-to-Registry path is:

```text
Atlas Resource
  ↓
Certifier Evaluation
  ↓
Certification Package
  ↓
SCRD
  ↓
SREG
```

The Certification Package remains Certifier's canonical certification object.

The SCRD remains a Certifier-owned certified record.

The SREG remains Registry's canonical catalog object.

This certification path is one interoperability pattern. It does not limit Registry to certifications.

---

## Other Source-Record Relationships

Registry may also catalog:

- Atlas canonical jurisdiction records;
- Chronicle historical events;
- Anchor integrity references;
- Beacon discovery signals;
- Attestor trust statements;
- Navigator workflow definitions;
- tools;
- media;
- schemas;
- policies;
- public institutional artifacts;
- other approved source records.

Each originating institution retains authority over its own canonical object.

---

## Registry References Rather Than Replaces

A SREG may reference:

- an Authoritative Source Record;
- a Certification Package;
- an SCRD;
- a repository;
- a public page;
- an integrity reference;
- an attestation;
- a historical event;
- a discovery signal;
- a workflow definition;
- another SREG.

Registry preserves the structured path back to authority.

It does not:

- duplicate every source;
- absorb source ownership;
- silently copy source authority;
- create a substitute source record;
- merge institutional responsibilities.

---

## Core SREG Components

### Registry Identifier

Every SREG receives a stable and unique Registry Identifier.

The Registry Identifier identifies the SREG itself.

It does not replace the Source-System Identifier.

### Registry Record Type

Every SREG receives a controlled primary classification.

Initial Record Types may include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

### Source Institution

Every SREG identifies the institution that created and maintains the Authoritative Source Record.

### Source-System Identifier

Every SREG preserves the source identifier when one exists.

The Source-System Identifier remains distinct from the Registry Identifier.

### Authoritative Source Record

Every SREG identifies and references the source record being cataloged.

### Registry Status

Every SREG preserves its condition within Registry.

Registry Status remains separate from Source-Record Status.

### Source-Record Status

Every SREG may report or reference the source-controlled status of the Authoritative Source Record.

### Versions

Every SREG preserves applicable:

- Registry Entry Version;
- SREG schema version;
- Record-Type Profile version;
- Registry specification version;
- Source-Record version.

### Relationships

Every SREG may preserve typed relationships to:

- other SREGs;
- Source Records;
- institutions;
- schemas;
- certifications;
- attestations;
- events;
- integrity references;
- discovery signals;
- workflows.

### Public References

Every SREG should preserve approved public locations and durable references, including:

- canonical URLs;
- repository paths;
- machine-readable records;
- public entry pages;
- persistent identifiers;
- approved API locations.

### Lifecycle History

Every SREG should preserve applicable:

- registration;
- update;
- correction;
- supersession;
- revocation;
- archival history.

---

## Conceptual SREG Fields

The Registry Schema Specification defines the authoritative field names, data types, constraints, and validation rules.

The Entry Model establishes the conceptual information that a complete SREG must support:

```text
Registry Identifier
Registry Record Type
Title
Source Institution
Source-System Identifier
Authoritative Source Record
Source-Record Version
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Schema Version
Public References
Relationships
Registration Date
Last Updated
Correction History
Supersession Information
Revocation Information
Archival Information
```

---

## Schema Architecture

SREGs are implemented through the following schema hierarchy:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Record-Type Profile
  ↓
Published SREG
```

### Registry Schema Specification

Defines Registry-wide requirements for identifiers, terminology, structure, validation, versions, relationships, lifecycle values, and compatibility.

### SREG Base Schema

Defines the common structure required for all SREGs.

### Record-Type Profile

Adds type-specific fields and validation requirements.

A Record-Type Profile extends the SREG Base Schema.

It does not create an unrelated record model.

### Published SREG

A human-readable or machine-readable Registry Entry validated under the applicable schema and profile.

---

## Registry Status and Source Status

The condition of the SREG and the condition of the Source Record must remain separate.

Example:

```text
Certification Outcome: Certified
Certification Status: Revoked
Registry Status: Active
```

In this example:

- the certification has been revoked by Certifier;
- the SREG remains active as a historical public catalog entry;
- Registry accurately reports the source condition;
- Registry preserves the record's discoverability and history.

---

## Version Model

Registry distinguishes among:

- Suite Standards version;
- Suite Methodology version;
- Registry specification version;
- SREG schema version;
- Record-Type Profile version;
- Registry Entry Version;
- Source-Record version.

These version layers are not interchangeable.

A Source Record may change without the SREG schema changing.

A SREG may be corrected without the Source Record changing.

A schema may evolve while older SREGs remain preserved under earlier schema versions.

---

## Correction Model

A SREG may change because:

- Registry-owned metadata changes;
- a reference is corrected;
- a relationship is added or changed;
- the Source Record changes;
- the Source-Record Status changes;
- the applicable schema evolves;
- the Record Type changes;
- a publication inconsistency is corrected.

Material changes should preserve:

```text
Prior SREG Version
  ↓
Documented Change
  ↓
Replacement SREG Version
```

Correction history should identify:

- what changed;
- why it changed;
- when it changed;
- which version was affected;
- which version replaced it;
- whether the Source Record changed;
- whether the change affected lifecycle or status.

---

## Lifecycle Model

A SREG may move through Registry lifecycle states such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states are not necessarily a single mandatory linear sequence.

The Entry Model supports lifecycle history while the Registry Lifecycle documentation defines permitted transitions and institutional conditions.

---

## Human-Readable Publication

A human-readable SREG may be published as:

- a Registry Entry HTML page;
- a public catalog listing;
- a relationship summary;
- a version-history page;
- a correction-history page;
- an archival page.

The human-readable publication should remain understandable without requiring access to the machine-readable record.

---

## Machine-Readable Publication

A machine-readable SREG may be published as:

- JSON;
- an API response;
- a structured manifest;
- another approved machine-readable format.

Machine-readable publication should preserve:

- the Registry Identifier;
- source identifiers;
- Record Type;
- Registry Status;
- Source-Record Status;
- versions;
- references;
- relationships;
- lifecycle history;
- schema version.

---

## Publication Consistency

Human-readable and machine-readable forms of the same SREG must agree on:

- identity;
- classification;
- Source Institution;
- Source Record;
- Registry Status;
- Source-Record Status;
- versions;
- relationships;
- public references;
- lifecycle history.

A SREG is not fully published when official forms materially disagree.

---

## Long-Term Discoverability

The Entry Model is designed to preserve discoverability even when:

- public pages move;
- repositories change;
- schemas evolve;
- Source Records change;
- institutions mature;
- new Suite systems are introduced;
- older versions are superseded;
- records are revoked or archived.

The SREG preserves the identity, provenance, references, relationships, versions, and historical context necessary to find and understand the Source Record later.

---

## Directory Role

This directory is intended to contain the public Entry Model page and related implementation materials.

A possible structure is:

```text
entry-model/
├── index.html
├── README.md
├── specification.md
├── schema/
│   ├── sreg.schema.json
│   └── record-types/
├── examples/
├── records/
└── assets/
```

The exact structure may evolve through documented Registry governance.

The distinction among public explanation, specification, schema, examples, records, and assets should remain clear.

---

## Related Registry Documentation

The Entry Model should remain consistent with:

- Registry Purpose;
- Registry Records;
- Registry Record Types;
- Registry Rules;
- Registry Schemas;
- Registry Corrections;
- Registry Integration;
- Registry Lifecycle;
- Registry Status;
- Registry Definitions;
- Registry Scope;
- Registry Policies;
- Registry Procedures;
- Registry Changelog.

---

## Guiding Principles

- SREG is Registry's canonical operational object.
- Every SREG references an Authoritative Source Record.
- Registry authority applies to the SREG.
- Source authority remains with the Source Institution.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Record Types are controlled classifications.
- Versions must remain independently traceable.
- Relationships should be typed and attributable.
- Human-readable and machine-readable forms should remain consistent.
- Corrections should preserve prior versions.
- Lifecycle history should remain discoverable.
- Registry should preserve the path back to authority.

---

## Disclaimer

The Entry Model defines the structure and institutional role of the SREG.

A SREG does not by itself create:

- ownership;
- legal rights;
- certification;
- attestation;
- verification;
- regulatory approval;
- source authority;
- historical truth;
- endorsement;
- affiliation.

Those forms of authority remain with the applicable Source Institution, Source Record, rights holder, governing authority, or responsible external system.

---

## Guiding Statement

> The source holds authority.
>
> The SREG preserves identity, classification, relationships, versions, and discovery.
>
> Registry preserves the path back to the source.
