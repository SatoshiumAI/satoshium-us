# Registry Record Update Policy

## Policy Status

**Policy Name:** Registry Record Update Policy  
**Policy Type:** Institutional Registry Policy  
**Applies To:** Existing Satoshium Registry Entries (SREGs)  
**Initial Policy Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-08-01  

---

## Purpose

This policy establishes the binding institutional requirements for updating an existing Satoshium Registry Entry, or SREG.

The purpose of an update is to improve or maintain the current Registry representation of an Authoritative Source Record while preserving:

- Registry identity;
- Source Institution authority;
- prior SREG versions;
- status and lifecycle history;
- source references;
- relationships;
- publication consistency;
- long-term discoverability;
- historical continuity.

An update changes an existing SREG.

It does not silently create a new Registry identity or erase the prior one.

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
Registry Record Update Policy
  ↓
Registry Record Update Procedure
  ↓
Replacement SREG Version
```

This policy is subordinate to applicable Suite Standards and Registry Rules.

The corresponding Record Update Procedure defines the repeatable operational steps required to implement this policy.

---

## Policy Statement

Registry may update an existing SREG when:

- new Registry-owned information becomes available;
- source-reported information changes;
- public references change;
- relationships evolve;
- status or lifecycle information changes;
- a schema migration is required;
- a Record-Type Profile changes;
- interoperability requirements change;
- expanded context improves the Registry record;
- publication forms require reconciliation.

Updates must be:

- authorized;
- attributable;
- documented;
- version-aware;
- schema-valid;
- consistent across official forms;
- limited to Registry authority;
- historically preserved.

Registry must not use an update to conceal a correction, avoid supersession, replace a Source Record, or erase prior versions.

---

## Scope

This policy applies to updates involving:

- Registry-owned metadata;
- Source Institution references;
- Source-System Identifier references;
- Source-Record version references;
- Source-Record status references;
- Registry Record Type;
- secondary classification;
- Registry Status;
- Registry Lifecycle State;
- Registry relationships;
- public references;
- version metadata;
- descriptive context;
- schema migration;
- profile migration;
- human-readable Registry pages;
- machine-readable SREG records;
- Registry indexes;
- Registry manifests;
- interoperability mappings.

---

## Outside Scope

This policy does not authorize Registry to:

- alter the Authoritative Source Record;
- change a Source-System Identifier at the source;
- change a Certification Outcome;
- change Certification Status;
- alter an attestation conclusion;
- reinterpret a Chronicle event;
- modify an Anchor integrity reference;
- redefine Atlas jurisdiction intelligence;
- rewrite a Navigator workflow;
- control ownership, licensing, or legal rights;
- use an update to create a materially different Source Record under the same SREG identity.

When the underlying issue is an error in Registry-owned information, the Registry Correction Policy applies.

When the existing SREG should leave active use, the Registry Record Retirement Policy applies.

---

## Update Authority

Registry may update Registry-owned information and Registry's representation of source-controlled information.

Update authority includes:

- adding or revising Registry metadata;
- adding or revising public references;
- adding or revising Registry relationships;
- reflecting a new Source-Record version;
- reflecting a new Source-Record status;
- updating Registry Status;
- updating Registry Lifecycle State;
- migrating a SREG to a newer schema;
- applying a newer Record-Type Profile;
- reconciling official publication forms.

Registry may report a source-controlled change.

Registry may not create that source-controlled change.

---

## Guiding Principles

### Accuracy

Updates should improve the accuracy and current usefulness of the SREG.

### Transparency

Material updates should be understandable and traceable.

### Continuity

The Registry Identifier and prior versions should remain preserved.

### Consistency

All official forms of the same SREG should reflect the update consistently.

### Preservation

Important prior information should not be removed without documented reason.

### Authority Separation

Registry must preserve the distinction between Registry-owned and source-controlled information.

### Proportionality

Documentation and review should correspond to the significance of the update.

### Interoperability

Updates should preserve valid identifiers, relationships, versions, and cross-institution references.

---

## Reasons for Updates

A SREG may be updated because of:

- new Registry metadata;
- improved descriptive context;
- new public references;
- repaired public references;
- new relationships;
- changed relationship targets;
- Source-Record version change;
- Source-Record status change;
- Source Institution publication change;
- Registry Status change;
- Registry Lifecycle transition;
- schema migration;
- Record-Type Profile migration;
- classification refinement;
- interoperability improvement;
- publication reconciliation;
- policy or procedure change;
- another documented operational reason.

The reason for update must be preserved.

---

## Update Types

### Metadata Update

Addresses Registry-owned descriptive information such as:

- title;
- dates;
- display labels;
- publication metadata;
- non-source-controlled description;
- catalog metadata.

### Source-Reference Update

Reflects a change in Registry's reference to source-controlled information, including:

- Source Institution;
- Source-System Identifier;
- source URL;
- Source-Record version;
- Source-Record status;
- source publication location.

A Source-Reference Update does not alter the Source Record.

### Reference Update

Adds, removes, repairs, or revises:

- canonical URLs;
- repository paths;
- machine-readable locations;
- public pages;
- archival locations;
- related institutional references.

### Relationship Update

Adds, removes, repairs, or revises typed relationships.

Examples include:

- references;
- related to;
- certified by;
- attested by;
- anchored by;
- documented by;
- discovered through;
- supersedes;
- superseded by;
- part of;
- coordinated through.

### Classification Update

Changes:

- Registry Record Type;
- secondary classification;
- taxonomy placement;
- hierarchy placement;
- Record-Type Profile assignment.

Classification updates may be material because they can affect validation, discovery, and interpretation.

### Status Update

Changes Registry Status or reflects a changed Source-Record Status.

The two must remain separate.

### Lifecycle Update

Reflects a permitted Registry Lifecycle transition.

Lifecycle updates must comply with Registry Lifecycle policy and transition rules.

### Schema Migration

Moves a SREG from one schema version to another.

Schema migration must preserve the prior version and should not imply that the Source Record changed.

### Profile Migration

Moves a SREG to a newer Record-Type Profile.

Profile migration must preserve the profile version previously used.

### Contextual Update

Adds explanatory or descriptive context without changing the identity or authority of the Source Record.

### Publication Reconciliation

Corrects disagreement among official forms where the underlying values are already known and no substantive Registry error remains.

If the disagreement resulted from an error, the Correction Policy may also apply.

---

## Update Versus Correction

Update and correction are not interchangeable.

### Update

Reflects new, changed, expanded, or newly available information.

### Correction

Repairs an error in Registry-owned information or Registry-controlled publication.

Examples:

```text
Source Record publishes Version 2.0
  = Update
```

```text
Registry incorrectly recorded Source Record Version 1.0
  = Correction
```

```text
A new relationship becomes relevant
  = Update
```

```text
Registry linked the wrong relationship target
  = Correction
```

A single action may involve both an update and a correction, but the two reasons must remain distinguishable.

---

## Update Versus Creation

An existing SREG should normally be updated when:

- the same Authoritative Source Record changes;
- Registry metadata improves;
- references change;
- relationships evolve;
- source status changes;
- source version changes;
- schema migration occurs.

A new SREG should be created when:

- a distinct Authoritative Source Record exists;
- a separate Registry identity is required;
- the new object has independent institutional meaning;
- the existing SREG cannot accurately represent the new source object.

Update must not be used to collapse two distinct Source Records into one SREG.

---

## Update Versus Supersession

An update preserves the same Registry identity.

Supersession replaces the current SREG or version with a successor.

Supersession may be required when:

- identity changes materially;
- the Source Record is replaced by a distinct successor;
- the original classification is fundamentally incompatible;
- a new Registry Identifier is required;
- architectural restructuring creates a distinct object.

A material change should not be treated as a routine update merely to avoid supersession history.

---

## Update Workflow

Registry updates must follow the approved workflow:

```text
Update Need Identified
  ↓
Authority and Update Type Determined
  ↓
Impact Reviewed
  ↓
Source and Registry Changes Distinguished
  ↓
Update Prepared
  ↓
Schema and Relationship Validation
  ↓
Replacement Version Assigned
  ↓
Update Record Created
  ↓
Official Forms Reconciled
  ↓
Update Published
  ↓
Prior Version Preserved
```

---

## Update Need Identification

An update need may be identified through:

- Source Institution notice;
- Registry review;
- Source Record version change;
- Source Record status change;
- public-reference monitoring;
- interoperability review;
- schema migration;
- relationship review;
- lifecycle review;
- user report;
- repository review;
- policy change.

Identification does not itself authorize publication.

---

## Authority and Update-Type Determination

Before updating a SREG, Registry must determine:

- whether the change is Registry-owned or source-controlled;
- whether the action is an update or correction;
- whether the action requires supersession;
- whether the action triggers lifecycle change;
- whether a new Registry Entry Version is required;
- whether Source Institution coordination is required;
- whether legal, privacy, rights, or access restrictions apply.

Unresolved authority questions should prevent publication.

---

## Impact Review

Registry should evaluate whether the update affects:

- Registry identity;
- Source Institution attribution;
- Source-System Identifier;
- Authoritative Source Record;
- Record Type;
- classification;
- Registry Status;
- Registry Lifecycle State;
- Source-Record Status;
- versions;
- relationships;
- public references;
- schema validation;
- interoperability;
- public interpretation;
- historical continuity.

The impact review determines whether the update is minor or material.

---

## Minor Updates

Minor updates may include:

- non-substantive wording improvements;
- added explanatory context;
- repaired link targets;
- non-material metadata additions;
- accessibility improvements;
- formatting improvements;
- additional public references that do not change meaning.

Minor updates may use simplified documentation when:

- identity does not change;
- Source Institution does not change;
- Record Type does not change;
- Registry Status does not change;
- Lifecycle State does not change;
- core relationships do not change;
- source authority does not change;
- institutional meaning does not change.

Even minor updates must remain consistent across affected official forms.

---

## Material Updates

An update is material when it changes or may change:

- interpretation of the SREG;
- Source Institution attribution;
- Source-System Identifier reference;
- Authoritative Source Record;
- Record Type;
- classification;
- Registry Status;
- Lifecycle State;
- Source-Record Status;
- core relationships;
- version history;
- public discoverability;
- interoperability behavior;
- machine-readable validation result.

Material updates require a formal Update Record and normally require a new Registry Entry Version.

---

## Version Requirements

Every material update must preserve version distinctions.

Registry should distinguish among:

- Registry Entry Version;
- SREG schema version;
- Record-Type Profile version;
- Registry specification version;
- Source-Record version;
- Source Institution publication version;
- applicable Suite Standards version;
- applicable Suite Methodology version.

A material update should normally follow:

```text
Prior SREG Version
  ↓
Update Record
  ↓
Replacement SREG Version
```

A Source-Record version change must not be confused with a Registry Entry Version change.

---

## Update Record Requirements

A formal Update Record should contain:

- update identifier;
- Registry Identifier;
- affected SREG version;
- update type;
- update reason;
- authority determination;
- changed fields;
- prior values;
- replacement values;
- Source Record impact;
- Source-Record version impact;
- Source-Record status impact;
- Registry Status impact;
- Lifecycle impact;
- schema impact;
- relationship impact;
- update date;
- responsible Registry action;
- replacement SREG version;
- review or approval information;
- publication locations;
- related correction, supersession, revocation, or archival records.

---

## Source-Driven Updates

When the Source Institution changes the Authoritative Source Record, Registry may update the SREG to reflect:

- new source version;
- new Source-Record Status;
- new canonical source URL;
- new source publication date;
- changed Source-System Identifier context;
- successor Source Record;
- new public references;
- source retirement or revocation.

Registry should preserve:

- prior source reference;
- prior source version;
- prior source status;
- date of source change;
- date Registry reflected the change;
- resulting SREG version;
- resulting lifecycle or status impact.

---

## Registry-Driven Updates

Registry may initiate an update when:

- Registry metadata improves;
- new relationships are established;
- public references expand;
- schema migration is required;
- Record-Type Profile changes;
- catalog presentation changes;
- lifecycle or status changes;
- interoperability mappings expand.

Registry-driven updates must not imply that the Source Record changed when it did not.

---

## Status Updates

Registry Status updates must use approved values.

A status update should preserve:

- prior Registry Status;
- new Registry Status;
- reason;
- effective date;
- affected SREG version;
- related lifecycle event;
- Source-Record Status;
- publication impact.

Registry Status and Source-Record Status must remain separate.

---

## Lifecycle Updates

Lifecycle updates must comply with Registry Lifecycle transition rules.

Possible patterns include:

```text
Active
  ↓
Updated
  ↓
Active
```

```text
Active
  ↓
Superseded
```

```text
Active
  ↓
Revoked
```

An update may trigger a lifecycle transition, but not every update requires one.

---

## Relationship Updates

A relationship update must preserve:

- relationship type;
- relationship direction;
- relationship target;
- target identifier;
- target institution;
- effective date;
- prior relationship where replaced;
- reason for addition, removal, or change.

Historical relationships should remain preserved when they continue to matter.

---

## Reference Updates

A reference update should distinguish among:

- new reference;
- replacement reference;
- repaired reference;
- archival reference;
- historical reference;
- removed reference;
- source-controlled reference;
- Registry-controlled reference.

When a canonical source location changes, the prior location should be preserved where practical.

---

## Classification Updates

A classification update should preserve:

- prior Record Type;
- new Record Type;
- prior profile version;
- new profile version;
- reason;
- schema impact;
- relationship impact;
- discovery impact;
- effective date;
- replacement SREG version.

A fundamental classification change may require supersession rather than routine update.

---

## Schema Migration

Schema migration should preserve:

- prior schema version;
- new schema version;
- migration date;
- migration reason;
- affected fields;
- transformation rules;
- validation result;
- prior SREG version;
- replacement SREG version.

Schema migration must not erase the structure under which the prior SREG version was published.

---

## Publication Requirements

A material update must be reflected consistently across:

- human-readable Registry Entry pages;
- machine-readable SREG records;
- catalog indexes;
- relationship indexes;
- version history;
- update history;
- correction history;
- supersession records;
- revocation records;
- archival records;
- interoperability references;
- repository manifests.

An update is incomplete when official Registry forms materially disagree.

---

## Human-Readable Disclosure

A material update should be understandable to a public reader.

Human-readable disclosure may include:

- update date;
- update summary;
- affected version;
- replacement version;
- update reason;
- Source Record impact;
- status or lifecycle impact;
- related Update Record;
- prior-version reference.

Minor updates may be represented through concise change history.

---

## Machine-Readable Disclosure

A machine-readable Update Record may include:

- update identifier;
- affected Registry Identifier;
- affected version;
- replacement version;
- update type;
- reason;
- changed fields;
- prior values;
- replacement values;
- timestamps;
- Source Record impact;
- status impact;
- lifecycle impact;
- schema impact;
- relationship impact;
- related records;
- schema version.

Machine-readable disclosure should follow the applicable update-record schema.

---

## Validation Requirements

Before publication, Registry should validate that:

- update authority is established;
- the update type is accurate;
- required documentation exists;
- affected versions are identified;
- replacement version is valid;
- Registry and source fields remain distinct;
- required references remain available;
- relationships remain structurally valid;
- status and lifecycle transitions are permitted;
- applicable schemas validate;
- official forms agree;
- update history is linked;
- prior material versions remain preserved.

---

## Source Institution Coordination

Registry should coordinate with the Source Institution when an update materially affects:

- Source Institution attribution;
- Source-System Identifier;
- source reference;
- Source-Record version;
- Source-Record Status;
- interoperability relationship;
- public interpretation of source-controlled information.

Coordination does not transfer update authority.

---

## Prohibited Update Practices

Registry must not:

- silently overwrite a material prior version;
- alter Source Record content;
- invent a Source-System Identifier;
- collapse Registry Identifier and Source-System Identifier;
- collapse Registry Status and Source-Record Status;
- use update to conceal a correction;
- use update to conceal supersession or revocation;
- create a distinct Source Record under an existing SREG identity;
- publish inconsistent HTML and JSON values;
- remove material history solely for convenience;
- backdate an update without documented reason;
- use an update to imply certification, attestation, endorsement, ownership, or legal recognition.

---

## Review and Approval

The level of review required should correspond to:

- update type;
- materiality;
- Source Institution impact;
- Record Type;
- schema impact;
- relationship impact;
- lifecycle impact;
- status impact;
- interoperability impact;
- public interpretation;
- legal or rights concerns.

The reviewing role and approval requirements should be defined by Registry Procedure.

---

## Policy Exceptions

Exceptions must be documented.

An exception should identify:

- affected SREG;
- applicable policy requirement;
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

- Registry Record Creation Policy;
- Registry Correction Policy;
- Registry Record Retirement Policy;
- Registry Lifecycle;
- Registry Status;
- Registry Schemas;
- Registry Entry Model;
- Registry Integration;
- Registry Procedures.

When policies overlap:

- Creation Policy governs new SREG creation.
- Update Policy governs non-correction changes to an existing SREG.
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
- profile architecture changes;
- update failures reveal ambiguity;
- publication formats change;
- interoperability requirements change;
- lifecycle or status values change;
- source integration patterns change.

Prior policy versions should remain preserved.

---

## Policy Summary

A compliant update should make clear:

- which SREG changed;
- why it changed;
- whether the change came from Registry or the Source Institution;
- which fields changed;
- which version was affected;
- which version replaced it;
- whether status or lifecycle changed;
- whether relationships or references changed;
- how official forms were reconciled;
- how prior history remains discoverable.

The objective is not simply to change the record.

The objective is to improve or maintain the SREG while preserving identity, authority, versions, and continuity.

---

## Disclaimer

This policy governs updates to Registry-owned SREGs.

It does not authorize Registry to alter:

- Source Record content;
- certification decisions;
- attestation conclusions;
- external legal records;
- ownership;
- licensing;
- regulatory determinations;
- Source Institution authority.

Those remain controlled by the applicable Source Institution or external authority.

---

## Guiding Statement

> Information changes.
>
> Registry reflects the change.
>
> Identity remains stable.
>
> Prior versions remain preserved.
>
> Authority remains at the source.
