# Satoshium Registry Identifiers

## Overview

The `registry/identifiers/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Identifier architecture.

The public page is published through:

```text
registry/identifiers/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how Satoshium Registry assigns, preserves, resolves, validates, corrects, and retires identifiers associated with Satoshium Registry Entries.

The Identifier architecture establishes:

- the permanent Registry Identifier assigned to each SREG;
- the distinction between Registry identity and Source-System identity;
- approved identifier domains;
- identifier structure and assignment authority;
- uniqueness, permanence, and non-reuse requirements;
- reserved, assigned, published, and historical identifier states;
- alias and alternate-reference handling;
- canonical URL and resolution requirements;
- correction and replacement procedures;
- supersession and successor relationships;
- validation rules;
- publication consistency.

---

## Constitutional Position

Identifier assignment follows a positive Registrability outcome and precedes operational SREG construction.

```text
Source Authority
  ↓
Registrability
  ↓
Registry Identifier Assignment
  ↓
SREG Construction
  ↓
Validation
  ↓
Publication
```

Registrability determines whether Registry should create a SREG.

Identifier assignment creates the permanent Registry identity for that SREG.

---

## Core Identifier Distinction

```text
Registry Identifier
  ≠
Source-System Identifier
```

The Registry Identifier identifies the SREG.

The Source-System Identifier identifies the Authoritative Source Record within the originating institution.

Registry connects these identifier domains without collapsing them.

---

## Canonical Identifier Relationship

```text
Registry Identifier
  ↓
SREG
  ↓
Source-System Identifier
  ↓
Authoritative Source Record
```

The Registry Identifier belongs to Registry.

The Source-System Identifier remains controlled by the Source Institution.

---

## Why Registry Identifiers Matter

Titles, URLs, repositories, institutions, and versions may change over time.

A permanent Registry Identifier allows the SREG to remain discoverable despite those changes.

Registry identity should remain stable when:

- a title changes;
- a canonical URL moves;
- a repository is reorganized;
- a Source Record receives a new version;
- a Source Institution changes through succession;
- the Registry Status changes;
- the Registry Lifecycle State changes;
- the SREG is corrected;
- the SREG is superseded;
- the SREG is revoked;
- the SREG is retired;
- the SREG is archived.

---

## Registry Authority

Registry is authoritative for:

- Registry Identifier assignment;
- Registry identifier namespaces;
- identifier patterns;
- uniqueness enforcement;
- reservation records;
- assignment records;
- canonical resolution;
- alias handling;
- identifier corrections;
- identifier replacements;
- identifier retirement;
- identifier history.

---

## Source Institution Authority

Source Institutions remain authoritative for identifiers assigned within their own systems.

Examples include:

- Certification Identifiers;
- Atlas package identifiers;
- jurisdiction identifiers;
- Attestation Identifiers;
- Chronicle event identifiers;
- Anchor integrity references;
- Beacon signal identifiers;
- Navigator workflow identifiers;
- repository identifiers;
- external publication identifiers.

Registry should preserve those identifiers without rewriting or replacing them.

---

## Identifier Domains

### Registry Identifier

Identifies one Satoshium Registry Entry.

### Source-System Identifier

Identifies the Authoritative Source Record within the Source Institution.

### External Identifier

Identifies the record, artifact, or subject within a third-party system.

### Version Identifier

Identifies a specific version, release, revision, or state.

### Artifact Identifier

Identifies a generated package, report, receipt, record, export, or derivative artifact.

### Relationship Identifier

Identifies a governed relationship object when Registry requires separate relationship identity.

### Integrity Identifier

Identifies a hash, signature, timestamp, commitment, Anchor reference, or other integrity object.

### Workflow Identifier

Identifies an operational review, validation, publication, correction, or Navigator workflow.

---

## Registry Identifier Requirements

Every production Registry Identifier should be:

- unique within Satoshium Registry;
- permanent after assignment;
- non-reusable;
- machine-readable;
- human-recognizable;
- resolvable;
- independent from mutable titles;
- independent from mutable URLs;
- independent from Source-System Identifiers;
- preserved after lifecycle changes;
- documented through an assignment record;
- validated before publication;
- historically traceable after correction.

---

## Identifier Structure

A production Registry Identifier should use a controlled pattern.

The canonical production pattern is:

```text
SREG-[YEAR]-[SEQUENCE]
```

Production examples:

```text
SREG-2026-0001
SREG-2026-0002
SREG-2026-0003
```

This production pattern was established by the inaugural operational Registry Entry, `SREG-2026-0001`.

Registry Record Type remains a separate controlled SREG field and is not encoded within the Registry Identifier.

---

## Identifier Segments

### Prefix

Identifies the Registry identifier domain.

Example:

```text
SREG
```

### Year Segment

Preserves the four-digit year in which the Registry Identifier is assigned.

The year is part of the permanent Registry Identifier and does not encode Registry Record Type.

### Record Type Separation

Registry Record Type remains a separate controlled SREG field.

Classification is governed through the Record Type field and applicable Record-Type Profile rather than through the Registry Identifier string.

### Sequence

Provides uniqueness within the applicable namespace.

---

## Assignment Authority

Registry alone assigns Registry Identifiers.

Assignment should occur only after:

- Source Authority review is complete or explicitly provisional;
- Registrability outcome permits progression;
- duplicate review is complete;
- one approved primary Record Type is selected;
- minimum identity metadata is available;
- identifier namespace is confirmed;
- sequence availability is confirmed;
- assignment event is recorded.

---

## Identifier Assignment Record

An assignment record should preserve:

- Registry Identifier;
- identifier namespace;
- identifier pattern version;
- Record Type;
- proposed SREG title;
- Source Institution;
- Source-System Identifier;
- assignment date;
- assignment authority;
- Registrability outcome reference;
- status at assignment;
- reservation or publication state;
- supporting workflow reference.

---

## Identifier States

### Reserved

The identifier is held for one approved pending SREG.

### Assigned

The identifier is permanently associated with one SREG.

### Published

The identifier resolves to the official Registry publication.

### Historical

The identifier remains resolvable after the SREG leaves active use.

These states should remain separate from Registry Status and Registry Lifecycle State.

---

## Reserved Identifiers

Registry may reserve an identifier after a positive Registrability outcome and before publication.

A reservation record should preserve:

- reserved identifier;
- reservation date;
- proposed Record Type;
- proposed Source Record;
- reservation status;
- expiration or review rule, if any;
- reservation reason;
- workflow or reviewer reference.

Reserved identifiers should not be silently reused if the proposal is withdrawn.

---

## Permanence and Non-Reuse

Once assigned, a production Registry Identifier must never be reassigned to another SREG.

This applies even if the original SREG becomes:

- superseded;
- revoked;
- retired;
- archived;
- withdrawn from active publication;
- historical;
- unavailable.

```text
Lifecycle may change.
Registry identity remains permanent.
```

---

## Source-System Identifiers

Registry should preserve Source-System Identifiers exactly as assigned whenever possible.

Registry should not:

- rewrite a Source-System Identifier for stylistic consistency;
- replace it with the Registry Identifier;
- infer an identifier that was never assigned;
- treat a URL as an identifier when it is only a location;
- collapse multiple source identifiers into one field;
- conceal source-identifier changes;
- represent a Registry Identifier as source-owned identity.

---

## Multiple Source Identifiers

A Source Record may have multiple valid identifiers.

Examples include:

- institutional identifier;
- repository identifier;
- publication identifier;
- package identifier;
- artifact identifier;
- legacy identifier;
- archive identifier;
- external standards identifier;
- integrity reference.

Registry should preserve each identifier together with:

- identifier value;
- identifier domain;
- issuing authority;
- purpose;
- status;
- effective dates;
- related version.

---

## Aliases and Alternate References

Aliases may support discovery without replacing the canonical Registry Identifier.

Potential aliases include:

- former titles;
- abbreviations;
- legacy identifiers;
- common names;
- translated names;
- former URLs;
- repository paths;
- external database references.

```text
An alias improves discovery.
It does not become canonical Registry identity.
```

---

## Identifier Resolution

A published Registry Identifier should resolve to the canonical SREG presentation.

Resolution should expose links or references to:

- human-readable SREG;
- machine-readable SREG;
- Authoritative Source Record;
- Source Institution;
- Source-System Identifier;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- correction history;
- supersession relationships;
- successor relationships;
- archival references.

---

## Canonical URLs

The Registry Identifier should remain independent from the canonical publication URL.

The canonical publication pattern currently resolves through Registered Items.

Example:

```text
https://satoshium.us/registry/registered-items/SREG-2026-0001/
```

If the publication path changes:

- preserve the Registry Identifier;
- update the canonical URL;
- maintain redirects when practical;
- preserve prior URL references;
- document material publication changes.

---

## Identifier Corrections

A Registry Identifier should not change merely because:

- title changes;
- source URL changes;
- source version changes;
- Source Institution changes;
- SREG receives a correction;
- Registry Status changes;
- Registry Lifecycle State changes.

Identifier correction should be exceptional.

Potential grounds include:

- assignment collision;
- malformed identifier;
- incorrect namespace;
- assignment to the wrong SREG;
- security or integrity failure;
- governance-directed identifier migration.

---

## Correction Without Erasure

When an identifier defect requires replacement, Registry should preserve:

- original identifier;
- replacement identifier;
- correction date;
- reason;
- governing authority;
- affected SREG;
- redirect behavior;
- correction record;
- machine-readable replacement relationship.

```text
An identifier correction changes the reference.
It must not erase the historical path.
```

---

## Supersession and Successor Identifiers

When one SREG is replaced by another:

```text
Prior Registry Identifier
  ↓
Superseded SREG
  ↓
Successor Relationship
  ↓
New Registry Identifier
```

The prior identifier remains permanent and resolvable.

Supersession creates a relationship between Registry identities.

It does not overwrite one identity with another.

---

## Version Identifiers

Registry Identifier and Registry Entry Version must remain separate.

Example:

```text
Registry Identifier: SREG-2026-0001
Registry Entry Version: 1.0
```

The Registry Identifier identifies the continuing SREG.

The Registry Entry Version identifies one state of that SREG.

Other version domains may include:

- Source-Record Version;
- SREG Base Schema Version;
- Record-Type Profile Version;
- Registry Schema Specification Version;
- Registry Rules Version;
- Registry Policy Version;
- Suite Standards Version;
- Suite Methodology Version.

---

## Relationship to Record Types

Registry Record Type does not alter the canonical Registry Identifier pattern.

The approved Record Type remains a separate controlled SREG field and is authoritative for classification.

```text
Identifier preserves Registry identity.
Record Type preserves Registry classification.
The two remain deliberately separate.
```

---

## Relationship to Relationships

Identifiers provide the stable endpoints used in Registry relationships.

A relationship should preserve:

- source identifier;
- source identifier domain;
- target identifier;
- target identifier domain;
- relationship type;
- direction;
- authority;
- effective date;
- version context;
- supporting reference.

---

## Relationship to Registry Lifecycle

The Registry Identifier remains stable across lifecycle conditions such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

Lifecycle describes institutional condition.

Identifier preserves Registry identity.

---

## Relationship to Publication

Official publication should expose the Registry Identifier consistently across:

- page title;
- metadata;
- canonical URL;
- human-readable SREG;
- machine-readable SREG;
- downloadable artifacts;
- relationship objects;
- correction records;
- history;
- version references.

---

## Relationship to Corrections

Corrections may affect titles, references, metadata, classification, or relationships without changing the Registry Identifier.

An identifier-specific correction should preserve:

- prior identifier state;
- corrected identifier state;
- reason;
- correction authority;
- effective date;
- affected SREG;
- affected Registry Entry Version;
- public correction reference.

---

## Relationship to Source Authority

Source Authority identifies the institution responsible for the Source Record.

Identifier architecture preserves the separate identities of:

- the SREG;
- the Source Record;
- external systems;
- versions;
- artifacts;
- workflows;
- integrity objects.

Identifier assignment does not create Source Authority.

---

## Relationship to Registrability

A production Registry Identifier should be assigned only after a positive Registrability outcome.

```text
Registrability authorizes identity creation.
Identifier assignment creates Registry identity.
```

Rejected or non-registrable proposals should not receive production identifiers unless an approved reservation policy explicitly requires one.

---

## Identifier Validation

Identifier validation should confirm:

- format matches the approved pattern;
- identifier is unique;
- identifier has not been reused;
- namespace is valid;
- year and sequence segments match the approved production pattern;
- assignment record exists;
- Registrability reference exists;
- Registry Identifier and Source-System Identifier are distinct;
- aliases are not represented as canonical identifiers;
- human-readable and machine-readable SREGs agree;
- resolution target exists or is intentionally historical;
- correction history is preserved;
- supersession relationships are preserved.

---

## Invalid Identifier Conditions

Invalid conditions include:

- duplicate Registry Identifier;
- reused identifier;
- identifier assigned before Registrability approval;
- Source-System Identifier used as Registry Identifier;
- mutable title embedded as required identity;
- incorrect year or sequence segment;
- missing assignment record;
- unresolvable published identifier without explanation;
- alias represented as canonical identity;
- silent identifier replacement;
- human-readable and machine-readable mismatch;
- namespace collision.

---

## Suite Identifier Examples

### Certifier

A Certification Identifier such as:

```text
SC-CERT-2026-0001
```

identifies a Certifier-owned Certification Package.

A Registry Certification SREG must receive its own separate Registry Identifier.

### Atlas

Atlas jurisdiction codes, package identifiers, repository paths, canonical JSON references, and generation-manifest references remain Atlas-controlled source identifiers.

### Attestor

Attestation identifiers remain controlled by Attestor.

Registry assigns a separate Registry Identifier to the SREG cataloging the attestation.

### Anchor

Hashes, signatures, timestamps, and integrity references remain Anchor or source-system identifiers and may be linked from a SREG.

### Chronicle

Chronicle event identifiers remain controlled by Chronicle.

### Beacon

Signal identifiers remain controlled by Beacon.

### Navigator

Workflow identifiers remain controlled by Navigator.

---

## Current Directory Structure

```text
registry/
└── identifiers/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Identifiers page.

### `README.md`

The directory-level documentation explaining Registry identity, identifier domains, assignment, permanence, resolution, aliases, correction, validation, and maintenance.

Future supporting materials may include:

```text
identifiers/
├── index.html
├── README.md
├── identifier-pattern.md
├── assignment-policy.md
├── reserved-identifiers.md
├── aliases.md
├── resolution.md
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
- Registry Entry Model;
- Registry Record Types;
- Registry Schemas;
- Registry Relationships;
- Registry Provenance;
- Registry Validation;
- Registry Publication;
- Registry Lifecycle;
- Registry Status;
- Registry Corrections;
- Registry Policies;
- Registry Procedures;
- Registry Governance;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Identifier architecture changes:

- update `index.html`;
- update this README;
- update identifier pattern definitions;
- update namespace rules;
- update assignment procedures;
- update reservation rules;
- update resolution requirements;
- update alias handling;
- update correction requirements;
- update supersession rules;
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

- Registry Identifier and Source-System Identifier remain separate.
- Registry alone assigns Registry Identifiers.
- Every production Registry Identifier is unique.
- Assigned identifiers are permanent.
- Assigned identifiers are never reused.
- Registry identity remains stable through lifecycle change.
- URLs are locations, not identity.
- Aliases support discovery but do not replace canonical identity.
- Identifier correction must preserve historical traceability.
- Supersession creates a relationship between identities.
- Version identifiers remain separate from Registry identity.
- Registry Record Type is not embedded in the production Registry Identifier pattern.
- Identifier assignment does not create Source Authority.
- Identifier assignment does not certify the Source Record.
- Human-readable and machine-readable forms must agree.

---

## Disclaimer

Registry Identifier assignment does not by itself establish:

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
- source truth;
- permanent source availability.

Those remain controlled by the Source Institution, rights holder, governing authority, Source Record, applicable policy, or external system.

---

## Guiding Statement

> The Registry Identifier identifies the SREG.
>
> The Source-System Identifier identifies the Source Record.
>
> Their relationship must be preserved without collapsing their authority.
