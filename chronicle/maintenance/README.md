# Chronicle Maintenance

## Purpose

This directory contains the public and institutional artifacts governing post-publication maintenance of Satoshium Chronicle Entries.

Canonical public route:

```text
https://satoshium.us/chronicle/maintenance/
```

Directory:

```text
/chronicle/maintenance/
```

---

# Files

```text
/chronicle/maintenance/
├── index.html
├── README.md
└── chronicle-maintenance-procedure.md
```

## `index.html`

Public explanation of Chronicle Maintenance.

It summarizes:

- post-publication maintenance;
- technical maintenance;
- reference maintenance;
- representation consistency;
- schema and Controlled Value maintenance;
- external authority changes;
- Correction and Version tests;
- new Occurrence handling;
- Reverification and Revalidation triggers;
- Publication maintenance;
- reciprocal Suite references;
- the first production maintenance baseline.

## `README.md`

Institutional directory documentation.

This file explains the purpose, responsibilities, boundaries, and maintenance expectations of the directory.

## `chronicle-maintenance-procedure.md`

The governing operational procedure.

It defines how Chronicle reviews and responds to post-publication conditions affecting published Chronicle Entries and associated Chronicle-owned artifacts.

---

# Institutional Role

Maintenance begins after publication.

Conceptually:

```text
Chronicle Entry
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
Correction / Versioning / New Occurrence where required
        ↓
Historical Preservation
```

Maintenance is not another canonical Chronicle object.

Maintenance is an institutional process applied to existing Chronicle records.

---

# Governing Principles

The core maintenance principles are:

> Maintain the record without erasing the record.

> Correct forward. Preserve backward.

> Distinguish correction from new history.

And across Suite references:

> Reference does not transfer authority.

---

# Maintenance Boundary

Routine maintenance may address:

- technical defects;
- broken references;
- changed URLs;
- representation inconsistencies;
- schema compatibility;
- Controlled Value changes;
- reciprocal links;
- public presentation;
- accessibility;
- documentation;
- historical preservation needs.

Maintenance must not silently alter substantive historical meaning.

If substantive meaning changes, Chronicle must evaluate whether the correct response is:

```text
Correction
```

```text
New Entry Version
```

or:

```text
New Preservation-Eligible Occurrence
```

---

# Correction vs. New History

The central maintenance question is:

> Is Chronicle's existing representation wrong, or did something new happen?

If Chronicle is wrong:

```text
Correction
→ New Entry Version where material
→ Reverification
→ Revalidation
→ Publication Gate where required
→ Publication of resulting Version
```

If Chronicle remains historically correct and a distinct later Occurrence happened:

```text
New Occurrence
→ Preservation Eligibility
→ New Chronicle Entry if eligible
```

Chronicle should not rewrite later history into an earlier Entry.

---

# Procedural Artifact Preservation

Historical procedural artifacts must preserve what was true at the time they were created.

Examples include:

```text
CHR-YYYY-NNNN-vN-validation.md
CHR-YYYY-NNNN-vN-publication-gate.md
```

A Publication Gate artifact created before publication may correctly state that publication had not yet occurred.

Later publication does not make that historical statement incorrect.

Historical review artifacts should not be rewritten merely to reflect later conditions.

---

# First Production Maintenance Baseline

The first production maintenance baseline is:

```text
CHR-2026-0001
```

Current established production state:

```text
Entry Version: 1
Lifecycle State: active
Verification State: verified
Validation Result: PASS
Publication Gate: APPROVED
Publication State: published
```

Routine post-publication cross-link additions, documentation reconciliation, and non-material presentation changes do not automatically require:

- a new Entry Version;
- Reverification;
- Revalidation;
- a new Publication Gate decision;
- a changed `published_at`.

---

# Relationship to Publication

Publication determines when an approved Entry Version enters public production use.

Maintenance determines how that published Entry is kept durable and institutionally accurate afterward.

Publication route:

```text
/chronicle/publication/
```

Maintenance route:

```text
/chronicle/maintenance/
```

The two functions are related but distinct.

---

# Relationship to Corrections and Versioning

Maintenance may identify a need for Correction or Versioning.

Maintenance does not replace either architecture.

Related routes:

```text
/chronicle/corrections/
/chronicle/versioning/
```

The governing distinction is:

```text
Correction
= why Chronicle changed its record

Version
= resulting preserved state
```

---

# Relationship to Historical Preservation

Maintenance protects the continuity required for long-term historical preservation.

It helps ensure that:

- prior substantive states remain reconstructable;
- authoritative references remain traceable;
- withdrawn or superseded states do not silently disappear;
- Corrections remain visible;
- Version lineage remains understandable;
- publication lineage remains reviewable.

Related route:

```text
/chronicle/historical-preservation/
```

---

# Authority Boundary

Maintenance applies to Chronicle-owned records and representations.

It does not authorize Chronicle to modify:

- Certification Packages;
- SREG Registry Entries;
- Atlas records;
- Anchor Integrity References;
- Beacon Discovery Signals;
- Attestor Trust Statements;
- Navigator Workflow Definitions;
- other externally authoritative objects.

Chronicle may update its own references when those external objects change.

It must preserve the distinction between an external authoritative change and a Chronicle Correction.

---

# Maintenance Outcomes

A maintenance review may result in:

```text
No Action Required
Editorial Maintenance
Reference Maintenance
Correction Required
New Entry Version Required
New Occurrence Review Required
Publication Review Required
Withdrawal Review Required
```

Not every review produces a new artifact.

Minimum necessary structure remains the governing approach.

---

# Status

**Operational Chronicle Maintenance directory.**

The directory contains:

- a public Maintenance explanation;
- institutional directory documentation;
- the governing Chronicle Maintenance Procedure.

Maintenance is now a defined post-publication Chronicle function and should evolve only when production experience demonstrates a stable need.
