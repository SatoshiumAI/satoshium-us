# Chronicle Validation Sequence

## Status

**Phase VIII — Validation and Operational Procedure**

This document defines the formal execution order for applying the Satoshium Chronicle Validation Rules to a production Chronicle Entry.

It operates together with:

```text
/chronicle/validation/index.html
/chronicle/validation/README.md
/chronicle/validation/chronicle-validation-rules.md
```

The governing Validation Rules are identified as:

```text
CHR-VAL-001 through CHR-VAL-014
```

---

# Purpose

The Chronicle Validation Rules define **what must be true**.

The Chronicle Validation Sequence defines **the order in which Chronicle evaluates those rules**.

The sequence exists to ensure that:

* prerequisite checks occur before dependent checks;
* machine-readable failures are identified before deeper institutional review;
* conditional rules are evaluated only when applicable;
* blocking failures are recorded consistently;
* Validation does not become an unordered checklist;
* PASS / FAIL behavior remains repeatable across Entries.

---

# Governing Principle

Validation proceeds from foundational identity and structure toward institutional coherence and publication readiness.

Conceptually:

```text
Identity
        ↓
Structure
        ↓
Specialization
        ↓
Controlled Meaning
        ↓
Required Content
        ↓
Authority
        ↓
Time
        ↓
Relationships
        ↓
Provenance
        ↓
Historical Lineage
        ↓
Verification Dependency
        ↓
Authority Boundary Integrity
        ↓
Cross-Format Consistency
        ↓
Publication Readiness
        ↓
Overall Result
```

---

# Canonical Validation Sequence

The standard Chronicle Validation order is:

```text
Entry Received for Validation
        ↓
CHR-VAL-001 — Entry Identifier
        ↓
CHR-VAL-002 — Base Schema Conformance
        ↓
CHR-VAL-003 — Event-Type Profile Conformance
        ↓
CHR-VAL-004 — Controlled Values
        ↓
CHR-VAL-005 — Required and Conditional Fields
        ↓
CHR-VAL-006 — Authoritative References
        ↓
CHR-VAL-007 — Date and Time Formatting
        ↓
CHR-VAL-008 — Relationship Integrity
        ↓
CHR-VAL-009 — Provenance
        ↓
CHR-VAL-010 — Correction and Version Consistency
        ↓
CHR-VAL-012 — Verification Dependency
        ↓
CHR-VAL-013 — Authority Boundary Integrity
        ↓
CHR-VAL-014 — Human and Machine Consistency
        ↓
CHR-VAL-011 — Publication Readiness
        ↓
Overall Validation Result
```

Publication Readiness is intentionally evaluated near the end because it depends on the preceding Validation domains.

---

# Step 0 — Entry Received for Validation

Before CHR-VAL-001 begins, Chronicle should identify the exact Entry state being evaluated.

Minimum intake context:

```text
entry_id
entry_version
schema_id
schema_version
event_type
event_type_profile where applicable
current Verification State
current Lifecycle State
current Publication State
```

The Entry supplied for Validation should be treated as one defined Version.

Validation must not silently combine fields from multiple Entry Versions.

---

# Step 1 — CHR-VAL-001: Entry Identifier

Chronicle first validates permanent Entry identity.

This check occurs first because all later Validation findings must attach to a defined Chronicle Entry.

Validate:

```text
identifier present
CHR-YYYY-NNNN pattern
Chronicle namespace
uniqueness
non-reuse
identity stability across Versions
assignment year distinction
```

## If PASS

Proceed to CHR-VAL-002.

## If FAIL

Record the failure.

If the identifier is missing or cannot identify the Entry being evaluated, later checks that depend on canonical identity may be marked:

```text
NOT EVALUATED — prerequisite failure
```

Schema checks that do not depend on issuance uniqueness may still be performed when useful.

---

# Step 2 — CHR-VAL-002: Base Schema Conformance

Chronicle validates the Entry against the declared Chronicle Base Schema.

This step establishes whether the Entry has a valid universal structural foundation.

Validate:

```text
schema_id
schema_version
required universal fields
field names
field types
formats
conditional Base constraints
additional-property restrictions
machine-readable parseability
```

## If PASS

Proceed to CHR-VAL-003.

## If FAIL

Record all Base Schema failures.

Chronicle should normally continue far enough to identify additional actionable defects when the Entry can still be interpreted safely.

If the Entry cannot be parsed or its structure is too malformed to evaluate reliably, dependent checks may be marked:

```text
NOT EVALUATED — Base Schema prerequisite failure
```

---

# Step 3 — CHR-VAL-003: Event-Type Profile Conformance

Chronicle determines whether an approved Event-Type Profile applies.

Decision:

```text
Does this Entry require an Event-Type Profile?
        ↓
Yes → Validate Profile
No  → Mark CHR-VAL-003 Not Applicable
```

When applicable, validate:

```text
Profile identity
Profile Version
Profile-specific Required fields
Profile-specific constraints
Profile-specific Controlled Values
Profile-specific authoritative references
Profile-specific date rules
Profile-specific Provenance requirements
```

## If PASS

Proceed to CHR-VAL-004.

## If FAIL

Record each blocking Profile failure.

Continue with later checks where the Entry remains interpretable.

---

# Step 4 — CHR-VAL-004: Controlled Values

Chronicle validates all governed values applicable to the Entry.

Potential domains include:

```text
Event Type
Verification State
Lifecycle State
Publication State
Relationship Type
Source Type
Evidence Type
Correction Type
```

This step follows Base Schema and Profile Validation because those artifacts determine which fields and value constraints apply.

## If PASS

Proceed to CHR-VAL-005.

## If FAIL

Record the invalid value and the governing Controlled Value set.

Do not silently normalize or substitute another value during Validation.

---

# Step 5 — CHR-VAL-005: Required and Conditional Fields

Chronicle confirms that all fields required by the combined governing requirements are present.

Evaluate:

```text
Base Required fields
Base Conditional fields
Profile Required fields
Profile Conditional fields
state-dependent fields
publication-dependent fields
Correction / Version-dependent fields
```

Examples may include:

```text
event_type_profile
originating_system
authoritative_record_references
published_at
limitations
prior_version_reference
correction_references
```

## If PASS

Proceed to CHR-VAL-006.

## If FAIL

Record each missing or invalid Required / Conditional field.

Later rules may still be evaluated when possible.

---

# Step 6 — CHR-VAL-006: Authoritative References

Determine whether authoritative references are required.

Decision:

```text
Does the Entry or governing Profile require
an authoritative reference?
        ↓
Yes → Validate
No  → Mark Not Applicable
```

Validate:

```text
required reference exists
referenced object is identifiable
owning system is represented correctly
reference structure is valid
Profile-specific authority requirements are satisfied
reference does not imply authority transfer
```

For Certification Event-Type Profile Entries, confirm at least one structured reference includes:

```text
reference
system: certifier
```

## If PASS

Proceed to CHR-VAL-007.

## If FAIL

Record the reference failure.

A missing authoritative reference is ordinarily blocking for any Entry whose Profile requires one.

---

# Step 7 — CHR-VAL-007: Date and Time Formatting

Chronicle validates temporal fields after the structural and Profile-specific requirements are known.

Evaluate applicable values including:

```text
event_date
entry_created_at
retrieved_at
published_at
updated_at
Correction date
Version-related date
```

Validate both:

```text
format
meaning
```

Chronicle must preserve the distinction among:

```text
Occurrence time
Entry creation time
retrieval time
publication time
Correction time
Version state
```

## If PASS

Proceed to CHR-VAL-008.

## If FAIL

Record the temporal field, expected rule, and actual defect.

Do not substitute one timestamp for another to obtain a PASS.

---

# Step 8 — CHR-VAL-008: Relationship Integrity

Determine whether Relationships exist or are required.

Decision:

```text
Relationships present or required?
        ↓
Yes → Validate
No  → Mark Not Applicable
```

Validate:

```text
approved Relationship Type
target identity
target system where necessary
direction
inverse coherence where represented
duplicate prevention
contradiction handling
authority boundary
semantic meaning
```

Preserve:

```text
Precedes ≠ Causes
Supersedes ≠ Deletes
References ≠ Owns
Related To ≠ Authoritative For
```

## If PASS

Proceed to CHR-VAL-009.

## If FAIL

Record each material Relationship failure.

---

# Step 9 — CHR-VAL-009: Provenance

Every production Chronicle Entry requires Provenance Validation.

Validate the minimum:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference where required
Material Provenance Limitations where applicable
```

Also validate applicable:

```text
transfer_history
transformation_history
preservation_path
integrity_metadata
```

## If PASS

Proceed to CHR-VAL-010.

## If FAIL

Record the missing, contradictory, or unsupported Provenance requirement.

Unknown Provenance must remain unknown rather than being invented for Validation.

---

# Step 10 — CHR-VAL-010: Correction and Version Consistency

Determine whether the Entry has prior Versions or material Corrections.

Decision:

```text
Initial Entry with no prior material state?
        ↓
Yes → Mark Not Applicable
No  → Validate lineage
```

Where applicable, validate:

```text
stable entry_id
correct entry_version
prior Version reference
formal Correction where required
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
Reverification where required
Revalidation requirement
publication lineage
```

## If PASS

Proceed to CHR-VAL-012.

## If FAIL

Record the lineage defect.

Silent material rewriting is a blocking failure.

---

# Step 11 — CHR-VAL-012: Verification Dependency

Chronicle now checks whether the Verification prerequisite has been satisfied.

This occurs after the Entry's main structural and provenance domains have been reviewed because Validation should know what representation is actually being considered.

Validate:

```text
Verification performed where required
Verification State approved
Verification limitations preserved
Verification State sufficient for intended publication
```

## If PASS

Proceed to CHR-VAL-013.

## If FAIL

Record the Verification dependency failure.

Return the Entry to Verification when additional substantive review is required.

Validation does not perform the missing Verification itself.

---

# Step 12 — CHR-VAL-013: Authority Boundary Integrity

Chronicle performs an explicit institutional boundary review.

Validate that the Entry does not improperly claim authority belonging to:

```text
Certifier
Registry
Anchor
Beacon
Attestor
Navigator
Atlas
external institutions
```

Confirm:

```text
Chronicle owns the Chronicle Entry
referenced systems retain their own authority
external determinations remain externally owned
references do not become Chronicle determinations
```

## If PASS

Proceed to CHR-VAL-014.

## If FAIL

Record the authority-boundary defect.

Authority-boundary violations are blocking.

---

# Step 13 — CHR-VAL-014: Human and Machine Consistency

Determine whether both official human-readable and machine-readable representations exist for the Entry Version.

Decision:

```text
Both official forms exist?
        ↓
Yes → Compare
No  → Mark Not Applicable
```

Compare material fields including:

```text
Entry Identifier
Entry Version
title
summary
Event Type
Event Date
Historical Context
authoritative references
Relationships
Provenance
Verification State
Lifecycle State
Publication State
Correction references
prior-Version references
publication date
```

## If PASS

Proceed to CHR-VAL-011.

## If FAIL

Record every material cross-format inconsistency.

An Entry is not publication-ready when its official forms materially disagree.

---

# Step 14 — CHR-VAL-011: Publication Readiness

Publication Readiness is evaluated after the underlying Validation domains.

Chronicle confirms that:

```text
CHR-VAL-001 = PASS
CHR-VAL-002 = PASS
CHR-VAL-003 = PASS or Not Applicable
CHR-VAL-004 = PASS
CHR-VAL-005 = PASS
CHR-VAL-006 = PASS or Not Applicable
CHR-VAL-007 = PASS
CHR-VAL-008 = PASS or Not Applicable
CHR-VAL-009 = PASS
CHR-VAL-010 = PASS or Not Applicable
CHR-VAL-012 = PASS
CHR-VAL-013 = PASS
CHR-VAL-014 = PASS or Not Applicable
```

and that:

```text
no unresolved blocking Validation failure remains
Verification State satisfies publication requirements
material limitations are visible where required
authority boundaries remain intact
publication prerequisites are satisfied
```

## If PASS

The Entry becomes:

```text
Eligible to Proceed to Publication Decision
```

## If FAIL

The Entry returns to the appropriate production step.

Publication Readiness PASS does not itself publish the Entry.

---

# Step 15 — Determine Overall Validation Result

The overall result is binary:

```text
PASS
FAIL
```

## Overall PASS

Overall PASS requires:

```text
Every applicable blocking CHR-VAL rule = PASS
```

Rules legitimately determined to be:

```text
Not Applicable
```

do not prevent PASS.

## Overall FAIL

Overall FAIL occurs when:

```text
Any applicable blocking CHR-VAL rule = FAIL
```

A numerical score is not calculated.

---

# Rule Dependency Map

The principal dependencies are:

```text
CHR-VAL-001
  establishes canonical Entry identity

CHR-VAL-002
  establishes Base structural validity

CHR-VAL-003
  depends on Event Type / Profile applicability
  and specializes CHR-VAL-002

CHR-VAL-004
  depends on governing Base / Profile vocabularies

CHR-VAL-005
  depends on Base / Profile field requirements

CHR-VAL-006
  depends on Base / Profile authoritative-reference rules

CHR-VAL-007
  depends on Base / Profile temporal rules

CHR-VAL-008
  depends on Relationship fields and Controlled Values

CHR-VAL-009
  depends on required Provenance structure

CHR-VAL-010
  depends on Version / Correction history

CHR-VAL-012
  depends on completed Chronicle Verification

CHR-VAL-013
  reviews institutional meaning across the Entry

CHR-VAL-014
  depends on availability of both official forms

CHR-VAL-011
  depends on the preceding applicable rules
```

---

# Universal Validation Path

Every production Chronicle Entry follows at least:

```text
CHR-VAL-001
        ↓
CHR-VAL-002
        ↓
CHR-VAL-004
        ↓
CHR-VAL-005
        ↓
CHR-VAL-007
        ↓
CHR-VAL-009
        ↓
CHR-VAL-012
        ↓
CHR-VAL-013
        ↓
CHR-VAL-011
```

These are the minimum universal Validation domains.

---

# Conditional Validation Path

Conditional rules are inserted when their governing condition applies:

```text
CHR-VAL-003
  Event-Type Profile exists

CHR-VAL-006
  authoritative reference required

CHR-VAL-008
  Relationships exist or are required

CHR-VAL-010
  prior Version / material Correction exists

CHR-VAL-014
  both official human and machine forms exist
```

Once applicable, a conditional rule is blocking unless another governing rule explicitly says otherwise.

---

# Certification Event-Type Profile Sequence

A certification-related Entry follows the full specialization path:

```text
CHR-VAL-001 — Entry Identifier
        ↓
CHR-VAL-002 — Base Schema
        ↓
CHR-VAL-003 — Certification Event-Type Profile
        ↓
CHR-VAL-004 — Controlled Values
        ↓
CHR-VAL-005 — Required / Conditional Fields
        ↓
CHR-VAL-006 — Certifier Authoritative Reference
        ↓
CHR-VAL-007 — Non-null Event Date / Date-Time Rules
        ↓
CHR-VAL-008 — Relationships where applicable
        ↓
CHR-VAL-009 — Certification-specific Provenance
        ↓
CHR-VAL-010 — Version / Correction if applicable
        ↓
CHR-VAL-012 — Verification Dependency
        ↓
CHR-VAL-013 — Certifier / Registry / Chronicle Authority Boundaries
        ↓
CHR-VAL-014 — Human / Machine Consistency when both exist
        ↓
CHR-VAL-011 — Publication Readiness
        ↓
PASS / FAIL
```

---

# Failure Collection Strategy

Chronicle should distinguish between:

```text
Fatal prerequisite failure
```

and:

```text
Independent blocking failure
```

## Fatal Prerequisite Failure

A fatal prerequisite failure prevents reliable evaluation of later dependent rules.

Examples:

```text
machine-readable Entry cannot parse
Entry identity cannot be determined
governing schema cannot be identified
```

Dependent rules may be recorded as:

```text
NOT EVALUATED — prerequisite failure
```

The overall result remains:

```text
FAIL
```

## Independent Blocking Failure

An independent failure does not necessarily prevent later checks.

Example:

```text
one invalid Controlled Value
```

Chronicle should continue Validation where practical so the Entry can return with a fuller list of corrective actions.

---

# Continue-Where-Practical Rule

Chronicle should avoid unnecessarily stopping after the first failure.

Preferred behavior:

```text
Detect Failure
        ↓
Record Failure
        ↓
Determine Whether Later Rule Can Be Reliably Evaluated
        ↓
Yes → Continue
No  → Mark Dependent Rule Not Evaluated
```

This reduces repeated correction cycles.

---

# Not Evaluated

`Not Evaluated` is procedural, not an official Validation outcome.

It may be used only for an individual rule when a prerequisite failure makes evaluation unreliable.

Example:

```text
CHR-VAL-002 = FAIL
Entry cannot parse
        ↓
CHR-VAL-003 = NOT EVALUATED
```

The overall Entry result remains:

```text
FAIL
```

`Not Evaluated` must never be used to hide an applicable requirement that could have been evaluated.

---

# Not Applicable

`Not Applicable` means the rule does not govern the Entry.

Examples:

```text
No Event-Type Profile applies
  → CHR-VAL-003 Not Applicable

No Relationships exist or are required
  → CHR-VAL-008 Not Applicable

Initial Entry Version with no Correction
  → CHR-VAL-010 Not Applicable

No second official representation yet exists
  → CHR-VAL-014 Not Applicable
```

`Not Applicable` is distinct from:

```text
PASS
FAIL
NOT EVALUATED
```

---

# Validation Result Logic

The decision logic is:

```text
For each CHR-VAL Rule
        ↓
Determine Applicability
        ↓
If Not Applicable
  record N/A
        ↓
If Applicable
  evaluate
        ↓
PASS or FAIL
```

Then:

```text
Any applicable FAIL?
        ↓
Yes → Overall FAIL
No  → Continue
```

Then:

```text
Any applicable rule Not Evaluated
because of unresolved prerequisite failure?
        ↓
Yes → Overall FAIL
No  → Continue
```

Then:

```text
CHR-VAL-011 Publication Readiness PASS?
        ↓
Yes → Overall PASS
No  → Overall FAIL
```

---

# Revalidation Sequence

When an Entry returns after correction:

```text
Identify Changed Domain
        ↓
Determine Scope of Impact
        ↓
Targeted or Full Revalidation
        ↓
Re-run affected CHR-VAL Rules
        ↓
Re-run dependent downstream rules
        ↓
Always re-run CHR-VAL-011 Publication Readiness
        ↓
Record new Overall Result
```

Examples:

```text
Authoritative reference corrected
        ↓
Re-run CHR-VAL-006
        ↓
Re-run CHR-VAL-009 if Provenance references changed
        ↓
Re-run CHR-VAL-013
        ↓
Re-run CHR-VAL-011
```

and:

```text
Entry Version materially changed
        ↓
Re-run full Validation unless scope can
be reliably bounded
```

---

# Publication Gate Rule

No Entry may pass from Validation into publication preparation while:

```text
any applicable blocking rule = FAIL
```

or:

```text
any applicable rule remains NOT EVALUATED
because of an unresolved prerequisite failure
```

The gate is:

```text
Overall Validation PASS
        ↓
Eligible for Publication Decision
```

not:

```text
Overall Validation PASS
        ↓
Automatically Published
```

---

# Validation Record Sequence

At the end of Validation, Chronicle should preserve:

```text
Entry Identifier
Entry Version
Validation Date / Time
Rules Applied
Rule-by-Rule Result
Not Applicable Rules
Not Evaluated Rules
Blocking Failures
Overall Result
Base Schema Version
Event-Type Profile Version where applicable
Validation Method
Revalidation Requirement
Supporting Artifact Reference where applicable
```

The result must be traceable to the exact Entry Version evaluated.

---

# Initial Operational Checklist

The operational checklist is:

```text
[ ] Entry Version identified
[ ] CHR-VAL-001 Entry Identifier
[ ] CHR-VAL-002 Base Schema
[ ] CHR-VAL-003 Event-Type Profile or N/A
[ ] CHR-VAL-004 Controlled Values
[ ] CHR-VAL-005 Required / Conditional Fields
[ ] CHR-VAL-006 Authoritative References or N/A
[ ] CHR-VAL-007 Date / Time
[ ] CHR-VAL-008 Relationships or N/A
[ ] CHR-VAL-009 Provenance
[ ] CHR-VAL-010 Correction / Version or N/A
[ ] CHR-VAL-012 Verification Dependency
[ ] CHR-VAL-013 Authority Boundary Integrity
[ ] CHR-VAL-014 Human / Machine Consistency or N/A
[ ] CHR-VAL-011 Publication Readiness
[ ] Overall PASS / FAIL recorded
```

---

# Sequence Principle

> Validate foundations before dependencies.

> Continue where practical so failures are actionable.

> A conditional rule becomes blocking when its condition applies.

> Publication Readiness is the final Validation gate.

> PASS means all applicable blocking requirements passed.

> FAIL means at least one applicable blocking requirement did not.

---

# Phase VIII Role

This sequence converts the Chronicle Validation Rules from a normative rule set into an operational order.

The Phase VIII relationship is now:

```text
Chronicle Validation Public Explanation
        ↓
Chronicle Validation Institutional Specification
        ↓
Chronicle Validation Rules
        ↓
Chronicle Validation Sequence
        ↓
Chronicle Entry Production Procedure
```

The next Phase VIII work can therefore define explicit Validation outcome handling and then incorporate the complete Validation sequence into the Chronicle Entry Production Procedure.
