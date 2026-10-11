# Satoshium Suite Governance Review — Supersession of Governance Decisions

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 3 of 4 — Governance Process, Decisions, Versioning & Accountability  
**Step:** 7 — Define Supersession of Governance Decisions Without Erasing the Prior Record  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record defines how a later governance decision may **supersede** an earlier governance decision without erasing, mutating, or falsifying the prior record.

The governing objective is:

> **Allow current governance authority to change while preserving an accurate record of what governed before.**

This preserves the settled Suite distinction:

```text
SUPERSESSION ≠ MUTATION
```

and the broader preservation principle:

> **Change prospectively. Preserve retrospectively.**

---

# I. Definition

**Supersession** is:

> **The governed replacement of a prior decision's current operative standing by a later approved governance decision, while preserving the prior decision as an intact historical record.**

Supersession changes:

```text
what governs now
```

It does not change:

```text
what governed before
```

---

# II. Core Supersession Rule

The governing rule is:

```text
PRIOR DECISION
→ remains historically valid for its effective period

NEW DECISION
→ becomes controlling prospectively

RELATIONSHIP
→ SUPERSEDES
```

Therefore:

```text
NEW DECISION
≠ rewritten old decision
```

and:

```text
SUPERSEDED
≠ DELETED
```

---

# III. When Supersession Is Required

A new governance decision should supersede a prior decision when the later decision materially changes the operative governance state.

Examples include:

- changed policy conclusion;
- changed governance interpretation;
- changed approval model;
- changed Standard requirement;
- changed Methodology requirement;
- changed institutional governance rule;
- changed canonical-object treatment;
- changed authority allocation;
- changed membership state;
- changed constitutional structure.

If the substantive conclusion changes:

```text
NEW GOVERNANCE DECISION REQUIRED
```

The prior decision must not simply be edited in place.

---

# IV. Supersession vs. Correction

Supersession and correction are distinct.

## Correction

A Correction repairs an error in the prior record.

Example:

```text
incorrect date
incorrect reference
non-substantive wording defect
```

The corrected record may retain the same underlying governance conclusion.

## Supersession

Supersession replaces the operative conclusion.

Example:

```text
Prior Decision:
Institution A owns Object X

Later Decision:
Institution B owns Object X prospectively
```

That is not a correction of the old decision.

It is a new decision that supersedes the earlier governance state.

Therefore:

```text
CORRECTION
→ repairs record

SUPERSESSION
→ replaces operative governance state
```

---

# V. Supersession vs. Amendment

An amendment modifies an existing governance instrument.

An amendment may produce:

- a new version of the same instrument;
- a new Decision if substantive meaning changes.

If the amendment changes a substantive governance conclusion, authority, obligation, or constitutional state:

```text
AMENDMENT
→ new governance decision
→ supersession relationship
```

A purely clarifying or non-substantive amendment may not require supersession.

---

# VI. Required Supersession Record

Every formal supersession should record:

```text
New Decision ID:
Prior Decision ID:
Relationship:
→ supersedes

Reason for Supersession:
Governed Subject:
Change Classification:
Approval Authority:
Decision Date:
Publication Date:
Effective Date:
Prior Decision Effective Period:
Implementation Requirements:
Compatibility / Transition Requirements:
Historical Preservation Location:
```

The record should make it possible to answer:

```text
What governed?
When did it govern?
What replaced it?
Why was it replaced?
When did the replacement take effect?
```

---

# VII. Effective-Date Rule

Supersession becomes operative on the approved **Effective Date**.

Before that date:

```text
Prior Decision
→ remains controlling
```

On and after that date:

```text
New Decision
→ becomes controlling
```

Therefore:

```text
Approval Date
≠ necessarily Supersession Effective Date
```

A future-effective supersession is valid.

The prior decision remains operative until the later decision takes effect.

---

# VIII. Historical Validity

A superseded governance decision remains historically valid for the period during which it governed.

This means later readers must be able to reconstruct:

- what authority existed;
- which rule applied;
- which version was current;
- which decision controlled;
- what implementation was legitimate at that time.

Therefore:

> **Supersession changes current authority, not historical truth.**

---

# IX. No Retroactive Rewrite Rule

A later decision must not rewrite the earlier decision to make it appear that the later rule always existed.

Prohibited practices include:

- editing the old decision's conclusion after supersession;
- replacing the old file without preserving it;
- changing historical effective dates to match the new decision;
- altering historical authority assignments;
- updating old records so they falsely reflect current architecture;
- deleting prior disagreement or prior governance states.

The old record may receive metadata such as:

```text
Status: SUPERSEDED

Superseded By: GDR-XXXX

Supersession Effective Date: YYYY-MM-DD
```

but its historical substantive content should remain intact.

---

# X. Superseded Decision Status

A superseded decision should carry an explicit status:

```text
SUPERSEDED
```

It should also identify:

```text
Superseded By
→ later Decision ID

Effective Until
→ date immediately before supersession takes effect
```

where appropriate.

The later decision should identify:

```text
Supersedes
→ prior Decision ID
```

This creates a bidirectional historical chain.

---

# XI. Supersession Chain

Governance may evolve through multiple successive decisions.

Example:

```text
GDR-001
→ superseded by GDR-014

GDR-014
→ superseded by GDR-027

GDR-027
→ current
```

The entire chain should remain discoverable.

This supports:

- auditability;
- historical reconstruction;
- implementation analysis;
- architecture history;
- accountability.

---

# XII. Partial Supersession

A later decision may supersede only part of an earlier decision.

When this occurs, the record must identify the exact affected portion.

Example:

```text
GDR-010
Sections 1–3
→ remain controlling

Section 4
→ superseded by GDR-022
```

Partial supersession must not create ambiguity about which provisions remain effective.

The preferred rule is:

> **Supersession scope must be explicit.**

---

# XIII. Complete Supersession

A complete supersession occurs when the later decision replaces the entire operative governance effect of the earlier decision.

Example:

```text
GDR-010
→ fully superseded by GDR-022
```

The prior decision remains preserved, but no part remains currently controlling unless explicitly stated.

---

# XIV. Constitutional Supersession

Constitutional decisions may be superseded only through a valid Constitutional governance process.

Examples include:

- Suite membership changes;
- institutional creation or removal;
- canonical ownership transfer;
- institutional-role reassignment;
- merger;
- division;
- retirement;
- successor replacement.

A Routine or Material process may not supersede a Constitutional decision.

Therefore:

```text
GOVERNANCE LEVEL OF SUPERSEDING DECISION
≥
GOVERNANCE LEVEL REQUIRED FOR SUBJECT
```

---

# XV. Institutional Supersession

Institution-level decisions may be superseded by the owning institution when the subject remains within settled institutional authority.

Examples:

```text
Policy V1
→ superseded by Policy V2

Procedure A
→ superseded by Procedure B
```

If the replacement crosses into Suite-level or Constitutional effect, escalation is required before supersession may occur.

---

# XVI. Supersession and Implementation

A new governance decision may be approved before implementation is complete.

Therefore:

```text
New Decision
→ APPROVED

Supersession Effective Date
→ may be future

Implementation
→ transition may occur before or after approval
```

The record must make clear when the new governance state becomes controlling.

Implementation delay does not justify silent coexistence.

If temporary coexistence is required, it must be explicitly authorized.

---

# XVII. Supersession and Publication

Publication should make the supersession visible.

The current governance surface should identify the new controlling decision.

The prior surface or archived record should identify that it is superseded.

Recommended linkage:

```text
Current Decision
→ Supersedes: GDR-XXXX

Prior Decision
→ Status: Superseded
→ Superseded By: GDR-YYYY
```

This ensures that neither current nor historical readers are misled.

---

# XVIII. Supersession and Versioning

Supersession may occur between:

- versions of the same governance instrument;
- separate Governance Decision Records;
- different constitutional states;
- replacement Standards;
- replacement policies.

The governing distinction is:

```text
VERSION
→ identifies edition

SUPERSESSION
→ identifies operative replacement relationship
```

A new version may or may not supersede the prior version depending on the approved effective-state model.

---

# XIX. Supersession and Preservation

The preservation requirement is absolute for formally published governance decisions.

At minimum, preserve:

```text
Prior Decision
New Decision
Supersession relationship
Effective dates
Approval record
Version history
Implementation transition
Correction history
```

The controlling preservation rule is:

> **A superseded decision leaves the current state but never leaves the governance history.**

---

# XX. Supersession and Reconciliation

Supersession does not erase the validity of the prior Reconciliation record.

If future Governance legitimately changes settled architecture:

```text
Reconciled Architecture A
→ preserved historically

Governance Decision B
→ explicitly supersedes affected architectural state

Architecture B
→ current prospectively
```

The Reconciliation remains accurate for the period and architecture it documented.

---

# XXI. Invalid Supersession

A claimed supersession is invalid if:

- the later decision lacks proper authority;
- required review did not occur;
- required approval did not occur;
- the scope is unclear;
- the prior decision is silently overwritten;
- the constitutional level is insufficient;
- effective date is undefined where necessary;
- the relationship is merely inferred from implementation.

In that case:

```text
Prior valid Decision
→ remains controlling
```

until a valid governance action occurs.

---

# XXII. Supersession Decision Test

Before marking a governance decision superseded, confirm:

```text
1. Is there a later approved decision?
2. Does the later decision govern the same subject?
3. Does it materially replace the prior operative state?
4. Was it approved at the correct governance level?
5. Is supersession explicit?
6. Is scope explicit?
7. Is the effective date explicit?
8. Is the prior record preserved?
9. Is the relationship bidirectionally traceable?
10. Are transition / implementation effects documented?
```

If any critical answer is NO:

```text
DO NOT MARK SUPERSEDED
```

---

# Governing Doctrine

> **Supersession replaces current operative authority without rewriting historical authority.**

Expanded:

> **A later approved governance decision may become controlling prospectively, but the prior decision must remain intact, identifiable, dated, attributable, and linked to its successor. Supersession changes what governs now; it does not change what governed before.**

---

## Final Disposition

```text
Governance Supersession
→ DEFINED

Supersession / Mutation distinction
→ PRESERVED

Supersession / Correction distinction
→ PRESERVED

Partial supersession
→ DEFINED

Complete supersession
→ DEFINED

Effective-date rule
→ ESTABLISHED

Historical-validity rule
→ ESTABLISHED

Bidirectional linkage
→ REQUIRED

Constitutional supersession boundary
→ ESTABLISHED

Silent overwrite
→ PROHIBITED

Prior record preservation
→ REQUIRED

Governance Decision Supersession
→ COMPLETE — APPROVED
```

# GOVERNANCE DECISION SUPERSESSION — COMPLETE — APPROVED
