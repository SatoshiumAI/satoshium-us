# Satoshium Suite Governance Review — Change-Type Classification Framework

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 2 of 4 — Institutional Change, Creation & Constitutional Boundaries  
**Step:** 2 — Distinguish Change Types  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record distinguishes seven forms of change that may occur across the Satoshium Suite:

1. Documentation Correction
2. Operational Refinement
3. Methodology Change
4. Governance Change
5. Canonical-Object Change
6. Institutional-Role Change
7. Constitutional Change

The purpose is to prevent routine maintenance from being unnecessarily escalated while ensuring that material architectural change cannot be hidden inside documentation, implementation, methodology, or governance updates.

The governing question is:

> **What exactly is changing, and at what level of authority must that change be governed?**

---

# Core Classification Principle

A change must be classified according to the **highest-order governed subject it actually alters**, not according to the file, page, codebase, or repository location in which the change appears.

Therefore:

```text
Changing documentation
does not necessarily mean
DOCUMENTATION CORRECTION.

Changing a methodology page
does not necessarily mean
METHODOLOGY CHANGE.

Changing governance documentation
does not necessarily mean
GOVERNANCE CHANGE.
```

If the substance changes institutional role, canonical ownership, or constitutional architecture, the higher classification controls.

---

# 1. Documentation Correction

## Definition

A **Documentation Correction** changes how existing, already-settled architecture or operation is described without changing the architecture or operation itself.

It may:

- correct stale terminology;
- correct an outdated operational status;
- correct a broken link or inaccurate route;
- align a README with an authoritative current page;
- replace legacy shorthand with settled canonical terminology;
- fix a factual documentation error;
- clarify wording where the underlying architecture is already settled.

## It Does Not

A Documentation Correction does not:

- create new authority;
- alter institutional role;
- alter canonical ownership;
- change lifecycle semantics;
- change governing Rules;
- change Methodology;
- create a new institution;
- change Suite membership.

## Example

```text
Beacon described as "in development"
when Beacon is already Operational
→ Documentation Correction
```

## Governing Level

```text
Institution / owning documentation surface
```

unless the correction concerns a Suite-level page.

## Escalation Trigger

If the proposed "correction" would require choosing among unresolved architectural interpretations, it is no longer merely a Documentation Correction.

---

# 2. Operational Refinement

## Definition

An **Operational Refinement** changes how an institution performs its existing authorized work without altering its settled role, canonical ownership, authority boundary, or constitutional position.

It may include:

- workflow improvement;
- automation;
- validation enhancement;
- performance optimization;
- internal process refinement;
- schema implementation refinement;
- publication tooling;
- monitoring;
- maintenance process;
- internal delegation;
- user-interface improvement;
- supporting-object refinement.

## It Does Not

An Operational Refinement does not:

- redefine what the institution is;
- create a new canonical responsibility;
- alter another institution's authority;
- change Suite membership;
- change a settled constitutional boundary.

## Example

```text
Anchor improves its Verification workflow
while remaining the Integrity Preservation institution
→ Operational Refinement
```

## Governing Level

```text
Institution-Level
```

unless the refinement produces cross-institution or constitutional effects.

## Escalation Trigger

If implementation creates de facto authority, mandatory dependency, or canonical ownership change, the matter must be reclassified.

---

# 3. Methodology Change

## Definition

A **Methodology Change** alters the governed method or repeatable process by which a Standard, requirement, evaluation, or institutional function is applied.

It changes:

```text
HOW governed work is performed
```

rather than merely changing implementation tooling.

Examples may include:

- changing an evaluation sequence;
- changing evidence-handling methodology;
- changing how a governed eligibility test is performed;
- changing the shared process by which a Suite Standard is applied;
- changing institution-specific methodological principles.

## Two Levels of Methodology Change

### Suite-Level Methodology Change

Changes shared methodological foundations applicable across more than one institution.

```text
Governing level
→ Suite
```

### Institution-Specific Methodology Change

Changes methodology within one institution's settled authority.

```text
Governing level
→ Institution
```

provided it remains consistent with applicable Suite Methodology.

## It Does Not Automatically Mean

A Methodology Change does not automatically alter:

- institutional role;
- canonical ownership;
- Suite membership;
- constitutional architecture.

## Example

```text
Certifier changes the governed sequence
for evaluating evidence under an existing Standard
→ Methodology Change
```

## Escalation Trigger

If the new methodology changes who has authority, what canonical object exists, or which institution owns a responsibility, it must be reclassified at the higher level.

---

# 4. Governance Change

## Definition

A **Governance Change** alters the rules controlling:

- authority;
- decision rights;
- approvals;
- accountability;
- delegation;
- review;
- change control;
- exceptions;
- conflict resolution;
- transparency;
- preservation of governance decisions.

It changes:

```text
HOW AUTHORITY IS EXERCISED AND CONTROLLED
```

rather than the substantive institutional role itself.

## Examples

```text
new Governance Decision Record requirement
→ Governance Change

new approval threshold for material institutional Rules
→ Governance Change

new reconsideration process
→ Governance Change
```

## Governing Level

May be:

```text
Institution-Level Governance Change
```

or:

```text
Suite-Level Governance Change
```

depending on the governed subject.

## Important Boundary

A Governance Change becomes a Constitutional Change when it reallocates foundational authority.

Example:

```text
changing who reviews a Registry Rule
→ Governance Change

giving Attestor authority to override Registry lifecycle
→ Constitutional Change
```

---

# 5. Canonical-Object Change

## Definition

A **Canonical-Object Change** alters the Suite-recognized canonical object architecture of an institution.

This includes:

- changing which object is canonical;
- adding a new canonical object family;
- removing a canonical object family;
- splitting a canonical object;
- merging canonical object families;
- transferring canonical ownership;
- changing the identity boundary of the canonical object itself.

## It Does Not Include

Routine changes to:

- schema fields;
- serialization;
- controlled values;
- presentation;
- internal supporting records;
- version metadata;

when the same canonical object and ownership remain intact.

## Examples

```text
Beacon adds a new field to Discovery Signal
→ NOT Canonical-Object Change

Beacon elevates Discovery Metadata
into an independently canonical Suite object
→ Canonical-Object Change
```

## Governing Level

```text
Suite-Level / Architectural
```

because canonical-object architecture participates in the shared Suite model.

## Constitutional Significance

A Canonical-Object Change is presumptively **material**.

A transfer of canonical ownership is **constitutional**.

---

# 6. Institutional-Role Change

## Definition

An **Institutional-Role Change** alters the settled responsibility assigned to a formal Suite institution.

It changes:

```text
WHAT THE INSTITUTION EXISTS TO DO
```

Examples:

```text
Beacon gains Verification authority

Anchor begins issuing Trust Statements

Registry gains certification authority

Navigator becomes approval authority over institutional decisions
```

## It Does Not Include

Expansion of tools or capabilities that remain clearly inside the existing role.

Example:

```text
Beacon adds another discovery mechanism
→ NOT Institutional-Role Change
```

## Governing Level

```text
Suite-Level / Constitutional Review
```

because institutional roles are part of the settled Suite architecture.

## Presumption

Institutional-role changes are presumptively constitutional unless clearly demonstrated to be a non-constitutional clarification inside the already-settled role.

---

# 7. Constitutional Change

## Definition

A **Constitutional Change** alters the foundational architecture by which the Suite exists as a system of independently governed institutions.

It includes changes to:

- formal Suite membership;
- institutional existence;
- institutional role allocation;
- canonical ownership assignment;
- foundational authority boundaries;
- institutional sovereignty;
- mandatory constitutional dependencies;
- the governance authority required to control the Suite itself.

It is the highest-order change classification in this framework.

## Examples

```text
add a ninth formal Suite institution
→ Constitutional Change

remove Chronicle from the Suite
→ Constitutional Change

transfer Trust Statement ownership from Attestor to Beacon
→ Constitutional Change

make Navigator a mandatory authority gate over all institutions
→ Constitutional Change

merge Registry and Chronicle into one formal institution
→ Constitutional Change
```

## Governing Level

```text
Formal Suite Governance
```

with explicit review, decision, record, implementation, and historical preservation.

## Rule

Constitutional change must never occur implicitly.

---

# Classification Hierarchy

The seven categories form a significance ladder:

```text
1. Documentation Correction
        ↓
2. Operational Refinement
        ↓
3. Methodology Change
        ↓
4. Governance Change
        ↓
5. Canonical-Object Change
        ↓
6. Institutional-Role Change
        ↓
7. Constitutional Change
```

This ladder represents increasing architectural significance.

It is **not** a mandatory process sequence.

---

# Highest-Order Change Rule

A proposal may contain several kinds of change simultaneously.

When that occurs:

> **The proposal is governed according to its highest-order material effect.**

Example:

```text
README update
+
new wording says Beacon now owns Verification
```

This is not merely:

```text
Documentation Correction
```

It is an attempted:

```text
Institutional-Role Change
```

and potentially:

```text
Constitutional Change
```

Likewise:

```text
schema update
+
new object becomes an independent canonical object
```

is not merely an Operational Refinement.

It is a:

```text
Canonical-Object Change
```

---

# Classification Decision Table

| Change Type | What Changes? | Default Governing Level | Architectural Effect |
|---|---|---|---|
| Documentation Correction | Description of settled reality | Owning documentation authority | None |
| Operational Refinement | Implementation of existing authority | Institution | None if boundary preserved |
| Methodology Change | How governed work is performed | Institution or Suite | Process / method |
| Governance Change | How authority is exercised or controlled | Institution or Suite | Decision/control structure |
| Canonical-Object Change | Canonical object architecture | Suite | Material architecture |
| Institutional-Role Change | What an institution exists to do | Suite | Institutional architecture |
| Constitutional Change | Foundational Suite structure or authority | Formal Suite Governance | Constitutional architecture |

---

# Classification Questions

When evaluating any proposed change, ask in this order:

```text
1. Is this only correcting the description of already-settled reality?
   YES → Documentation Correction

2. Does it only improve execution within existing authority?
   YES → Operational Refinement

3. Does it change the governed method used to perform or evaluate work?
   YES → Methodology Change

4. Does it change decision rights, approvals, accountability, delegation, or change control?
   YES → Governance Change

5. Does it change what object is canonical or who owns a canonical object?
   YES → Canonical-Object Change

6. Does it change what an institution exists to do?
   YES → Institutional-Role Change

7. Does it change Suite membership, institutional sovereignty, foundational authority, canonical ownership assignment, or constitutional dependency?
   YES → Constitutional Change
```

If more than one answer is YES:

```text
CLASSIFY AT THE HIGHEST MATERIAL LEVEL
```

---

# Relationship to Day 2 Step 1

Day 2 Step 1 established:

```text
INSTITUTIONAL EVOLUTION
→ changes how an institution performs its role

INSTITUTIONAL CHANGE
→ changes role, authority, identity, ownership, or constitutional status
```

This framework refines that distinction.

Generally:

```text
Documentation Correction
Operational Refinement
Institution-specific Methodology Change
some Governance Changes
→ may remain Institutional Evolution

Canonical-Object Change
Institutional-Role Change
Constitutional Change
→ presumptively Institutional Change
```

Suite-level Methodology or Governance Changes may also become institutional changes when they alter authority or constitutional architecture.

---

# Anti-Evasion Rule

No lower-level classification may be used to conceal a higher-order change.

Therefore:

```text
Documentation
cannot conceal Architecture

Implementation
cannot conceal Authority Transfer

Methodology
cannot conceal Role Change

Governance
cannot conceal Constitutional Change

Schema
cannot conceal Canonical-Object Creation
```

---

# Governing Classification Rule

> **Classify the change by what it substantively alters, not by where the edit occurs or what the change is called. The highest material effect controls the required governance level.**

---

## Final Disposition

```text
Documentation Correction
→ DEFINED

Operational Refinement
→ DEFINED

Methodology Change
→ DEFINED

Governance Change
→ DEFINED

Canonical-Object Change
→ DEFINED

Institutional-Role Change
→ DEFINED

Constitutional Change
→ DEFINED

Highest-order change rule
→ ESTABLISHED

Anti-evasion rule
→ ESTABLISHED

Change-Type Classification Framework
→ COMPLETE — APPROVED
```

# CHANGE-TYPE CLASSIFICATION FRAMEWORK — COMPLETE — APPROVED
