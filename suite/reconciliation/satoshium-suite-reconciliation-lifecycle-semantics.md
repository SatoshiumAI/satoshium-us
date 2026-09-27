# Satoshium Suite Reconciliation — Lifecycle Semantics

**Date:** September 26, 2026  
**Phase:** Phase II — Objects, Terminology & Semantics  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record reconciles lifecycle semantics across the Satoshium Suite.

The purpose is to preserve clear distinctions among:

- canonical creation;
- lifecycle activation;
- publication;
- currentness;
- validation;
- certification;
- support;
- supersession;
- withdrawal;
- versioning.

The governing principle is:

> **CANONICAL CREATION ≠ LIFECYCLE ACTIVATION ≠ PUBLICATION**

These events may occur close together operationally, but they are not semantically identical.

---

# Core Lifecycle Model

The Suite adopts the following conceptual progression:

```text
Canonical Creation
        ↓
Lifecycle Activation
        ↓
Publication
```

These are distinct governance events.

They answer different questions.

---

## Canonical Creation

Canonical Creation answers:

> **Does the canonical object exist?**

Creation establishes:

- canonical identity;
- institutional ownership;
- existence of the governed object.

Creation does not automatically mean:

- active;
- published;
- valid;
- certified;
- supported;
- current.

Therefore:

> **Created ≠ Active**

and:

> **Created ≠ Published**

---

## Lifecycle Activation

Lifecycle Activation answers:

> **Is the canonical object operative within its institution?**

Activation establishes operational standing under the owning institution's lifecycle rules.

Activation does not automatically mean:

- public;
- valid under every relevant framework;
- certified;
- supported;
- current forever.

Therefore:

> **Active ≠ Published**

and:

> **Active ≠ Valid by definition**

---

## Publication

Publication answers:

> **Is the canonical object or an approved representation publicly accessible?**

Publication exposes an existing object or approved representation.

It does not create institutional authority.

Therefore:

> **Publication exposes authority; it does not create authority.**

And:

```text
Published ≠ Active
Published ≠ Valid
Published ≠ Certified
Published ≠ Supported
Published ≠ Current
```

unless those states are independently true.

---

# Lifecycle State and Publication State Must Remain Separate

The Suite should preserve:

```text
lifecycle_state
```

and:

```text
publication_state
```

as distinct semantic domains.

An object may legitimately be:

```text
Lifecycle State: Superseded
Publication State: Published
```

or:

```text
Lifecycle State: Active
Publication State: Unpublished
```

where the owning institution permits those combinations.

Therefore:

> **Lifecycle State ≠ Publication State**

---

# Publication Does Not Define Currentness

An object may remain publicly available after it is no longer current.

For example:

```text
Lifecycle State: Superseded
Publication State: Published
```

may be necessary for historical traceability.

Therefore:

> **Published ≠ Current**

and:

> **Superseded ≠ Unpublished**

---

# Withdrawal and Publication

Withdrawal concerns lifecycle or operative standing.

Publication concerns accessibility.

A withdrawn object may remain publicly available as a historical record if institutional rules allow it.

Therefore:

> **Withdrawn ≠ Unpublished by definition**

The two states must remain separately governed.

---

# Version Lifecycle

A version may itself pass through lifecycle events.

Conceptually:

```text
Version Created
        ↓
Version Activated
        ↓
Version Published
```

Therefore:

> **Version Creation ≠ Version Activation ≠ Version Publication**

Likewise:

> **Version creation does not automatically create a new canonical identity.**

Whether a new identity is required depends on materiality and institutional rules.

---

# Creation Does Not Encode Validation

A newly created object is not automatically valid.

Validation remains a separate governed process.

Therefore:

```text
Created
≠
Valid
```

An object may exist canonically and later fail Validation.

---

# Activation Does Not Encode Certification

An Active object is not automatically Certified.

For example:

```text
Lifecycle State: Active
```

does not imply:

```text
Certification Outcome: Certified
```

unless the relevant institution explicitly says so.

Therefore:

> **Lifecycle state does not substitute for substantive decision fields.**

---

# Publication Does Not Encode Evaluation Outcome

For Attestor:

```text
TRST-2026-0001
Publication State: Published
```

does not reveal whether the Trust Statement conclusion is:

```text
Supported
Partially Supported
Not Supported
Contradicted
Indeterminate
```

The conclusion must remain explicit.

Therefore:

> **Publication State ≠ Evaluation Outcome**

---

# Institutional Lifecycle Independence

Each canonical object is governed by its owning institution.

For example:

```text
Certification Package
→ Certifier lifecycle

SREG
→ Registry lifecycle

Chronicle Entry
→ Chronicle lifecycle

Integrity Reference
→ Anchor lifecycle

Discovery Signal
→ Beacon lifecycle

Attestation / Trust Statement
→ Attestor lifecycle
```

Relationships among objects do not create a single shared lifecycle.

Therefore:

> **Relationship ≠ shared lifecycle**

---

# Lifecycle State Does Not Automatically Propagate

If a source object changes state, connected objects do not automatically inherit that state.

For example:

```text
SC-CERT-2026-0001
→ Superseded
```

does not automatically mean:

```text
SREG-2026-0001
→ Superseded

CHR-2026-0001
→ Superseded

ANCH-2026-0001
→ Superseded

BEAC-2026-0001
→ Superseded

ATT-2026-0001
→ Superseded

TRST-2026-0001
→ Superseded
```

Each owning institution must determine the lifecycle effect under its own rules.

Therefore:

> **Lifecycle does not propagate automatically through relationships.**

---

# Publication State Does Not Automatically Propagate

The same rule applies to publication.

Publishing a source object does not automatically publish a downstream object.

Likewise, unpublishing a source object does not automatically unpublish every related object.

Therefore:

> **Publication does not propagate automatically through relationships.**

---

# Creation, Activation, and Publication May Be Operationally Simultaneous

The Suite allows implementations to create, activate, and publish an object in rapid succession or within one governed operation.

But even when timing is effectively simultaneous, the semantics remain distinct.

For example:

```text
Created: 10:00:00
Activated: 10:00:00
Published: 10:00:00
```

does not collapse the meanings.

Therefore:

> **Operational simultaneity does not erase semantic distinction.**

---

# Currentness

Currentness is a separate concept from publication.

An object is current only where the owning institution recognizes it as the presently operative or authoritative version/state.

Therefore:

```text
Current ≠ Published
Current ≠ Active by syntax alone
```

Currentness must be determined by institutional lifecycle rules.

---

# Supersession

Supersession changes operative standing while preserving historical continuity.

A superseded object remains historically real.

Therefore:

> **Superseded ≠ Deleted**

and:

> **Superseded ≠ Mutated into successor**

The successor is a distinct governed object or version as defined by institutional rules.

---

# Historical Preservation of Lifecycle

Chronicle may preserve lifecycle-related occurrences, such as:

- creation;
- activation;
- publication;
- correction;
- supersession;
- withdrawal.

Chronicle's preservation does not become the source of those lifecycle states.

The source institution remains authoritative for its object's lifecycle.

Therefore:

> **Chronicle records lifecycle history; it does not own another institution's lifecycle.**

---

# Anchor and Lifecycle

Anchor may protect a representation of an object in a specific lifecycle state.

If the source object later changes state, the Integrity Reference can still remain valid for the representation originally protected.

Therefore:

> **Integrity verification ≠ source currentness**

and:

> **Integrity state ≠ source lifecycle state**

---

# Beacon and Lifecycle

Beacon may discover or signal a lifecycle change.

That does not make Beacon authoritative for the source object's state.

Therefore:

> **Observed lifecycle state ≠ Beacon-owned lifecycle state**

The source institution remains authoritative.

---

# Attestor and Lifecycle

Attestor may evaluate evidence that includes lifecycle state.

That does not transfer lifecycle authority.

A Trust Statement conclusion does not automatically change the lifecycle state of an upstream object.

Therefore:

> **Evaluation does not rewrite source lifecycle.**

---

# Reconciled Lifecycle Principles

The Suite adopts the following rules:

1. **Canonical Creation ≠ Lifecycle Activation ≠ Publication.**
2. Creation establishes existence and canonical identity.
3. Activation establishes operative standing.
4. Publication establishes accessibility.
5. Created ≠ Active.
6. Active ≠ Published.
7. Published ≠ Current.
8. Published ≠ Valid.
9. Published ≠ Certified.
10. Published ≠ Supported.
11. Lifecycle State ≠ Publication State.
12. Superseded ≠ Unpublished.
13. Withdrawn ≠ Unpublished by definition.
14. Version Creation ≠ Version Activation ≠ Version Publication.
15. Version creation does not automatically create new canonical identity.
16. Lifecycle state does not substitute for substantive institutional outcomes.
17. Related objects do not automatically share lifecycle.
18. Lifecycle changes do not automatically propagate across relationships.
19. Publication changes do not automatically propagate across relationships.
20. Operational simultaneity does not erase semantic distinction.
21. Supersession preserves historical reality.
22. Chronicle may preserve lifecycle events without owning source lifecycle.
23. Anchor integrity state remains distinct from source lifecycle state.
24. Beacon observation does not transfer lifecycle authority.
25. Attestor evaluation does not rewrite source lifecycle.

---

# Governing Formulation

The Suite adopts the following concise formulation:

> **CREATION DEFINES EXISTENCE. ACTIVATION DEFINES OPERATIVE STATE. PUBLICATION DEFINES ACCESSIBILITY.**

And:

> **These dimensions may interact, but they must not be collapsed.**

---

## Final Disposition

# LIFECYCLE SEMANTICS RECONCILIATION — COMPLETE — APPROVED

The Satoshium Suite now preserves one consistent lifecycle model across institutions:

```text
Canonical Creation
→ Lifecycle Activation
→ Publication
```

with each event treated as semantically distinct and independently governed.

No institution may use lifecycle or publication terminology as an implied substitute for validity, certification, evaluation outcome, trust, or authority.
