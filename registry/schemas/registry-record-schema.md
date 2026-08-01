# SREG Base Schema

## Overview

This document defines the foundational schema for the Satoshium Registry Entry, or SREG.

The SREG Base Schema is the common Registry structure from which all approved Registry Record-Type Profiles extend.

Current initial Registry Record Types include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Future Registry Record Types may be introduced through documented governance.

The SREG Base Schema establishes a consistent framework for identifying, classifying, attributing, relating, versioning, validating, publishing, maintaining, correcting, and preserving Registry Entries across the Satoshium Suite.

---

## Constitutional Position

The SREG Base Schema operates within the following hierarchy:

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

The SREG Base Schema must remain consistent with:

- Suite Standards;
- Suite Methodology;
- Suite Interoperability;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Entry Model;
- Registry Record Types;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections.

---

## Canonical Registry Hierarchy

The schema implements the Registry's canonical operational hierarchy:

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

The institution responsible for Registry operations and the public catalog.

### Registry Entry

The canonical Registry-owned operational object.

### Registry Record Type

The approved primary classification assigned to the SREG.

### Authoritative Source Record

The source object created and controlled by the originating institution.

---

## Schema Purpose

A valid SREG should answer:

- What Registry Entry is this?
- What Registry Identifier identifies it?
- What Record Type applies?
- Which Source Institution created the Source Record?
- What Authoritative Source Record is being cataloged?
- What Source-System Identifier identifies the source object?
- What is the Registry Status?
- What is the Registry Lifecycle State?
- What is the Source-Record Status?
- Which versions apply?
- What public references exist?
- What relationships connect this SREG to other objects?
- What corrections, updates, supersession, revocation, or archival history exists?
- How can the SREG and its source be found later?

---

## Base Schema Principle

Every operational Registry Entry must satisfy the SREG Base Schema.

A Record-Type Profile may add requirements.

It must not remove or contradict required base fields.

```text
SREG Base Schema
  +
Approved Record-Type Profile
  =
Valid Published SREG
```

---

## Required Fields

### Registry Identifier

A unique identifier assigned by Satoshium Registry.

Example:

```text
SREG-JUR-US-CA-0001
```

Requirements:

- must be unique within Registry;
- must remain stable across ordinary updates;
- must not be reused for another SREG;
- must identify the Registry Entry, not the Source Record;
- must follow the approved Registry Identifier specification.

---

### Title

A human-readable Registry title.

Requirements:

- must be present;
- should be concise and descriptive;
- should identify the SREG clearly;
- may reproduce the source title when appropriate;
- must not introduce unsupported claims.

---

### Registry Record Type

The approved primary classification assigned to the SREG.

Current initial values:

```text
Tool
Jurisdiction
Media
Certification
Attestation
Signal
```

Requirements:

- exactly one primary Record Type must be assigned;
- the value must be approved;
- the corresponding Record-Type Profile must be identified;
- a Record Type must not be improvised during individual record creation.

---

### Source Institution

The institution responsible for the Authoritative Source Record.

Examples may include:

- Satoshium Atlas;
- Satoshium Certifier;
- Satoshium Registry;
- Satoshium Chronicle;
- Satoshium Anchor;
- Satoshium Beacon;
- Satoshium Attestor;
- Satoshium Navigator;
- another approved institution.

Requirements:

- must be identifiable;
- must remain distinct from Registry unless Registry is itself the Source Institution;
- must reflect source authority accurately.

---

### Authoritative Source Record

A structured reference to the Source Record being cataloged.

The object should identify:

- source title or name;
- canonical source reference;
- source object type;
- source institution;
- source version, when available;
- source identifier, when available.

The SREG must not silently replace the Source Record.

---

### Registry Status

The current Registry-controlled operational status of the SREG.

Requirements:

- must use an approved Registry Status value;
- must remain distinct from Source-Record Status;
- must remain distinct from Registry Lifecycle State;
- must not be used to represent certification, attestation, legal, governmental, publication, or operational status belonging to another institution.

---

### Registry Lifecycle State

The current lifecycle condition of the SREG.

Potential approved values may include:

```text
Pending Registration
Registered
Active
Updated
Superseded
Revoked
Archived
```

Requirements:

- must use an approved value;
- must describe the SREG;
- must remain distinct from source lifecycle;
- must not be treated as a mandatory linear sequence unless a governing policy explicitly requires one.

---

### Registry Entry Version

The version of the Registry Entry.

Example:

```text
1.0.0
```

Requirements:

- must be present;
- must follow the approved versioning convention;
- must remain distinct from Source-Record Version;
- must change when Registry-controlled content changes materially under the applicable versioning policy.

---

### SREG Base Schema Version

The version of the SREG Base Schema used to validate the entry.

Example:

```text
1.0.0
```

---

### Record-Type Profile Version

The version of the applicable Record-Type Profile.

Example:

```text
1.0.0
```

---

### Registration Date

The date Registry first published or formally registered the SREG.

This date must remain distinct from:

- source creation date;
- source publication date;
- certification date;
- attestation date;
- effective date;
- last updated date.

---

### Last Updated Date

The date of the most recent Registry-controlled update to the SREG.

This field should not be changed merely because the Source Record changed unless the SREG was actually updated.

---

## Conditionally Required Fields

### Source-System Identifier

Required when the Source Institution provides a stable identifier.

Example:

```text
SC-CERT-2026-0001
```

Requirements:

- must preserve the source-controlled value;
- must remain distinct from the Registry Identifier;
- must identify the Source Record or source object;
- must not be invented when the source provides none.

---

### Source-Record Status

Required when the Source Institution exposes a meaningful source-controlled status.

Examples may include:

```text
Active
Published
Certified
Revoked
Withdrawn
Superseded
Historical
Archived
```

Requirements:

- must remain attributable to the Source Institution;
- must not be treated as Registry Status;
- must preserve the exact source-controlled meaning where practical.

---

### Source-Record Version

Required when the Source Institution exposes version information.

Requirements:

- must remain distinct from Registry Entry Version;
- should preserve the source's own version convention;
- should identify which source version the SREG references.

---

### Public References

Required when public references are necessary to locate the Source Record or understand the SREG.

References may include:

- canonical source page;
- machine-readable source record;
- institutional landing page;
- repository path;
- public artifact;
- archival location;
- integrity reference;
- related record page.

---

### Relationships

Required when the Record-Type Profile or source context requires links to other SREGs or institutional records.

Relationships must use approved typed structures.

---

## Optional Base Fields

### Description

A concise Registry summary of the entry.

The description should:

- remain source-attributable where it reports source meaning;
- distinguish Registry context from source claims;
- avoid unsupported conclusions;
- not replace structured fields.

---

### Alternate Titles

May preserve:

- former titles;
- source titles;
- abbreviations;
- translated titles;
- common names;
- historical names.

Each alternate title should identify its type and, where applicable, language or effective dates.

---

### Source Publication Date

The source-controlled publication date.

Must remain distinct from Registry Registration Date.

---

### Source Effective Date

The date a source-controlled decision, status, certification, attestation, or other object became effective.

---

### Language

The primary language or languages of the Source Record or SREG publication.

Controlled language codes should be used when practical.

---

### Notes

Additional Registry context that supports interpretation.

Notes must not replace structured fields when a structured field exists.

---

### Rights and Access

May report:

- rights holder;
- license;
- access designation;
- visibility;
- usage terms;
- restrictions;
- privacy classification.

Registry must not infer rights that the source does not grant.

---

### Integrity References

May identify:

- Anchor records;
- cryptographic hashes;
- checksums;
- timestamps;
- signatures;
- archival manifests;
- preservation packages.

Integrity references remain distinct from Registry schema validation.

---

### Validation Metadata

May identify:

- validation date;
- validator version;
- schema result;
- profile result;
- warnings;
- reconciliation result;
- publication consistency result.

---

## Core Record Structure

```text
Registry Identifier
Title
Registry Record Type
Source Institution
Source-System Identifier
Authoritative Source Record
Description
Alternate Titles
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
SREG Base Schema Version
Record-Type Profile Version
Registry Schema Specification Version
Public References
Typed Relationships
Rights and Access
Integrity References
Registration Date
Last Updated Date
Source Publication Date
Source Effective Date
Validation Metadata
Correction References
Update References
Supersession References
Revocation References
Retirement References
Archival References
Notes
```

---

## Identifier Domains

The SREG Base Schema must preserve identifier domains separately.

Examples include:

```text
Registry Identifier
Source-System Identifier
Certification Identifier
Attestation Identifier
Integrity Reference Identifier
Workflow Identifier
External Identifier
```

Identifiers may be related.

They must not be collapsed into one field.

```text
Registry Identifier
  ≠
Source-System Identifier
```

---

## Status Domains

The SREG Base Schema must preserve distinct status domains.

Examples include:

- Registry Status;
- Source-Record Status;
- Certification Status;
- Attestation Status;
- Tool Implementation Status;
- Media Publication Status;
- Signal Publication Status;
- Jurisdictional or Legal Status.

A value from one domain must not be reused as though it belongs to another without an explicit mapping.

---

## Lifecycle Domains

Registry Lifecycle State describes the SREG.

It does not replace:

- source lifecycle;
- certification lifecycle;
- attestation lifecycle;
- tool lifecycle;
- media lifecycle;
- signal lifecycle;
- jurisdictional legal condition.

A Source Record may be revoked, retired, or unavailable while the SREG remains active as a historical catalog entry.

---

## Version Domains

The SREG Base Schema should preserve independent version fields for:

- Registry Entry Version;
- Source-Record Version;
- SREG Base Schema Version;
- Record-Type Profile Version;
- Registry Schema Specification Version;
- Registry Rules Version;
- Registry Policy Version;
- Suite Standards Version;
- Suite Methodology Version.

A change in one version domain does not automatically imply a change in another.

---

## Relationship Structure

Every relationship should be represented as a typed, attributable, directional object.

A relationship may include:

```text
Relationship Type
Source Registry Identifier
Target Identifier
Target Identifier Domain
Target Institution
Direction
Status
Effective Date
Version Context
Historical Context
Supporting Reference
```

Potential relationship types include:

- references;
- produced by;
- produces;
- sourced from;
- certifies;
- certified by;
- attests to;
- attested by;
- anchored by;
- discovers;
- documents;
- concerns;
- parent jurisdiction;
- child jurisdiction;
- depends on;
- integrates with;
- part of;
- derivative of;
- supersedes;
- superseded by;
- coordinated through.

Relationship types must be approved through Registry governance.

---

## Public Reference Structure

A public reference may include:

```text
Reference Type
Title
Institution
URL or Path
Canonical Status
Access Status
Version
Effective Date
Historical Status
```

Potential reference types include:

- canonical source;
- Registry HTML;
- SREG JSON;
- repository;
- source artifact;
- archival copy;
- integrity reference;
- related institutional page;
- correction record;
- update record;
- retirement record.

---

## History and Change References

A SREG may preserve structured references to:

- Update Records;
- Correction Records;
- superseding SREGs;
- superseded SREGs;
- revocation records;
- retirement records;
- archival records;
- migration records;
- prior publication versions.

Material history must not be silently erased.

---

## Specialized Record-Type Profiles

The SREG Base Schema serves as the foundation for profiles including:

### Tool Record-Type Profile

Adds fields for Tool Class, purpose, function, owner or maintainer, implementation status, dependencies, repositories, and integrations.

### Jurisdiction Record-Type Profile

Adds fields for Jurisdiction Class, canonical name, alternate names, parent jurisdiction, codes, hierarchy, and historical relationships.

### Media Record-Type Profile

Adds fields for Media Class, format, subject, publisher, visibility, access, rights, derivatives, and integrity references.

### Certification Record-Type Profile

Adds fields for Certification Identifier, certified subject, class, outcome, Certification Status, standards, methodology, scope, evidence, Certification Package, SCPR, SCR, and SCRD references.

### Attestation Record-Type Profile

Adds fields for attestation classification, attested subject, statement, evidence, Attestor-controlled status, and trust relationships.

### Signal Record-Type Profile

Adds fields for Signal Class, statement, chronology, associated subject or event, originating channel, and discovery relationships.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-MED-US-NH-0001 |
| Title | New Hampshire Orientation Video |
| Registry Record Type | Media |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | ATLAS-MEDIA-US-NH-001 |
| Source-Record Status | Published |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |
| Source-Record Version | 1.0.0 |
| SREG Base Schema Version | 1.0.0 |
| Record-Type Profile Version | 1.0.0 |
| Registration Date | 2026-08-01 |
| Last Updated Date | 2026-08-01 |

This example is illustrative.

It does not establish final production identifiers or controlled values.

---

## Example Machine-Readable Structure

```json
{
  "registry_identifier": "SREG-MED-US-NH-0001",
  "title": "New Hampshire Orientation Video",
  "registry_record_type": "Media",
  "source_institution": "Satoshium Atlas",
  "source_system_identifier": "ATLAS-MEDIA-US-NH-001",
  "authoritative_source_record": {
    "title": "New Hampshire Orientation Video",
    "reference": "https://example.invalid/atlas/us/new-hampshire/media/orientation/",
    "record_type": "Video",
    "version": "1.0.0"
  },
  "description": "Orientation video introducing New Hampshire jurisdiction resources.",
  "source_record_status": "Published",
  "registry_status": "Active",
  "registry_lifecycle_state": "Active",
  "registry_entry_version": "1.0.0",
  "source_record_version": "1.0.0",
  "sreg_base_schema_version": "1.0.0",
  "record_type_profile": {
    "name": "Media",
    "version": "1.0.0"
  },
  "public_references": [],
  "relationships": [],
  "registration_date": "2026-08-01",
  "last_updated_date": "2026-08-01",
  "validation_metadata": {
    "base_schema_valid": true,
    "record_type_profile_valid": true,
    "publication_reconciled": true
  }
}
```

The URL is intentionally non-operational.

The example illustrates structure only.

---

## Validation Requirements

A valid SREG must satisfy the following checks.

### Identity Validation

- Registry Identifier is present.
- Registry Identifier is unique and structurally valid.
- Title is present.
- Registry Record Type is approved.
- applicable Record-Type Profile is identified.

### Source Validation

- Source Institution is present.
- Authoritative Source Record is identifiable.
- Source-System Identifier is preserved when available.
- source attribution is internally consistent.
- the SREG does not replace the Source Record.

### Status Validation

- Registry Status is approved.
- Registry Lifecycle State is approved.
- Source-Record Status is not conflated with Registry Status.
- source-controlled statuses remain attributable.

### Version Validation

- Registry Entry Version is present.
- SREG Base Schema Version is present.
- Record-Type Profile Version is present.
- Source-Record Version is preserved when available.
- version domains remain distinct.

### Relationship Validation

- relationship types are approved;
- source and target identifiers are present;
- identifier domains are clear;
- direction is valid;
- targets exist or are historically documented;
- duplicate relationships are avoided;
- required supporting references are present.

### Reference Validation

- canonical references are identified where available;
- public reference types are clear;
- historical references are distinguishable;
- access status is not misrepresented.

### Publication Validation

- human-readable and machine-readable forms agree materially;
- dates use approved formats;
- required fields are public unless a documented restriction applies;
- validation metadata is present when required.

---

## Invalid Conditions

A SREG should fail validation when:

- Registry Identifier is absent, duplicated, or malformed;
- Source Institution is unidentified;
- Authoritative Source Record cannot be identified;
- Record Type is unapproved;
- the required Record-Type Profile is absent;
- Registry and source identifiers are conflated;
- Registry Status and Source-Record Status are conflated;
- lifecycle domains are conflated;
- required version fields are missing;
- relationship targets are invalid;
- source authority is misrepresented;
- the SREG asserts ownership, certification, attestation, or rights without support;
- official publication forms materially disagree.

---

## Human-Readable Publication Requirements

A human-readable SREG should communicate:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- description;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- public references;
- relationships;
- registration date;
- last updated date;
- material correction or retirement notices.

---

## Machine-Readable Publication Requirements

A machine-readable SREG should preserve equivalent institutional meaning.

It should represent:

- identifiers;
- controlled classifications;
- source attribution;
- source references;
- status domains;
- lifecycle;
- versions;
- typed relationships;
- public references;
- dates;
- rights and access metadata where applicable;
- integrity references;
- validation metadata;
- history references.

---

## Publication Consistency

Official forms of the same SREG must agree on:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- references;
- relationships;
- dates.

A SREG is not fully reconciled when official forms materially disagree.

---

## Updates

A SREG may be updated when:

- source information changes;
- Source-Record Status changes;
- public references change;
- relationships change;
- Registry metadata improves;
- a schema migration occurs;
- the applicable Record-Type Profile changes.

Updates must preserve Registry and source authority boundaries.

---

## Corrections

A correction may repair Registry-owned errors such as:

- incorrect identifier reference;
- incorrect source attribution;
- incorrect title;
- incorrect Record Type;
- incorrect status;
- incorrect relationship;
- incorrect version metadata;
- inconsistent publication.

A correction must not rewrite the Source Record.

---

## Supersession

A SREG may be superseded when:

- a distinct successor Registry Entry replaces it;
- a new Registry Identifier is required;
- the represented object changes identity materially;
- the prior Record Type is no longer valid;
- governance requires replacement.

The prior SREG should remain discoverable.

---

## Revocation

Registry may revoke a SREG when:

- registration was invalid;
- the Source Institution was materially misidentified;
- the Source Record did not support the represented object;
- the SREG materially misrepresented the source;
- governance requires withdrawal.

Registry revocation affects the SREG.

It does not automatically affect the Source Record.

---

## Retirement and Archival

A retired or archived SREG should preserve:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- versions;
- references;
- relationships;
- update history;
- correction history;
- supersession history;
- revocation history;
- retirement or archival date;
- reason;
- successor or replacement, when applicable.

Archived does not mean deleted.

---

## Schema Versioning

Every published SREG Base Schema should include:

- schema name;
- schema identifier;
- schema version;
- status;
- effective date;
- prior version;
- superseded version, when applicable;
- compatibility notes;
- migration guidance;
- validation reference;
- changelog reference.

Prior schema versions should remain discoverable.

---

## Schema Migration

Schema migration should preserve:

- prior schema version;
- new schema version;
- migration date;
- changed fields;
- transformation rules;
- validation result;
- prior Registry Entry Version;
- replacement Registry Entry Version;
- compatibility notes;
- breaking-change notes.

```text
Schema migration
  ≠
Source Record change
```

A schema migration changes Registry structure.

It does not necessarily mean the Source Record changed.

---

## Schema Governance

The SREG Base Schema should be reviewed when:

- Suite Standards change;
- Suite Methodology changes;
- Suite Interoperability changes;
- Registry Rules change;
- Registry Policies change;
- identifier architecture changes;
- Record Types change;
- status or lifecycle frameworks change;
- versioning requirements change;
- relationship models change;
- publication formats change;
- validation failures reveal ambiguity.

Material changes should be versioned and documented in the Registry Changelog.

---

## Relationship to Other Documentation

This schema should remain consistent with:

- Registry Schemas;
- Registry Schema Specification;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Lifecycle;
- Registry Status;
- Registry Integration;
- Registry Corrections;
- Registry Changelog;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When the SREG Base Schema changes:

- update this document;
- increment the schema version when required;
- update the Registry Schema Specification;
- review every Record-Type Profile;
- update validation logic;
- update controlled values;
- update examples;
- review affected SREGs;
- preserve prior schema versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication;
- create migration guidance where necessary.

---

## Guiding Principles

- The SREG is Registry's canonical operational object.
- The SREG Base Schema provides shared Registry structure.
- Record-Type Profiles add controlled type-specific requirements.
- Source Institutions own Source Records.
- Registry owns SREGs.
- The SREG must not replace the Source Record.
- Registry and source identifiers remain distinct.
- Registry and source status domains remain distinct.
- Registry and source lifecycle domains remain distinct.
- Versions remain independently traceable.
- Relationships are typed, directional, and attributable.
- Validation confirms Registry structure, not source truth.
- Human-readable and machine-readable forms must agree.
- Material history remains discoverable.
- Registration does not create authority.

---

## Disclaimer

The SREG Base Schema defines the structure of Registry-owned Satoshium Registry Entries.

It does not by itself create:

- Source Institution authority;
- certification;
- attestation;
- verification;
- ownership;
- legal rights;
- governmental recognition;
- regulatory approval;
- endorsement;
- affiliation;
- truth.

Those remain controlled by the applicable Source Institution, Source Record, rights holder, governing authority, or external system.

---

## Guiding Statement

> Source Records preserve institutional authority.
>
> SREGs preserve Registry context.
>
> Record-Type Profiles preserve specialized meaning.
>
> The Base Schema preserves coherence across them all.
