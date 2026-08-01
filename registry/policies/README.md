# Registry Policies

## Overview

The `registry/policies/` directory contains the institutional policy documents that govern how Satoshium Registry creates, updates, corrects, retires, preserves, and maintains Satoshium Registry Entries, or SREGs.

This directory does not require an `index.html` file.

Its primary institutional artifact is this `README.md`, supported by individual policy documents.

Registry Policies define binding institutional requirements for Registry operations. They translate Registry Rules and Suite-wide expectations into governed implementation requirements that Registry Procedures can execute.

---

## Constitutional Position

Registry Policies operate within the Satoshium Suite hierarchy:

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
Operational SREG Actions
```

### Suite Standards

Define shared expectations across the Suite.

### Suite Methodology

Defines repeatable implementation principles.

### Suite Interoperability

Defines how institutions exchange records, identifiers, references, and relationships while preserving authority boundaries.

### Registry Rules

Establish foundational Registry requirements and institutional constraints.

### Registry Policies

Define binding operational requirements for specific Registry activities.

### Registry Procedures

Define the repeatable steps used to carry out those policies.

---

## Purpose

Registry Policies exist to answer questions such as:

- Under what conditions may a SREG be created?
- What information must be present before registration?
- When may a SREG be updated?
- What constitutes a correction?
- When should a SREG be superseded, revoked, retired, or archived?
- How must versions and prior states be preserved?
- How should Source Record changes be reflected?
- Which Registry actions require documentation or review?
- How is publication consistency maintained?
- How are authority boundaries preserved?

Policies establish consistent institutional requirements for answering these questions.

---

## Policy Authority

Registry Policies govern Registry-owned actions and Registry-owned information.

They may govern:

- Registry Identifier assignment;
- Registry Record Type assignment;
- registrability;
- SREG creation;
- Registry Status;
- Registry Lifecycle State;
- SREG versions;
- Registry corrections;
- Registry relationships;
- Registry publication;
- supersession;
- revocation;
- archival;
- preservation;
- policy review and amendment.

Registry Policies do not authorize Registry to control:

- Source Record content;
- Source-System Identifiers;
- Certification Outcomes;
- Certification Status;
- attestation conclusions;
- historical event meaning;
- integrity references;
- jurisdiction intelligence;
- workflow definitions;
- ownership or legal rights.

Those remain under the applicable Source Institution or external authority.

---

## Current Directory Structure

```text
registry/
└── policies/
    ├── README.md
    ├── correction-policy.md
    ├── record-creation-policy.md
    ├── record-retirement-policy.md
    └── record-update-policy.md
```

No `index.html` file is required for this directory.

The README serves as the primary explanation of policy scope, authority, hierarchy, and maintenance.

---

## Current Policy Documents

### `record-creation-policy.md`

Defines the institutional requirements for creating a new SREG.

It should address:

- Source Institution identification;
- Authoritative Source Record identification;
- registrability;
- Record Type selection;
- Registry Identifier assignment;
- required references;
- required relationships;
- schema validation;
- Registry Status;
- initial Lifecycle State;
- publication requirements;
- human-readable and machine-readable consistency.

### `record-update-policy.md`

Defines when and how an existing SREG may be updated.

It should distinguish among:

- Registry-owned metadata update;
- source-reported change;
- relationship update;
- reference repair;
- schema migration;
- Record Type refinement;
- material correction;
- version change.

It should require preservation of prior versions where applicable.

### `correction-policy.md`

Defines how Registry-owned errors are corrected.

It should address:

- correction authority;
- correction classes;
- minor and material corrections;
- version impact;
- correction records;
- publication consistency;
- source authority boundaries;
- correction history;
- relationship to supersession, revocation, and archival.

### `record-retirement-policy.md`

Defines how a SREG leaves active operational use.

It should distinguish among:

- supersession;
- revocation;
- retirement;
- archival;
- source removal;
- source retirement;
- institutional discontinuation.

It should preserve identity, provenance, versions, references, and historical discoverability.

---

## Policy and Procedure Distinction

Policy and procedure are not interchangeable.

```text
Policy
  = what Registry requires and under what conditions

Procedure
  = how Registry performs the required action
```

Example:

```text
Policy:
A material correction must preserve the prior SREG version.

Procedure:
Create a correction record, assign the replacement version,
validate all official forms, and publish the updated SREG.
```

Policies define institutional obligation.

Procedures define operational execution.

---

## Policy and Rule Distinction

Registry Rules and Registry Policies also remain distinct.

```text
Rules define foundational expectations.
Policies define binding implementation requirements.
Procedures define repeatable actions.
Schemas define structural validation.
```

A policy must not contradict a Registry Rule or Suite Standard.

A procedure must not contradict the policy it implements.

---

## Policy Objectives

Registry Policies should support the following objectives.

### Consistency

Similar Registry actions should be governed by similar requirements.

### Transparency

Material actions should be understandable, attributable, and traceable.

### Continuity

Prior Registry identity, versions, source references, and relationships should remain preserved.

### Discoverability

Policy implementation should support long-term public usability of Registry records.

### Authority Preservation

Registry actions must not absorb or redefine Source Institution authority.

### Interoperability

Policies should remain compatible with Suite-wide identifiers, schemas, relationships, and institutional objects.

### Validation

Policy requirements should be enforceable through review, schema validation, or procedural controls where practical.

### Preservation

Superseded, revoked, retired, and archived records should remain historically understandable.

---

## General Policy Requirements

Every Registry Policy should identify:

- policy title;
- policy purpose;
- policy scope;
- governing authority;
- applicable Registry objects;
- definitions;
- mandatory requirements;
- prohibited actions;
- exceptions, if any;
- documentation requirements;
- version requirements;
- review requirements;
- publication requirements;
- related procedures;
- related schemas;
- effective date;
- policy version;
- amendment history.

---

## Policy Status

Each policy should clearly identify its status.

Suggested policy statuses include:

- Draft;
- Under Review;
- Approved;
- Active;
- Superseded;
- Retired;
- Archived.

Policy Status applies to the policy document.

It must not be confused with:

- Registry Status;
- SREG Lifecycle State;
- Source-Record Status;
- Certification Status;
- workflow status.

---

## Policy Versioning

Registry Policies should use explicit versions.

A policy version should change when:

- a material requirement changes;
- policy scope changes;
- institutional authority changes;
- required documentation changes;
- a new exception is introduced;
- a procedure dependency changes materially;
- a schema dependency changes materially.

Minor editorial changes may be documented without changing substantive policy meaning, according to the applicable governance convention.

Prior policy versions should remain preserved when they governed historical Registry actions.

---

## Policy Review

Policies should be reviewed when:

- Suite Standards change;
- Suite Methodology changes;
- Suite Interoperability changes;
- Registry architecture changes;
- Record Types expand;
- schemas change materially;
- operational problems reveal ambiguity;
- a policy conflict is identified;
- a procedure can no longer implement the policy accurately;
- a Source Institution relationship changes materially.

Policy review should document:

- reason for review;
- reviewing authority;
- findings;
- required amendments;
- effective date;
- affected procedures;
- affected schemas;
- affected SREG operations.

---

## Policy Amendment

A policy amendment should preserve:

- prior policy version;
- amendment date;
- amendment reason;
- changed sections;
- approving authority;
- effective date;
- related procedure changes;
- related schema changes;
- transitional requirements;
- historical applicability.

Policy changes should not silently rewrite the requirements that governed earlier Registry actions.

---

## Policy Conflicts

When a policy conflicts with a higher authority, the higher authority governs.

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Rules
  ↓
Registry Policy
  ↓
Registry Procedure
```

A conflicting policy should be:

- identified;
- reviewed;
- corrected;
- versioned;
- documented;
- republished where applicable.

A procedure must not be used to bypass a policy conflict.

---

## Policy Enforcement

Policy enforcement may include:

- required review;
- schema validation;
- identifier validation;
- transition validation;
- publication checks;
- version checks;
- correction records;
- audit history;
- approval controls;
- automated validation;
- manual institutional review.

Not every policy requirement must be automated.

Every binding requirement should remain reviewable.

---

## Policy Exceptions

Exceptions should be rare and documented.

An approved exception should identify:

- applicable policy;
- affected SREG or Registry action;
- exception reason;
- approving authority;
- duration;
- conditions;
- risk;
- required follow-up;
- expiration or review date.

An exception should not permanently rewrite policy without formal amendment.

---

## Relationship to SREG Creation

The Record Creation Policy should ensure that an operational SREG is not published until Registry has:

- identified the Source Institution;
- identified the Authoritative Source Record;
- determined registrability;
- assigned the Record Type;
- assigned the Registry Identifier;
- preserved the Source-System Identifier when available;
- established required references;
- established required relationships;
- assigned Registry Status and Lifecycle State;
- validated the applicable schema;
- reconciled human-readable and machine-readable forms.

---

## Relationship to SREG Updates

The Record Update Policy should distinguish the reason for change.

Possible update causes include:

- Registry metadata improvement;
- corrected public reference;
- new relationship;
- source version change;
- source status change;
- schema migration;
- Record Type refinement;
- publication reconciliation;
- policy-driven update.

Every material update should preserve:

- prior SREG version;
- update reason;
- affected fields;
- source impact;
- replacement version;
- publication history.

---

## Relationship to Corrections

The Correction Policy should apply only to Registry-owned information and Registry-controlled publication.

Registry may correct:

- Registry metadata;
- Registry classification;
- Registry references;
- Registry relationships;
- Registry status;
- Registry lifecycle values;
- Registry publication inconsistencies.

Registry may not rewrite Source Record content.

A source-controlled error should be referred to or reflected from the Source Institution rather than silently corrected as though Registry owned it.

---

## Relationship to Retirement

The Record Retirement Policy should distinguish among:

### Supersession

The SREG or version has been replaced.

### Revocation

Registry has withdrawn the SREG from active recognition.

### Retirement

The SREG is no longer used operationally under the applicable policy.

### Archival

The SREG remains preserved outside active use.

Retirement policy should not equate removal from active use with deletion.

---

## Publication Consistency

Policy implementation should remain consistent across:

- Registry HTML pages;
- SREG JSON records;
- catalog indexes;
- relationship indexes;
- version history;
- correction history;
- supersession records;
- revocation records;
- archival records;
- interoperability references.

A policy action is incomplete when official Registry forms materially disagree.

---

## Policy Documentation

Each policy should link to or identify:

- related Registry Rule;
- related Registry Procedure;
- related schema;
- related definitions;
- related lifecycle state;
- related Registry Status;
- related Record Type;
- related correction or history records.

Policies should be understandable both independently and within the broader Registry architecture.

---

## Future Policy Areas

Future policy documents may include:

- identifier policy;
- classification policy;
- metadata policy;
- relationship policy;
- schema governance policy;
- lifecycle transition policy;
- publication policy;
- preservation policy;
- interoperability policy;
- external-source policy;
- attestation-reference policy;
- integrity-reference policy;
- historical-record policy;
- access and availability policy;
- policy governance policy.

Future additions should be created only when a genuine operational requirement exists.

---

## Repository Maintenance

When policy files are added or changed:

- update this README when the directory structure changes;
- preserve prior policy versions when historically applicable;
- update related procedures;
- update related schemas where required;
- document effective dates;
- document amendment history;
- reconcile public references;
- avoid leaving obsolete policy language in active procedures;
- confirm consistency with Suite Standards and Registry Rules.

---

## Disclaimer

Registry Policies govern Registry-owned institutional actions.

They do not by themselves create:

- Source Institution authority;
- ownership;
- certification;
- attestation;
- legal rights;
- regulatory approval;
- verification;
- endorsement;
- affiliation.

Those forms of authority remain with the applicable Source Institution, rights holder, governing authority, or responsible external system.

---

## Policy Philosophy

Policies should create enough structure to preserve consistency, accountability, authority boundaries, and long-term continuity without introducing unnecessary complexity.

Policies should be:

- clear;
- bounded;
- reviewable;
- versioned;
- enforceable;
- adaptable through governance;
- subordinate to higher Suite authority.

---

## Guiding Statement

> Rules define expectations.
>
> Policies define binding requirements.
>
> Procedures define repeatable actions.
>
> Schemas validate structure.
>
> Registry preserves the result.
