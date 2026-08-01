# Example Media Record

> **Example Status:** Illustrative only.  
> This document is not an official Satoshium Registry Entry, has not been assigned a production Registry Identifier, and has not been published as an operational SREG.

---

## Example Purpose

This example demonstrates how a media-related Authoritative Source Record may be represented within Satoshium Registry.

It is intended to illustrate:

- the SREG model;
- Registry Record Type assignment;
- Source Institution and Source Record separation;
- Registry Identifier and Source-System Identifier separation;
- Registry Status and Source-Record Status separation;
- media classification;
- public references;
- typed relationships;
- version metadata;
- lifecycle and correction expectations.

This example does not establish an authoritative Registry record for the New Hampshire Orientation Video.

---

## Constitutional Position

This example follows the Satoshium Suite implementation hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Institutional Implementation
  ↓
Example SREG
```

The example illustrates Registry implementation.

It does not create Registry authority, media ownership, certification, attestation, verification, endorsement, or publication rights.

---

## Canonical Operational Hierarchy

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Media Record Type
  ↓
Authoritative Media Source Record
```

Registry would create and maintain the SREG.

The Source Institution or media owner would remain authoritative for the underlying media resource, its publication status, its content, and its usage rights.

---

## Example Registry Entry

| Field | Example Value |
|---|---|
| Example Status | Illustrative only |
| Registry Record Type | Media |
| Proposed Registry Identifier | EXAMPLE-SREG-MED-US-NH-0001 |
| Title | New Hampshire Orientation Video |
| Source Institution | Example only; not assigned |
| Source-System Identifier | Example only; not assigned |
| Authoritative Source Record | Example public orientation video resource |
| Source-Record Version | Example only |
| Source-Record Status | Example: Published |
| Registry Status | Example: Active |
| Registry Lifecycle State | Example: Active |
| Registry Entry Version | 0.1.0-example |
| Schema Version | Example draft |
| Registration Date | Not registered |
| Last Updated | 2026-08-01 |
| Publication Status | Example only |

The identifier `EXAMPLE-SREG-MED-US-NH-0001` is a reserved illustrative value and must not be interpreted as an official Registry Identifier.

---

## Media Classification

```text
Media
└── Video
    └── Orientation
        └── New Hampshire
```

### Primary Registry Record Type

**Media**

### Media Type

**Video**

### Media Classification

**Orientation**

### Related Jurisdiction

**New Hampshire**

This classification is illustrative and should be validated against the applicable Media Record-Type Profile before operational use.

---

## Authoritative Source Record

The Authoritative Source Record for an operational Media SREG would be the actual published media resource or the canonical record maintained by the Source Institution.

An operational SREG should preserve:

- Source Institution;
- Source-System Identifier;
- canonical public location;
- media title;
- media type;
- source publication date;
- source-record version;
- source-record status;
- visibility;
- related jurisdiction;
- related Atlas, certification, Chronicle, Anchor, Beacon, Attestor, or Navigator records.

This example does not invent production values for those fields.

---

## Source Institution

The Source Institution is the institution, publisher, repository, or approved external source responsible for the media resource.

The Source Institution remains authoritative for:

- media content;
- publication status;
- source-record version;
- creator attribution;
- licensing;
- ownership;
- visibility;
- distribution rights;
- takedown or retirement decisions.

Registry may catalog these values but does not control them.

---

## Registry Identifier

An operational Media SREG would receive a stable Registry Identifier assigned by Satoshium Registry.

The Registry Identifier would identify the SREG itself.

It would not replace:

- the media platform identifier;
- the source repository identifier;
- the video identifier;
- the creator's publication identifier;
- another Source-System Identifier.

---

## Source-System Identifier

The Source-System Identifier would be assigned by the Source Institution or hosting platform.

Registry would preserve that identifier within the SREG.

The Source-System Identifier and Registry Identifier must remain distinct.

---

## Registry Status and Source-Record Status

Registry Status and Source-Record Status are separate values.

Example:

```text
Source-Record Status: Published
Registry Status: Active
```

A future source change could produce:

```text
Source-Record Status: Removed
Registry Status: Active
```

In that case, Registry could preserve the SREG as an active historical catalog entry while accurately reporting that the source media had been removed or was no longer publicly available.

---

## Public Availability

Public availability is source-controlled metadata.

Example:

**Visibility:** Public

Registry may report whether the Source Record is publicly available, restricted, unlisted, private, removed, or archived.

Registry does not control access to the underlying media merely by cataloging it.

---

## Lifecycle

An operational Media SREG may move through Registry lifecycle states such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

This example uses:

**Registry Lifecycle State:** Example: Active

This is illustrative only and does not indicate actual registration.

---

## Versions

An operational Media SREG should distinguish among:

- Registry specification version;
- SREG schema version;
- Media Record-Type Profile version;
- Registry Entry Version;
- Source-Record version;
- media edition or revision;
- applicable Suite Standards version.

For this example:

| Version Layer | Example Value |
|---|---|
| Registry Entry Version | 0.1.0-example |
| SREG Schema Version | Example draft |
| Media Profile Version | Example draft |
| Source-Record Version | Example only |

---

## Public References

An operational Media SREG may preserve references such as:

- canonical media URL;
- source media page;
- source repository;
- thumbnail;
- transcript;
- caption file;
- related jurisdiction page;
- Atlas page;
- Registry HTML entry;
- Registry JSON entry;
- related certification;
- Chronicle event;
- Anchor integrity reference.

Example references should not be substituted for official publication locations.

---

## Relationships

An operational Media SREG may include typed relationships such as:

### Source Relationship

```text
Media SREG → references → Authoritative Media Source Record
```

### Jurisdiction Relationship

```text
Media SREG → related to → New Hampshire Jurisdiction SREG
```

### Atlas Relationship

```text
Media SREG → related to → Atlas Jurisdiction Resource
```

### Certification Relationship

```text
Media SREG → referenced by → Certification Record
```

### Historical Relationship

```text
Media SREG → related to → Chronicle Publication Event
```

### Integrity Relationship

```text
Media SREG → anchored by → Anchor Integrity Reference
```

### Discovery Relationship

```text
Media SREG → discovered through → Beacon Discovery Signal
```

### Attestation Relationship

```text
Media SREG → attested by → Attestor Trust Statement
```

These relationships are illustrative and require approved relationship types before operational use.

---

## Related Suite Records

### Atlas

Atlas may reference the media resource as part of jurisdiction intelligence, evidence resources, or public orientation materials.

### Certifier

Certifier may reference the media resource as supporting evidence, contextual material, or part of a certification record.

Registry should preserve the distinction between:

- the media resource;
- the certification record;
- the certification outcome.

### Chronicle

Chronicle may preserve a publication milestone, release event, correction event, retirement event, or other historical occurrence related to the media.

### Anchor

Anchor may preserve hashes, timestamps, signatures, or integrity references related to the media or its metadata.

### Beacon

Beacon may publish discovery signals or metadata that help users locate the media resource.

### Attestor

Attestor may create trust statements or attestations related to the media resource.

### Navigator

Navigator may coordinate workflows involving media publication, certification, cataloging, discovery, or archival.

---

## Media Metadata

The following fields illustrate media-specific metadata that may appear in a Media Record-Type Profile.

| Field | Example Value |
|---|---|
| Media Title | New Hampshire Orientation Video |
| Media Type | Video |
| Media Classification | Orientation |
| Related Jurisdiction | New Hampshire |
| Visibility | Public |
| Source Institution | Example only |
| Source-Record Status | Example: Published |
| Registry Record Type | Media |
| Registry Status | Example: Active |

These values are illustrative and do not define the final machine-readable schema.

---

## Human-Readable Representation

A human-readable operational Media Registry Entry may include:

- title;
- Registry Identifier;
- Record Type;
- media type;
- Source Institution;
- source reference;
- visibility;
- Registry Status;
- Source-Record Status;
- version information;
- related jurisdiction;
- related records;
- lifecycle history;
- correction history;
- public references.

---

## Machine-Readable Representation

A machine-readable Media SREG may include:

- stable Registry Identifier;
- Record Type;
- source-system metadata;
- source reference;
- media classification;
- visibility;
- status values;
- versions;
- relationships;
- lifecycle metadata;
- public references;
- validation metadata.

The final field names and constraints must follow:

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

---

## Validation Expectations

Before an operational Media SREG is published, Registry should confirm:

- the Source Institution is identified;
- the Authoritative Source Record exists or is historically documented;
- the Source-System Identifier is preserved when available;
- the proposed Registry Identifier is valid;
- the Media Record Type is appropriate;
- media classification is valid;
- visibility is reported accurately;
- required public references exist;
- Registry Status and Source-Record Status are separate;
- version metadata is complete;
- relationships are structurally valid;
- the SREG satisfies the applicable schema;
- human-readable and machine-readable forms agree.

Registry validation does not certify the media content or grant publication rights.

---

## Correction Example

A future correction might address:

- a broken media URL;
- an incorrect title;
- a changed thumbnail;
- an incorrect media type;
- an incorrect related jurisdiction;
- an outdated Source-Record status;
- a missing relationship;
- schema nonconformance.

A material correction should preserve:

```text
Prior Example Version
  ↓
Documented Correction
  ↓
Replacement Example Version
```

For an operational SREG, correction history would be preserved under Registry policy and procedure.

---

## Source Removal or Unavailability

If the source media becomes unavailable, Registry should not automatically erase the SREG.

Registry may instead preserve:

- the prior source location;
- the last known Source-Record status;
- the date availability changed;
- related integrity references;
- Archive or Chronicle relationships;
- a new Registry Entry Version;
- appropriate lifecycle or archival history.

Registry preserves the record of the reference even when the source is no longer publicly available.

---

## Hosting and Custody

Registry does not necessarily host the media resource.

Registry may preserve:

- metadata;
- canonical source reference;
- public availability;
- integrity references;
- related records;
- historical context.

Hosting, custody, licensing, and distribution remain the responsibility of the Source Institution or rights holder unless expressly assigned elsewhere.

---

## Production Requirements

This example must not be converted directly into a production SREG without:

- confirming the Authoritative Source Record;
- identifying the actual Source Institution;
- obtaining the real Source-System Identifier;
- confirming publication and visibility status;
- assigning an official Registry Identifier;
- applying the published Media Record-Type Profile;
- validating required fields and relationships;
- confirming Registry and source status values;
- confirming media rights and source references where applicable;
- publishing consistent human-readable and machine-readable artifacts;
- completing the approved Registry registration procedure.

---

## Example Record Disclaimer

This file is an illustrative example.

It does not constitute:

- an official SREG;
- an authoritative media record;
- registration;
- certification;
- attestation;
- verification;
- ownership;
- copyright permission;
- publication authority;
- endorsement;
- affiliation.

The media resource, if it exists, remains controlled by its Source Institution or rights holder.

Registry would remain authoritative only for an officially created and published SREG.

---

## Guiding Statement

> Media may inform and educate.
>
> The Source Institution retains authority over the media.
>
> Registry creates the SREG that preserves the structured path back to it.
