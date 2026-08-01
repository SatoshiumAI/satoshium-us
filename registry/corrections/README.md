# Satoshium Registry Corrections

**Institutional correction framework for Satoshium Registry**

This directory contains the public documentation and supporting materials for the Satoshium Registry Corrections framework.

Registry Corrections define how Registry improves Registry-owned information while preserving source authority, transparent version history, institutional continuity, and the public path back to authoritative records.

The correction framework operates within the constitutional hierarchy of the Satoshium Suite:

```text
Suite Standards
  ↓
Registry Policy
  ↓
Registry Procedure
  ↓
SREG Correction
  ↓
Preserved History
```

Registry corrects Registry-owned information.

The Source Institution remains authoritative for changes to the Source Record.

---

## Purpose

The purpose of the Corrections framework is to ensure that Satoshium Registry can improve accuracy without erasing provenance, obscuring prior versions, or assuming authority over records created by other Suite institutions.

Corrections may be necessary when a Satoshium Registry Entry, or SREG, contains:

- inaccurate metadata;
- broken references;
- incorrect classifications;
- incomplete relationships;
- version mismatches;
- schema nonconformance;
- source-attribution errors;
- outdated source metadata;
- publication inconsistencies.

The objective is not merely to make the current entry appear correct.

The objective is to preserve a trustworthy record of what changed, why it changed, and which Registry version replaced the earlier one.

---

## Constitutional Position

Registry Corrections are implemented beneath:

- Satoshium Suite Standards;
- Satoshium Suite Methodology;
- Satoshium Suite Interoperability;
- Registry Rules;
- Registry Policies;
- Registry Procedures.

The framework must preserve:

- controlled terminology;
- version distinctions;
- governance history;
- source attribution;
- institutional separation;
- human-readable and machine-readable consistency;
- long-term archival continuity.

---

## Correction Authority

Registry may correct Registry-owned information, including:

- Registry Identifier formatting or assignment errors;
- Registry Record Type or subtype classification;
- Registry-authored titles, descriptions, and summaries;
- Source Institution attribution;
- Source-System Identifier transcription;
- canonical URLs and repository paths;
- public references;
- Registry relationships and relationship types;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- schema-version metadata;
- registration and update dates;
- supersession, revocation, and archival dates;
- machine-readable structure;
- required fields;
- validation errors;
- human-readable presentation where institutional meaning remains unchanged.

Registry correction authority applies to the SREG.

It does not extend to the content or authority of the underlying Source Record.

---

## Source Authority

The Source Institution remains authoritative for the Authoritative Source Record.

Registry does not correct or redefine:

- Certification Outcomes controlled by Certifier;
- Certification Status controlled by Certifier;
- Attestation conclusions controlled by Attestor;
- historical event content controlled by Chronicle;
- integrity determinations controlled by Anchor;
- discovery signals controlled by Beacon;
- jurisdiction intelligence controlled by Atlas;
- workflow definitions controlled by Navigator;
- third-party ownership, legal rights, or external-source content.

When a Source Record changes, Registry may update:

- the source reference;
- source-reported metadata;
- related Registry relationships;
- Registry lifecycle information;
- the SREG version;
- correction or update history.

The source change and the Registry update must remain distinguishable.

---

## Correction Classes

### Editorial Correction

A non-substantive correction to spelling, punctuation, formatting, or display that does not alter institutional meaning.

### Metadata Correction

A correction to Registry-owned descriptive fields, dates, identifiers, classifications, references, or relationships.

### Structural Correction

A correction required to restore schema compliance, machine readability, field organization, or Record-Type Profile conformity.

### Source-Reference Correction

A correction to the source location, Source-System Identifier, source version, source status, or Source Institution attribution.

### Material Correction

A correction that changes how the SREG is identified, classified, interpreted, related, versioned, or maintained within Registry.

### Administrative Correction

A correction to Registry publication, processing, or maintenance metadata that does not change the substance of the Source Record.

---

## Correction Workflow

Registry uses the following correction sequence:

```text
Issue Identified
  ↓
Authority Determined
  ↓
Impact Reviewed
  ↓
Correction Prepared
  ↓
Schema Validated
  ↓
Version Assigned
  ↓
History Documented
  ↓
Published
```

### 1. Issue Identified

A potential error, omission, broken reference, classification problem, source change, or schema issue is identified.

### 2. Authority Determined

Registry determines whether the matter belongs to Registry or to the Source Institution.

### 3. Impact Reviewed

The effect on identifiers, references, relationships, versions, lifecycle, interoperability, and public presentation is evaluated.

### 4. Correction Prepared

The corrected Registry-owned information is prepared without altering source authority.

### 5. Schema Validated

The corrected SREG is validated against the applicable Registry Schema Specification, SREG Base Schema, and Record-Type Profile.

### 6. Version Assigned

A new SREG version is assigned when the correction is material or otherwise requires versioned publication.

### 7. History Documented

The correction record preserves:

- what changed;
- why it changed;
- when it changed;
- which version was affected;
- which version replaced it;
- the resulting Registry action.

### 8. Published

Updated human-readable and machine-readable Registry artifacts are published consistently.

---

## Minor Corrections

Minor corrections may include:

- typographical changes;
- formatting repairs;
- non-substantive link repairs;
- display improvements;
- presentation corrections that do not change Registry meaning.

Minor corrections may not require a new semantic version, but they should remain traceable through repository history or another approved audit mechanism.

---

## Major Corrections

Major corrections may include:

- Registry Identifier reassignment;
- Record Type changes;
- structural revisions;
- entry mergers;
- entry splits;
- material relationship changes;
- correction of source-authority errors;
- changes that materially affect interpretation, status, lifecycle, or interoperability.

Major corrections require:

- explicit documentation;
- a new SREG version;
- preserved prior history;
- schema validation;
- publication reconciliation across all official Registry formats.

---

## Versioning

Registry distinguishes among:

- SREG version;
- Registry schema version;
- Record-Type Profile version;
- Registry specification version;
- Source-Record version.

These version layers are not interchangeable.

A correction to the SREG does not necessarily change the Source-Record version.

A change to the Source Record does not necessarily change the Registry schema.

Every material correction should preserve the following relationship:

```text
Prior SREG Version
  ↓
Correction Record
  ↓
Replacement SREG Version
```

---

## Correction History

A material Correction Record should preserve, at minimum:

- affected Registry Identifier;
- affected SREG version;
- correction classification;
- issue description;
- authority determination;
- reason for correction;
- correction date;
- replacement version;
- schema version;
- Source Record impact, if any;
- publication locations updated;
- responsible Registry action;
- related supersession, revocation, or archival information.

---

## Correction, Supersession, Revocation, and Archival

Not every issue should be handled as a simple correction.

### Correction

Improves Registry-owned information.

### Supersession

Replaces a SREG or SREG version with a newer Registry object while preserving the earlier version.

### Revocation

Withdraws a SREG from active Registry recognition for a documented reason.

### Archival

Preserves a SREG that is no longer in active operational use.

The selected action should reflect the actual institutional condition of the SREG and preserve the clearest possible historical record.

---

## Publication Consistency

Corrections must be applied consistently across every official representation of the same SREG.

This includes:

- human-readable Registry Entry pages;
- machine-readable SREG records;
- catalog indexes;
- relationship indexes;
- version history;
- correction history;
- interoperability references;
- archival records.

A correction is incomplete when official Registry formats disagree about the identity, classification, status, version, source, or relationships of the same SREG.

---

## Machine-Readable Correction Records

Future operational correction artifacts may include machine-readable records containing:

- correction identifier;
- Registry Identifier;
- prior SREG version;
- replacement SREG version;
- correction class;
- correction reason;
- correction date;
- affected fields;
- Source Record impact;
- responsible Registry authority;
- publication status;
- schema version;
- related lifecycle action.

Any machine-readable correction schema should remain consistent with the Registry Schema Specification and Suite Schema Standard.

---

## Directory Role

This directory is intended to contain the public Corrections page and related operational materials.

A possible structure is:

```text
corrections/
├── index.html
├── README.md
├── policy.md
├── procedure.md
├── schema/
│   └── correction-record.schema.json
├── records/
└── examples/
```

The exact structure may evolve through documented Registry governance.

The distinction among public explanation, policy, procedure, schema, records, and examples should remain clear.

---

## Related Registry Documentation

Corrections should remain consistent with:

- Registry Entry Model;
- Registry Lifecycle;
- Registry Status;
- Registry Schemas;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Definitions;
- Registry Scope;
- Registry Interoperability;
- Registry Changelog.

---

## Guiding Principles

- Registry corrects Registry-owned information.
- Source Institutions retain authority over Source Records.
- Corrections should be attributable.
- Material corrections should be versioned.
- Prior versions should remain preserved.
- Source changes and Registry changes should remain distinguishable.
- Human-readable and machine-readable artifacts should remain consistent.
- Correction history should remain publicly understandable.
- Corrections should improve accuracy without erasing provenance.
- Preservation should include the truth of the change.

---

## Disclaimer

The Registry Corrections framework governs changes to Satoshium Registry records and Registry-owned metadata.

It does not authorize Registry to alter:

- legal rights;
- ownership;
- certification outcomes;
- attestations;
- external records;
- governmental records;
- third-party content;
- the authority of another Suite institution.

A corrected SREG remains a Registry catalog object.

The Authoritative Source Record remains controlled by the Source Institution.

---

## Guiding Statement

> Correct the Registry Entry.
>
> Preserve the prior version.
>
> Attribute the source.
>
> Document the change.
>
> Maintain the path back to authority.
