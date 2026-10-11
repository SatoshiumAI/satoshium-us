# Satoshium Suite Governance Review — Threshold Between Ordinary Institutional Evolution and Suite-Level Architectural Change

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 2 of 4 — Institutional Change, Creation & Constitutional Boundaries  
**Step:** 4 — Establish the Threshold Between Ordinary Institutional Evolution and Suite-Level Architectural Change  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record establishes the formal threshold between:

```text
ORDINARY INSTITUTIONAL EVOLUTION
```

and:

```text
SUITE-LEVEL ARCHITECTURAL CHANGE
```

The objective is to allow institutions to improve, mature, automate, refine, and expand within their settled authority without requiring unnecessary Suite intervention, while preventing architectural change from being disguised as local implementation work.

The central question is:

> **When does a change stop being an institution exercising its existing authority and become a change to the Suite architecture itself?**

---

# Governing Threshold Rule

> **Ordinary institutional evolution changes how an institution performs its settled responsibility. Suite-level architectural change alters the responsibility, authority, canonical ownership, constitutional dependency, or institutional relationship defined by the Suite.**

The threshold can therefore be expressed as:

```text
CHANGE WITHIN SETTLED AUTHORITY
→ ORDINARY INSTITUTIONAL EVOLUTION

CHANGE TO SETTLED AUTHORITY
→ SUITE-LEVEL ARCHITECTURAL CHANGE
```

---

# Ordinary Institutional Evolution

A change is ordinary institutional evolution when all of the following remain true:

- the institution remains the same formal institution;
- its settled institutional role remains unchanged;
- its canonical object ownership remains unchanged;
- its source-authority boundaries remain unchanged;
- its lifecycle authority remains unchanged;
- its correction authority remains unchanged;
- its versioning authority remains unchanged;
- its conclusion or determination authority remains unchanged;
- no other institution gains or loses constitutional authority;
- no new mandatory cross-institution dependency is created;
- the formal Suite roster remains unchanged.

Ordinary evolution may still be substantial.

It may include:

- new operational capabilities;
- new schemas;
- new Procedures;
- new Policies;
- new controlled values;
- new supporting objects;
- new internal tooling;
- automation;
- new validation mechanisms;
- improved publication methods;
- expanded evidence handling;
- new Signal Types;
- new Event Types;
- new Certification Classes;
- new integrity methods;
- new workflow templates;
- internal organizational changes.

The size of the work does not make it architectural.

---

# Suite-Level Architectural Change

A change crosses the threshold into Suite-level architectural change when it alters one or more of the following.

## 1. Institutional Role

```text
what the institution exists to do
```

Example:

```text
Beacon expands from Discovery & Signals
into certification authority
→ Suite-level architectural change
```

---

## 2. Canonical Object Architecture

```text
what the institution canonically owns
```

Example:

```text
Discovery Metadata becomes a second
independent Beacon canonical object
→ Suite-level architectural change
```

---

## 3. Canonical Ownership

```text
which institution owns a canonical responsibility
```

Example:

```text
Trust Statement ownership moves
from Attestor to another institution
→ Suite-level architectural change
```

---

## 4. Authority Boundary

```text
who may make, approve, alter, or supersede a governed decision
```

Example:

```text
Registry gains authority to override Certifier status
→ Suite-level architectural change
```

---

## 5. Institutional Sovereignty

```text
whether an institution can independently exercise
its settled authority
```

Example:

```text
Certifier must receive Navigator approval
before making a certification determination
→ Suite-level architectural change
```

---

## 6. Constitutional Dependency

```text
whether another institution becomes
a mandatory gate for institutional authority
```

Example:

```text
Attestor approval becomes mandatory
before Beacon may publish
→ Suite-level architectural change
```

---

## 7. Suite Membership or Institutional Existence

```text
who belongs to the formal Suite
```

Examples:

```text
new formal institution
institution removed
institution merged
institution divided
institution replaced
→ Suite-level architectural change
```

---

## 8. Settled Suite Semantics

A change becomes architectural if it alters a settled Suite-wide semantic distinction such as:

```text
REFERENCE DOES NOT TRANSFER AUTHORITY

CONNECTION ≠ IDENTITY

AUTHORITY ≠ PROVENANCE

CORRECTION ≠ DELETION

SUPERCESSION ≠ MUTATION
```

These distinctions are part of the architecture itself.

---

# The Threshold Test

A proposed change remains ordinary institutional evolution only if every answer below is **NO**:

```text
1. Does this change the institution's settled role?

2. Does this change its canonical object family?

3. Does this change canonical ownership?

4. Does this change who may exercise authority?

5. Does this give another institution new authority over it?

6. Does this create a mandatory constitutional dependency?

7. Does this change the formal Suite roster?

8. Does this alter a settled Suite-wide semantic rule?

9. Does this reopen a settled Reconciliation decision?

10. Would another institution have to change its own architecture
    in order for this change to work?
```

If every answer is NO:

```text
ORDINARY INSTITUTIONAL EVOLUTION
```

If any answer is YES:

```text
PRESUMPTIVE SUITE-LEVEL ARCHITECTURAL CHANGE
```

and the matter must be escalated for Suite review.

---

# Cross-Institution Impact Test

Not every change affecting more than one institution is architectural.

A local change may have downstream effects without changing architecture.

Example:

```text
Certifier publishes a new schema version
→ Registry, Chronicle, Anchor, Beacon, or Attestor
may update parsers or references

Result
→ cross-institution implementation impact
→ NOT automatically architectural change
```

The threshold is crossed only when another institution must change its:

- authority;
- canonical ownership;
- role;
- lifecycle sovereignty;
- required approval relationship;
- constitutional dependency.

Therefore:

```text
CROSS-INSTITUTION IMPACT
≠
SUITE-LEVEL ARCHITECTURAL CHANGE
```

but:

```text
CROSS-INSTITUTION AUTHORITY CHANGE
=
SUITE-LEVEL ARCHITECTURAL CHANGE
```

---

# Materiality Alone Does Not Control

A very large change may remain ordinary evolution.

Example:

```text
complete rewrite of Beacon's implementation
while preserving role, canonical object, authority, and lifecycle
→ ordinary institutional evolution
```

A very small textual change may be architectural.

Example:

```text
one sentence states:
"Registry approval is required before Certifier may certify"
→ Suite-level architectural change
```

Therefore:

> **Architectural significance is determined by authority and ownership effect, not implementation size.**

---

# Supporting Object Boundary

Adding a supporting object remains ordinary evolution when the object:

- supports an existing role;
- remains noncanonical;
- does not create independent authority;
- does not require Suite-wide recognition as a canonical object;
- does not duplicate another institution's canonical responsibility.

The threshold is crossed when the supporting object becomes:

```text
independently canonical
+
independently authoritative
+
constitutionally recognized
```

At that point:

```text
SUITE-LEVEL ARCHITECTURAL CHANGE
```

---

# Procedure / Methodology Boundary

A Procedure or Methodology change remains ordinary institutional evolution when it changes:

```text
HOW
```

without changing:

```text
WHO
WHAT
AUTHORITY
OWNERSHIP
```

Example:

```text
Attestor changes evaluation sequence
→ ordinary institutional evolution

Attestor changes rules so it may override Certifier's certification
→ Suite-level architectural change
```

---

# Role Clarification Boundary

Clarifying an already-settled role is not architectural change when the clarification:

- preserves the same responsibility;
- preserves the same canonical object;
- preserves the same authority boundary;
- merely improves wording or precision.

If the clarification materially expands or narrows responsibility, the threshold is crossed.

Therefore:

```text
ROLE CLARIFICATION
→ ordinary governance/documentation

ROLE REALLOCATION
→ Suite-level architectural change
```

---

# Escalation Presumption

When classification is uncertain:

```text
if the uncertainty concerns implementation
→ presume institutional

if the uncertainty concerns authority,
canonical ownership,
role,
membership,
or constitutional dependency
→ escalate to Suite Governance
```

This prevents both over-centralization and silent architectural change.

---

# Threshold Matrix

| Change | Ordinary Evolution? | Suite-Level Architectural Change? |
|---|---:|---:|
| New Procedure | Yes, if authority unchanged | Yes, if Procedure creates new authority |
| New schema | Yes, if canonical identity unchanged | Yes, if schema creates a new canonical object |
| New supporting object | Yes | Yes, if elevated to canonical status |
| New capability | Yes, within settled role | Yes, if it enters another institutional domain |
| New methodology | Yes, within settled authority | Yes, if it changes authority or ownership |
| New approval step | Usually | Yes, if another institution becomes mandatory authority gate |
| Role wording clarification | Yes | Yes, if responsibility actually changes |
| Canonical object replacement | No | Yes |
| Canonical ownership transfer | No | Yes |
| New formal institution | No | Yes |
| Institution merger / division | No | Yes |
| Cross-institution technical dependency | Usually | Yes, if it becomes constitutional authority dependency |
| Documentation correction | Yes | Yes, if it substantively rewrites architecture |

---

# Governing Doctrine

> **Institutions are free to evolve inside the architecture. They are not free to redefine the architecture.**

Expanded:

> **The threshold is crossed when a proposed change ceases to be an exercise of existing institutional authority and instead changes the allocation, ownership, dependency, or meaning of that authority within the Suite.**

---

## Final Disposition

```text
Ordinary Institutional Evolution
→ DEFINED

Suite-Level Architectural Change
→ DEFINED

Authority threshold
→ ESTABLISHED

Canonical ownership threshold
→ ESTABLISHED

Cross-institution impact distinction
→ ESTABLISHED

Materiality distinction
→ ESTABLISHED

Escalation presumption
→ ESTABLISHED

Threshold Review
→ COMPLETE — APPROVED
```

# ORDINARY INSTITUTIONAL EVOLUTION / SUITE-LEVEL ARCHITECTURAL CHANGE THRESHOLD — COMPLETE — APPROVED
