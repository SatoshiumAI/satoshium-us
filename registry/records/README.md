# Satoshium Registry Records

## Overview

The `registry/records/` directory contains the public Registry Records page and supporting documentation that explain how authoritative source records are represented through Satoshium Registry Entries, or SREGs.

The public page is published through:

```text
registry/records/index.html
```

This `README.md` serves as the directory-level documentation for that page.

Registry Records are not the Authoritative Source Records themselves.

A Registry Record is an operational SREG maintained by Satoshium Registry.

---

## Purpose of This Directory

The purpose of this directory is to explain:

- what a Registry Record is;
- how Registry Records relate to SREGs;
- how SREGs relate to Authoritative Source Records;
- which Record Types may be used;
- what information a Registry Record preserves;
- how Registry authority differs from Source Institution authority;
- how records are created, validated, published, updated, corrected, superseded, revoked, and archived;
- how human-readable and machine-readable forms remain consistent.

---

## Constitutional Position

Registry Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Institutional Implementation
  ↓
Published SREG
```

Registry applies Suite-wide expectations through:

- Registry Identifiers;
- Registry Record Types;
- source attribution;
- public references;
- relationships;
- Registry Status;
- Registry Lifecycle State;
- versions;
- corrections;
- publication;
- preservation.

---

## What Is a Registry Record?

A Registry Record is a Satoshium Registry Entry, or SREG.

```text
Registry Record = Satoshium Registry Entry (SREG)
```

A SREG is Registry's structured, public, version-aware representation of how an Authoritative Source Record can be:

- identified;
- classified;
- referenced;
- related;
- versioned;
- discovered;
- maintained;
- preserved.

The SREG does not replace the Authoritative Source Record.

---

## Canonical Operational Hierarchy

Registry Records operate within the canonical Registry architecture:

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

---

## Current Registry Record Types

The current controlled Registry Record Types are:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Each operational SREG should receive one primary Record Type.

Secondary classifications may be permitted by the applicable Record-Type Profile.

---

# Tool Records

Tool SREGs catalog systems, applications, services, frameworks, platforms, institutions, and operational components.

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
- source reference;
- operational role;
- status;
- versions;
- public documentation;
- relationships.

---

# Jurisdiction Records

Jurisdiction SREGs catalog authoritative jurisdiction resources.

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
- Source Institution;
- Source-System Identifier;
- canonical source reference;
- status;
- versions;
- relationships.

Atlas may serve as the Source Institution for canonical jurisdiction intelligence.

---

# Media Records

Media SREGs catalog public or institutionally significant media resources.

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
- Source-System Identifier;
- canonical media location;
- visibility;
- source status;
- related jurisdiction;
- relationships;
- versions.

Registry does not necessarily host the media.

---

# Certification Records

Certification SREGs catalog Certifier-owned certification artifacts.

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
- Source Record;
- Certification Status;
- Certification Outcome;
- Registry Status;
- versions;
- public references;
- relationships.

Registry does not create the Certification Outcome.

---

# Attestation Records

Attestation SREGs catalog Attestor-owned trust statements and attestation artifacts.

Examples may include:

- attestations;
- trust statements;
- validation reports;
- verification references;
- supporting evidence relationships.

Attestor remains authoritative for the trust statement.

Registry remains authoritative for the SREG.

---

# Signal Records

Signal SREGs catalog Beacon-owned discovery signals and discovery-oriented records.

Examples may include:

- discovery signals;
- announcements;
- visibility metadata;
- public signals;
- distribution references;
- other approved signaling artifacts.

Beacon remains authoritative for the signal.

Registry preserves the catalog entry and its relationships.

---

## What Registry Records Answer

Registry Records exist to answer questions such as:

- What Source Record exists?
- Which institution created it?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the Source Record?
- What Registry Record Type applies?
- Where can the source be found?
- What is the Registry Status?
- What is the Registry Lifecycle State?
- What is the Source-Record Status?
- Which versions apply?
- What relationships exist?
- What corrections or historical changes occurred?
- What prior states remain discoverable?

---

## Core Registry Record Components

### Registry Identifier

Identifies the SREG and remains distinct from the Source-System Identifier.

### Title

Provides the public human-readable name of the SREG.

### Registry Record Type

Assigns one approved primary classification to the SREG.

### Source Institution

Identifies the institution that created and maintains the Authoritative Source Record.

### Source-System Identifier

Identifies the Authoritative Source Record within the originating institution.

### Authoritative Source Record

Identifies the source object being cataloged.

### Registry Status

Preserves the current operational designation of the SREG.

### Registry Lifecycle State

Preserves the institutional condition of the SREG over time.

### Source-Record Status

Reports the condition of the Source Record as controlled by the Source Institution.

### Versions

Preserves Registry Entry, schema, profile, specification, and source versions.

### Public References

Preserves canonical source locations, repository paths, public pages, and machine-readable records.

### Relationships

Preserves typed links among SREGs, Source Records, institutions, certifications, events, attestations, integrity references, signals, and workflows.

### History

Preserves creation, update, correction, supersession, revocation, retirement, and archival history.

---

## Registry Authority

Registry is authoritative for:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry correction history;
- Registry publication;
- Registry catalog presentation.

Registry authority applies to the SREG.

---

## Source Institution Authority

The Source Institution remains authoritative for:

- Source Record content;
- Source-System Identifier;
- Source-Record version;
- Source-Record Status;
- institutional meaning;
- Certification Outcome;
- Certification Status;
- attestation conclusion;
- ownership;
- licensing;
- external legal or regulatory status.

Registry may report or reference source-controlled values.

Registry does not redefine them.

---

## Registry Record Method

Registry Records are created and maintained through the following method:

```text
Identify or Receive Source Record
  ↓
Confirm Source Institution and Authority
  ↓
Determine Registrability
  ↓
Assign Registry Record Type
  ↓
Assign Registry Identifier
  ↓
Establish References and Relationships
  ↓
Construct SREG
  ↓
Validate
  ↓
Publish
  ↓
Maintain Lifecycle, Versions, Corrections, and History
```

This method preserves a repeatable path from an authoritative source object to an operational Registry Record.

---

## Registrability

A Source Record may be registrable when:

- the Source Institution can be identified;
- the Authoritative Source Record can be identified;
- sufficient provenance exists;
- an approved Record Type applies;
- required references are available;
- required relationships can be established;
- the SREG can satisfy the applicable schema;
- no unresolved authority conflict exists.

Registrability does not imply:

- certification;
- attestation;
- endorsement;
- ownership;
- legal recognition;
- verification.

---

## Schema Architecture

Every operational Registry Record should follow the Registry schema hierarchy:

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

Defines the common structure shared by all Registry Records.

### Record-Type Profile

Adds type-specific requirements.

### Published SREG

The final human-readable and machine-readable Registry Record.

---

## Required Record Information

A complete operational SREG should support:

```text
Registry Identifier
Title
Registry Record Type
Source Institution
Source-System Identifier
Authoritative Source Record
Source-Record Version
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Schema Version
Record-Type Profile Version
Public References
Relationships
Registration Date
Last Updated
Correction History
Supersession Information
Revocation Information
Archival Information
```

The authoritative field names and constraints belong to the Registry Schema Specification.

---

## Human-Readable Publication

A Registry Record may be published through:

- Registry Entry HTML page;
- public catalog listing;
- relationship summary;
- version-history page;
- correction-history page;
- supersession notice;
- revocation notice;
- archival page.

The human-readable form should remain understandable without requiring access to machine-readable data.

---

## Machine-Readable Publication

A Registry Record may also be published through:

- SREG JSON;
- catalog indexes;
- relationship indexes;
- lifecycle event records;
- correction records;
- version manifests;
- API responses;
- archival records.

Machine-readable publication should preserve the same institutional meaning as the human-readable form.

---

## Publication Consistency

Official forms of the same SREG must agree on:

- Registry Identifier;
- title;
- Record Type;
- Source Institution;
- Source-System Identifier;
- Source Record;
- Registry Status;
- Registry Lifecycle State;
- Source-Record Status;
- versions;
- public references;
- relationships;
- registration date;
- last updated date.

A Registry Record is not fully reconciled when official forms materially disagree.

---

## Registry Record Lifecycle

Registry Records may move through approved lifecycle states such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states do not form one mandatory linear sequence.

Lifecycle describes the condition of the SREG.

It does not replace the lifecycle or status of the Source Record.

---

## Updates

A Registry Record may be updated because:

- Registry metadata improves;
- public references change;
- relationships evolve;
- the Source Record publishes a new version;
- Source-Record Status changes;
- schema migration occurs;
- the Record-Type Profile changes;
- interoperability requirements change.

Material updates should preserve prior SREG versions and create an Update Record where required.

---

## Corrections

A correction repairs Registry-owned information or Registry-controlled publication.

Examples include:

- incorrect Registry classification;
- broken Registry reference;
- incorrect Registry Status;
- incorrect relationship;
- publication mismatch;
- schema defect;
- source-reference transcription error.

Corrections must preserve source authority and prior material versions.

---

## Supersession

A Registry Record may be superseded when:

- a replacement SREG exists;
- a new Registry Identifier is required;
- a successor Source Record exists;
- the original classification is no longer suitable;
- architectural restructuring creates a distinct Registry object.

The prior SREG should remain discoverable and reference its successor.

---

## Revocation

Registry may revoke a SREG when:

- registration was invalid;
- source authority was materially misidentified;
- the SREG materially misrepresented the Source Record;
- a material defect cannot be corrected under the same Registry identity;
- governance requires withdrawal from active recognition.

Revocation preserves accountability.

It does not require deletion.

---

## Archival

An archived SREG remains preserved outside active operational use.

Archival should preserve:

- Registry identity;
- prior versions;
- source attribution;
- source references;
- relationships;
- correction history;
- supersession history;
- revocation history;
- archival date and reason.

Archived does not mean deleted.

---

## Validation Requirements

Before publication, Registry should confirm:

- Source Institution is identified;
- Authoritative Source Record exists or is historically documented;
- Registry Identifier is valid;
- Source-System Identifier is preserved when available;
- Record Type is approved;
- required metadata is complete;
- required references exist;
- required relationships are structurally valid;
- Registry Status and Source-Record Status remain separate;
- version metadata is complete;
- applicable schema validates;
- human-readable and machine-readable forms agree.

Registry validation does not independently certify or attest to the Source Record.

---

## Current Directory Structure

The current directory structure is:

```text
registry/
└── records/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Records page.

### `README.md`

The directory-level documentation explaining Registry Records, SREG architecture, authority boundaries, Record Types, schemas, lifecycle, versions, corrections, validation, publication, and preservation.

Future supporting files may include:

```text
records/
├── index.html
├── README.md
├── entries/
├── indexes/
├── relationships/
├── history/
└── examples/
```

These directories should be introduced only when the corresponding operational materials exist.

---

## Relationship to Other Registry Documentation

The Records page should remain consistent with:

- Registry Purpose;
- Registry Entry Model;
- Registry Record Types;
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

The Records page defines how operational SREGs are understood and maintained.

The Record Types page defines their primary classifications.

The Schemas page defines their structural implementation.

---

## Maintenance Requirements

When the Registry Records architecture changes:

- update the public `index.html`;
- update this README;
- update the SREG Base Schema;
- update affected Record-Type Profiles;
- update policies and procedures;
- update lifecycle and status documentation;
- update examples;
- reconcile human-readable and machine-readable publication;
- preserve prior versions;
- document material changes in the Registry Changelog.

---

## Guiding Principles

- A Registry Record is a SREG.
- The SREG is not the Source Record.
- Registry controls the SREG.
- Source Institutions retain source authority.
- Every SREG has one primary Record Type.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and Source Lifecycle remain distinct.
- Versions remain independently traceable.
- Relationships should be typed and attributable.
- Human-readable and machine-readable forms should agree.
- Prior states should remain discoverable.
- Registration does not create authority.

---

## Disclaimer

Registry Records are Registry-owned SREGs.

They do not by themselves create:

- certification;
- attestation;
- verification;
- ownership;
- legal rights;
- regulatory approval;
- endorsement;
- affiliation;
- Source Institution authority.

Those forms of authority remain with the applicable Source Institution, Source Record, rights holder, governing authority, or responsible external system.

---

## Guiding Statement

> Source records hold authority.
>
> Registry Records preserve identity, classification, relationships, versions, and discovery.
>
> The SREG preserves the structured path back to the source.
