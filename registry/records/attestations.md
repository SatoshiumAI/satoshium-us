# Registry Attestation Records

## Overview

This document defines how Attestation Records are represented within Satoshium Registry.

An Attestation Record is a Satoshium Registry Entry, or SREG, that catalogs an Authoritative Source Record created by Satoshium Attestor or another approved attestation-producing institution.

Registry catalogs the attestation.

Registry does not perform the attestation.

---

## Constitutional Position

Attestation Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Attestor Institutional Implementation
  ↓
Authoritative Attestation Record
  ↓
Registry Attestation SREG
```

Attestor creates the attestation and retains authority over its meaning, conclusion, evidence basis, and status.

Registry creates and maintains the SREG that identifies, classifies, references, relates, versions, and preserves discoverability of that attestation record.

---

## Canonical Relationship

The canonical relationship is:

```text
Attestor
  ↓
Authoritative Attestation Record
  ↓
Registry Attestation SREG
```

This relationship preserves institutional separation:

- Attestor owns the attestation;
- Registry owns the SREG;
- the SREG points back to the Authoritative Source Record;
- Registry does not absorb Attestor authority.

---

## Purpose

Attestation Records exist to improve:

- discoverability;
- source attribution;
- version awareness;
- relationship mapping;
- lifecycle visibility;
- public reference management;
- historical continuity;
- machine-readable interoperability.

A Registry Attestation SREG should help answer:

- What attestation exists?
- Which institution created it?
- What Source-System Identifier identifies it?
- What Registry Identifier identifies the SREG?
- What was attested?
- What attestation type applies?
- What is the Source-Record Status?
- What is the Registry Status?
- Which versions apply?
- What evidence or supporting records are referenced?
- What related certifications, tools, jurisdictions, media, or integrity references exist?
- Where can the Authoritative Source Record be found?

---

## Record Type

The primary Registry Record Type is:

```text
Attestation
```

Every operational Attestation SREG must use the approved Attestation Record-Type Profile.

The profile may define:

- required fields;
- optional fields;
- controlled attestation classifications;
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
Satoshium Attestor
```

An approved external attestation-producing institution may also serve as the Source Institution when permitted by Registry governance.

The Source Institution field must remain distinct from Registry.

---

## Authoritative Source Record

Every Attestation SREG must identify the Authoritative Source Record being cataloged.

The source record may include:

- attestation statement;
- trust statement;
- validation report;
- verification record;
- integrity confirmation;
- evidence attestation;
- certification-related attestation;
- historical attestation;
- another approved attestation artifact.

The SREG must preserve a durable source reference whenever available.

---

## Registry Identifier and Source-System Identifier

An Attestation SREG must preserve two distinct identifiers when the source provides its own identifier.

### Registry Identifier

Assigned by Satoshium Registry.

Identifies the SREG.

### Source-System Identifier

Assigned by Attestor or the originating institution.

Identifies the Authoritative Attestation Record.

Example:

```text
Registry Identifier: SREG-ATT-0001
Source-System Identifier: SATTEST-2026-0001
```

The Registry Identifier must not replace or overwrite the Source-System Identifier.

---

## Potential Attestation Classifications

Controlled Attestation classifications may include:

### Verification Attestation

Addresses whether specified information, records, claims, or resources satisfy defined verification conditions.

### Integrity Attestation

Addresses whether a referenced resource, artifact, package, or record remains consistent with an expected integrity reference.

### Evidence Attestation

Addresses the existence, relationship, provenance, or reviewed condition of evidence and supporting materials.

### Certification Attestation

Addresses an independent trust statement associated with a certification artifact or certification process.

### Historical Attestation

Addresses a significant historical event, milestone, publication, or preserved institutional state.

### Identity or Authority Attestation

Addresses a declared identity, role, authority, or institutional relationship when supported by the applicable Attestor method.

Additional classifications require approval through Attestor and Registry governance as applicable.

---

## Required SREG Elements

An operational Attestation SREG should include:

### Identity

- Registry Identifier;
- title;
- Registry Record Type;
- Attestation classification.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier;
- canonical source reference.

### Attestation Context

- attested subject or resource;
- attestation statement or summary;
- attestation date;
- applicable evidence references;
- applicable method or standard reference;
- Attestor-controlled status.

### Registry Context

- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG schema version;
- Attestation Record-Type Profile version;
- registration date;
- last updated date.

### Relationships

- related SREGs;
- related Source Records;
- related certifications;
- related evidence;
- related integrity references;
- related historical events;
- related tools or jurisdictions.

---

## Example Record Structure

```text
Registry Identifier
Title
Registry Record Type
Attestation Classification
Source Institution
Source-System Identifier
Authoritative Source Record
Attested Subject
Attestation Statement
Attestation Date
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Source-Record Version
Schema Version
Profile Version
Evidence References
Public References
Relationships
Registration Date
Last Updated
```

The authoritative field definitions belong to the Registry Schema Specification and Attestation Record-Type Profile.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-ATT-0001 |
| Registry Record Type | Attestation |
| Attestation Classification | Integrity Attestation |
| Source Institution | Satoshium Attestor |
| Source-System Identifier | SATTEST-2026-0001 |
| Source-Record Status | Active |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Attested Subject | Certification Package |
| Attestation Date | 2026-08-01 |
| Registry Entry Version | 1.0.0 |

This example is illustrative and does not establish final production identifiers or controlled values.

---

## Authority Boundary

### Attestor Authority

Attestor remains authoritative for:

- attestation statement;
- attestation conclusion;
- attestation type or classification;
- evidence interpretation;
- verification method;
- Source-System Identifier;
- Source-Record Status;
- Source-Record version;
- issuance, update, revocation, or retirement of the attestation.

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

Registry may report Attestor-controlled values.

Registry does not redefine them.

---

## Related Registry Records

An Attestation SREG may relate to:

- Tool SREGs;
- Jurisdiction SREGs;
- Media SREGs;
- Certification SREGs;
- Signal SREGs;
- Historical Event SREGs;
- Integrity Reference SREGs;
- Evidence records;
- Workflow records;
- other Attestation SREGs.

Relationships should use approved typed relationships.

Examples:

```text
Attestation SREG
  → attests to
  → Certification SREG
```

```text
Attestation SREG
  → supported by
  → Evidence Record
```

```text
Attestation SREG
  → anchored by
  → Integrity Reference
```

```text
Attestation SREG
  → concerns
  → Jurisdiction SREG
```

---

## Attestation Record Workflow

Registry should create an Attestation SREG through the following process:

```text
Attestation Source Record Identified
  ↓
Source Institution Confirmed
  ↓
Source Authority Confirmed
  ↓
Registrability Determined
  ↓
Attestation Record Type Assigned
  ↓
Registry Identifier Assigned
  ↓
Source References and Relationships Established
  ↓
SREG Constructed
  ↓
Schema and Profile Validated
  ↓
Human-Readable and Machine-Readable Forms Reconciled
  ↓
Published
  ↓
Lifecycle, Versions, Updates, and History Maintained
```

---

## Lifecycle

An Attestation SREG may move through approved Registry Lifecycle States such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states describe the SREG.

They do not replace the lifecycle or status of the Authoritative Attestation Record.

Example:

```text
Source-Record Status: Revoked
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for a source attestation that Attestor has revoked.

---

## Updates

An Attestation SREG may be updated when:

- Attestor publishes a new source version;
- Source-Record Status changes;
- new evidence references become available;
- public references change;
- relationships evolve;
- Registry metadata improves;
- schema migration occurs;
- the Record-Type Profile changes.

Updates must preserve the distinction between source-controlled changes and Registry-controlled changes.

---

## Corrections

A correction may be required when Registry incorrectly records:

- Source Institution;
- Source-System Identifier;
- source URL;
- Attestation classification;
- Registry Status;
- relationship target;
- version metadata;
- publication data.

Registry may correct Registry-owned errors.

Registry may not rewrite Attestor's attestation conclusion through a Registry correction.

---

## Supersession, Revocation, and Archival

### Supersession

A SREG may be superseded when a successor Registry Entry or distinct successor attestation record replaces it.

### Revocation

Registry may revoke the SREG for a Registry-controlled reason, such as invalid registration or material source misidentification.

Attestor may separately revoke the Authoritative Attestation Record.

These actions must remain distinct.

### Archival

An Attestation SREG may be archived while preserving:

- Registry Identifier;
- Source Institution;
- Source-System Identifier;
- source references;
- versions;
- relationships;
- status history;
- correction history;
- supersession history;
- revocation history.

---

## Validation Requirements

Before publication, Registry should confirm:

- Source Institution is identified;
- Authoritative Attestation Record exists or is historically documented;
- Registry Identifier is valid;
- Source-System Identifier is preserved when available;
- Attestation Record Type is approved;
- Attestation classification is valid;
- attested subject is identified;
- required references are present;
- required relationships are valid;
- Registry Status and Source-Record Status remain separate;
- version metadata is complete;
- the SREG Base Schema validates;
- the Attestation Record-Type Profile validates;
- human-readable and machine-readable forms agree.

Registry validation does not constitute a new attestation.

---

## Human-Readable Publication

The human-readable Attestation SREG should communicate:

- Registry Identifier;
- title;
- Source Institution;
- Source-System Identifier;
- Attestation classification;
- attested subject;
- source attestation summary;
- Source-Record Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- evidence and public references;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication

The machine-readable Attestation SREG should preserve equivalent institutional meaning.

It may include:

- identifiers;
- controlled classifications;
- source references;
- status values;
- lifecycle values;
- version metadata;
- typed relationships;
- evidence references;
- dates;
- schema version;
- profile version;
- validation metadata.

---

## Publication Consistency

Official forms of the same Attestation SREG must agree on:

- Registry Identifier;
- title;
- Record Type;
- Attestation classification;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- attested subject;
- Source-Record Status;
- Registry Status;
- Lifecycle State;
- versions;
- references;
- relationships;
- dates.

A record is not fully reconciled when official forms materially disagree.

---

## Future Development

As Satoshium Attestor develops, Attestation Records may expand to support:

- controlled attestation classes;
- attestation methods;
- evidence manifests;
- trust levels;
- signature references;
- timestamp references;
- integrity anchors;
- independent reviewer references;
- revocation records;
- supersession records;
- machine-verifiable attestations;
- cross-institution attestation relationships.

Future additions should preserve the established authority boundary:

```text
Attestor creates the attestation.
Registry creates the SREG.
```

---

## Registry Notes

Registry records and organizes attestation information.

Registry does not independently:

- verify the attested claim;
- certify the subject;
- issue the attestation;
- create the attestation conclusion;
- guarantee the continued availability of the source;
- create ownership, legal rights, or regulatory approval.

Registration means the attestation record has been cataloged.

It does not mean Registry endorses or independently confirms the attestation.

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
- Attestor institutional documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When the Attestation Record architecture changes:

- update this document;
- update the Attestation Record-Type Profile;
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

- Attestor creates the attestation.
- Registry creates the Attestation SREG.
- The SREG is not the Source Record.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and source lifecycle remain distinct.
- Registry may report an attestation conclusion but may not redefine it.
- Relationships should be typed and attributable.
- Versions should remain independently traceable.
- Human-readable and machine-readable forms should agree.
- Revoked or superseded attestations should remain historically discoverable.
- Registration does not itself verify the attestation.

---

## Disclaimer

An Attestation SREG is a Registry-owned catalog record.

It does not by itself create:

- an attestation;
- verification;
- certification;
- endorsement;
- ownership;
- legal rights;
- regulatory approval;
- affiliation;
- source authority.

Those remain controlled by Attestor, the Source Institution, the Source Record, the rights holder, or the applicable external authority.

---

## Guiding Statement

> Attestor creates the trust statement.
>
> Registry creates the SREG.
>
> The SREG preserves identity, context, relationships, and the path back to the attestation.
