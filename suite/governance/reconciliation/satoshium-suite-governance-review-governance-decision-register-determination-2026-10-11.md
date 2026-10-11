# Satoshium Suite Governance Review — Governance Decision Register Determination

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 3 of 4 — Governance Process, Decisions, Versioning & Accountability  
**Step:** 11 — Determine Whether the Suite Needs a Formal Governance Decision Register  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record determines whether the Satoshium Suite requires a formal **Governance Decision Register**.

The Governance Review has already established:

- a standard governance decision lifecycle;
- governance decision roles and decision rights;
- review escalation thresholds;
- governance versioning;
- supersession rules;
- correction procedures;
- a Governance Decision Record (GDR) model;
- minimum required GDR fields.

The remaining question is whether those individual decision records should also be indexed in a formal Suite-level register.

---

# Determination

# YES.

The Satoshium Suite should maintain a formal **Governance Decision Register**.

The reason is structural:

> **Governance Decision Records preserve individual decisions. The Governance Decision Register preserves the discoverability, continuity, status, and relationship of those decisions as a governed body of record.**

Without a register, the Suite could possess valid GDRs while still making it difficult to determine:

- which decisions currently govern;
- which have been superseded;
- which remain pending;
- which are constitutional;
- which institutions are affected;
- which decisions relate to a particular canonical object;
- which decisions changed prior governance;
- which decisions remain unresolved or under implementation.

The Register therefore serves as the authoritative index of formal governance decisions.

---

# I. Governance Decision Record vs. Governance Decision Register

The distinction is:

```text
GDR
→ authoritative record of one governance decision

Governance Decision Register
→ authoritative index of governance decisions
```

Therefore:

```text
RECORD
≠
REGISTER
```

The Register does not replace the GDR.

The GDR does not replace the Register.

---

# II. Why the Register Is Needed

## 1. Current-State Visibility

The Register should make it possible to identify:

```text
CURRENT
SUPERSEDED
REJECTED
WITHDRAWN
PENDING
IMPLEMENTATION IN PROGRESS
```

without opening every GDR individually.

---

## 2. Decision Lineage

The Register should expose relationships such as:

```text
GDR-2026-0001
→ superseded by GDR-2027-0004
```

This supports governance continuity.

---

## 3. Constitutional Traceability

The Suite now distinguishes:

```text
Routine
Material
Constitutional
```

The Register allows Constitutional decisions to remain immediately discoverable as a distinct governance class.

---

## 4. Institutional Accountability

The Register can show which institutions were affected by each decision.

This supports:

- accountability;
- review;
- institutional history;
- architecture analysis.

---

## 5. Canonical-Object Traceability

Because Governance Decisions may affect canonical objects, the Register should expose which objects were governed.

This enables questions such as:

```text
Which governance decisions have affected SREG?

Which decisions have affected Trust Statement authority?

Which decisions changed Certification Package governance?
```

---

## 6. Supersession Control

A Register makes it much harder for outdated governance to remain accidentally treated as current.

It provides a current-state pointer.

Therefore:

> **The Register reduces governance ambiguity by making operative standing visible.**

---

## 7. Correction Visibility

Material corrections should be discoverable through the Register.

This prevents corrected or superseded governance from appearing silently unchanged.

---

## 8. Reviewability

A Governance Decision Register gives reviewers a bounded starting point for:

- governance audits;
- architecture reconciliation;
- interoperability review;
- documentation reconciliation;
- future constitutional review.

---

# III. Scope of the Register

The formal Governance Decision Register should include:

```text
Material Governance Decisions
Constitutional Governance Decisions
selected Routine Governance Decisions where long-term traceability is warranted
```

Not every trivial operational decision needs a formal Register entry.

The governing threshold is:

> **If the decision materially affects governance history, authority, institutional behavior, canonical objects, interoperability, or constitutional structure, it belongs in the Register.**

---

# IV. Required Register Fields

Each Register entry should contain at minimum:

```text
Decision ID
Decision Date
Title / Subject
Classification
Decision Type
Affected Institution(s)
Affected Canonical Object(s)
Status
Effective State
Version
Supersedes
Superseded By
GDR Location
```

Strongly recommended additional fields:

```text
Approval Authority
Effective Date
Implementation Status
Correction Status
Related GDRs
Preservation Location
```

---

# V. Recommended Register Structure

A concise tabular register may use:

| Decision ID | Date | Subject | Classification | Institutions | Canonical Objects | Status | Effective State | Supersession |
|---|---|---|---|---|---|---|---|---|

Each row should link to the full Governance Decision Record.

The Register itself should remain lightweight.

Detailed reasoning belongs in the GDR.

---

# VI. Register Status Model

Recommended decision-status values:

```text
PROPOSED
UNDER REVIEW
DETERMINED
APPROVED
PUBLISHED
EFFECTIVE
IMPLEMENTATION IN PROGRESS
IMPLEMENTED
SUPERSEDED
REJECTED
WITHDRAWN
ARCHIVED
```

The Register should identify one current status for each decision.

---

# VII. Register Authority

The Governance Decision Register is a **Suite governance artifact**.

It does not create authority independently.

It records the status of Governance Decisions issued under valid authority.

Therefore:

```text
REGISTER ENTRY
≠
GOVERNANCE DECISION
```

and:

```text
GDR
→ establishes the Decision

REGISTER
→ indexes and exposes the Decision
```

---

# VIII. Register Maintenance

The Register should be updated when a GDR is:

- approved;
- published;
- made effective;
- implemented;
- corrected;
- superseded;
- withdrawn;
- archived.

The update must preserve prior decision history.

The Register should not delete prior entries simply because they are no longer current.

---

# IX. Historical Preservation

The Register itself should be versioned or preserved over time.

This allows later reviewers to reconstruct:

```text
what the Register showed
at a prior point in Suite history
```

However, the current Register should always identify the current operative standing of each GDR.

---

# X. Relationship to the Existing Reconciliation Decision Register

The completed Suite Reconciliation already demonstrated the value of a formal Decision Register for a bounded review process.

That precedent supports adoption of a permanent Governance Decision Register.

The distinction should remain:

```text
Suite Reconciliation Decision Register
→ records decisions from the completed reconciliation process

Governance Decision Register
→ ongoing formal register of governance decisions after reconciliation
```

The former is historical and review-specific.

The latter is persistent and operational.

---

# XI. Recommended Repository Location

Recommended location:

```text
suite/governance/decision-register.md
```

or, if a dedicated governance record structure is adopted:

```text
suite/governance/decisions/README.md
```

with individual GDRs under:

```text
suite/governance/decisions/
```

A later implementation decision may determine the final repository layout.

The present Governance Review establishes the requirement for the Register, not the final file-system implementation.

---

# XII. Governing Doctrine

> **A Governance Decision Record preserves the decision. A Governance Decision Register preserves the governance system's ability to find, relate, and understand those decisions over time.**

Expanded:

> **The Suite requires a formal Governance Decision Register because governance accountability depends not only on preserving individual decisions, but also on maintaining a durable current-state index of their classification, status, affected subjects, and supersession relationships.**

---

## Final Disposition

```text
Formal Governance Decision Register needed?
→ YES

Register scope
→ Material + Constitutional + selected significant Routine decisions

Register authority
→ index only; does not independently create governance authority

Current-state visibility
→ REQUIRED

Supersession visibility
→ REQUIRED

Affected-institution visibility
→ REQUIRED

Canonical-object visibility
→ REQUIRED

Historical preservation
→ REQUIRED

Relationship to GDRs
→ DEFINED

Relationship to Reconciliation Decision Register
→ DEFINED

Governance Decision Register
→ REQUIRED

Governance Decision Register Determination
→ COMPLETE — APPROVED
```

# GOVERNANCE DECISION REGISTER — REQUIRED — COMPLETE — APPROVED
