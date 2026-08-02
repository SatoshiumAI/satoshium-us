# Satoshium Registry Relationships

## Overview

The `registry/relationships/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Relationships architecture.

The public page is published through:

```text
registry/relationships/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how Satoshium Registry preserves structured relationships among:

- Satoshium Registry Entries;
- Authoritative Source Records;
- Source Institutions;
- Suite institutions;
- certifications;
- attestations;
- signals;
- historical events;
- integrity references;
- workflows;
- dependencies;
- successors;
- archival records;
- approved external objects.

Relationships make Registry more than a collection of isolated entries.

They preserve the institutional context surrounding each SREG.

---

## Constitutional Position

Relationships operate within the SREG model after identity and classification are established.

```text
Source Authority
  ↓
Registrability
  ↓
Registry Identifier
  ↓
SREG
  ↓
Typed Relationships
```

Relationships connect records and institutions without transferring or absorbing authority.

---

## Core Principle

```text
Relationships connect identity, authority, history, and interoperability.
They do not absorb them.
```

Registry may publish a relationship without becoming authoritative for the substantive meaning of every object it connects.

---

## Canonical Relationship Model

```text
Source Identifier
  ↓
Relationship Type
  ↓
Target Identifier
```

A complete Registry relationship should also preserve:

- source identifier domain;
- target identifier domain;
- direction;
- authority;
- effective date;
- end date, when applicable;
- version context;
- relationship status;
- supporting references;
- correction history.

---

## Why Relationships Matter

Records rarely exist in isolation.

Examples include:

- a certification concerns a subject;
- an attestation refers to an artifact;
- a signal announces a milestone;
- an Anchor reference preserves integrity;
- a Chronicle event documents change;
- a workflow coordinates institutional action;
- a successor replaces a prior record;
- an archive preserves an unavailable source.

Relationships allow Registry to preserve these connections in structured form.

---

## Relationship Requirements

Every governed relationship should identify:

- relationship identifier, when required;
- source identifier;
- source identifier domain;
- target identifier;
- target identifier domain;
- relationship type;
- direction;
- relationship authority;
- effective date;
- end date, when applicable;
- version context;
- relationship status;
- supporting reference;
- assertion or creation date;
- correction and history references.

---

## Relationship Characteristics

### Typed

Every relationship uses an approved controlled relationship type.

### Directional

Every relationship identifies a source and target.

### Attributable

The institution or process asserting the relationship is preserved.

### Version-Aware

The relationship may apply to a continuing SREG, one Registry Entry Version, one Source-Record Version, or one artifact version.

### Time-Aware

Effective dates, end dates, withdrawal dates, and historical applicability may be preserved.

### Correctable

Changes must preserve prior values and documented history.

---

## Initial Controlled Relationship Types

Initial controlled values may include:

- sourced from;
- source of;
- produced by;
- produces;
- references;
- referenced by;
- concerns;
- concerned by;
- certifies;
- certified by;
- attests to;
- attested by;
- anchored by;
- integrity reference for;
- documents;
- documented by;
- announces;
- announced by;
- parent jurisdiction;
- child jurisdiction;
- depends on;
- dependency of;
- integrates with;
- coordinated through;
- supersedes;
- superseded by;
- successor to;
- predecessor of;
- derivative of;
- has derivative;
- version of;
- archived as;
- archival representation of.

Final labels, inverses, semantics, and usage requirements remain subject to Registry governance.

---

## Relationship Categories

### Source Relationships

Connect a SREG to:

- Authoritative Source Record;
- Source Institution;
- repository;
- package;
- canonical publication;
- canonical JSON;
- generation manifest;
- evidence record;
- archival snapshot;
- integrity reference.

### Institutional Relationships

Connect SREGs to Suite or external institutions responsible for:

- creation;
- issuance;
- maintenance;
- publication;
- verification;
- preservation;
- coordination.

### Operational Relationships

Connect:

- tools;
- services;
- workflows;
- dependencies;
- inputs;
- outputs;
- integrations.

### Historical Relationships

Connect:

- predecessors;
- successors;
- superseded entries;
- prior versions;
- archival records;
- Chronicle events;
- unavailable sources;
- historical representations.

### Trust Relationships

Connect:

- certifications;
- attestations;
- evidence;
- integrity references;
- verification artifacts.

### Discovery Relationships

Connect:

- Beacon signals;
- announcements;
- media;
- public pages;
- discovery metadata.

---

## Direction and Inverse Relationships

Relationships remain directional even when an inverse form is defined.

Example:

```text
SREG-JUR-2026-0001 certified by SC-CERT-2026-0001
SC-CERT-2026-0001 certifies SREG-JUR-2026-0001
```

Each direction should use the controlled type appropriate to the source and target.

```text
A relationship may have a defined inverse.
It should not be treated as automatically symmetrical.
```

---

## Symmetrical Relationships

Some relationship types may be symmetrical.

Potential examples include:

- integrates with;
- related to;
- interoperates with.

Symmetry must be explicitly defined by the controlled relationship type.

Registry should not infer symmetry merely because two objects reference each other.

---

## Relationship Authority

Every material relationship should identify who is authorized to assert it.

Potential authorities include:

- Registry, for Registry-owned catalog relationships;
- Source Institution, for source-controlled relationships;
- Certifier, for certification relationships;
- Attestor, for attestation relationships;
- Chronicle, for historical event relationships;
- Anchor, for integrity-reference relationships;
- Beacon, for signal relationships;
- Navigator, for workflow relationships;
- approved external institutions.

Registry may publish a relationship asserted by another institution while preserving that institution as the relationship authority.

---

## Relationship Assertion Classes

### Registry-Asserted

Registry creates the relationship as part of catalog organization or maintenance.

### Source-Asserted

The Source Institution states or controls the relationship.

### Derived

The relationship is derived from structured evidence or interoperable source data.

### Provisional

The relationship is published with explicit uncertainty or pending review.

---

## Relationship Status

Potential relationship conditions may include:

### Active

The relationship currently applies.

### Historical

The relationship applied previously and remains preserved.

### Superseded

The relationship has been replaced by a newer relationship.

### Revoked

The asserting authority withdrew the relationship.

### Disputed

Competing claims or interpretations remain unresolved.

### Provisional

The relationship is pending additional evidence or review.

### Invalid

The relationship was erroneous or structurally defective.

Relationship Status must remain separate from:

- Registry Status;
- Registry Lifecycle State;
- Source-Record Status;
- Certification Status;
- Attestation Status.

---

## Version Context

A relationship may apply to:

- the continuing SREG;
- one Registry Entry Version;
- one Source-Record Version;
- one artifact version;
- one schema version;
- one historical period;
- all future versions until withdrawn.

```text
A relationship applying to one version does not automatically apply to every later version.
```

---

## Temporal Context

Relationships may preserve:

- assertion date;
- effective date;
- future effective date;
- review date;
- end date;
- withdrawal date;
- supersession date;
- historical applicability.

Temporal context should be explicit whenever a relationship changes over time.

---

## Relationship Evidence

Material relationships should preserve supporting evidence or references.

Potential evidence includes:

- Source Record metadata;
- Certification Package references;
- attestation statements;
- Chronicle events;
- Anchor integrity references;
- Beacon announcements;
- workflow records;
- repository metadata;
- version history;
- governance decisions;
- public institutional statements.

---

## Relationship Objects

Registry may represent relationships as:

- embedded SREG structures;
- separately identifiable relationship objects;
- machine-readable relationship records;
- human-readable relationship summaries.

An illustrative machine-readable structure is:

```text
relationship_type: "certified_by"
source_identifier: "SREG-JUR-2026-0001"
source_domain: "satoshium-registry"
target_identifier: "SC-CERT-2026-0001"
target_domain: "satoshium-certifier"
authority: "Satoshium Certifier"
status: "active"
```

Final field names and controlled values remain subject to the SREG Base Schema and Registry Schema Specification.

---

## Source Record Relationships

Every SREG should preserve a primary relationship to its Authoritative Source Record.

```text
SREG
  ↓
sourced from
  ↓
Authoritative Source Record
```

Supporting relationships may connect the SREG to:

- Source Institution;
- repository;
- canonical HTML page;
- canonical JSON record;
- generation manifest;
- evidence;
- archived snapshot;
- integrity reference.

---

## Certification Relationships

A certification relationship may preserve the operational chain:

```text
Certification Subject
  ↓
Certification Package
  ↓
SCPR
  ↓
SCR
  ↓
SCRD
  ↓
Certification SREG
```

Certifier remains authoritative for:

- Certification Package;
- Certification Outcome;
- Certification Status;
- SCPR;
- SCR;
- SCRD.

Registry remains authoritative for the SREG and Registry-owned relationship metadata.

---

## Attestation Relationships

Attestation relationships may connect:

- Attestation SREG to Attestor-owned Attestation Record;
- attestation to subject;
- attestation to evidence;
- attestation to certification;
- attestation to integrity reference;
- attestation to historical event;
- attestation to issuing institution.

Attestor remains authoritative for the attestation statement.

---

## Jurisdiction Relationships

Jurisdiction relationships may include:

- parent jurisdiction;
- child jurisdiction;
- part of;
- contains;
- predecessor jurisdiction;
- successor jurisdiction;
- merged into;
- split from;
- boundary changed by;
- governed by;
- recognized by.

Atlas remains authoritative for Atlas jurisdiction intelligence and source-domain jurisdiction relationships.

---

## Tool and Workflow Relationships

Tool SREGs may preserve:

- depends on;
- dependency of;
- integrates with;
- produces;
- consumes;
- operated by;
- implements;
- coordinated through;
- validated by;
- published by;
- replaced by;
- version of.

Navigator remains authoritative for Navigator-created workflow definitions and coordination records.

---

## Historical and Archival Relationships

Registry should preserve relationships among:

- prior and current versions;
- predecessors and successors;
- superseded and replacement SREGs;
- original records and archival copies;
- active and historical records;
- withdrawn sources and preserved snapshots;
- SREGs and Chronicle events;
- records and integrity references.

Historical relationships preserve continuity without implying current applicability.

---

## Relationship Corrections

A relationship correction may be required when:

- source identifier is incorrect;
- target identifier is incorrect;
- identifier domain is incorrect;
- relationship type is misclassified;
- direction is reversed;
- authority is misidentified;
- effective date is incorrect;
- version context is omitted or wrong;
- a duplicate relationship exists;
- a provisional relationship is presented as confirmed.

---

## Correction Without Erasure

Corrected relationships should preserve:

- prior source identifier;
- prior target identifier;
- prior relationship type;
- corrected values;
- correction reason;
- correction date;
- correction authority;
- affected Registry Entry Version;
- supporting evidence;
- replacement or supersession relationship.

The original relationship history should remain discoverable.

---

## Relationship Validation

Validation should confirm:

- source identifier exists or is a valid external reference;
- target identifier exists or is a valid external reference;
- identifier domains are declared;
- relationship type is approved;
- direction is valid;
- relationship authority is identified;
- effective dates are coherent;
- version context is explicit when required;
- inverse relationship is correct when published;
- duplicate relationships are prevented;
- relationship status is valid;
- supporting references are preserved;
- human-readable and machine-readable forms agree.

---

## Invalid Relationship Conditions

Invalid conditions include:

- unrecognized relationship type;
- missing source identifier;
- missing target identifier;
- undeclared identifier domain;
- reversed or ambiguous direction;
- unsupported authority claim;
- impossible or contradictory dates;
- incorrect inverse relationship;
- duplicate relationship;
- relationship applied to the wrong version;
- historical relationship presented as current;
- provisional relationship presented as confirmed;
- human-readable and machine-readable mismatch.

---

## Relationship to Identifiers

Identifiers provide the stable endpoints used by Registry relationships.

A relationship should preserve both the identifier and its domain.

Examples include:

- Registry Identifier;
- Source-System Identifier;
- Certification Identifier;
- Attestation Identifier;
- Chronicle Identifier;
- Anchor reference;
- external identifier.

Registry should not infer identifier meaning from value alone.

---

## Relationship to Provenance

Provenance preserves the path from a SREG back to the Source Record and Source Institution.

Relationships connect that path to other records, institutions, artifacts, and events.

```text
Provenance explains origin.
Relationships explain context.
```

---

## Relationship to Publication

Official publication should expose relationships consistently across:

- human-readable SREG;
- machine-readable SREG;
- relationship summaries;
- linked record pages;
- version history;
- correction records;
- supersession notices;
- archival presentation.

---

## Relationship to Lifecycle

Relationships may change while a SREG remains the same Registry object.

Registry should preserve:

- current relationships;
- historical relationships;
- superseded relationships;
- revoked relationships;
- provisional relationships;
- relationship changes tied to lifecycle events.

Relationship Status and Registry Lifecycle State remain separate.

---

## Relationship to Corrections

Relationship corrections should follow Registry correction requirements.

Corrections should be:

- attributable;
- dated;
- version-aware;
- evidence-supported;
- historically preserved;
- reflected in human-readable and machine-readable forms.

---

## Relationship to Governance

Registry governance should control:

- approved relationship types;
- inverse definitions;
- symmetry rules;
- authority requirements;
- status values;
- version requirements;
- evidence requirements;
- validation rules;
- exception handling;
- relationship-object identifiers;
- deprecation and migration rules.

---

## Current Directory Structure

```text
registry/
└── relationships/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Relationships page.

### `README.md`

The directory-level documentation explaining relationship structure, authority, direction, status, version context, evidence, validation, correction, and maintenance.

Future supporting materials may include:

```text
relationships/
├── index.html
├── README.md
├── relationship-types.md
├── inverse-relationships.md
├── relationship-statuses.md
├── relationship-schema.md
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
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
- Registry Provenance;
- Registry Validation;
- Registry Publication;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections;
- Registry Integration;
- Registry Policies;
- Registry Procedures;
- Registry Governance;
- Registry Controlled Values;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Relationship architecture changes:

- update `index.html`;
- update this README;
- update controlled relationship types;
- update inverse definitions;
- update symmetry rules;
- update relationship statuses;
- update authority requirements;
- update version and temporal rules;
- update evidence requirements;
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

- Relationships must be typed.
- Relationships must be directional.
- Relationship authority must be preserved.
- Identifier domains must be explicit.
- Relationships may be version-specific.
- Relationships may be time-specific.
- Inverse relationships must be defined.
- Symmetry must not be assumed.
- Historical relationships must remain discoverable.
- Corrections must preserve prior states.
- Provenance and relationships remain distinct.
- Registry may publish another institution's relationship without absorbing its authority.
- Human-readable and machine-readable forms must agree.
- Relationships connect context without transferring authority.

---

## Disclaimer

A Registry relationship does not by itself establish:

- Source Authority;
- certification;
- attestation;
- verification;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- endorsement;
- affiliation;
- permanence;
- current applicability;
- source truth.

Those remain controlled by the applicable Source Institution, rights holder, governing authority, asserting institution, Source Record, or external system.

---

## Guiding Statement

> Registry becomes meaningful when identity is preserved together with context.
>
> Relationships connect authoritative objects.
>
> They do not collapse their authority.
