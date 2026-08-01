# Registry Correction Policy

## Policy Status

**Policy Name:** Registry Correction Policy  
**Policy Type:** Institutional Registry Policy  
**Applies To:** Satoshium Registry Entries (SREGs) and Registry-owned publication artifacts  
**Initial Policy Version:** 1.0.0  
**Status:** Active  
**Effective Date:** 2026-08-01  

---

## Purpose

This policy establishes the binding institutional requirements for correcting Registry-owned information within Satoshium Registry.

The purpose of a correction is to improve accuracy, consistency, and usability while preserving:

- Registry identity;
- prior versions;
- source authority;
- provenance;
- public continuity;
- correction history;
- institutional accountability.

A correction must not silently erase the prior Registry state.

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
Registry Correction Policy
  ↓
Registry Correction Procedure
  ↓
Correction Record and Replacement SREG Version
```

This policy is subordinate to applicable Suite Standards and Registry Rules.

The corresponding correction procedure defines how Registry performs the actions required by this policy.

---

## Policy Statement

Registry must correct Registry-owned information when a confirmed error, inconsistency, omission, broken reference, invalid relationship, or material publication defect affects an official SREG or Registry publication.

Corrections must be:

- authorized;
- attributable;
- documented;
- version-aware;
- schema-valid;
- consistent across official forms;
- limited to Registry authority;
- historically preserved.

Registry must not use a correction to rewrite or assume ownership of Source Institution information.

---

## Scope

This policy applies to corrections involving:

- Registry Identifiers;
- Registry Record Types;
- Registry classifications;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Versions;
- Registry-owned metadata;
- Registry-controlled relationships;
- Registry-controlled references;
- Registry publication dates;
- Registry correction history;
- human-readable Registry pages;
- machine-readable SREG records;
- Registry indexes;
- Registry manifests;
- Registry relationship maps;
- Registry archival or supersession notices.

---

## Outside Scope

This policy does not authorize Registry to correct:

- Source Record content;
- Source-System Identifiers;
- Certification Outcomes;
- Certification Status;
- attestation conclusions;
- Chronicle event meaning;
- Anchor integrity references;
- Beacon discovery signals;
- Atlas jurisdiction intelligence;
- Navigator workflow definitions;
- ownership or licensing statements controlled by another authority;
- external legal or governmental records.

When an apparent error belongs to a Source Institution, Registry should:

1. preserve the currently known source-reported value;
2. document the discrepancy where appropriate;
3. refer the issue to the Source Institution;
4. update the SREG only after a source-controlled change or approved Registry action;
5. preserve the distinction between source correction and Registry correction.

---

## Correction Authority

Registry is authorized to correct only Registry-owned information.

Correction authority includes:

- correcting Registry metadata;
- correcting Registry classification;
- correcting Registry references;
- correcting Registry relationships;
- correcting Registry publication inconsistencies;
- correcting Registry status or lifecycle values when incorrectly applied;
- correcting machine-readable structural defects;
- correcting human-readable and machine-readable mismatches.

Correction authority does not include changing the substantive meaning of an Authoritative Source Record.

---

## Guiding Principles

### Transparency

Material corrections must be understandable and traceable.

### Continuity

Prior Registry identity, references, versions, and relationships should remain preserved.

### Accuracy

Corrections should improve the factual and structural accuracy of Registry-owned information.

### Preservation

Prior official versions should remain available or historically represented when material changes occur.

### Authority Separation

Registry must not absorb or redefine Source Institution authority.

### Consistency

All official forms of the same SREG must reflect the correction consistently.

### Proportionality

Documentation requirements should reflect the significance of the correction.

### Accountability

Material corrections should identify the reason, date, affected version, and responsible Registry action.

---

## Correction Classes

### Editorial Correction

Addresses:

- typographical errors;
- punctuation;
- formatting;
- spacing;
- non-substantive wording;
- accessibility labels;
- minor presentation defects.

Editorial corrections do not change the institutional meaning of the SREG.

### Metadata Correction

Addresses Registry-owned metadata such as:

- title;
- date;
- Registry Status;
- Registry Lifecycle State;
- version label;
- publication metadata;
- display name;
- non-source-controlled descriptive fields.

### Classification Correction

Addresses:

- incorrect Registry Record Type;
- incorrect Registry taxonomy;
- incorrect hierarchy placement;
- incorrect profile assignment;
- incorrect Registry classification.

Classification corrections may be material because they can affect schemas, relationships, discovery, and interpretation.

### Reference Correction

Addresses:

- broken links;
- incorrect canonical URLs;
- invalid repository paths;
- missing public references;
- incorrect source references;
- incorrect machine-readable locations.

### Relationship Correction

Addresses:

- incorrect relationship type;
- incorrect relationship target;
- missing required relationship;
- invalid reciprocal relationship;
- duplicate relationship;
- structurally invalid relationship.

### Structural Correction

Addresses:

- schema nonconformance;
- invalid field structure;
- malformed JSON;
- missing required Registry fields;
- incompatible version declaration;
- publication-format inconsistency.

### Source-Reference Correction

Addresses Registry's representation of source-controlled information, including:

- incorrect Source Institution;
- incorrect Source-System Identifier;
- incorrect source URL;
- incorrect source version reference;
- incorrect source status transcription.

A Source-Reference Correction changes Registry's reference to the source.

It does not change the Source Record itself.

### Material Correction

A correction is material when it changes or may change:

- the interpretation of the SREG;
- Record Type;
- classification;
- Registry Status;
- Lifecycle State;
- source attribution;
- authoritative source reference;
- core relationships;
- version history;
- discoverability;
- interoperability behavior;
- machine-readable validation result.

### Administrative Correction

Addresses:

- internal processing metadata;
- correction-record linkage;
- approval metadata;
- repository organization;
- publication housekeeping;
- non-substantive operational fields.

Administrative corrections must still preserve official consistency.

---

## Minor Corrections

Minor corrections may include:

- typographical corrections;
- punctuation corrections;
- formatting corrections;
- non-substantive accessibility improvements;
- repair of an obviously broken link where the intended target is unchanged;
- minor display metadata correction.

Minor corrections may use simplified documentation when:

- institutional meaning does not change;
- source attribution does not change;
- Registry Status does not change;
- Lifecycle State does not change;
- Record Type does not change;
- material relationships do not change;
- schema meaning does not change.

Even minor corrections must be reflected consistently across affected official forms.

---

## Material Corrections

Material corrections require a formal Correction Record.

A material correction should preserve:

- Registry Identifier;
- affected SREG version;
- correction class;
- correction reason;
- affected fields;
- prior value;
- replacement value;
- correction date;
- responsible Registry action;
- Source Record impact;
- resulting Registry Status;
- resulting Lifecycle State;
- replacement SREG version;
- related publication updates;
- approval or review record where required.

Material corrections should normally produce a new Registry Entry Version.

---

## Correction Workflow

Registry corrections must follow the approved correction workflow:

```text
Issue Identified
  ↓
Authority Determined
  ↓
Impact Reviewed
  ↓
Correction Classified
  ↓
Correction Prepared
  ↓
Schema Validated
  ↓
Version Assigned
  ↓
Correction Record Created
  ↓
Official Forms Reconciled
  ↓
Correction Published
  ↓
History Preserved
```

---

## Issue Identification

A correction issue may be identified through:

- Registry review;
- Source Institution notice;
- user report;
- schema validation failure;
- publication mismatch;
- broken-reference monitoring;
- interoperability review;
- lifecycle review;
- correction audit;
- repository review.

Issue identification does not itself authorize a correction.

---

## Authority Determination

Before correcting an issue, Registry must determine whether the affected information is:

- Registry-owned;
- source-controlled;
- jointly represented;
- externally controlled;
- unclear.

If authority is unclear, the correction should not proceed as a Registry-owned correction until responsibility is resolved.

---

## Impact Review

Registry should evaluate whether the proposed correction affects:

- SREG identity;
- Source Institution attribution;
- Source-System Identifier;
- Record Type;
- Registry Status;
- Lifecycle State;
- versions;
- relationships;
- public references;
- schema validity;
- human-readable publication;
- machine-readable publication;
- indexes;
- interoperability;
- historical interpretation.

The impact review determines whether the correction is minor or material.

---

## Version Requirements

A correction must preserve version distinctions.

Registry should distinguish among:

- Registry Entry Version;
- SREG schema version;
- Record-Type Profile version;
- Registry specification version;
- Source-Record version;
- Source Institution publication version.

A material Registry correction should normally follow:

```text
Prior SREG Version
  ↓
Correction Record
  ↓
Replacement SREG Version
```

A correction to Registry-owned information must not falsely imply that the Source Record version changed.

---

## Correction Record Requirements

A formal Correction Record should contain:

- correction identifier;
- Registry Identifier;
- affected SREG version;
- correction class;
- correction severity;
- issue description;
- authority determination;
- correction reason;
- prior value or condition;
- replacement value or condition;
- affected fields;
- Source Record impact;
- schema impact;
- relationship impact;
- status impact;
- lifecycle impact;
- correction date;
- responsible Registry action;
- replacement SREG version;
- approval or review information;
- publication locations;
- related correction, supersession, revocation, or archival records.

---

## Record Status During Correction

A SREG may remain Active while a correction is prepared when:

- the issue is minor;
- the issue does not materially mislead users;
- source attribution remains valid;
- no critical integrity defect exists.

A SREG may require a temporary Registry designation such as:

- Under Review;
- Correction Pending;
- Publication Hold;
- Restricted from Active Use.

Temporary designations should be defined by the Registry Status framework rather than improvised.

Source-Record Status must remain separate from temporary Registry designations.

---

## Corrections and Updates

Correction and update are not interchangeable.

### Correction

Repairs an error in Registry-owned information or Registry-controlled publication.

### Update

Reflects new, changed, or expanded information that may not have been erroneous.

Example:

```text
Broken Registry URL
  = Correction
```

```text
Source Record publishes a new version
  = Source-driven Update
```

The applicable Record Update Policy should govern non-correction updates.

---

## Corrections and Supersession

A correction may require supersession when:

- the prior SREG is materially defective;
- the Record Type changes fundamentally;
- identity must be restructured;
- a replacement SREG is required;
- the prior entry cannot remain the current canonical Registry representation.

Supersession should preserve:

- prior Registry Identifier;
- replacement Registry Identifier or version;
- reason;
- date;
- relationship between old and new records;
- historical discoverability.

---

## Corrections and Revocation

A correction may lead to revocation when:

- registration was invalid;
- source authority was misidentified;
- the SREG materially misrepresented the Source Record;
- correction cannot restore institutional validity;
- an approved governance action requires withdrawal.

Revocation must follow the applicable Lifecycle and Record Retirement policies.

A correction should not be mislabeled as revocation merely because a value changed.

---

## Corrections and Archival

A corrected, superseded, or revoked SREG may later be archived.

Archival must preserve:

- prior identity;
- prior versions;
- correction history;
- source attribution;
- source references;
- relationship history;
- supersession or revocation history.

Archived does not mean deleted.

---

## Source Institution Notification

Registry should notify or coordinate with the Source Institution when a correction materially affects:

- Source Institution attribution;
- Source-System Identifier;
- source reference;
- source version;
- source status transcription;
- interoperability relationship;
- public interpretation of the source.

Notification does not transfer correction authority.

---

## Publication Consistency

Corrections must be applied consistently across all affected official Registry artifacts, including:

- human-readable Registry Entry pages;
- machine-readable SREG records;
- catalog indexes;
- relationship indexes;
- version history;
- correction history;
- supersession notices;
- revocation notices;
- archival records;
- interoperability references;
- repository manifests.

A correction is incomplete when official Registry forms materially disagree.

---

## Validation Requirements

Before publication, Registry should validate that:

- correction authority is established;
- the correction class is accurate;
- required documentation exists;
- affected versions are identified;
- replacement version is valid;
- Registry and source fields remain distinct;
- required references remain available;
- relationships remain structurally valid;
- applicable schemas validate;
- official forms agree;
- correction history is linked;
- prior material versions remain preserved.

---

## Human-Readable Disclosure

A material correction should be understandable to a public reader.

Human-readable disclosure may include:

- correction notice;
- correction date;
- correction summary;
- affected version;
- replacement version;
- reason;
- source impact;
- link to correction history.

Minor editorial corrections may be recorded through concise change history.

---

## Machine-Readable Disclosure

A machine-readable Correction Record may include:

- correction identifier;
- affected Registry Identifier;
- affected version;
- replacement version;
- correction class;
- correction severity;
- reason;
- affected fields;
- prior values;
- replacement values;
- timestamps;
- source impact;
- status impact;
- lifecycle impact;
- related records;
- schema version.

Machine-readable disclosure should follow the applicable correction-record schema.

---

## Prohibited Correction Practices

Registry must not:

- silently overwrite a material prior version;
- alter Source Record content;
- change a Source-System Identifier without preserving the prior reference;
- collapse Registry Status and Source-Record Status;
- use correction to conceal a revocation or supersession;
- delete correction history solely for convenience;
- publish inconsistent HTML and JSON values;
- relabel a source change as a Registry correction;
- use a correction to imply certification, attestation, endorsement, or legal recognition;
- backdate a correction without documented reason.

---

## Review and Approval

Material corrections should receive the level of review required by Registry Procedure.

Review may confirm:

- authority;
- severity;
- classification;
- version impact;
- source impact;
- lifecycle impact;
- publication completeness;
- schema validity;
- preservation of prior history.

The reviewing role and approval requirement should be documented by procedure.

---

## Policy Exceptions

Exceptions to this policy must be documented.

An exception should identify:

- affected SREG;
- applicable policy requirement;
- reason;
- approving authority;
- duration;
- risk;
- preservation measures;
- follow-up requirement;
- review or expiration date.

An exception does not permanently amend this policy.

---

## Relationship to Other Registry Policies

This policy works with:

- Record Creation Policy;
- Record Update Policy;
- Record Retirement Policy;
- Registry Lifecycle;
- Registry Status;
- Registry Schemas;
- Registry Entry Model;
- Registry Integration;
- Registry Procedures.

When policies overlap:

- Correction Policy governs repair of Registry-owned errors.
- Update Policy governs non-correction changes.
- Retirement Policy governs removal from active use.
- Lifecycle governs state transitions.
- Status defines current operational designation.

---

## Policy Review

This policy should be reviewed when:

- Suite Standards change;
- Registry Rules change;
- Registry schemas change materially;
- Record Types expand;
- correction classes prove insufficient;
- repeated correction failures occur;
- publication formats change;
- interoperability requirements change;
- operational ambiguity is identified.

Policy review should preserve prior versions and amendment history.

---

## Policy Summary

A Registry correction must improve Registry accuracy without erasing identity, source authority, prior versions, or historical context.

The correction process should make clear:

- what was wrong;
- who had authority to correct it;
- what changed;
- why it changed;
- which version was affected;
- which version replaced it;
- whether the Source Record changed;
- how the correction was published and preserved.

---

## Disclaimer

This policy governs Registry-owned corrections.

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

> Errors may occur.
>
> Authority must be identified.
>
> Corrections must be documented.
>
> Prior versions must remain preserved.
>
> Transparency protects trust.
