# Validation

## Overview

**Validation** determines whether a Satoshium Anchor Integrity Reference satisfies Anchor's structural and institutional requirements.

Validation is distinct from Verification.

```text
Validation
→ Does the Integrity Reference satisfy Anchor's requirements?

Verification
→ Does the Reviewed Representation match the preserved integrity evidence?
```

The governing principle is:

> Validate the institution before publishing the record.

---

## Validation Outcome

Formal Validation produces:

```text
PASS
```

or:

```text
FAIL
```

A blocking rule failure produces overall:

```text
FAIL
```

`NOT APPLICABLE` may be recorded at the individual-rule level where needed, but it is not a third overall outcome.

---

## Validation Sequence

The production sequence is now:

```text
Integrity Reference constructed
        ↓
Anchor Identifier assigned
        ↓
Anchor Version assigned
        ↓
Formal Validation
        ↓
Initial Verification
        ↓
canonical HTML / JSON consistency
        ↓
Publication Gate
        ↓
Published Integrity Reference
```

If Validation remediation changes integrity-relevant content, Initial Verification must use the corrected production Version.

---

## Identifier Assignment Resolution

Validation resolves the earlier open question about when a production Anchor Identifier is assigned.

Because:

```text
anchor_identifier
```

is required by the Integrity Reference Base Schema and Validation must evaluate the real production candidate:

```text
Anchor Identifier assignment
→ before formal Validation
```

However:

```text
Anchor Identifier assigned
≠
publicly authoritative
```

Public authority begins only after Publication Gate approval and publication.

Once assigned, a production Anchor Identifier should not be recycled for a different Integrity Reference.

---

## Validation Rule Families

The initial rule set covers:

```text
Identity
Source
Representation
Integrity Method
Provenance
Relationships
Record State
Versioning
Corrections
Verification Readiness
Publication Readiness
Human / Machine Consistency
```

The detailed governed rule set is maintained in:

```text
anchor-validation-rules.md
```

---

## Validation vs. Schema Validation

JSON Schema validation is necessary but not sufficient.

Schema validation asks whether data has the required machine-readable structure.

Anchor Validation additionally asks whether the record is institutionally coherent.

For example, JSON Schema may accept two non-empty strings for:

```text
source_system_identifier
anchor_identifier
```

while Anchor Validation must still reject a record that improperly reuses the same identifier for both authorities.

---

## Validation vs. Verification

```text
Validation
≠
Verification
```

A record may be structurally and institutionally valid but fail to match the reviewed representation.

A record may cryptographically match while still violate Anchor requirements.

Publication requires both.

---

## Validation vs. Publication

```text
Validation PASS
≠
Publication Gate APPROVED
```

Validation is evidence for the Publication Gate.

The Gate remains the institutional decision that permits a Version to become publicly authoritative.

---

## Rule Numbering

The initial rule set uses:

```text
VAL-001
through
VAL-042
```

These identifiers are stable within the 1.0-draft Validation Rule Set.

They identify Validation rules, not Anchor-owned Integrity References.

Future rule revisions should preserve historical meaning rather than silently changing what an existing rule number means.

---

## Validation Record

A future formal Validation record should preserve at least:

```text
Anchor Identifier
Anchor Version
Schema Version
Validation Rule Set Version
validated_at
individual rule results
overall PASS / FAIL
```

Whether Validation records receive their own institutional identifiers remains unfrozen.

---

## First Production Application

The first published production Integrity Reference, `ANCH-2026-0001`, has exercised the Validation and Publication boundaries. Its defined source representation is the complete canonical JSON for `SCRD-SC-CERT-2026-0001`.

This first production case establishes operational use of the current rule framework; it does **not** prove every possible rule, failure path, or later extension has been exercised. Future reviews should assess:

```text
rules that block useful production
rules that fail to catch ambiguity
rules that duplicate Schema
rules that should become machine-enforced
rules that should remain procedural
new rules proven necessary
```

Validation PASS alone does not perform Initial Verification, approve the Publication Gate, or publish the Integrity Reference.

---

## Status

**Operational · Production-Exercised Anchor Validation**

Anchor Validation semantics, PASS/FAIL behavior, rule families, rule numbering, publication relationship, and identifier-assignment timing are now defined.

**Validation Rule Set:** 1.0-draft  
**Maintained By:** Satoshium
