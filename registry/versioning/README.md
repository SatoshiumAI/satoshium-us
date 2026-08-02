# Satoshium Registry Versioning

## Overview

The `registry/versioning/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Versioning framework.

The public page is published through:

```text
registry/versioning/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how Satoshium Registry:

- identifies distinct version domains;
- assigns Registry Entry Versions;
- preserves Source-Record Versions;
- separates Registry identity from Registry version;
- records schema and profile versions;
- records rules, policies, procedures, standards, and methodology versions;
- determines version increments;
- preserves current and historical versions;
- manages migration, correction, rollback, and supersession;
- validates version lineage;
- publishes accountable version history.

Versioning allows Registry to show what changed, when it changed, which requirements applied, and which prior states remain discoverable.

---

## Constitutional Position

Versioning operates across the complete Registry lifecycle.

```text
Source Record
  ↓
SREG Construction
  ↓
Registry Entry Version
  ↓
Validation
  ↓
Publication
  ↓
Version History
```

Registry Identifier preserves continuing identity.

Versioning preserves the changing states of that identity.

---

## Core Principle

```text
Identity remains stable.
Versions record change.
History preserves accountability.
```

A SREG should retain one permanent Registry Identifier while each material Registry state receives an accountable Registry Entry Version.

---

## Canonical Version Distinction

```text
Registry Identifier
  ≠
Registry Entry Version
  ≠
Source-Record Version
```

The Registry Identifier identifies the continuing SREG.

The Registry Entry Version identifies one published state of the SREG.

The Source-Record Version identifies one state of the Authoritative Source Record.

These values belong to separate authority domains.

---

## Why Versioning Matters

A SREG may change because:

- the Source Record changes;
- Registry metadata changes;
- relationships are added or corrected;
- provenance is expanded;
- Registry Status changes;
- Registry Lifecycle State changes;
- schemas evolve;
- Record-Type Profiles evolve;
- controlled values change;
- publication requirements mature;
- corrections are issued;
- archival references are added.

Versioning makes these changes attributable and historically discoverable.

---

## Version Domains

### Registry Entry Version

The version of the SREG controlled by Registry.

### Source-Record Version

The version assigned by the Source Institution to the Authoritative Source Record.

### SREG Base Schema Version

The version of the shared structural requirements applied to all SREGs.

### Record-Type Profile Version

The version of the Record-Type-specific requirements applied to the SREG.

### Registry Schema Specification Version

The version of the broader Registry schema architecture.

### Registry Rules Version

The version of the governing Registry Rules.

### Registry Policy Version

The version of an applicable Registry policy.

### Registry Procedure Version

The version of an operational Registry procedure.

### Controlled-Value Set Version

The version of approved enumerations and controlled terms.

### Validation Workflow Version

The version of the checklist, process, or automated method used for validation.

### Suite Standards Version

The version of applicable Suite Standards.

### Suite Methodology Version

The version of applicable Suite Methodology.

### Suite Interoperability Version

The version of applicable Suite Interoperability requirements.

---

## Version-Domain Independence

A change in one version domain does not automatically require a change in every other domain.

Examples:

- a Source-Record Version may change without a schema change;
- a schema may change without a Source-Record Version change;
- a Registry correction may create a new Registry Entry Version while the Source Record remains unchanged;
- a policy version may change without requiring immediate migration of every SREG;
- a controlled-value set may add a value without altering existing records.

Each version domain must be preserved independently.

---

## Registry Entry Version

Every published SREG should declare a Registry Entry Version.

Illustrative example:

```text
Registry Identifier: SREG-JUR-2026-0001
Registry Entry Version: 1.2.0
```

The Registry Entry Version should change whenever the official Registry object changes materially.

---

## Source-Record Version

Registry should preserve the Source-Record Version exactly as assigned by the Source Institution whenever available.

Registry should not:

- replace the Source-Record Version with the Registry Entry Version;
- invent a Source-Record Version that was never assigned;
- normalize source-version syntax without preserving the original value;
- assume the Source Record changed merely because Registry changed;
- assume Registry must change merely because a source version label changed;
- take control of another institution's version domain.

---

## Illustrative Version Relationship

```text
Registry Identifier: SREG-CERT-2026-0001
Registry Entry Version: 1.1.0
Source-System Identifier: SC-CERT-2026-0001
Source-Record Version: 1.0.0
SREG Base Schema Version: 1.0.0
Certification Profile Version: 1.0.0
```

Each value identifies a different Registry, source, schema, or profile context.

---

## Version Increment Model

Registry may use semantic versioning for Registry Entry Versions:

```text
MAJOR.MINOR.PATCH
```

### Major Version

May be used when a change materially alters:

- structure;
- identity interpretation;
- institutional meaning;
- compatibility;
- migration requirements.

### Minor Version

May be used when a change adds or materially updates Registry information without replacing the continuing SREG identity.

### Patch Version

May be used for limited corrections or clarifications that do not materially change institutional meaning.

### No Version Change

May apply to deployment or presentation changes that do not alter the official SREG content.

Final increment rules remain subject to Registry governance.

---

## Potential Major-Version Triggers

Potential triggers include:

- incompatible SREG structure;
- material change to identity interpretation;
- migration to a new identifier architecture;
- material Record-Type reclassification requiring reconstruction;
- governance-directed reset of version lineage;
- replacement of the canonical source object while preserving controlled continuity;
- substantial publication architecture change affecting machine compatibility.

---

## Potential Minor-Version Triggers

Potential triggers include:

- new relationship;
- new provenance information;
- source-version update reflected in Registry;
- Registry Status change;
- Registry Lifecycle transition;
- material metadata addition;
- new archival reference;
- new integrity reference;
- backward-compatible profile migration;
- material publication notice.

---

## Potential Patch-Version Triggers

Potential triggers include:

- typographical correction;
- formatting correction;
- broken-link repair that does not alter source identity;
- clarifying note;
- non-material metadata correction;
- accessibility improvement that does not alter record meaning;
- machine-readable formatting correction without a canonical field-value change.

---

## Version Assignment Authority

Registry assigns Registry Entry Versions.

Source Institutions assign Source-Record Versions within their own systems.

Applicable governance authorities assign versions to:

- schemas;
- Record-Type Profiles;
- Rules;
- Policies;
- Procedures;
- controlled-value sets;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability requirements.

---

## Version Assignment Record

Every material Registry Entry Version should preserve:

- Registry Identifier;
- new Registry Entry Version;
- prior Registry Entry Version;
- version date;
- version authority or workflow;
- change classification;
- change summary;
- changed fields;
- reason for change;
- Source-Record Version, when applicable;
- schema version;
- Record-Type Profile Version;
- applicable governance versions;
- validation result;
- publication record;
- correction or supersession reference.

---

## Version History

Version history should preserve:

- every published Registry Entry Version;
- release date;
- change summary;
- validation result;
- applicable schema version;
- applicable Record-Type Profile Version;
- Source-Record Version;
- Registry Status at publication;
- Registry Lifecycle State at publication;
- correction references;
- supersession relationships;
- archival access;
- canonical publication path;
- downloadable historical artifacts.

---

## Current and Historical Versions

One Registry Entry Version should be designated as the current published version.

Prior versions should remain:

- identifiable;
- resolvable;
- dated;
- linked to the current version;
- clearly marked as historical;
- available with applicable notices;
- available with applicable restrictions.

```text
Current publication identifies the latest valid state.
Historical publication preserves how that state was reached.
```

---

## Version Relationships

Version lineage may use typed relationships such as:

- version of;
- previous version;
- next version;
- derived from;
- corrects;
- corrected by;
- supersedes;
- superseded by;
- migrated from;
- migrated to;
- compatible with;
- incompatible with.

Final labels and controlled values remain subject to Registry governance.

---

## Version and Correction Distinction

Every material correction may create a new Registry Entry Version.

Not every new Registry Entry Version represents a correction.

```text
Correction
  ↓
New Version

New Version
  ≠
Correction
```

A new version may result from ordinary update, migration, lifecycle transition, added provenance, or relationship change.

---

## Version and Supersession Distinction

A new Registry Entry Version updates the continuing SREG.

Supersession may replace one SREG with another SREG and another Registry Identifier.

```text
Versioning preserves states within one identity.
Supersession connects separate identities.
```

---

## Schema and Profile Migration

When schemas or Record-Type Profiles change, Registry should determine whether existing SREGs require:

- no change;
- validation against the new version;
- targeted migration;
- new Registry Entry Version;
- major Registry Entry Version;
- deprecation notice;
- continued publication under the prior schema;
- compatibility bridge;
- governance exception.

---

## Migration Conditions

### Backward Compatible

Existing records remain valid without structural reconstruction.

### Migration Required

Existing SREGs must be updated to satisfy the new schema or profile.

### Deprecated

The prior structure remains historically supported but should not be used for new SREGs.

### Unsupported

The prior structure is no longer accepted for current operational publication.

---

## Controlled-Value Versioning

Registry should version controlled-value sets for:

- Registry Record Types;
- Registry Status values;
- Registry Lifecycle States;
- relationship types;
- relationship statuses;
- validation outcomes;
- publication-readiness outcomes;
- authority-review outcomes;
- Registrability outcomes;
- correction categories;
- notice types.

A removed, renamed, or deprecated controlled value should remain interpretable in historical SREGs.

---

## Version Validation

Validation should confirm:

- Registry Entry Version is declared;
- version syntax is valid;
- prior version exists when required;
- increment classification matches the change;
- Source-Record Version remains separate;
- schema version is declared;
- Record-Type Profile Version is declared;
- applicable governance versions are identifiable;
- current and historical versions are not confused;
- supersession does not overwrite version lineage;
- human-readable and machine-readable version fields agree;
- version history is complete;
- historical artifacts remain attributable.

---

## Invalid Version Conditions

Invalid conditions include:

- missing Registry Entry Version;
- invalid version syntax;
- version rollback without governance approval;
- duplicate version number for different published states;
- Registry Entry Version used as Source-Record Version;
- Source-Record Version overwritten;
- undeclared schema version;
- undeclared Record-Type Profile Version;
- major change represented as a patch;
- silent version replacement;
- historical version presented as current;
- prior version made undiscoverable;
- human-readable and machine-readable mismatch.

---

## Version Rollback

Registry should not silently restore an earlier version as though later versions never existed.

A rollback should preserve:

- version being withdrawn;
- version being restored or recreated;
- rollback date;
- rollback authority;
- reason;
- validation result;
- publication record;
- access to intervening versions;
- new Registry Entry Version, when required.

Rollback is a new accountable event, not historical erasure.

---

## Relationship to Identifiers

Registry Identifier remains stable through all Registry Entry Versions.

```text
Registry Identifier
  ↓
Version 1.0.0
  ↓
Version 1.1.0
  ↓
Version 2.0.0
```

The identifier represents the continuing Registry object.

The versions represent its changing states.

---

## Relationship to Publication

Every material publication should identify the Registry Entry Version being released.

Publication should expose:

- current version;
- prior versions;
- release dates;
- change summaries;
- validation outcomes;
- schema versions;
- Record-Type Profile Versions;
- Source-Record Version;
- correction references;
- supersession references.

---

## Relationship to Provenance

Version history is part of Registry Provenance.

Provenance should preserve how each version was:

- created;
- validated;
- published;
- corrected;
- superseded;
- revoked;
- archived;
- migrated.

---

## Relationship to Validation

Every material Registry Entry Version should undergo appropriate validation.

Validation should identify:

- version being validated;
- prior version;
- changed domains;
- requirements applied;
- validation outcome;
- warnings;
- exceptions;
- blocking defects.

---

## Relationship to Lifecycle

Version changes and lifecycle transitions are related but distinct.

Examples:

- an update may create a new version while the SREG remains Active;
- supersession may create a final version and identify a successor SREG;
- revocation may create a new version carrying the revocation notice;
- archival transition may create a final archival publication version.

---

## Relationship to Corrections

A material correction may create a new Registry Entry Version.

The correction record should preserve:

- prior version;
- corrected version;
- changed fields;
- reason;
- correction authority;
- correction date;
- validation result;
- publication record.

---

## Relationship to Governance

Registry governance should control:

- version syntax;
- increment rules;
- rollback requirements;
- migration requirements;
- deprecation rules;
- compatibility rules;
- version-history requirements;
- current-version designation;
- historical-version publication;
- controlled-value versioning;
- exception handling.

---

## Relationship to Source Institutions

### Atlas

Atlas controls versions of:

- Atlas resources;
- jurisdiction records;
- Atlas packages;
- generation manifests;
- source artifacts.

### Certifier

Certifier controls versions of:

- Certification Packages;
- SCPR;
- SCR;
- SCRD;
- certification frameworks;
- certification profiles;
- certification procedures.

### Chronicle

Chronicle controls versions of Chronicle-created event records and chronology artifacts.

### Anchor

Anchor controls versions of Anchor-created integrity records and reference structures.

### Beacon

Beacon controls versions of Beacon-created signals and discovery records.

### Attestor

Attestor controls versions of attestations, trust statements, and Attestor-owned schemas.

### Navigator

Navigator controls versions of workflow definitions and coordination records.

### Registry

Registry controls:

- Registry Entry Versions;
- SREG Base Schema Versions;
- Record-Type Profile Versions;
- Registry Schema Specification Versions;
- Registry Rules Versions;
- Registry Policy Versions;
- Registry Procedure Versions;
- Registry-controlled value-set versions.

---

## Current Directory Structure

```text
registry/
└── versioning/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Versioning page.

### `README.md`

The directory-level documentation explaining version domains, increment rules, history, migration, rollback, validation, publication, and maintenance.

Future supporting materials may include:

```text
versioning/
├── index.html
├── README.md
├── versioning-policy.md
├── increment-rules.md
├── migration-rules.md
├── compatibility.md
├── rollback.md
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
- Registry Validation;
- Registry Publication;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
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

When Versioning architecture changes:

- update `index.html`;
- update this README;
- update version domains;
- update increment rules;
- update assignment-record requirements;
- update version-history requirements;
- update migration rules;
- update compatibility rules;
- update deprecation rules;
- update rollback procedures;
- update controlled-value versioning;
- update Validation requirements;
- update Publication requirements;
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

- Registry Identifier and Registry Entry Version remain separate.
- Registry Entry Version and Source-Record Version remain separate.
- Registry controls Registry versioning.
- Source Institutions control source versioning.
- Each version domain must be explicit.
- Version increments should reflect the scale of change.
- Current and historical versions must remain distinguishable.
- Prior versions must remain discoverable.
- Corrections must preserve prior states.
- Rollback must not erase intervening history.
- Versioning and supersession remain distinct.
- Schema and profile migrations require documented review.
- Controlled values require version history.
- Human-readable and machine-readable forms must agree.
- Version history is part of Registry Provenance.

---

## Disclaimer

Registry Versioning does not by itself establish:

- Source Authority;
- certification;
- attestation;
- verification;
- substantive improvement;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- endorsement;
- affiliation;
- backward compatibility;
- permanent availability.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, policy, or external system.

---

## Guiding Statement

> Identity remains stable.
>
> Versions record change.
>
> History preserves accountability.
