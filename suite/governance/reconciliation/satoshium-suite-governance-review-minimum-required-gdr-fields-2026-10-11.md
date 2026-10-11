# Satoshium Suite Governance Review — Minimum Required Governance Decision Record Fields

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 3 of 4 — Governance Process, Decisions, Versioning & Accountability  
**Step:** 10 — Establish Minimum Required Governance Decision Record Fields  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record establishes the **minimum required fields** for a Satoshium Suite **Governance Decision Record (GDR)**.

The objective is to ensure that every formal governance decision contains enough information to answer:

```text
What was decided?
Who had authority to decide it?
Why was it decided?
What does it affect?
When does it govern?
What version is current?
What prior governance does it replace or correct?
```

The governing principle is:

> **A Governance Decision Record is incomplete if a later reviewer cannot reconstruct the authority, scope, rationale, operative effect, and historical relationship of the decision from the record itself.**

---

# Minimum Required Fields

The following fields are mandatory for every formal Material or Constitutional Governance Decision Record.

Routine GDR Lite records may use the same fields in abbreviated form where appropriate, but none of the underlying concepts may be omitted if they are materially relevant.

---

## 1. Decision Identifier

### Required Field

```text
Decision ID:
```

Recommended format:

```text
GDR-YYYY-NNNN
```

Example:

```text
GDR-2026-0001
```

### Purpose

Provides a stable, unique identity for the governance decision.

### Rule

> **The Decision ID identifies the decision itself and must not change when the document is later versioned.**

---

## 2. Date

### Required Field

```text
Decision Date:
```

The Decision Date is the date on which the governance decision was formally approved.

If another date controls operative effect, the GDR must additionally record:

```text
Effective Date:
```

### Purpose

Distinguishes:

```text
when the decision was made
```

from, where necessary:

```text
when the decision began governing
```

### Rule

```text
Decision Date
≠ necessarily
Effective Date
```

---

## 3. Subject

### Required Field

```text
Subject:
```

### Purpose

Identifies the governed matter.

Examples:

```text
Beacon Discovery Signal lifecycle

Suite Governance Standard revision

Canonical ownership of Object X

Admission of proposed Institution Y
```

### Rule

The Subject should identify the governance question precisely enough that the Decision can be distinguished from adjacent governance matters.

---

## 4. Scope

### Required Field

```text
Scope:
```

Where useful, divide into:

```text
In Scope:
Out of Scope:
```

### Purpose

Defines the boundary of the Decision.

The Scope must identify:

- what the Decision governs;
- what the Decision does not govern;
- any explicit limitations.

### Rule

> **Implementation may not exceed the approved Scope.**

---

## 5. Authority

### Required Field

```text
Authority:
```

The field must identify the authority under which the Decision is valid.

As applicable, it should record:

```text
Determining Authority:
Approving Authority:
```

For Constitutional matters, the final constitutional approving authority must be explicit.

### Purpose

Answers:

```text
Who had legitimate authority to make this decision?
```

### Rule

> **A decision without identifiable authority is not a complete governance decision.**

---

## 6. Rationale

### Required Field

```text
Rationale:
```

### Purpose

Explains why the Decision was made.

The rationale should identify, as applicable:

- governing problem;
- evidence;
- architectural basis;
- relevant Standards;
- institutional boundary;
- conflict being resolved;
- reason alternatives were rejected.

### Rule

The Rationale should preserve enough reasoning that later governance does not need to reconstruct intent from implementation behavior.

---

## 7. Decision

### Required Field

```text
Decision:
```

### Purpose

States the actual governed conclusion.

It must be explicit.

Examples:

```text
APPROVED

REJECTED

APPROVED WITH CONDITIONS

NO CHANGE REQUIRED

SUPERSEDED

CONSTITUTIONAL ADMISSION APPROVED
```

Where necessary, the Decision field should include the substantive conclusion rather than only the disposition label.

### Rule

> **The Decision must state what governance concluded—not merely that review occurred.**

---

## 8. Affected Institutions

### Required Field

```text
Affected Institutions:
```

Possible values include:

```text
None
Atlas
Navigator
Certifier
Registry
Chronicle
Anchor
Beacon
Attestor
Multiple Institutions
Suite-Wide
```

### Purpose

Identifies which formal institutions are materially affected.

### Rule

An institution should be listed when the Decision materially changes or constrains its:

- operations;
- governance;
- interoperability;
- authority;
- canonical responsibility;
- lifecycle;
- publication;
- implementation obligations.

Incidental reference alone does not make an institution affected.

---

## 9. Affected Canonical Objects

### Required Field

```text
Affected Canonical Objects:
```

Possible values may include:

```text
None

Jurisdiction Intelligence Package

Navigator Workflow Definition

Certification Package

Satoshium Registry Entry

Chronicle Entry

Integrity Reference

Discovery Signal

Attestation

Trust Statement
```

### Purpose

Makes canonical-object impact explicit.

### Rule

If canonical ownership changes, that fact must be stated separately and the Decision must be classified at the appropriate Constitutional level.

---

## 10. Effective State

### Required Field

```text
Effective State:
```

### Purpose

States the governance condition that becomes controlling after the Decision takes effect.

Examples:

```text
Current / Effective

Approved — Future Effective

Superseded

Deprecated

Retired

External / Pre-Suite

Operational

Constitutional Member
```

The field should answer:

```text
What governance state is in force as a result of this Decision?
```

### Effective Date

If the effective state does not begin on the Decision Date, include:

```text
Effective Date:
```

### Rule

> **The Decision states what was authorized; Effective State states what becomes controlling.**

---

## 11. Version

### Required Field

```text
Version:
```

Example:

```text
1.0
```

### Purpose

Identifies the edition of the Governance Decision Record itself.

The Version field is distinct from the Decision ID.

Therefore:

```text
Decision ID
→ stable decision identity

Version
→ edition of the record
```

### Rule

A later non-substantive correction may create a new GDR version.

A changed substantive conclusion requires a new governance decision rather than silent mutation of the existing one.

---

## 12. Supersession / Correction History

### Required Field

```text
Supersession / Correction History:
```

At minimum, this must state:

```text
None
```

or identify the applicable relationship.

Where applicable:

```text
Supersedes:
Superseded By:
Corrects:
Corrected By:
Prior Version:
Correction Date:
Supersession Effective Date:
```

### Purpose

Preserves the governance lineage.

### Rule

> **Every GDR must affirmatively show whether it has historical governance relationships rather than leaving the reader to infer them.**

---

# Minimum Required Field Set

The minimum standard is therefore:

```text
Decision ID:
Decision Date:
Subject:
Scope:
Authority:
Rationale:
Decision:
Affected Institutions:
Affected Canonical Objects:
Effective State:
Version:
Supersession / Correction History:
```

Where applicable:

```text
Effective Date:
```

must also be included.

---

# Recommended Compact GDR Header

A standard GDR may begin:

```text
Decision ID:
Decision Date:
Effective Date:
Subject:
Scope:
Authority:
Classification:
Version:
Status:
```

followed by:

```text
Rationale:
Decision:
Affected Institutions:
Affected Canonical Objects:
Effective State:
Supersession / Correction History:
```

Although **Classification** and **Status** are strongly recommended and already part of the full GDR model, the twelve fields established in this record define the irreducible minimum decision content requested by this Governance Review.

---

# Completeness Test

Before a GDR may be considered complete, ask:

```text
1. Can the decision be uniquely identified?
2. Is its date known?
3. Is the governed subject clear?
4. Is the scope bounded?
5. Is the legitimate authority identifiable?
6. Is the rationale preserved?
7. Is the actual decision explicit?
8. Are affected institutions identified?
9. Are affected canonical objects identified?
10. Is the resulting effective state clear?
11. Is the record version identified?
12. Is supersession / correction history explicit?
```

If any required answer is NO:

```text
GDR
→ INCOMPLETE
```

---

# No Blank-Ambiguity Rule

Required fields should not be silently omitted.

If a field has no applicable value, state:

```text
None
```

or:

```text
Not Applicable
```

as appropriate.

Examples:

```text
Affected Canonical Objects:
None

Supersession / Correction History:
None
```

This distinguishes:

```text
no impact
```

from:

```text
impact not evaluated
```

---

# Material & Constitutional Expansion

The fields above are the minimum.

Material and Constitutional GDRs should additionally include the fuller fields already established by the Governance Decision Record Model, including:

- classification;
- review record;
- determining authority;
- approving authority;
- interoperability impact;
- architecture reconciliation result where required;
- implementation requirements;
- publication information;
- preservation location;
- related governance records.

For Constitutional GDRs, omission of those applicable expanded fields would make the record incomplete even though the twelve core fields are present.

---

# Governing Doctrine

> **Every Governance Decision Record must identify the decision, its authority, its reason, its boundaries, its affected institutional and canonical subjects, the state it creates, and its place in governance history.**

Expanded:

> **A GDR should never force future reviewers to infer who decided, what was decided, what it affected, when it governed, or what it replaced. Those facts belong in the record itself.**

---

## Final Disposition

```text
Decision Identifier
→ REQUIRED

Date
→ REQUIRED

Subject
→ REQUIRED

Scope
→ REQUIRED

Authority
→ REQUIRED

Rationale
→ REQUIRED

Decision
→ REQUIRED

Affected Institutions
→ REQUIRED

Affected Canonical Objects
→ REQUIRED

Effective State
→ REQUIRED

Version
→ REQUIRED

Supersession / Correction History
→ REQUIRED

Effective Date
→ REQUIRED WHEN DISTINCT FROM DECISION DATE

No-blank ambiguity rule
→ ESTABLISHED

GDR completeness test
→ ESTABLISHED

Minimum Required GDR Fields
→ COMPLETE — APPROVED
```

# MINIMUM REQUIRED GOVERNANCE DECISION RECORD FIELDS — COMPLETE — APPROVED
