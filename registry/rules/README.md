# Satoshium Registry Rules

## Overview

The `registry/rules/` directory contains the public Registry Rules page and supporting documentation that define the foundational institutional requirements governing Satoshium Registry.

The public page is published through:

```text
registry/rules/index.html
```

This `README.md` serves as the directory-level documentation for that page.

Registry Rules govern how Satoshium Registry Entries, or SREGs, are:

- identified;
- classified;
- attributed;
- related;
- versioned;
- validated;
- published;
- updated;
- corrected;
- superseded;
- revoked;
- retired;
- archived;
- preserved.

---

## Purpose of This Directory

The purpose of this directory is to explain:

- what Registry Rules are;
- where they sit in the Suite hierarchy;
- what authority they govern;
- how they differ from policies and procedures;
- which foundational requirements apply to SREGs;
- how Registry preserves Source Institution authority;
- how Registry maintains identity, provenance, status, lifecycle, versions, relationships, and history;
- how rules are reviewed, versioned, and maintained.

---

## Constitutional Position

Registry Rules operate within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Rules
  ↓
Registry Policies
  ↓
Registry Procedures
  ↓
Published SREG
```

### Suite Standards

Define shared expectations across the Satoshium Suite.

### Suite Methodology

Defines implementation principles and repeatable methods.

### Suite Interoperability

Defines how institutions exchange identifiers, references, relationships, and metadata while preserving authority boundaries.

### Registry Rules

Define Registry's foundational institutional requirements.

### Registry Policies

Define how the rules apply to specific operational domains such as creation, update, correction, and retirement.

### Registry Procedures

Define the repeatable steps used to implement the policies.

### Published SREG

The resulting operational Registry Entry.

Registry Rules are subordinate to Suite Standards, Suite Methodology, and Suite Interoperability.

---

## Rules, Policies, and Procedures

These three layers serve different purposes.

```text
Rules
  = foundational institutional requirements

Policies
  = domain-specific implementation requirements

Procedures
  = repeatable operational steps
```

A policy must not contradict a Registry Rule.

A procedure must not contradict the policy or rule it implements.

---

## Canonical Registry Architecture

Registry Rules govern the following operational hierarchy:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

### Satoshium Registry

The institution responsible for Registry operations and the public catalog.

### Registry Entry (SREG)

Registry's canonical operational object.

### Registry Record Type

The controlled primary classification assigned to the SREG.

### Authoritative Source Record

The source object created and maintained by the originating institution.

---

# Rule 1 — Registry Governs the SREG

Registry is authoritative for Registry-owned information.

Registry authority includes:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry corrections;
- Registry publication;
- Registry archival history;
- Registry catalog presentation.

Registry authority applies to the SREG.

It does not automatically extend to the Source Record.

---

# Rule 2 — Source Authority Must Be Preserved

The Source Institution retains authority over the Authoritative Source Record.

Source authority may include:

- Source-System Identifier;
- source content;
- source meaning;
- source version;
- Source-Record Status;
- institutional classification;
- certification outcomes;
- attestation conclusions;
- ownership;
- licensing;
- legal rights;
- external authority.

Registry may report or reference source-controlled values.

Registry must not redefine them.

---

# Rule 3 — The SREG Must Not Replace the Source

A SREG catalogs an Authoritative Source Record.

It must not silently become a substitute for:

- a missing Source Record;
- an inaccessible Source Record;
- an undefined source object;
- a source-controlled institutional decision;
- source ownership or legal authority.

When the Source Record is unavailable, Registry may preserve historical references and availability context.

It must not invent the source.

---

# Rule 4 — Every SREG Must Be Identifiable

Every operational SREG must contain sufficient information to distinguish it from other Registry Entries.

Required identity elements should include:

- Registry Identifier;
- title;
- Registry Record Type;
- Source Institution;
- Authoritative Source Record;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- public reference context.

---

# Rule 5 — Identifiers Must Remain Distinct

The Registry Identifier identifies the SREG.

The Source-System Identifier identifies the Authoritative Source Record.

```text
Registry Identifier
  ≠
Source-System Identifier
```

Registry must not:

- overwrite the source identifier;
- reuse a Registry Identifier;
- present one identifier as the other;
- invent a source identifier when none exists.

---

# Rule 6 — Every SREG Must Have One Primary Record Type

Every operational SREG must receive one approved primary Registry Record Type.

Current initial types include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Secondary classifications may be permitted by the applicable Record-Type Profile.

They must not conflict with the primary type.

---

# Rule 7 — Record Types Require Governance

A new Record Type must not be improvised during individual record creation.

New Record Types should require:

- documented need;
- defined scope;
- clear authority boundary;
- approved name;
- corresponding Record-Type Profile;
- schema support;
- relationship rules;
- validation rules;
- governance approval;
- changelog documentation.

---

# Rule 8 — Relationships Must Be Typed

Relationships among Registry and source objects must use approved relationship types.

Examples include:

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
- depends on;
- integrates with;
- part of;
- supersedes;
- superseded by;
- coordinated through.

Relationships should preserve direction where applicable.

---

# Rule 9 — Status Domains Must Remain Separate

Registry Status must remain distinct from source-controlled status domains.

Examples include:

```text
Registry Status
  ≠
Source-Record Status
```

```text
Registry Status
  ≠
Certification Status
```

```text
Registry Status
  ≠
Attestation Status
```

A Source Record may be revoked, retired, or unavailable while its SREG remains active as a historical Registry Entry.

---

# Rule 10 — Lifecycle Domains Must Remain Separate

Registry Lifecycle State describes the institutional condition of the SREG.

It does not replace:

- source lifecycle;
- certification lifecycle;
- attestation lifecycle;
- tool lifecycle;
- jurisdictional status;
- media publication lifecycle.

Registry may preserve a Source Record after the source object leaves active use.

---

# Rule 11 — Versions Must Be Independently Traceable

Registry must preserve distinctions among:

- Registry Entry Version;
- Source-Record Version;
- SREG schema version;
- Record-Type Profile version;
- Registry Schema Specification version;
- Registry Rules version;
- Registry Policy version;
- Suite Standards version;
- Suite Methodology version.

A version change in one domain does not automatically imply a version change in another.

---

# Rule 12 — Official Forms Must Agree

Human-readable and machine-readable forms of the same SREG must agree on material values.

These include:

- Registry Identifier;
- title;
- Record Type;
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

# Rule 13 — Registrability Must Be Determined

Registry may create a SREG only when:

- the Source Institution is identifiable;
- the Authoritative Source Record is identifiable;
- sufficient provenance exists;
- an approved Record Type applies;
- required references can be established;
- required relationships can be established;
- the SREG can satisfy the applicable schema and profile;
- no unresolved authority conflict prevents publication.

Registrability is a Registry determination.

It is not:

- certification;
- attestation;
- endorsement;
- ownership;
- legal recognition;
- verification.

---

# Rule 14 — Provenance Must Be Preserved

Every operational SREG should preserve enough information to determine:

- where the Source Record came from;
- which institution controls it;
- what identifier the source uses;
- which version was referenced;
- where the source can be found;
- when Registry cataloged it;
- what changes occurred later.

Provenance supports accountability and future interpretation.

---

# Rule 15 — References Must Be Durable

Registry should preserve durable references whenever available.

These may include:

- canonical source URLs;
- repository paths;
- machine-readable source records;
- public institutional pages;
- Certification Packages;
- SCRDs;
- attestations;
- Chronicle events;
- Anchor references;
- Beacon signals;
- Navigator workflows;
- archival locations;
- integrity references.

When a reference changes, the prior reference should remain historically discoverable where practical.

---

# Rule 16 — History Must Not Be Silently Erased

Registry should preserve:

- prior material versions;
- Update Records;
- Correction Records;
- supersession history;
- revocation history;
- retirement history;
- archival history;
- prior references;
- prior relationships.

History may be removed only when required by:

- law;
- privacy;
- safety;
- security;
- rights restrictions;
- another documented exceptional condition.

---

# Rule 17 — Updates and Corrections Must Remain Distinct

### Update

Reflects new, changed, expanded, or newly available information.

### Correction

Repairs an error in Registry-owned information or Registry-controlled publication.

An update must not conceal a correction.

A correction must not be presented as a routine update when accountability requires explicit correction history.

---

# Rule 18 — Retirement Must Not Mean Disappearance

Superseded, revoked, retired, or archived SREGs should remain discoverable when legally and operationally appropriate.

Retirement history should preserve:

- Registry Identifier;
- affected version;
- retirement action;
- reason;
- effective date;
- successor or replacement;
- Source Record condition;
- archival location;
- relationships;
- prior history.

---

# Rule 19 — Deletion Is Exceptional

Registry should normally prefer:

- correction;
- update;
- redaction;
- supersession;
- revocation;
- retirement;
- archival.

Deletion may be considered for:

- unlawful publication;
- sensitive information published in error;
- security-critical information;
- malicious content;
- accidental test records;
- invalid records with no meaningful independent history;
- another documented exceptional condition.

Deletion must not be used merely to simplify history.

---

# Rule 20 — Validation Is Required

Operational SREGs must satisfy:

- Registry Schema Specification;
- SREG Base Schema;
- applicable Record-Type Profile;
- controlled-value requirements;
- relationship rules;
- identifier requirements;
- version requirements;
- publication consistency requirements.

Validation confirms Registry structure.

It does not certify or attest to the Source Record.

---

# Rule 21 — Registration Does Not Create Authority

Registration does not create:

- certification;
- attestation;
- ownership;
- legal rights;
- governmental recognition;
- regulatory approval;
- verification;
- endorsement;
- affiliation;
- truth;
- Source Institution authority.

Registration creates a Registry Entry.

Authority remains with the applicable source.

---

## Schema Rule

Registry schemas follow this hierarchy:

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

Record Types must extend one shared SREG architecture.

They should not create unrelated Registry record models.

---

## Operational Rule

Registry uses the following institutional method:

```text
Identify or Receive Source Record
  ↓
Confirm Source Institution and Authority
  ↓
Determine Registrability
  ↓
Assign Record Type
  ↓
Assign Registry Identifier
  ↓
Preserve Source-System Identifier
  ↓
Establish References and Relationships
  ↓
Construct SREG
  ↓
Validate
  ↓
Publish
  ↓
Maintain Lifecycle, Versions, Corrections, and History
```

Policies implement this method for specific operational domains.

Procedures define the repeatable steps.

---

## Interoperability Rule

Registry must connect Suite institutions without absorbing their authority.

Atlas, Certifier, Chronicle, Anchor, Beacon, Attestor, and Navigator retain authority over their own canonical objects.

Registry creates SREGs that catalog and relate those objects.

```text
Interoperability connects authority.
It does not collapse authority.
```

---

## Relationship to Registry Policies

Registry Rules are implemented through policies including:

- Registry Record Creation Policy;
- Registry Record Update Policy;
- Registry Correction Policy;
- Registry Record Retirement Policy;
- future approved Registry policies.

Policies must remain consistent with these Rules.

---

## Relationship to Registry Procedures

Registry Procedures define how Registry performs operational work.

Procedures may include:

- record creation;
- update processing;
- correction processing;
- retirement processing;
- identifier assignment;
- classification review;
- source-authority review;
- validation;
- publication reconciliation;
- version maintenance;
- archival processing.

Procedures remain subordinate to Rules and Policies.

---

## Rule Governance

Registry Rules should be reviewed when:

- Suite Standards change;
- Suite Methodology changes;
- Suite Interoperability changes;
- Registry authority boundaries change;
- new Record Types are introduced;
- schemas change materially;
- identifier architecture changes;
- lifecycle or status frameworks change;
- repeated policy conflicts reveal ambiguity;
- publication architecture changes;
- new Suite institutions are introduced.

Prior rule versions should remain preserved and discoverable.

---

## Current Directory Structure

The current directory structure is:

```text
registry/
└── rules/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Rules page.

### `README.md`

The directory-level documentation explaining the purpose, hierarchy, authority, requirements, implementation relationships, governance, and maintenance of Registry Rules.

Future supporting files may include:

```text
rules/
├── index.html
├── README.md
├── versions/
├── governance/
└── history/
```

These directories should be introduced only when the corresponding operational materials exist.

---

## Relationship to Other Registry Documentation

The Rules page should remain consistent with:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Entry Model;
- Registry Records;
- Registry Record Types;
- Registry Schemas;
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

When Registry Rules change:

- update the public `index.html`;
- update this README;
- review all Registry Policies;
- review all Registry Procedures;
- review the SREG Base Schema;
- review affected Record-Type Profiles;
- review lifecycle and status documentation;
- review examples;
- document material changes in the Registry Changelog;
- preserve the prior rule version;
- identify affected operational SREGs;
- reconcile human-readable and machine-readable documentation.

---

## Guiding Principles

- Registry governs the SREG.
- Source Institutions govern Source Records.
- The SREG must not replace the source.
- Registry and source identifiers remain distinct.
- Registry and source statuses remain distinct.
- Registry and source lifecycles remain distinct.
- Versions remain independently traceable.
- Every SREG has one primary Record Type.
- Relationships are typed and attributable.
- Provenance is preserved.
- Official forms agree.
- History remains discoverable.
- Deletion is exceptional.
- Registration does not create authority.

---

## Disclaimer

Registry Rules govern Registry-owned SREGs and Registry-controlled operations.

They do not create:

- Source Institution authority;
- certification;
- attestation;
- verification;
- ownership;
- legal rights;
- governmental recognition;
- regulatory approval;
- endorsement;
- affiliation;
- truth.

Those remain controlled by the applicable Source Institution, Source Record, rights holder, governing authority, or external system.

---

## Guiding Statement

> Preserve source authority.
>
> Preserve Registry identity.
>
> Preserve history.
>
> Publish consistently.
