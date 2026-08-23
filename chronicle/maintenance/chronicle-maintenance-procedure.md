# Chronicle Maintenance Procedure

## Purpose

The Chronicle Maintenance Procedure defines how Satoshium Chronicle reviews, preserves, and maintains published Chronicle Entries after they enter production.

Maintenance exists to ensure that Chronicle remains:

- resolvable;
- internally consistent;
- historically accurate;
- traceable to authority;
- schema-aware;
- interoperable;
- correction-ready;
- version-aware;
- publication-aware;
- durable over time.

Maintenance does not silently rewrite history.

The governing principle is:

> Maintain the record without erasing the record.

And operationally:

> Correct forward. Preserve backward.

---

# Scope

This procedure applies to published Chronicle Entries and their associated Chronicle-owned artifacts.

It may include review of:

- canonical Entry HTML;
- canonical Entry JSON;
- Entry README documentation;
- Validation artifacts;
- Publication Gate artifacts;
- authoritative references;
- Source references;
- Evidence references;
- Provenance;
- Relationships;
- Controlled Values;
- schema compatibility;
- Verification state;
- Validation lineage;
- Publication State;
- Lifecycle State;
- Corrections;
- Entry Versions;
- reciprocal Suite references;
- historical preservation requirements.

This procedure does not authorize Chronicle to modify authoritative records owned by other institutions.

---

# Maintenance Position

Chronicle maintenance begins after an Entry has entered production.

Conceptually:

```text
Occurrence
  ↓
Preservation Eligibility
  ↓
Entry Creation
  ↓
Verification
  ↓
Validation
  ↓
Publication Gate
  ↓
Publication
  ↓
Maintenance
  ↓
Correction / Versioning / New Entry where required
  ↓
Historical Preservation
```

Maintenance is not a second Validation run by default.

It is a continuing institutional review process used to determine whether any later condition requires action.

---

# Maintenance Questions

A maintenance review should ask:

```text
Does the canonical Entry still resolve?

Does the machine-readable record still resolve?

Do authoritative references still resolve?

Do referenced Suite records still exist at their expected locations?

Has an authoritative record materially changed?

Did a new authoritative action occur?

Are Chronicle's human-readable and machine-readable representations still aligned?

Has a schema or Event-Type Profile changed?

Have relevant Controlled Values changed?

Are Relationships still accurate?

Is Provenance still sufficient?

Have limitations changed?

Has a Correction become necessary?

Has a new Entry Version become necessary?

Has a distinct new Preservation-Eligible Occurrence happened?

Is Publication State still correct?

Is Lifecycle State still correct?

Are reciprocal Suite references intact?

Is historical continuity preserved?
```

---

# Maintenance Categories

Chronicle maintenance should distinguish among several kinds of change.

## 1. Technical Maintenance

Technical Maintenance addresses non-substantive implementation conditions.

Examples:

- broken HTML markup;
- accessibility repair;
- CSS repair;
- broken navigation;
- internal-link repair;
- external URL redirect where Source identity is unchanged;
- formatting cleanup;
- metadata presentation repair;
- file-path correction;
- reciprocal link addition;
- footer or shared component update.

Technical Maintenance should not alter historical meaning.

A new Entry Version is ordinarily not required when the underlying Chronicle representation remains materially unchanged.

---

## 2. Reference Maintenance

Reference Maintenance reviews the continued resolvability and identity of authoritative and supporting references.

Examples:

- Certification Package URL changes;
- Registry URL changes;
- Atlas record location changes;
- archived replacement URL becomes necessary;
- external Source disappears;
- canonical reference changes while underlying identity remains the same.

Chronicle should preserve the durable identity of the referenced object whenever possible.

A changed URL alone does not necessarily mean the underlying referenced record changed.

---

## 3. Representation Maintenance

Representation Maintenance checks agreement among coordinated Chronicle artifacts.

For a production Entry, this may include:

```text
index.html
record.json
README.md
```

The human-readable and machine-readable representations describe the same canonical Chronicle Entry.

Material discrepancies should be treated as Chronicle representation defects.

Chronicle should determine whether the defect is:

```text
Editorial / technical
```

or:

```text
Substantive
```

before deciding whether a Correction or new Entry Version is required.

---

## 4. Schema Maintenance

Schema Maintenance reviews whether a published Entry remains understandable and valid under the Schema Version that originally governed it.

A later schema release does not automatically invalidate an older Entry.

Chronicle should preserve:

- original `schema_id`;
- original `schema_version`;
- applicable Event-Type Profile;
- compatibility information;
- migration requirements where applicable;
- historical interpretability.

Older Entries should remain understandable under the schema that governed them when published.

Migration should not occur merely to make all historical Entries conform to the newest schema.

---

## 5. Controlled Value Maintenance

Controlled Value Maintenance reviews whether governed vocabularies affecting an Entry have changed.

Examples include changes to:

- Event Types;
- Verification States;
- Lifecycle States;
- Publication States;
- Relationship Types;
- Source Types;
- Evidence Types;
- Correction Types.

A newly added Controlled Value does not require historic Entries to change.

A deprecated or corrected value may require review if an existing Entry uses it.

Chronicle must distinguish:

```text
new vocabulary availability
```

from:

```text
existing Entry defect
```

---

## 6. Authority Reference Maintenance

Chronicle should periodically review authoritative references that materially support published Entries.

Maintenance may confirm:

- reference still resolves;
- identifier remains stable;
- owning institution remains clear;
- authoritative record has not been replaced;
- authority boundary remains correctly represented;
- Chronicle is not presenting a supporting artifact as the authoritative object.

The governing rule remains:

> Reference does not transfer authority.

---

# External Authoritative Changes

When another Suite institution changes its authoritative record, Chronicle must not automatically edit the existing Chronicle Entry.

Chronicle must first ask:

> Is Chronicle's existing historical representation wrong, or did something new happen?

This distinction controls the next action.

## If Chronicle's existing representation is wrong

Use:

```text
Correction
→ New Entry Version where material
→ Reverification
→ Revalidation
→ Publication Gate where publication is affected
→ Publication of resulting Version
```

## If a distinct later Occurrence happened

Use:

```text
New Occurrence
→ Preservation Eligibility
→ New Chronicle Entry
```

Examples of distinct later Occurrences may include:

- certification renewed;
- certification suspended;
- certification revoked;
- certification expired;
- new Registry action;
- material institutional decision;
- later preservation-significant Suite milestone.

Chronicle should not rewrite an earlier Entry merely because the authoritative system later changed state.

---

# Correction Test

Maintenance should trigger a Correction review when Chronicle discovers that its own record contains a material defect.

Potential triggers include:

- wrong Event Date;
- wrong Event Type;
- wrong authoritative reference;
- materially incomplete Historical Context;
- incorrect Relationship;
- incorrect Provenance;
- materially wrong limitation;
- mischaracterized authority;
- machine-readable value inconsistent with the human-readable representation;
- published representation inconsistent with the reviewed Entry Version.

The governing test is:

> Would a future reviewer reasonably need to know that Chronicle previously represented this differently?

If yes, formal Correction and/or Version lineage should be considered.

---

# Editorial Update Test

A simple Editorial Update may be sufficient when historical or institutional meaning does not change.

Examples may include:

- spelling;
- punctuation;
- formatting;
- accessibility text;
- layout;
- broken-link repair where identity is unchanged;
- reciprocal link addition;
- navigation improvement;
- non-substantive explanatory wording.

Editorial maintenance must not be used to conceal substantive change.

---

# Entry Version Test

A new Entry Version should ordinarily be created when the same canonical Entry remains correct in identity but its preserved representation changes materially.

Examples:

- corrected Event Date;
- materially changed Historical Context;
- changed authoritative reference;
- changed material Relationship;
- changed Provenance;
- new material limitation;
- material classification correction;
- substantive correction affecting future interpretation.

The Entry identifier remains stable.

Conceptually:

```text
Same Occurrence
Same Chronicle Entry identity
Material Chronicle change
        ↓
New Entry Version
```

---

# New Entry Test

A new Chronicle Entry should ordinarily be created when a distinct qualifying Occurrence happens.

Conceptually:

```text
Distinct qualifying Occurrence
        ↓
Preservation Eligibility
        ↓
New CHR identifier
```

Maintenance must not collapse multiple Occurrences into one Entry merely because they involve the same external record or institution.

---

# Verification During Maintenance

Routine maintenance does not automatically require Reverification.

Reverification should be considered when maintenance affects:

- historical meaning;
- Event Date;
- Event Type;
- authoritative references;
- material Sources or Evidence;
- Provenance;
- Relationships;
- limitations;
- classification;
- Correction lineage;
- material public representation.

A material Correction should ordinarily trigger Reverification.

---

# Validation During Maintenance

Routine technical maintenance does not automatically require full Revalidation.

Revalidation should be considered when:

- a new Entry Version is created;
- machine-readable content changes materially;
- required fields change;
- Controlled Values change materially;
- authoritative-reference structure changes;
- Provenance changes;
- Relationship semantics change;
- a Correction affects validated content;
- an applicable schema or Event-Type Profile requires it.

When Revalidation occurs, it applies to the exact Entry Version under review.

---

# Publication Gate During Maintenance

A new Publication Gate decision should be considered when maintenance results in a new or materially changed Entry Version intended for public production use.

The sequence remains:

```text
Reverification where required
        ↓
Revalidation
        ↓
CHR-VAL-011 Publication Readiness
        ↓
Publication Gate
        ↓
APPROVED / WITHHELD
        ↓
Publication
```

The rule remains:

> CHR-VAL-011 tests readiness. The Publication Gate makes the institutional decision.

---

# Publication State Maintenance

Maintenance should confirm that Publication State remains accurate.

Approved Publication States are:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Maintenance may identify conditions requiring withdrawal or later republication.

Withdrawal must not erase historical publication lineage.

---

# Lifecycle State Maintenance

Maintenance should also review whether Lifecycle State remains accurate.

Approved Lifecycle States are:

```text
draft
active
superseded
withdrawn
preserved
```

Lifecycle State remains distinct from:

- Verification State;
- Validation result;
- Publication State;
- external authority status.

Chronicle should not create a generic Entry Status that collapses these systems.

---

# Reciprocal Suite Reference Maintenance

Chronicle may maintain reciprocal references across Suite institutions where those references improve durable discovery.

Examples may include:

```text
Atlas
↔ Certifier
↔ Registry
↔ Chronicle
```

Maintenance should confirm that reciprocal references:

- still resolve;
- identify the correct record;
- preserve authority boundaries;
- do not imply ownership transfer;
- do not convert discovery links into authority claims.

Reciprocal links may be added editorially when they do not change historical meaning.

---

# Broken Reference Procedure

When a referenced resource no longer resolves:

1. Confirm whether the failure is temporary.
2. Confirm whether the authoritative object moved.
3. Identify a new canonical location if available.
4. Preserve the original identifier where stable.
5. Use an archive reference where appropriate.
6. Record material limitations when the source is no longer directly accessible.
7. Determine whether the change is editorial or substantive.
8. Escalate to Correction / Versioning when historical meaning or authority traceability changes materially.

Chronicle should not silently substitute a different object merely because the original link fails.

---

# Human / Machine Consistency Review

Maintenance should periodically compare the canonical human-readable and machine-readable representations.

At minimum, review consistency of:

- Entry identifier;
- Entry Version;
- schema identity;
- schema version;
- title;
- summary;
- Event Type;
- Event Date;
- authoritative references;
- Relationships;
- Provenance;
- Verification State;
- Lifecycle State;
- Publication State;
- `entry_created_at`;
- `published_at`;
- limitations where applicable.

A discrepancy should be investigated before either representation is silently changed.

---

# Procedural Artifact Maintenance

Durable Entry-Version procedural artifacts may include:

```text
CHR-YYYY-NNNN-vN-validation.md
CHR-YYYY-NNNN-vN-publication-gate.md
```

These artifacts preserve historical review state.

They should not be rewritten after the fact merely to reflect later conditions.

For example:

- a Publication Gate artifact created before publication may correctly state that publication had not yet occurred;
- later publication does not make that historical statement defective;
- a later review should be recorded through a new maintenance, Correction, Validation, or Version artifact where justified.

Historical procedural records should preserve what was true at the time they were created.

---

# Maintenance Record

Routine maintenance does not require creation of a new canonical Chronicle object.

Where useful, Chronicle may preserve a lightweight maintenance record or journal note documenting:

```text
Entry reviewed
Review date
Review scope
Issues found
Actions taken
Whether Correction was required
Whether Versioning was required
Whether Reverification was required
Whether Revalidation was required
Whether Publication Gate review was required
```

A maintenance record should not receive a CHR identifier merely because maintenance occurred.

If maintenance reveals a distinct Preservation-Eligible Occurrence, that Occurrence should be evaluated separately for a new Chronicle Entry.

---

# Recommended Review Cadence

Chronicle may perform maintenance:

- after material external authority changes;
- after schema changes;
- after Controlled Value changes;
- after reported broken references;
- after identified representation defects;
- after Corrections;
- after Entry Version changes;
- after major Suite interoperability changes;
- periodically as part of institutional review.

The procedure does not require every Entry to be re-reviewed on an arbitrary fixed schedule.

Risk, change, and institutional significance should guide maintenance frequency.

---

# Maintenance Outcomes

A maintenance review should result in one of the following outcomes:

## No Action Required

The Entry remains accurate, resolvable, internally consistent, and appropriately published.

## Editorial Maintenance

A non-substantive technical or presentation update is applied.

## Reference Maintenance

A reference is repaired or updated without changing underlying identity or historical meaning.

## Correction Required

Chronicle's existing representation contains a material defect.

## New Entry Version Required

The same canonical Entry requires a materially changed preserved state.

## New Occurrence Review Required

A distinct later event may qualify for Preservation Eligibility and a new Chronicle Entry.

## Publication Review Required

Publication State or a new public Entry Version requires Publication Gate review.

## Withdrawal Review Required

The public Entry Version may need to be withdrawn from active publication while preserving historical lineage.

---

# First Production Maintenance Baseline

The first production Chronicle Entry is:

```text
CHR-2026-0001
```

It preserves the July 5, 2026 creation of:

```text
SC-CERT-2026-0001
```

and references:

```text
SREG-2026-0001
```

The first production Entry established:

```text
Entry Version: 1
Verification: verified
Validation: PASS
Publication Gate: APPROVED
Publication State: published
Lifecycle State: active
```

Its production package includes:

```text
/chronicle/entries/CHR-2026-0001/
├── index.html
├── record.json
├── README.md
├── CHR-2026-0001-v1-validation.md
└── CHR-2026-0001-v1-publication-gate.md
```

Maintenance of this Entry should preserve the original August 22, 2026 production lineage.

Routine cross-link additions, documentation reconciliation, or non-material presentation changes should not silently alter:

```text
entry_version
published_at
Validation result
Publication Gate decision
```

unless the governing condition actually changes.

---

# Maintenance Decision Tree

Use the following decision sequence:

```text
Condition discovered
        ↓
Does it change historical or institutional meaning?
        ↓
No ─────────────→ Editorial / Technical Maintenance
        ↓ Yes
Is Chronicle's existing representation wrong?
        ↓
Yes ─────────────→ Correction Review
        ↓
Does material change require a new Entry Version?
        ↓
Yes ─────────────→ New Entry Version
        ↓
Reverification / Revalidation / Publication Gate as required
```

If Chronicle's existing representation is not wrong:

```text
Did a distinct later Occurrence happen?
        ↓
Yes
        ↓
Preservation Eligibility
        ↓
New Chronicle Entry if eligible
```

---

# Authority Boundary

Maintenance does not authorize Chronicle to change another institution's record.

Chronicle may update its references to reflect another institution's governed action.

Examples:

- Certifier changes certification lifecycle state.
- Registry updates a SREG.
- Atlas changes its canonical jurisdiction record.
- Anchor publishes a new Integrity Reference.
- Beacon publishes new Discovery Metadata.
- Attestor issues a new Trust Statement.
- Navigator changes a Workflow Definition.

Chronicle must preserve the distinction between:

```text
external authoritative change
```

and:

```text
Chronicle correction
```

The governing rule remains:

> Reference does not transfer authority.

---

# Preservation Requirements

Maintenance must protect long-term historical continuity.

Chronicle should preserve:

- canonical identifiers;
- prior substantive Entry states;
- Correction rationale;
- Entry Version lineage;
- original schema association;
- authoritative reference history where material;
- historical Publication State;
- withdrawal history;
- procedural review artifacts;
- material limitations;
- relationship history where institutionally significant.

Superseded or withdrawn historical information should not disappear merely because a newer public state exists.

---

# Prohibited Maintenance Behavior

Chronicle maintenance must not:

- silently rewrite substantive history;
- overwrite prior material Entry Versions;
- replace an authoritative object with a different object without review;
- reinterpret a later external event as though it had always been true;
- reset `published_at` for routine editorial maintenance;
- convert Validation PASS into retroactive Publication Gate approval;
- rewrite historical Publication Gate artifacts after publication;
- create unnecessary Source, Evidence, Verification, Validation, or Maintenance objects merely for symmetry;
- create new CHR identifiers for routine maintenance;
- collapse distinct state systems into generic status;
- manufacture causal Relationships from chronology alone.

---

# Design Principles

## Maintain Without Erasing

Technical and institutional maintenance should preserve historical continuity.

## Correct Forward

Material defects are corrected visibly.

## Preserve Backward

Prior substantive states remain reviewable.

## External Change Is Not Automatically a Correction

A later authoritative action may be a new Occurrence.

## Revalidate the Exact Version

Validation applies to the Entry Version under review.

## Publication Remains a Separate Decision

Validation readiness does not itself authorize publication.

## Minimum Necessary Structure

Do not create supporting records merely because the architecture allows them.

## Authority Remains External

Chronicle maintains references without absorbing authority.

---

# Guiding Principle

> Maintain the record without erasing the record.

And operationally:

> Correct forward. Preserve backward. Distinguish correction from new history.

---

## Status

**Operational Chronicle Maintenance Procedure.**

This procedure governs post-publication maintenance of Chronicle Entries and associated Chronicle-owned artifacts.

It is aligned with:

- Chronicle Entry Model;
- Preservation Eligibility;
- Rules;
- Identifiers;
- Controlled Values;
- Relationships;
- Provenance;
- Sources and Evidence;
- Verification;
- Validation;
- Publication;
- Lifecycle;
- Versioning;
- Corrections;
- Historical Preservation;
- Suite authority boundaries.

The procedure should evolve only when production experience demonstrates a stable institutional need.
