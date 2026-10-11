# Satoshium Suite Governance Review — Definition of Institutional Change

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 2 of 4 — Institutional Change, Creation & Constitutional Boundaries  
**Step:** 1 — Define What Constitutes an Institutional Change  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record defines what constitutes an **institutional change** within the Satoshium Suite.

Its purpose is to distinguish ordinary institutional evolution from changes that materially alter the identity, authority, structure, or constitutional position of a formal Suite institution.

The central question is:

> **When does a change stop being ordinary maintenance or operational refinement and become a change to the institution itself?**

---

## Governing Definition

An **institutional change** is:

> **A governed change that alters the formal identity, settled role, authority boundary, canonical-object ownership, constitutional position, or institutional existence of a Satoshium Suite institution.**

Institutional change is not defined by size, effort, code volume, public visibility, or implementation complexity.

It is defined by whether the change alters what the institution **is**, what it **owns**, what it is **authorized to do**, or how it stands in relation to the rest of the Suite.

---

## What Is Not, By Itself, an Institutional Change

The following do **not** constitute institutional change when they remain within settled authority:

- documentation correction;
- wording clarification;
- visual redesign;
- navigation change;
- schema refinement that preserves canonical ownership;
- Procedure change;
- Policy refinement;
- operational workflow improvement;
- internal automation;
- implementation change;
- Validation enhancement;
- publication-format change;
- maintenance process;
- internal delegation;
- internal role reassignment that does not alter institutional authority;
- addition of a supporting object that does not become canonical;
- introduction of a new controlled value;
- lifecycle-state refinement consistent with the settled model;
- interoperability implementation that preserves authority and canonical ownership.

These may be material operational changes. They are not automatically institutional changes.

---

## Institutional Change Triggers

A change becomes institutional when one or more of the following occur.

### 1. Institutional Identity Changes

Examples include renaming that changes constitutional identity, merger, division, replacement, retirement, or reconstitution.

This changes **who the institution is**.

### 2. Settled Institutional Role Changes

Examples include Registry gaining certification authority, Beacon gaining formal Verification authority, Anchor issuing Trust Statements, or Navigator becoming decision authority over participating institutions.

This changes **what the institution is responsible for**.

### 3. Canonical Object Ownership Changes

Examples include moving a canonical object family to another institution, adding a new canonical object family, splitting canonical ownership, or elevating a supporting object into a canonical object.

This changes **what the institution owns**.

### 4. Authority Boundary Changes

Examples include one institution gaining power to approve another institution's decisions, alter another institution's lifecycle state, or acquire source authority through registration, orchestration, interoperability, or reference.

This changes **what the institution is authorized to control**.

### 5. Formal Suite Membership Changes

Examples include admission, removal, promotion of an external system into the Suite, demotion outside the Suite, or a merger changing the formal roster.

This changes **who belongs to the Suite**.

### 6. Constitutional Dependency Changes

A change is institutional when it makes one institution constitutionally dependent on another in a way that did not previously exist.

Examples:

```text
Certifier may no longer act unless Registry first approves

Beacon may not publish unless Attestor approves

Chronicle becomes mandatory for every institutional object lifecycle

Navigator becomes a compulsory gate for all Suite operations
```

This changes **how independently governed institutions may exercise their settled authority**.

### 7. Canonical Responsibility Is Reallocated

If historical preservation leaves Chronicle, integrity preservation leaves Anchor, discovery leaves Beacon, or attestation leaves Attestor, the constitutional allocation of responsibility has changed.

### 8. Institutional Existence Changes

Creation, retirement, suspension as a formal institution, replacement, merger, division, or constitutional reconstitution are inherently institutional changes.

---

## Institutional Change vs. Institutional Evolution

```text
INSTITUTIONAL EVOLUTION
→ changes how an institution performs its role

INSTITUTIONAL CHANGE
→ changes the institution's role, authority, identity, ownership, or constitutional status
```

Examples:

```text
new Registry Validation sequence
→ institutional evolution

Registry acquires certification authority
→ institutional change

new Anchor Verification procedure
→ institutional evolution

Anchor gains Trust Statement ownership
→ institutional change

new Beacon schema
→ institutional evolution

Beacon becomes mandatory approval gate for publication
→ institutional change
```

---

## Institutional Change vs. Documentation Change

A documentation change is not an institutional change unless the documentation purports to alter architecture.

```text
correct stale wording
→ documentation correction

clarify canonical-object terminology
→ documentation correction

rewrite a page so an institution appears to own another institution's authority
→ unauthorized architectural claim
→ potential institutional change attempt
```

Documentation may record institutional change. It may not silently create it.

---

## Institutional Change vs. Interoperability Change

Interoperability may change interfaces, serialization, identifier resolution, exchange constraints, handoff mechanics, compatibility, or state/version propagation.

These are not institutional changes if they preserve role, authority, canonical ownership, lifecycle ownership, and institutional independence.

An interoperability change becomes institutional when it creates de facto authority transfer or constitutional dependency.

---

## Institutional Change vs. Governance Change

Not every governance change is institutional.

```text
new governance decision-record format
→ governance change

new transparency requirement
→ governance change

change to who owns Certification Packages
→ institutional change

change to whether Registry can override Certifier status
→ institutional change
```

Institutional change is therefore one class of governance-significant change, not the same thing as governance change generally.

---

## Constitutional Significance Test

A proposed change should be treated as an institutional change if the answer to any of these questions is **YES**:

```text
Does this change who the institution is?

Does this change the institution's settled role?

Does this change what canonical object the institution owns?

Does this change what authority the institution may exercise?

Does this change what authority another institution may exercise over it?

Does this change whether the institution belongs to the formal Suite?

Does this create a new mandatory constitutional dependency?

Does this merge, divide, retire, replace, or create an institution?

Does this reopen a settled Reconciliation decision about institutional architecture?
```

If all answers are **NO**, the change is presumptively not an institutional change.

---

## Change Classification Boundary

For Day 2, the Governance Review will use the following high-level distinction:

```text
ROUTINE OPERATIONAL CHANGE
→ remains within institution

MATERIAL INSTITUTIONAL EVOLUTION
→ may require institution + Suite review depending on cross-Suite effect

INSTITUTIONAL CHANGE
→ Suite governance review required

CONSTITUTIONAL CHANGE
→ formal Suite-level decision required
```

Later Day 2 steps will refine these categories.

---

## Examples Across the Eight Institutions

### Atlas

```text
new intelligence source
→ NOT institutional change

new package schema
→ NOT institutional change

Atlas loses Authoritative Intelligence role
→ INSTITUTIONAL CHANGE
```

### Navigator

```text
new workflow template
→ NOT institutional change

new orchestration engine
→ NOT institutional change

Navigator becomes mandatory approval authority
→ INSTITUTIONAL CHANGE
```

### Certifier

```text
new certification Procedure
→ NOT institutional change

new Certification Class
→ NOT automatically institutional change

Certifier loses Certification Package ownership
→ INSTITUTIONAL CHANGE
```

### Registry

```text
new Record Type
→ NOT automatically institutional change

new SREG field
→ NOT institutional change

Registry gains source-record authority
→ INSTITUTIONAL CHANGE
```

### Chronicle

```text
new Event Type
→ NOT institutional change

new preservation Procedure
→ NOT institutional change

Chronicle becomes source-state authority
→ INSTITUTIONAL CHANGE
```

### Anchor

```text
new integrity method
→ NOT institutional change

new Verification Procedure
→ NOT institutional change

Anchor gains certification authority
→ INSTITUTIONAL CHANGE
```

### Beacon

```text
new Signal Type
→ NOT institutional change

new discovery channel
→ NOT institutional change

Beacon becomes mandatory approval gate
→ INSTITUTIONAL CHANGE
```

### Attestor

```text
new Evaluation Rule
→ NOT automatically institutional change

new Trust Statement schema version
→ NOT institutional change

Attestor gains universal truth authority
→ INSTITUTIONAL CHANGE
```

---

## Governing Rule

> **An institutional change alters the institution itself—not merely how the institution performs its existing work.**

Expanded:

> **A change is institutional when it modifies formal identity, settled role, canonical ownership, authority boundary, constitutional dependency, Suite membership, or institutional existence. Operational refinement within settled authority remains institutional evolution, not institutional change.**

---

## Final Disposition

```text
Institutional change
→ DEFINED

Institutional evolution
→ DISTINGUISHED

Documentation change
→ DISTINGUISHED

Interoperability change
→ DISTINGUISHED

Governance change
→ DISTINGUISHED

Constitutional significance test
→ ESTABLISHED

Institutional Change Definition
→ COMPLETE — APPROVED
```

# DEFINITION OF INSTITUTIONAL CHANGE — COMPLETE — APPROVED
