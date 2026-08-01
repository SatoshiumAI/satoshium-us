# Satoshium Registry Schemas

## Overview

The `registry/schemas/` directory contains the public Registry Schemas page and supporting documentation that define the structural architecture used by Satoshium Registry Entries, or SREGs.

The public page is published through:

```text
registry/schemas/index.html
```

This `README.md` serves as the directory-level documentation for that page.

Registry Schemas define:

- common SREG fields;
- controlled values;
- identifier structures;
- status and lifecycle domains;
- version fields;
- references;
- typed relationships;
- validation requirements;
- human-readable and machine-readable publication consistency.

---

## Purpose of This Directory

The purpose of this directory is to explain:

- what Registry Schemas are;
- how they fit within the Satoshium Suite hierarchy;
- how the SREG Base Schema supports all Registry Entries;
- how Record-Type Profiles add type-specific requirements;
- how Registry schemas remain separate from Source Institution schemas;
- how identifiers, statuses, lifecycles, and versions remain independently traceable;
- how validation and schema migration are governed;
- how schemas support interoperability and long-term preservation.

---

## Constitutional Position

Registry Schemas operate within the following hierarchy:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Record-Type Profile
  ↓
Published SREG
```

### Suite Schema Standard

Defines Suite-wide structural expectations for:

- identifiers;
- versions;
- dates;
- references;
- relationships;
- authority attribution;
- machine-readable publication;
- compatibility.

### Registry Schema Specification

Defines Registry-wide structural requirements, controlled values, schema governance, validation behavior, and publication consistency.

### SREG Base Schema

Defines the fields and behaviors shared by every operational SREG.

### Record-Type Profile

Adds controlled requirements for one approved Registry Record Type.

### Published SREG

The resulting human-readable and machine-readable Registry Entry.

---

## Core Schema Principle

Registry uses one shared SREG architecture.

Record Types do not create unrelated record models.

They extend the SREG Base Schema through controlled Record-Type Profiles.

```text
Shared SREG structure
  +
Type-specific profile
  =
Validated Registry Entry
```

---

## Registry Schema Specification

The Registry Schema Specification should define:

- schema identifiers;
- schema versions;
- required fields;
- optional fields;
- field types;
- controlled values;
- identifier formats;
- status domains;
- lifecycle domains;
- version fields;
- date formats;
- relationship structures;
- reference requirements;
- validation rules;
- compatibility behavior;
- publication requirements;
- migration requirements.

The specification governs Registry-owned SREG structure.

It does not govern the internal structure of Source Institution records.

---

## SREG Base Schema

The SREG Base Schema should define the common fields used across all Registry Entries.

These may include:

```text
Registry Identifier
Title
Registry Record Type
Source Institution
Authoritative Source Record
Source-System Identifier
Registry Status
Registry Lifecycle State
Source-Record Status
Registry Entry Version
Source-Record Version
SREG Schema Version
Record-Type Profile Version
Public References
Typed Relationships
Registration Date
Last Updated Date
Correction References
Update References
Supersession References
Revocation References
Archival References
```

The Base Schema defines common Registry structure.

It should not contain unnecessary type-specific fields.

---

## Record-Type Profiles

Each approved Registry Record Type should have a corresponding Record-Type Profile.

The current initial profiles are:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

A Record-Type Profile may define:

- required type-specific fields;
- optional type-specific fields;
- controlled classifications;
- required relationships;
- permitted relationships;
- identifier expectations;
- status requirements;
- lifecycle requirements;
- source-reference requirements;
- public-reference requirements;
- validation constraints;
- publication rules.

---

# Tool Record-Type Profile

The Tool profile may add fields for:

- Tool Class;
- tool name;
- institutional purpose;
- operational function;
- owner or maintainer;
- implementation status;
- repository reference;
- documentation reference;
- dependencies;
- integrations;
- interoperability references.

---

# Jurisdiction Record-Type Profile

The Jurisdiction profile may add fields for:

- Jurisdiction Class;
- canonical jurisdiction name;
- alternate names;
- parent jurisdiction;
- country or region;
- jurisdiction codes;
- hierarchy relationships;
- predecessor and successor jurisdictions;
- historical relationships.

---

# Media Record-Type Profile

The Media profile may add fields for:

- Media Class;
- format;
- subject;
- associated resource;
- publisher or platform;
- publication date;
- language;
- visibility;
- access designation;
- rights or licensing reference;
- integrity references.

---

# Certification Record-Type Profile

The Certification profile may add fields for:

- Certification Identifier;
- certified subject;
- certification class;
- Certification Outcome;
- Certification Status;
- certification date;
- standards reference;
- methodology reference;
- scope;
- evidence references;
- Certification Package reference;
- SCPR reference;
- SCR reference;
- SCRD reference.

---

# Attestation Record-Type Profile

The Attestation profile may add fields for:

- attestation identifier;
- attestation classification;
- attested subject;
- attestation statement;
- attestation date;
- evidence references;
- Attestor-controlled status;
- validation or trust relationships.

---

# Signal Record-Type Profile

The Signal profile may add fields for:

- Signal Class;
- signal statement;
- signal date;
- effective date;
- associated subject or event;
- originating channel;
- intended audience;
- chronology;
- discovery and historical relationships.

---

## Authority Separation

Registry Schemas govern Registry-owned SREG structure.

Source Institution schemas govern Source Records.

```text
Source schema
  = defines the Source Record

Registry schema
  = defines how Registry catalogs the Source Record
```

Registry must not:

- overwrite a Source Institution schema;
- redefine source-controlled fields;
- collapse source and Registry identifiers;
- present Registry validation as source certification;
- treat a SREG as a replacement for the Source Record.

---

## Identifier Requirements

Registry Schemas must preserve identifier domains separately.

Examples include:

- Registry Identifier;
- Source-System Identifier;
- Certification Identifier;
- Attestation Identifier;
- Integrity Reference Identifier;
- Workflow Identifier;
- other institution-controlled identifiers.

```text
Registry Identifier
  ≠
Source-System Identifier
```

Identifiers may be related through references or relationships.

They must not be collapsed into one field.

---

## Status Requirements

Registry Schemas must distinguish among status domains.

Examples include:

- Registry Status;
- Source-Record Status;
- Certification Status;
- attestation status;
- tool implementation status;
- media publication status;
- signal publication or withdrawal status.

A value from one status domain must not be used as though it belongs to another without an explicit mapping.

---

## Lifecycle Requirements

Registry Lifecycle State describes the institutional condition of the SREG.

It must remain distinct from:

- source lifecycle;
- certification lifecycle;
- attestation lifecycle;
- tool lifecycle;
- media publication lifecycle;
- signal lifecycle;
- jurisdictional or legal status.

Possible Registry Lifecycle States may include:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states do not form one mandatory linear sequence.

---

## Version Requirements

Registry Schemas should preserve independently traceable versions for:

- Registry Entry Version;
- Source-Record Version;
- SREG Base Schema version;
- Record-Type Profile version;
- Registry Schema Specification version;
- Registry Rules version;
- Registry Policy version;
- Suite Standards version;
- Suite Methodology version.

A change in one version domain does not automatically imply a change in another.

---

## Relationship Structure

Relationships should be represented as typed, attributable, directional structures.

A relationship may include:

```text
Relationship Type
Source Identifier
Target Identifier
Direction
Target Institution
Effective Date
Status
Version Context
Historical Context
Supporting Reference
```

Examples of relationship types may include:

- references;
- produced by;
- produces;
- certifies;
- certified by;
- attests to;
- attested by;
- anchored by;
- discovers;
- documents;
- concerns;
- depends on;
- integrates with;
- part of;
- supersedes;
- superseded by;
- coordinated through.

---

## Reference Requirements

Registry Schemas may require references such as:

- canonical Source Record URL;
- repository path;
- machine-readable source record;
- public institutional page;
- Certification Package;
- SCPR;
- SCR;
- SCRD;
- attestation record;
- Chronicle event;
- Anchor reference;
- Beacon signal;
- Navigator workflow;
- archival location;
- integrity reference.

References should identify whether they are:

- source-controlled;
- Registry-controlled;
- canonical;
- historical;
- archival;
- replacement;
- supporting.

---

## Validation

Schema validation should confirm:

- required fields are present;
- field types are correct;
- controlled values are approved;
- identifiers follow expected formats;
- required relationships exist;
- relationship targets are valid;
- status values belong to the correct domain;
- lifecycle values belong to the correct domain;
- version metadata is complete;
- dates use approved formats;
- source and Registry fields remain distinct;
- required public references exist;
- human-readable and machine-readable forms agree materially.

Registry validation confirms SREG structure.

It does not certify, attest to, or independently verify the Source Record.

---

## Human-Readable Publication

A human-readable SREG may be published through:

- Registry Entry HTML;
- catalog page;
- relationship summary;
- version history;
- correction history;
- supersession notice;
- revocation notice;
- archival page.

The human-readable form should remain understandable without requiring access to the JSON record.

---

## Machine-Readable Publication

A machine-readable SREG may be published through:

- SREG JSON;
- catalog index;
- relationship index;
- version manifest;
- Update Record;
- Correction Record;
- Retirement Record;
- archival record;
- API response.

The machine-readable form should preserve equivalent institutional meaning.

---

## Publication Consistency

Official forms of the same SREG must agree on:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- Registry Status;
- Registry Lifecycle State;
- Source-Record Status;
- versions;
- public references;
- relationships;
- dates.

A SREG is not fully reconciled when official forms materially disagree.

---

## Schema Versioning

Every published schema should include:

- schema name;
- schema identifier;
- schema version;
- status;
- effective date;
- prior version;
- superseded version, when applicable;
- compatibility notes;
- migration guidance;
- validation references;
- changelog reference.

Prior schema versions should remain preserved and discoverable.

---

## Schema Migration

Schema migration should preserve:

- prior schema version;
- new schema version;
- migration date;
- changed fields;
- transformation rules;
- validation result;
- prior SREG version;
- replacement SREG version;
- compatibility notes;
- breaking-change notes.

```text
Schema migration
  ≠
Source Record change
```

A schema migration changes Registry structure.

It does not necessarily mean the Source Record changed.

---

## Relationship to Rules, Policies, and Procedures

Schemas, Rules, Policies, and Procedures serve different functions.

```text
Rules
  = foundational requirements

Policies
  = domain-specific obligations

Procedures
  = repeatable operational steps

Schemas
  = structures that must validate
```

A schema must remain consistent with the Rules and Policies it implements.

A procedure should identify the schema and profile used for validation.

---

## Interoperability

Registry Schemas support interoperability by preserving:

- source attribution;
- stable identifiers;
- typed relationships;
- version references;
- status mappings;
- lifecycle separation;
- canonical references;
- machine-readable publication;
- authority boundaries.

Interoperability connects institutional objects.

Schema design must not collapse institutional authority.

---

## Schema Governance

Registry Schemas should be reviewed when:

- Suite Standards change;
- Suite Methodology changes;
- Registry Rules change;
- Registry Policies change;
- new Record Types are introduced;
- identifier architecture changes;
- status or lifecycle frameworks change;
- new relationship types are introduced;
- publication formats change;
- validation failures reveal ambiguity;
- interoperability requirements change.

Material schema changes should be versioned and documented in the Registry Changelog.

---

## Current Directory Structure

The current directory structure is:

```text
registry/
└── schemas/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Schemas page.

### `README.md`

The directory-level documentation explaining the schema hierarchy, SREG Base Schema, Record-Type Profiles, authority separation, validation, versioning, migration, interoperability, and governance.

Future supporting files may include:

```text
schemas/
├── index.html
├── README.md
├── registry-schema-specification.md
├── sreg-base-schema.json
├── profiles/
├── examples/
├── versions/
└── migrations/
```

These files and directories should be introduced only when the corresponding operational materials exist.

---

## Relationship to Other Registry Documentation

The Schemas page should remain consistent with:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Rules;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Lifecycle;
- Registry Status;
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

When Registry Schemas change:

- update the public `index.html`;
- update this README;
- update the Registry Schema Specification;
- update the SREG Base Schema;
- update affected Record-Type Profiles;
- update validation logic;
- update examples;
- review affected Registry Policies;
- review affected Registry Procedures;
- review lifecycle and status documentation;
- preserve prior schema versions;
- identify affected SREGs;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable publication.

---

## Guiding Principles

- Registry Schemas govern SREG structure.
- Source schemas govern Source Records.
- One shared SREG Base Schema supports all Record Types.
- Record-Type Profiles add controlled type-specific requirements.
- Registry and source identifiers remain distinct.
- Registry and source status domains remain distinct.
- Registry and source lifecycle domains remain distinct.
- Versions remain independently traceable.
- Relationships are typed and attributable.
- Validation confirms structure, not source truth.
- Human-readable and machine-readable forms must agree.
- Prior schema versions remain discoverable.
- Schema migration does not automatically imply a Source Record change.

---

## Disclaimer

Registry Schemas define Registry-owned SREG structure.

They do not by themselves create:

- Source Institution authority;
- certification;
- attestation;
- verification;
- ownership;
- legal rights;
- regulatory approval;
- endorsement;
- affiliation;
- truth.

Those remain controlled by the applicable Source Institution, Source Record, rights holder, governing authority, or external system.

---

## Guiding Statement

> Records preserve information.
>
> SREGs preserve Registry context.
>
> Schemas preserve structure.
>
> Authority remains at the source.
