# Registry Signal Records

## Overview

This document defines how Signal Records are represented within Satoshium Registry.

A Signal Record is a Satoshium Registry Entry, or SREG, that catalogs an Authoritative Source Record for a discovery signal, announcement, declaration, marker, observation, notice, or other approved informational artifact.

Registry catalogs the signal.

Registry does not necessarily create the signal or determine its ultimate significance.

---

## Constitutional Position

Signal Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Beacon or Source Institution Implementation
  ↓
Authoritative Signal Record
  ↓
Registry Signal SREG
```

Beacon or another approved Source Institution creates and maintains the Authoritative Signal Record.

Registry creates and maintains the SREG that identifies, classifies, references, relates, versions, and preserves discoverability of that source record.

---

## Canonical Relationship

The canonical relationship is:

```text
Beacon or Source Institution
  ↓
Authoritative Signal Record
  ↓
Registry Signal SREG
```

This relationship preserves institutional separation:

- the Source Institution owns the signal;
- Registry owns the SREG;
- the SREG points back to the Authoritative Source Record;
- Registry does not absorb source authority or signal meaning.

---

## Purpose

Signal Records exist to improve:

- discoverability;
- source attribution;
- signal classification;
- event and record linkage;
- chronology;
- public reference management;
- version awareness;
- lifecycle visibility;
- preservation context;
- cross-system interoperability;
- historical continuity.

A Registry Signal SREG should help answer:

- What signal was issued?
- Which institution issued it?
- What Registry Identifier identifies the SREG?
- What Source-System Identifier identifies the signal?
- What Signal Class applies?
- When was the signal issued or recorded?
- What information did it communicate?
- What event, record, tool, jurisdiction, certification, attestation, or media artifact is associated with it?
- What is the Source-Record Status?
- What is the Registry Status?
- Which versions apply?
- Where can the Authoritative Source Record be found?
- How can the signal remain discoverable later?

---

## What Is a Signal?

A signal is an intentional informational artifact preserved for future discovery, interpretation, or reference.

Signals may document:

- discoveries;
- announcements;
- declarations;
- milestones;
- questions;
- observations;
- historical markers;
- development events;
- publication events;
- status notices;
- warnings;
- calls for attention;
- ecosystem developments.

A signal does not necessarily establish a conclusion.

It may preserve only that a particular statement, observation, or notice existed at a defined point in time.

---

## Record Type

The primary Registry Record Type is:

```text
Signal
```

Every operational Signal SREG must use the approved Signal Record-Type Profile.

The profile may define:

- required fields;
- optional fields;
- controlled Signal Classes;
- chronology fields;
- required relationships;
- permitted relationships;
- source-reference requirements;
- status requirements;
- lifecycle requirements;
- validation rules;
- publication requirements.

---

## Source Institutions

Signal Records may originate from:

- Beacon;
- Atlas;
- Certifier;
- Registry;
- Chronicle;
- Anchor;
- Attestor;
- Navigator;
- another approved Satoshium Suite institution;
- an approved external institution or publisher.

Beacon will normally serve as the Source Institution for discovery-oriented signals.

The Source Institution must remain distinct from Registry.

---

## Authoritative Source Record

Every Signal SREG must identify the Authoritative Source Record being cataloged.

The Source Record may include:

- Beacon discovery signal;
- public announcement;
- institutional declaration;
- development notice;
- milestone signal;
- observation record;
- historical marker;
- preservation notice;
- publication signal;
- another approved signal artifact.

The SREG should preserve the canonical source reference whenever available.

---

## Registry Identifier and Source-System Identifier

A Signal SREG must preserve distinct identifiers.

### Registry Identifier

Assigned by Satoshium Registry.

Identifies the SREG.

### Source-System Identifier

Assigned by Beacon or the originating Source Institution.

Identifies the Authoritative Signal Record.

Example:

```text
Registry Identifier: SREG-SIG-0001
Source-System Identifier: SBEACON-2026-0001
```

The Registry Identifier must not replace, modify, or overwrite the Source-System Identifier.

When no source identifier exists, the absence should be documented rather than replaced with an invented source identifier.

---

## Signal Classes

Controlled Signal Classes may include:

### Discovery Signal

Documents a discovery, newly surfaced resource, observation, or item requiring future attention.

### Historical Signal

Preserves a notable milestone, event, transition, or historically significant publication.

### Development Signal

Documents Suite development, growth, release activity, institutional change, or architectural progress.

### Public Signal

Communicates information intended for public review, discovery, or reference.

### Reference Signal

Preserves a reference primarily for continuity, linkage, or future discoverability.

### Status Signal

Communicates a current status, transition, availability condition, or operational state.

### Warning Signal

Communicates risk, uncertainty, limitation, anomaly, or a condition requiring attention.

### Preservation Signal

Marks a record, resource, or event as significant for preservation or archival continuity.

Additional classes require approval through Beacon and Registry governance as applicable.

---

## Required SREG Elements

An operational Signal SREG should include:

### Identity

- Registry Identifier;
- title;
- Registry Record Type;
- Signal Class.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier, when available;
- canonical source reference.

### Signal Context

- signal statement or summary;
- signal date;
- effective date, when applicable;
- associated event or subject;
- originating channel or publication;
- intended audience, when relevant;
- Source-Record Status.

### Registry Context

- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG schema version;
- Signal Record-Type Profile version;
- registration date;
- last updated date.

### Relationships

- related Tool SREGs;
- related Jurisdiction SREGs;
- related Media SREGs;
- related Certification SREGs;
- related Attestation SREGs;
- related Historical Event SREGs;
- related Integrity Reference SREGs;
- related Workflow records;
- related Signal SREGs.

---

## Example Record Structure

```text
Registry Identifier
Title
Registry Record Type
Signal Class
Source Institution
Source-System Identifier
Authoritative Source Record
Signal Statement
Signal Date
Effective Date
Associated Subject or Event
Originating Channel
Intended Audience
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

The authoritative field definitions belong to the Registry Schema Specification and Signal Record-Type Profile.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-SIG-0001 |
| Registry Record Type | Signal |
| Signal Class | Historical Signal |
| Source Institution | Satoshium Beacon |
| Source-System Identifier | SBEACON-2026-0001 |
| Signal Date | 2026-08-01 |
| Associated Subject | Registry Launch Milestone |
| Source-Record Status | Published |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Registry Entry Version | 1.0.0 |

This example is illustrative and does not establish final production identifiers or controlled values.

---

## Authority Boundary

### Source Institution Authority

The Source Institution remains authoritative for:

- signal content;
- signal meaning;
- Source-System Identifier;
- publication date;
- source version;
- Source-Record Status;
- source classification;
- originating channel;
- intended audience;
- revision, withdrawal, supersession, or retirement.

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

Registry may report source-controlled signal values.

Registry does not redefine the original signal or determine its ultimate significance.

---

## Related Registry Records

A Signal SREG may relate to:

- Tool SREGs;
- Jurisdiction SREGs;
- Media SREGs;
- Certification SREGs;
- Attestation SREGs;
- Historical Event SREGs;
- Integrity Reference SREGs;
- Workflow records;
- other Signal SREGs.

Examples:

```text
Signal SREG
  → announces
  → Tool SREG
```

```text
Signal SREG
  → concerns
  → Jurisdiction SREG
```

```text
Signal SREG
  → discovers
  → Media SREG
```

```text
Signal SREG
  → references
  → Certification SREG
```

```text
Signal SREG
  → documents
  → Historical Event SREG
```

```text
Signal SREG
  → anchored by
  → Integrity Reference
```

Relationships must use approved types and preserve direction where applicable.

---

## Signal Record Workflow

Registry should create a Signal SREG through the following process:

```text
Signal Source Record Identified
  ↓
Source Institution Confirmed
  ↓
Source Authority Confirmed
  ↓
Registrability Determined
  ↓
Signal Record Type Assigned
  ↓
Signal Class Assigned
  ↓
Registry Identifier Assigned
  ↓
Source-System Identifier Preserved
  ↓
References, Chronology, and Relationships Established
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

## Chronology

Signal Records are often time-sensitive.

A Signal SREG may preserve:

- signal date;
- publication date;
- effective date;
- observation date;
- registration date;
- last updated date;
- withdrawal date;
- supersession date;
- archival date.

These dates should remain distinct.

Chronology should identify whether a date belongs to the source signal or the Registry action.

---

## Lifecycle

A Signal SREG may move through approved Registry Lifecycle States such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states describe the SREG.

They do not replace the Source-Record Status of the signal.

Example:

```text
Source-Record Status: Withdrawn
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

Registry may preserve an active historical catalog entry for a source signal that has been withdrawn.

---

## Updates

A Signal SREG may be updated when:

- the Source Institution revises the signal;
- a new source version is published;
- Source-Record Status changes;
- chronology becomes clearer;
- public references change;
- relationships evolve;
- associated records are added;
- Registry metadata improves;
- schema migration occurs;
- the Signal Record-Type Profile changes.

Updates must preserve the distinction between source-controlled and Registry-controlled changes.

---

## Corrections

A Registry correction may be required when Registry incorrectly records:

- Source Institution;
- Source-System Identifier;
- signal date;
- Signal Class;
- canonical source reference;
- associated event;
- Registry Status;
- relationship target;
- version metadata;
- publication data.

Registry may correct its representation of source-controlled values.

Registry may not rewrite the original signal through a Registry correction.

---

## Supersession

A Signal SREG may be superseded when:

- a distinct replacement signal exists;
- a new Registry Identifier is required;
- the original signal is replaced by a successor Source Record;
- a substantially different signal supersedes the prior one;
- governance requires a replacement SREG.

The prior SREG should remain discoverable and reference its successor.

---

## Withdrawal and Revocation

Two distinct actions may exist.

### Source Withdrawal or Revocation

The Source Institution withdraws, revokes, retracts, or deprecates the signal.

Registry should preserve the updated Source-Record Status and historical source references.

### Registry Revocation

Registry revokes the SREG because of a Registry-controlled defect, such as invalid registration or material source misidentification.

These actions must remain separate.

Registry revocation does not withdraw the signal.

Source withdrawal does not require deletion of the SREG.

---

## Archival

A Signal SREG may be archived while preserving:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- signal content summary;
- chronology;
- source references;
- versions;
- relationships;
- corrections;
- supersession history;
- revocation history;
- archival date and reason.

Archived does not mean deleted.

---

## Significance and Interpretation

Registry does not independently determine the significance of a signal.

A signal may be minor at issuance and significant later.

Registry may preserve:

- source-stated significance;
- related Chronicle events;
- later references;
- resulting certifications or attestations;
- related media;
- successor signals;
- historical interpretation records.

Later significance should be represented through attributed relationships or later source records rather than retroactively rewriting the original signal.

---

## Integrity and Preservation

Signal Records may reference:

- Anchor records;
- cryptographic hashes;
- timestamps;
- archived source pages;
- preservation packages;
- Chronicle events;
- version manifests;
- public snapshots.

Integrity references should remain distinct from Registry validation.

Registry validation confirms the SREG structure.

An integrity reference addresses preservation or consistency of the signal artifact.

---

## Validation Requirements

Before publication, Registry should confirm:

- Source Institution is identified;
- Authoritative Signal Record exists or is historically documented;
- Registry Identifier is valid;
- Source-System Identifier is preserved when available;
- Signal Record Type is approved;
- Signal Class is valid;
- signal date is recorded where known;
- signal statement or summary is attributable;
- associated subject or event is identified where required;
- required references are present;
- required relationships are valid;
- Registry Status and Source-Record Status remain separate;
- chronology fields are not conflated;
- version metadata is complete;
- the SREG Base Schema validates;
- the Signal Record-Type Profile validates;
- human-readable and machine-readable forms agree.

Registry validation does not verify the truth or importance of the signal.

---

## Human-Readable Publication

The human-readable Signal SREG should communicate:

- Registry Identifier;
- title;
- Signal Class;
- Source Institution;
- Source-System Identifier;
- signal statement or summary;
- signal date;
- associated subject or event;
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

The machine-readable Signal SREG should preserve equivalent institutional meaning.

It may include:

- identifiers;
- controlled signal classifications;
- source references;
- chronology;
- status values;
- lifecycle values;
- version metadata;
- typed relationships;
- associated subjects or events;
- publication channels;
- integrity references;
- schema version;
- profile version;
- validation metadata.

---

## Publication Consistency

Official forms of the same Signal SREG must agree on:

- Registry Identifier;
- title;
- Record Type;
- Signal Class;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- signal date;
- associated subject or event;
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

Signal Records may expand to support:

- richer Signal Class taxonomies;
- signal hierarchies;
- discovery frameworks;
- signal confidence metadata;
- urgency or priority fields;
- public distribution channels;
- machine-readable notification records;
- historical relationship graphs;
- integrity anchors;
- automated source monitoring;
- cross-system interoperability;
- signal-to-event mapping;
- signal-to-workflow mapping;
- source withdrawal records;
- successor-signal chains.

Future development must preserve the established authority boundary:

```text
Beacon or another Source Institution creates the signal.
Registry creates the SREG.
```

---

## Registry Notes

Registry records and organizes signal information.

Registry does not independently:

- issue the signal;
- verify every signal claim;
- determine its significance;
- guarantee its accuracy;
- guarantee continued source availability;
- create certification or attestation;
- create ownership or legal rights;
- establish truth merely by registration.

Registration means the signal record has been cataloged.

It does not mean Registry endorses the signal or confirms its importance.

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
- Beacon institutional documentation;
- applicable Source Institution documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When the Signal Record architecture changes:

- update this document;
- update the Signal Record-Type Profile;
- update schema enumerations;
- update validation rules;
- update examples;
- update Beacon integration documentation;
- review affected SREGs;
- reconcile human-readable and machine-readable publication;
- preserve prior versions;
- document material changes in the Registry Changelog.

---

## Guiding Principles

- Beacon or another approved Source Institution creates the signal.
- Registry creates the Signal SREG.
- The SREG is not the signal itself.
- Registry Identifier and Source-System Identifier remain distinct.
- Registry Status and Source-Record Status remain distinct.
- Registry Lifecycle and source lifecycle remain distinct.
- Signal chronology should preserve source and Registry dates separately.
- Registry may report significance but should not invent it.
- Relationships should be typed, directional, and attributable.
- Versions should remain independently traceable.
- Human-readable and machine-readable forms should agree.
- Withdrawn or superseded signals should remain historically discoverable where appropriate.
- Registration does not itself verify, endorse, or elevate the signal.

---

## Disclaimer

A Signal SREG is a Registry-owned catalog record.

It does not by itself create:

- truth;
- significance;
- certification;
- attestation;
- verification;
- endorsement;
- ownership;
- legal rights;
- regulatory approval;
- affiliation;
- Source Institution authority.

Those remain controlled by the Source Institution, Source Record, rights holder, governing authority, or applicable external system.

---

## Guiding Statement

> A signal may be small.
>
> A signal may become significant.
>
> The Source Institution creates the signal.
>
> Registry creates the SREG.
>
> The SREG preserves identity, chronology, relationships, versions, and the path back to the source.
