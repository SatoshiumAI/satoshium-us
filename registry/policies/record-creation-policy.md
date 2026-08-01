# Registry Record Creation Policy

## Policy Status

**Policy Name:** Registry Record Creation Policy  
**Policy Type:** Institutional Registry Policy  
**Applies To:** Proposed Satoshium Registry Entries (SREGs)  
**Initial Policy Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-08-01  

---

## Purpose

This policy establishes the binding institutional requirements for creating a new Satoshium Registry Entry, or SREG.

The purpose of record creation is to ensure that every operational Registry Entry is:

- registrable;
- attributable to an identifiable Source Institution;
- linked to an Authoritative Source Record;
- assigned an approved Registry Record Type;
- assigned a unique Registry Identifier;
- structurally valid;
- version-aware;
- relationship-aware;
- publicly discoverable;
- consistent across human-readable and machine-readable forms.

Registry creates the SREG.

The Source Institution retains authority over the Source Record.

---

## Constitutional Position

This policy operates within the Satoshium Suite hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Rules
  ↓
Registry Record Creation Policy
  ↓
Registry Record Creation Procedure
  ↓
Published SREG
```

This policy is subordinate to applicable Suite Standards and Registry Rules.

The corresponding Record Creation Procedure defines the repeatable operational steps required to implement this policy.

---

## Policy Statement

Registry may create a SREG only when:

- an Authoritative Source Record can be identified;
- the Source Institution can be identified;
- the proposed object is registrable;
- an approved Registry Record Type applies;
- the required source and public references are available;
- the SREG can satisfy the applicable schema and profile;
- Registry can preserve the separation between Registry authority and Source Institution authority;
- publication can be completed consistently.

A Registry Entry must not be created merely because information exists.

The information must be appropriate for structured Registry cataloging.

---

## Scope

This policy applies to the creation of new SREGs for approved Record Types, including:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal;
- other approved Registry Record Types.

It also applies to:

- Registry Identifier assignment;
- Source Institution identification;
- Source-System Identifier preservation;
- Record Type assignment;
- initial Registry Status;
- initial Registry Lifecycle State;
- initial SREG version;
- required relationships;
- required public references;
- schema validation;
- initial publication.

---

## Outside Scope

This policy does not authorize Registry to:

- create or alter Source Records;
- certify a subject;
- create an attestation;
- establish legal or governmental authority;
- create historical truth;
- issue an integrity reference;
- define a workflow for another institution;
- replace a Source-System Identifier;
- claim ownership over external content;
- create a SREG where no identifiable Source Record exists.

The originating institution remains authoritative for the Source Record.

---

## Registrability

A proposed record is registrable when it satisfies all applicable Registry requirements.

Registrability should consider:

- identifiable Source Institution;
- identifiable Authoritative Source Record;
- sufficient provenance;
- suitable Registry Record Type;
- adequate public or institutional references;
- clear institutional relevance;
- support for long-term discoverability;
- compatibility with the SREG model;
- applicable schema support;
- absence of unresolved authority conflicts.

Registrability is a Registry determination.

It is not certification, endorsement, attestation, or legal recognition.

---

## Eligible Registry Record Types

A SREG may be created only under an approved Registry Record Type.

Initial Record Types may include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Future Record Types may be introduced through documented Registry governance.

A new Record Type should not be improvised during individual record creation.

---

## Source Institution Requirement

Every operational SREG must identify the Source Institution responsible for the Authoritative Source Record.

The Source Institution may be:

- Atlas;
- Certifier;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- another approved Satoshium Suite institution;
- an approved external institution or source.

The Source Institution must remain distinguishable from Satoshium Registry.

---

## Authoritative Source Record Requirement

Every operational SREG must identify the Authoritative Source Record being cataloged.

The Source Record should be:

- identifiable;
- attributable;
- referenceable;
- sufficiently stable for cataloging;
- capable of supporting provenance;
- distinct from the SREG.

Registry must not create a SREG that silently becomes a substitute for a missing Source Record.

---

## Registry Identifier Requirement

Every SREG must receive a unique Registry Identifier.

The Registry Identifier:

- identifies the SREG;
- is assigned by Registry;
- must remain stable;
- must not be reused;
- must remain distinct from the Source-System Identifier;
- must remain discoverable after update, supersession, revocation, or archival.

The Registry Identifier must not be used to imply source ownership or source authority.

---

## Source-System Identifier Requirement

When the Source Record has its own identifier, the SREG must preserve it.

The Source-System Identifier:

- identifies the Authoritative Source Record;
- is controlled by the Source Institution;
- must remain distinct from the Registry Identifier;
- should be preserved exactly where practical;
- should include its source context;
- should not be rewritten by Registry.

If no Source-System Identifier exists, the absence should be documented rather than replaced with an invented source identifier.

---

## Required SREG Elements

Every operational SREG should include, at minimum:

### Identity

- Registry Identifier;
- title;
- Registry Record Type.

### Source Attribution

- Source Institution;
- Authoritative Source Record;
- Source-System Identifier, when available;
- canonical source reference.

### Status and Lifecycle

- Registry Status;
- Registry Lifecycle State;
- Source-Record Status, when available.

### Versions

- Registry Entry Version;
- SREG schema version;
- Record-Type Profile version;
- Source-Record version, when available.

### References and Relationships

- public references;
- required typed relationships;
- related institutional objects where applicable.

### Dates

- registration date;
- last updated date.

### Publication

- human-readable publication location;
- machine-readable publication location;
- publication consistency confirmation.

---

## Record Type Assignment

Each SREG must receive one primary Registry Record Type.

The selected Record Type must:

- accurately reflect the Source Record;
- correspond to an approved Record-Type Profile;
- support the required metadata;
- support the required relationships;
- support schema validation;
- support public discoverability.

Secondary classifications may be permitted when defined by the applicable profile.

A SREG must not receive multiple conflicting primary Record Types.

---

## Initial Registry Status

Every new SREG must receive an initial Registry Status defined by the Registry Status framework.

Possible initial designations may include:

- Pending;
- Registered;
- Active;
- Under Review;
- another approved status.

Status values must not be improvised.

The initial Registry Status must remain distinct from the Source-Record Status.

---

## Initial Lifecycle State

Every new SREG must receive an initial Registry Lifecycle State.

A typical path may include:

```text
Pending Registration
  ↓
Registered
  ↓
Active
```

The selected state must reflect the actual institutional condition of the SREG.

Lifecycle State must remain distinct from Registry Status.

---

## Initial Version

Every newly created SREG must receive an initial Registry Entry Version.

The version should identify the first operational publication of the SREG.

Versioning must remain distinct from:

- Source-Record version;
- schema version;
- Record-Type Profile version;
- Registry specification version;
- Suite Standards version.

---

## Relationship Requirements

When applicable, a new SREG should preserve typed relationships such as:

- references;
- derived from;
- certified by;
- attested by;
- anchored by;
- discovered through;
- documented by;
- coordinated through;
- part of;
- related to.

Relationships must:

- use approved relationship types;
- identify valid targets;
- preserve direction where applicable;
- remain machine-readable;
- remain consistent across official publications.

---

## Public Reference Requirements

A new SREG should preserve durable public or institutional references, including where applicable:

- canonical Source Record URL;
- repository path;
- machine-readable source record;
- public institutional page;
- Registry HTML entry;
- Registry JSON entry;
- integrity reference;
- certification package;
- attestation;
- historical event;
- discovery signal;
- workflow definition.

Broken or unverified references should not be treated as authoritative.

---

## Metadata Requirements

Metadata must be sufficient to support:

- identification;
- classification;
- source attribution;
- discovery;
- interpretation;
- relationship mapping;
- lifecycle management;
- version tracking;
- correction history;
- archival continuity.

Metadata requirements should follow the SREG Base Schema and applicable Record-Type Profile.

---

## Schema Requirements

Every new SREG must conform to the Registry schema hierarchy:

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

A SREG should not be published when:

- required fields are missing;
- field types are invalid;
- enumerated values are unapproved;
- required relationships are missing;
- identifiers are malformed;
- version fields are inconsistent;
- human-readable and machine-readable forms disagree materially.

---

## Record Creation Workflow

Registry record creation must follow the approved workflow:

```text
Need Identified
  ↓
Source Institution Confirmed
  ↓
Authoritative Source Record Confirmed
  ↓
Registrability Determined
  ↓
Record Type Assigned
  ↓
Registry Identifier Assigned
  ↓
References and Relationships Established
  ↓
SREG Constructed
  ↓
Schema Validated
  ↓
Status and Lifecycle Assigned
  ↓
Human-Readable and Machine-Readable Forms Reconciled
  ↓
Published
  ↓
Creation History Preserved
```

---

## Need Identification

A creation request may arise through:

- institutional handoff;
- approved public source;
- Registry review;
- Navigator workflow;
- repository publication;
- Suite interoperability need;
- preservation need;
- public discoverability need.

Need identification does not itself authorize SREG creation.

---

## Authority Review

Before creation, Registry must determine:

- who owns the Source Record;
- which institution controls source meaning;
- whether Registry has authority to catalog the Source Record;
- whether any licensing, privacy, access, or legal restriction prevents publication;
- whether the record belongs in Registry.

Unresolved authority questions should prevent publication.

---

## Classification Review

Registry must confirm:

- the primary Record Type;
- applicable secondary classifications;
- applicable Record-Type Profile;
- required fields;
- required relationships;
- required source references;
- applicable lifecycle and status values.

Classification should occur before final SREG construction.

---

## Validation Review

Before publication, Registry should confirm:

- Source Institution is identified;
- Source Record exists;
- Source-System Identifier is preserved when available;
- Registry Identifier is valid;
- Record Type is approved;
- required metadata is complete;
- required relationships are valid;
- references resolve or are historically documented;
- Registry Status is valid;
- Lifecycle State is valid;
- version metadata is complete;
- schema validation succeeds;
- human-readable and machine-readable forms agree.

---

## Publication Requirements

A new SREG should not be considered operationally published until required official forms are available.

Publication may include:

- human-readable Registry Entry page;
- machine-readable SREG JSON;
- catalog index entry;
- relationship index entry;
- version history;
- creation record;
- interoperability references.

A publication is incomplete when official forms materially disagree.

---

## Human-Readable Publication

The human-readable SREG should clearly communicate:

- Registry Identifier;
- title;
- Record Type;
- Source Institution;
- Authoritative Source Record;
- Registry Status;
- Source-Record Status;
- Lifecycle State;
- versions;
- public references;
- relationships;
- registration date.

---

## Machine-Readable Publication

The machine-readable SREG should preserve equivalent institutional meaning.

It should include:

- stable identifiers;
- controlled classifications;
- status values;
- lifecycle values;
- version metadata;
- source references;
- typed relationships;
- dates;
- schema version;
- validation metadata where applicable.

---

## Publication Consistency

The following values must agree across official forms:

- Registry Identifier;
- title;
- Record Type;
- Source Institution;
- Source-System Identifier;
- Source Record;
- Registry Status;
- Source-Record Status;
- Lifecycle State;
- versions;
- relationships;
- public references;
- registration date.

A SREG must not be published with unresolved material inconsistencies.

---

## Creation Record

Registry should preserve a Creation Record for each operational SREG.

The Creation Record may include:

- Registry Identifier;
- creation date;
- source of request;
- Source Institution;
- Authoritative Source Record;
- registrability determination;
- assigned Record Type;
- assigned initial status;
- assigned initial Lifecycle State;
- initial SREG version;
- schema version;
- validation result;
- responsible Registry action;
- publication locations;
- related approval or review.

---

## Duplicate Prevention

Before creating a new SREG, Registry should check for:

- an existing SREG for the same Source Record;
- duplicate Source-System Identifier;
- duplicate canonical source reference;
- overlapping identity;
- prior superseded or archived entries;
- related records that should be updated rather than duplicated.

When an existing SREG already catalogs the Source Record, Registry should normally apply the Record Update Policy instead of creating a duplicate.

---

## Creation Versus Update

A new SREG should be created when:

- a new Authoritative Source Record exists;
- a distinct Registry identity is required;
- a new Record Type applies to a distinct object;
- the existing SREG cannot accurately represent the new source object.

An existing SREG should be updated when:

- the same Source Record changes;
- Registry metadata improves;
- source status changes;
- relationships expand;
- references change;
- schema migration occurs.

Creation must not be used to avoid version or correction history.

---

## Creation Versus Supersession

A replacement SREG may be created when:

- identity changes materially;
- the original classification was fundamentally wrong;
- the new Source Record is distinct;
- the old SREG must remain preserved as superseded;
- a documented governance action requires a new Registry Identifier.

The relationship between the prior and replacement SREG must remain explicit.

---

## Prohibited Creation Practices

Registry must not:

- create a SREG without an identifiable Source Record;
- invent a Source Institution;
- invent a Source-System Identifier;
- reuse a Registry Identifier;
- collapse Registry Identifier and Source-System Identifier;
- publish conflicting official forms;
- assign an unapproved Record Type;
- omit required provenance;
- classify registration as certification;
- imply endorsement or ownership through registration;
- create duplicates to avoid updating an existing SREG;
- create a SREG that silently replaces the Source Record.

---

## Review and Approval

The level of review required should correspond to:

- Record Type;
- source complexity;
- authority sensitivity;
- publication impact;
- interoperability impact;
- legal or rights concerns;
- schema maturity;
- novelty of the source object.

The reviewing role and approval requirements should be defined by Registry Procedure.

---

## Policy Exceptions

Exceptions must be documented.

An exception should identify:

- proposed SREG;
- applicable requirement;
- reason;
- approving authority;
- duration;
- risk;
- mitigation;
- required follow-up;
- review or expiration date.

An exception does not permanently amend this policy.

---

## Relationship to Other Registry Policies

This policy works with:

- Registry Correction Policy;
- Registry Record Update Policy;
- Registry Record Retirement Policy;
- Registry Lifecycle;
- Registry Status;
- Registry Schemas;
- Registry Entry Model;
- Registry Integration;
- Registry Procedures.

When policies overlap:

- Creation Policy governs new SREG creation.
- Update Policy governs changes to an existing SREG.
- Correction Policy governs repair of Registry-owned errors.
- Retirement Policy governs removal from active use.
- Lifecycle governs state transitions.
- Status defines the current operational designation.

---

## Policy Review

This policy should be reviewed when:

- Suite Standards change;
- Registry Rules change;
- new Record Types are introduced;
- schemas change materially;
- identifier architecture changes;
- creation failures reveal ambiguity;
- duplicate records increase;
- interoperability requirements change;
- publication formats change;
- operational authority boundaries change.

Prior policy versions should remain preserved.

---

## Policy Summary

A new SREG may be created only when Registry can identify:

- what is being cataloged;
- who owns the Source Record;
- why the record is registrable;
- which Record Type applies;
- which Registry Identifier is assigned;
- which source identifier is preserved;
- which relationships and references are required;
- which versions apply;
- which status and lifecycle values apply;
- how the SREG will be validated and published.

The objective is not simply to record information.

The objective is to create a durable, attributable, structured, and discoverable Registry Entry.

---

## Disclaimer

This policy governs creation of Registry-owned SREGs.

It does not create:

- Source Institution authority;
- certification;
- attestation;
- ownership;
- legal rights;
- regulatory approval;
- verification;
- endorsement;
- affiliation.

Those forms of authority remain with the applicable Source Institution, rights holder, governing authority, or responsible external system.

---

## Guiding Statement

> Identify the source.
>
> Preserve its authority.
>
> Create the SREG.
>
> Validate the structure.
>
> Publish the path back to the record.
