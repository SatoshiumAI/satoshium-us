# Tool Record-Type Profile

## Overview

This document defines the Registry Record-Type Profile for Tool Satoshium Registry Entries, or Tool SREGs.

The profile extends the SREG Base Schema with the additional fields, controlled values, relationships, validation requirements, and publication rules needed to catalog authoritative tool records.

A Tool SREG may catalog an application, service, framework, system, platform, utility, protocol, institutional implementation, or another approved operational component.

Registry catalogs the tool record.

Registry does not operate, maintain, test, certify, secure, or guarantee the tool merely by registering it.

---

## Constitutional Position

The Tool Record-Type Profile operates within the following schema hierarchy:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Tool Record-Type Profile
  ↓
Published Tool SREG
```

This profile must remain consistent with:

- Suite Standards;
- Suite Methodology;
- Suite Interoperability;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Entry Model;
- Registry Record Types;
- Registry Tool Records documentation.

---

## Canonical Relationship

The canonical tool relationship is:

```text
Source Institution
  ↓
Authoritative Tool Record
  ↓
Tool SREG
```

The Source Institution owns or controls the tool and its authoritative documentation.

Registry owns the SREG.

The SREG must preserve the path back to the source.

---

## Profile Purpose

A valid Tool SREG should answer:

- What tool is being referenced?
- Which institution owns or maintains it?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the tool or Source Record?
- What Tool Class applies?
- What is the tool's institutional purpose?
- What operational function does it perform?
- What records or artifacts does it produce?
- What inputs, dependencies, integrations, or workflows does it use?
- What is the Source-Record Status?
- What is the Registry Status?
- What Registry Lifecycle State applies?
- Which versions apply?
- Which related Registry Records exist?
- Where can authoritative documentation be found?

---

## Base Schema Dependency

Every Tool SREG must first satisfy the SREG Base Schema.

The Tool Record-Type Profile adds tool-specific fields and validation rules.

```text
SREG Base Schema
  +
Tool Record-Type Profile
  =
Valid Tool SREG
```

---

## Required Base Fields

The following SREG Base Schema fields are required:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Authoritative Source Record;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG Base Schema version;
- Tool Record-Type Profile version;
- registration date;
- last updated date.

The Source-System Identifier is required when the Source Institution provides one.

---

## Required Tool Fields

### Registry Record Type

Required value:

```text
Tool
```

---

### Tool Class

The primary controlled classification assigned to the tool.

Approved or potential values include:

```text
Intelligence System
Certification System
Registry System
Historical System
Integrity System
Discovery System
Attestation System
Workflow System
Utility
Governance System
Research Tool
Preservation System
External Tool
```

Additional values require Registry governance approval and profile revision.

---

### Tool Name

The authoritative human-readable name of the tool.

Example:

```text
Satoshium Atlas
```

Registry may reproduce the source-controlled name.

Registry should not silently replace it with an invented institutional name.

---

### Institutional Purpose

A concise source-attributable description of why the tool exists.

Example:

```text
Atlas organizes and publishes jurisdiction intelligence resources.
```

This field should describe institutional purpose rather than marketing language.

---

### Operational Function

A concise description of what the tool does operationally.

Examples may include:

- creates jurisdiction resources;
- performs certification;
- creates SREGs;
- records historical events;
- creates integrity references;
- creates discovery signals;
- creates attestations;
- coordinates workflows.

---

### Source Institution

The institution responsible for the Authoritative Tool Record.

Possible values may include:

- Satoshium Atlas;
- Satoshium Certifier;
- Satoshium Registry;
- Satoshium Chronicle;
- Satoshium Anchor;
- Satoshium Beacon;
- Satoshium Attestor;
- Satoshium Navigator;
- another approved Suite institution;
- an approved external institution or developer.

---

### Authoritative Source Record

A durable reference to the authoritative tool resource.

Examples may include:

- institutional landing page;
- tool specification;
- repository;
- architecture document;
- operational manual;
- public release record;
- canonical documentation;
- governance record;
- another approved tool artifact.

---

### Registry Status

The operational status of the SREG.

This field is controlled by Registry.

It must remain separate from Source-Record Status, implementation status, release status, service availability, and deprecation status.

---

### Registry Lifecycle State

The lifecycle condition of the SREG.

Potential values may include:

```text
Pending Registration
Registered
Active
Updated
Superseded
Revoked
Archived
```

These values do not necessarily form one mandatory linear sequence.

---

## Conditionally Required Fields

### Source-System Identifier

Required when the Source Institution provides a stable identifier.

Example:

```text
SATOSHIUM-ATLAS
```

The Source-System Identifier must remain distinct from the Registry Identifier.

---

### Owner or Maintainer

Required when the responsible institution, team, developer, or maintainer is known and materially relevant.

The value should remain source-attributable.

---

### Implementation Status

Required when the Source Institution exposes an operational implementation condition.

Possible values may include:

```text
Concept
Planned
In Development
Operational
Limited Operation
Deprecated
Retired
Archived
```

Implementation Status is source-controlled context.

It is not Registry Status.

---

### Source-Record Status

Required when the Authoritative Source Record exposes a meaningful source-controlled status.

Possible values may include:

```text
Draft
Published
Active
Superseded
Deprecated
Withdrawn
Archived
```

---

### Canonical Documentation Reference

Required when a stable public or internal documentation location exists.

---

## Optional Tool Fields

### Description

A source-attributable narrative summary of the tool.

The description should not replace Institutional Purpose or Operational Function when those fields are available.

---

### Repository Reference

May identify:

- source-code repository;
- documentation repository;
- schema repository;
- release repository;
- archival repository.

The repository role should be identified explicitly.

---

### Public Landing Page

The canonical public page representing the tool or institution.

---

### Produced Record Types

May identify the classes of Source Records or artifacts produced by the tool.

Examples:

```text
Atlas
  → Jurisdiction Resources

Certifier
  → Certification Packages
  → SCPR
  → SCR
  → SCRD

Registry
  → SREGs

Chronicle
  → Historical Events

Anchor
  → Integrity References

Beacon
  → Signals

Attestor
  → Attestations

Navigator
  → Workflow Definitions
```

---

### Consumed Record Types

May identify the Source Records, Registry Records, schemas, or artifacts consumed by the tool.

---

### Dependencies

May identify:

- institutional dependencies;
- schema dependencies;
- data dependencies;
- workflow dependencies;
- service dependencies;
- repository dependencies;
- external platform dependencies;
- version dependencies.

---

### Integrations

May identify formal or operational interoperability relationships with other Suite institutions or external systems.

---

### Supported Interfaces

May include:

- HTML publication;
- JSON publication;
- API;
- repository interface;
- workflow interface;
- command-line interface;
- internal service interface.

---

### Release Information

May include:

- current release;
- release date;
- release channel;
- supported versions;
- compatibility notes;
- deprecation date;
- migration reference.

---

### Licensing and Rights

May identify:

- software license;
- documentation license;
- ownership;
- usage terms;
- distribution restrictions;
- external rights.

Registry must not infer licensing rights that the source does not provide.

---

### Security References

May identify:

- security documentation;
- disclosure policy;
- known limitations;
- integrity references;
- security review;
- access controls.

Registry registration does not constitute a security assessment.

---

### Public References

May include:

- landing page;
- repository;
- documentation;
- release notes;
- media resources;
- certification records;
- attestation records;
- Chronicle events;
- Anchor references;
- Beacon signals;
- Navigator workflows;
- archival references.

---

### Notes

May preserve additional Registry context needed for interpretation.

Notes must not replace structured fields when a structured field exists.

---

## Current Suite Tool Classes

### Atlas

Recommended Tool Class:

```text
Intelligence System
```

Institutional function:

```text
Creates and maintains jurisdiction intelligence resources.
```

### Certifier

Recommended Tool Class:

```text
Certification System
```

Institutional function:

```text
Performs standards-based certification and creates certification artifacts.
```

### Registry

Recommended Tool Class:

```text
Registry System
```

Institutional function:

```text
Creates and maintains Satoshium Registry Entries.
```

### Chronicle

Recommended Tool Class:

```text
Historical System
```

Institutional function:

```text
Creates and preserves historical events and institutional chronology.
```

### Anchor

Recommended Tool Class:

```text
Integrity System
```

Institutional function:

```text
Creates and preserves integrity references.
```

### Beacon

Recommended Tool Class:

```text
Discovery System
```

Institutional function:

```text
Creates discovery signals and visibility-oriented metadata.
```

### Attestor

Recommended Tool Class:

```text
Attestation System
```

Institutional function:

```text
Creates attestations, trust statements, and verification references.
```

### Navigator

Recommended Tool Class:

```text
Workflow System
```

Institutional function:

```text
Creates workflow definitions and coordinates cross-system activity.
```

---

## Identifier Requirements

A Tool SREG must preserve identifier domains separately.

### Registry Identifier

Assigned by Registry.

Example:

```text
SREG-TOOL-0001
```

### Source-System Identifier

Assigned by the Source Institution.

Example:

```text
SATOSHIUM-ATLAS
```

### Repository Identifier

Assigned by the repository platform when applicable.

### Release Identifier

Assigned by the Source Institution or release system.

### Workflow or Integration Identifier

Assigned by Navigator or another integration system when applicable.

Identifiers may be related.

They must not be collapsed into one field.

---

## Dependency Requirements

A dependency object may include:

```text
Dependency Type
Target Identifier
Target Identifier Domain
Target Institution
Required Version
Minimum Version
Maximum Version
Mandatory or Optional
Effective Date
Status
Source Reference
Replacement Reference
```

Potential dependency types include:

- institutional;
- schema;
- data;
- workflow;
- service;
- repository;
- platform;
- version;
- external system.

Registry records the dependency.

Registry does not create it.

---

## Relationship Requirements

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

Relationships must use approved Registry relationship types.

---

## Relationship Object Structure

A Tool relationship may include:

```text
Relationship Type
Source Identifier
Target Identifier
Target Identifier Domain
Direction
Target Institution
Effective Date
Status
Version Context
Supporting Reference
```

Dependency relationships should not be represented as generic associations when the dependency type is known.

---

## Status Separation

A Tool SREG must distinguish:

```text
Registry Status
  ≠
Registry Lifecycle State
  ≠
Source-Record Status
  ≠
Implementation Status
  ≠
Release Status
  ≠
Service Availability
  ≠
Deprecation Status
```

Example:

```text
Implementation Status: Deprecated
Source-Record Status: Published
Registry Status: Active
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for a deprecated or retired tool.

---

## Version Requirements

A Tool SREG should preserve:

- Registry Entry Version;
- Source-Record Version;
- Tool Release Version;
- SREG Base Schema version;
- Tool Record-Type Profile version;
- Registry Schema Specification version, when required;
- applicable integration version;
- applicable workflow version;
- Suite Standards version, when required;
- Suite Methodology version, when required.

A source release change does not automatically require a profile version change.

A schema migration does not automatically mean the tool changed.

---

## Core Record Structure

```text
Registry Identifier
Title
Registry Record Type
Tool Class
Tool Name
Institutional Purpose
Operational Function
Source Institution
Source-System Identifier
Authoritative Source Record
Owner or Maintainer
Implementation Status
Description
Canonical Documentation Reference
Public Landing Page
Repository References
Produced Record Types
Consumed Record Types
Dependencies
Integrations
Supported Interfaces
Release Information
Licensing and Rights
Security References
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
Tool Release Version
SREG Base Schema Version
Tool Profile Version
Public References
Typed Relationships
Registration Date
Last Updated Date
Correction References
Update References
Supersession References
Revocation References
Retirement References
Archival References
Notes
```

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-TOOL-0001 |
| Title | Satoshium Atlas |
| Registry Record Type | Tool |
| Tool Class | Intelligence System |
| Tool Name | Atlas |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | SATOSHIUM-ATLAS |
| Institutional Purpose | Organizes and publishes jurisdiction intelligence resources |
| Implementation Status | Operational |
| Source-Record Status | Active |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |
| SREG Base Schema Version | 1.0.0 |
| Tool Profile Version | 1.0.0 |

This example is illustrative.

It does not establish final production identifiers or controlled values.

---

## Example Machine-Readable Structure

```json
{
  "registry_identifier": "SREG-TOOL-0001",
  "title": "Satoshium Atlas",
  "registry_record_type": "Tool",
  "tool_class": "Intelligence System",
  "tool_name": "Atlas",
  "institutional_purpose": "Organizes and publishes jurisdiction intelligence resources.",
  "operational_function": "Creates and maintains authoritative jurisdiction resources.",
  "source_institution": "Satoshium Atlas",
  "source_system_identifier": "SATOSHIUM-ATLAS",
  "authoritative_source_record": {
    "reference": "https://example.invalid/atlas/"
  },
  "owner_or_maintainer": "Satoshium Atlas",
  "implementation_status": "Operational",
  "source_record_status": "Active",
  "registry_status": "Active",
  "registry_lifecycle_state": "Active",
  "registry_entry_version": "1.0.0",
  "source_record_version": "1.0.0",
  "tool_release_version": "1.0.0",
  "sreg_base_schema_version": "1.0.0",
  "record_type_profile_version": "1.0.0",
  "dependencies": [],
  "integrations": [],
  "public_references": [],
  "relationships": [],
  "registration_date": "2026-08-01",
  "last_updated_date": "2026-08-01"
}
```

The URL is intentionally non-operational.

The example illustrates structure only.

---

## Validation Requirements

A valid Tool SREG should satisfy the following checks.

### Identity Validation

- Registry Identifier is present and valid.
- Title is present.
- Registry Record Type equals `Tool`.
- Tool Class is approved.
- Tool Name is present.

### Source Validation

- Source Institution is present.
- Authoritative Source Record is present.
- Source-System Identifier is preserved when available.
- source attribution is internally consistent.
- Registry is not presented as the tool operator unless Registry is the Source Institution.

### Purpose and Function Validation

- Institutional Purpose is present.
- Operational Function is present.
- purpose and function do not materially conflict.
- unsupported capability claims are not introduced.

### Status Validation

- Registry Status is valid.
- Registry Lifecycle State is valid.
- Source-Record Status is not conflated with Registry Status.
- Implementation Status is not represented as Registry Status.
- service availability is not represented as Registry Lifecycle State.

### Version Validation

- Registry Entry Version is present.
- SREG Base Schema version is present.
- Tool Record-Type Profile version is present.
- Source-Record Version is preserved when available.
- Tool Release Version is preserved when available.
- version domains remain distinct.

### Dependency Validation

- dependency types are approved;
- dependency targets are identified;
- required versions are formatted correctly;
- mandatory and optional dependencies are distinguishable;
- circular dependencies are documented when legitimate and rejected when structurally invalid;
- obsolete dependencies include replacement or retirement context where available.

### Relationship Validation

- relationship types are approved;
- direction is valid;
- targets exist or are historically documented;
- produced records use appropriate `produces` relationships;
- integrations are not misrepresented as ownership;
- duplicate relationships are avoided.

### Publication Validation

- human-readable and machine-readable forms agree materially;
- canonical references are valid where available;
- dates use approved formats;
- licensing and security information are not overstated;
- required fields are public unless a documented restriction applies.

---

## Invalid Conditions

A Tool SREG should fail validation when:

- Source Institution is unidentified;
- Authoritative Source Record cannot be identified;
- Tool Class is unapproved;
- Tool Name is absent;
- Institutional Purpose is absent;
- Operational Function is absent;
- Registry and source identifiers are conflated;
- Implementation Status is used as Registry Status;
- the record claims functionality unsupported by the source;
- a dependency target is invalid;
- ownership or licensing is asserted without support;
- required versions are missing;
- official publication forms materially disagree.

---

## Tool Renaming

A tool may be renamed while retaining the same underlying identity.

A rename may be represented through:

- title update;
- Tool Name update;
- alternate-name addition;
- source-version update;
- canonical-reference update;
- relationship update.

When the renamed tool is materially a distinct successor system, supersession may be required.

Prior names should remain discoverable when historically significant.

---

## Replacement and Supersession

A Tool SREG may be superseded when:

- a distinct successor tool replaces it;
- a new Registry Identifier is required;
- the source system changes identity materially;
- the original Tool Class no longer accurately represents the source;
- governance requires a replacement SREG.

The superseded SREG should remain discoverable and reference its successor.

---

## Deprecation and Retirement

A source tool may become:

- deprecated;
- retired;
- unsupported;
- discontinued;
- replaced;
- archived.

The Tool SREG should preserve:

- final source version;
- final implementation status;
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
- governance requires withdrawal.

Registry revocation affects the SREG.

It does not deactivate, revoke, or remove the tool itself.

---

## Archival

An archived Tool SREG should preserve:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- Tool Name;
- Tool Class;
- purpose;
- function;
- implementation status;
- repositories;
- versions;
- dependencies;
- integrations;
- relationships;
- correction history;
- supersession history;
- revocation history;
- archival date;
- archival reason.

Archived does not mean deleted.

---

## Interoperability Requirements

A Tool SREG may preserve:

- canonical integration page;
- produced artifact types;
- consumed artifact types;
- identifier exchanges;
- schema dependencies;
- workflow relationships;
- version compatibility;
- status synchronization rules;
- authority boundaries.

Interoperability metadata must connect institutional objects without collapsing institutional responsibility.

---

## Human-Readable Publication Requirements

The human-readable Tool SREG should present:

- Registry Identifier;
- title;
- Tool Class;
- Tool Name;
- Source Institution;
- Source-System Identifier;
- Institutional Purpose;
- Operational Function;
- owner or maintainer;
- Implementation Status;
- canonical documentation;
- repository references;
- produced and consumed record types;
- dependencies;
- integrations;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- public references;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication Requirements

The machine-readable Tool SREG should preserve equivalent institutional meaning.

It should represent:

- identifiers;
- controlled Tool Classes;
- source attribution;
- purpose and function;
- implementation status;
- versions;
- dependencies;
- integrations;
- produced and consumed record types;
- typed relationships;
- repository and documentation references;
- status domains;
- lifecycle;
- dates;
- validation metadata.

---

## Publication Consistency

Official forms of the same Tool SREG must agree on:

- Registry Identifier;
- title;
- Registry Record Type;
- Tool Class;
- Tool Name;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- Institutional Purpose;
- Operational Function;
- Implementation Status;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- dependencies;
- integrations;
- references;
- relationships;
- dates.

A Tool SREG is not fully reconciled when official forms materially disagree.

---

## Profile Versioning

Every published Tool Record-Type Profile should include:

- profile name;
- profile identifier;
- profile version;
- status;
- effective date;
- prior version;
- superseded version, when applicable;
- compatibility notes;
- migration guidance;
- validation reference;
- changelog reference.

Prior profile versions should remain discoverable.

---

## Profile Governance

This profile should be reviewed when:

- Suite Standards change;
- Suite Methodology changes;
- Registry Rules change;
- the SREG Base Schema changes;
- Tool Classes change;
- dependency structures change;
- interoperability requirements change;
- identifier architecture changes;
- lifecycle or status frameworks change;
- release or implementation fields change;
- validation failures reveal ambiguity.

Material changes should be versioned and documented in the Registry Changelog.

---

## Relationship to Other Documentation

This profile should remain consistent with:

- Registry Schemas;
- Registry Schema Specification;
- SREG Base Schema;
- Registry Entry Model;
- Registry Record Types;
- Registry Tool Records;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Lifecycle;
- Registry Status;
- Registry Integration;
- Registry Corrections;
- applicable Source Institution documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When this profile changes:

- update this document;
- increment the profile version when required;
- update schema validation logic;
- update controlled Tool Classes;
- update dependency and integration structures;
- update examples;
- review affected Tool SREGs;
- preserve prior profile versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication.

---

## Guiding Principles

- The SREG Base Schema provides shared Registry structure.
- This profile adds tool-specific requirements.
- The Source Institution operates or controls the tool.
- Registry owns the Tool SREG.
- The SREG is not the tool itself.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status, Source-Record Status, Implementation Status, and availability remain distinct.
- Versions remain independently traceable.
- Dependencies and integrations are typed and attributable.
- Purpose and function must remain source-supported.
- Validation confirms structure, not functionality, security, availability, or endorsement.
- Human-readable and machine-readable forms must agree.
- Deprecated and superseded tools should remain historically discoverable where appropriate.
- Registration does not establish functionality, certification, security, ownership, or endorsement.

---

## Disclaimer

This profile defines the structure of a Registry-owned Tool SREG.

It does not by itself create:

- functionality;
- availability;
- security;
- certification;
- attestation;
- verification;
- ownership;
- licensing;
- legal rights;
- regulatory approval;
- endorsement;
- affiliation;
- Source Institution authority.

Those remain controlled by the Source Institution, tool operator, developer, maintainer, rights holder, Source Record, governing authority, or applicable external system.

---

## Guiding Statement

> Tools perform work.
>
> The Source Institution preserves the authoritative tool record.
>
> The SREG preserves Registry context.
>
> The profile preserves structure.
