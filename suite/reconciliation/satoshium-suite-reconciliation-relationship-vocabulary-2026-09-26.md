# Satoshium Suite Reconciliation — Relationship Vocabulary Reconciliation

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record documents the Suite-wide reconciliation of relationship vocabulary conducted during the September 26, 2026 phase of the Satoshium Suite Reconciliation.

The review preserves distinct meanings for the following relationship terms:

- `references`
- `derived-from`
- `supports`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

The purpose of this record is to ensure that cross-object and cross-institution relationships communicate exact semantic meaning rather than functioning as generic links.

The governing principles are:

> **RELATIONSHIPS MUST SAY WHAT THE CONNECTION MEANS — NOT MERELY THAT A CONNECTION EXISTS.**

> **REFERENCE ≠ DERIVATION ≠ SUPPORT.**

> **CONNECTION ≠ IDENTITY.**

> **RELATIONSHIP DOES NOT TRANSFER AUTHORITY.**

---

# 1. `references`

## Controlled Definition

`references` means that one object identifies, cites, points to, or links to another object without asserting derivation, evidentiary support, ownership, or replacement.

Example:

```text
SREG
    references
Certification Package
```

This means the Registry Entry points to the Certification Package.

It does not mean that:

- SREG derives from the Certification Package;
- SREG supports the Certification Package;
- Registry owns the Certification Package;
- Registry inherits certification authority.

## Controlled Distinctions

- references ≠ derived-from
- references ≠ supports
- references ≠ ownership
- references ≠ authority transfer

## Governing Rule

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# 2. `derived-from`

## Controlled Definition

`derived-from` means that a downstream object or representation was produced from, transformed from, or substantively generated using an upstream object as part of its basis.

Examples:

```text
Trust Statement
    derived-from
Attestation
```

```text
JSON Representation
    derived-from
Atlas Canonical Markdown
```

This relationship asserts lineage rather than simple connection.

## Controlled Distinctions

- derived-from ≠ references
- derived-from ≠ supports
- derived-from ≠ identity

The derived item remains distinct from its source.

## Governing Rule

> **DERIVATION ESTABLISHES LINEAGE, NOT IDENTITY.**

---

# 3. `supports`

## Controlled Definition

`supports` means that one piece of evidence, record, or governed object contributes substantive evidentiary or logical support to a proposition, determination, or conclusion.

Examples:

```text
Evidence Record
    supports
Certification Finding
```

```text
Source Evidence
    supports
Attestation Assertion
```

This is stronger than a neutral reference.

## Controlled Distinctions

- supports ≠ references
- supports ≠ derived-from
- supports ≠ authority transfer

A record may be referenced without supporting the proposition.

## Governing Rule

> **SUPPORT IS EVIDENTIARY OR LOGICAL; REFERENCE IS NOT.**

---

# 4. `evaluates`

## Controlled Definition

`evaluates` means that a governed evaluation process applies criteria, rules, and evidence to a subject, assertion, or canonical object.

Example:

```text
Rule-Constrained Evaluation
    evaluates
Attestation
```

This is a process-to-subject relationship.

## Controlled Distinctions

- evaluates ≠ derived-from
- evaluates ≠ results-in
- evaluates ≠ ownership

The evaluation acts upon the subject but does not replace it.

## Governing Rule

> **EVALUATES IDENTIFIES WHAT THE PROCESS ACTS UPON.**

---

# 5. `results-in`

## Controlled Definition

`results-in` means that a governed process or event produces a resulting state, determination, output, or canonical object.

Examples:

```text
Rule-Constrained Evaluation
    results-in
Evaluation Outcome
```

```text
Certification Review
    results-in
Certification Decision
```

This is a causal or process-output relationship.

## Controlled Distinctions

- results-in ≠ derived-from
- results-in ≠ evaluates

`results-in` answers:

> **What did this process produce?**

`derived-from` answers:

> **What source or prior object did this downstream thing originate from?**

## Governing Rule

> **RESULTS-IN DESCRIBES PROCESS OUTPUT; DERIVED-FROM DESCRIBES LINEAGE.**

---

# 6. `supersedes`

## Controlled Definition

`supersedes` means that one object or version replaces another in current operative standing while preserving the earlier object's identity and history.

Example:

```text
TRST-2026-0002
    supersedes
TRST-2026-0001
```

The inverse relationship may be expressed as:

```text
TRST-2026-0001
    superseded-by
TRST-2026-0002
```

## Controlled Distinctions

- supersedes ≠ corrects
- supersedes ≠ deletes
- supersedes ≠ mutates

The earlier object remains historically identifiable.

## Governing Rule

> **SUPERSESSION CHANGES OPERATIVE STANDING WITHOUT ERASING PRIOR IDENTITY.**

---

# 7. `corrects`

## Controlled Definition

`corrects` means that a later version or object fixes an error, omission, or defect in an earlier version or object.

Example:

```text
Version 1.1
    corrects
Version 1.0
```

This relationship records remedial intent.

It does not necessarily mean that the corrected object has a new canonical identity.

## Non-Material Correction

```text
Same canonical object
New version
    corrects
Prior version
```

## Material Change

```text
New canonical object
    may supersede
Prior object
```

## Controlled Distinction

> **corrects ≠ supersedes by definition**

A correction may also supersede where both relationships are accurate, but neither should be inferred from the other.

## Governing Rule

> **CORRECTS REPAIRS; SUPERSEDES REPLACES OPERATIVE STANDING.**

---

# 8. `related-to`

## Controlled Definition

`related-to` means that two objects have a meaningful association, but no more precise governed relationship has been established.

Example:

```text
Object A
    related-to
Object B
```

This is the weakest acceptable relationship in the controlled vocabulary.

## Usage Rule

Use `related-to` only when none of the stronger relationship types accurately apply.

Do not use it as a generic replacement for:

- references
- derived-from
- supports
- evaluates
- results-in
- supersedes
- corrects

## Governing Rule

> **RELATED-TO IS A FALLBACK RELATIONSHIP, NOT THE DEFAULT.**

---

# 9. Comparative Relationship Model

```text
references
→ points to

derived-from
→ originates from / is generated from

supports
→ provides evidentiary or logical support

evaluates
→ process acts upon subject

results-in
→ process produces outcome or output

supersedes
→ replaces operative standing

corrects
→ repairs prior error or defect

related-to
→ generic association when no stronger term applies
```

---

# 10. Collision Boundaries

## `references` vs `derived-from`

A reference is a pointer.

Derivation is lineage.

> **REFERENCE DOES NOT IMPLY DERIVATION.**

## `references` vs `supports`

A reference may be neutral.

Support is substantive.

> **REFERENCE DOES NOT IMPLY SUPPORT.**

## `derived-from` vs `supports`

A downstream object may derive from a source without that source proving the downstream conclusion.

> **DERIVATION DOES NOT AUTOMATICALLY IMPLY EVIDENTIARY SUPPORT.**

## `evaluates` vs `results-in`

`evaluates` identifies the subject of the process.

`results-in` identifies the output of the process.

Example:

```text
Rule-Constrained Evaluation
    evaluates
Attestation

Rule-Constrained Evaluation
    results-in
Evaluation Outcome
```

> **EVALUATES ≠ RESULTS-IN**

## `corrects` vs `supersedes`

A correction repairs.

A supersession replaces operative standing.

A new version may legitimately have both relationships:

```text
Version 1.1
    corrects
Version 1.0

Version 1.1
    supersedes
Version 1.0
```

where both statements are accurate.

> **CORRECTS ≠ SUPERSEDES**

---

# 11. Authority Boundary

None of the controlled relationship types transfers authority by itself.

Examples:

```text
SREG
    references
Certification Package
```

does not grant Registry certification authority.

```text
Trust Statement
    derived-from
Attestation
```

does not erase the Attestation's canonical identity.

```text
Chronicle Entry
    related-to
Integrity Reference
```

does not transfer Anchor authority to Chronicle.

Therefore:

> **RELATIONSHIP DOES NOT TRANSFER AUTHORITY.**

---

# 12. Controlled Relationship Matrix

| Term | Controlled Meaning |
|---|---|
| `references` | Points to or identifies another object |
| `derived-from` | Originated or was generated from another object |
| `supports` | Provides substantive evidentiary or logical support |
| `evaluates` | Governed process acts upon a subject or object |
| `results-in` | Process produces a determination, state, or output |
| `supersedes` | Replaces another object or version in operative standing |
| `corrects` | Repairs an error or defect in an earlier object or version |
| `related-to` | Generic association when no stronger relationship applies |

---

# 13. Prohibited Semantic Collapses

The Suite must not treat the following as equivalent:

- references = derived-from
- references = supports
- derived-from = supports
- evaluates = results-in
- supersedes = corrects
- supersedes = mutation
- corrects = deletion
- related-to = any stronger typed relationship
- relationship = authority transfer
- connection = identity

---

# 14. Suite-Wide Rules

The Relationship Vocabulary Reconciliation establishes the following rules:

1. Every relationship should use the most precise supported semantic term.
2. `references` is neutral linkage.
3. `derived-from` records lineage.
4. `supports` records evidentiary or logical support.
5. `evaluates` identifies the subject of a governed evaluation.
6. `results-in` identifies a process output.
7. `supersedes` changes operative standing while preserving history.
8. `corrects` records remedial change.
9. `related-to` is a fallback relationship only.
10. Relationship type does not imply identity.
11. Relationship type does not transfer authority.
12. **REFERENCE ≠ DERIVATION ≠ SUPPORT.**
13. **EVALUATES ≠ RESULTS-IN.**
14. **SUPERSEDES ≠ CORRECTS.**
15. **CONNECTION ≠ IDENTITY.**
16. **RELATIONSHIP DOES NOT TRANSFER AUTHORITY.**

---

# Governing Formulation

> **RELATIONSHIPS MUST SAY WHAT THE CONNECTION MEANS — NOT MERELY THAT A CONNECTION EXISTS.**

---

# Final Disposition

**Relationship Vocabulary Reconciliation — COMPLETE — APPROVED**

This record should govern future relationship metadata, cross-institution references, derivation chains, evidentiary support, process-output semantics, supersession, correction history, and documentation conformance across the Satoshium Suite.
