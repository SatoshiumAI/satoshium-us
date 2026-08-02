# Satoshium Registry Registered Items

## Overview

The `registry/registered-items/` directory contains the public directory of completed Satoshium Registry Entries.

The public page is published through:

```text
registry/registered-items/index.html
```

This `README.md` serves as the directory-level documentation for that page and the SREG directories contained beneath it.

---

## Purpose of This Directory

The purpose of `registered-items/` is to provide the public Registry directory for completed registrations.

Each registered item receives a dedicated SREG directory containing:

- a registration overview;
- the canonical human-readable Registry Entry;
- the canonical machine-readable Registry record;
- repository-level documentation.

The initial structure is:

```text
registry/
└── registered-items/
    ├── index.html
    ├── README.md
    └── SREG-2026-0001/
        ├── index.html
        ├── registry-entry.html
        ├── record.json
        └── README.md
```

---

## Architectural Position

Registered Items sits between the Registry institution and each completed SREG package.

```text
Satoshium Registry
  ↓
Registered Items
  ↓
SREG Directory
  ↓
Canonical Registry Entry
```

Registered Items provides the public list.

The SREG directory provides the complete registration package.

The Registry Entry is the actual canonical SREG.

---

## Registered Items and the Registry Catalog

Registered Items and the Registry Catalog serve related but distinct purposes.

### Registered Items

Provides a direct public list of completed SREG registrations.

### Registry Catalog

Provides broader discovery capabilities, including:

- browsing;
- searching;
- filtering;
- Record-Type collections;
- relationship navigation;
- current and historical views;
- machine-readable indexes;
- Catalog Versioning.

```text
Registered Items
= concise list of completed registrations

Registry Catalog
= broader discovery and resolution layer
```

---

## First Registered Item

The first registered item is:

```text
SREG-2026-0001
```

It represents the certification record associated with:

```text
SC-CERT-2026-0001
```

The first item establishes the operational relationship:

```text
SREG-2026-0001
  ↓
Registry Record Type: Certification
  ↓
Certification Package SC-CERT-2026-0001
  ↓
Satoshium Certifier
```

---

## Authority Boundary

Satoshium Registry owns:

- SREG-2026-0001;
- its Registry Identifier;
- its Registry Record Type;
- Registry-owned metadata;
- Registry Relationships;
- Registry Entry Version;
- Registry Status;
- Registry Lifecycle State;
- Registry Publication;
- Registry Corrections;
- Registry History;
- Registry Catalog presentation.

Satoshium Certifier retains authority over:

- the Certification Package;
- the certification outcome;
- certification scope;
- certification status;
- certification validity;
- certification evidence;
- SCPR;
- SCR;
- SCRD HTML;
- SCRD JSON;
- other Certifier-created artifacts.

```text
Registry records certification.
Certifier performs certification.
```

---

## SREG Directory Requirements

Each completed SREG directory should contain:

```text
SREG-YYYY-NNNN/
├── index.html
├── registry-entry.html
├── record.json
└── README.md
```

Additional governed artifacts may be added later when operationally required.

---

## `index.html`

The item-level `index.html` serves as the registration overview.

It should summarize:

- Registry Identifier;
- title;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- registration date;
- Source Institution;
- Source Authority;
- Authoritative Source Record;
- Source-System Identifier;
- Source-Record Version;
- provenance;
- relationships;
- Validation;
- Publication;
- History;
- notices;
- restrictions;
- available SREG artifacts.

The overview should link to:

- `registry-entry.html`;
- `record.json`;
- `README.md`;
- authoritative source materials;
- related Registry framework pages.

---

## `registry-entry.html`

The `registry-entry.html` file is the canonical human-readable Satoshium Registry Entry.

It should contain the complete Registry-owned representation of the SREG.

At minimum, it should identify:

- Registry Identifier;
- Registry Entry Version;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- title;
- description;
- Source Institution;
- Source Authority;
- Authoritative Source Record;
- Source-System Identifier;
- Source-Record Version;
- canonical source URL;
- related source artifacts;
- relationships;
- provenance;
- Validation information;
- Publication information;
- History;
- Corrections;
- notices;
- restrictions;
- canonical human-readable URL;
- canonical machine-readable URL.

---

## `record.json`

The `record.json` file is the canonical machine-readable representation of the SREG.

It should remain materially aligned with `registry-entry.html`.

```text
registry-entry.html
        ↕
record.json
```

The two representations should not contain conflicting Registry facts.

The JSON record should use:

- the SREG Base Schema;
- the applicable Record-Type Profile;
- governed Controlled Values;
- current Registry field names;
- current version identifiers;
- canonical Registry and source references.

---

## `README.md`

The item-level `README.md` documents:

- the purpose of the SREG directory;
- file responsibilities;
- authority boundaries;
- source relationships;
- Registry and Source-System identifiers;
- versioning expectations;
- Validation requirements;
- Publication requirements;
- Correction requirements;
- History requirements;
- maintenance expectations;
- related institutional pages.

---

## Registered Items Index Requirements

The `registered-items/index.html` page should provide, for each listed SREG:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- registration or Publication date;
- link to the item overview;
- link to the canonical Registry Entry;
- link to the machine-readable record.

As additional SREGs are created, they should be added in governed Registry order.

---

## Identifier Pattern

The initial Registry Identifier pattern is:

```text
SREG-YYYY-NNNN
```

Example:

```text
SREG-2026-0001
```

The identifier should remain:

- unique;
- permanent;
- non-reused;
- stable across Registry Entry Versions;
- distinct from the Source-System Identifier.

---

## Source-System Identifier

The first SREG preserves the Certifier identifier:

```text
SC-CERT-2026-0001
```

This remains a Source-System Identifier.

It does not replace the Registry Identifier.

```text
Registry Identifier:
SREG-2026-0001

Source-System Identifier:
SC-CERT-2026-0001
```

---

## Canonical Source Record

For SREG-2026-0001, the Authoritative Source Record is the Certification Package.

```text
Certification Package SC-CERT-2026-0001
```

Related Certifier artifacts may include:

- Certification Process Report;
- Certification Receipts;
- Certified Record;
- SCRD HTML;
- SCRD JSON.

These artifacts support the registration but do not replace the Certification Package as the authoritative source record.

---

## Certifier Correlation

The first registered item should preserve direct correlation with:

```text
https://satoshium.us/certifier/registry/
```

Additional related Certifier pages include:

```text
https://satoshium.us/certifier/certified-items/
https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/
```

This relationship should remain reciprocal where operationally appropriate.

---

## Registry Framework Dependencies

Registered Items depends on the following Registry frameworks:

- Entry Model;
- Records;
- Record Types;
- Scope;
- Definitions;
- Source Authority;
- Registrability;
- Identifiers;
- Relationships;
- Provenance;
- Schemas;
- Controlled Values;
- Validation;
- Publication;
- Versioning;
- Corrections;
- Status;
- Lifecycle;
- Catalog;
- History;
- Transparency;
- Governance.

---

## Registration Sequence

The operational sequence for a registered item is:

```text
Identify or Receive Source Record
  ↓
Confirm Registry Scope
  ↓
Confirm Source Authority
  ↓
Determine Registrability
  ↓
Assign Registry Record Type
  ↓
Assign Registry Identifier
  ↓
Preserve Source-System Identifier
  ↓
Establish Provenance and Relationships
  ↓
Construct SREG
  ↓
Validate
  ↓
Publish
  ↓
List in Registered Items
  ↓
Maintain Versions, Corrections, Status, Lifecycle, History, and Catalog Presence
```

---

## Validation Requirements

Before a SREG is listed in Registered Items, Validation should confirm:

- Registry Identifier is valid;
- Registry Record Type is approved;
- Source Authority is sufficient;
- Registrability has been determined;
- required SREG fields are present;
- Source-System Identifier is preserved;
- provenance is sufficient;
- relationships are valid;
- Controlled Values are approved;
- Registry Entry Version is assigned;
- Registry Status is valid;
- Registry Lifecycle State is valid;
- human-readable and machine-readable records agree;
- Publication requirements are satisfied;
- restrictions and notices are represented correctly.

---

## Publication Requirements

A SREG should not appear in Registered Items until:

- Publication has been authorized;
- the canonical human-readable Registry Entry is available;
- the machine-readable record is available;
- canonical URLs resolve;
- required notices are visible;
- Validation has produced an acceptable outcome;
- Source Authority and provenance remain clear;
- the item directory is complete.

---

## Correction Requirements

When a registered item requires Correction:

- preserve the prior Registry Entry Version;
- document the prior value;
- document the corrected value;
- identify Correction Authority;
- identify the correction date;
- provide the reason;
- update `registry-entry.html`;
- update `record.json`;
- update the item overview;
- update the item README when architecture or interpretation changes;
- preserve Correction History;
- update Registered Items metadata when necessary.

Material Corrections must not be silent.

---

## Versioning Requirements

Registry Entry Versioning should remain distinct from:

- Source-Record Version;
- SREG Base Schema Version;
- Record-Type Profile Version;
- Catalog Version;
- Definitions Version;
- Controlled-Value Set Version.

A new Registry Entry Version should be created when material Registry-owned content changes.

---

## History Requirements

Each registered item should preserve History for:

- initial registration;
- first Validation;
- first Publication;
- Registry Entry Version changes;
- Corrections;
- Registry Status changes;
- Registry Lifecycle transitions;
- relationship changes;
- provenance changes;
- restrictions;
- supersession;
- revocation;
- retirement;
- archival preservation.

---

## Status and Lifecycle Requirements

Registered Items should clearly distinguish:

### Registry Status

The current Registry condition of the SREG.

### Registry Lifecycle State

The stage occupied by the SREG within the Registry lifecycle.

### Source-Record Status

The status assigned by the Source Institution to the Authoritative Source Record.

These values must not be treated as interchangeable.

---

## Restrictions

A SREG may remain registered while access or Publication is restricted.

Restrictions may affect:

- Source Record access;
- Registry fields;
- downloadable artifacts;
- machine-readable records;
- Catalog indexing;
- historical materials.

A restriction does not automatically remove an item from Registered Items unless Governance or Publication rules require removal from current public view.

---

## Future Registered Items

As Registry expands, additional SREG directories may represent:

- jurisdictions;
- tools;
- media;
- certifications;
- attestations;
- signals;
- Chronicle records;
- Anchor records;
- Beacon records;
- workflows;
- institutions;
- schemas;
- Governance Decisions;
- other approved Registry Record Types.

Each new item should follow the same canonical directory pattern.

---

## Current Directory Structure

```text
registry/
└── registered-items/
    ├── index.html
    ├── README.md
    └── SREG-2026-0001/
        ├── index.html
        ├── registry-entry.html
        ├── record.json
        └── README.md
```

---

## Maintenance Requirements

When Registered Items changes:

- update `index.html`;
- update this README;
- add or remove SREG listings only through authorized Registry action;
- verify every item directory resolves;
- verify every `registry-entry.html` resolves;
- verify every `record.json` resolves;
- verify item-level READMEs remain current;
- verify Registry Identifiers are unique;
- verify Source-System Identifiers are preserved;
- verify human-readable and machine-readable records agree;
- verify Registry Status and Lifecycle values are current;
- verify Corrections and History remain discoverable;
- verify Certifier or other Source Institution correlations remain accurate;
- update Catalog indexes when required;
- document material changes in Registry History or Changelog.

---

## Guiding Principles

- Registered Items should list only completed Registry registrations.
- Every listed item should resolve to a dedicated SREG directory.
- The Registry Entry is the canonical SREG.
- The JSON record is the canonical machine-readable equivalent.
- Registry and Source Institution authority must remain distinct.
- Registry Identifier and Source-System Identifier must remain distinct.
- The Authoritative Source Record must remain clearly identified.
- Human-readable and machine-readable records must agree.
- Material Corrections must not be silent.
- Prior Registry Entry Versions must remain historically resolvable.
- Registered Items and Catalog should remain related but distinct.
- Every registration should preserve a durable path back to Source Authority.

---

## Disclaimer

Listing a SREG in Registered Items does not by itself establish:

- certification;
- attestation;
- endorsement;
- affiliation;
- Source Authority;
- Source-Record truth;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- permanent Source Record availability.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, Rule, Policy, Procedure, or external system.

---

## Guiding Statement

> Registered Items provides the list.
>
> The item directory provides the package.
>
> The Registry Entry is the SREG.
