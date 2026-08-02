# Satoshium Registry Registrability

## Overview

The `registry/registrability/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Registrability framework.

The public page is published through:

```text
registry/registrability/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define the institutional threshold an Authoritative Source Record must satisfy before Satoshium Registry may create, validate, and publish a Satoshium Registry Entry, or SREG.

Registrability determines:

- whether a proposed Source Record belongs within Registry scope;
- whether Source Authority is sufficiently established;
- whether one approved Registry Record Type applies;
- whether minimum metadata is available;
- whether provenance can be preserved;
- whether the proposed entry would duplicate an existing SREG;
- whether legal, privacy, safety, security, or institutional restrictions apply;
- whether the source has durable value sufficient to justify Registry identity;
- whether Registry should proceed to identifier assignment and SREG construction.

---

## Constitutional Position

Registrability operates after Source Authority review and before operational SREG construction.

```text
Source Identified
  ↓
Source Authority Reviewed
  ↓
Registrability Determined
  ↓
Registry Identifier Assigned
  ↓
SREG Constructed
  ↓
SREG Validated
  ↓
SREG Published
```

Source Authority answers who controls the source.

Registrability determines whether Registry should create a SREG for that source.

---

## Canonical Registrability Threshold

```text
Authority
  +
Identity
  +
Scope
  +
Record Type
  +
Minimum Metadata
  +
Provenance
  +
Durable Relevance
  =
Registrable Source Record
```

The exact requirements may vary by Registry Record Type.

Every operational SREG must still satisfy the shared institutional minimum.

---

## Core Principle

```text
Not every identifiable source should become a SREG.
```

Registry must preserve a deliberate threshold for inclusion.

A Registry that catalogs sources without authority, classification, scope, metadata, or durable relevance risks becoming inconsistent, duplicative, and difficult to trust.

---

## Core Registrability Requirements

A proposed Source Record should normally satisfy the following requirements:

- Source Institution is sufficiently identified;
- Authoritative Source Record is sufficiently identified;
- Source Authority determination is supported;
- source falls within Registry scope;
- one approved primary Registry Record Type applies;
- required SREG Base Schema fields are available;
- required Record-Type Profile fields are available;
- canonical or archival reference exists;
- sufficient provenance can be preserved;
- duplicate and conflict checks are complete;
- no unresolved defect would materially misrepresent the source;
- rights, privacy, safety, and security requirements permit registration;
- source has durable institutional or historical relevance;
- Registrability outcome is documented.

---

## Authority Requirement

The Source Institution must be identified with enough confidence to support attribution and preserve institutional responsibility.

Potential Source Authority outcomes that may support Registrability include:

- Confirmed;
- Confirmed with Conditions;
- Provisional, when Registry policy allows controlled progression.

Ambiguous, Insufficient, or Rejected authority findings will normally prevent operational registration.

---

## Identity Requirement

The proposed Source Record must be distinguishable from:

- its subject;
- other records about the same subject;
- prior and later versions;
- mirrors;
- copies;
- exports;
- derivatives;
- translations;
- archived snapshots;
- predecessor records;
- successor records.

A SREG identifies a Registry representation of one Source Record.

It does not identify a general topic unless an approved Record Type explicitly permits that function.

---

## Scope Requirement

A proposed source should align with one or more approved Registry purposes:

- public discoverability;
- institutional continuity;
- cross-Suite interoperability;
- preservation of identity;
- preservation of provenance;
- authoritative record classification;
- relationship mapping;
- version tracking;
- lifecycle tracking;
- historical preservation;
- machine-readable publication;
- future workflow or query support.

A legitimate and authoritative source may still be non-registrable when it falls outside Registry scope.

---

## Record-Type Requirement

Every operational SREG must receive one approved primary Registry Record Type.

Initial Registry Record Types include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Additional Record Types may be introduced through Registry governance.

A proposed source should not be forced into an inaccurate Record Type merely to permit registration.

---

## Minimum Metadata Requirement

The shared minimum should normally include:

- proposed title;
- proposed Registry Record Type;
- Source Institution;
- Authoritative Source Record;
- Source-System Identifier, when available;
- canonical or archival reference;
- source object description;
- Source-Record Status, when available;
- source version, when available;
- source publication or effective date, when available;
- provenance information;
- applicable Record-Type Profile;
- Registrability review outcome;
- review date;
- supporting references.

Record-Type Profiles may require additional fields.

---

## Provenance Requirement

Registry must be able to preserve a traceable path from the proposed SREG back to the Authoritative Source Record.

Provenance may include:

- Source Institution;
- Source-System Identifier;
- canonical source reference;
- source version;
- publication date;
- effective date;
- repository or publisher;
- archival references;
- integrity references;
- predecessor or successor references;
- historical custody;
- authority-review evidence.

A source should not proceed when Registry cannot explain where it came from or how the entry relates to the source.

---

## Durable-Relevance Requirement

Registry should prioritize records that possess value beyond a temporary mention, isolated draft, or transient technical artifact.

Durable relevance may arise from:

- institutional authority;
- operational use;
- historical significance;
- public accountability;
- cross-Suite relationships;
- version or lifecycle importance;
- workflow dependency;
- preservation need;
- machine-readable interoperability;
- continuing discovery value.

Durable relevance does not require permanent current activity.

Historical records may remain highly registrable.

---

## Potential Registrable Source Categories

Potential registrable categories include:

- Suite institutional records;
- Atlas jurisdiction resources;
- Certifier certification artifacts;
- Chronicle historical events;
- Anchor integrity references;
- Beacon signals;
- Attestor attestations;
- Navigator workflow definitions;
- approved tools and systems;
- approved media records;
- approved external records;
- historical records with durable institutional relevance.

Membership in a general category does not guarantee that every individual source is registrable.

---

## Public and Non-Public Sources

Public availability may support registration but is not always required.

Registry may consider:

- public Source Records;
- restricted institutional records;
- historical records preserved by archives;
- machine-readable sources without public presentation;
- public summaries referencing controlled source artifacts;
- entries whose metadata may be public while source content remains restricted.

Restricted registration requires:

- clear authority;
- documented access boundaries;
- rights review;
- privacy review;
- safety and security review;
- controlled publication rules.

---

## Registrability Classes

### Public Registrability

The SREG and its required metadata may be published openly.

### Restricted Registrability

The SREG may be created with limited or controlled publication because of rights, privacy, safety, security, or institutional policy.

### Historical Registrability

The Source Record may be registered after retirement, revocation, withdrawal, supersession, unavailability, or institutional dissolution.

### Provisional Registrability

Registry may preserve a controlled pending state while awaiting additional evidence, metadata, classification, or governance review.

### External Registrability

An external Source Record may be registered when authority, scope, identity, provenance, and durable relevance are sufficiently established.

---

## Historical and Unavailable Records

A Source Record may remain registrable even when it is no longer active or publicly available.

Historical Registrability may be supported by:

- archival copies;
- prior canonical URLs;
- version history;
- integrity references;
- institutional release records;
- Chronicle events;
- documented withdrawal;
- documented retirement;
- successor references;
- preservation records.

```text
Current unavailability does not erase historical registrability.
```

---

## External Records

External records may be registrable when:

- Source Institution is identifiable;
- source falls within Registry scope;
- one approved Record Type applies;
- durable relevance exists;
- minimum metadata is available;
- provenance can be preserved;
- rights and publication boundaries are respected;
- registration does not imply endorsement, ownership, or affiliation.

Registry should preserve the distinction between Suite-owned and externally controlled records.

---

## Duplicate and Redundant Sources

Registry should determine whether a proposed source is:

- already represented by an existing SREG;
- a new version of an existing Source Record;
- a duplicate publication;
- a mirror;
- a derivative that merits separate identity;
- a distinct record concerning the same subject;
- a successor requiring supersession;
- an archival representation of an unavailable source.

```text
Duplicate publication should not create duplicate Registry identity.
```

When an existing SREG already represents the source, Registry should update or relate that entry rather than create an unnecessary duplicate.

---

## Potentially Non-Registrable Sources

A proposed source may be non-registrable when:

- Source Authority cannot be established;
- Source Record cannot be identified reliably;
- source falls outside Registry scope;
- no approved Record Type applies;
- minimum metadata is unavailable;
- proposal represents only a duplicate or mirror;
- source is too transient to justify durable Registry identity;
- proposed SREG would misrepresent institutional authority;
- publication would violate rights, privacy, safety, or security requirements;
- proposal seeks endorsement rather than cataloging;
- record is fabricated, deceptive, or materially unsupported;
- proposal creates an unresolved contradiction with existing Registry records.

---

## Registrability Review Process

```text
Receive Proposal
  ↓
Confirm Source Authority
  ↓
Evaluate Registry Scope
  ↓
Identify Record Type
  ↓
Review Minimum Metadata
  ↓
Evaluate Provenance
  ↓
Check Duplicates and Conflicts
  ↓
Review Restrictions
  ↓
Assess Durable Relevance
  ↓
Record Registrability Outcome
```

A positive Registrability outcome authorizes Registry to proceed.

It does not complete SREG validation or publication.

---

## Registrability Review Record

A Registrability review should preserve:

- proposed Source Institution;
- proposed Authoritative Source Record;
- Source Authority outcome;
- scope determination;
- proposed Record Type;
- metadata assessment;
- provenance assessment;
- duplicate and conflict review;
- rights review;
- privacy review;
- safety and security review;
- durable-relevance assessment;
- review outcome;
- conditions or limitations;
- review date;
- reviewer or process;
- supporting references;
- required follow-up.

---

## Registrability Outcomes

### Registrable

The Source Record satisfies the required threshold.

Registry may proceed to Registry Identifier assignment and SREG construction.

### Registrable with Conditions

Registry may proceed subject to documented limitations, controls, follow-up, or future review.

### Provisionally Registrable

Registry may proceed only within a controlled pending state.

### Deferred

The Source Record may become registrable after additional evidence, metadata, classification, or governance review.

### Non-Registrable

The Source Record does not satisfy the current Registry threshold.

Registry should not create an operational SREG under the existing proposal.

### Rejected

The proposal is materially unsupported, deceptive, prohibited, or outside institutional scope.

These outcomes govern Registry action.

They do not determine the substantive truth or merit of the Source Record.

---

## Conditional Registrability

Conditions may include:

- additional authority evidence;
- restricted publication;
- metadata completion;
- provisional classification;
- scheduled review;
- source-version confirmation;
- rights clarification;
- relationship reconciliation;
- duplicate resolution;
- governance approval.

Conditions should be:

- explicit;
- attributable;
- dated;
- versioned;
- reviewable;
- capable of closure or renewal.

---

## Relationship to Source Authority

Source Authority establishes who controls the Source Record.

Registrability determines whether that record qualifies for a SREG.

```text
Source Authority
  ↓
Registrability
```

A record should not proceed when Registry cannot identify or support the Source Institution.

---

## Relationship to Identifier Assignment

Registry should assign a permanent Registry Identifier only after a positive Registrability outcome.

```text
Registrability authorizes identity creation.
Identifier assignment does not create Registrability.
```

Rejected, non-registrable, or deferred proposals should not receive production SREG identifiers unless a controlled reservation policy explicitly requires one.

---

## Relationship to SREG Construction

Registrability occurs before the SREG is fully constructed.

A positive outcome authorizes Registry to:

- assign Registry Identifier;
- preserve Source-System Identifier;
- apply the SREG Base Schema;
- apply the Record-Type Profile;
- establish references;
- establish relationships;
- assign initial Registry Status;
- assign initial Registry Lifecycle State;
- create the first Registry Entry Version.

---

## Relationship to Validation

Registrability and Validation are distinct.

### Registrability

Determines whether Registry should create the SREG.

### Validation

Determines whether the constructed SREG satisfies:

- SREG Base Schema;
- applicable Record-Type Profile;
- identifier requirements;
- source attribution requirements;
- status requirements;
- lifecycle requirements;
- version requirements;
- relationship requirements;
- provenance requirements;
- publication requirements.

```text
Registrability comes before construction.
Validation comes after construction.
```

---

## Relationship to Registry Lifecycle

A proposed entry may remain in a pending state while Registrability review is underway.

Potential relationships include:

- pending review before registration;
- Registrable outcome allowing progression toward Registered;
- conditional outcome requiring controlled status;
- Deferred outcome preserving review history without creating an active SREG;
- Non-Registrable or Rejected outcome preventing operational registration.

Registrability outcome and Registry Lifecycle State must remain distinct.

---

## Relationship to Registry Status

Registrability does not itself establish Registry Status.

A positive outcome may permit Registry to assign an initial Registry Status during SREG construction.

A source may be Registrable but subject to:

- restricted publication;
- pending validation;
- provisional recognition;
- historical presentation;
- additional review.

---

## Relationship to Corrections

A Registrability determination may require correction when:

- Source Authority was misidentified;
- source was outside Registry scope;
- wrong Record Type was selected;
- duplicate identity was overlooked;
- minimum metadata was materially incomplete;
- rights or restrictions were misstated;
- review outcome was recorded incorrectly.

Corrections should preserve:

- prior determination;
- corrected determination;
- reason;
- correction date;
- supporting evidence;
- affected Registry Entry Version;
- public Correction Record, when applicable.

---

## Relationship to Governance

Registry governance should control:

- Registrability thresholds;
- approved outcomes;
- exception handling;
- external-source eligibility;
- restricted registration;
- provisional registration;
- minimum metadata waivers;
- new Record-Type approval;
- contested decisions;
- review and appeal procedures;
- version changes to Registrability rules.

---

## Validation Requirements

A valid Registrability review should confirm:

- Source Authority review is complete or explicitly provisional;
- source falls within Registry scope;
- one approved primary Record Type applies;
- minimum metadata is present;
- required references are available;
- provenance is sufficient;
- duplicate and conflict checks were performed;
- rights, privacy, safety, and security conditions were reviewed;
- durable relevance was assessed;
- conditions and limitations are explicit;
- outcome is attributable and dated;
- human-readable and machine-readable review records agree.

---

## Current Directory Structure

```text
registry/
└── registrability/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Registrability page.

### `README.md`

The directory-level documentation explaining Registrability thresholds, requirements, outcomes, review procedures, limitations, and maintenance.

Future supporting materials may include:

```text
registrability/
├── index.html
├── README.md
├── registrability-review-schema.md
├── registrability-outcomes.md
├── minimum-metadata.md
├── external-records.md
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
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
- Registry Identifiers;
- Registry Provenance;
- Registry Validation;
- Registry Publication;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections;
- Registry Integration;
- Registry Policies;
- Registry Procedures;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Registrability architecture changes:

- update `index.html`;
- update this README;
- update Registrability thresholds;
- update minimum metadata requirements;
- update review outcomes;
- update review procedures;
- update Source Authority dependencies;
- update the SREG Base Schema;
- update affected Record-Type Profiles;
- update identifier-assignment requirements;
- update Validation requirements;
- update Registry Policies;
- update Registry Procedures;
- update examples;
- review affected pending proposals;
- preserve prior versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable materials.

---

## Guiding Principles

- Not every source requires a SREG.
- Source Authority is a prerequisite for Registrability.
- Registrability protects Registry quality and coherence.
- One approved primary Record Type must apply.
- Minimum metadata must support accurate representation.
- Provenance must preserve the path back to the source.
- Duplicate publication should not create duplicate Registry identity.
- Historical and unavailable records may remain registrable.
- External records require clear authority and scope.
- Conditions and limitations must be explicit.
- Registrability does not certify or endorse the source.
- Identifier assignment follows Registrability.
- Validation follows SREG construction.
- Registration does not transfer source authority.

---

## Disclaimer

A positive Registrability determination does not by itself establish:

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
- permanent availability;
- unrestricted publication.

Those remain controlled by the Source Institution, rights holder, governing authority, Source Record, applicable policy, or external system.

---

## Guiding Statement

> Authority makes the source attributable.
>
> Registrability determines whether Registry should create the SREG.
>
> The Registry threshold protects the catalog.
