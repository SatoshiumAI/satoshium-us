# Satoshium Registry Record Types

## Overview

The `registry/record-types/` directory contains the public Record Types page and supporting documentation that define the controlled primary classifications applied to Satoshium Registry Entries, or SREGs.

The public page is published through:

```text
registry/record-types/index.html
```

This `README.md` serves as the directory-level documentation for that page.

Registry Record Types organize different kinds of authoritative source records within one shared SREG architecture.

They improve:

- classification;
- discoverability;
- schema consistency;
- relationship clarity;
- validation;
- interoperability;
- long-term maintenance.

---

## Purpose of This Directory

The purpose of this directory is to explain:

- what a Registry Record Type is;
- how Record Types relate to SREGs;
- which Record Types are currently recognized;
- how Record-Type Profiles extend the SREG Base Schema;
- how Record Types differ from Source Institution classifications;
- how new Record Types may be introduced;
- how Record Type changes are governed;
- how Record Type validation supports consistent publication.

---

## Constitutional Position

Registry Record Types operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Registry Rules
  ↓
Record Type Governance
  ↓
Record-Type Profile
  ↓
Published SREG
```

### Suite Standards

Define shared expectations across the Satoshium Suite.

### Registry Rules

Define foundational Registry requirements and institutional boundaries.

### Record Type Governance

Defines how Record Types are proposed, reviewed, approved, revised, deprecated, or retired.

### Record-Type Profile

Defines type-specific requirements applied to the SREG Base Schema.

### Published SREG

The final Registry Entry classified under one approved primary Record Type.

---

## Canonical Operational Hierarchy

Record Types operate within the canonical Registry architecture:

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

### Registry Record Type

The controlled primary classification assigned to the SREG.

### Authoritative Source Record

The record created and maintained by the originating institution.

Registry classifies the SREG.

The Source Institution retains authority over the Source Record.

---

## One Primary Record Type

Every operational SREG must receive one primary Registry Record Type.

Secondary classifications may be permitted by the applicable Record-Type Profile, but they must not conflict with the primary type.

```text
Primary Record Type
  = how Registry principally classifies the SREG

Relationships
  = how the SREG connects to other Registry and source objects
```

A SREG should not use multiple conflicting primary Record Types.

---

## Current Record Types

The initial controlled Registry Record Types are:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

These types reflect the current operational architecture of Satoshium Registry.

---

# Tool

Tool Records catalog systems, applications, services, frameworks, institutions, platforms, and operational components.

Examples may include:

- Atlas;
- Certifier;
- Registry;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- approved external tools.

A Tool SREG may preserve:

- tool name;
- Tool Class;
- Source Institution;
- operational role;
- source reference;
- status;
- versions;
- relationships;
- public documentation;
- repository or canonical page.

Tool Records do not transfer authority over the tool to Registry.

---

# Jurisdiction

Jurisdiction Records catalog authoritative jurisdiction resources.

Examples may include:

- countries;
- states;
- provinces;
- territories;
- regions;
- municipalities;
- other approved geographic or governmental classifications.

A Jurisdiction SREG may preserve:

- jurisdiction name;
- jurisdiction class;
- parent jurisdiction;
- country or subdivision code;
- Source Institution;
- source identifier;
- source reference;
- related Atlas resource;
- status;
- versions;
- relationships.

Atlas may serve as the Source Institution for canonical jurisdiction intelligence.

Registry catalogs the Atlas Source Record through the SREG.

---

# Media

Media Records catalog public or institutionally significant media resources.

Examples may include:

- videos;
- images;
- thumbnails;
- transcripts;
- audio resources;
- media pages;
- other approved media assets.

A Media SREG may preserve:

- title;
- media type;
- media classification;
- Source Institution;
- source identifier;
- canonical media location;
- visibility;
- source status;
- related jurisdiction;
- relationships;
- versions.

Registry does not necessarily host the media.

The Source Institution or rights holder retains authority over ownership, licensing, publication, and access.

---

# Certification

Certification Records catalog Certifier-owned certification artifacts.

Examples may include:

- Certification Packages;
- Certification Process Reports;
- Certification Receipts;
- SCRDs;
- certification records;
- related certification artifacts.

A Certification SREG may preserve:

- Certifier as Source Institution;
- Certification Identifier;
- source record;
- Certification Status;
- Certification Outcome;
- Registry Status;
- versions;
- public references;
- relationships.

Registry does not create the Certification Outcome.

Certifier remains authoritative for certification meaning and status.

---

# Attestation

Attestation Records catalog Attestor-owned trust statements and attestation artifacts.

Examples may include:

- attestations;
- trust statements;
- validation reports;
- verification references;
- supporting evidence relationships.

A SREG may catalog the Attestor Source Record without redefining the attestation conclusion.

Attestor remains authoritative for the trust statement.

Registry remains authoritative for the SREG.

---

# Signal

Signal Records catalog Beacon-owned discovery signals and discovery-oriented records.

Examples may include:

- discovery signals;
- announcements;
- visibility metadata;
- public signals;
- distribution references;
- other approved signaling artifacts.

Beacon remains authoritative for the discovery signal.

Registry preserves the catalog entry and its relationships.

---

## Additional and Future Record Types

Registry may introduce additional Record Types when a genuine operational need exists.

Potential future Record Types may include:

- Historical Event;
- Integrity Reference;
- Workflow Definition;
- Schema;
- Policy;
- Governance;
- Preservation;
- Reference;
- Evidence;
- Research;
- External Institutional Record.

A potential future category is not an approved Record Type until formally adopted through Registry governance.

---

## Record-Type Profiles

Each approved Record Type should have a corresponding Record-Type Profile.

A Record-Type Profile extends the common SREG structure by defining type-specific requirements.

A profile may define:

- required fields;
- optional fields;
- controlled classifications;
- required relationships;
- permitted relationships;
- identifier expectations;
- Registry Status values;
- lifecycle requirements;
- source-reference requirements;
- public-reference requirements;
- validation rules;
- publication requirements.

The profile must remain compatible with the SREG Base Schema.

---

## Schema Architecture

Record Types operate through the Registry schema hierarchy:

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

Defines Registry-wide structural and validation requirements.

### SREG Base Schema

Defines fields and behaviors shared by all SREGs.

### Record-Type Profile

Adds the requirements specific to one approved Record Type.

### Published SREG

The human-readable and machine-readable Registry Entry validated under the applicable schema and profile.

Record Types should not create unrelated Registry record architectures.

They should extend the shared SREG model.

---

## Classification Authority

Registry is authoritative for assigning the Registry Record Type to the SREG.

The Source Institution remains authoritative for:

- the Source Record's own classification;
- source meaning;
- source status;
- source version;
- source content.

```text
Registry classification
  = how Registry catalogs the source

Source classification
  = how the Source Institution describes its own record
```

These classifications may relate, but they are not interchangeable.

---

## Record Type and Source Institution

Record Type and Source Institution are separate fields.

The same Source Institution may produce records that belong to different Registry Record Types.

Example:

```text
Atlas
├── Tool SREG for Atlas as an institution
├── Jurisdiction SREG for an Atlas jurisdiction record
└── Media SREG for an Atlas media resource
```

Likewise, multiple Source Institutions may produce records cataloged under the same Record Type.

---

## Record Type and Relationships

Record Type defines the primary classification of the SREG.

Relationships describe how the SREG connects to other objects.

Examples:

```text
Tool SREG
  → produces
  → Jurisdiction SREG
```

```text
Jurisdiction SREG
  → related to
  → Media SREG
```

```text
Certification SREG
  → references
  → Jurisdiction SREG
```

```text
Attestation SREG
  → attests to
  → Certification SREG
```

```text
Signal SREG
  → discovers
  → Media SREG
```

```text
SREG
  → anchored by
  → Integrity Reference
```

Relationships must use approved relationship types and preserve direction where applicable.

---

## Record Type Approval

A new Record Type should be approved only when:

- existing Record Types cannot accurately classify the source object;
- a distinct institutional object exists;
- the proposed type has clear scope and boundaries;
- a Record-Type Profile can be defined;
- schema validation can be supported;
- relationship behavior can be documented;
- interoperability consequences are understood;
- governance approval is recorded.

Record Type expansion should reflect architectural need rather than convenience.

---

## Record Type Changes

A Record Type change may be material because it can affect:

- schema validation;
- required fields;
- relationships;
- public discovery;
- lifecycle behavior;
- interoperability;
- public interpretation;
- profile assignment.

A Record Type change should follow the applicable Registry Record Update Policy or Registry Correction Policy.

A fundamental classification change may require supersession when the existing Registry identity can no longer accurately represent the object.

---

## Record Type Deprecation or Retirement

A Record Type may be deprecated or retired when:

- it duplicates another type;
- its scope is no longer coherent;
- its records migrate to a replacement type;
- schema support ends;
- institutional architecture changes;
- governance determines the type is no longer appropriate.

Deprecation or retirement should preserve:

- prior type definition;
- prior profile versions;
- affected SREGs;
- migration requirements;
- successor type;
- effective date;
- governance record;
- historical discoverability.

Existing SREGs should not be silently reclassified without policy-governed migration.

---

## Record Type Validation

Before publication, Registry should confirm:

- the primary Record Type is approved;
- the selected type accurately fits the Source Record;
- the applicable profile version is identified;
- required fields are present;
- required relationships are present;
- controlled values are valid;
- identifiers conform to applicable requirements;
- Registry and source classifications remain distinct;
- the SREG satisfies the applicable schema;
- human-readable and machine-readable forms agree.

---

## Publication Consistency

The Record Type must agree across:

- Registry HTML entry;
- SREG JSON record;
- catalog index;
- relationship index;
- version history;
- correction history;
- interoperability references;
- archival or supersession records.

A SREG is not fully reconciled when official forms identify conflicting primary Record Types.

---

## Directory Structure

The current directory structure is:

```text
registry/
└── record-types/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Record Types page.

### `README.md`

The directory-level documentation explaining Record Type purpose, authority, current classifications, profile architecture, governance, validation, and relationship to the SREG model.

Future supporting files may include:

```text
record-types/
├── index.html
├── README.md
├── profiles/
├── governance/
├── examples/
└── schemas/
```

These directories should be introduced only when the corresponding materials exist.

---

## Relationship to Other Registry Documentation

The Record Types page should remain consistent with:

- Registry Purpose;
- Registry Entry Model;
- Registry Records;
- Registry Rules;
- Registry Schemas;
- Registry Corrections;
- Registry Integration;
- Registry Lifecycle;
- Registry Status;
- Registry Policies;
- Registry Procedures;
- Registry Definitions;
- Registry Scope;
- Registry Changelog.

The Entry Model defines the SREG.

The Record Types page defines how SREGs are primarily classified.

The Schemas page defines how those classifications are structurally implemented.

---

## Maintenance Requirements

When Record Types change:

- update the public `index.html`;
- update this README;
- update applicable Record-Type Profiles;
- update schema enumerations;
- update validation logic;
- update examples;
- update related policies and procedures;
- document material changes in the Registry Changelog;
- preserve prior type and profile versions;
- review affected SREGs;
- reconcile human-readable and machine-readable publication.

---

## Guiding Principles

- Every operational SREG has one primary Record Type.
- Record Type classifies the SREG.
- Record Type does not redefine the Source Record.
- Registry controls Registry classification.
- Source Institutions retain source authority.
- Record Types extend one shared SREG architecture.
- Every approved type should have a Record-Type Profile.
- Relationships connect objects without replacing classification.
- Material type changes require documented governance.
- Future Record Types require approval before operational use.
- Human-readable and machine-readable forms must agree.

---

## Disclaimer

Registry Record Types classify SREGs within Satoshium Registry.

They do not by themselves create:

- Source Institution authority;
- certification;
- attestation;
- ownership;
- legal rights;
- regulatory recognition;
- endorsement;
- verification;
- affiliation.

Those forms of authority remain with the applicable Source Institution, Source Record, rights holder, governing authority, or responsible external system.

---

## Guiding Statement

> Information may take many forms.
>
> Record Types preserve those distinctions.
>
> The SREG provides the shared structure.
>
> Source Institutions retain authority.
