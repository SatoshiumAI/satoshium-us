# Satoshium Registry Publication

## Overview

The `registry/publication/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Publication framework.

The public page is published through:

```text
registry/publication/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how validated Satoshium Registry Entries, or SREGs, are:

- released;
- resolved;
- maintained;
- corrected;
- versioned;
- superseded;
- revoked;
- archived;
- withdrawn;
- preserved through official human-readable and machine-readable Registry forms.

Publication is the point at which a validated SREG becomes publicly discoverable as an official Satoshium Registry object.

---

## Constitutional Position

Publication follows successful Registry Validation.

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

Validation confirms that the SREG is ready.

Publication makes the validated Registry object discoverable.

---

## Core Principle

```text
Validation protects the Registry object.
Publication makes it discoverable.
History keeps it accountable.
```

Publication should preserve stable identity, accurate source attribution, version clarity, current condition, correction history, and long-term discoverability.

---

## Canonical Publication Model

```text
Validated SREG
  ↓
Human-Readable Form
  +
Machine-Readable Form
  +
Canonical Resolution
  ↓
Published Registry Entry
```

Official publication should preserve one consistent Registry object across all supported forms.

---

## Reusable SREG Publication Package

A normal production SREG is published through a reusable four-file package using the Registry Identifier as the directory name.

```text
SREG-YYYY-NNNN/
├── index.html
├── registry-entry.html
├── record.json
└── README.md
```

- `index.html` — Registration Overview;
- `registry-entry.html` — canonical human-readable SREG;
- `record.json` — canonical machine-readable SREG;
- `README.md` — directory-level documentation.

Record-Type Profiles may require additional source artifacts, relationships, references, or supporting materials, but they do not replace the canonical four-file publication package.

---

## Why Publication Matters

A SREG may be structurally complete and validated but still unavailable to users, systems, and Suite institutions until it is formally published.

Publication provides:

- official public recognition of the SREG;
- canonical Registry resolution;
- human-readable discovery;
- machine-readable interoperability;
- downloadable artifacts;
- visible status and lifecycle notices;
- correction and version history;
- archival continuity.

---

## Publication Requirements

A production publication should normally include:

- successful Validation outcome;
- permanent Registry Identifier;
- canonical human-readable URL;
- canonical machine-readable URL;
- declared Registry Entry Version;
- declared Registry Record Type;
- Source Institution attribution;
- Source-System Identifier, when available;
- canonical source reference;
- Registry Status;
- Registry Lifecycle State;
- provenance information;
- relationship information;
- version references;
- correction references;
- publication date;
- validation date;
- consistent official forms;
- complete reusable four-file SREG package;
- discovery through Registered Items.

---

## Publication Classes

### Human-Readable Publication

Presents the SREG through a structured public page designed for people to read, understand, navigate, and verify.

### Machine-Readable Publication

Presents the SREG in a structured form suitable for validation, indexing, interoperability, automation, and reuse.

### Artifact Publication

Provides downloadable records, snapshots, reports, manifests, or other official publication artifacts.

### Historical Publication

Preserves prior versions, corrections, superseded entries, revoked records, archived states, and former publication paths.

---

## Human-Readable SREG

The public SREG page should make the following information clear:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Authoritative Source Record;
- Source-System Identifier;
- canonical source link;
- Registry Status;
- Registry Lifecycle State;
- Source-Record Status, when available;
- Registry Entry Version;
- Source-Record Version, when available;
- provenance summary;
- relationships;
- validation result;
- correction references;
- history references;
- machine-readable download or link.

---

## Machine-Readable SREG

The machine-readable form should:

- conform to the declared SREG Base Schema;
- conform to the applicable Record-Type Profile;
- declare schema and profile versions;
- use approved controlled values;
- preserve identifier domains;
- preserve Source Institution attribution;
- preserve Source-System Identifier;
- preserve provenance;
- preserve relationships;
- preserve Registry Status;
- preserve Registry Lifecycle State;
- preserve version history;
- preserve correction history;
- parse successfully;
- agree with the human-readable form.

---

## Cross-Format Publication Consistency

Official publication forms should agree on canonical fields.

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
- validation outcome;
- publication date;
- correction dates.

```text
Multiple formats may present information differently.
They must not describe different Registry objects.
```

---

## Canonical URLs

Every published SREG should have a stable canonical Registry location that resolves through **Registered Items**.

Production example:

```text
https://satoshium.us/registry/registered-items/SREG-2026-0001/
```

The canonical human-readable SREG and machine-readable SREG are published within the same Registry Identifier directory.

```text
https://satoshium.us/registry/registered-items/SREG-2026-0001/registry-entry.html
https://satoshium.us/registry/registered-items/SREG-2026-0001/record.json
```

Registered Items is the production publication location for completed SREG registrations.

URL architecture may evolve through governed change, but the Registry Identifier must remain stable and prior resolution must remain historically traceable.

---

## Identifier Resolution

A published Registry Identifier should resolve to:

- current canonical SREG;
- current Registry Entry Version;
- current Registry Status;
- current Registry Lifecycle State;
- machine-readable form;
- Authoritative Source Record;
- Source Institution;
- prior versions;
- correction records;
- supersession notices;
- successor references;
- archival references when no longer active.

---

## Operational Publication Sequence

```text
Construct SREG Package
  ↓
Validate
  ↓
Publish
  ↓
Registered Items
  ↓
Maintain
```

Publication is operationally complete when the validated SREG package resolves through its production Registry location and is discoverable through **Registered Items**.

Maintenance after publication is governed through Registry Versioning, Corrections, Status, Lifecycle, History, and the applicable update, supersession, revocation, restriction, and archival procedures.

---

## Publication Readiness

A SREG is publication-ready only when:

- required Validation is complete;
- blocking defects are resolved;
- warnings and conditions are documented;
- canonical fields are complete;
- official forms agree;
- source references are attributable;
- relationships are coherent;
- provenance is coherent;
- status and lifecycle notices are accurate;
- version fields are declared;
- publication artifacts are generated;
- canonical URLs are assigned;
- publication authority is identified.

---

## Publication Readiness Outcomes

### Ready

All required publication conditions are satisfied.

### Ready with Notices

Publication may proceed with visible warnings, limitations, or approved conditions.

### Restricted

Publication is limited by privacy, rights, safety, security, contractual, or institutional requirements.

### Not Ready

One or more blocking validation, consistency, authority, or publication defects remain.

---

## Publication Authority

Registry is authoritative for publishing SREGs and Registry-owned metadata.

Publication authority should be documented through:

- publication workflow;
- responsible Registry role or process;
- publication date;
- validated Registry Entry Version;
- release or deployment reference;
- governing rules and policy versions;
- applicable restrictions;
- applicable notices.

Registry publication does not transfer Source Authority.

---

## Publication Record

Every material publication should preserve:

- Registry Identifier;
- Registry Entry Version;
- publication date and time;
- publication authority;
- canonical human-readable URL;
- canonical machine-readable URL;
- published artifact references;
- validation outcome;
- validation date;
- Registry Status at publication;
- Registry Lifecycle State at publication;
- schema version;
- Record-Type Profile Version;
- release notes or change summary;
- superseded publication reference, when applicable.

---

## Publication Notices

Potential public notices include:

- provisional publication;
- restricted source access;
- source unavailable;
- validation warning;
- correction issued;
- superseded entry;
- revoked entry;
- archived entry;
- historical record;
- disputed relationship;
- external-source disclaimer;
- rights or reuse limitation.

Notices should be clear, visible, attributable, and consistent across official forms.

---

## Restricted Publication

A SREG may require restricted publication when full release would conflict with:

- privacy requirements;
- intellectual-property rights;
- licensing restrictions;
- safety concerns;
- security requirements;
- contractual obligations;
- controlled-access source conditions;
- institutional policy.

Restricted publication may expose public metadata while withholding or limiting access to:

- Source Record;
- selected Registry fields;
- supporting evidence;
- machine-readable artifacts;
- downloadable records.

---

## External Source Publication

Publication of an external-source SREG should clearly distinguish:

- Registry ownership of the SREG;
- external ownership of the Source Record;
- Source Institution attribution;
- external identifier domains;
- rights and reuse limitations;
- absence of endorsement or affiliation unless supported;
- source availability and access conditions;
- date Registry last verified the source reference.

---

## Publication Updates

A material SREG update should create:

- new Registry Entry Version;
- new publication record;
- updated human-readable form;
- updated machine-readable form;
- change summary;
- revalidation result, when required.

Potential triggers include:

- Source Record version change;
- metadata correction;
- relationship change;
- provenance update;
- Registry Status change;
- Registry Lifecycle transition;
- schema migration;
- profile migration;
- canonical source change;
- publication-path change;
- new archival reference;
- new integrity reference.

---

## Publication Corrections

A publication correction should preserve:

- prior published value;
- corrected value;
- correction reason;
- correction date;
- correction authority;
- affected Registry Entry Version;
- new Registry Entry Version;
- public correction notice;
- updated machine-readable form;
- historical access to the prior state.

```text
Publication correction improves the current record.
It must not erase the previously published state.
```

---

## Supersession and Successor Publication

When a SREG is superseded:

- prior Registry Identifier remains resolvable;
- prior page displays a supersession notice;
- successor Registry Identifier is linked;
- supersession date is preserved;
- reason or governing event is documented;
- prior versions remain accessible;
- machine-readable relationships are updated;
- successor does not overwrite prior identity.

---

## Revoked and Archived Publication

Revoked or archived SREGs should remain discoverable unless publication itself must be restricted or removed.

Their pages should preserve:

- Registry Identifier;
- title;
- historical Registry Entry Version;
- revoked or archived condition;
- effective date;
- reason, when public;
- successor reference, when applicable;
- correction references;
- history references;
- archival source information;
- provenance information.

```text
Leaving active use does not erase Registry identity.
```

---

## Publication Withdrawal

Registry may restrict or withdraw public access when required by:

- lawful authority;
- rights violation;
- privacy harm;
- security risk;
- safety risk;
- material deception;
- publication defect;
- governance decision.

Withdrawal should preserve:

- Registry Identifier;
- withdrawal date;
- withdrawal authority;
- reason or reason category;
- affected versions;
- replacement or correction path;
- historical resolution behavior.

---

## Publication History

Publication history should preserve:

- first publication;
- every Registry Entry Version;
- release dates;
- change summaries;
- validation outcomes;
- corrections;
- supersession;
- revocation;
- retirement;
- archival transition;
- URL changes;
- withdrawal events;
- republication events.

---

## Publication Validation

Before release, Registry should confirm:

- Validation outcome permits publication;
- canonical URLs are correct;
- Registry Identifier resolves correctly;
- human-readable and machine-readable forms agree;
- required artifacts are available;
- source links are accurate;
- status and lifecycle notices are correct;
- version fields are visible;
- correction references are present;
- history references are present;
- restricted information is not exposed;
- metadata and canonical tags are correct;
- publication record is complete;
- the SREG is discoverable through Registered Items.

---

## Invalid Publication Conditions

Invalid conditions include:

- publication before required Validation;
- missing Registry Identifier;
- incorrect canonical URL;
- unresolved production identifier;
- missing machine-readable form;
- human-readable and machine-readable mismatch;
- incorrect Source Institution attribution;
- broken canonical source reference;
- incorrect Registry Status;
- incorrect Registry Lifecycle State;
- missing version information;
- missing required notice;
- restricted information exposed publicly;
- silent correction;
- silent replacement;
- prior identity overwritten during supersession.

---

## Relationship to Validation

Validation determines whether a SREG conforms to Registry requirements.

Publication releases the validated SREG through official Registry channels.

```text
Validation confirms readiness.
Publication creates discoverability.
```

---

## Relationship to Registered Items

Registered Items is the concise public listing of completed Registry registrations.

A newly published SREG should be added to Registered Items after production publication and resolution are confirmed.

```text
Validated SREG
  ↓
Published SREG Package
  ↓
Registered Items
  ↓
Ongoing Maintenance
```

Registered Items does not replace the canonical SREG package. It provides direct public discovery of completed registrations.

---

## Relationship to Identifiers

Publication resolves the Registry Identifier through stable public locations.

URL changes may require redirects or publication updates.

They must not change the permanent Registry Identifier.

---

## Relationship to Provenance

Publication should expose enough provenance to trace the SREG back to:

- Authoritative Source Record;
- Source Institution;
- Source-System Identifier;
- source version;
- publication history;
- custody history;
- correction history.

Historical publication records become part of Registry Provenance.

---

## Relationship to Relationships

Publication should expose typed relationships consistently across:

- human-readable SREG;
- machine-readable SREG;
- linked record pages;
- history;
- correction records;
- supersession notices;
- archival presentation.

---

## Relationship to Lifecycle

Publication presentation should reflect the current Registry Lifecycle State.

- Pending entries should not appear as active SREGs.
- Active entries should resolve normally.
- Updated entries should expose current and prior versions.
- Superseded entries should identify successors.
- Revoked entries should display revocation notices.
- Archived entries should remain historically discoverable.

---

## Relationship to Corrections

Publication Corrections should follow Registry correction requirements.

Corrections should be:

- attributable;
- dated;
- version-aware;
- evidence-supported;
- historically preserved;
- reflected in all official forms.

---

## Relationship to Chronicle

Material publication events may be recorded through Chronicle when they have institutional or historical significance.

Examples include:

- first public SREG publication;
- major Registry release;
- material correction;
- supersession;
- revocation;
- archival transition;
- publication-policy change.

Registry remains authoritative for the publication record.

Chronicle remains authoritative for Chronicle-created historical event records.

---

## Relationship to Beacon

Beacon may create signals announcing:

- newly published SREGs;
- materially updated SREGs;
- major Registry milestones;
- corrections;
- supersession;
- archival transitions.

Registry remains authoritative for the SREG.

Beacon remains authoritative for its discovery signal.

---

## Relationship to Governance

Registry governance should control:

- publication requirements;
- readiness outcomes;
- publication authority;
- canonical URL patterns;
- official publication formats;
- restricted-publication rules;
- notice requirements;
- correction publication;
- supersession publication;
- revocation and archival presentation;
- withdrawal procedures;
- publication-history requirements;
- exception handling.

---

## Current Directory Structure

```text
registry/
└── publication/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Publication page.

### `README.md`

The directory-level documentation explaining publication readiness, official forms, canonical resolution, notices, updates, corrections, historical continuity, and maintenance.

Future supporting materials may include:

```text
publication/
├── index.html
├── README.md
├── publication-checklist.md
├── publication-record-schema.md
├── canonical-urls.md
├── notices.md
├── restricted-publication.md
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
- Registry Registered Items;
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

When Publication architecture changes:

- update `index.html`;
- update this README;
- update publication requirements;
- update readiness outcomes;
- update canonical URL rules;
- update reusable SREG package requirements;
- update Registered Items publication and discovery requirements;
- update publication-record fields;
- update notice requirements;
- update restricted-publication rules;
- update correction publication;
- update supersession handling;
- update withdrawal procedures;
- update publication-history requirements;
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

- Publication follows Validation.
- Normal production publication uses the canonical four-file SREG package.
- Completed publications should be discoverable through Registered Items.
- Registry Identifier must resolve consistently.
- Human-readable and machine-readable forms must agree.
- Canonical URLs may change; Registry identity must not.
- Publication authority belongs to Registry for SREGs.
- Source Authority remains with the Source Institution.
- Notices must make material context visible.
- Restricted publication must preserve rights and safety boundaries.
- Corrections must preserve prior states.
- Supersession must not overwrite prior identity.
- Revoked and archived SREGs should remain historically discoverable.
- Withdrawal must preserve an accountable record.
- Publication history is part of Registry Provenance.
- Publication does not create certification, attestation, ownership, or endorsement.

---

## Disclaimer

Registry Publication does not by itself establish:

- Source Authority;
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
- permanent source availability.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, policy, or external system.

---

## Guiding Statement

> Validation protects the Registry object.
>
> Publication makes it discoverable.
>
> History keeps it accountable.
