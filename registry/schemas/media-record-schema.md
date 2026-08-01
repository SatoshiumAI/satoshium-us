# Media Record-Type Profile

## Overview

This document defines the Registry Record-Type Profile for Media Satoshium Registry Entries, or Media SREGs.

The profile extends the SREG Base Schema with the additional fields, controlled values, relationships, validation requirements, and publication rules needed to catalog authoritative media resources.

A Media SREG may catalog a video, image, thumbnail, audio resource, document, media page, composite media package, or another approved media artifact.

Registry catalogs the media resource.

Registry does not necessarily create, host, own, license, control, or verify the media.

---

## Constitutional Position

The Media Record-Type Profile operates within the following schema hierarchy:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Media Record-Type Profile
  ↓
Published Media SREG
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
- Registry Media Records documentation.

---

## Canonical Relationship

The canonical media relationship is:

```text
Source Institution
  ↓
Authoritative Media Resource
  ↓
Media SREG
```

The Source Institution or rights holder controls the Authoritative Media Resource.

Registry owns the SREG.

The SREG must preserve the path back to the source.

---

## Profile Purpose

A valid Media SREG should answer:

- What media resource is being referenced?
- Which institution created or published it?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the media?
- What Media Class applies?
- What format does the media use?
- What subject or resource is associated with it?
- Where is the canonical media resource located?
- What is the Source-Record Status?
- What is the Registry Status?
- What Registry Lifecycle State applies?
- What rights, license, visibility, or access information is known?
- Which versions apply?
- Which related records exist?
- How can the media remain discoverable over time?

---

## Base Schema Dependency

Every Media SREG must first satisfy the SREG Base Schema.

The Media Record-Type Profile adds media-specific fields and validation rules.

```text
SREG Base Schema
  +
Media Record-Type Profile
  =
Valid Media SREG
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
- Media Record-Type Profile version;
- registration date;
- last updated date.

The Source-System Identifier is required when the Source Institution or publishing platform provides one.

---

## Required Media Fields

### Registry Record Type

Required value:

```text
Media
```

---

### Media Class

The primary controlled classification assigned to the media resource.

Approved or potential values include:

```text
Video
Image
Thumbnail
Audio
Document
Media Page
Composite Media
```

Additional values require Registry governance approval and profile revision.

---

### Media Title

The human-readable title reported by the Source Institution or publisher.

Example:

```text
New Hampshire Orientation Video
```

Registry may reproduce this value.

Registry should not silently replace a source title with an invented title.

---

### Source Institution

The institution responsible for the Authoritative Media Resource.

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
- an approved external publisher, archive, repository, platform, or rights holder.

---

### Authoritative Source Record

A durable reference to the authoritative media resource.

Examples may include:

- video page;
- direct media file;
- image page;
- audio page;
- PDF;
- media landing page;
- repository resource;
- publication page;
- archived media reference;
- another approved media artifact.

---

### Registry Status

The operational status of the SREG.

This field is controlled by Registry.

It must remain separate from Source-Record Status, publication status, visibility, licensing status, and platform availability.

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

Required when the Source Institution or platform provides a stable identifier.

Examples may include:

```text
ATLAS-MEDIA-US-NH-001
YOUTUBE-VIDEO-ID
MEDIA-ASSET-0001
```

The Source-System Identifier must remain distinct from the Registry Identifier.

---

### Media Format

Required when the technical format is known and relevant.

Examples may include:

```text
MP4
WEBM
PNG
JPEG
SVG
MP3
WAV
PDF
HTML
```

The value should identify the actual media format rather than merely repeat the Media Class.

---

### Associated Resource

Required when the media exists primarily to document, explain, depict, or support another resource.

Examples may include:

- Atlas resource;
- jurisdiction;
- certification;
- attestation;
- tool;
- signal;
- historical event;
- workflow;
- integrity reference.

The associated resource should preferably reference another SREG or an attributable Source Record.

---

### Source-Record Status

Required when the Source Institution exposes a meaningful source-controlled status.

Examples may include:

```text
Draft
Published
Private
Restricted
Removed
Superseded
Archived
Withdrawn
```

This field is controlled by the Source Institution or platform.

---

## Optional Media Fields

### Description

A source-attributable summary of the media resource.

Example:

```text
Orientation video introducing New Hampshire jurisdiction resources.
```

Registry descriptions should not introduce unsupported claims.

---

### Media Subject

The principal subject represented by the media.

Examples may include:

- jurisdiction;
- Suite institution;
- certification;
- historical event;
- technical concept;
- evidence package;
- workflow.

---

### Publisher or Platform

The publisher, repository, or delivery platform.

Examples may include:

- Satoshium;
- YouTube;
- GitHub;
- Internet Archive;
- external institutional website.

---

### Publication Date

The date the Source Institution or platform published the media.

This date must remain distinct from Registry registration and update dates.

---

### Language

The primary language or languages of the media.

A controlled language code should be used when practical.

---

### Duration

Applicable to time-based media such as video and audio.

A standardized duration format should be used.

---

### Dimensions

Applicable to visual media.

May include:

- pixel width;
- pixel height;
- aspect ratio;
- page dimensions.

---

### File Size

The known file size of the media artifact.

This value should identify units explicitly.

---

### Visibility

May include:

```text
Public
Unlisted
Private
Restricted
Internal
Archived
```

Visibility is source-controlled context.

It is not Registry Status.

---

### Access Designation

May describe:

- open access;
- membership access;
- authenticated access;
- institutional access;
- restricted access;
- unavailable access.

Registry must not bypass access controls.

---

### Rights or Licensing Reference

May identify:

- copyright holder;
- license;
- usage terms;
- public-domain declaration;
- attribution requirements;
- reuse restrictions;
- platform terms.

Absence of a rights field does not imply unrestricted reuse.

---

### Transcript or Caption Reference

May identify:

- transcript;
- subtitles;
- closed captions;
- audio description;
- accessibility notes.

---

### Thumbnail Reference

May identify a related thumbnail Media SREG or Source Record.

---

### Derivative References

May identify:

- resized image;
- clipped video;
- compressed copy;
- translated version;
- transcript;
- audio extraction;
- preview;
- derivative publication.

A derivative should not be represented as the original media object.

---

### Integrity References

May include:

- cryptographic hash;
- checksum;
- Anchor record;
- timestamp;
- file manifest;
- preservation package;
- archived snapshot.

---

### Public References

May include:

- canonical media page;
- direct media file;
- repository path;
- related Atlas page;
- Certification Record;
- Attestation Record;
- Chronicle event;
- Beacon signal;
- Anchor reference;
- archival location.

---

### Notes

May preserve additional Registry context needed for interpretation.

Notes must not replace structured fields when a structured field is available.

---

## Identifier Requirements

A Media SREG must preserve identifier domains separately.

### Registry Identifier

Assigned by Registry.

Example:

```text
SREG-MED-US-NH-0001
```

### Source-System Identifier

Assigned by the Source Institution or platform.

Example:

```text
ATLAS-MEDIA-US-NH-001
```

### Platform Identifier

Assigned by an external media platform.

Example:

```text
YouTube Video ID
```

### Integrity Reference Identifier

Assigned by Anchor or another integrity system.

Identifiers may be related.

They must not be collapsed into one field.

---

## Relationship Requirements

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
Media SREG
  → documents
  → Historical Event SREG
```

```text
Media SREG
  → anchored by
  → Integrity Reference
```

```text
Media SREG
  → derivative of
  → Media SREG
```

Relationships must use approved Registry relationship types.

---

## Relationship Object Structure

A media relationship may include:

```text
Relationship Type
Source Identifier
Target Identifier
Direction
Target Institution
Effective Date
Status
Version Context
Supporting Reference
```

Derivative and thumbnail relationships should clearly identify which object is original and which is derived.

---

## Status Separation

A Media SREG must distinguish:

```text
Registry Status
  ≠
Source-Record Status
  ≠
Visibility
  ≠
Access Designation
  ≠
Licensing Status
  ≠
Platform Availability
```

Example:

```text
Source-Record Status: Removed
Visibility: Unavailable
Registry Status: Active
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for media that is no longer publicly available.

---

## Version Requirements

A Media SREG should preserve:

- Registry Entry Version;
- Source-Record Version;
- media file version, when available;
- SREG Base Schema version;
- Media Record-Type Profile version;
- Registry Schema Specification version, when required;
- Suite Standards version, when required;
- Suite Methodology version, when required.

A schema migration does not automatically mean the media changed.

A source media revision does not automatically require a new profile version.

---

## Core Record Structure

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
Publisher or Platform
Publication Date
Language
Duration
Dimensions
File Size
Visibility
Access Designation
Rights or Licensing Reference
Transcript or Caption Reference
Thumbnail Reference
Derivative References
Integrity References
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
SREG Base Schema Version
Media Profile Version
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
| Registry Identifier | SREG-MED-US-NH-0001 |
| Title | New Hampshire Orientation Video |
| Registry Record Type | Media |
| Media Class | Video |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | ATLAS-MEDIA-US-NH-001 |
| Media Format | MP4 |
| Associated Resource | New Hampshire Atlas Resource |
| Publisher or Platform | Satoshium |
| Source-Record Status | Published |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |
| SREG Base Schema Version | 1.0.0 |
| Media Profile Version | 1.0.0 |

This example is illustrative.

It does not establish final production identifiers or controlled values.

---

## Example Machine-Readable Structure

```json
{
  "registry_identifier": "SREG-MED-US-NH-0001",
  "title": "New Hampshire Orientation Video",
  "registry_record_type": "Media",
  "media_class": "Video",
  "source_institution": "Satoshium Atlas",
  "source_system_identifier": "ATLAS-MEDIA-US-NH-001",
  "authoritative_source_record": {
    "reference": "https://example.invalid/atlas/us/new-hampshire/media/orientation/"
  },
  "media_format": "MP4",
  "media_subject": "New Hampshire jurisdiction resource",
  "associated_resource": {
    "registry_identifier": "SREG-JUR-US-NH-0001"
  },
  "publisher_or_platform": "Satoshium",
  "publication_date": "2026-08-01",
  "language": "en",
  "visibility": "Public",
  "rights_or_licensing_reference": null,
  "source_record_status": "Published",
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

A valid Media SREG should satisfy the following checks.

### Identity Validation

- Registry Identifier is present and valid.
- Title is present.
- Registry Record Type equals `Media`.
- Media Class is approved.

### Source Validation

- Source Institution is present.
- Authoritative Source Record is present.
- Source-System Identifier is preserved when available.
- source attribution is internally consistent.

### Media Validation

- Media Format is present when known and required.
- Associated Resource is present when required.
- Media Class and format are not conflated.
- publication date is attributable.
- visibility and access fields use approved values.
- rights information is not misrepresented.

### Status Validation

- Registry Status is valid.
- Registry Lifecycle State is valid.
- Source-Record Status is not conflated with Registry Status.
- visibility is not represented as Registry Status.
- availability is not represented as Registry Lifecycle State.

### Version Validation

- Registry Entry Version is present.
- SREG Base Schema version is present.
- Media Record-Type Profile version is present.
- Source-Record Version is preserved when available.

### Relationship Validation

- relationship types are approved;
- direction is valid;
- referenced targets exist or are historically documented;
- derivative relationships distinguish original and derivative media;
- duplicate relationships are avoided;
- required supporting references are present.

### Publication Validation

- human-readable and machine-readable forms agree materially;
- canonical references are valid where available;
- dates use approved formats;
- rights and access information are represented consistently;
- required fields are public unless a documented restriction applies.

---

## Invalid Conditions

A Media SREG should fail validation when:

- the Source Institution is unidentified;
- the Source Record cannot be identified;
- Media Class is unapproved;
- Registry and source identifiers are conflated;
- the SREG implies ownership or licensing without support;
- visibility is used as Registry Status;
- the media format conflicts with the Source Record;
- a derivative is represented as the original;
- required versions are missing;
- official publication forms materially disagree.

---

## Media Replacement and Supersession

A Media SREG may be superseded when:

- a distinct replacement media resource exists;
- a new Registry Identifier is required;
- the original source object is replaced;
- the prior media becomes a historical object;
- a materially different artifact replaces it.

A routine revision of the same media resource may be handled as an update when source identity remains stable.

The superseded SREG should remain discoverable.

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
- successor media;
- related Chronicle events;
- historical context.

Registry must not bypass access controls or republish content without authority.

---

## Rights and Licensing

A Media SREG may report available rights and licensing information.

Registry does not independently grant rights.

The profile must not infer that media is free to use merely because:

- it is publicly accessible;
- no license is listed;
- Registry catalogs it;
- a copy exists in an archive;
- a platform permits viewing.

Rights remain controlled by the rights holder, Source Institution, publisher, platform, or applicable law.

---

## Integrity and Preservation

A Media SREG may reference:

- cryptographic hashes;
- checksums;
- timestamps;
- Anchor records;
- archived copies;
- preservation packages;
- file manifests;
- version manifests.

Integrity references remain distinct from Registry validation.

Registry validation confirms SREG structure.

An integrity reference addresses the referenced media artifact.

---

## Supersession

A Media SREG may be superseded when:

- a distinct successor media object replaces it;
- the Source Record changes identity materially;
- a new Registry Identifier is required;
- the original classification no longer accurately represents the source;
- governance requires a replacement SREG.

A superseded SREG should remain discoverable and reference its successor.

---

## Revocation

Registry may revoke a Media SREG when:

- registration was invalid;
- the Source Institution was materially misidentified;
- the Source Record did not support the represented media object;
- the SREG materially misrepresented ownership, rights, or source identity;
- governance requires withdrawal.

Registry revocation does not remove the underlying media from the Source Institution or platform.

---

## Archival

An archived Media SREG should preserve:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- title;
- Media Class;
- format;
- associated resources;
- rights and access context;
- integrity references;
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

The human-readable Media SREG should present:

- Registry Identifier;
- title;
- Media Class;
- Source Institution;
- Source-System Identifier;
- media format;
- media subject;
- associated resource;
- publisher or platform;
- publication date;
- language;
- visibility;
- access designation;
- rights or licensing reference;
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

The machine-readable Media SREG should preserve equivalent institutional meaning.

It should represent:

- identifiers;
- controlled classifications;
- source references;
- technical media metadata;
- status domains;
- lifecycle;
- versions;
- typed relationships;
- rights and access metadata;
- integrity references;
- dates;
- validation metadata.

---

## Publication Consistency

Official forms of the same Media SREG must agree on:

- Registry Identifier;
- title;
- Registry Record Type;
- Media Class;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- media format;
- associated resource;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- rights and access references;
- public references;
- relationships;
- dates.

A Media SREG is not fully reconciled when official forms materially disagree.

---

## Profile Versioning

Every published Media Record-Type Profile should include:

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
- Media Classes change;
- rights or access fields change;
- relationship rules change;
- integrity requirements change;
- publication formats change;
- validation failures reveal ambiguity;
- Source Institution integration changes.

Material changes should be versioned and documented in the Registry Changelog.

---

## Relationship to Other Documentation

This profile should remain consistent with:

- Registry Schemas;
- Registry Schema Specification;
- SREG Base Schema;
- Registry Entry Model;
- Registry Record Types;
- Registry Media Records;
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
- update controlled Media Classes;
- update rights and access fields;
- update relationship rules;
- update examples;
- review affected Media SREGs;
- preserve prior profile versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication.

---

## Guiding Principles

- The SREG Base Schema provides shared Registry structure.
- This profile adds media-specific requirements.
- The Source Institution controls the media resource.
- Registry owns the Media SREG.
- The SREG is not the media itself.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status, Source-Record Status, visibility, and access remain distinct.
- Versions remain independently traceable.
- Relationships are typed and attributable.
- Rights information must not be inferred.
- Validation confirms structure, not ownership, authenticity, or permission to reuse.
- Human-readable and machine-readable forms must agree.
- Removed and superseded media should remain historically discoverable where appropriate.
- Registration does not establish ownership, licensing, authenticity, or endorsement.

---

## Disclaimer

This profile defines the structure of a Registry-owned Media SREG.

It does not by itself create:

- ownership;
- copyright;
- a license;
- permission to reuse;
- authenticity;
- certification;
- attestation;
- verification;
- endorsement;
- legal rights;
- regulatory approval;
- affiliation;
- Source Institution authority.

Those remain controlled by the Source Institution, publisher, platform, rights holder, Source Record, governing authority, or applicable law.

---

## Guiding Statement

> Media communicates information.
>
> The Source Institution preserves the authoritative media resource.
>
> The SREG preserves Registry context.
>
> The profile preserves structure.
