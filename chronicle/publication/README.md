# Chronicle Publication

## Purpose

This directory defines and documents the publication architecture of Satoshium Chronicle.

Chronicle Publication is the institutional process through which a reviewed Chronicle Entry Version enters public production use through its canonical human-readable and machine-readable representations.

Publication is distinct from:

- Preservation Eligibility
- Verification
- Validation
- Publication Readiness
- Publication Gate approval
- Lifecycle State
- Versioning
- Corrections

The governing distinction is:

```text
Verification
≠
Validation
≠
Publication Gate
≠
Publication
```

And operationally:

> CHR-VAL-011 tests readiness. The Publication Gate makes the institutional decision.

---

# Directory Role

The public publication page is:

```text
/chronicle/publication/index.html
```

Its canonical public URI is:

```text
https://satoshium.us/chronicle/publication/
```

This README preserves the institutional and maintenance context for that page.

The Publication page explains:

- what Publication means in Chronicle;
- Publication prerequisites;
- Publication State;
- Validation and Publication Readiness;
- the separate Publication Gate;
- canonical public Entry representations;
- machine-readable publication;
- `published_at`;
- withdrawal from publication;
- Corrections and Versioning after publication;
- preservation of prior public states;
- authority boundaries;
- the first production publication precedent.

---

# Publication Sequence

Chronicle publication follows this sequence:

```text
Preservation Eligibility
        ↓
Chronicle Entry Created
        ↓
Authoritative References / Sources / Evidence / Provenance / Relationships
        ↓
Verification
        ↓
Validation
        ↓
CHR-VAL-011 — Publication Readiness
        ↓
Publication Gate
        ↓
APPROVED / WITHHELD
        ↓
Publication
        ↓
Maintenance / Correction / Versioning / Preservation
```

Each stage answers a different institutional question.

---

# Verification

Verification asks whether Chronicle has adequately reviewed its own historical representation.

Verification may examine:

- Entry identity;
- Event Date;
- Event Type;
- Historical Context;
- authoritative references;
- Sources;
- Evidence;
- Provenance;
- Relationships;
- limitations;
- temporal consistency.

Verification does not itself publish the Entry.

---

# Validation

Validation asks:

> Does this Chronicle Entry Version conform to the institutional and machine-readable requirements governing it?

Validation evaluates the exact Entry Version under review.

Chronicle Validation produces an overall:

```text
PASS
FAIL
```

Individual Validation rules may produce:

```text
PASS
FAIL
N/A
```

Validation does not itself authorize publication.

---

# CHR-VAL-011 — Publication Readiness

`CHR-VAL-011` is the final Validation-domain readiness test.

Its purpose is to determine whether the Entry Version is ready to proceed to the Publication Gate.

The rule is:

> CHR-VAL-011 tests readiness. The Publication Gate makes the institutional decision.

Therefore:

```text
CHR-VAL-011 PASS
≠
Publication approved
```

And:

```text
Validation PASS
≠
Publication approved
```

---

# Publication Gate

The Publication Gate is a separate institutional decision point.

It determines whether a Validation-ready Chronicle Entry Version is:

```text
APPROVED
```

or:

```text
WITHHELD
```

for publication.

The Publication Gate is not:

- a Validation rule;
- a universal Base Schema field;
- a separate canonical Chronicle object;
- a separate CHR identifier;
- an independent lifecycle system.

A durable Publication Gate artifact may be preserved for the exact Entry Version reviewed.

Recommended naming pattern:

```text
CHR-YYYY-NNNN-vN-publication-gate.md
```

---

# Publication State

Chronicle uses the following Publication State values:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

These values are governed independently from Lifecycle State, Verification State, and Validation result.

## `not_published`

The Entry Version has not entered public production use.

## `pending_publication`

The Entry Version is awaiting or completing the publication process.

## `published`

The Entry Version has been publicly released through its canonical representations.

## `withdrawn_from_publication`

The Entry Version is no longer presented as an active public production representation.

Withdrawal does not erase the historical fact that the Entry Version previously existed or was published.

---

# Canonical Publication Location

Published Chronicle Entries resolve beneath:

```text
/chronicle/entries/
```

Canonical Entry path pattern:

```text
/chronicle/entries/CHR-YYYY-NNNN/
```

The Entries collection remains Chronicle's public production collection.

Chronicle should not create a competing `/preserved-events/` collection unless future operational experience demonstrates a genuinely distinct need.

---

# Published Entry Representations

A production Chronicle Entry may include:

```text
index.html
record.json
README.md
```

These three files form the coordinated canonical Entry representation.

Where applicable, durable procedural artifacts may also be preserved:

```text
CHR-YYYY-NNNN-vN-validation.md
CHR-YYYY-NNNN-vN-publication-gate.md
```

The Validation and Publication Gate artifacts:

- apply to an exact Entry Version;
- preserve review history;
- do not become separate canonical Chronicle objects;
- do not receive separate CHR identifiers;
- do not replace the canonical Entry representation.

---

# Human-Readable and Machine-Readable Consistency

The human-readable and machine-readable representations of a Chronicle Entry describe the same canonical Chronicle object.

They must remain materially consistent.

A discrepancy between:

```text
index.html
record.json
```

should be treated as a Chronicle representation problem and corrected under the applicable maintenance, Correction, or Versioning rules.

---

# `published_at`

When:

```text
publication_state: published
```

the Chronicle Entry preserves:

```text
published_at
```

`published_at` records when the Entry Version entered public production use.

Later editorial maintenance, cross-link additions, or non-material presentation changes do not silently reset the original publication timestamp for that same Entry Version.

---

# Corrections After Publication

Publication does not prevent later Correction.

If Chronicle discovers that its own historical representation is materially wrong, incomplete, or misleading, the Corrections architecture applies.

The governing rule remains:

> Correct forward. Preserve backward.

Material Corrections may require:

```text
Prior state preserved
        ↓
Correction documented
        ↓
New Entry Version
        ↓
Reverification
        ↓
Revalidation
        ↓
Publication Gate
        ↓
Publication of resulting Version
```

A later external institutional action should not automatically be rewritten into an earlier Chronicle Entry.

Chronicle must first determine whether:

```text
the existing Entry is wrong
```

or:

```text
a new qualifying Occurrence happened
```

If the existing Chronicle representation is wrong:

```text
Correction / Versioning
```

If a distinct later qualifying Occurrence happened:

```text
New Chronicle Entry
```

---

# Withdrawal from Publication

Withdrawal from publication changes public presentation.

It does not erase historical lineage.

When an Entry Version is withdrawn, Chronicle should preserve enough information for future reviewers to determine:

- that the Entry Version existed;
- that it was previously published, if applicable;
- when withdrawal occurred;
- why withdrawal occurred;
- what later Version, Correction, or Entry replaced or superseded it, if applicable.

Withdrawal must not become silent historical deletion.

---

# Authority Boundary

Chronicle publishes Chronicle-owned historical-preservation records.

Publication does not transfer authority over referenced objects.

Examples:

- Certifier retains authority over Certification Packages and certification decisions.
- Registry retains authority over SREGs and Registry-controlled fields.
- Atlas retains authority over Atlas records and jurisdiction intelligence.
- Anchor retains authority over Integrity References.
- Beacon retains authority over Discovery Signals and metadata.
- Attestor retains authority over Attestations and Trust Statements.
- Navigator retains authority over Workflow Definitions.

The governing rule is:

> Reference does not transfer authority.

---

# First Production Publication

Chronicle's first production publication was:

```text
CHR-2026-0001
```

Entry Version:

```text
1
```

Occurrence:

```text
July 5, 2026 creation of SC-CERT-2026-0001
```

Event Type:

```text
certification_created
```

Authoritative record:

```text
SC-CERT-2026-0001
```

Related Registry Entry:

```text
SREG-2026-0001
```

Production review state:

```text
Verification: verified
Validation: PASS
CHR-VAL-011: PASS
Publication Gate: APPROVED
Publication State: published
```

Published at:

```text
2026-08-22T08:38:00-07:00
```

The first production publication established the operational sequence:

```text
Validation PASS
        ↓
CHR-VAL-011 PASS
        ↓
Publication Gate APPROVED
        ↓
Publication executed
```

---

# First Production Entry Package

The first published Entry package established the following production structure:

```text
/chronicle/entries/CHR-2026-0001/
├── index.html
├── record.json
├── README.md
├── CHR-2026-0001-v1-validation.md
└── CHR-2026-0001-v1-publication-gate.md
```

The first three files form the coordinated canonical Entry representation.

The Validation and Publication Gate files preserve procedural review history for Entry Version 1.

---

# Publication and Lifecycle

Publication State and Lifecycle State remain separate.

For example:

```text
lifecycle_state: active
publication_state: published
```

is valid.

A future Entry may also be:

```text
lifecycle_state: preserved
publication_state: published
```

or:

```text
lifecycle_state: withdrawn
publication_state: withdrawn_from_publication
```

depending on the governed circumstances.

Chronicle should not collapse these state systems into a generic Entry Status.

---

# Publication and Validation Artifacts

Validation artifacts and Publication Gate artifacts are durable procedural records associated with an Entry Version.

They support:

- reviewability;
- auditability;
- institutional accountability;
- publication lineage;
- future maintenance;
- Correction and Version reconstruction.

They do not create new canonical record classes merely because they are durable.

---

# Publication Maintenance

Published Chronicle Entries should be maintained over time.

Maintenance may include reviewing:

- broken authoritative references;
- missing or changed external resources;
- machine-readable representation consistency;
- schema compatibility;
- Controlled Value changes;
- Correction requirements;
- Version lineage;
- reciprocal Suite references;
- publication-state accuracy;
- historical continuity.

Maintenance should not silently alter historical meaning.

---

# Design Principles

## Publication Is a Separate Institutional Act

Validation readiness does not equal publication approval.

## Validation Comes Before the Gate

The exact Entry Version must conform before the Publication Gate is evaluated.

## The Gate Decides

The Publication Gate makes the institutional approval decision.

## Publication Changes Public State

Publication records that the approved Entry Version has entered public production use.

## Preserve the Lineage

Later Corrections, Versions, withdrawals, and maintenance must not erase prior substantive public states.

## Reference, Do Not Absorb

Publishing a Chronicle Entry does not transfer authority over referenced Suite objects.

---

# Guiding Principle

> Validate the representation. Approve the release. Publish the Entry. Preserve the lineage.

---

## Status

**Operational Chronicle Publication architecture.**

The Publication architecture has been exercised through the first canonical production Chronicle Entry, `CHR-2026-0001`.

Chronicle now distinguishes:

```text
Verification
Validation
Publication Readiness
Publication Gate
Publication State
```

as separate institutional concepts.

The first production precedent confirms:

```text
CHR-VAL-011 tests readiness.
The Publication Gate makes the institutional decision.
Publication changes the public production state.
```
