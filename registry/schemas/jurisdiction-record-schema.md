# Jurisdiction Record-Type Profile

## Overview

This document defines the Registry Record-Type Profile for Jurisdiction Satoshium Registry Entries, or Jurisdiction SREGs.

The profile extends the SREG Base Schema with the additional fields, controlled values, relationships, validation requirements, and publication rules needed to catalog authoritative jurisdiction resources.

A Jurisdiction SREG catalogs a Source Record describing a country, state, province, territory, region, municipality, historical jurisdiction, or other approved jurisdiction class.

Registry catalogs the jurisdiction record.

Registry does not create the jurisdiction, define sovereignty, determine legal boundaries, or establish governmental authority.

---

## Constitutional Position

The Jurisdiction Record-Type Profile operates within the following schema hierarchy:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Jurisdiction Record-Type Profile
  ↓
Published Jurisdiction SREG
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
- Registry Jurisdiction Records documentation.

---

## Canonical Relationship

The canonical jurisdiction relationship is:

```text
Atlas or Approved Source Institution
  ↓
Authoritative Jurisdiction Resource
  ↓
Jurisdiction SREG
```

The Source Institution owns the Authoritative Source Record.

Registry owns the SREG.

The SREG must preserve the path back to the source.

---

## Profile Purpose

A valid Jurisdiction SREG should answer:

- What jurisdiction is being referenced?
- Which institution created or maintains the Source Record?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the source resource?
- What Jurisdiction Class applies?
- What canonical name applies?
- What alternate or historical names are known?
- What parent jurisdiction applies?
- What jurisdiction codes are available?
- What is the Source-Record Status?
- What is the Registry Status?
- What Registry Lifecycle State applies?
- Which versions apply?
- Which related records exist?
- Where can the Authoritative Source Record be found?

---

## Base Schema Dependency

Every Jurisdiction SREG must first satisfy the SREG Base Schema.

The Jurisdiction Record-Type Profile adds jurisdiction-specific fields and validation rules.

```text
SREG Base Schema
  +
Jurisdiction Record-Type Profile
  =
Valid Jurisdiction SREG
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
- Jurisdiction Record-Type Profile version;
- registration date;
- last updated date.

The Source-System Identifier is required when the Source Institution provides one.

---

## Required Jurisdiction Fields

### Registry Record Type

Required value:

```text
Jurisdiction
```

---

### Jurisdiction Class

The primary controlled classification assigned to the jurisdiction.

Approved or potential values include:

```text
Country
State
Province
Territory
Region
Municipality
Special Jurisdiction
Historical Jurisdiction
```

Additional values require Registry governance approval and profile revision.

---

### Canonical Jurisdiction Name

The primary human-readable name reported by the Source Institution.

Example:

```text
California
```

Registry may reproduce this value.

Registry does not independently create the jurisdiction's legal name.

---

### Source Institution

The institution responsible for the Authoritative Source Record.

Typical value:

```text
Satoshium Atlas
```

Other approved governmental, administrative, legal, geographic, or institutional sources may be used when appropriate.

---

### Authoritative Source Record

A durable reference to the source jurisdiction resource.

Examples may include:

- Atlas jurisdiction page;
- Atlas jurisdiction profile;
- machine-readable jurisdiction package;
- governmental record;
- administrative reference;
- historical jurisdiction source;
- another approved source artifact.

---

### Registry Status

The operational status of the SREG.

This field is controlled by Registry.

It must remain separate from Source-Record Status and jurisdictional legal status.

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
ATLAS-US-CA
```

The Source-System Identifier must remain distinct from the Registry Identifier.

---

### Parent Jurisdiction

Required when the jurisdiction exists within a defined parent hierarchy.

Example:

```text
United States
```

The value should preferably reference another Jurisdiction SREG.

---

### Country or Region

Required when needed to establish geographic or administrative context and when not already clear from the parent relationship.

---

### Source-Record Status

Required when the Source Institution exposes a meaningful source-controlled status.

Examples may include:

```text
Active
Historical
Superseded
Deprecated
Withdrawn
```

This field is controlled by the Source Institution.

---

## Optional Jurisdiction Fields

### Alternate Names

May include:

- abbreviations;
- former names;
- alternate spellings;
- multilingual names;
- colloquial names;
- historical names.

Each alternate name should identify its type and, where relevant, effective dates or language.

---

### Jurisdiction Codes

May include:

- ISO codes;
- national administrative codes;
- Atlas identifiers;
- geographic codes;
- legal or governmental codes;
- abbreviations.

Each code should identify its issuing authority or code system.

---

### Description

A source-attributable summary of the jurisdiction.

Registry descriptions should not introduce unsupported legal, political, or geographic conclusions.

---

### Geographic Context

May include:

- region;
- continent;
- coordinates;
- geographic extent;
- adjacent jurisdictions;
- containing jurisdiction;
- map reference.

Geographic information should remain attributable.

---

### Administrative Context

May include:

- governmental level;
- administrative role;
- legal classification;
- governing body;
- capital;
- effective dates;
- administrative hierarchy.

Registry should report source-controlled values without redefining governmental authority.

---

### Historical Context

May include:

- predecessor jurisdiction;
- successor jurisdiction;
- prior parent jurisdiction;
- merger history;
- split history;
- renaming history;
- effective dates;
- historical source references.

---

### Public References

May include:

- Atlas page;
- official government page;
- machine-readable source record;
- media page;
- certification record;
- attestation record;
- Chronicle event;
- Anchor reference;
- archival source.

---

### Notes

May preserve additional Registry context needed for interpretation.

Notes must not replace structured fields when a structured field is available.

---

## Identifier Requirements

A Jurisdiction SREG must preserve identifier domains separately.

### Registry Identifier

Assigned by Registry.

Example:

```text
SREG-JUR-US-CA-0001
```

### Source-System Identifier

Assigned by the Source Institution.

Example:

```text
ATLAS-US-CA
```

### External Jurisdiction Codes

Assigned by external code systems.

Examples may include:

```text
US-CA
CA
06
```

Identifiers may be related.

They must not be collapsed into one field.

---

## Hierarchy Requirements

Jurisdiction hierarchy should be represented through typed relationships rather than unstructured text alone.

Example:

```text
World
  └── United States
      └── California
```

Possible relationship types include:

```text
parent jurisdiction
child jurisdiction
contains
contained by
predecessor of
successor of
merged into
split into
part of region
```

Hierarchy relationships should preserve:

- source identifier;
- target identifier;
- direction;
- effective date, when known;
- source attribution;
- historical context;
- supporting reference.

---

## Relationship Requirements

A Jurisdiction SREG may relate to:

- Tool SREGs;
- Media SREGs;
- Certification SREGs;
- Attestation SREGs;
- Signal SREGs;
- Historical Event SREGs;
- Integrity Reference SREGs;
- Workflow records;
- other Jurisdiction SREGs.

Examples:

```text
Jurisdiction SREG
  → sourced from
  → Atlas Tool SREG
```

```text
Jurisdiction SREG
  → parent jurisdiction
  → Country SREG
```

```text
Certification SREG
  → certifies
  → Jurisdiction SREG
```

```text
Attestation SREG
  → concerns
  → Jurisdiction SREG
```

Relationships must use approved Registry relationship types.

---

## Status Separation

A Jurisdiction SREG must distinguish:

```text
Registry Status
  ≠
Source-Record Status
  ≠
Jurisdictional Legal Status
```

Example:

```text
Source-Record Status: Historical
Registry Status: Active
Registry Lifecycle State: Active
```

Registry may maintain an active historical catalog entry for a jurisdiction that no longer exists in its prior form.

---

## Version Requirements

A Jurisdiction SREG should preserve:

- Registry Entry Version;
- Source-Record Version;
- SREG Base Schema version;
- Jurisdiction Record-Type Profile version;
- Registry Schema Specification version, when required;
- Atlas resource version, when available;
- Suite Standards version, when required;
- Suite Methodology version, when required.

A schema migration does not automatically mean the Source Record changed.

A source update does not automatically require a new schema version.

---

## Core Record Structure

```text
Registry Identifier
Title
Registry Record Type
Jurisdiction Class
Source Institution
Source-System Identifier
Authoritative Source Record
Canonical Jurisdiction Name
Alternate Names
Parent Jurisdiction
Country or Region
Jurisdiction Codes
Description
Geographic Context
Administrative Context
Historical Context
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
SREG Base Schema Version
Jurisdiction Profile Version
Public References
Typed Relationships
Registration Date
Last Updated Date
Correction References
Update References
Supersession References
Revocation References
Archival References
```

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-JUR-US-CA-0001 |
| Title | California |
| Registry Record Type | Jurisdiction |
| Jurisdiction Class | State |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | ATLAS-US-CA |
| Canonical Jurisdiction Name | California |
| Parent Jurisdiction | United States |
| Jurisdiction Code | US-CA |
| Source-Record Status | Active |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |
| SREG Base Schema Version | 1.0.0 |
| Jurisdiction Profile Version | 1.0.0 |

This example is illustrative.

It does not establish final production identifiers or controlled values.

---

## Example Machine-Readable Structure

```json
{
  "registry_identifier": "SREG-JUR-US-CA-0001",
  "title": "California",
  "registry_record_type": "Jurisdiction",
  "jurisdiction_class": "State",
  "source_institution": "Satoshium Atlas",
  "source_system_identifier": "ATLAS-US-CA",
  "authoritative_source_record": {
    "reference": "https://example.invalid/atlas/us/california/"
  },
  "canonical_jurisdiction_name": "California",
  "alternate_names": [],
  "parent_jurisdiction": {
    "registry_identifier": "SREG-JUR-US-0001"
  },
  "jurisdiction_codes": [
    {
      "system": "ISO 3166-2",
      "value": "US-CA"
    }
  ],
  "source_record_status": "Active",
  "registry_status": "Active",
  "registry_lifecycle_state": "Active",
  "registry_entry_version": "1.0.0",
  "source_record_version": "1.0.0",
  "sreg_base_schema_version": "1.0.0",
  "record_type_profile_version": "1.0.0",
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

A valid Jurisdiction SREG should satisfy the following checks.

### Identity Validation

- Registry Identifier is present and valid.
- Title is present.
- Registry Record Type equals `Jurisdiction`.
- Jurisdiction Class is approved.

### Source Validation

- Source Institution is present.
- Authoritative Source Record is present.
- Source-System Identifier is preserved when available.
- Source attribution is internally consistent.

### Hierarchy Validation

- Parent Jurisdiction is present when required.
- Parent relationship targets a valid jurisdiction object.
- The record does not create an impossible self-parent relationship.
- Circular hierarchy relationships are not permitted.
- Historical and current hierarchy relationships are distinguishable.

### Status Validation

- Registry Status is valid.
- Registry Lifecycle State is valid.
- Source-Record Status is not conflated with Registry Status.
- Jurisdictional legal status is not represented as Registry Status.

### Version Validation

- Registry Entry Version is present.
- SREG Base Schema version is present.
- Jurisdiction Record-Type Profile version is present.
- Source-Record Version is preserved when available.

### Relationship Validation

- relationship types are approved;
- direction is valid;
- referenced targets exist or are historically documented;
- required supporting references are present;
- duplicate relationships are avoided.

### Publication Validation

- human-readable and machine-readable forms agree materially;
- canonical references are valid where available;
- dates use approved formats;
- required fields are public unless a documented restriction applies.

---

## Invalid Conditions

A Jurisdiction SREG should fail validation when:

- the Source Institution is unidentified;
- the Source Record cannot be identified;
- Jurisdiction Class is unapproved;
- Registry and source identifiers are conflated;
- Parent Jurisdiction conflicts with the cited source;
- hierarchy creates a circular relationship;
- Registry Status is used as legal recognition;
- the record asserts sovereignty or boundaries without source attribution;
- required versions are missing;
- official publication forms materially disagree.

---

## Name Changes

A jurisdiction name change may be represented through:

- canonical-name update;
- alternate-name addition;
- historical-name entry;
- source-version update;
- successor relationship;
- supersession.

The correct action depends on whether the underlying jurisdiction identity remains the same.

Prior names should remain discoverable when historically significant.

---

## Boundary and Authority Changes

Boundary or authority changes should be represented through source-attributable fields and relationships.

Possible structures include:

- effective date;
- prior boundary reference;
- new boundary reference;
- prior parent jurisdiction;
- new parent jurisdiction;
- predecessor relationship;
- successor relationship;
- merger relationship;
- split relationship;
- Chronicle event reference;
- supporting source.

Registry must not independently resolve disputed boundaries.

---

## Mergers and Splits

### Merger

When multiple jurisdictions become one successor jurisdiction, the records should preserve:

- prior Registry Identifiers;
- successor Registry Identifier;
- effective date;
- merger source;
- historical relationships;
- lifecycle changes.

### Split

When one jurisdiction becomes multiple successors, the records should preserve:

- prior Registry Identifier;
- successor Registry Identifiers;
- effective date;
- split source;
- historical relationships;
- lifecycle changes.

---

## Supersession

A Jurisdiction SREG may be superseded when:

- a distinct successor jurisdiction replaces it;
- the Source Record changes identity materially;
- a new Registry Identifier is required;
- a merger or split creates a different canonical object;
- the original classification is no longer valid.

A superseded SREG should remain discoverable.

---

## Revocation

Registry may revoke a Jurisdiction SREG when:

- registration was invalid;
- the Source Institution was materially misidentified;
- the Source Record did not support the represented jurisdiction;
- the SREG materially misrepresented the source;
- governance requires withdrawal.

Registry revocation does not dissolve, invalidate, or legally affect the jurisdiction.

---

## Archival

An archived Jurisdiction SREG should preserve:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- canonical and alternate names;
- hierarchy;
- jurisdiction codes;
- versions;
- relationships;
- correction history;
- supersession history;
- revocation history;
- archival date;
- archival reason.

Archived does not mean deleted.

---

## Human-Readable Publication Requirements

The human-readable Jurisdiction SREG should present:

- Registry Identifier;
- title;
- Jurisdiction Class;
- Source Institution;
- Source-System Identifier;
- canonical name;
- alternate names;
- parent jurisdiction;
- jurisdiction codes;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- references;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication Requirements

The machine-readable Jurisdiction SREG should preserve equivalent institutional meaning.

It should represent:

- identifiers;
- controlled classifications;
- source references;
- hierarchy;
- jurisdiction codes;
- status domains;
- lifecycle;
- versions;
- typed relationships;
- dates;
- validation metadata.

---

## Publication Consistency

Official forms of the same Jurisdiction SREG must agree on:

- Registry Identifier;
- title;
- Registry Record Type;
- Jurisdiction Class;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- canonical name;
- parent jurisdiction;
- jurisdiction codes;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- references;
- relationships;
- dates.

A Jurisdiction SREG is not fully reconciled when official forms materially disagree.

---

## Profile Versioning

Every published Jurisdiction Record-Type Profile should include:

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
- Jurisdiction Classes change;
- identifier architecture changes;
- hierarchy rules change;
- geographic code support changes;
- lifecycle or status frameworks change;
- Atlas integration changes;
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
- Registry Jurisdiction Records;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Lifecycle;
- Registry Status;
- Registry Integration;
- Registry Corrections;
- Atlas institutional documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When this profile changes:

- update this document;
- increment the profile version when required;
- update schema validation logic;
- update controlled Jurisdiction Classes;
- update relationship rules;
- update examples;
- review affected Jurisdiction SREGs;
- preserve prior profile versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication.

---

## Guiding Principles

- The SREG Base Schema provides shared Registry structure.
- This profile adds jurisdiction-specific requirements.
- Atlas or another approved Source Institution owns the jurisdiction resource.
- Registry owns the Jurisdiction SREG.
- The SREG is not the jurisdiction itself.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and source lifecycle remain distinct.
- Hierarchy must remain typed and source-attributable.
- Versions remain independently traceable.
- Validation confirms structure, not sovereignty or legal authority.
- Human-readable and machine-readable forms must agree.
- Historical and superseded jurisdictions should remain discoverable.
- Registration does not create legal recognition.

---

## Disclaimer

This profile defines the structure of a Registry-owned Jurisdiction SREG.

It does not by itself create:

- a jurisdiction;
- sovereignty;
- governmental authority;
- legal boundaries;
- legal recognition;
- regulatory approval;
- ownership;
- certification;
- attestation;
- endorsement;
- affiliation;
- Source Institution authority.

Those remain controlled by the applicable government, legal authority, Source Institution, Source Record, rights holder, or external system.

---

## Guiding Statement

> Jurisdictions define places and authority through their own institutions.
>
> The Source Institution preserves the authoritative jurisdiction resource.
>
> The SREG preserves Registry context.
>
> The profile preserves structure.
