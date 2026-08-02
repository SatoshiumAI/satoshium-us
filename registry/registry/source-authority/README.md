# Satoshium Registry Source Authority

## Overview

The `registry/source-authority/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Source Authority framework.

The public page is published through:

```text
registry/source-authority/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how Satoshium Registry:

- identifies the institution responsible for an Authoritative Source Record;
- distinguishes source authority from Registry authority;
- preserves the path from a SREG back to the Source Institution;
- documents evidence supporting an authority determination;
- handles mirrors, copies, derivatives, archives, and unavailable sources;
- addresses multiple or conflicting authority claims;
- preserves historical changes in institutional responsibility;
- determines whether source authority is sufficient to proceed to Registrability review.

---

## Constitutional Position

Source Authority operates within the Satoshium Suite constitutional hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Source Institution
  ↓
Authoritative Source Record
  ↓
Satoshium Registry Entry (SREG)
```

The Source Institution creates or controls the Source Record.

Registry creates and controls the SREG that catalogs it.

---

## Canonical Authority Relationship

```text
Source Institution
  ↓
Authoritative Source Record
  ↓
Registry Reference
  ↓
SREG
```

The Source Institution owns the source-domain meaning of the record.

Registry preserves the structured public path back to it.

---

## Core Principle

```text
The Source Institution owns the Source Record.
Registry owns the SREG.
```

Registration does not transfer source authority to Registry.

Registry may identify, classify, reference, relate, version, publish, correct, and preserve a SREG without becoming the institution that created the underlying Source Record.

---

## What Source Authority Determines

Source Authority answers the following questions:

- Which institution created, issued, published, or maintains the Source Record?
- Which object is the Authoritative Source Record?
- What Source-System Identifier applies?
- Where is the canonical source located?
- What evidence supports the authority determination?
- Is the source direct, delegated, historical, external, mirrored, or derivative?
- Are multiple institutions claiming authority?
- Has authority changed over time?
- Is the authority determination sufficient for Registrability review?

---

## Registry Responsibility

Registry is responsible for documenting:

- Source Institution;
- Source Institution identifier, when available;
- Authoritative Source Record;
- Source-System Identifier;
- canonical source reference;
- source object type;
- source version;
- source publication or issuance date;
- source effective date;
- Source-Record Status;
- publisher or repository;
- supporting authority evidence;
- authority determination date;
- Registry review outcome.

---

## Registry Limitation

Registry does not create:

- source authority;
- ownership;
- legal rights;
- certification authority;
- attestation authority;
- governmental authority;
- editorial authority;
- licensing rights;
- regulatory approval;
- truth.

Registry records its determination about who controls the source.

That determination must remain attributable, reviewable, and subject to correction.

---

## Source Authority Evidence

Registry may use the following evidence when identifying a Source Institution:

- canonical institutional publication;
- official repository ownership;
- signed or issued institutional artifact;
- documented identifier assignment;
- governing policy;
- institutional statement;
- recognized publication channel;
- record metadata identifying the issuer or maintainer;
- version or release history;
- corresponding machine-readable source record;
- archival evidence preserving prior institutional control.

Authority evidence supports the Registry determination.

It does not replace the authority of the Source Institution.

---

## Authority Classes

### Direct Authority

The Source Institution publishes or issues the Source Record through its own canonical channel.

### Delegated Publication

The Source Institution authorizes another platform, repository, publisher, or service to distribute the record while retaining institutional authority.

### Historical Authority

The original Source Institution may no longer operate, but historical evidence identifies who created or controlled the record.

### External Authority

Registry may catalog an approved external record when its institutional ownership, provenance, scope, and registrability are sufficiently established.

### Archival Custody

An archive preserves the record without necessarily inheriting the original institution's substantive authority.

---

## Institutional Roles

### Source Institution

The institution responsible for the Source Record's institutional meaning.

### Supporting Institution

An institution that provides evidence, hosting, preservation, publication, or interoperability support without controlling the Source Record.

### Platform or Repository

A technical service that hosts or distributes a record.

Hosting does not automatically establish source authority.

### Rights Holder

The person or institution controlling ownership or licensing rights.

The Rights Holder may be distinct from the Source Institution.

### Registry

The institution responsible for creating and maintaining the SREG.

---

## Multiple Sources

Multiple records may concern the same subject without representing the same source object.

Registry should determine whether multiple publications represent:

- the same Source Record;
- separate versions of one Source Record;
- distinct Source Records about the same subject;
- a canonical source and one or more mirrors;
- an original source and one or more derivatives;
- competing authority claims;
- predecessor and successor records.

```text
Similar subject matter does not make two records the same source object.
```

---

## Conflicting Authority Claims

When multiple institutions claim authority over the same Source Record, Registry should not silently select one claim.

Registry may:

- delay registration;
- identify the authority determination as unresolved;
- request additional evidence;
- register separate records when the source objects are genuinely distinct;
- preserve competing claims as structured relationships;
- record a provisional determination;
- refer the matter through Registry governance.

The review history should remain discoverable.

---

## Mirrors, Copies, and Derivatives

A mirror, cached page, transcript, export, translation, snapshot, or derivative representation may support discovery or preservation.

It should not be treated as the Authoritative Source Record unless the Source Institution designates it as authoritative.

```text
A preserved copy may be important.
A preserved copy is not automatically the canonical source.
```

---

## Unavailable or Removed Sources

A Source Record may become unavailable because:

- a page moved;
- a repository was removed;
- access became restricted;
- a platform deleted content;
- the Source Institution ceased operation;
- the public source was replaced;
- archival access became necessary.

Registry may preserve:

- the last known Source Institution;
- the last known canonical reference;
- the Source-System Identifier;
- the last known source version;
- Source-Record Status;
- archival references;
- integrity references;
- historical relationships;
- the date availability changed;
- the reason for unavailability, when known.

Source unavailability does not automatically erase prior authority or require deletion of the SREG.

---

## Authority Changes

Institutional responsibility may change through:

- organizational succession;
- repository transfer;
- publisher migration;
- merger or acquisition;
- governance reassignment;
- formal delegation;
- institutional dissolution;
- archival transfer.

Registry should preserve prior and current authority context.

It should not silently overwrite the historical record.

---

## Authority Change Versus Source Replacement

### Authority Change

The responsible institution changes while the underlying Source Record remains the same continuing object.

### Source Replacement

A new Source Record replaces the prior object.

Source replacement may require:

- a new Source-System Identifier;
- a new SREG;
- supersession;
- successor relationships;
- archival preservation of the prior SREG.

These conditions must not be treated as interchangeable.

---

## Source Authority Review

A source-authority review should document:

- proposed Source Institution;
- proposed Authoritative Source Record;
- supporting authority evidence;
- canonical source reference;
- Source-System Identifier;
- known mirrors or derivatives;
- competing claims;
- historical context;
- certainty or confidence;
- review outcome;
- review date;
- reviewer or process;
- required follow-up.

---

## Potential Review Outcomes

### Confirmed

The Source Institution and Authoritative Source Record are sufficiently established.

### Confirmed with Conditions

Authority is established, but limitations or review conditions remain.

### Provisional

The best available authority is identified pending additional evidence.

### Ambiguous

Multiple plausible authority claims remain unresolved.

### Insufficient

Available evidence does not support an operational authority determination.

### Rejected

The proposed authority claim is materially unsupported or incorrect.

These outcomes describe Registry's review.

They do not create or revoke source authority.

---

## Relationship to Registrability

Source Authority is a prerequisite for Registrability.

```text
Source Identified
  ↓
Authority Reviewed
  ↓
Authority Outcome Recorded
  ↓
Registrability Review
```

A source should not proceed to operational SREG creation when Registry cannot identify who controls the Source Record or explain the basis for its authority determination.

---

## Relationship to Provenance

Source Authority answers:

```text
Who controls the source?
```

Provenance answers:

```text
How can the SREG be traced back to that source?
```

Authority and provenance are related but distinct.

---

## Relationship to Validation

Source-authority validation should confirm:

- Source Institution is identified;
- Authoritative Source Record is identifiable;
- source reference is attributable;
- Source-System Identifier is preserved when available;
- mirrors and derivatives are not represented as canonical sources;
- ownership and licensing are not inferred without support;
- authority changes are historically preserved;
- review outcomes are recorded;
- human-readable and machine-readable SREG forms agree.

Validation confirms the structure and support for Registry's determination.

It does not certify the substantive truth of the Source Record.

---

## Relationship to Corrections

A Source Authority correction may be required when:

- the Source Institution was misidentified;
- the canonical source was incorrect;
- a mirror was represented as authoritative;
- authority evidence was incomplete;
- a successor institution was omitted;
- historical custody was confused with substantive authority;
- a Source-System Identifier was incorrectly assigned.

Corrections should preserve:

- prior value;
- corrected value;
- correction reason;
- correction date;
- supporting evidence;
- affected Registry Entry Version;
- public correction reference.

---

## Relationship to Registry Lifecycle

Source Authority may affect Registry Lifecycle without determining it automatically.

Examples:

- insufficient authority may prevent registration;
- unresolved authority may keep an entry pending;
- corrected authority may require a Registry update;
- invalid authority may require Registry revocation;
- historical authority may support an active historical entry;
- source unavailability may require archival references without archiving the SREG.

---

## Relationship to Suite Institutions

### Atlas

Atlas is authoritative for Atlas jurisdiction resources, evidence layers, canonical jurisdiction records, and machine-readable Atlas packages.

### Certifier

Certifier is authoritative for Certification Packages, SCPR, SCR, SCRD, Certification Outcome, and Certification Status.

### Chronicle

Chronicle is authoritative for Chronicle-created historical events and institutional chronology records.

### Anchor

Anchor is authoritative for Anchor-created integrity references, hashes, timestamps, signatures, and verification points.

### Beacon

Beacon is authoritative for Beacon-created signals and discovery metadata.

### Attestor

Attestor is authoritative for attestations, trust statements, validation records, and Attestor-controlled statuses.

### Navigator

Navigator is authoritative for Navigator-created workflow definitions and coordination records.

### Registry

Registry is authoritative for SREGs and Registry-owned metadata.

Registry is not authoritative for the substantive source objects created by other institutions.

---

## Current Directory Structure

```text
registry/
└── source-authority/
    ├── index.html
    └── README.md
```

### `index.html`

The public Source Authority page.

### `README.md`

The directory-level documentation explaining Source Institution identification, authority evidence, review outcomes, conflicts, historical changes, validation, and maintenance.

Future supporting materials may include:

```text
source-authority/
├── index.html
├── README.md
├── authority-review-schema.md
├── authority-outcomes.md
├── evidence-requirements.md
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
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
- Registry Integration;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections;
- Registry Policies;
- Registry Procedures;
- Registry Registrability;
- Registry Provenance;
- Registry Validation;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Source Authority architecture changes:

- update `index.html`;
- update this README;
- update authority-review fields;
- update authority outcomes;
- update the SREG Base Schema;
- update affected Record-Type Profiles;
- update Registrability requirements;
- update Provenance requirements;
- update Validation requirements;
- update Registry Policies;
- update Registry Procedures;
- update examples;
- review affected SREGs;
- preserve prior versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication.

---

## Guiding Principles

- Authority begins at the source.
- Registry owns the SREG, not the Source Record.
- Hosting does not automatically create authority.
- Archival custody does not automatically create substantive authority.
- Mirrors and derivatives must not be represented as canonical sources.
- Similar subject matter does not make records identical.
- Conflicting claims require documented review.
- Authority changes must preserve historical context.
- Source Authority is a prerequisite for Registrability.
- Authority and provenance remain distinct.
- Validation confirms support for the Registry determination, not source truth.
- Registration does not transfer institutional authority.

---

## Disclaimer

A Registry Source Authority determination does not by itself establish:

- legal ownership;
- intellectual-property rights;
- licensing rights;
- governmental authority;
- regulatory approval;
- certification;
- attestation;
- verification;
- endorsement;
- affiliation;
- source truth;
- permanent availability.

Those remain controlled by the applicable Source Institution, rights holder, governing authority, Source Record, or external system.

---

## Guiding Statement

> Authority begins at the source.
>
> Registry identifies it.
>
> The SREG preserves the path back to it.
