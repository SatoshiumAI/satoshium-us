# Satoshium Registry Controlled Values

## Overview

The `registry/controlled-values/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Controlled Values framework.

The public page is published through:

```text
registry/controlled-values/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define the governed vocabularies, enumerations, codes, statuses, lifecycle states, relationship types, validation outcomes, publication notices, and other approved values used across:

- Satoshium Registry Entries;
- Registry schemas;
- Record-Type Profiles;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Validation;
- Publication;
- Versioning;
- Corrections;
- Governance;
- Interoperability.

Controlled Values ensure that human-readable and machine-readable Registry materials use the same institutional language.

---

## Constitutional Position

Controlled Values operate beneath Registry Governance and within the SREG Base Schema, Record-Type Profiles, Rules, Policies, Procedures, Validation, Publication, and Interoperability requirements.

```text
Suite Standards
  ↓
Registry Governance
  ↓
Controlled-Value Sets
  ↓
Schemas and Profiles
  ↓
Published SREGs
```

Controlled Values define approved language.

They do not replace the institutional Rules, Policies, Procedures, or authority determinations governing when each value applies.

---

## Core Principle

```text
Structure organizes data.
Controlled Values preserve meaning.
Governance keeps that meaning stable.
```

A controlled value should have one canonical representation, one governed meaning, and a traceable history.

---

## Why Controlled Values Matter

Without governed values, equivalent concepts may be expressed through inconsistent:

- labels;
- abbreviations;
- capitalization;
- spelling;
- machine-readable codes;
- relationship terms;
- status names;
- lifecycle names;
- outcome descriptions;
- notice types;
- interpretations.

Controlled Values reduce ambiguity and support reliable Validation, Publication, and Interoperability.

---

## Canonical Controlled-Value Model

```text
Value Set
  ↓
Approved Value
  ↓
Definition
  ↓
Usage Rule
  ↓
Schema Field
```

Every value belongs to a defined value set and should be used only in fields and contexts approved for that value.

---

## Controlled-Value Requirements

Every governed value should identify:

- value-set identifier;
- value-set title;
- value-set version;
- canonical value;
- machine-readable code;
- human-readable label;
- definition;
- usage rule;
- authority;
- effective date;
- status;
- aliases or legacy values;
- replacement value, when applicable;
- related schema fields;
- change history.

---

## Controlled-Value Characteristics

### Canonical

One approved value represents the concept in current Registry materials.

### Defined

Every value has a stable institutional definition and usage boundary.

### Versioned

Changes to values and value sets preserve prior versions and effective dates.

### Validatable

Schemas and Procedures can determine whether a submitted value is approved.

### Governed

Creation, amendment, deprecation, retirement, and migration require approved authority.

---

## Machine-Readable Controlled Values

Registry now publishes a canonical machine-readable Controlled Values resource alongside this human-readable framework.

```text
Controlled Values Framework
  ↓
controlled-values.json
  ↓
Schemas and Record-Type Profiles
  ↓
Published SREGs
```

Current production metadata:

- **Canonical File:** `controlled-values.json`
- **Version:** `1.0`
- **Authority:** Satoshium Registry
- **Effective Date:** August 14, 2026
- **Canonical URL:** `https://satoshium.us/registry/controlled-values/controlled-values.json`
- **Current Machine-Readable Scope:** the initial published resource operationalizes the **Registry Status** value set beginning with the production value **Active**.

The machine-readable resource does not replace this institutional framework.

This README and the public Controlled Values page define the governed meaning, architecture, usage boundaries, and maintenance expectations of Controlled Values. `controlled-values.json` provides the canonical machine-readable publication of value sets as they are formally operationalized.

---

## Core Controlled-Value Sets

The Registry Controlled Values framework may include:

- Registry Record Types;
- Registry Status values;
- Registry Lifecycle States;
- Source Authority Review Outcomes;
- Registrability Outcomes;
- Identifier States;
- Relationship Types;
- Relationship Statuses;
- Validation Outcomes;
- Validation Finding Classes;
- Publication Readiness Outcomes;
- Publication Notice Types;
- Correction Categories;
- Access and Restriction Conditions;
- Custody Types;
- Provenance Artifact Types;
- Version Change Classes;
- Governance Decision Statuses;
- Policy Statuses;
- Procedure Statuses;
- Exception Statuses;
- Preservation Conditions.

---

## Registry Record Types

Initial Registry Record Types may include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal;
- Event;
- Integrity Reference;
- Workflow;
- Institution;
- Schema;
- Policy;
- Procedure;
- Governance Decision.

Final Record Types and Profile assignments remain subject to Registry Governance.

---

## Registry Status Values

Registry Status describes the current Registry condition of the SREG.

### Pending

Under Registry review and not yet operational.

### Active

Valid and currently published for operational use.

### Restricted

Operational but subject to access or publication limits.

### Disputed

A material Registry or source conflict remains unresolved.

### Superseded

Replaced by a successor SREG or Registry representation.

### Revoked

Withdrawn from valid operational use by Registry authority.

### Retired

Intentionally removed from active use without direct revocation.

### Archived

Preserved primarily for historical reference.

Registry Status must remain separate from:

- Source-Record Status;
- Certification Status;
- Attestation Status;
- Registry Lifecycle State.

---

## Registry Lifecycle States

Registry Lifecycle State describes where the SREG is within its institutional lifecycle.

Initial values may include:

- Proposed;
- Under Review;
- Registered;
- Published;
- Updated;
- Superseded;
- Revoked;
- Retired;
- Archived.

Permitted transitions and exact semantics remain governed by the Registry Lifecycle framework.

---

## Source Authority Review Outcomes

### Confirmed

Source Authority is sufficiently established.

### Confirmed with Conditions

Authority is sufficient, but limitations apply.

### Delegated

Authority is exercised through a documented delegation.

### Historical

Authority applied historically and remains relevant for provenance.

### External

Authority belongs to an institution outside the Suite.

### Conflicted

Competing authority claims remain unresolved.

### Insufficient

Available evidence does not support Source Authority.

### Not Evaluated

Review has not yet occurred.

---

## Registrability Outcomes

### Registrable

Registrability requirements are satisfied.

### Conditionally Registrable

Registration may proceed under documented conditions.

### Provisionally Registrable

Registration may proceed pending additional review.

### Restricted Registrable

Registration is permitted with access limitations.

### Historical Registrable

The record is appropriate for historical Registry preservation.

### Not Registrable

One or more blocking conditions prevent registration.

### Indeterminate

Available evidence is insufficient to decide.

### Not Evaluated

Review has not yet occurred.

---

## Identifier States

### Reserved

Held for a proposed Registry object.

### Assigned

Formally assigned to a SREG.

### Published

Resolves through an official Registry publication.

### Superseded

Remains resolvable but points to a successor context.

### Revoked

No longer valid for active operational use.

### Archived

Preserved for historical resolution.

Identifier State describes the condition of the identifier.

It does not replace Registry Status or Registry Lifecycle State.

---

## Relationship Types

Initial Relationship Types may include:

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
- depends on;
- dependency of;
- integrates with;
- supersedes;
- superseded by;
- successor to;
- predecessor of;
- derived from;
- has derivative;
- version of;
- archived as;
- archival representation of.

Final labels, codes, inverse definitions, and symmetry rules remain subject to Registry Governance.

---

## Relationship Statuses

Initial Relationship Status values may include:

- Active;
- Historical;
- Provisional;
- Disputed;
- Superseded;
- Revoked;
- Invalid.

Relationship Status remains separate from Registry Status, Registry Lifecycle State, and Source-Record Status.

---

## Validation Outcomes

Initial Validation Outcomes include:

- Valid;
- Valid with Warnings;
- Conditionally Valid;
- Invalid;
- Indeterminate;
- Not Evaluated.

These values describe Registry-object conformance.

They do not certify the Source Record.

---

## Validation Finding Classes

Initial finding classes include:

- Blocking Error;
- Warning;
- Exception;
- Informational Finding.

These values support consistent Validation reporting and decision thresholds.

---

## Publication Readiness Outcomes

Initial Publication Readiness Outcomes include:

- Ready;
- Ready with Notices;
- Restricted;
- Not Ready.

These values describe whether a validated SREG may proceed to official publication.

---

## Publication Notice Types

Initial notice types may include:

- provisional publication;
- restricted source access;
- source unavailable;
- validation warning;
- correction issued;
- superseded entry;
- revoked entry;
- retired entry;
- archived entry;
- historical record;
- disputed relationship;
- external-source disclaimer;
- rights or reuse limitation;
- governance exception;
- migration notice.

---

## Correction Categories

Initial Correction Categories may include:

- Identifier Correction;
- Source Attribution Correction;
- Classification Correction;
- Provenance Correction;
- Relationship Correction;
- Status Correction;
- Lifecycle Correction;
- Version Correction;
- Publication Correction;
- Schema or Format Correction;
- Typographical Correction.

---

## Access and Restriction Conditions

Initial Access and Restriction Conditions may include:

- Public;
- Public Metadata Only;
- Restricted;
- Controlled Access;
- Internal;
- Withdrawn;
- Unavailable.

These values should be used together with applicable access, rights, privacy, safety, security, and publication requirements.

---

## Custody Types

Initial Custody Types may include:

- Original Custody;
- Delegated Custody;
- Archival Custody;
- Successor Custody;
- External Custody.

```text
Custody describes possession or preservation.
It does not establish Source Authority.
```

---

## Provenance Artifact Types

Initial Provenance Artifact Types may include:

- Original Source;
- Canonical Source;
- Derived Artifact;
- Generated Artifact;
- Mirror;
- Archived Snapshot;
- Generation Manifest;
- Integrity Reference;
- Supporting Evidence.

These values help distinguish source origin, derivation, preservation, and evidentiary role.

---

## Version Change Classes

Initial Version Change Classes may include:

- Major;
- Minor;
- Patch;
- Non-Versioned;
- Rollback;
- Migration.

Final increment rules remain governed by the Registry Versioning framework.

---

## Governance Decision Statuses

Initial Governance Decision Statuses may include:

- Draft;
- Under Review;
- Approved;
- Active;
- Amended;
- Superseded;
- Retired;
- Archived.

These values describe Governance Decision Records rather than SREG lifecycle conditions.

---

## Policy and Procedure Statuses

Initial Policy and Procedure Statuses may include:

- Draft;
- Under Review;
- Approved;
- Active;
- Revised;
- Superseded;
- Retired;
- Archived.

Policy and Procedure status values should preserve their own authority and version history.

---

## Exception Statuses

Initial Exception Statuses may include:

- Requested;
- Under Review;
- Approved;
- Approved with Conditions;
- Denied;
- Expired;
- Revoked;
- Closed.

---

## Preservation Conditions

Initial Preservation Conditions may include:

- Current;
- Historically Preserved;
- Archived;
- Source Unavailable;
- Partial Preservation;
- Integrity Verified;
- Integrity Unverified;
- Preservation Restricted.

---

## Machine-Readable Codes

Controlled Values use stable machine-readable codes while preserving corresponding human-readable labels.

The current production resource includes:

```text
registry_status: "active"
```

Framework examples for additional governed sets include:

```text
registry_lifecycle_state: "published"
validation_outcome: "valid_with_warnings"
publication_readiness: "ready_with_notices"
```

The canonical machine-readable publication is:

```text
https://satoshium.us/registry/controlled-values/controlled-values.json
```

Additional value sets and codes should be added to `controlled-values.json` as they are formally operationalized and reconciled with:

- the SREG Base Schema;
- applicable Record-Type Profiles;
- the Registry Schema Specification;
- Registry Governance.

---

## Labels, Codes, and Definitions

Each controlled concept may include:

- canonical machine-readable code;
- canonical human-readable label;
- plain-language description;
- formal institutional definition;
- usage conditions;
- prohibited uses;
- legacy labels;
- aliases;
- replacement value, when deprecated.

```text
Labels support presentation.
Codes support consistency.
Definitions preserve meaning.
```

---

## Aliases and Legacy Values

Registry may preserve aliases for:

- historic terminology;
- deprecated labels;
- prior machine-readable codes;
- common abbreviations;
- source-system equivalents;
- migration compatibility.

Aliases should not replace the current canonical value in new Registry records.

Historical records may continue to preserve the original value when required for authenticity and interpretation.

---

## Deprecation and Retirement

When a value is deprecated or retired, Registry should preserve:

- prior canonical code;
- prior label;
- definition;
- effective period;
- deprecation date;
- retirement date;
- reason;
- replacement value, when applicable;
- migration guidance;
- historical interpretation requirements.

```text
A retired value may disappear from new records.
It must remain understandable in historical records.
```

---

## Controlled-Value Versioning

Value-set changes should preserve:

- prior value-set version;
- new value-set version;
- change date;
- effective date;
- approval authority;
- added values;
- amended values;
- deprecated values;
- retired values;
- replacement mappings;
- affected schemas;
- affected Record-Type Profiles;
- migration requirements;
- historical publication.

---

## Controlled-Value Governance

Registry Governance should control:

- creation of value sets;
- value definitions;
- codes;
- labels;
- usage rules;
- aliases;
- inverse relationships;
- symmetry rules;
- versioning;
- deprecation;
- retirement;
- migration;
- exception handling;
- publication;
- historical preservation.

---

## Controlled-Value Validation

Validation should confirm:

- value belongs to the approved value set;
- value-set version is declared when required;
- machine-readable code and human-readable label correspond;
- deprecated values are not used in new records without authorization;
- retired values remain interpretable historically;
- field usage matches the value definition;
- aliases are not used as canonical values;
- human-readable and machine-readable forms agree;
- source-owned values are not replaced improperly;
- migration mappings are preserved.

---

## Invalid Controlled-Value Conditions

Invalid conditions include:

- unrecognized value;
- incorrect machine-readable code;
- label and code mismatch;
- value used in the wrong field;
- deprecated value used without authorization;
- retired value presented as current;
- alias used as canonical value;
- source-owned value overwritten by Registry terminology;
- undefined inverse relationship;
- assumed symmetry without Governance;
- missing value-set version when required;
- human-readable and machine-readable mismatch.

---

## Relationship to Schemas

Schemas identify:

- which fields require Controlled Values;
- which value set applies;
- cardinality;
- formatting;
- conditional requirements.

Controlled Values define the permitted institutional language within those fields.

```text
Schemas define structure.
Controlled Values define permitted institutional language.
```

---

## Relationship to Record-Type Profiles

Record-Type Profiles may:

- require specific Controlled Values;
- limit a field to a subset of a value set;
- define type-specific relationships;
- define type-specific status conditions;
- require additional notice values;
- require additional provenance values;
- prohibit values that do not apply to the Record Type.

---

## Relationship to Source Values

Registry-controlled values and Source-System values should remain distinct when their meanings or authorities differ.

Registry may preserve:

- original source value;
- source-value definition;
- Registry mapping;
- mapping authority;
- mapping confidence;
- mapping limitation;
- effective mapping version.

```text
Mapping supports interoperability.
It does not transfer authority over the source value.
```

---

## Relationship to Interoperability

Controlled Values support Interoperability by providing stable meanings, codes, and mappings.

Interoperability records should preserve:

- canonical Registry value;
- external equivalent;
- mapping direction;
- mapping authority;
- mapping version;
- known semantic differences;
- deprecation history;
- migration history.

---

## Relationship to Governance

Registry Governance determines:

- who may create a value set;
- who may approve a value;
- who may amend a definition;
- how values are versioned;
- how aliases are handled;
- how values are deprecated or retired;
- how migrations are approved;
- how historical interpretation is preserved.

---

## Relationship to Validation

Validation uses Controlled Values to determine whether SREG fields contain approved and contextually correct terms.

Validation should not treat an approved value as correct merely because it exists in a value set.

The value must also be valid for the specific field, Record Type, version, and institutional context.

---

## Relationship to Publication

Publication should expose canonical labels and codes consistently across:

- human-readable SREGs;
- machine-readable SREGs;
- downloadable artifacts;
- notices;
- history;
- correction records;
- relationship records;
- archival presentations.

---

## Current Directory Structure

```text
registry/
└── controlled-values/
    ├── index.html
    ├── README.md
    └── controlled-values.json
```

### `index.html`

The public Registry Controlled Values page.

### `README.md`

The directory-level documentation explaining value sets, codes, labels, definitions, statuses, outcomes, aliases, versioning, Governance, Validation, and maintenance.

### `controlled-values.json`

The canonical machine-readable publication of Registry Controlled-Value sets as they are formally operationalized. Version 1.0 begins with the production Registry Status value set and may be expanded through governed updates without fragmenting each value set into a separate file unless operational requirements later justify that structure.

Future supporting materials may include:

```text
controlled-values/
├── index.html
├── README.md
├── controlled-values.json
├── record-types.md
├── registry-statuses.md
├── lifecycle-states.md
├── authority-outcomes.md
├── registrability-outcomes.md
├── identifier-states.md
├── relationship-types.md
├── relationship-statuses.md
├── validation-outcomes.md
├── publication-notices.md
├── correction-categories.md
├── access-conditions.md
├── custody-types.md
├── provenance-artifact-types.md
├── version-change-classes.md
├── governance-statuses.md
├── mappings/
├── history/
└── versions/
```

These materials should be introduced only when corresponding operational value sets are formally established.

---

## Relationship to Other Registry Documentation

This directory should remain consistent with:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Governance;
- Registry Source Authority;
- Registry Registrability;
- Registry Identifiers;
- Registry Relationships;
- Registry Provenance;
- Registry Validation;
- Registry Publication;
- Registry Versioning;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections;
- Registry Integration;
- Registry Catalog;
- Registry History;
- Registry Transparency;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Controlled-Value architecture changes:

- update `index.html`;
- update this README;
- update `controlled-values.json`;
- update value-set identifiers;
- update definitions;
- update codes and labels;
- update usage rules;
- update aliases and legacy values;
- update inverse relationships;
- update symmetry rules;
- update version information;
- update deprecation and retirement records;
- update migration mappings;
- update affected schemas;
- update affected Record-Type Profiles;
- update Validation requirements;
- update Publication requirements;
- update Registry Policies;
- update Registry Procedures;
- preserve prior value-set versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable materials.

---

## Guiding Principles

- Controlled Values must be governed.
- Machine-readable Controlled Values must remain aligned with the human-readable framework.
- Every canonical value must be defined.
- Codes and labels must correspond.
- Value-set versions must be preserved.
- Aliases must not replace canonical values.
- Deprecated values must remain historically interpretable.
- Retired values must remain discoverable in prior records.
- Source-owned values must not be overwritten.
- Mappings do not transfer Source Authority.
- Relationship inverses must be governed.
- Symmetry must not be assumed.
- Schemas and Controlled Values must remain aligned.
- Human-readable and machine-readable forms must agree.
- Controlled Values must not silently change meaning.
- Governance must preserve semantic continuity.

---

## Disclaimer

Registry Controlled Values do not by themselves establish:

- Source Authority;
- Source-Record truth;
- certification;
- attestation;
- verification;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- endorsement;
- affiliation;
- identity between similar source and Registry terms;
- authority outside Registry scope.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, Rule, Policy, Procedure, or external system.

---

## Guiding Statement

> Structure organizes data.
>
> Controlled Values preserve meaning.
>
> Governance keeps that meaning stable.
