# Registry Tool Records

## Overview

This document defines how Tool Records are represented within Satoshium Registry.

A Tool Record is a Satoshium Registry Entry, or SREG, that catalogs an Authoritative Source Record describing an application, service, framework, system, platform, institution, utility, protocol, or other approved operational component.

Registry catalogs the tool.

Registry does not perform the operational functions of the tool.

---

## Constitutional Position

Tool Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Source Institution Tool Implementation
  ↓
Authoritative Tool Record
  ↓
Registry Tool SREG
```

The Source Institution creates and maintains the Authoritative Tool Record.

Registry creates and maintains the SREG that identifies, classifies, references, relates, versions, and preserves discoverability of that Source Record.

---

## Canonical Relationship

The canonical relationship is:

```text
Source Institution
  ↓
Authoritative Tool Record
  ↓
Registry Tool SREG
```

This relationship preserves institutional separation:

- the Source Institution owns the tool and its authoritative documentation;
- Registry owns the SREG;
- the SREG points back to the Authoritative Source Record;
- Registry does not absorb operational authority.

---

## Purpose

Tool Records exist to improve:

- discoverability;
- source attribution;
- tool classification;
- dependency mapping;
- interoperability;
- relationship mapping;
- version awareness;
- lifecycle visibility;
- public reference management;
- historical continuity.

A Registry Tool SREG should help answer:

- What tool exists?
- Which institution owns or maintains it?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the tool?
- What Tool Class applies?
- What is the tool's institutional purpose?
- What records does it produce?
- What systems does it depend on?
- What other Suite institutions does it interact with?
- What is the Source-Record Status?
- What is the Registry Status?
- Which versions apply?
- Where can the authoritative documentation be found?

---

## Record Type

The primary Registry Record Type is:

```text
Tool
```

Every operational Tool SREG must use the approved Tool Record-Type Profile.

The profile may define:

- required fields;
- optional fields;
- controlled Tool Classes;
- ownership and maintenance fields;
- required relationships;
- permitted relationships;
- dependency fields;
- interoperability fields;
- source-reference requirements;
- status requirements;
- lifecycle requirements;
- validation rules;
- publication requirements.

---

## Source Institutions

A Tool Record may originate from:

- Atlas;
- Certifier;
- Registry;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- another approved Satoshium Suite institution;
- an approved external institution or developer.

The Source Institution must remain distinct from Registry, even when the tool being cataloged is Registry itself.

---

## Authoritative Source Record

Every Tool SREG must identify the Authoritative Source Record being cataloged.

The Source Record may include:

- institutional landing page;
- tool specification;
- repository;
- canonical documentation;
- operational manual;
- schema package;
- public release record;
- governance record;
- architecture document;
- another approved tool artifact.

The SREG should preserve a durable canonical source reference whenever available.

---

## Registry Identifier and Source-System Identifier

A Tool SREG must preserve distinct identifiers.

### Registry Identifier

Assigned by Satoshium Registry.

Identifies the SREG.

### Source-System Identifier

Assigned by the Source Institution.

Identifies the Authoritative Tool Record or operational tool object.

Example:

```text
Registry Identifier: SREG-TOOL-0001
Source-System Identifier: SATOSHIUM-ATLAS
```

The Registry Identifier must not replace, alter, or overwrite the Source-System Identifier.

When the tool has no source identifier, the absence should be documented rather than replaced with an invented source identifier.

---

## Tool Classes

Controlled Tool Classes may include:

### Intelligence System

Creates or maintains structured intelligence resources.

Example:

```text
Atlas
```

### Certification System

Performs standards-based certification and creates certification artifacts.

Example:

```text
Certifier
```

### Registry System

Creates and maintains structured public Registry Entries.

Example:

```text
Registry
```

### Historical System

Creates and preserves historical events, milestones, and institutional chronology.

Example:

```text
Chronicle
```

### Integrity System

Creates or preserves integrity references, hashes, timestamps, signatures, or related preservation artifacts.

Example:

```text
Anchor
```

### Discovery System

Creates discovery signals and visibility-oriented metadata.

Example:

```text
Beacon
```

### Attestation System

Creates trust statements, attestations, validation records, and verification references.

Example:

```text
Attestor
```

### Workflow System

Creates workflow definitions and coordinates cross-system operational activity.

Example:

```text
Navigator
```

### Utility

Provides supporting operational functionality.

### Governance System

Supports institutional governance, policy, rule, or standards administration.

### Research Tool

Supports research, evidence review, analysis, or structured inquiry.

### Preservation System

Supports archival preservation, continuity, or long-term record retention.

### External Tool

Catalogs an approved non-Satoshium operational system.

Additional Tool Classes require approval through Registry governance.

---

## Current Suite Tool Records

Registry should support Tool SREGs for the principal Suite institutions.

### Atlas

Creates jurisdiction intelligence, canonical jurisdiction records, evidence resources, machine-readable packages, and generation manifests.

### Certifier

Creates Certification Packages, Certification Process Reports, Certification Receipts, SCRDs, and related certification artifacts.

### Registry

Creates SREGs and maintains the Suite's public catalog layer.

### Chronicle

Creates and preserves historical events and institutional chronology.

### Anchor

Creates and preserves integrity references, hashes, timestamps, signatures, and durable verification points.

### Beacon

Creates discovery signals and visibility-oriented metadata.

### Attestor

Creates trust statements, attestations, validations, and supporting verification references.

### Navigator

Creates workflow definitions and coordinates cross-system operational activity.

Each Tool SREG must preserve the distinction between:

- the institution;
- the operational tool;
- the Source Record describing it;
- the Registry Entry cataloging it.

---

## Required SREG Elements

An operational Tool SREG should include:

### Identity

- Registry Identifier;
- title;
- Registry Record Type;
- Tool Class.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier, when available;
- canonical source reference.

### Tool Context

- tool name;
- institutional purpose;
- operational function;
- owner or maintainer;
- implementation status;
- public repository or documentation;
- Source-Record Status.

### Registry Context

- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG schema version;
- Tool Record-Type Profile version;
- registration date;
- last updated date.

### Relationships

- produces;
- produced by;
- depends on;
- integrates with;
- governed by;
- references;
- certified by;
- attested by;
- anchored by;
- documented by;
- coordinated through;
- supersedes;
- superseded by.

---

## Example Record Structure

```text
Registry Identifier
Title
Registry Record Type
Tool Class
Source Institution
Source-System Identifier
Authoritative Source Record
Tool Name
Institutional Purpose
Operational Function
Owner or Maintainer
Implementation Status
Canonical Source Reference
Repository Reference
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
Schema Version
Profile Version
Public References
Relationships
Dependencies
Registration Date
Last Updated
```

The authoritative field definitions belong to the Registry Schema Specification and Tool Record-Type Profile.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-TOOL-0001 |
| Registry Record Type | Tool |
| Tool Class | Intelligence System |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | SATOSHIUM-ATLAS |
| Tool Name | Atlas |
| Implementation Status | Active |
| Source-Record Status | Active |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |

This example is illustrative and does not establish final production identifiers or controlled values.

---

## Authority Boundary

### Source Institution Authority

The Source Institution remains authoritative for:

- tool name;
- tool purpose;
- operational function;
- Source-System Identifier;
- source version;
- Source-Record Status;
- implementation status;
- repository;
- documentation;
- releases;
- deprecation;
- ownership;
- maintenance;
- licensing.

### Registry Authority

Registry remains authoritative for:

- Registry Identifier;
- Registry Record Type;
- Registry classification;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry publication;
- Registry correction history;
- Registry archival history.

Registry may report source-controlled tool values.

Registry does not operate, certify, own, or maintain the tool merely by registering it.

---

## Related Registry Records

A Tool SREG may relate to:

- Jurisdiction SREGs;
- Media SREGs;
- Certification SREGs;
- Attestation SREGs;
- Signal SREGs;
- Historical Event SREGs;
- Integrity Reference SREGs;
- Workflow records;
- other Tool SREGs.

Examples:

```text
Atlas Tool SREG
  → produces
  → Jurisdiction SREG
```

```text
Certifier Tool SREG
  → produces
  → Certification SREG
```

```text
Beacon Tool SREG
  → produces
  → Signal SREG
```

```text
Attestor Tool SREG
  → produces
  → Attestation SREG
```

```text
Navigator Tool SREG
  → coordinates
  → Workflow Record
```

```text
Tool SREG
  → integrates with
  → Tool SREG
```

Relationships must use approved types and preserve direction where applicable.

---

## Tool Dependencies

A Tool SREG may preserve dependencies such as:

- institutional dependency;
- schema dependency;
- data dependency;
- workflow dependency;
- service dependency;
- repository dependency;
- external platform dependency;
- version dependency.

Dependency records should identify:

- dependency type;
- dependency target;
- required version, when applicable;
- whether the dependency is mandatory or optional;
- source attribution;
- effective date;
- replacement or retirement information.

Registry records the dependency.

Registry does not create the dependency.

---

## Tool Record Workflow

Registry should create a Tool SREG through the following process:

```text
Tool Source Record Identified
  ↓
Source Institution Confirmed
  ↓
Source Authority Confirmed
  ↓
Registrability Determined
  ↓
Tool Record Type Assigned
  ↓
Tool Class Assigned
  ↓
Registry Identifier Assigned
  ↓
Source-System Identifier Preserved
  ↓
References, Dependencies, and Relationships Established
  ↓
SREG Constructed
  ↓
Schema and Profile Validated
  ↓
Human-Readable and Machine-Readable Forms Reconciled
  ↓
Published
  ↓
Lifecycle, Versions, Updates, Corrections, and History Maintained
```

---

## Lifecycle

A Tool SREG may move through approved Registry Lifecycle States such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states describe the SREG.

They do not replace the operational lifecycle or status of the tool itself.

Example:

```text
Source-Record Status: Deprecated
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for a deprecated or discontinued tool.

---

## Updates

A Tool SREG may be updated when:

- the Source Institution publishes a new version;
- the canonical documentation changes;
- the repository changes;
- operational status changes;
- dependencies change;
- integrations change;
- public references expand;
- relationships evolve;
- Registry metadata improves;
- schema migration occurs;
- the Tool Record-Type Profile changes.

Updates must preserve the distinction between source-controlled and Registry-controlled changes.

---

## Corrections

A Registry correction may be required when Registry incorrectly records:

- Source Institution;
- Source-System Identifier;
- tool name;
- Tool Class;
- canonical source reference;
- repository reference;
- implementation status;
- dependency;
- Registry Status;
- relationship target;
- version metadata;
- publication data.

Registry may correct its representation of source-controlled values.

Registry may not alter the tool or its authoritative documentation through a Registry correction.

---

## Tool Renaming

A tool may be renamed while retaining the same institutional identity.

A rename may be handled through:

- title update;
- alternate-name addition;
- source-version update;
- canonical source-reference update;
- relationship update.

When the renamed tool is materially a distinct successor system, supersession may be required.

Prior names should remain discoverable when historically significant.

---

## Replacement and Supersession

A Tool SREG may be superseded when:

- a distinct successor tool replaces it;
- a new Registry Identifier is required;
- the source system changes identity materially;
- the original tool is replaced by a new institutional object;
- governance requires a replacement SREG.

The prior SREG should remain discoverable and reference its successor.

---

## Deprecation and Retirement

A source tool may become:

- deprecated;
- retired;
- unsupported;
- discontinued;
- replaced;
- archived.

Registry should preserve:

- final source version;
- final Source-Record Status;
- effective date;
- successor tool;
- migration reference;
- historical relationships;
- archival references;
- related Chronicle events.

Source retirement does not automatically require deletion or retirement of the SREG.

---

## Revocation

Registry may revoke a Tool SREG when:

- registration was invalid;
- the Source Institution was materially misidentified;
- the Source Record did not support the represented tool;
- the SREG materially misrepresented the source;
- governance requires withdrawal from active recognition.

Registry revocation does not deactivate or revoke the tool itself.

---

## Archival

A Tool SREG may be archived while preserving:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- tool name;
- Tool Class;
- source references;
- repository references;
- versions;
- dependencies;
- relationships;
- corrections;
- supersession history;
- revocation history;
- archival date and reason.

Archived does not mean deleted.

---

## Interoperability

Tool Records are central to Suite interoperability.

A Tool SREG may preserve:

- canonical integration page;
- supported source record types;
- produced artifact types;
- consumed artifact types;
- identifier exchanges;
- schema dependencies;
- workflow relationships;
- status synchronization rules;
- version compatibility;
- authority boundaries.

Interoperability documentation should explain how tools connect without collapsing institutional responsibility.

---

## Validation Requirements

Before publication, Registry should confirm:

- Source Institution is identified;
- Authoritative Tool Record exists or is historically documented;
- Registry Identifier is valid;
- Source-System Identifier is preserved when available;
- Tool Record Type is approved;
- Tool Class is valid;
- tool name is identified;
- institutional purpose is documented;
- canonical source reference is present where available;
- owner or maintainer is identified where known;
- dependencies and relationships are valid;
- Registry Status and Source-Record Status remain separate;
- version metadata is complete;
- the SREG Base Schema validates;
- the Tool Record-Type Profile validates;
- human-readable and machine-readable forms agree.

Registry validation does not constitute operational testing, certification, or endorsement of the tool.

---

## Human-Readable Publication

The human-readable Tool SREG should communicate:

- Registry Identifier;
- title;
- Tool Class;
- Source Institution;
- Source-System Identifier;
- institutional purpose;
- operational function;
- owner or maintainer;
- implementation status;
- canonical source reference;
- repository or documentation reference;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- dependencies;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication

The machine-readable Tool SREG should preserve equivalent institutional meaning.

It may include:

- identifiers;
- controlled Tool Classes;
- source references;
- status values;
- lifecycle values;
- version metadata;
- typed relationships;
- dependencies;
- interoperability references;
- repository references;
- dates;
- schema version;
- profile version;
- validation metadata.

---

## Publication Consistency

Official forms of the same Tool SREG must agree on:

- Registry Identifier;
- title;
- Record Type;
- Tool Class;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- tool name;
- implementation status;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- dependencies;
- references;
- relationships;
- dates.

A record is not fully reconciled when official forms materially disagree.

---

## Future Development

Tool Records may expand to support:

- richer Tool Class taxonomies;
- dependency graphs;
- service maps;
- version compatibility matrices;
- release histories;
- deprecation notices;
- migration paths;
- security references;
- operational health references;
- schema compatibility;
- automated interoperability discovery;
- external tool integration;
- AI agent records;
- network service records;
- governance system records;
- preservation system records.

Future development must preserve the established authority boundary:

```text
The Source Institution operates the tool.
Registry creates the SREG.
```

---

## Registry Notes

Registry records and organizes information about tools.

Registry does not independently:

- operate the tool;
- maintain the tool;
- test the tool;
- certify the tool;
- attest to the tool;
- guarantee uptime;
- guarantee security;
- guarantee accuracy;
- create ownership or legal rights;
- grant licensing;
- guarantee continued source availability.

Registration means the tool record has been cataloged.

It does not mean Registry endorses or independently validates the tool.

---

## Relationship to Other Registry Documentation

This document should remain consistent with:

- Registry Records;
- Registry Record Types;
- Registry Entry Model;
- Registry Schemas;
- Registry Lifecycle;
- Registry Status;
- Registry Integration;
- Registry Corrections;
- Registry Policies;
- Registry Procedures;
- Registry Definitions;
- applicable Source Institution documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When the Tool Record architecture changes:

- update this document;
- update the Tool Record-Type Profile;
- update schema enumerations;
- update validation rules;
- update examples;
- update integration documentation;
- review affected SREGs;
- reconcile human-readable and machine-readable publication;
- preserve prior versions;
- document material changes in the Registry Changelog.

---

## Guiding Principles

- The Source Institution operates the tool.
- Registry creates the Tool SREG.
- The SREG is not the tool itself.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and source lifecycle remain distinct.
- Tool Class and Source Institution remain separate.
- Dependencies and relationships should be typed and attributable.
- Versions should remain independently traceable.
- Human-readable and machine-readable forms should agree.
- Deprecated or superseded tools should remain historically discoverable where appropriate.
- Registration does not itself establish functionality, security, certification, or endorsement.

---

## Disclaimer

A Tool SREG is a Registry-owned catalog record.

It does not by itself create:

- functionality;
- availability;
- security;
- certification;
- attestation;
- verification;
- endorsement;
- ownership;
- licensing;
- legal rights;
- regulatory approval;
- affiliation;
- Source Institution authority.

Those remain controlled by the Source Institution, tool operator, developer, maintainer, rights holder, Source Record, or applicable external authority.

---

## Guiding Statement

> Tools perform work.
>
> Source Institutions operate the tools.
>
> Registry creates the SREG.
>
> The SREG preserves identity, purpose, dependencies, relationships, versions, and the path back to the source.
