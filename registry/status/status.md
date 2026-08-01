# Satoshium Registry Status

## Overview

The `registry/status/` directory contains the public Registry Status page and supporting documentation that define:

- the current institutional development condition of Satoshium Registry;
- Registry-controlled status values;
- Registry Lifecycle States;
- source-controlled status domains;
- status ownership;
- status mappings;
- transition requirements;
- validation and publication expectations.

The public page is published through:

```text
registry/status/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to explain:

- what Registry Status means;
- how Registry Status differs from Registry Lifecycle State;
- how both differ from Source-Record Status;
- which institution owns each status domain;
- how source statuses may be referenced without transferring authority;
- how status transitions should be recorded;
- how source-to-Registry mappings should be governed;
- how historical SREGs remain discoverable after source revocation, retirement, withdrawal, or unavailability;
- how status values are validated and published consistently.

---

## Constitutional Position

Registry status architecture operates within the following institutional relationship:

```text
Source Institution
  ↓
Source-Record Status

Registry
  ↓
Registry Status
  ↓
Registry Lifecycle State
```

Each institution owns the status values whose meaning it creates.

Registry may reproduce source-controlled status values inside a SREG.

Registry does not become authoritative for those values merely by cataloging them.

---

## Status Ownership Principle

Status follows authority.

Examples include:

- Certifier owns Certification Status and Certification Outcome;
- Attestor owns attestation status and attestation conclusions;
- Atlas owns status values attached to Atlas Source Records;
- Chronicle owns event status within Chronicle;
- Anchor owns integrity-reference status;
- Beacon owns signal status;
- Navigator owns workflow status;
- Registry owns Registry Status and Registry Lifecycle State.

```text
Reference does not transfer authority.
```

---

## Current Registry Development Condition

**Project:** Satoshium Registry

**Development Condition:** Active Institutional Implementation

**Current Focus:** Formalizing the operational SREG architecture

Registry is establishing:

- institutional rules;
- definitions;
- scope boundaries;
- SREG architecture;
- Registry Record Types;
- Record-Type Profiles;
- schemas;
- lifecycle states;
- Registry Status values;
- policies;
- procedures;
- integration pages;
- public institutional documentation;
- validation requirements;
- publication consistency requirements.

The current development effort is no longer limited to conceptual planning.

The foundational architecture is being converted into a publication-ready operational framework.

---

## Current Institutional Priority

The current priority is to establish one coherent Registry model that preserves:

- stable Registry identity;
- Source Institution authority;
- one primary Record Type per SREG;
- distinct identifier domains;
- distinct status domains;
- distinct lifecycle domains;
- independently traceable versions;
- typed relationships;
- durable references;
- validation;
- correction history;
- long-term discoverability.

---

## Current Capabilities

Registry now has the architecture required to support:

### Source Identification

Identifying the Source Institution and Authoritative Source Record.

### Registrability Review

Determining whether a source object can become an operational SREG.

### Registry Identifier Assignment

Assigning a unique Registry-controlled identifier.

### Record Classification

Assigning one approved primary Registry Record Type.

### Schema Validation

Validating against the SREG Base Schema and applicable Record-Type Profile.

### Relationship Mapping

Creating typed and attributable relationships.

### Status and Lifecycle Management

Recording Registry Status, Registry Lifecycle State, and source-controlled status values separately.

### Version Management

Preserving Registry Entry, Source Record, schema, profile, Standards, and Methodology versions independently.

### Publication

Supporting equivalent human-readable and machine-readable SREG forms.

### Historical Preservation

Maintaining update, correction, supersession, revocation, retirement, and archival history.

---

## Current Limitations

Continuing implementation is still required for:

- operational SREG populations;
- final controlled Registry Status enumerations;
- machine-readable status dictionaries;
- automated validation;
- status-transition records;
- source-to-Registry mapping tables;
- lifecycle automation;
- catalog filtering;
- status-history indexes;
- cross-institution synchronization;
- automated publication reconciliation.

These limitations reflect implementation maturity rather than architectural absence.

---

# Registry Status

Registry Status describes the Registry-controlled operational condition of a SREG.

It answers questions such as:

- Is the SREG eligible for active publication?
- Is it maintained as a historical entry?
- Is access restricted?
- Has Registry suspended or withdrawn recognition?
- Is the SREG preserved in archival status?

Registry Status does not describe:

- certification outcome;
- certification status;
- attestation conclusion;
- source validity;
- governmental authority;
- tool availability;
- media visibility;
- legal recognition;
- truth.

---

## Potential Registry Status Values

Controlled values may include:

### Pending Review

The proposed SREG has not completed Registry review.

### Active

The SREG is actively published and recognized within Registry.

### Active Historical Entry

The SREG remains actively discoverable as a historical record even though the Source Record may be revoked, retired, withdrawn, superseded, unavailable, or no longer operational.

### Restricted

The SREG exists but some publication or access is limited by policy, rights, privacy, safety, or security requirements.

### Suspended

Active Registry recognition or publication has been temporarily suspended pending review or resolution.

### Withdrawn

Registry has withdrawn the SREG from normal active recognition without necessarily deleting its historical record.

### Archived

The SREG is preserved outside active operational use.

These values remain subject to formal controlled-value governance.

---

# Registry Lifecycle State

Registry Lifecycle State describes the institutional condition of the SREG over time.

Potential states include:

```text
Pending Registration
Registered
Active
Updated
Superseded
Revoked
Archived
```

These states do not necessarily form one mandatory linear sequence.

A SREG moves only through the states required by its actual history.

---

## Pending Registration

The source object has been identified for possible registration.

The SREG has not yet completed:

- source-authority review;
- registrability review;
- Record Type assignment;
- identifier assignment;
- schema validation;
- publication review.

---

## Registered

Registry has:

- created the SREG;
- assigned the Registry Identifier;
- preserved the source identity;
- assigned the Record Type;
- completed minimum registration controls.

Registered does not automatically mean active public publication under every future policy.

---

## Active

The SREG is the current Registry representation of the Source Record or is intentionally maintained as an active historical entry.

---

## Updated

Registry has published a revised SREG version because of:

- new source information;
- changed Registry metadata;
- new references;
- changed relationships;
- Source-Record Status changes;
- schema migration;
- Record-Type Profile changes.

Updated may function as a recorded lifecycle event or state according to the final lifecycle specification.

---

## Superseded

A distinct successor SREG or replacement Registry object has taken its place.

The superseded entry should remain discoverable and reference its successor.

---

## Revoked

Registry has withdrawn the SREG from active Registry recognition because of a Registry-controlled defect or documented governance decision.

Possible reasons include:

- invalid registration;
- material source misidentification;
- unsupported Source Record representation;
- serious Registry publication error;
- governance-directed withdrawal.

Registry revocation affects the SREG.

It does not automatically revoke or invalidate the Source Record.

---

## Archived

The SREG is preserved outside active operational use.

Archived records should retain:

- Registry Identifier;
- Source-System Identifier;
- Source Institution;
- Authoritative Source Record;
- versions;
- references;
- relationships;
- updates;
- corrections;
- supersession history;
- revocation history;
- archival date;
- archival reason.

```text
Archived does not mean deleted.
```

---

# Source-Record Status

Source-Record Status describes the condition of the Authoritative Source Record.

It is controlled by the Source Institution.

Examples may include:

- Draft;
- Published;
- Active;
- Certified;
- Revoked;
- Withdrawn;
- Superseded;
- Deprecated;
- Historical;
- Archived;
- Removed;
- Unavailable.

Registry may reproduce the value.

Registry must preserve its attribution and source-controlled meaning.

---

## Source-Specific Status Domains

Different institutions may maintain their own status domains.

### Certifier

- Certification Outcome;
- Certification Status;
- Certification Package status;
- SCRD status.

### Attestor

- attestation status;
- trust-statement status;
- validation status;
- revocation status.

### Atlas

- resource status;
- evidence status;
- publication status;
- package status.

### Chronicle

- event status;
- publication status;
- historical classification.

### Anchor

- integrity-reference status;
- anchor status;
- verification-reference status.

### Beacon

- signal status;
- publication status;
- withdrawal status.

### Navigator

- workflow status;
- workflow execution status;
- coordination status.

### Tool and Media Sources

- implementation status;
- release status;
- service availability;
- publication status;
- visibility;
- access status;
- deprecation status.

These values must remain in their proper domains.

---

## Status Domains Must Remain Distinct

```text
Registry Status
  ≠
Registry Lifecycle State
  ≠
Source-Record Status
  ≠
Certification Status
  ≠
Certification Outcome
  ≠
Attestation Status
  ≠
Tool Implementation Status
  ≠
Media Visibility
```

A value may appear similar across domains.

That does not make the domains interchangeable.

---

## Illustrative Status Combination

A Certification SREG may validly contain:

```text
Certification Outcome: Certified
Certification Status: Revoked
Source-Record Status: Published Historical Record
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

This means:

- Certifier once issued a certified outcome;
- Certifier later revoked the certification;
- the source artifact remains published as a historical record;
- Registry continues to publish the SREG for historical discoverability;
- the SREG itself remains active.

No contradiction exists because each value belongs to a different authority domain.

---

## Status Mapping

Registry may define explicit mappings between source-controlled statuses and Registry behavior.

A mapping should identify:

- source institution;
- source status domain;
- source status value;
- Registry interpretation;
- Registry Status effect, if any;
- Registry Lifecycle effect, if any;
- publication effect;
- review requirement;
- effective date;
- mapping version;
- governing policy.

Example:

```text
Source Status: Revoked
Registry Interpretation: Preserve for historical discovery
Registry Status Effect: Active Historical Entry
Lifecycle Effect: No automatic change
Human Review: Required
```

A mapping does not transfer ownership of the source status to Registry.

---

## Status Transition Requirements

A Registry Status or Registry Lifecycle transition should preserve:

- Registry Identifier;
- affected Registry Entry Version;
- prior status or state;
- new status or state;
- effective date;
- reason;
- authority for the transition;
- operator or process;
- related Source-Record Status change;
- supporting reference;
- governing policy;
- successor reference, when applicable;
- archival reference, when applicable.

Material transitions should remain historically discoverable.

---

## Relationship to Certifier

The canonical certification path is:

```text
Certification Package
  ↓
SCRD
  ↓
Certification SREG
```

Certifier remains authoritative for:

- Certification Identifier;
- Certification Outcome;
- Certification Status;
- Certification Package;
- SCPR;
- SCR;
- SCRD;
- certification versions;
- certification revocation.

Registry remains authoritative for:

- Registry Identifier;
- Certification SREG;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry corrections;
- Registry publication;
- Registry archival history.

---

## Relationship to the Suite

Registry connects Suite institutions without absorbing their authority.

```text
Atlas
  → creates jurisdiction intelligence

Certifier
  → creates certification records

Chronicle
  → creates historical events

Anchor
  → creates integrity references

Beacon
  → creates signals

Attestor
  → creates attestations

Navigator
  → creates workflows

Registry
  → creates SREGs
```

Registry catalogs and relates these institutional objects.

---

## Validation Requirements

Status validation should confirm:

- Registry Status uses an approved Registry-controlled value;
- Registry Lifecycle State uses an approved lifecycle value;
- Source-Record Status remains attributable to the Source Institution;
- source-specific values remain in the correct domains;
- source and Registry statuses are not conflated;
- status mappings are explicit;
- transition history is preserved;
- effective dates are recorded;
- version context is available;
- human-readable and machine-readable forms agree;
- status values do not imply unsupported authority.

---

## Publication Requirements

Human-readable and machine-readable forms of the same SREG should agree on:

- Registry Status;
- Registry Lifecycle State;
- Source-Record Status;
- source-specific status values;
- effective dates;
- version context;
- transition references;
- successor references;
- revocation references;
- archival references.

A SREG is not fully reconciled when official forms materially disagree.

---

## Relationship to Registry Lifecycle

Registry Status and Registry Lifecycle State are related but distinct.

### Registry Status

Describes Registry's current operational recognition or publication condition.

### Registry Lifecycle State

Describes where the SREG stands in its institutional history.

Example:

```text
Registry Status: Active Historical Entry
Registry Lifecycle State: Active
```

Another example:

```text
Registry Status: Archived
Registry Lifecycle State: Archived
```

A final controlled-value model should define which combinations are allowed.

---

## Relationship to Updates and Corrections

### Update

May change Registry Status when new information or source status affects current Registry publication.

### Correction

May repair an incorrectly recorded status value.

A correction should preserve:

- incorrect prior value;
- corrected value;
- correction reason;
- correction date;
- affected version;
- public Correction Record.

A status correction must not rewrite a source-controlled status value without authoritative source support.

---

## Relationship to Supersession and Revocation

### Supersession

A successor SREG replaces the prior Registry representation.

The prior SREG remains historically discoverable.

### Registry Revocation

Registry withdraws the SREG because of a Registry-controlled defect.

### Source Revocation

The Source Institution revokes the Source Record, certification, attestation, signal, or other source object.

These actions must remain distinct.

---

## Current Directory Structure

The current directory structure is:

```text
registry/
└── status/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Status page.

### `README.md`

The directory-level documentation explaining development condition, status ownership, Registry Status, Registry Lifecycle State, source-status domains, mappings, transitions, validation, and maintenance.

Future supporting files may include:

```text
status/
├── index.html
├── README.md
├── registry-status-values.md
├── status-mappings.md
├── transition-rules.md
├── versions/
└── history/
```

These files and directories should be introduced only when the corresponding operational materials exist.

---

## Relationship to Other Registry Documentation

The Status page should remain consistent with:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Rules;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
- Registry Lifecycle;
- Registry Integration;
- Registry Corrections;
- Registry Policies;
- Registry Procedures;
- Registry Changelog;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Registry Status architecture changes:

- update the public `index.html`;
- update this README;
- update controlled Registry Status values;
- update Registry Lifecycle documentation;
- update the SREG Base Schema;
- update affected Record-Type Profiles;
- update status mappings;
- update transition rules;
- update Registry Policies;
- update Registry Procedures;
- update examples;
- review affected SREGs;
- preserve prior status-model versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication.

---

## Future Development

Future capabilities may include:

- machine-readable Registry Status enumerations;
- machine-readable Registry Lifecycle enumerations;
- status-transition records;
- source-to-Registry mapping tables;
- automated validation;
- status-history indexes;
- status-based catalog filters;
- cross-institution synchronization;
- lifecycle automation;
- human-review controls;
- compatibility rules for status-model versions.

Future development must preserve institutional status ownership.

---

## Guiding Principles

- Status follows authority.
- Registry owns Registry Status.
- Registry owns Registry Lifecycle State.
- Source Institutions own source statuses.
- Registry may reproduce source values but may not redefine them.
- Registry Status and Registry Lifecycle State remain distinct.
- Status domains must not be collapsed.
- Status mappings must be explicit.
- Transitions must preserve reason, authority, date, and version context.
- Historical SREGs may remain active after source revocation or retirement.
- Archived does not mean deleted.
- Publication forms must agree.
- Registration does not create source authority.

---

## Disclaimer

Registry Status values describe Registry-owned SREGs and Registry-controlled operations.

They do not by themselves establish:

- source validity;
- certification;
- Certification Outcome;
- attestation;
- verification;
- tool functionality;
- media availability;
- governmental authority;
- ownership;
- legal rights;
- regulatory approval;
- endorsement;
- affiliation;
- truth.

Those remain controlled by the applicable Source Institution, Source Record, governing authority, rights holder, or external system.

---

## Guiding Statement

> Status follows authority.
>
> Lifecycle follows the SREG.
>
> Registry preserves both without confusing them.
