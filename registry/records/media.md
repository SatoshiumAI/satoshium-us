# Registry Media Records

## Overview

This document defines how Media Records are represented within Satoshium Registry.

A Media Record is a Satoshium Registry Entry, or SREG, that catalogs an Authoritative Source Record for a video, image, graphic, thumbnail, audio resource, document, media page, or other approved media artifact.

Registry catalogs the media resource.

Registry does not necessarily create, host, own, license, or control the media.

---

## Constitutional Position

Media Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Source Institution Media Implementation
  ↓
Authoritative Media Resource
  ↓
Registry Media SREG
```

A Satoshium Suite institution or approved external institution creates and maintains the Authoritative Media Resource.

Registry creates and maintains the SREG that identifies, classifies, references, relates, versions, and preserves discoverability of that source resource.

---

## Canonical Relationship

The canonical relationship is:

```text
Source Institution
  ↓
Authoritative Media Resource
  ↓
Registry Media SREG
```

This relationship preserves institutional separation:

- the Source Institution owns or controls the media record;
- Registry owns the SREG;
- the SREG points back to the Authoritative Source Record;
- Registry does not absorb source authority, ownership, or licensing.

---

## Purpose

Media Records exist to improve:

- discoverability;
- source attribution;
- media classification;
- public reference management;
- relationship mapping;
- version awareness;
- lifecycle visibility;
- preservation context;
- machine-readable interoperability;
- historical continuity.

A Registry Media SREG should help answer:

- What media resource exists?
- Which institution created or published it?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the media?
- What Media Class applies?
- Where is the canonical media resource located?
- What tool, jurisdiction, certification, attestation, signal, or event is associated with it?
- What is the Source-Record Status?
- What is the Registry Status?
- Which versions apply?
- What rights, visibility, or access information is known?
- How can the media be found later?

---

## Record Type

The primary Registry Record Type is:

```text
Media
```

Every operational Media SREG must use the approved Media Record-Type Profile.

The profile may define:

- required fields;
- optional fields;
- controlled media classes;
- format requirements;
- required relationships;
- permitted relationships;
- source-reference requirements;
- rights and access fields;
- status requirements;
- lifecycle requirements;
- validation rules;
- publication requirements.

---

## Source Institutions

Media Records may originate from:

- Atlas;
- Certifier;
- Registry;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- another approved Satoshium Suite institution;
- an approved external publisher, archive, repository, platform, or rights holder.

The Source Institution must be identified separately from Registry.

---

## Authoritative Source Record

Every Media SREG must identify the Authoritative Source Record being cataloged.

The Source Record may include:

- video;
- image;
- illustration;
- diagram;
- thumbnail;
- audio recording;
- transcript;
- PDF;
- publication;
- report;
- media page;
- orientation page;
- resource hub;
- media collection;
- another approved media artifact.

The SREG should preserve the canonical source location whenever available.

---

## Registry Identifier and Source-System Identifier

A Media SREG must preserve distinct identifiers.

### Registry Identifier

Assigned by Satoshium Registry.

Identifies the SREG.

### Source-System Identifier

Assigned by the Source Institution or publishing platform.

Identifies the Authoritative Media Resource.

Example:

```text
Registry Identifier: SREG-MED-0001
Source-System Identifier: ATLAS-MEDIA-US-CA-001
```

The Registry Identifier must not replace, alter, or overwrite the Source-System Identifier.

When no source identifier exists, the absence should be documented rather than replaced with an invented source identifier.

---

## Media Classes

Controlled Media Classes may include:

### Video

Examples include:

- orientation videos;
- educational videos;
- demonstrations;
- project updates;
- interviews;
- historical recordings;
- certification explainers.

### Image

Examples include:

- photographs;
- graphics;
- illustrations;
- diagrams;
- maps;
- visual assets.

### Thumbnail

Examples include:

- video thumbnails;
- preview images;
- social media images;
- catalog previews.

### Audio

Examples include:

- podcasts;
- recordings;
- audio briefings;
- interviews;
- narrated materials.

### Document

Examples include:

- PDFs;
- reports;
- publications;
- transcripts;
- reference materials;
- presentation exports.

### Media Page

Examples include:

- landing pages;
- orientation pages;
- media collections;
- galleries;
- resource hubs.

### Composite Media

A coordinated media package containing multiple approved media forms.

Additional classes require approval through Registry governance.

---

## Required SREG Elements

An operational Media SREG should include:

### Identity

- Registry Identifier;
- title;
- Registry Record Type;
- Media Class.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier, when available;
- canonical source reference;
- publisher or platform, when applicable.

### Media Context

- media format;
- media subject;
- associated resource;
- publication date;
- language;
- visibility or access designation;
- rights or licensing reference, when available;
- Source-Record Status.

### Registry Context

- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG schema version;
- Media Record-Type Profile version;
- registration date;
- last updated date.

### Relationships

- related Tool SREGs;
- related Jurisdiction SREGs;
- related Certification SREGs;
- related Attestation SREGs;
- related Signal SREGs;
- related Historical Event SREGs;
- related integrity references;
- related workflows;
- related Media SREGs.

---

## Example Record Structure

```text
Registry Identifier
Title
Registry Record Type
Media Class
Source Institution
Source-System Identifier
Authoritative Source Record
Media Format
Media Subject
Associated Resource
Canonical Source Reference
Publisher or Platform
Publication Date
Language
Visibility
Rights or Licensing Reference
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

The authoritative field definitions belong to the Registry Schema Specification and Media Record-Type Profile.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-MED-0001 |
| Registry Record Type | Media |
| Media Class | Video |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | ATLAS-MEDIA-US-CA-001 |
| Associated Resource | California Atlas Resource |
| Media Format | MP4 |
| Source-Record Status | Published |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |

This example is illustrative and does not establish final production identifiers or controlled values.

---

## Authority Boundary

### Source Institution Authority

The Source Institution or rights holder remains authoritative for:

- media content;
- Source-System Identifier;
- source title;
- source description;
- publication status;
- source version;
- hosting;
- visibility;
- access controls;
- ownership;
- licensing;
- copyright;
- takedown or removal decisions.

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

Registry may report source-controlled media values.

Registry does not redefine ownership, licensing, or publication authority.

---

## Related Registry Records

A Media SREG may relate to:

- Tool SREGs;
- Jurisdiction SREGs;
- Certification SREGs;
- Attestation SREGs;
- Signal SREGs;
- Historical Event SREGs;
- Integrity Reference SREGs;
- Workflow records;
- other Media SREGs.

Examples:

```text
Tool SREG
  → publishes
  → Media SREG
```

```text
Media SREG
  → depicts
  → Jurisdiction SREG
```

```text
Media SREG
  → explains
  → Certification SREG
```

```text
Signal SREG
  → discovers
  → Media SREG
```

```text
Media SREG
  → anchored by
  → Integrity Reference
```

Relationships must use approved types and preserve direction where applicable.

---

## Media Record Workflow

Registry should create a Media SREG through the following process:

```text
Media Source Record Identified
  ↓
Source Institution Confirmed
  ↓
Source Authority and Rights Context Confirmed
  ↓
Registrability Determined
  ↓
Media Record Type Assigned
  ↓
Media Class Assigned
  ↓
Registry Identifier Assigned
  ↓
Source-System Identifier Preserved
  ↓
References and Relationships Established
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

A Media SREG may move through approved Registry Lifecycle States such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states describe the SREG.

They do not replace the publication, visibility, licensing, or availability status of the Authoritative Media Resource.

Example:

```text
Source-Record Status: Removed
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for media that is no longer publicly available.

---

## Updates

A Media SREG may be updated when:

- the Source Institution publishes a new media version;
- the canonical media location changes;
- visibility or access changes;
- Source-Record Status changes;
- rights or licensing information changes;
- captions or transcripts become available;
- public references expand;
- relationships evolve;
- Registry metadata improves;
- schema migration occurs;
- the Media Record-Type Profile changes.

Updates must preserve the distinction between source-controlled and Registry-controlled changes.

---

## Corrections

A Registry correction may be required when Registry incorrectly records:

- Source Institution;
- Source-System Identifier;
- canonical source URL;
- Media Class;
- format;
- associated resource;
- publication date;
- rights reference;
- Registry Status;
- relationship target;
- version metadata;
- publication data.

Registry may correct its representation of source-controlled values.

Registry may not alter the media itself through a Registry correction.

---

## Media Replacement and Supersession

A Media SREG may be superseded when:

- a distinct replacement media resource exists;
- a new Registry Identifier is required;
- the original source object is replaced;
- the prior media becomes a historical version;
- a substantially different media artifact replaces it.

The prior SREG should remain discoverable and reference its successor.

A routine revision of the same source media may be handled as an update when source identity remains stable.

---

## Removal or Unavailability

A media resource may become:

- removed;
- private;
- restricted;
- relocated;
- unavailable;
- deleted by the platform;
- withdrawn by the rights holder;
- superseded.

Source unavailability does not automatically require deletion of the SREG.

Registry may preserve:

- last known canonical location;
- last known Source-Record Status;
- date availability changed;
- archived references;
- integrity references;
- related Chronicle events;
- successor media;
- historical context.

Registry must not bypass access restrictions or republish content without authority.

---

## Rights, Licensing, and Access

A Media SREG may report available rights and access information.

Possible fields may include:

- copyright holder;
- license;
- usage terms;
- public-domain status;
- access designation;
- platform restrictions;
- archival permissions;
- attribution requirements.

Registry does not independently grant rights.

Absence of a rights field does not imply that the media is free to use.

---

## Integrity and Preservation

Media Records may reference:

- cryptographic hashes;
- timestamps;
- Anchor records;
- archived copies;
- preservation packages;
- file manifests;
- media checksums;
- version manifests.

Integrity references should remain distinguishable from Registry validation.

Registry validation confirms SREG structure.

An integrity reference addresses the referenced media artifact.

---

## Validation Requirements

Before publication, Registry should confirm:

- Source Institution is identified;
- Authoritative Media Resource exists or is historically documented;
- Registry Identifier is valid;
- Source-System Identifier is preserved when available;
- Media Record Type is approved;
- Media Class is valid;
- canonical source reference is present where available;
- media format is recorded where known;
- associated resource is identified where required;
- rights and access information is not misrepresented;
- required references are present;
- required relationships are valid;
- Registry Status and Source-Record Status remain separate;
- version metadata is complete;
- the SREG Base Schema validates;
- the Media Record-Type Profile validates;
- human-readable and machine-readable forms agree.

Registry validation does not establish ownership, authenticity, or permission to reuse the media.

---

## Human-Readable Publication

The human-readable Media SREG should communicate:

- Registry Identifier;
- title;
- Media Class;
- Source Institution;
- Source-System Identifier;
- media subject;
- associated resource;
- media format;
- canonical source reference;
- publisher or platform;
- publication date;
- visibility;
- rights or licensing reference;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication

The machine-readable Media SREG should preserve equivalent institutional meaning.

It may include:

- identifiers;
- controlled media classifications;
- formats;
- source references;
- status values;
- lifecycle values;
- version metadata;
- typed relationships;
- publication dates;
- language;
- visibility;
- rights references;
- integrity references;
- schema version;
- profile version;
- validation metadata.

---

## Publication Consistency

Official forms of the same Media SREG must agree on:

- Registry Identifier;
- title;
- Record Type;
- Media Class;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- associated resource;
- canonical source reference;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- references;
- relationships;
- dates.

A record is not fully reconciled when official forms materially disagree.

---

## Future Development

Media Records may expand to support:

- richer media metadata;
- duration and dimensions;
- codecs and technical formats;
- multilingual titles and descriptions;
- transcripts and caption references;
- media collections;
- derivative relationships;
- thumbnail relationships;
- accessibility metadata;
- preservation manifests;
- integrity anchors;
- certification relationships;
- attestation relationships;
- automated reference monitoring;
- machine-readable rights statements.

Future development must preserve the established authority boundary:

```text
The Source Institution creates or publishes the media resource.
Registry creates the SREG.
```

---

## Registry Notes

Registry records and organizes information about media resources.

Registry does not independently:

- create the media;
- own the media;
- host the media;
- grant a license;
- waive copyright;
- verify all media claims;
- guarantee authenticity;
- guarantee continued availability;
- bypass access controls;
- certify or attest to the media merely by registration.

Registration means the media record has been cataloged.

It does not mean Registry endorses the media or authorizes its reuse.

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

When the Media Record architecture changes:

- update this document;
- update the Media Record-Type Profile;
- update schema enumerations;
- update validation rules;
- update examples;
- update Source Institution integration documentation;
- review affected SREGs;
- reconcile human-readable and machine-readable publication;
- preserve prior versions;
- document material changes in the Registry Changelog.

---

## Guiding Principles

- The Source Institution creates or publishes the media resource.
- Registry creates the Media SREG.
- The SREG is not the media resource.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and source lifecycle remain distinct.
- Registry may report rights information but does not grant rights.
- Media relationships should be typed and attributable.
- Versions should remain independently traceable.
- Human-readable and machine-readable forms should agree.
- Removed or superseded media should remain historically discoverable where appropriate.
- Registration does not itself establish authenticity, ownership, licensing, or endorsement.

---

## Disclaimer

A Media SREG is a Registry-owned catalog record.

It does not by itself create:

- ownership;
- copyright;
- a license;
- permission to reuse;
- authenticity;
- certification;
- attestation;
- endorsement;
- legal rights;
- regulatory approval;
- affiliation;
- Source Institution authority.

Those remain controlled by the Source Institution, publisher, platform, rights holder, Source Record, or applicable external authority.

---

## Guiding Statement

> Media communicates information.
>
> The Source Institution preserves the authoritative resource.
>
> Registry creates the SREG.
>
> The SREG preserves identity, context, relationships, versions, and the path back to the media.
