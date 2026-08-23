# Chronicle Validation Behavior

## Status

**Phase VIII — Validation and Operational Procedure**

This document defines how Satoshium Chronicle responds to Validation outcomes.

It operates together with:

```text
/chronicle/validation/index.html
/chronicle/validation/README.md
/chronicle/validation/chronicle-validation-rules.md
/chronicle/validation/chronicle-validation-sequence.md
```

---

# Purpose

Chronicle Validation produces a conformance result for one defined Chronicle Entry Version.

The authoritative outcome model is:

```text
PASS
FAIL
```

This document defines what happens after either result.

Validation behavior must remain distinct from:

```text
Preservation Eligibility
Verification
Correction
Versioning
Publication
Historical Preservation
```

---

# Core Principle

Validation establishes whether the current Chronicle representation conforms.

It does not establish whether the historical Occurrence itself is true or false.

Therefore:

```text
Validation PASS
  = current representation conforms

Validation FAIL
  = current representation does not yet conform
```

---

# PASS Behavior

When the overall Validation result is:

```text
PASS
```

Chronicle may move the Entry forward toward the Publication decision.

The operational path is:

```text
Validation PASS
        ↓
CHR-VAL-011 Publication Readiness PASS
        ↓
Eligible to Proceed to Publication Gate
        ↓
Publication Gate Decision
```

PASS means:

* all applicable blocking Validation Rules passed;
* no unresolved prerequisite failure remains;
* applicable schema and Profile requirements are satisfied;
* required authority and Provenance requirements are satisfied;
* Publication Readiness passed.

PASS does not mean:

* the Entry is automatically published;
* the historical Occurrence has been independently proven by Chronicle;
* Chronicle has acquired authority belonging to another institution;
* future Revalidation can never be required.

---

# FAIL Behavior

When the overall Validation result is:

```text
FAIL
```

the current Entry Version does not proceed through the Publication gate.

Instead:

```text
Validation FAIL
        ↓
Failed Rule Identified
        ↓
Entry Returned for Correction / Completion / Review
        ↓
Reverification if Required
        ↓
Revalidation
```

The Entry should return to the production function capable of resolving the defect.

Examples:

```text
Identifier failure
  → Identifier review

Schema failure
  → Entry construction

Event-Type Profile failure
  → classification / Profile review

Controlled Value failure
  → classification correction

Authoritative-reference failure
  → reference review

Date / time failure
  → temporal correction

Relationship failure
  → Relationship review

Provenance failure
  → Provenance review

Correction / Version failure
  → Correction / Versioning process

Verification dependency failure
  → Verification

Publication Readiness failure
  → publication preparation
```

---

# Validation Failure Does Not Delete the Entry

A Validation failure must not automatically delete a Chronicle Entry.

The current representation may be incomplete, malformed, inconsistent, or otherwise nonconforming while the underlying preservation decision remains valid.

Therefore:

```text
Validation FAIL
        ≠
Delete Entry
```

The preferred response is:

```text
Correct
Complete
Review
Reverify where necessary
Revalidate
```

If the Entry is already published, Chronicle must use applicable Correction, Versioning, Publication, and Lifecycle procedures.

---

# Validation Failure Does Not Erase the Occurrence

Validation evaluates Chronicle's representation.

It does not determine whether the underlying historical Occurrence happened.

Therefore:

```text
Validation FAIL
        ≠
Occurrence False
```

A failed Entry may still represent a genuine and preservation-worthy Occurrence.

The failure may concern only:

```text
structure
classification
missing field
invalid reference
incorrect date format
Relationship defect
Provenance deficiency
Version inconsistency
publication prerequisite
```

---

# Validation Failure Does Not Reopen Preservation Eligibility Automatically

Preservation Eligibility asks:

```text
Should Chronicle preserve this Occurrence?
```

Validation asks:

```text
Does the resulting Entry conform?
```

A Validation failure ordinarily means:

```text
Occurrence remains eligible
        +
Entry representation requires correction
```

Preservation Eligibility should be reopened only when the Validation failure reveals that the original eligibility decision itself depended on materially incorrect assumptions.

---

# Validation Failure Does Not Override External Authority

If a certification-related Chronicle Entry fails Validation:

```text
Certifier's Certification Package
```

does not become invalid because Chronicle's representation failed.

Likewise, Validation failure does not invalidate:

```text
Registry SREG
Anchor Integrity Reference
Beacon Discovery Signal
Attestor Trust Statement
Navigator Workflow Definition
Atlas authoritative material
```

Chronicle may identify a problem in its reference to those objects.

It does not invalidate the authoritative object merely through Chronicle Validation.

---

# Correction After FAIL

A FAIL result should identify the failed requirement precisely enough to support correction.

At minimum:

```text
CHR-VAL rule
affected field or domain
failure reason
blocking condition
required corrective action
Reverification requirement
Revalidation scope
```

Where correction materially changes the Entry:

```text
prior state preserved
        ↓
Correction documented
        ↓
new Entry Version where required
        ↓
Reverification
        ↓
Revalidation
```

The governing principle remains:

> Correct forward. Preserve backward.

---

# Initial Unpublished Entry Failure

For a draft Entry that has never been published, Validation failure may ordinarily return the draft for correction without creating unnecessary formal historical lineage for trivial drafting mistakes.

However, if the change is material enough that Chronicle has already treated the prior state as a governed Entry Version, Versioning rules apply.

The production procedure should distinguish:

```text
ordinary pre-publication drafting correction
```

from:

```text
material governed Correction / Version change
```

---

# Published Entry Failure

If an already-published Entry later fails Validation:

```text
Failure Identified
        ↓
Current Publication Condition Reviewed
        ↓
Correction / New Version where required
        ↓
Reverification
        ↓
Revalidation
        ↓
Republish / Maintain / Withdraw as governed
```

Chronicle must preserve the prior material state.

A later Validation failure is not permission to erase the historical record.

---

# Revalidation Behavior

After correction, Chronicle determines whether Revalidation should be:

```text
Targeted
```

or:

```text
Full
```

## Targeted Revalidation

Appropriate when:

* the changed domain is isolated;
* dependencies are known;
* unaffected Validation domains remain reliable.

## Full Revalidation

Appropriate when:

* the Entry Version materially changed;
* multiple domains changed;
* the dependency scope is unclear;
* authority, Provenance, Event Type, or Profile selection changed;
* prior Validation reliability is uncertain.

Publication Readiness must always be reevaluated after any blocking failure is corrected.

---

# No Numerical Outcome Substitution

Chronicle does not convert PASS / FAIL into a numerical confidence model.

Examples that must not replace the official result:

```text
95% valid
8.5 / 10
high confidence
mostly compliant
```

A non-blocking note may exist.

But:

```text
blocking requirement failed
        =
FAIL
```

---

# Warnings and Notes

Chronicle may preserve:

```text
warnings
limitations
informational findings
maintenance notes
```

without creating additional official Validation States.

A warning may coexist with:

```text
PASS
```

only when it is genuinely non-blocking.

A blocking condition must produce:

```text
FAIL
```

---

# Publication Gate

The governing publication behavior is:

```text
PASS
  → Entry may proceed to the separate Publication Gate

FAIL
  → Entry returns for correction / completion / review
```

Neither outcome performs Publication itself.

Publication remains a separate institutional act.

---

# Behavioral Summary

```text
PASS
  current Entry Version conforms
  may proceed toward Publication

FAIL
  current Entry Version does not yet conform
  returns for correction / completion / review

FAIL does not:
  delete the Entry
  erase the Occurrence
  invalidate an external authoritative object
  automatically reverse Preservation Eligibility
  transfer authority
  permit silent rewriting
```

---

# First Production Application

This behavior model has now been exercised in production.

For:

```text
CHR-2026-0001
Entry Version 1
```

Chronicle recorded:

```text
Verification:
verified

Overall Validation:
PASS

CHR-VAL-011 — Publication Readiness:
PASS

Publication Gate:
APPROVED FOR PUBLICATION

Publication State after publication:
published
```

The production case confirmed the intended behavior:

```text
Validation PASS
        ↓
Publication Readiness PASS
        ↓
Publication Gate approval
        ↓
separate Publication action
```

The Validation result itself did not publish the Entry or change `publication_state`.

---

# Guiding Principle

> Validation judges the representation, not the existence of the history.

And operationally:

> PASS may proceed. FAIL must return. Neither result erases history.

