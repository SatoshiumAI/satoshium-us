# Satoshium Registry Provenance

## Overview

The `registry/provenance/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Provenance framework.

The public page is published through:

```text
registry/provenance/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how every Satoshium Registry Entry preserves a traceable, attributable, version-aware path back to:

- the Authoritative Source Record;
- the Source Institution;
- the Source-System Identifier;
- the canonical source reference;
- source versions;
- publication history;
- custody history;
- derived artifacts;
- validation and workflow history;
- corrections;
- supersession;
- archival preservation.

Provenance allows Registry users to understand where a SREG came from, what source supports it, which institution controls that source, and how the Registry record changed over time.

---

## Constitutional Position

Provenance operates across the complete SREG lifecycle.

```text
Source Institution
  ↓
Authoritative Source Record
  ↓
Source References
  ↓
SREG
  ↓
Registry History
```

Provenance begins with Source Authority and continues through:

- Registrability;
- Identifier Assignment;
- SREG Construction;
- Validation;
- Publication;
- Updates;
- Corrections;
- Supersession;
- Revocation;
- Retirement;
- Archival preservation.

---

## Core Principle

```text
Authority identifies who controls the source.
Provenance preserves the path from the SREG back to it.
```

A Registry Entry should never become detached from the institutional and historical path that supports it.

---

## Canonical Provenance Path

```text
SREG
  ↓
Registry Source Reference
  ↓
Authoritative Source Record
  ↓
Source Institution
```

Supporting provenance layers may include:

- source versions;
- publication locations;
- repositories;
- package structures;
- manifests;
- generation records;
- archival copies;
- integrity references;
- workflow records;
- correction history;
- successor relationships.

---

## Why Provenance Matters

A SREG without provenance may identify a record but fail to explain:

- where the record originated;
- who created or issued it;
- which source is canonical;
- which version applies;
- how Registry acquired or registered it;
- what changed over time;
- whether the record is original, derived, mirrored, or archived;
- how prior states remain discoverable.

Provenance preserves the institutional chain needed to reconstruct the SREG's history.

---

## Core Provenance Requirements

A SREG should preserve the following provenance information when applicable:

- Source Institution;
- Source Institution identifier;
- Authoritative Source Record;
- Source-System Identifier;
- canonical source reference;
- source object type;
- source version;
- source publication or issuance date;
- source effective date;
- Source-Record Status;
- repository, publisher, or platform;
- acquisition or registration context;
- authority-review reference;
- Registrability review reference;
- identifier-assignment reference;
- validation reference;
- publication reference;
- correction history;
- version history;
- lifecycle history;
- archival references;
- integrity references.

---

## Provenance Categories

### Origin Provenance

Identifies where the Source Record originated and which institution created or issued it.

### Custody Provenance

Preserves how the Source Record moved through repositories, publishers, archives, custodians, or successor institutions.

### Version Provenance

Connects the SREG to the relevant Source-Record Version and Registry Entry Version.

### Publication Provenance

Preserves where, when, and in what form the Source Record and SREG were published.

### Operational Provenance

Preserves reviews, workflows, validations, corrections, and maintenance actions.

### Historical Provenance

Preserves prior states, supersession, withdrawal, retirement, archival custody, and successor relationships.

---

## Source Provenance

Source Provenance should preserve:

- Source Institution name;
- Source Institution identifier;
- Source-System Identifier;
- canonical source title;
- canonical source location;
- source object type;
- source version;
- publication date;
- effective date;
- source status;
- publisher or repository;
- rights or licensing reference;
- known mirrors;
- known derivatives;
- predecessor sources;
- successor sources.

---

## Registration Provenance

Registry should preserve how a Source Record became a proposed and then operational SREG.

```text
Source Identified
  ↓
Authority Reviewed
  ↓
Registrability Determined
  ↓
Identifier Assigned
  ↓
SREG Constructed
```

Registration provenance should include:

- review outcomes;
- review dates;
- responsible authority;
- workflow references;
- conditions;
- limitations;
- supporting evidence;
- assignment events.

---

## Publication Provenance

Publication provenance should preserve:

- first publication date;
- canonical human-readable URL;
- canonical machine-readable URL;
- publication version;
- publication authority;
- validation result;
- SREG Base Schema Version;
- Record-Type Profile Version;
- downloadable artifact references;
- integrity references;
- prior publication paths;
- redirects;
- archival publication references.

---

## Version Provenance

Version Provenance should distinguish among:

- Registry Entry Version;
- Source-Record Version;
- SREG Base Schema Version;
- Record-Type Profile Version;
- Registry Schema Specification Version;
- Registry Rules Version;
- Registry Policy Version;
- Suite Standards Version;
- Suite Methodology Version.

```text
A change in one version domain does not automatically imply a change in another.
```

---

## Custody Provenance

A Source Record may move between:

- institutional repositories;
- public websites;
- package structures;
- publication platforms;
- archives;
- successor institutions;
- preservation services;
- controlled-access environments.

Registry should preserve custody changes without implying that every custodian becomes the Source Institution.

```text
Custody identifies who holds or preserves a record.
Authority identifies who controls its institutional meaning.
```

---

## Custody Classes

### Original Custody

The Source Institution directly publishes or stores the Source Record.

### Delegated Custody

Another platform or repository hosts the record on behalf of the Source Institution.

### Archival Custody

An archive preserves the record after active publication changes or ends.

### Successor Custody

A successor institution assumes preservation or maintenance responsibility.

---

## Derived and Generated Records

Provenance must distinguish original Source Records from derived or generated artifacts.

Examples include:

- Certification Package and generated SCPR, SCR, and SCRD artifacts;
- canonical Markdown and derived JSON;
- jurisdiction JSON and matched generation manifest;
- source media and generated thumbnails;
- source evidence and generated summaries;
- original record and archived snapshot;
- source data and machine-readable export.

Derived artifacts may be authoritative representations within their defined role, but they must preserve the path back to the canonical source.

---

## Provenance Relationships

Provenance may use typed relationships such as:

- sourced from;
- produced by;
- derived from;
- generated from;
- published by;
- hosted by;
- preserved by;
- archived as;
- version of;
- supersedes;
- superseded by;
- successor to;
- predecessor of;
- validated by;
- anchored by;
- documented by.

Final relationship labels and controlled values remain subject to Registry governance.

---

## Provenance Evidence

Supporting evidence may include:

- institutional metadata;
- repository history;
- release records;
- publication manifests;
- generation manifests;
- version-control history;
- signed artifacts;
- hashes;
- integrity references;
- Chronicle events;
- Attestor statements;
- Certifier artifacts;
- archival snapshots;
- governance decisions;
- correction records.

---

## Machine-Readable Provenance

Machine-readable SREGs should preserve provenance through structured fields rather than narrative alone.

Illustrative structure:

```text
source_institution: "Satoshium Atlas"
source_identifier: "atlas-jurisdiction-el-salvador"
source_version: "1.0.0"
canonical_source: "https://satoshium.us/atlas/..."
derived_artifact: "jurisdiction.json"
generation_manifest: "manifest.json"
registry_identifier: "SREG-JUR-2026-0001"
```

Final field names and structures remain subject to the SREG Base Schema and Registry Schema Specification.

---

## Human-Readable Provenance

Human-readable SREGs should allow a visitor to determine:

- who created the Source Record;
- what the authoritative source is;
- where the source can be found;
- which version applies;
- when it was published or became effective;
- how Registry registered it;
- what derived artifacts exist;
- what changed over time;
- where prior versions or archival copies can be found.

---

## Unavailable Sources

When a Source Record becomes unavailable, Registry should preserve:

- last known Source Institution;
- last known canonical source reference;
- Source-System Identifier;
- last known source version;
- last known Source-Record Status;
- archival references;
- integrity references;
- date availability changed;
- reason for unavailability, when known;
- successor or replacement source.

```text
Source unavailability changes access.
It does not erase provenance.
```

---

## Historical Provenance

Historical Provenance should preserve:

- prior Source Institutions;
- prior canonical URLs;
- prior Source-System Identifiers;
- prior source versions;
- prior Registry Entry Versions;
- superseded relationships;
- revoked relationships;
- withdrawal events;
- retirement events;
- archival events;
- custody transfers;
- correction history;
- Chronicle event references;
- successor and predecessor records.

---

## Provenance Corrections

A Provenance correction may be required when:

- Source Institution was misidentified;
- Source-System Identifier was incorrect;
- canonical source reference was wrong;
- source version was misstated;
- publication date was incorrect;
- custody was confused with authority;
- a mirror was presented as canonical;
- a derivative was presented as original;
- a historical source was presented as current;
- generation path was incomplete;
- archival reference was misclassified.

---

## Correction Without Erasure

Provenance corrections should preserve:

- prior provenance value;
- corrected provenance value;
- correction reason;
- correction date;
- correction authority;
- supporting evidence;
- affected Registry Entry Version;
- affected relationship;
- affected reference;
- public Correction Record.

Corrected provenance should improve traceability without deleting the history of the original Registry assertion.

---

## Provenance Validation

Validation should confirm:

- Source Institution is identified;
- Authoritative Source Record is identifiable;
- Source-System Identifier is preserved when available;
- canonical source reference is attributable;
- source and Registry versions are distinguishable;
- custody and authority are not conflated;
- derived artifacts identify their source;
- archival references are labeled accurately;
- corrections preserve prior values;
- historical records are not presented as current;
- required supporting references exist;
- human-readable and machine-readable provenance agree.

---

## Invalid Provenance Conditions

Invalid conditions include:

- missing Source Institution;
- missing Source Record reference;
- unsupported source attribution;
- mirror presented as canonical source;
- derivative presented as original;
- custodian presented as Source Institution without support;
- Source-System Identifier replaced by Registry Identifier;
- source and Registry versions collapsed;
- historical source presented as current;
- unavailable source removed without archival context;
- silent provenance correction;
- human-readable and machine-readable mismatch.

---

## Relationship to Source Authority

Source Authority determines who controls the Source Record.

Provenance preserves the traceable path from the SREG back to that Source Institution and Source Record.

```text
Authority answers who.
Provenance explains how the record can be traced.
```

---

## Relationship to Registrability

Registrability requires enough provenance to support accurate registration.

A source should not become an operational SREG when Registry cannot preserve:

- identifiable origin;
- source attribution;
- canonical reference;
- Source-System Identifier, when available;
- minimum version and publication context;
- durable path back to the Source Record.

---

## Relationship to Identifiers

Provenance should preserve the distinction among:

- Registry Identifier;
- Source-System Identifier;
- external identifier;
- version identifier;
- artifact identifier;
- integrity identifier.

Identifier domains should remain explicit throughout provenance history.

---

## Relationship to Relationships

Typed relationships connect:

- SREG to Source Record;
- Source Record to Source Institution;
- derived artifact to canonical source;
- current version to prior version;
- active source to archival source;
- record to integrity reference;
- SREG to review, correction, and publication history.

```text
Provenance explains origin.
Relationships explain context.
```

---

## Relationship to Validation

Provenance validation confirms that Registry can support and reconstruct its source attribution and history.

It does not certify the substantive truth of the Source Record.

---

## Relationship to Publication

Provenance should be visible and consistent across:

- human-readable SREG;
- machine-readable SREG;
- canonical Registry page;
- downloadable records;
- version history;
- correction records;
- archival presentation;
- relationship objects.

---

## Relationship to Lifecycle

Provenance should remain intact across:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

Lifecycle changes the institutional condition of the SREG.

Provenance preserves how the SREG reached that condition.

---

## Relationship to Corrections

Provenance corrections should follow Registry correction requirements.

They should be:

- attributable;
- dated;
- version-aware;
- evidence-supported;
- historically preserved;
- reflected in human-readable and machine-readable forms.

---

## Relationship to Governance

Registry governance should control:

- required provenance fields;
- provenance evidence requirements;
- custody classifications;
- derived-artifact rules;
- archival reference rules;
- correction procedures;
- version-history requirements;
- unavailable-source handling;
- validation rules;
- exception handling;
- controlled provenance relationship types.

---

## Suite Provenance Examples

### Atlas

Provenance may connect:

- canonical Markdown;
- jurisdiction JSON;
- generation manifest;
- repository path;
- Atlas package;
- Jurisdiction SREG.

### Certifier

Provenance may connect:

- Certification Package;
- SCPR;
- SCR;
- SCRD HTML;
- SCRD JSON;
- certification subject;
- evidence;
- Certification SREG.

### Attestor

Provenance may connect:

- Attestation Record;
- issuing authority;
- attestation subject;
- evidence;
- certification;
- integrity reference;
- Attestation SREG.

### Anchor

Provenance may connect:

- record version;
- hash;
- signature;
- timestamp;
- commitment;
- durable integrity reference.

### Chronicle

Provenance may connect Registry changes to Chronicle-created historical events.

### Beacon

Provenance may connect signals to the records, events, or milestones they announce.

### Navigator

Provenance may connect SREG creation and maintenance to workflow definitions and execution records.

---

## Current Directory Structure

```text
registry/
└── provenance/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Provenance page.

### `README.md`

The directory-level documentation explaining provenance origin, custody, versions, publication, evidence, validation, corrections, and maintenance.

Future supporting materials may include:

```text
provenance/
├── index.html
├── README.md
├── provenance-schema.md
├── custody-types.md
├── derived-artifacts.md
├── unavailable-sources.md
├── examples/
├── history/
└── versions/
```

These materials should be introduced only when corresponding operational resources exist.

---

## Relationship to Other Registry Documentation

This directory should remain consistent with:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Rules;
- Registry Source Authority;
- Registry Registrability;
- Registry Identifiers;
- Registry Relationships;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
- Registry Validation;
- Registry Publication;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections;
- Registry Integration;
- Registry Policies;
- Registry Procedures;
- Registry Governance;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Provenance architecture changes:

- update `index.html`;
- update this README;
- update required provenance fields;
- update custody classifications;
- update derived-artifact requirements;
- update unavailable-source handling;
- update version-history rules;
- update relationship types;
- update correction procedures;
- update Validation requirements;
- update the SREG Base Schema;
- update affected Record-Type Profiles;
- update Registry Policies;
- update Registry Procedures;
- update examples;
- preserve prior versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable materials.

---

## Guiding Principles

- Every SREG must preserve a path back to authority.
- Provenance begins with the Source Institution.
- Source Authority and custody remain distinct.
- Source-System Identifier and Registry Identifier remain distinct.
- Derived artifacts must identify their source.
- Mirrors must not be represented as canonical sources.
- Historical provenance must remain discoverable.
- Unavailable sources must retain archival context.
- Corrections must preserve prior values.
- Version domains must remain separate.
- Provenance and relationships remain distinct.
- Validation confirms traceability, not source truth.
- Human-readable and machine-readable forms must agree.

---

## Disclaimer

Registry Provenance does not by itself establish:

- certification;
- attestation;
- verification;
- source truth;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- endorsement;
- affiliation;
- current availability;
- canonical status of every preserved copy.

Those remain controlled by the Source Institution, rights holder, governing authority, Source Record, applicable policy, or external system.

---

## Guiding Statement

> Authority begins at the source.
>
> Provenance preserves the path.
>
> Registry keeps that path discoverable.
