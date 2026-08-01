# Registry Certification Records

## Overview

This document defines how Certification Records are represented within Satoshium Registry.

A Certification Record is a Satoshium Registry Entry, or SREG, that catalogs an Authoritative Source Record created by Satoshium Certifier.

Registry catalogs the certification record.

Registry does not perform certification.

---

## Constitutional Position

Certification Records operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Certifier Institutional Implementation
  ↓
Certification Package and Supporting Certification Records
  ↓
Registry Certification SREG
```

Certifier remains authoritative for:

- the certification process;
- the applied standard and methodology;
- the certification scope;
- the certification class;
- the certification outcome;
- Certification Status;
- the Certification Package;
- supporting reports, receipts, and structured records.

Registry creates and maintains the SREG that identifies, classifies, references, relates, versions, and preserves discoverability of the Certifier-owned source record.

---

## Canonical Certification Relationship

The canonical operational relationship is:

```text
Certifier
  ↓
Certification Package
  ↓
Certification Process Report (SCPR)
  ↓
Certification Receipt (SCR)
  ↓
Structured Certified Record Data (SCRD)
  ↓
Registry Certification SREG
```

The Certification Package is Certifier's canonical certification object.

The SCRD is a Certifier-owned structured certification record.

The SREG is Registry's canonical operational object.

Registry does not replace any Certifier-owned artifact.

---

## Purpose

Certification Records exist to improve:

- discoverability;
- source attribution;
- certification-reference continuity;
- relationship mapping;
- lifecycle visibility;
- version awareness;
- evidence traceability;
- public reference management;
- machine-readable interoperability;
- historical preservation.

A Registry Certification SREG should help answer:

- What certification exists?
- What was certified?
- Which institution issued it?
- Which Certification Identifier identifies it?
- Which Registry Identifier identifies the SREG?
- Which standard and methodology were applied?
- What certification class applies?
- What Certification Outcome was issued?
- What is the Certification Status?
- What is the Registry Status?
- Which versions apply?
- What evidence and supporting records exist?
- Where can the Certification Package and supporting artifacts be found?
- What other Registry Records are related?

---

## Record Type

The primary Registry Record Type is:

```text
Certification
```

Every operational Certification SREG must use the approved Certification Record-Type Profile.

The profile may define:

- required fields;
- optional fields;
- controlled certification classifications;
- required relationships;
- permitted relationships;
- source-reference requirements;
- certification-reference requirements;
- status requirements;
- lifecycle requirements;
- validation rules;
- publication requirements.

---

## Source Institution

The Source Institution for Satoshium certification records is:

```text
Satoshium Certifier
```

Certifier remains authoritative for all certification-owned values.

Registry must identify Certifier as the Source Institution without implying that Registry issued or approved the certification.

---

## Authoritative Source Record

Every Certification SREG must identify the Authoritative Source Record being cataloged.

The primary source record should normally be one of the following:

- Certification Package;
- Structured Certified Record Data;
- another approved Certifier-owned canonical record.

Supporting source records may include:

- Certification Process Report;
- Certification Receipt;
- evidence package;
- standards reference;
- methodology reference;
- certification scope;
- subject profile;
- supporting decision record.

The SREG must preserve durable references to the Certification Package and other required Certifier-owned records.

---

## Registry Identifier and Certification Identifier

A Certification SREG must preserve distinct identifiers.

### Registry Identifier

Assigned by Satoshium Registry.

Identifies the SREG.

### Certification Identifier

Assigned by Satoshium Certifier.

Identifies the certification.

Example:

```text
Registry Identifier: SREG-CERT-0001
Certification Identifier: SC-CERT-2026-0001
```

The Registry Identifier must not replace, modify, or duplicate the institutional role of the Certification Identifier.

---

## Certification Artifacts

A Certification SREG may reference the following Certifier-owned artifacts:

### Certification Package

The canonical certification object containing the integrated certification record and authoritative artifact references.

### Certification Process Report

The detailed record of the certification process, review, evidence, methodology, and findings.

Abbreviation:

```text
SCPR
```

### Certification Receipt

The concise public record of the certification result.

Abbreviation:

```text
SCR
```

### Structured Certified Record Data

The machine-readable structured certification record.

Abbreviation:

```text
SCRD
```

### Evidence References

References to the evidence used or reviewed during certification.

### Standards and Methodology References

References to the Suite Standards, Suite Methodology, Certifier implementation materials, profiles, scope, and supporting requirements applied during certification.

---

## Certification Classes

Certification classes are controlled by Certifier.

A Certification SREG may report the applicable class but must not redefine it.

Potential or approved classes may include:

### Informational

The subject or resource exists and has been documented under the applicable Certifier framework.

### Operational

The subject or resource demonstrates operational functionality under the applicable certification scope.

### Verified

The subject or resource has been reviewed against an established standard and supported by evidence.

Additional certification classes may be introduced by Certifier governance.

Registry should preserve the exact source-controlled class value and the applicable Certifier profile or version.

---

## Certification Outcome

The Certification Outcome is controlled by Certifier.

Registry may report the outcome in the SREG.

Registry must not:

- create the outcome;
- revise the outcome;
- reinterpret the outcome;
- convert Registry Status into Certification Outcome;
- imply a different conclusion than the Source Record.

The SREG should preserve the exact source-controlled value whenever practical.

---

## Certification Status and Registry Status

Certification Status and Registry Status are separate fields.

### Certification Status

Controlled by Certifier.

Describes the institutional status of the certification.

### Registry Status

Controlled by Registry.

Describes the operational status of the SREG.

Example:

```text
Certification Status: Active
Registry Status: Active
```

Another example:

```text
Certification Status: Revoked
Registry Status: Active Historical Entry
```

Registry may preserve an active historical catalog entry for a certification that Certifier has revoked.

---

## Required SREG Elements

An operational Certification SREG should include:

### Identity

- Registry Identifier;
- title;
- Registry Record Type;
- Certification Identifier.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- canonical Certification Package reference;
- Source-System Identifier;
- source repository or publication location.

### Certification Context

- certified subject;
- certification class;
- Certification Outcome;
- Certification Status;
- certification date;
- standard reference;
- methodology reference;
- certification scope;
- evidence references.

### Registry Context

- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- SREG schema version;
- Certification Record-Type Profile version;
- registration date;
- last updated date.

### Supporting Artifacts

- SCPR reference;
- SCR reference;
- SCRD reference;
- Certification Package reference;
- evidence references;
- related public pages.

### Relationships

- related Tool SREGs;
- related Jurisdiction SREGs;
- related Media SREGs;
- related Attestation SREGs;
- related Signal SREGs;
- related historical records;
- integrity references;
- workflow references.

---

## Example Record Structure

```text
Registry Identifier
Title
Registry Record Type
Certification Identifier
Source Institution
Authoritative Source Record
Certified Subject
Certification Class
Certification Outcome
Certification Status
Registry Status
Registry Lifecycle State
Certification Date
Standard Reference
Methodology Reference
Certification Scope
Certification Package Reference
SCPR Reference
SCR Reference
SCRD Reference
Evidence References
Registry Entry Version
Source-Record Version
Schema Version
Profile Version
Public References
Relationships
Registration Date
Last Updated
```

The authoritative field definitions belong to the Registry Schema Specification and Certification Record-Type Profile.

---

## Example Metadata

| Field | Example |
|---|---|
| Registry Identifier | SREG-CERT-0001 |
| Registry Record Type | Certification |
| Certification Identifier | SC-CERT-2026-0001 |
| Source Institution | Satoshium Certifier |
| Certified Subject | El Salvador Atlas Resource |
| Certification Class | Verified |
| Certification Outcome | Certified |
| Certification Status | Active |
| Registry Status | Active |
| Registry Lifecycle State | Active |
| Certification Date | 2026-07-05 |
| Registry Entry Version | 1.0.0 |

This example is illustrative and should not override the authoritative Certification Package or current controlled values.

---

## Authority Boundary

### Certifier Authority

Certifier remains authoritative for:

- Certification Identifier;
- Certification Package;
- certified subject;
- certification scope;
- certification class;
- applied standards;
- applied methodology;
- evidence review;
- findings;
- Certification Outcome;
- Certification Status;
- source version;
- issuance;
- update;
- supersession;
- revocation;
- retirement.

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

Registry may report Certifier-controlled values.

Registry does not redefine them.

---

## Related Registry Records

A Certification SREG may relate to:

- Tool SREGs;
- Jurisdiction SREGs;
- Media SREGs;
- Attestation SREGs;
- Signal SREGs;
- Historical Event SREGs;
- Integrity Reference SREGs;
- Evidence records;
- Workflow records;
- other Certification SREGs.

Examples:

```text
Certification SREG
  → certifies
  → Jurisdiction SREG
```

```text
Certification SREG
  → produced by
  → Certifier Tool SREG
```

```text
Certification SREG
  → supported by
  → Evidence Record
```

```text
Certification SREG
  → attested by
  → Attestation SREG
```

```text
Certification SREG
  → anchored by
  → Integrity Reference
```

Relationships must use approved types and preserve direction where applicable.

---

## Certification Record Workflow

Registry should create a Certification SREG through the following process:

```text
Certification Source Record Identified
  ↓
Certifier Authority Confirmed
  ↓
Certification Package and Supporting Artifacts Confirmed
  ↓
Registrability Determined
  ↓
Certification Record Type Assigned
  ↓
Registry Identifier Assigned
  ↓
Certification Identifier Preserved
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

## First Operational Certification Path

The first operational Registry certification path is:

```text
Atlas Resource
  ↓
Certifier Evaluation
  ↓
Certification Package
  ↓
SCRD
  ↓
Registry Certification SREG
```

This path demonstrates Suite interoperability while preserving institutional authority:

- Atlas owns the jurisdiction resource;
- Certifier owns the Certification Package and SCRD;
- Registry owns the Certification SREG.

---

## Lifecycle

A Certification SREG may move through approved Registry Lifecycle States such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states describe the SREG.

They do not replace Certification Status or the Certifier lifecycle.

A Registry lifecycle transition may occur without a Certifier status change, and a Certifier status change may be reflected through a Registry update without retiring the SREG.

---

## Updates

A Certification SREG may be updated when:

- Certifier publishes a new Certification Package version;
- the SCRD is updated;
- Certification Status changes;
- public references change;
- evidence references expand;
- relationships evolve;
- Registry metadata improves;
- schema migration occurs;
- the Certification Record-Type Profile changes.

Updates must preserve the distinction between Certifier-controlled and Registry-controlled changes.

---

## Corrections

A Registry correction may be required when Registry incorrectly records:

- Certification Identifier;
- Source Institution;
- Certification Package reference;
- Certification class;
- Certification Outcome;
- Certification Status;
- Registry Status;
- relationship target;
- version metadata;
- publication data.

Registry may correct its representation of Certifier-controlled values.

Registry may not alter the authoritative certification decision.

---

## Supersession

A Certification SREG may be superseded when:

- a distinct successor certification record replaces it;
- a new Registry Identifier is required;
- a new authoritative certification object replaces the prior one;
- the original classification no longer accurately represents the source;
- governance requires a replacement SREG.

The prior SREG should remain discoverable and reference its successor.

---

## Revocation

Two distinct revocation actions may exist.

### Certifier Revocation

Certifier revokes the certification.

Registry should preserve the updated Certification Status and historical source references.

### Registry Revocation

Registry revokes the SREG because of a Registry-controlled defect, such as invalid registration or material source misidentification.

These actions must remain separate.

Registry revocation does not revoke the certification.

Certifier revocation does not require deletion of the SREG.

---

## Archival

A Certification SREG may be archived while preserving:

- Registry Identifier;
- Certification Identifier;
- Source Institution;
- Certification Package reference;
- supporting artifacts;
- Certification Outcome;
- Certification Status;
- Registry Status history;
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

- Certifier is correctly identified as Source Institution;
- the Authoritative Source Record exists;
- the Certification Identifier is preserved;
- the Registry Identifier is valid;
- the Certification Record Type is approved;
- the certified subject is identified;
- Certification class is reported accurately;
- Certification Outcome is reported accurately;
- Certification Status and Registry Status remain separate;
- Certification Package, SCPR, SCR, and SCRD references are correct where required;
- required evidence and public references are present;
- required relationships are valid;
- version metadata is complete;
- the SREG Base Schema validates;
- the Certification Record-Type Profile validates;
- human-readable and machine-readable forms agree.

Registry validation does not constitute a new certification.

---

## Human-Readable Publication

The human-readable Certification SREG should communicate:

- Registry Identifier;
- Certification Identifier;
- title;
- certified subject;
- Source Institution;
- Certification class;
- Certification Outcome;
- Certification Status;
- Registry Status;
- Registry Lifecycle State;
- certification date;
- versions;
- standards and methodology references;
- Certification Package and supporting artifact references;
- evidence references;
- relationships;
- registration date;
- last updated date.

---

## Machine-Readable Publication

The machine-readable Certification SREG should preserve equivalent institutional meaning.

It may include:

- Registry and certification identifiers;
- controlled classifications;
- source references;
- certification values;
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

Official forms of the same Certification SREG must agree on:

- Registry Identifier;
- Certification Identifier;
- title;
- Record Type;
- Source Institution;
- certified subject;
- Certification class;
- Certification Outcome;
- Certification Status;
- Registry Status;
- Registry Lifecycle State;
- versions;
- references;
- relationships;
- dates.

A record is not fully reconciled when official forms materially disagree.

---

## Future Development

Certification Records may expand to support:

- additional Certifier-controlled classes;
- certification hierarchies;
- multi-subject certifications;
- formal evidence manifests;
- standards and methodology version bindings;
- automated artifact reconciliation;
- machine-verifiable receipts;
- integrity references;
- attestation relationships;
- revocation records;
- supersession records;
- certification renewal history;
- cross-institution interoperability.

Future development must preserve the established authority boundary:

```text
Certifier performs certification.
Registry catalogs the certification.
```

---

## Registry Notes

Registry records and organizes certification information.

Registry does not independently:

- certify the subject;
- issue the Certification Outcome;
- approve the applied standard;
- validate the Certifier decision;
- guarantee the continued availability of source artifacts;
- create ownership, legal rights, or regulatory approval.

Registration means the certification record has been cataloged.

It does not mean Registry performed or independently endorsed the certification.

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
- Certifier institutional documentation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When the Certification Record architecture changes:

- update this document;
- update the Certification Record-Type Profile;
- update schema enumerations;
- update validation rules;
- update examples;
- update Certifier integration documentation;
- review affected SREGs;
- reconcile human-readable and machine-readable publication;
- preserve prior versions;
- document material changes in the Registry Changelog.

---

## Guiding Principles

- Certifier performs certification.
- Registry creates the Certification SREG.
- The SREG is not the Certification Package.
- The SREG is not the SCRD.
- Registry Identifier and Certification Identifier remain distinct.
- Registry Status and Certification Status remain distinct.
- Registry Lifecycle and Certifier lifecycle remain distinct.
- Registry may report Certification Outcome but may not redefine it.
- Versions should remain independently traceable.
- Relationships should be typed and attributable.
- Human-readable and machine-readable forms should agree.
- Revoked or superseded certifications should remain historically discoverable.
- Registration does not itself certify the subject.

---

## Disclaimer

A Certification SREG is a Registry-owned catalog record.

It does not by itself create:

- certification;
- Certification Outcome;
- verification;
- attestation;
- endorsement;
- ownership;
- legal rights;
- regulatory approval;
- affiliation;
- Certifier authority.

Those remain controlled by Certifier, the Certification Package, the Source Record, the rights holder, or the applicable external authority.

---

## Guiding Statement

> Certifier performs the certification.
>
> The Certification Package preserves the authoritative certification record.
>
> Registry creates the SREG.
>
> The SREG preserves identity, relationships, versions, and the path back to Certifier.
