# Registry Jurisdiction Records

## Overview

This document defines how Jurisdiction Records are represented within Satoshium Registry.

A Jurisdiction Record is a Satoshium Registry Entry, or SREG, that catalogs an Authoritative Source Record describing a geographic, governmental, political, legal, or administrative jurisdiction.

Registry catalogs the jurisdiction record.

Registry does not create the jurisdiction, define its legal authority, or determine its boundaries.

---

## Constitutional Position

Jurisdiction Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Atlas Institutional Implementation
  ↓
Authoritative Jurisdiction Resource
  ↓
Registry Jurisdiction SREG
```

Atlas may create and maintain canonical jurisdiction intelligence resources.

Registry creates and maintains the SREG that identifies, classifies, references, relates, versions, and preserves discoverability of the Atlas-owned or otherwise authoritative Source Record.

---

## Canonical Relationship

The canonical operational relationship is:

```text
Atlas
  ↓
Authoritative Jurisdiction Resource
  ↓
Registry Jurisdiction SREG
```

This relationship preserves institutional separation:

- Atlas owns the jurisdiction intelligence resource;
- Registry owns the SREG;
- the SREG points back to the Authoritative Source Record;
- Registry does not absorb Atlas authority.

---

## Purpose

Jurisdiction Records exist to improve:

- geographic discoverability;
- source attribution;
- jurisdiction classification;
- hierarchy mapping;
- relationship mapping;
- version awareness;
- lifecycle visibility;
- public reference management;
- interoperability;
- historical continuity.

A Registry Jurisdiction SREG should help answer:

- What jurisdiction is being referenced?
- Which institution created the Source Record?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the source resource?
- What Jurisdiction Class applies?
- What parent jurisdiction applies?
- What canonical source reference exists?
- What is the Registry Status?
- What is the Source-Record Status?
- Which versions apply?
- What media, certifications, attestations, signals, or historical records are related?
- How can the Authoritative Source Record be found?

---

## Record Type

The primary Registry Record Type is:

```text
Jurisdiction
```

Every operational Jurisdiction SREG must use the approved Jurisdiction Record-Type Profile.

The profile may define:

- required fields;
- optional fields;
- controlled jurisdiction classes;
- parent-child requirements;
- identifier expectations;
- required relationships;
- permitted relationships;
- source-reference requirements;
- status requirements;
- lifecycle requirements;
- validation rules;
- publication requirements.

---

## Source Institution

The Source Institution will normally be:

```text
Satoshium Atlas
```

An approved governmental, legal, administrative, geographic, or external institutional source may also serve as the Source Institution when permitted by Registry governance.

The Source Institution must remain distinct from Registry.

---

## Authoritative Source Record

Every Jurisdiction SREG must identify the Authoritative Source Record being cataloged.

The Source Record may include:

- Atlas jurisdiction page;
- Atlas jurisdiction profile;
- machine-readable jurisdiction package;
- canonical jurisdiction metadata;
- evidence-backed jurisdiction resource;
- external governmental or administrative record;
- historical jurisdiction reference;
- another approved jurisdiction artifact.

The SREG should preserve a durable canonical source reference whenever available.

---

## Registry Identifier and Source-System Identifier

A Jurisdiction SREG must preserve distinct identifiers.

### Registry Identifier

Assigned by Satoshium Registry.

Identifies the SREG.

### Source-System Identifier

Assigned by Atlas or the originating Source Institution.

Identifies the Authoritative Jurisdiction Resource.

Example:

```text
Registry Identifier: SREG-JUR-US-CA-0001
Source-System Identifier: ATLAS-US-CA
```

The Registry Identifier must not replace, alter, or overwrite the Source-System Identifier.

---

## Jurisdiction Classes

Controlled Jurisdiction Classes may include:

### Country

A national-level sovereign or internationally recognized political entity.

### State

A first-order subnational entity commonly used in federal or similar systems.

### Province

A first-order or major administrative division used by various countries.

### Territory

A territorial, dependent, autonomous, or specially administered entity.

### Region

A geographic, administrative, political, economic, or organizational region.

### Municipality

A city, county, district, borough, commune, township, or other local administrative entity.

### Special Jurisdiction

A jurisdiction with a distinct legal, administrative, economic, or political status.

### Historical Jurisdiction

A former, renamed, merged, divided, superseded, or otherwise historically significant jurisdiction.

Additional classes require approval through Atlas and Registry governance as applicable.

---

## Jurisdiction Hierarchy

Jurisdiction Records may preserve hierarchical relationships.

Example:

```text
World
  └── United States
      └── California
          └── San Joaquin County
              └── Ripon
```

A Jurisdiction SREG may preserve:

- parent jurisdiction;
- child jurisdictions;
- peer jurisdictions;
- containing region;
- associated territory;
- historical predecessor;
- historical successor.

Hierarchy is a Registry relationship model.

It must not be used to invent legal, political, or administrative authority.

---

## Required SREG Elements

An operational Jurisdiction SREG should include:

### Identity

- Registry Identifier;
- title;
- Registry Record Type;
- Jurisdiction Class.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier;
- canonical source reference.

### Jurisdiction Context

- canonical jurisdiction name;
- alternate names;
- parent jurisdiction;
- applicable country or region;
- jurisdiction codes;
- geographic or administrative classification;
- Source-Record Status.

### Registry Context

- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG schema version;
- Jurisdiction Record-Type Profile version;
- registration date;
- last updated date.

### Relationships

- parent and child jurisdictions;
- related Tool SREGs;
- related Media SREGs;
- related Certification SREGs;
- related Attestation SREGs;
- related Signal SREGs;
- related Historical Event SREGs;
- related integrity references;
- related workflows.

---

## Example Record Structure

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
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
Schema Version
Profile Version
Public References
Relationships
Registration Date
Last Updated
```

The authoritative field definitions belong to the Registry Schema Specification and Jurisdiction Record-Type Profile.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-JUR-US-CA-0001 |
| Registry Record Type | Jurisdiction |
| Jurisdiction Class | State |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | ATLAS-US-CA |
| Canonical Jurisdiction Name | California |
| Parent Jurisdiction | United States |
| Source-Record Status | Active |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |

This example is illustrative and does not establish final production identifiers or controlled values.

---

## Authority Boundary

### Atlas or Source Institution Authority

The Source Institution remains authoritative for:

- Source-System Identifier;
- Source Record content;
- canonical jurisdiction description;
- source version;
- Source-Record Status;
- source evidence;
- source publication;
- source-controlled classifications;
- source-controlled geographic or administrative interpretation.

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

Registry may report source-controlled jurisdiction values.

Registry does not create the jurisdiction or redefine its legal status.

---

## Related Registry Records

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
Jurisdiction SREG
  → related to
  → Media SREG
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

Relationships must use approved types and preserve direction where applicable.

---

## Jurisdiction Record Workflow

Registry should create a Jurisdiction SREG through the following process:

```text
Jurisdiction Source Record Identified
  ↓
Source Institution Confirmed
  ↓
Source Authority Confirmed
  ↓
Registrability Determined
  ↓
Jurisdiction Record Type Assigned
  ↓
Jurisdiction Class Assigned
  ↓
Registry Identifier Assigned
  ↓
Source-System Identifier Preserved
  ↓
Hierarchy, References, and Relationships Established
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

A Jurisdiction SREG may move through approved Registry Lifecycle States such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states describe the SREG.

They do not replace the legal, governmental, administrative, or source-controlled status of the jurisdiction.

Example:

```text
Source-Record Status: Historical
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for a jurisdiction that no longer exists in its prior form.

---

## Updates

A Jurisdiction SREG may be updated when:

- Atlas publishes a new source version;
- Source-Record Status changes;
- the canonical source location changes;
- parent-child relationships change;
- jurisdiction codes change;
- names or alternate names change;
- public references expand;
- relationships evolve;
- Registry metadata improves;
- schema migration occurs;
- the Jurisdiction Record-Type Profile changes.

Updates must preserve the distinction between source-controlled changes and Registry-controlled changes.

---

## Corrections

A Registry correction may be required when Registry incorrectly records:

- Source Institution;
- Source-System Identifier;
- source URL;
- Jurisdiction Class;
- parent jurisdiction;
- jurisdiction code;
- Registry Status;
- relationship target;
- version metadata;
- publication data.

Registry may correct its representation of source-controlled values.

Registry may not redefine the jurisdiction's legal or governmental status through a Registry correction.

---

## Name Changes

Jurisdiction names may change over time.

A name change may be handled through:

- alternate-name update;
- canonical-name update;
- source-version update;
- historical relationship;
- supersession;
- successor SREG creation.

The correct action depends on whether the underlying jurisdiction identity remains the same.

Prior names should remain discoverable when historically significant.

---

## Boundary and Authority Changes

Jurisdiction boundaries, administrative structures, or legal relationships may change.

Registry should distinguish among:

- source-reported boundary change;
- source-reported authority change;
- classification update;
- parent-jurisdiction update;
- successor jurisdiction;
- split;
- merger;
- historical transition.

Registry must not independently determine disputed boundaries or governmental authority.

Where sources conflict, Registry should preserve source attribution and avoid presenting an unsupported definitive conclusion.

---

## Mergers and Splits

### Merger

Multiple prior jurisdictions may be replaced by one successor jurisdiction.

### Split

One prior jurisdiction may be replaced by multiple successor jurisdictions.

The Registry record structure should preserve:

- prior Registry Identifiers;
- successor identifiers;
- effective date;
- source references;
- historical relationships;
- version history;
- lifecycle changes;
- public continuity.

---

## Supersession

A Jurisdiction SREG may be superseded when:

- a distinct successor jurisdiction record replaces it;
- a new Registry Identifier is required;
- the prior Source Record is replaced by a successor resource;
- the original classification no longer accurately represents the source;
- a merger, split, or identity change creates a distinct object.

The prior SREG should remain discoverable and reference its successor.

---

## Revocation

Registry may revoke a Jurisdiction SREG when:

- registration was invalid;
- the Source Institution was materially misidentified;
- the Source Record did not support the represented jurisdiction;
- the SREG materially misrepresented the source;
- governance requires withdrawal from active recognition.

Registry revocation does not revoke or dissolve the jurisdiction.

---

## Archival

A Jurisdiction SREG may be archived while preserving:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- canonical and alternate names;
- jurisdiction hierarchy;
- source references;
- versions;
- relationships;
- corrections;
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
- Jurisdiction Record Type is approved;
- Jurisdiction Class is valid;
- canonical jurisdiction name is identified;
- parent jurisdiction is valid where required;
- jurisdiction codes are formatted correctly where present;
- required references are present;
- required relationships are valid;
- Registry Status and Source-Record Status remain separate;
- version metadata is complete;
- the SREG Base Schema validates;
- the Jurisdiction Record-Type Profile validates;
- human-readable and machine-readable forms agree.

Registry validation does not establish governmental, legal, or geographic authority.

---

## Human-Readable Publication

The human-readable Jurisdiction SREG should communicate:

- Registry Identifier;
- title;
- Jurisdiction Class;
- Source Institution;
- Source-System Identifier;
- canonical jurisdiction name;
- alternate names;
- parent jurisdiction;
- jurisdiction codes;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- public references;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication

The machine-readable Jurisdiction SREG should preserve equivalent institutional meaning.

It may include:

- identifiers;
- controlled jurisdiction classifications;
- source references;
- status values;
- lifecycle values;
- version metadata;
- hierarchy relationships;
- typed relationships;
- jurisdiction codes;
- alternate names;
- dates;
- schema version;
- profile version;
- validation metadata.

---

## Publication Consistency

Official forms of the same Jurisdiction SREG must agree on:

- Registry Identifier;
- title;
- Record Type;
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

A record is not fully reconciled when official forms materially disagree.

---

## Historical Jurisdiction Tracking

Historical jurisdiction tracking may preserve:

- prior names;
- prior boundaries;
- predecessor jurisdictions;
- successor jurisdictions;
- prior parent jurisdictions;
- merger and split history;
- source versions;
- effective dates;
- historical maps or references;
- Chronicle relationships;
- archival evidence.

Historical tracking should distinguish documented source history from Registry interpretation.

---

## Future Development

Jurisdiction Records may expand to support:

- broader geographic hierarchies;
- regional classifications;
- municipality-level records;
- historical jurisdiction graphs;
- source confidence metadata;
- disputed-boundary source mapping;
- multilingual names;
- standardized geographic codes;
- Atlas interoperability enhancements;
- integrity references;
- certification and attestation relationships;
- machine-readable parent-child indexes.

Future development must preserve the established authority boundary:

```text
Atlas or another Source Institution creates the jurisdiction resource.
Registry creates the SREG.
```

---

## Registry Notes

Registry records and organizes jurisdiction information.

Registry does not independently:

- create jurisdictions;
- define legal boundaries;
- establish governmental authority;
- determine sovereignty;
- resolve territorial disputes;
- create ownership or legal rights;
- certify the jurisdiction;
- guarantee the continued availability of source resources.

Registration means the jurisdiction record has been cataloged.

It does not mean Registry legally recognizes or independently validates the jurisdiction.

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
- Atlas institutional documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When the Jurisdiction Record architecture changes:

- update this document;
- update the Jurisdiction Record-Type Profile;
- update schema enumerations;
- update validation rules;
- update examples;
- update Atlas integration documentation;
- review affected SREGs;
- reconcile human-readable and machine-readable publication;
- preserve prior versions;
- document material changes in the Registry Changelog.

---

## Guiding Principles

- Atlas or another approved Source Institution creates the jurisdiction resource.
- Registry creates the Jurisdiction SREG.
- The SREG is not the jurisdiction itself.
- The SREG is not the Atlas Source Record.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and source lifecycle remain distinct.
- Registry may report jurisdiction classifications but may not create governmental authority.
- Jurisdiction hierarchy must remain source-attributable.
- Versions should remain independently traceable.
- Relationships should be typed and directional.
- Human-readable and machine-readable forms should agree.
- Historical and superseded jurisdictions should remain discoverable.
- Registration does not itself establish legal recognition.

---

## Disclaimer

A Jurisdiction SREG is a Registry-owned catalog record.

It does not by itself create:

- a jurisdiction;
- sovereignty;
- governmental authority;
- legal boundaries;
- regulatory recognition;
- ownership;
- legal rights;
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
> Atlas preserves jurisdiction intelligence.
>
> Registry creates the SREG.
>
> The SREG preserves identity, hierarchy, relationships, versions, and the path back to the source.
