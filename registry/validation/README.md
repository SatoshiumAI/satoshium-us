# Satoshium Registry Validation

## Overview

The `registry/validation/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Validation framework.

The public page is published through:

```text
registry/validation/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how Satoshium Registry confirms that a constructed Satoshium Registry Entry, or SREG, satisfies the structural, institutional, identifier, provenance, relationship, version, lifecycle, status, correction, and publication requirements governing Registry records.

Validation determines whether a SREG is ready for official publication or continued presentation as a valid Registry object.

Validation does not certify the substantive truth of the Authoritative Source Record.

---

## Constitutional Position

Validation occurs after SREG construction and before publication or material republication.

```text
Source Authority
  ↓
Registrability
  ↓
Identifier Assignment
  ↓
SREG Construction
  ↓
Validation
  ↓
Publication
```

Registrability determines whether Registry should create the SREG.

Validation determines whether the constructed SREG conforms to the applicable Registry requirements.

---

## Core Principle

```text
Validation confirms Registry conformance.
Certification evaluates a subject.
```

Registry Validation and Certifier Certification remain institutionally distinct.

Registry validates the SREG as a Registry object.

Certifier evaluates a certification subject under applicable certification standards and methodology.

---

## Canonical Validation Model

```text
Registry Rules
  +
SREG Base Schema
  +
Record-Type Profile
  +
Institutional Requirements
  =
Validation Result
```

Validation applies the approved requirements to one defined Registry Entry Version.

---

## Why Validation Matters

A source may be registrable while the constructed SREG still contains defects.

Potential defects include:

- incomplete identifiers;
- incorrect Source Institution attribution;
- broken source references;
- invalid controlled values;
- missing provenance;
- incorrect relationship direction;
- collapsed version domains;
- inconsistent status or lifecycle fields;
- silent corrections;
- disagreement between HTML and JSON forms.

Validation protects the integrity of the Registry object before publication.

---

## Validation Domains

Registry Validation may include:

- Source Authority validation;
- Registrability validation;
- Identifier validation;
- schema validation;
- Record-Type Profile validation;
- provenance validation;
- relationship validation;
- version validation;
- Registry Status validation;
- Registry Lifecycle validation;
- correction validation;
- publication validation;
- human-readable and machine-readable consistency validation.

---

## Validation Classes

### Structural Validation

Confirms:

- required fields;
- data types;
- formats;
- cardinality;
- schema conformance;
- machine-readable parsing.

### Institutional Validation

Confirms:

- Registry authority;
- Source Authority;
- scope;
- institutional boundaries;
- appropriate ownership of fields and outcomes.

### Referential Validation

Confirms:

- identifiers;
- source references;
- relationships;
- canonical URLs;
- linked records;
- historical references.

### Semantic Validation

Confirms controlled values and fields are used according to their defined meaning.

### Temporal Validation

Confirms dates, versions, effective periods, supersession, and lifecycle order are coherent.

### Publication Validation

Confirms official human-readable and machine-readable forms are complete, aligned, and ready for release.

---

## Validation Inputs

Every validation should identify the requirement versions being applied.

Potential inputs include:

- SREG Base Schema Version;
- Record-Type Profile Version;
- Registry Schema Specification Version;
- Registry Rules Version;
- Registry Policy Version;
- Registry Procedure Version;
- Suite Standards Version;
- Suite Methodology Version;
- Suite Interoperability requirements;
- controlled-value set versions;
- validation checklist or workflow version.

```text
A validation result is meaningful only when the governing requirement versions are known.
```

---

## Source Authority Validation

Source Authority validation should confirm:

- Source Institution is identified;
- Authoritative Source Record is identifiable;
- authority evidence or review reference exists;
- custody is not represented as authority;
- mirrors and derivatives are not presented as canonical sources;
- authority changes are historically preserved;
- Registry does not claim source-domain authority.

---

## Registrability Validation

Registrability validation should confirm:

- positive Registrability outcome exists;
- conditions or limitations are preserved;
- approved Record Type applies;
- minimum metadata requirements were satisfied;
- duplicate and conflict review was performed;
- source remains within Registry scope;
- restricted publication requirements are honored.

---

## Identifier Validation

Identifier validation should confirm:

- Registry Identifier matches the approved pattern;
- Registry Identifier is unique;
- identifier has not been reused;
- assignment record exists;
- identifier namespace is valid;
- Registry Identifier and Source-System Identifier remain distinct;
- aliases are not represented as canonical identifiers;
- resolution target exists or is intentionally historical;
- supersession and replacement relationships are preserved.

---

## Schema Validation

Schema validation should confirm:

- required fields are present;
- field names match the approved schema;
- data types are correct;
- formats are valid;
- cardinality requirements are satisfied;
- controlled values are approved;
- required objects and arrays are correctly structured;
- deprecated fields are absent or handled through migration rules;
- schema version is declared;
- machine-readable representation parses successfully.

---

## Record-Type Profile Validation

Record-Type Profile validation should confirm:

- one approved primary Record Type is assigned;
- correct Profile Version is declared;
- profile-specific required fields are present;
- profile-specific controlled values are valid;
- required relationships are represented;
- record-type publication requirements are satisfied;
- the SREG is not forced into an inaccurate classification.

---

## Provenance Validation

Provenance validation should confirm:

- Source Institution is attributable;
- Source Record is traceable;
- Source-System Identifier is preserved when available;
- canonical source reference is present;
- source and Registry versions remain separate;
- derived artifacts identify their source;
- archival references are labeled accurately;
- historical provenance remains discoverable;
- corrections preserve prior provenance values.

---

## Relationship Validation

Relationship validation should confirm:

- source identifier exists or is a valid external reference;
- target identifier exists or is a valid external reference;
- identifier domains are declared;
- relationship type is approved;
- direction is valid;
- relationship authority is identified;
- version context is coherent;
- temporal context is coherent;
- inverse relationships are correct when published;
- duplicate relationships are prevented;
- relationship status is valid;
- supporting references exist when required.

---

## Version Validation

Version validation should confirm:

- Registry Entry Version is declared;
- Source-Record Version is preserved when available;
- schema and profile versions are declared;
- version changes follow approved increment rules;
- prior versions remain discoverable;
- current and historical versions are not confused;
- supersession does not overwrite prior identity;
- human-readable and machine-readable version fields agree.

---

## Status and Lifecycle Validation

Validation should confirm:

- Registry Status uses an approved controlled value;
- Registry Lifecycle State uses an approved controlled value;
- Source-Record Status remains separate;
- Certification Status remains Certifier-owned;
- Attestation Status remains Attestor-owned;
- status and lifecycle dates are coherent;
- transitions follow approved rules;
- superseded, revoked, retired, and archived states preserve history;
- public notices match the current Registry condition.

---

## Correction Validation

Correction validation should confirm:

- prior value is preserved;
- corrected value is identified;
- correction reason is documented;
- correction date is preserved;
- correction authority is identified;
- affected Registry Entry Version is identified;
- supporting evidence exists;
- public correction notice is published when required;
- human-readable and machine-readable corrections agree;
- correction does not erase historical traceability.

---

## Publication Validation

Publication validation should confirm:

- canonical title is correct;
- Registry Identifier is visible;
- canonical URL is declared;
- human-readable SREG is complete;
- machine-readable SREG is complete;
- downloadable artifacts are available when required;
- Source Record link is present;
- Source Institution link or reference is present;
- Registry Status is accurate;
- Registry Lifecycle State is accurate;
- version information is visible;
- relationships are represented consistently;
- provenance is represented consistently;
- metadata and page content agree;
- redirects and historical references are preserved.

---

## Cross-Format Consistency

Registry should compare official human-readable and machine-readable forms field by field.

Consistency review should include:

- Registry Identifier;
- title;
- Record Type;
- Source Institution;
- Source-System Identifier;
- canonical source reference;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Source-Record Version;
- relationships;
- provenance;
- correction references;
- publication dates.

```text
A SREG is not fully validated when its official formats disagree.
```

---

## Validation Methods

### Automated Validation

May apply:

- schema checks;
- controlled-value checks;
- identifier pattern checks;
- required-field checks;
- format checks;
- cardinality checks;
- machine-readable parsing;
- cross-file consistency checks.

### Institutional Review

Confirms:

- authority boundaries;
- meaning;
- classification;
- exceptions;
- provenance;
- relationships;
- publication readiness.

### Cross-Artifact Review

Compares:

- HTML;
- JSON;
- downloadable records;
- packages;
- manifests;
- source references;
- integrity artifacts.

### Historical Review

Confirms:

- corrections;
- supersession;
- archived versions;
- prior states;
- historical references;
- redirects.

---

## Validation Workflow

```text
Prepare SREG
  ↓
Run Structural Checks
  ↓
Review Authority and Provenance
  ↓
Validate Relationships and Versions
  ↓
Validate Status and Lifecycle
  ↓
Compare Publication Formats
  ↓
Record Validation Result
  ↓
Publish or Return for Correction
```

---

## Validation Record

Every material validation should preserve:

- Registry Identifier;
- Registry Entry Version;
- validation date;
- validation authority or workflow;
- requirements and versions applied;
- checks performed;
- findings;
- warnings;
- exceptions;
- result;
- required corrections;
- revalidation date, when applicable;
- supporting report or artifact reference.

---

## Validation Outcomes

### Valid

All required checks pass.

### Valid with Warnings

Required checks pass, but non-blocking concerns remain documented.

### Conditionally Valid

Publication may proceed only under explicit approved conditions.

### Invalid

One or more blocking requirements fail.

### Indeterminate

Available evidence or system capability is insufficient to determine validity.

### Not Evaluated

Validation has not yet been completed.

These outcomes describe Registry-object conformance.

They do not certify the substantive truth of the Source Record.

---

## Finding Classes

### Blocking Error

Prevents publication or continued presentation as a valid operational SREG.

### Warning

Identifies a non-blocking concern that remains visible and reviewable.

### Exception

Documents an approved departure from a requirement under defined governance.

### Informational Finding

Records context that does not affect the validation outcome.

---

## Invalid Conditions

Invalid conditions may include:

- missing required field;
- invalid controlled value;
- duplicate Registry Identifier;
- reused Registry Identifier;
- unsupported Source Authority;
- missing Registrability outcome;
- incorrect Record Type;
- broken canonical source reference;
- missing provenance;
- contradictory provenance;
- invalid relationship direction;
- invalid relationship type;
- collapsed version domains;
- incoherent Registry Status;
- incoherent Registry Lifecycle State;
- silent correction;
- human-readable and machine-readable mismatch;
- publication before required validation is complete.

---

## Revalidation

Revalidation may be required after:

- Registry Entry update;
- Source Record version change;
- schema change;
- Record-Type Profile change;
- identifier correction;
- relationship change;
- provenance correction;
- status transition;
- lifecycle transition;
- publication-path change;
- governance exception;
- material rule update;
- material policy update;
- discovery of a validation defect.

Revalidation should identify:

- changed domains;
- affected versions;
- prior validation result;
- required review scope;
- whether full or targeted validation is necessary.

---

## Validation of Existing Publications

If a published SREG later fails validation, Registry may:

- publish a correction notice;
- return the SREG to review;
- restrict publication;
- mark validation as failed;
- mark validation as indeterminate;
- supersede the affected version;
- revoke the SREG when required;
- archive the SREG when required;
- preserve the prior public state for history;
- publish a corrected Registry Entry Version.

```text
Validation failure should change the Registry condition transparently.
It should not erase the historical record.
```

---

## Relationship to Registrability

Registrability occurs before construction.

It answers:

```text
Should Registry create this SREG?
```

Validation occurs after construction.

It answers:

```text
Does this SREG conform to Registry requirements?
```

---

## Relationship to Certification

Registry Validation and Certifier Certification are separate institutional acts.

```text
Registry Validation
  ≠
Certifier Certification
```

Registry validates the SREG as a Registry object.

Certifier evaluates a certification subject and produces Certification Packages, Certification Outcomes, SCPR, SCR, and SCRD artifacts.

A valid SREG is not automatically a certified subject.

---

## Relationship to Attestation

Validation does not create an attestation.

Attestor may issue a separate trust statement concerning:

- a Source Record;
- a SREG;
- a process;
- a validation result;
- an integrity reference.

Registry may catalog the Attestation Record through a separate SREG.

---

## Relationship to Source Authority

Validation confirms that Registry represented the Source Institution and Authoritative Source Record consistently with the Source Authority determination.

Validation does not create Source Authority.

---

## Relationship to Identifiers

Validation confirms that:

- Registry Identifier is valid;
- Source-System Identifier is preserved;
- identifier domains remain distinct;
- aliases are not canonicalized improperly;
- historical identifiers remain traceable;
- resolution behavior is coherent.

---

## Relationship to Provenance

Validation confirms Registry can reconstruct the path from the SREG back to:

- Source Record;
- Source Institution;
- source version;
- publication context;
- custody history;
- derived artifacts;
- corrections;
- prior Registry Entry Versions.

---

## Relationship to Relationships

Validation confirms that relationships are:

- typed;
- directional;
- attributable;
- version-aware;
- time-aware;
- supported;
- non-duplicative;
- consistent across publication formats.

---

## Relationship to Publication

A production SREG should not be presented as valid until required validation is complete.

Publication should preserve:

- validation outcome;
- validation date;
- validated Registry Entry Version;
- requirements applied;
- warnings;
- conditions;
- exceptions;
- revalidation history;
- validation report reference, when public.

---

## Relationship to Corrections

Validation should be repeated after a material correction.

The correction and revalidation record should preserve:

- prior validation result;
- correction reference;
- changed fields;
- affected version;
- new validation result;
- revalidation date;
- responsible authority.

---

## Relationship to Governance

Registry governance should control:

- validation requirements;
- validation outcomes;
- finding classifications;
- blocking and non-blocking criteria;
- exception approval;
- revalidation triggers;
- automated-validation rules;
- institutional-review requirements;
- validation record structure;
- publication thresholds;
- migration rules.

---

## Current Directory Structure

```text
registry/
└── validation/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Validation page.

### `README.md`

The directory-level documentation explaining validation scope, domains, methods, outcomes, findings, records, revalidation, and maintenance.

Future supporting materials may include:

```text
validation/
├── index.html
├── README.md
├── validation-checklist.md
├── validation-schema.md
├── validation-outcomes.md
├── exceptions.md
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
- Registry Provenance;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
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

When Validation architecture changes:

- update `index.html`;
- update this README;
- update validation domains;
- update validation inputs;
- update validation checklists;
- update validation outcomes;
- update finding classifications;
- update revalidation triggers;
- update publication thresholds;
- update automated-validation rules;
- update institutional-review requirements;
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

- Validation applies to the SREG as a Registry object.
- Validation follows SREG construction.
- Validation precedes official publication.
- Validation and Certification remain distinct.
- Validation and Attestation remain distinct.
- Governing requirement versions must be recorded.
- Structural and institutional review are both required.
- Identifier domains must remain separate.
- Provenance must remain traceable.
- Relationships must be typed and valid.
- Version domains must remain distinct.
- Corrections must preserve prior values.
- Revalidation follows material change.
- Human-readable and machine-readable forms must agree.
- Validation failure must not erase history.

---

## Disclaimer

Registry Validation does not by itself establish:

- certification;
- attestation;
- source truth;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- endorsement;
- affiliation;
- permanent availability;
- substantive accuracy of every source claim.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, policy, or external system.

---

## Guiding Statement

> Validation protects the integrity of the Registry object.
>
> It confirms conformance without claiming authority over the source.
