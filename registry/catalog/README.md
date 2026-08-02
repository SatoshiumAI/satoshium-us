# Satoshium Registry Catalog

## Overview

The `registry/catalog/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Catalog framework.

The public page is published through:

```text
registry/catalog/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define how published Satoshium Registry Entries are:

- organized;
- browsed;
- searched;
- filtered;
- resolved;
- related;
- versioned;
- presented;
- corrected;
- historically preserved.

The Catalog is the public discovery and resolution layer of Satoshium Registry.

It presents Registry-owned SREGs while preserving direct attribution to their Authoritative Source Records and Source Institutions.

---

## Constitutional Position

The Catalog sits above published SREGs.

```text
Authoritative Source Record
  ↓
SREG
  ↓
Validation
  ↓
Publication
  ↓
Registry Catalog
```

Publication makes an individual SREG available.

The Catalog makes the wider body of published SREGs discoverable as one coherent Registry system.

---

## Core Principle

```text
Publication makes a record available.
The Catalog makes the Registry discoverable.
Resolution preserves identity.
```

The Catalog should support discovery without changing canonical SREG meaning or source authority.

---

## Why the Catalog Matters

The Catalog provides:

- a unified public view of published Registry records;
- stable Registry Identifier resolution;
- browsing by Record Type;
- browsing by Source Institution;
- search by identifier, title, source, and metadata;
- filtering by governed fields;
- relationship navigation;
- version awareness;
- correction and notice visibility;
- access to machine-readable records;
- access to downloadable artifacts;
- historical continuity.

---

## Canonical Catalog Model

```text
Published SREGs
  ↓
Catalog Metadata
  ↓
Browse, Search, Filter, Resolve
  ↓
Canonical SREG Page
```

The Catalog is an index and presentation layer.

The canonical SREG remains the authoritative Registry object.

---

## Catalog Functions

The Registry Catalog may support:

- browsing published SREGs;
- searching by Registry Identifier;
- searching by Source-System Identifier;
- searching by title;
- searching by Source Institution;
- searching by keyword;
- filtering by Registry Record Type;
- filtering by Registry Status;
- filtering by Registry Lifecycle State;
- filtering by Source Institution;
- filtering by publication or update date;
- resolving Registry Identifiers;
- navigating typed relationships;
- viewing current and historical versions;
- viewing corrections;
- viewing notices;
- viewing restrictions;
- viewing supersession;
- accessing machine-readable records;
- accessing downloadable artifacts;
- supporting Suite discovery;
- supporting external-system discovery.

---

## Catalog Interaction Modes

### Browse

Presents ordered collections of published SREGs by institutional category.

### Search

Finds SREGs through identifiers, titles, source references, and indexed metadata.

### Filter

Narrows results through governed fields and Controlled Values.

### Resolve

Connects a Registry Identifier to its canonical current and historical Registry context.

---

## Catalog Entry

Each Catalog result should represent one published SREG.

A Catalog entry may display:

- Registry Identifier;
- title;
- short description;
- Registry Record Type;
- Source Institution;
- Source-System Identifier;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- publication date;
- last update date;
- restriction indicator;
- notice indicator;
- canonical SREG link;
- machine-readable record link.

---

## Illustrative Catalog Entry

```text
registry_identifier: "SREG-JUR-2026-0001"
title: "El Salvador"
record_type: "jurisdiction"
source_institution: "Satoshium Atlas"
source_system_identifier: "atlas-jurisdiction-el-salvador"
registry_status: "active"
registry_lifecycle_state: "published"
registry_entry_version: "1.0.0"
```

This example is illustrative and does not establish final schema syntax.

---

## Primary Catalog Views

### All Records

The complete current public Catalog.

### By Record Type

Published SREGs grouped by approved Registry Record Type.

### By Source Institution

Published SREGs grouped by Source Institution.

### By Status

Published SREGs grouped by current Registry Status.

### By Lifecycle

Published SREGs grouped by Registry Lifecycle State.

### Recently Published

SREGs ordered by first-publication date.

### Recently Updated

SREGs ordered by latest material update.

### Corrections and Notices

SREGs carrying material public notices.

### Historical Records

Superseded, revoked, retired, or archived SREGs.

---

## Record-Type Collections

Catalog collections may include:

- Tools;
- Jurisdictions;
- Media;
- Certifications;
- Attestations;
- Signals;
- Events;
- Integrity References;
- Workflows;
- Institutions;
- Schemas;
- Policies;
- Procedures;
- Governance Decisions.

Catalog collections reflect Registry classifications.

They do not redefine the Source Records placed within them.

---

## Searchable Fields

Catalog search may index:

- Registry Identifier;
- Source-System Identifier;
- title;
- alternate titles;
- description;
- Registry Record Type;
- Source Institution;
- canonical source URL;
- jurisdiction;
- keywords;
- relationships;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- publication date;
- correction metadata;
- notice metadata.

---

## Search Behavior

Catalog search should:

- prioritize exact Registry Identifier matches;
- preserve Source-System Identifier matches;
- distinguish current SREGs from historical SREGs;
- surface current records before historical records when relevance is comparable;
- expose disputed conditions;
- expose restricted conditions;
- expose superseded conditions;
- expose revoked conditions;
- expose archived conditions;
- avoid presenting aliases as canonical identity;
- preserve Source Institution attribution;
- support machine-readable query and response patterns when implemented.

---

## Catalog Filters

Filters should use approved Controlled Values where applicable.

Potential Catalog filters include:

- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Source Institution;
- Access Condition;
- Validation Outcome;
- Publication Readiness Outcome;
- publication date range;
- last-update date range;
- version condition;
- notice type;
- historical condition.

---

## Canonical Resolution

Every published Registry Identifier should resolve to its canonical current SREG context.

Illustrative path:

```text
https://satoshium.us/registry/catalog/SREG-JUR-2026-0001/
```

The canonical page should expose:

- current Registry Entry Version;
- current Registry Status;
- current Registry Lifecycle State;
- Source Institution;
- Authoritative Source Record;
- machine-readable form;
- relationships;
- provenance;
- corrections;
- historical versions;
- supersession notices;
- archival notices.

---

## Machine-Readable Catalog

Registry may publish a machine-readable Catalog index.

Illustrative path:

```text
https://satoshium.us/registry/catalog/index.json
```

A machine-readable Catalog may include:

- Catalog Version;
- generation date;
- included Registry Identifiers;
- current Registry Entry Versions;
- Registry Record Types;
- Source Institutions;
- Registry Status values;
- Registry Lifecycle States;
- canonical URLs;
- machine-readable URLs;
- publication dates;
- update dates;
- notices;
- restrictions;
- generation references;
- integrity references.

---

## Catalog Versioning

The Catalog itself may be versioned independently from individual SREGs.

Catalog version records should preserve:

- Catalog Version;
- generation date;
- included records;
- added SREGs;
- updated SREGs;
- records removed from current views;
- schema or index-format version;
- generation method;
- integrity reference;
- prior Catalog Version.

```text
Catalog Version describes the indexed collection.
Registry Entry Version describes an individual SREG.
```

---

## Current and Historical Catalog Views

The current Catalog should prioritize current operational SREGs.

Historical Catalog views should preserve:

- superseded SREGs;
- revoked SREGs;
- retired SREGs;
- archived SREGs;
- prior Registry Entry Versions;
- prior Catalog Versions;
- correction history;
- former classifications;
- former Registry Status values;
- former Registry Lifecycle States;
- former canonical paths where applicable.

---

## Relationship Navigation

Catalog pages may provide navigable relationships between:

- Source Record and Source Institution;
- certification and certified subject;
- attestation and attested subject;
- jurisdiction and related certifications;
- event and documented records;
- signal and announced record;
- integrity reference and protected artifact;
- workflow and dependent records;
- predecessor and successor SREGs;
- current and historical versions;
- derived and archival artifacts.

Relationship navigation should preserve:

- direction;
- identifier domains;
- Relationship Authority;
- Relationship Status;
- version context;
- temporal context;
- correction history.

---

## Notices and Conditions

Catalog results and canonical SREG pages should visibly identify material conditions such as:

- provisional publication;
- restricted access;
- source unavailable;
- validation warning;
- correction issued;
- disputed relationship;
- superseded entry;
- revoked entry;
- retired entry;
- archived entry;
- external-source disclaimer;
- rights or reuse limitation;
- Governance exception;
- migration notice.

---

## Restricted Catalog Entries

Restricted SREGs may appear with limited public metadata when appropriate.

A restricted Catalog entry may expose:

- Registry Identifier;
- title or generalized title;
- Registry Record Type;
- Source Institution;
- Registry Status;
- Registry Lifecycle State;
- restriction notice;
- public provenance summary;
- review date;
- access condition.

Restricted content must not be exposed through:

- search indexes;
- machine-readable Catalog files;
- cached excerpts;
- downloadable artifacts;
- public relationship summaries.

---

## Catalog Ordering

Catalog views may support ordering by:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- first-publication date;
- last-update date;
- Registry Status;
- Registry Lifecycle State;
- relevance;
- historical sequence.

Catalog ordering should not imply:

- institutional rank;
- endorsement;
- quality;
- priority;
- substantive importance;

unless such meaning is explicitly governed and disclosed.

---

## Catalog Metadata

Catalog-specific metadata may include:

- Catalog inclusion date;
- Catalog display title;
- Catalog summary;
- search keywords;
- browse collections;
- filter facets;
- sort values;
- thumbnail or visual reference;
- featured condition;
- highlighted condition;
- indexing status;
- last-indexed date;
- Catalog Version.

Catalog metadata supports discovery.

It must not silently change canonical SREG meaning.

---

## Catalog Inclusion

A SREG should enter the public Catalog only when:

- required Validation permits publication;
- official Publication is complete;
- canonical resolution is functioning;
- Catalog metadata is complete;
- Controlled Values are valid;
- notices are correctly represented;
- restrictions are correctly represented;
- machine-readable and human-readable forms agree;
- search and filter fields are safe for indexing.

---

## Removal from Current Views

A SREG may be removed from current browse views when it becomes:

- superseded;
- revoked;
- retired;
- archived;
- withdrawn from public access;
- restricted from indexing;
- invalidly published.

Removal from current views should not erase:

- Registry Identifier resolution;
- historical Catalog presence;
- prior Registry Entry Versions;
- correction history;
- supersession history;

unless access itself must be restricted.

---

## Catalog Validation

Validation should confirm:

- Catalog entry points to the correct Registry Identifier;
- title matches the canonical SREG;
- Registry Record Type matches the canonical SREG;
- Source Institution is accurate;
- Registry Status is current;
- Registry Lifecycle State is current;
- Registry Entry Version is current;
- canonical URL resolves;
- machine-readable URL resolves;
- filters use approved Controlled Values;
- notices are visible;
- restrictions are visible;
- historical SREGs are not presented as current;
- restricted fields are not indexed;
- Catalog metadata does not contradict canonical SREG content;
- current and historical views remain distinguishable.

---

## Invalid Catalog Conditions

Invalid conditions include:

- Catalog entry resolves to the wrong SREG;
- duplicate canonical Catalog entry;
- missing Registry Identifier;
- incorrect Registry Record Type;
- incorrect Source Institution;
- stale Registry Status;
- stale Registry Lifecycle State;
- historical version presented as current;
- broken canonical URL;
- broken machine-readable URL;
- restricted information exposed;
- unapproved filter value;
- Catalog summary contradicts the SREG;
- superseded SREG presented without notice;
- revoked SREG presented without notice;
- Catalog metadata silently alters canonical meaning.

---

## Relationship to Publication

Publication creates the official SREG.

The Catalog indexes and presents that published SREG for discovery and resolution.

```text
Publication establishes availability.
The Catalog establishes discoverability.
```

---

## Relationship to Identifiers

The Catalog uses Registry Identifiers as canonical resolution keys.

Source-System Identifiers and aliases may support discovery.

They must not replace the permanent Registry Identifier.

---

## Relationship to Relationships

The Catalog makes typed Registry Relationships navigable across:

- SREG pages;
- Record-Type collections;
- Source Institution collections;
- current views;
- historical views;
- correction records;
- supersession records.

---

## Relationship to Controlled Values

Catalog filters, facets, labels, notices, and collection names should use approved Controlled Values whenever the underlying field is governed.

---

## Relationship to Provenance

Catalog entries should preserve enough provenance to identify:

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier;
- canonical source reference;
- source availability;
- historical source context.

The Catalog should not replace the fuller provenance available in the canonical SREG.

---

## Relationship to Versioning

The Catalog should distinguish:

- Catalog Version;
- Registry Entry Version;
- Source-Record Version;
- schema version;
- Record-Type Profile Version.

Historical Catalog views should preserve prior Registry Entry Versions without presenting them as current.

---

## Relationship to Beacon

Beacon may announce:

- newly published SREGs;
- updated SREGs;
- corrected SREGs;
- superseded SREGs;
- archived SREGs.

Beacon signals may link into the Catalog.

Registry remains authoritative for Catalog entries and SREGs.

---

## Relationship to Chronicle

Chronicle may record:

- historically significant Catalog releases;
- major Registry publication milestones;
- material institutional transitions;
- major changes to Catalog architecture.

Registry remains authoritative for Catalog Versions and Catalog inclusion history.

Chronicle remains authoritative for Chronicle-created event records.

---

## Relationship to Governance

Registry Governance should control:

- Catalog inclusion requirements;
- Catalog metadata fields;
- browse collections;
- search behavior;
- filter facets;
- ordering rules;
- featured conditions;
- restricted indexing;
- Catalog Versioning;
- historical Catalog views;
- machine-readable Catalog publication;
- Catalog corrections;
- Catalog withdrawal.

---

## Current Directory Structure

```text
registry/
└── catalog/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Catalog framework page.

### `README.md`

The directory-level documentation explaining discovery, resolution, browsing, search, filtering, Catalog entries, versions, restrictions, Validation, and maintenance.

Future operational materials may include:

```text
catalog/
├── index.html
├── index.json
├── README.md
├── catalog-schema.md
├── search.md
├── filters.md
├── collections.md
├── notices.md
├── current/
├── historical/
├── records/
├── history/
└── versions/
```

These materials should be introduced only when corresponding operational Catalog resources exist.

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
- Registry Controlled Values;
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
- Registry History;
- Registry Transparency;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Catalog architecture changes:

- update `index.html`;
- update this README;
- update Catalog entry requirements;
- update Catalog metadata fields;
- update browse collections;
- update searchable fields;
- update search behavior;
- update filters;
- update ordering rules;
- update canonical resolution requirements;
- update machine-readable Catalog requirements;
- update Catalog Versioning;
- update historical views;
- update relationship navigation;
- update notice handling;
- update restricted-indexing requirements;
- update Catalog inclusion criteria;
- update removal-from-current-view criteria;
- update Catalog Validation;
- update affected Controlled Values;
- update affected schemas;
- update Publication requirements;
- preserve prior Catalog Versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable materials.

---

## Guiding Principles

- The Catalog presents published SREGs.
- The canonical SREG remains authoritative for Registry content.
- The Authoritative Source Record remains under Source Institution authority.
- Registry Identifiers are the canonical resolution keys.
- Search aliases must not replace canonical identity.
- Filters should use governed Controlled Values.
- Catalog metadata must not alter canonical meaning.
- Current and historical views must remain distinguishable.
- Restrictions must apply to indexes as well as pages.
- Corrections and supersession must remain visible.
- Removal from current views must not erase history.
- Catalog Version and Registry Entry Version must remain separate.
- Ordering must not imply endorsement or importance.
- Human-readable and machine-readable Catalog forms must agree.
- The Catalog should make discovery easier without weakening institutional boundaries.

---

## Disclaimer

The Registry Catalog does not by itself establish:

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
- institutional rank;
- substantive importance;
- permanent source availability.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, Rule, Policy, Procedure, or external system.

---

## Guiding Statement

> Publication makes a record available.
>
> The Catalog makes the Registry discoverable.
>
> Resolution preserves identity.
