# Satoshium Suite Interoperability Review — Relationship Serialization Review

**Date:** October 3, 2026  
**Review:** Satoshium Suite Interoperability Review  
**Step:** 6 — Review Relationship Serialization  
**Status:** COMPLETE — APPROVED

---

## Purpose

This review tests the settled Satoshium Suite relationship vocabulary across institutional boundaries and defines how each relationship should be encoded, resolved, interpreted, and directionally preserved in machine-facing interoperability.

The settled relationship vocabulary is:

```text
references
derived-from
supports
evaluates
results-in
supersedes
corrects
related-to
```

This review standardizes representation.

It does not redefine relationship meaning.

The governing distinctions remain:

```text
REFERENCE ≠ DERIVATION
REFERENCE ≠ SUPPORT
EVALUATES ≠ RESULTS-IN
SUPERSEDES ≠ CORRECTS
CONNECTION ≠ IDENTITY
```

And:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

---

# 1. Relationship Serialization Objective

Every cross-institution relationship must carry enough information to answer:

```text
What object is the subject?
What object is the target?
What relationship is being asserted?
What direction does the relationship run?
Which institution is asserting or recording it?
What provenance supports the relationship?
What version / state context applies?
Is the relationship current, historical, superseded, corrected, or unresolved?
```

A machine-readable relationship must not rely on prose, identifier similarity, page location, or record order to convey its meaning.

---

# 2. Minimum Machine Relationship Envelope

The following fields are adopted as the minimum relationship-serialization structure.

| Field | Requirement | Purpose |
|---|---|---|
| `subject_identifier` | **REQUIRED** | Identifies the object from which the relationship is asserted. |
| `relationship_type` | **REQUIRED** | Uses one governed relationship value. |
| `object_identifier` | **REQUIRED** | Identifies the target object. |
| `subject_institution` | **REQUIRED** | Identifies the institution governing the subject object. |
| `object_institution` | **REQUIRED** | Identifies the institution governing the target object. |
| `direction` | **REQUIRED** | Preserves subject → relationship → object direction. |
| `relationship_provenance` | **REQUIRED** | Records how the relationship was established or observed. |
| `authority_context` | **REQUIRED** | Preserves institutional authority boundaries. |
| `effective_time` | **REQUIRED WHEN MATERIAL** | Records when the relationship became applicable or was observed. |
| `version_scope` | **REQUIRED WHEN MATERIAL** | Identifies source/target versions where the relationship is version-specific. |
| `relationship_state` | **REQUIRED WHEN GOVERNED** | Indicates current, historical, superseded, corrected, unresolved, or equivalent governed state. |

Institution-specific extensions are permitted.

The common envelope is an interoperability structure, not a canonical Suite object.

---

# 3. Directionality Model

The machine form is:

```text
SUBJECT
→ RELATIONSHIP TYPE
→ OBJECT
```

Example:

```text
TRST-2026-0001
→ derived-from
→ ATT-2026-0001
```

The reverse relationship must not be inferred unless separately encoded or explicitly computable under a governed inverse mapping.

Therefore:

```text
A derived-from B
≠ automatically serialized as
B derived-from A
```

Directionality is mandatory for all relationship types in the common exchange model.

---

# 4. `references`

## Meaning

```text
references
→ points to / identifies
```

A reference says that one object identifies, cites, uses, or points to another object.

It does not establish:

```text
derivation
support
authority transfer
ownership
certification
trust
identity merger
```

## Encoding

```text
subject_identifier
relationship_type: references
object_identifier
```

## Direction

Directional.

Example:

```text
BEAC-2026-0001
→ references
→ SC-CERT-2026-0001
```

## Resolution

The target identifier should resolve through the originating institution's canonical resolution path or declared public/machine reference.

## Interpretation

The target remains governed by its source institution.

### Determination

**PASS**

`references` is suitable as the default explicit pointer relationship when no stronger governed relationship is intended.

---

# 5. `derived-from`

## Meaning

```text
derived-from
→ establishes lineage / origin
```

This relationship asserts that the subject was produced from, generated from, or materially originates from the object.

## Encoding

```text
subject_identifier
relationship_type: derived-from
object_identifier
```

## Direction

Directional.

Correct:

```text
TRST-2026-0001
→ derived-from
→ ATT-2026-0001
```

Incorrect reversal:

```text
ATT-2026-0001
→ derived-from
→ TRST-2026-0001
```

unless a separately governed relationship says so.

## Resolution

Both subject and object must remain independently resolvable canonical identities.

## Interpretation

Derivation establishes lineage.

It does not transfer authority.

### Determination

**PASS**

---

# 6. `supports`

## Meaning

```text
supports
→ provides evidentiary or logical support
```

This is stronger than `references`.

A source may be referenced without supporting a conclusion.

## Encoding

```text
subject_identifier
relationship_type: supports
object_identifier
```

The implementation must define whether the subject is the supporting evidence or the supported assertion/object and keep that convention stable Suite-wide.

For this review, the adopted convention is:

```text
supporting object
→ supports
→ supported object / assertion
```

## Direction

Directional.

## Resolution

The relationship must preserve the provenance of the supporting object and the authority of both sides.

## Interpretation

Support is evidentiary or logical.

It does not itself establish:

```text
truth
certification
validation
trust
authority transfer
```

### Determination

**APPROVED WITH DIRECTION CONVENTION**

The Suite should serialize the supporting object as subject and the supported object/assertion as target.

---

# 7. `evaluates`

## Meaning

```text
evaluates
→ process / governed evaluation acts on subject matter
```

This relationship records that an evaluation process or governed evaluation object acts on another object, assertion, or input.

## Encoding

Preferred semantic pattern:

```text
evaluation-bearing subject
→ evaluates
→ evaluated object / assertion
```

Where the evaluation process itself is not a canonical object, the relationship may be carried by the canonical object that records or owns the evaluation context.

## Direction

Directional.

## Resolution

The target remains a distinct object.

## Interpretation

Evaluation does not merge the evaluator and evaluated object.

### Determination

**PASS WITH IMPLEMENTATION PROFILE REQUIRED**

Institution-specific serialization must state what object is permitted to be the relationship subject when the evaluation process itself is non-canonical.

---

# 8. `results-in`

## Meaning

```text
results-in
→ process or governed object produces an output / result
```

This relationship is distinct from `evaluates`.

## Encoding

```text
producing subject
→ results-in
→ produced result / output
```

Example conceptual pattern:

```text
Rule-Constrained Evaluation context
→ results-in
→ Evaluation Outcome / Trust Statement
```

Where the process is not itself canonical, the implementing institution must anchor the relationship in the appropriate canonical or governed process representation.

## Direction

Directional.

## Resolution

The resulting object or result must preserve its own identity and governing institution.

## Interpretation

The evaluated subject is not automatically the result.

### Determination

**PASS WITH IMPLEMENTATION PROFILE REQUIRED**

---

# 9. `supersedes`

## Meaning

```text
supersedes
→ replaces operative standing while preserving history
```

## Encoding

Adopted direction:

```text
newer / successor object
→ supersedes
→ prior object
```

## Direction

Directional.

## Resolution

Both objects must remain historically resolvable where policy permits.

## Interpretation

The prior object must not be silently mutated or deleted.

```text
supersedes
≠ corrects
≠ replaces identifier identity
```

### Determination

**PASS**

---

# 10. `corrects`

## Meaning

```text
corrects
→ repairs an error or defect in a prior object / representation
```

## Encoding

Adopted direction:

```text
correcting object / version
→ corrects
→ prior object / version
```

## Direction

Directional.

## Resolution

The prior object or prior version must remain historically traceable.

## Interpretation

Correction is distinct from:

```text
version
supersession
deletion
```

A correction may produce a new version or identity depending on the governing institution's rules, but `corrects` itself does not determine that outcome.

### Determination

**PASS**

---

# 11. `related-to`

## Meaning

```text
related-to
→ weakest general relationship
```

This relationship indicates a meaningful connection when no stronger governed relationship is appropriate or established.

## Encoding

```text
subject_identifier
relationship_type: related-to
object_identifier
```

## Direction

The semantic meaning may be symmetric in some contexts, but machine serialization must still preserve the direction in which the relationship was recorded.

If true symmetry is intended, implementations may either:

```text
encode one relationship with symmetry explicitly declared
```

or:

```text
encode reciprocal related-to edges
```

according to the eventual serialization standard.

## Resolution

Both objects remain independently resolvable.

## Interpretation

`related-to` must not be used as a convenience substitute for:

```text
references
derived-from
supports
evaluates
results-in
supersedes
corrects
```

### Determination

**APPROVED AS WEAK FALLBACK ONLY**

---

# 12. Strongest-Correct-Relationship Rule

The Suite adopts the following interoperability rule:

> **Use the strongest correct governed relationship that is actually supported by the evidence and architecture.**

Examples:

```text
If A is produced from B
→ use derived-from
→ not related-to

If A explicitly cites B
→ use references
→ not related-to

If A provides evidentiary support for B
→ use supports
→ not references alone where support is the intended semantic

If A replaces the operative standing of B
→ use supersedes
→ not related-to

If A repairs B
→ use corrects
→ not supersedes unless both are separately true and separately encoded
```

The stronger relationship must not be inferred unless supported.

Therefore:

```text
strongest correct
≠ strongest imaginable
```

---

# 13. Multi-Relationship Rule

Two objects may legitimately have more than one relationship.

Example:

```text
A references B
A derived-from B
```

may both be true.

If so, both relationships should be serialized independently.

One relationship must not be overloaded to carry multiple meanings.

Therefore:

```text
one edge
≠ multiple unstated semantics
```

---

# 14. Relationship Provenance

Every cross-institution relationship must preserve how the relationship became known.

Examples:

```text
declared by source object
declared by receiving object
observed from canonical public record
derived from production workflow evidence
established by governed review
imported from external source
```

Relationship provenance is separate from object provenance.

A relationship may be validly recorded even when the two objects have different source provenance histories.

---

# 15. Authority Context

No relationship transfers authority.

Examples:

```text
SREG-2026-0001
→ references
→ SC-CERT-2026-0001
```

does not make Registry the certification authority.

```text
BEAC-2026-0001
→ references
→ ANCH-2026-0001
```

does not make Beacon the integrity authority.

```text
TRST-2026-0001
→ derived-from
→ ATT-2026-0001
```

does not erase the independent identity of either Attestor object.

Authority context must remain explicit in the relationship envelope.

---

# 16. Version Scope

Some relationships attach to the canonical object generally.

Others attach to a specific version or observed state.

The serialization must distinguish:

```text
object-level relationship
version-level relationship
state-at-use relationship
historical relationship
```

A relationship that was true for Version 1.0 must not silently be treated as true for Version 2.0 if the semantic basis changed.

---

# 17. Relationship State

Where material, a relationship should be able to represent:

```text
current
historical
superseded
corrected
unresolved
inactive
unknown
```

These are relationship-state concepts, not object lifecycle states.

The serialization standard must not collapse:

```text
relationship_state
≠ lifecycle_state
```

---

# 18. Unknown Relationship Types

If an institution encounters an unsupported relationship type:

```text
unsupported
≠ related-to automatically
```

The implementation should preserve the original relationship token or source representation where possible and mark it unsupported or unmapped.

Silent coercion to `related-to` is prohibited.

---

# 19. Cross-Institution Vocabulary Test

| Relationship | Meaning Stable Across Boundaries? | Direction Required? | Target Must Resolve Independently? | Authority Transfer? | `related-to` Substitute Allowed? |
|---|---:|---:|---:|---:|---:|
| references | Yes | Yes | Yes | No | No |
| derived-from | Yes | Yes | Yes | No | No |
| supports | Yes | Yes | Yes | No | No |
| evaluates | Yes | Yes | Yes | No | No |
| results-in | Yes | Yes | Yes | No | No |
| supersedes | Yes | Yes | Yes | No | No |
| corrects | Yes | Yes | Yes | No | No |
| related-to | Yes, weak/general | Preserve recorded direction | Yes | No | N/A |

---

# 20. Relationship Encoding Model

Recommended conceptual serialization:

```yaml
relationship:
  subject_identifier: <canonical identifier>
  subject_institution: <institution>
  relationship_type: <governed relationship>
  object_identifier: <canonical identifier>
  object_institution: <institution>
  direction: subject-to-object
  relationship_provenance: <how established>
  authority_context: <authority remains institution-specific>
  effective_time: <timestamp or null>
  version_scope:
    subject_version: <value or null>
    object_version: <value or null>
  relationship_state: <current/historical/etc.>
```

The exact machine syntax may vary.

The semantic fields must remain compatible.

---

# 21. Findings

## RS-01 — Settled vocabulary remains coherent

**PASS**

The eight governed relationship types remain semantically distinct across institutional boundaries.

---

## RS-02 — Directionality

**APPROVED**

All relationship types must preserve subject → relationship → object direction in machine serialization.

For semantically symmetric uses of `related-to`, symmetry must be explicitly represented rather than assumed from omission of direction.

---

## RS-03 — `references`

**PASS**

Suitable for explicit pointer/reference semantics without authority transfer.

---

## RS-04 — `derived-from`

**PASS**

Suitable for lineage/origin and must not be confused with reference.

---

## RS-05 — `supports`

**APPROVED WITH DIRECTION CONVENTION**

Supporting object → supports → supported object/assertion.

---

## RS-06 — `evaluates`

**PASS WITH IMPLEMENTATION PROFILE REQUIRED**

Institution-specific schemas must identify the valid relationship-bearing subject.

---

## RS-07 — `results-in`

**PASS WITH IMPLEMENTATION PROFILE REQUIRED**

Institution-specific schemas must identify the producing relationship-bearing subject.

---

## RS-08 — `supersedes`

**PASS**

Successor → supersedes → prior object.

Historical resolution must remain possible.

---

## RS-09 — `corrects`

**PASS**

Correcting object/version → corrects → prior object/version.

---

## RS-10 — `related-to`

**APPROVED AS WEAK FALLBACK ONLY**

It must not replace a stronger governed relationship.

---

## RS-11 — Unsupported relationships

**APPROVED**

Unsupported or unknown predicates must remain explicit.

They must not silently degrade to `related-to`.

---

## RS-12 — Multi-relationship support

**APPROVED**

Multiple independently true relationships between the same objects should be encoded separately.

---

# Review Determination

The Suite's settled relationship vocabulary is sufficient for cross-institution interoperability.

No relationship meaning requires redesign.

The remaining work is implementation standardization around:

```text
common field names
machine predicate tokens
direction encoding
relationship provenance
version scope
relationship state
inverse handling
symmetry declaration
unknown predicate handling
```

These are serialization questions, not architecture questions.

---

# FINAL DISPOSITION

# RELATIONSHIP SERIALIZATION REVIEW — COMPLETE — APPROVED

Adopted interoperability rule:

> **Use the strongest correct governed relationship actually supported by the architecture and evidence.**

And preserve:

```text
REFERENCE ≠ DERIVATION
REFERENCE ≠ SUPPORT
EVALUATES ≠ RESULTS-IN
SUPERSEDES ≠ CORRECTS
RELATED-TO = WEAKEST FALLBACK
```

All machine relationships must preserve explicit subject/object direction, relationship provenance, version scope where material, and institutional authority boundaries.

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**
