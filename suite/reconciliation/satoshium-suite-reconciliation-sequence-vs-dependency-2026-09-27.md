# Satoshium Suite Reconciliation — Sequence vs Dependency

**Date:** September 27, 2026  
**Phase:** Phase III — Whole-Suite Architecture  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record separates conceptual sequence from architectural dependency across the Satoshium Suite.

The purpose is to prevent diagrams, production histories, or explanatory flows from implying that every object must pass through every institution that appears earlier in a conceptual sequence.

The governing rule is:

> **SEQUENCE ≠ DEPENDENCY**

A conceptual flow may explain useful ordering.

A dependency establishes an actual requirement.

These are not the same thing.

---

# Conceptual Sequence

A conceptual sequence explains how Suite functions may relate.

For example:

```text
Authoritative Information
        ↓
Certification
        ↓
Registration / Preservation / Integrity / Discovery
        ↓
Attestation / Evaluation
```

This may be useful as a high-level explanatory model.

But it must not be interpreted as:

```text
Every object must:
start in Atlas
→ be certified
→ be registered
→ be chronicled
→ be anchored
→ be discovered
→ be attested
```

That would incorrectly convert conceptual architecture into a universal mandatory pipeline.

---

# Dependency

A dependency exists only where one institutional action actually requires:

- another object;
- another event;
- another condition;
- another result;
- or another governed step.

Dependencies must be explicit.

Examples:

```text
SREG
depends on
a qualifying registrable source object
```

```text
Chronicle Entry
depends on
a qualifying historical occurrence
```

```text
Integrity Reference
depends on
a defined Integrity Subject
```

```text
Attestor Evaluation
depends on
eligible governed inputs and an Attestation
```

These are real dependencies.

They do not mean every prior institution in a diagram must have acted.

---

# Position in a Conceptual Flow Does Not Create a Prerequisite

If Beacon appears after Anchor in a conceptual diagram, that does not mean:

> Anchor must act before Beacon.

If Attestor appears after Beacon, that does not mean:

> every Attestation requires a Beacon Discovery Signal.

If Chronicle appears after Registry, that does not mean:

> every Chronicle Entry requires a SREG.

Therefore:

> **POSITION IN A CONCEPTUAL FLOW ≠ PREREQUISITE**

---

# Atlas Example

Atlas often appears early because it provides:

> **Authoritative Intelligence**

But a later institution may act on something that did not originate in Atlas.

Therefore:

```text
Atlas earlier in flow
≠
Atlas required for all Suite objects
```

Atlas is a valid upstream authority where applicable.

It is not a universal dependency.

---

# Navigator Example

Navigator may appear above or across the Suite because it coordinates workflows.

But not every institutional action depends on a Navigator Workflow Definition.

Therefore:

```text
Navigator present in architecture
≠
Navigator required for every institutional action
```

Navigator becomes a workflow dependency only where a defined workflow actually invokes it.

---

# Certifier Example

Certifier may create a Certification Package that later becomes relevant to Registry, Chronicle, Anchor, Beacon, or Attestor.

But those institutions are not conceptually restricted to certification-derived matters.

Therefore:

```text
Certifier earlier in exercised lineage
≠
Certifier prerequisite for every later institution
```

---

# Registry Example

Registry provides:

> **Canonical Registration / Public Catalog**

But a Chronicle Entry does not universally require a prior SREG.

Chronicle requires:

> **a qualifying historical occurrence**

Likewise, an Integrity Reference does not require Registry unless a specific operation explicitly uses a Registry object as its subject or source.

Therefore:

> **Registration position ≠ universal downstream prerequisite**

---

# Chronicle Example

Chronicle preserves:

> **qualifying historical occurrences**

Its presence earlier than another institution in a diagram does not make Chronicle a prerequisite for that institution.

For example:

```text
Beacon Discovery Signal
```

may arise from observing a source object directly.

Beacon does not require Chronicle to first preserve that object or event.

Therefore:

> **Historical preservation ≠ universal dependency**

---

# Anchor Example

Anchor may contribute integrity evidence that later supports evaluation or interpretation.

But integrity protection is not automatically required before Beacon or Attestor acts.

Where a specific rule, method, or profile requires Anchor evidence, it becomes an explicit scoped dependency.

Where not required, it remains contextual or optional.

Therefore:

> **Integrity evidence may be required in a specific process without becoming a universal Suite prerequisite.**

---

# Beacon Example

Beacon may provide a Discovery Signal that later becomes relevant to Attestor.

But Attestor does not inherently depend on Beacon.

Attestor's actual requirements are:

```text
Eligible Governed Inputs
+
Attestation
+
Applicable Rules
```

The governed inputs may include Beacon.

They may also come from other authoritative sources.

Therefore:

> **Beacon is not a universal prerequisite for Attestor.**

---

# Attestor Example

Attestor naturally appears late in many conceptual models because it evaluates attributable assertions using already available evidence and context.

But:

```text
Attestor later
≠
all prior institutions required
```

The actual requirement is:

```text
Eligible Governed Inputs
+
Attestation
+
Applicable Rules
+
Evaluation Basis
→ Rule-Constrained Evaluation
```

The composition of governed inputs depends on the matter.

---

# Dependency Types

To avoid ambiguity, dependencies should be identified by type.

The Suite recognizes useful dependency classes including:

## Source Dependency

Requires a particular source object or authoritative input.

## Event Dependency

Requires an occurrence to have happened.

## Artifact Dependency

Requires a specific artifact or representation.

## Evidence Dependency

Requires evidence meeting defined criteria.

## Eligibility Dependency

Requires threshold conditions to be satisfied before entry into a governed process.

## Workflow Dependency

Requires a Navigator-defined workflow step or condition.

## Governance Dependency

Requires a rule, approval, institutional decision, or governed prerequisite.

## Publication Dependency

Requires public availability only where explicitly necessary.

These distinctions are preferable to using generic arrows as though every relationship meant “must come before.”

---

# Mandatory vs Optional Dependencies

Dependencies should also be interpreted as:

```text
Mandatory
or
Optional / Contextual
```

Example:

```text
Attestor Evaluation
→ mandatory dependency:
Attestation
```

while:

```text
Attestor Evaluation
→ possible contextual dependency:
Beacon Discovery Signal
```

This is more accurate than treating all upstream Suite objects as mandatory.

---

# Diagram Discipline

Arrows are easy to overread.

A diagram such as:

```text
A → B → C
```

often causes readers to infer:

> A must happen before B and B must happen before C.

That inference may be false.

Therefore Suite diagrams should distinguish conceptual progression from actual dependency wherever the difference matters.

Conceptually:

```text
A
↓ conceptual progression
B
```

is not equivalent to:

```text
B
requires
A
```

---

# Exercised First-Production Lineage

The first production lineage is real:

```text
SC-CERT-2026-0001
→ SREG-2026-0001
→ CHR-2026-0001
→ ANCH-2026-0001
→ BEAC-2026-0001
→ ATT-2026-0001
→ TRST-2026-0001
```

But this should be interpreted as a historically exercised and semantically connected production lineage.

It should not be interpreted as:

> every future object must follow this chain.

Therefore:

> **EXERCISED LINEAGE ≠ UNIVERSAL DEPENDENCY MODEL**

---

# Sequence and Dependency as Separate Architectural Dimensions

The Suite should treat sequence and dependency as distinct metadata concepts.

Conceptually:

```text
sequence_position
→ explanatory

dependency
→ explicit
→ typed
→ scoped
```

A later institution may depend on:

- one earlier object;
- several earlier objects;
- no prior Suite object;
- an external authoritative source;
- a qualifying event;
- a workflow condition.

All of these are compatible with the mature architecture.

---

# Dependency Does Not Transfer Authority

Even where a real dependency exists, authority does not automatically move downstream.

For example:

```text
Attestor
depends on
a governed source object
```

does not mean:

```text
Attestor owns the source object
```

Likewise:

```text
Registry
depends on
a registrable source object
```

does not mean:

```text
Registry owns the source object's substantive authority
```

Therefore:

> **DEPENDENCY ≠ AUTHORITY TRANSFER**

And:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# Relationship to Navigator

Navigator may encode workflow-specific dependencies.

For example:

```text
Workflow X:
Step B requires completion of Step A
```

That requirement belongs to the specific Workflow Definition.

It must not automatically become a universal Suite dependency.

Therefore:

> **WORKFLOW-SPECIFIC SEQUENCE ≠ SUITE-WIDE ARCHITECTURE**

---

# Relationship to Lifecycle

Sequence and dependency must also remain separate from lifecycle.

For example:

```text
Object B depends on Object A
```

does not mean:

- B shares A's lifecycle;
- B becomes Active when A becomes Active;
- B becomes Superseded when A becomes Superseded.

Therefore:

> **Dependency ≠ shared lifecycle**

---

# Relationship to Publication

Likewise, dependency does not create shared publication state.

An object may depend on another object while still having its own:

- publication decision;
- publication timing;
- publication state.

Therefore:

> **Dependency ≠ shared publication**

---

# Governing Rules

The Suite adopts the following rules:

1. **Sequence ≠ Dependency.**
2. Conceptual order does not create prerequisites.
3. A dependency must be explicit.
4. A dependency should be typed.
5. A dependency should be scoped.
6. A dependency may be mandatory or contextual.
7. Later institutional position does not imply all earlier institutions are required.
8. Atlas is not a universal prerequisite.
9. Navigator is not a universal prerequisite.
10. Certifier is not a universal prerequisite.
11. Registry is not a universal prerequisite.
12. Chronicle is not a universal prerequisite.
13. Anchor is not a universal prerequisite.
14. Beacon is not a universal prerequisite.
15. Attestor may consume multiple upstream sources without requiring the entire Suite lineage.
16. Exercised production lineage does not establish a universal dependency chain.
17. Workflow-specific order does not create Suite-wide order.
18. Dependency does not transfer authority.
19. Dependency does not create shared lifecycle.
20. Dependency does not create shared publication.
21. Conceptual diagrams must not silently turn progression into obligation.

---

# Governing Formulation

The primary formulation is:

> **SEQUENCE EXPLAINS ORDER. DEPENDENCY ESTABLISHES REQUIREMENT.**

And:

> **AN INSTITUTION APPEARING LATER IN A CONCEPTUAL FLOW DOES NOT MEAN EVERY OBJECT MUST PASS THROUGH EVERY EARLIER INSTITUTION.**

---

## Final Disposition

# SEQUENCE VS DEPENDENCY RECONCILIATION — COMPLETE — APPROVED

The Satoshium Suite is confirmed as a modular institutional architecture.

Conceptual sequence may explain progression.

Actual dependencies must remain:

- explicit;
- typed;
- scoped;
- governed.

No conceptual diagram or first-production lineage should be interpreted as a universal mandatory processing chain.
