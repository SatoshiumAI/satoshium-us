# Satoshium Registry Procedures

## Overview

The `registry/procedures/` directory contains the public institutional page and supporting documentation for the Satoshium Registry Procedures framework.

The public page is published through:

```text
registry/procedures/index.html
```

This `README.md` serves as the directory-level documentation for that page.

---

## Purpose of This Directory

The purpose of this directory is to define the repeatable operational methods used by Satoshium Registry to:

- receive or identify Source Records;
- review Source Authority;
- determine Registrability;
- review duplicates and conflicts;
- assign Registry Record Types;
- assign Registry Identifiers;
- construct SREGs;
- construct relationships;
- construct provenance;
- validate Registry records;
- publish official forms;
- process updates;
- issue corrections;
- assign versions;
- manage status and lifecycle transitions;
- supersede or revoke Registry records;
- restrict publication;
- preserve archival history;
- manage exceptions;
- review and revise procedures.

Procedures translate Registry Rules and Registry Policies into consistent, attributable, reviewable operational actions.

---

## Constitutional Position

Registry Procedures operate beneath Suite Standards, Suite Methodology, Registry Rules, and Registry Policies.

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Registry Rules
  ↓
Registry Policies
  ↓
Registry Procedures
  ↓
Operational Actions
```

Rules establish requirements.

Policies establish durable institutional decisions.

Procedures define how those decisions are carried out.

---

## Core Principle

```text
Policies establish durable decisions.
Procedures create repeatable action.
Records preserve accountability.
```

A Procedure should make a Registry operation reproducible without silently creating new authority or changing policy.

---

## Why Procedures Matter

Procedures reduce:

- inconsistent treatment;
- undocumented judgment;
- silent operational changes;
- dependence on individual memory;
- unclear responsibility;
- incomplete records;
- unreviewable exceptions;
- variation between human and automated workflows.

They help ensure that comparable cases receive comparable treatment.

---

## Canonical Registry Procedure

```text
Receive or Identify Source
  ↓
Confirm Source Authority
  ↓
Determine Registrability
  ↓
Assign Record Type
  ↓
Assign Registry Identifier
  ↓
Construct SREG
  ↓
Validate
  ↓
Publish
  ↓
Maintain History
```

This sequence defines the standard operational path from candidate source to maintained Registry Entry.

---

## Core Procedure Domains

The Registry Procedures framework includes:

- Source Intake Procedure;
- Source Authority Review Procedure;
- Registrability Review Procedure;
- Duplicate and Conflict Review Procedure;
- Record-Type Assignment Procedure;
- Registry Identifier Assignment Procedure;
- SREG Construction Procedure;
- Relationship Construction Procedure;
- Provenance Construction Procedure;
- Validation Procedure;
- Publication Procedure;
- Update Procedure;
- Correction Procedure;
- Versioning Procedure;
- Status Transition Procedure;
- Lifecycle Transition Procedure;
- Supersession Procedure;
- Revocation Procedure;
- Restricted-Publication Procedure;
- Archival and Preservation Procedure;
- Exception Procedure;
- Procedure Review and Change Procedure.

---

## Procedure Characteristics

### Repeatable

The same operational conditions should produce comparable treatment.

### Attributable

Material actions should identify the responsible role, process, workflow, or authority.

### Versioned

The Procedure Version applied to a material action should be identifiable.

### Reviewable

The operational record should preserve enough evidence to reconstruct what was done and why.

### Governed

Procedures require defined authority, approval, effective dates, review, and historical preservation.

---

## Procedure Document Requirements

Every formal Registry Procedure should identify:

- procedure title;
- procedure identifier;
- procedure version;
- authority;
- effective date;
- purpose;
- scope;
- prerequisites;
- required inputs;
- roles and responsibilities;
- ordered steps;
- decision points;
- required outputs;
- validation or quality checks;
- exception path;
- records to preserve;
- related Policies;
- related Rules;
- review date;
- change history.

---

## Illustrative Procedure Record

```text
procedure_identifier: "SREG-PROC-PUBLICATION"
procedure_title: "Registry Publication Procedure"
procedure_version: "1.0.0"
authority: "Satoshium Registry"
effective_date: "2026-08-02"
status: "active"
```

Final procedure identifiers, field names, controlled values, and version syntax remain subject to Registry Governance.

---

## Source Intake Procedure

The Source Intake Procedure should:

1. Receive or identify the proposed Source Record.
2. Record the source title and known Source-System Identifier.
3. Identify the apparent Source Institution.
4. Capture the canonical source location.
5. Record source format, version, publication date, and access conditions.
6. Preserve initial supporting evidence.
7. Assign an intake reference or workflow identifier.
8. Route the source to Source Authority Review.

```text
Intake records a candidate source.
It does not establish Source Authority or Registrability.
```

---

## Source Authority Review Procedure

The Source Authority Review Procedure should:

1. Identify the institution that created, issued, or controls the Source Record.
2. Review canonical publication, repository, metadata, and institutional evidence.
3. Distinguish authority from hosting, custody, mirroring, or archival preservation.
4. Determine whether authority is direct, delegated, historical, or external.
5. Identify conflicting authority claims.
6. Record the review outcome and supporting evidence.
7. Apply conditions or limitations when authority is incomplete.
8. Route approved sources to Registrability Review.

---

## Registrability Review Procedure

The Registrability Review Procedure should:

1. Confirm positive or sufficient Source Authority.
2. Confirm the object has distinguishable identity.
3. Confirm the object falls within Registry scope.
4. Identify an approved Registry Record Type.
5. Confirm minimum metadata and provenance are available.
6. Review durable institutional or historical relevance.
7. Review access, rights, privacy, safety, and security limitations.
8. Perform duplicate and conflict review.
9. Record the Registrability outcome.
10. Route approved records to Identifier Assignment.

---

## Duplicate and Conflict Review Procedure

The Duplicate and Conflict Review Procedure should:

1. Search existing SREGs using titles, identifiers, source references, and metadata.
2. Compare the candidate source with existing Source Records.
3. Determine whether the candidate is identical, derivative, versioned, related, or distinct.
4. Review conflicting Source Authority or Source-System Identifier claims.
5. Determine whether to reject, merge, relate, supersede, or register separately.
6. Record findings and rationale.
7. Preserve unresolved conflicts as visible conditions.

---

## Record-Type Assignment Procedure

The Record-Type Assignment Procedure should:

1. Review the nature and institutional role of the Source Record.
2. Compare the source against approved Registry Record Types.
3. Select one primary Record Type.
4. Identify the applicable Record-Type Profile.
5. Confirm profile-specific required fields and relationships.
6. Document ambiguous or conditional classification.
7. Record the assigned Record Type and Profile Version.

---

## Registry Identifier Assignment Procedure

The Registry Identifier Assignment Procedure should:

1. Confirm a positive Registrability outcome.
2. Confirm the assigned Registry Record Type.
3. Confirm the current production Registry Identifier pattern: `SREG-[YEAR]-[SEQUENCE]`.
4. Determine the applicable issuance year.
5. Generate the next available annual sequence value.
6. Construct the Registry Identifier using the approved pattern.
7. Check uniqueness and non-reuse.
8. Create the identifier-assignment record.
9. Preserve Registry Record Type as a separate controlled classification and do not encode it into the Registry Identifier.
10. Preserve the Source-System Identifier separately.
11. Reserve or assign the Registry Identifier.
12. Route the record to SREG Construction.

```text
Registry identity and Registry classification are separate.
The production Registry Identifier does not contain a Record Type segment.
```

---

## SREG Construction Procedure

The SREG Construction Procedure should:

1. Open a new SREG using the assigned Registry Identifier.
2. Apply the current SREG Base Schema.
3. Apply the applicable Record-Type Profile.
4. Populate Registry-owned identity and classification fields.
5. Preserve Source Institution and Source-System Identifier.
6. Preserve the canonical Source Record reference.
7. Construct provenance fields.
8. Construct typed relationships.
9. Assign Registry Status and Registry Lifecycle State.
10. Assign Registry Entry Version.
11. Construct the reusable four-file SREG package using the assigned Registry Identifier as the directory name.
12. Generate `index.html` as the Registration Overview.
13. Generate `registry-entry.html` as the canonical human-readable SREG.
14. Generate `record.json` as the canonical machine-readable SREG.
15. Generate `README.md` as the directory-level documentation.
16. Confirm the four files describe the same Registry object and preserve the same canonical identity, authority, provenance, relationship, version, Validation, and Publication context.
17. Route the completed SREG package to Validation.

```text
SREG-YYYY-NNNN/
├── index.html
├── registry-entry.html
├── record.json
└── README.md
```

The four-file package is the repeatable publication structure for a normal SREG.

Record-Type Profiles may require additional fields, relationships, source artifacts, or supporting references, but they do not replace the canonical four-file package.

---

## Relationship Construction Procedure

The Relationship Construction Procedure should:

1. Identify source and target objects.
2. Preserve source and target identifier domains.
3. Select an approved relationship type.
4. Confirm direction and any governed inverse.
5. Identify Relationship Authority.
6. Preserve version and temporal context.
7. Attach supporting evidence when required.
8. Check for duplicates or contradictions.
9. Assign Relationship Status.
10. Publish consistently across official forms.

---

## Provenance Construction Procedure

The Provenance Construction Procedure should:

1. Identify the Source Institution.
2. Identify the Authoritative Source Record.
3. Preserve the Source-System Identifier.
4. Preserve source version, date, status, and canonical location.
5. Identify repository, publisher, custody, or archive.
6. Distinguish original, derived, mirrored, and archived artifacts.
7. Preserve generation manifests and integrity references when available.
8. Record registration, validation, and publication history.
9. Preserve predecessor, successor, and unavailable-source context.

---

## Validation Procedure

The Validation Procedure should:

1. Identify the Registry Entry Version being validated.
2. Record the applicable Rules, Policies, schemas, profiles, and controlled-value versions.
3. Run structural and machine-readable checks.
4. Review Source Authority and Registrability records.
5. Validate identifiers, provenance, and relationships.
6. Validate Registry Status, Registry Lifecycle State, and version fields.
7. Compare human-readable and machine-readable forms.
8. Classify findings as blocking errors, warnings, exceptions, or informational findings.
9. Record the Validation outcome.
10. Return invalid SREGs for correction or route valid SREGs to Publication.

---

## Publication Procedure

The Publication Procedure should:

1. Confirm the Validation outcome permits publication.
2. Confirm the current Registry Entry Version.
3. Confirm the canonical SREG directory and four-file publication package are complete.
4. Assign canonical human-readable and machine-readable URLs.
5. Confirm the Registry Identifier resolves correctly.
6. Confirm required downloadable or supporting artifacts are available.
7. Confirm official forms agree.
8. Apply required warnings, restrictions, or historical notices.
9. Create the publication record.
10. Release the SREG through official Registry channels.
11. Add the published SREG to **Registered Items**.
12. Verify production resolution, file availability, and Registered Items discovery.
13. Record publication history and any Chronicle or Beacon references.

```text
Registered Items is the concise public listing of completed Registry registrations.
Publication of a SREG is not operationally complete until the published entry is discoverable there.
```

---

## Update Procedure

The Update Procedure should:

1. Identify the update trigger.
2. Determine which version domains changed.
3. Preserve the prior Registry Entry Version.
4. Update affected fields, relationships, provenance, status, or lifecycle data.
5. Assign a new Registry Entry Version when required.
6. Record the change summary and changed fields.
7. Perform targeted or full revalidation.
8. Publish the updated SREG.
9. Preserve prior publication and version history.

---

## Correction Procedure

The Correction Procedure should:

1. Receive or identify the suspected error.
2. Confirm the affected Registry Identifier and Registry Entry Version.
3. Review evidence and determine whether correction is required.
4. Preserve the prior value.
5. Record the corrected value, reason, date, and correction authority.
6. Assign a new Registry Entry Version when required.
7. Update all official formats.
8. Revalidate affected domains.
9. Publish a Correction Record or notice when required.
10. Preserve historical access to the prior state.

```text
Material corrections must never be applied silently.
```

---

## Versioning Procedure

The Versioning Procedure should:

1. Identify the current Registry Entry Version.
2. Identify the nature and scale of the proposed change.
3. Determine whether the change is major, minor, patch, or non-versioned.
4. Confirm Source-Record Version remains separate.
5. Assign the new Registry Entry Version.
6. Create the version-assignment record.
7. Preserve schema, profile, policy, and Procedure Versions applied.
8. Validate the new version.
9. Publish current and historical version links.

---

## Status Transition Procedure

The Status Transition Procedure should:

1. Identify the current Registry Status.
2. Identify the proposed Registry Status.
3. Confirm the transition is allowed.
4. Preserve Source-Record Status separately.
5. Record transition date, authority, reason, and evidence.
6. Assign a new Registry Entry Version when material.
7. Revalidate affected publication fields.
8. Publish the updated status and history.

---

## Lifecycle Transition Procedure

The Lifecycle Transition Procedure should:

1. Identify the current Registry Lifecycle State.
2. Identify the proposed state.
3. Confirm the transition is permitted.
4. Identify required notices, relationships, or successor records.
5. Record date, authority, reason, and evidence.
6. Assign a new Registry Entry Version when required.
7. Revalidate status, publication, provenance, and relationship fields.
8. Publish the new state and preserve prior history.

---

## Supersession Procedure

The Supersession Procedure should:

1. Identify the SREG being superseded.
2. Identify or create the successor SREG.
3. Confirm supersession rather than an ordinary version update is appropriate.
4. Create typed predecessor and successor relationships.
5. Record supersession date, reason, and authority.
6. Update Registry Status and Registry Lifecycle State.
7. Publish supersession notices in all official forms.
8. Preserve resolution of the prior Registry Identifier.
9. Link prior versions and successor publication.

---

## Revocation Procedure

The Revocation Procedure should:

1. Identify the basis for revocation.
2. Confirm Registry has authority to revoke the SREG's Registry condition.
3. Preserve Source Institution and Source-Record Status separately.
4. Record revocation date, reason, authority, and supporting evidence.
5. Assign a new Registry Entry Version when required.
6. Update Registry Status and Registry Lifecycle State.
7. Publish a revocation notice.
8. Preserve prior versions and historical resolution.
9. Identify successor or replacement records when applicable.

---

## Restricted-Publication Procedure

The Restricted-Publication Procedure should:

1. Identify the restriction basis.
2. Determine which fields, artifacts, or sources require restriction.
3. Preserve the least restrictive public metadata appropriate.
4. Apply access controls or publication limitations.
5. Publish a restriction notice when appropriate.
6. Record authority, date, scope, and review condition.
7. Validate that restricted information is not exposed.
8. Review the restriction periodically or when conditions change.

---

## Archival and Preservation Procedure

The Archival and Preservation Procedure should:

1. Identify the record, version, artifact, or source requiring preservation.
2. Capture canonical metadata and last-known source references.
3. Preserve historical Registry Entry Versions.
4. Preserve downloadable artifacts and manifests when permitted.
5. Label archival copies accurately.
6. Preserve integrity references when available.
7. Record custody and archival location.
8. Update lifecycle and publication notices.
9. Confirm archival resolution remains functional.

---

## Exception Procedure

The Exception Procedure should:

1. Identify the governing requirement from which departure is requested.
2. Document the reason and operational need.
3. Assess scope, risk, impact, and alternatives.
4. Identify the approving authority.
5. Define duration or review date.
6. Document compensating controls.
7. Record approval, denial, or modification.
8. Expose the exception in Validation and Publication when material.
9. Close, renew, or supersede the exception at review.

```text
An exception permits a governed departure.
It does not silently rewrite a Rule, Policy, or Procedure.
```

---

## Procedure Records

Material operational Procedure records should preserve:

- Procedure Identifier;
- Procedure Version;
- Registry Identifier or workflow reference;
- date and time;
- responsible role or process;
- inputs reviewed;
- steps completed;
- decision points;
- findings;
- exceptions;
- outputs produced;
- Validation result;
- Publication or Correction reference;
- supporting evidence.

---

## Procedure Validation

Before approval or republication, a Procedure should be reviewed for:

- authority;
- scope;
- consistency with Rules and Policies;
- clear prerequisites;
- complete inputs;
- complete outputs;
- ordered and actionable steps;
- defined decision points;
- recordkeeping requirements;
- exception handling;
- validation or quality checks;
- version and effective date;
- historical continuity.

---

## Procedure Lifecycle

```text
Draft
  ↓
Review
  ↓
Approved
  ↓
Active
  ↓
Revised
  ↓
Superseded or Retired
  ↓
Archived
```

Procedure lifecycle values should remain separate from SREG Lifecycle States.

---

## Procedure Versioning

Procedure changes should preserve:

- prior Procedure Version;
- new Procedure Version;
- change date;
- effective date;
- approval authority;
- change summary;
- affected Policies;
- affected Rules;
- affected workflows;
- affected forms;
- training requirements;
- migration requirements;
- supersession reference;
- historical publication.

---

## Procedure Review

Procedures should be reviewed when:

- Rules change;
- Policies change;
- schemas change;
- Record-Type Profiles change;
- repeated errors occur;
- repeated exceptions occur;
- Validation identifies systemic defects;
- new automation becomes available;
- source architecture changes;
- publication architecture changes;
- archival architecture changes;
- roles or authority boundaries change;
- Suite Interoperability requirements change;
- scheduled review date arrives.

---

## Automated and Manual Procedures

Registry Procedures may include:

- fully manual institutional review;
- automated structural checks;
- assisted record construction;
- hybrid validation workflows;
- automated publication deployment;
- manual exception approval;
- periodic automated source checks;
- manual archival review.

```text
Automation may execute Procedure steps.
It does not eliminate institutional accountability.
```

---

## Procedure Conflicts

When Procedures conflict, Registry should:

1. Identify the conflicting steps.
2. Determine the governing Rule and Policy.
3. Apply the more specific current Procedure when appropriate.
4. Suspend ambiguous action when material risk exists.
5. Escalate unresolved conflicts to Governance.
6. Document interim treatment.
7. Correct or supersede the conflicting Procedure.
8. Preserve the historical record.

---

## Relationship to Policies

Policies establish durable institutional decisions.

Procedures convert those decisions into repeatable steps.

```text
Policy
  ↓
Required Institutional Position
  ↓
Procedure
  ↓
Operational Action
```

A Procedure may implement a Policy but must not silently expand or contradict it.

---

## Relationship to Rules

Rules establish binding Registry requirements.

Procedures operationalize those requirements through documented steps.

A Procedure must not weaken, bypass, or redefine a Rule.

---

## Relationship to Navigator

Navigator may represent or coordinate Registry Procedures as formal workflows.

Registry remains authoritative for Registry Procedures.

Navigator remains authoritative for Navigator-created:

- workflow definitions;
- workflow execution structures;
- coordination records;
- cross-system workflow references.

---

## Relationship to Validation

Validation may be one Procedure domain and may also be used to confirm that other Procedures were followed correctly.

Procedure records should preserve:

- Procedure Version;
- checks performed;
- findings;
- exceptions;
- outputs;
- Validation result.

---

## Relationship to Publication

Publication Procedures convert validated SREGs into official Registry publications.

They should preserve:

- publication authority;
- Registry Entry Version;
- canonical URLs;
- official formats;
- notices;
- release records;
- historical continuity.

---

## Relationship to Governance

Registry Governance should control:

- Procedure authority;
- approval;
- versioning;
- effective dates;
- exception handling;
- conflict resolution;
- review cycles;
- supersession;
- retirement;
- publication;
- historical preservation.

---

## Current Directory Structure

```text
registry/
└── procedures/
    ├── index.html
    └── README.md
```

### `index.html`

The public Registry Procedures page.

### `README.md`

The directory-level documentation explaining the canonical Registry workflow, individual operational Procedures, Procedure records, validation, versioning, review, conflict handling, and maintenance.

Future supporting materials may include:

```text
procedures/
├── index.html
├── README.md
├── source-intake.md
├── source-authority-review.md
├── registrability-review.md
├── identifier-assignment.md
├── sreg-construction.md
├── validation.md
├── publication.md
├── correction.md
├── versioning.md
├── supersession.md
├── restricted-publication.md
├── archival-preservation.md
├── exceptions.md
├── examples/
├── history/
└── versions/
```

These materials should be introduced only when corresponding operational procedures are formally established.

---

## Relationship to Other Registry Documentation

This directory should remain consistent with:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Rules;
- Registry Policies;
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
- Registry Governance;
- Registry Controlled Values;
- Suite Standards;
- Suite Methodology;
- Suite Interoperability.

---

## Maintenance Requirements

When Procedure architecture changes:

- update `index.html`;
- update this README;
- update Procedure domains;
- update Procedure document requirements;
- update ordered operational steps;
- update roles and responsibilities;
- update required inputs and outputs;
- update recordkeeping requirements;
- update exception handling;
- update Procedure Validation requirements;
- update Procedure Lifecycle values;
- update Procedure Versioning rules;
- update review triggers;
- update Navigator integration;
- update affected Registry Policies;
- update affected Registry Rules;
- update Validation requirements;
- update Publication requirements;
- update examples;
- preserve prior Procedure Versions;
- document material changes in the Registry Changelog;
- reconcile human-readable and machine-readable materials.

---

## Guiding Principles

- Procedures implement existing authority.
- Procedures must remain consistent with Rules and Policies.
- Procedures must be repeatable.
- Procedures must be attributable.
- Procedures must be versioned.
- Procedures must preserve operational records.
- Registry identity and Record Type classification must remain separate.
- SREG construction should use the canonical reusable four-file package.
- Publication should include Registered Items discovery.
- Decision points must be explicit.
- Exceptions must be governed and documented.
- Automation does not eliminate accountability.
- Material corrections must not be silent.
- Prior Procedure Versions must remain discoverable.
- Procedure conflicts must be escalated and resolved transparently.
- Procedures must not absorb Source Authority.
- Procedures must not expand Registry beyond its scope.
- Operational records preserve institutional memory.

---

## Disclaimer

Registry Procedures do not by themselves establish:

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
- authority outside Registry scope.

Those remain controlled by the applicable Source Institution, Certifier, Attestor, rights holder, governing authority, Source Record, Policy, Rule, or external system.

---

## Guiding Statement

> Policies establish durable decisions.
>
> Procedures create repeatable action.
>
> Records preserve accountability.
