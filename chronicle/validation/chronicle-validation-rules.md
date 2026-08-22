# Chronicle Validation Rules

## Status

**Phase VIII — Validation and Operational Procedure**

This document defines the normative Validation Rules applied to production Satoshium Chronicle Entries.

It is an institutional artifact of:

```text
/chronicle/validation/
```

and operates together with:

```text
/chronicle/validation/index.html
/chronicle/validation/README.md
/chronicle/schemas/chronicle-base-schema.json
applicable Event-Type Profiles
Chronicle Controlled Values
Chronicle Identifier rules
Chronicle Relationship rules
Chronicle Provenance requirements
Chronicle Versioning and Correction rules
```

---

# Purpose

Chronicle Validation determines whether the current Chronicle Entry Version conforms to the institutional and machine-readable requirements that govern it.

The core question is:

> Does this Chronicle Entry conform to the requirements governing this Entry Version?

Validation applies to Chronicle's own record.

It does not transfer authority from another Satoshium Suite institution.

---

# Governing Distinction

```text
Schema
  defines structure.

Verification
  reviews Chronicle's historical representation.

Validation
  tests conformance.

Publication
  determines public production state.
```

Therefore:

```text
Schema ≠ Verification ≠ Validation ≠ Publication
```

---

# Validation Outcome Model

Chronicle uses a deliberately simple Validation outcome model:

```text
PASS
FAIL
```

Chronicle does not use a universal numerical Validation confidence score.

A percentage, points system, or generalized confidence number must not substitute for explicit conformance to governing requirements.

---

# PASS

A Chronicle Entry receives:

```text
PASS
```

only when every blocking Validation Rule applicable to the current Entry Version is satisfied.

PASS means:

```text
The current Entry Version conforms
to the requirements governing it.
```

PASS permits the Entry to proceed toward the Publication decision.

PASS does not itself publish the Entry.

---

# FAIL

A Chronicle Entry receives:

```text
FAIL
```

when one or more blocking Validation Rules applicable to the current Entry Version are not satisfied.

FAIL means:

```text
The current Chronicle representation
is not ready to proceed.
```

FAIL does not mean:

* the historical Occurrence did not happen;
* the authoritative external record is invalid;
* the Entry must be deleted;
* Chronicle gains authority over the external subject;
* prior material history may be silently rewritten.

---

# Rule Application

Each Validation Rule is evaluated as:

```text
Applicable
Not Applicable
```

If Applicable:

```text
PASS
FAIL
```

A rule marked Not Applicable does not count as a PASS or FAIL.

The reason a conditional rule is Not Applicable should be evident from the Entry structure or governing Profile.

---

# CHR-VAL-001 — Entry Identifier

## Rule

Every production Chronicle Entry must possess a valid Chronicle Entry identifier.

The identifier must:

```text
be present
match CHR-YYYY-NNNN
belong to the Chronicle namespace
be unique
not be reused
remain stable across Entry Versions
```

The identifier must not encode:

```text
Event Type
Verification State
Lifecycle State
Publication State
originating system
jurisdiction
Entry Version
```

The `YYYY` component represents identifier assignment year.

It must not be interpreted as the Event Date.

## PASS

PASS when all applicable identifier requirements are satisfied.

## FAIL

FAIL when the identifier is:

* missing;
* malformed;
* duplicated;
* reused;
* altered across Versions of the same canonical Entry;
* assigned under the wrong namespace;
* semantically misrepresented.

---

# CHR-VAL-002 — Base Schema Conformance

## Rule

Every production Chronicle Entry must conform to the Chronicle Base Schema governing that Entry Version.

Current production schema:

```text
/chronicle/schemas/chronicle-base-schema.json
```

Validation must confirm:

```text
schema_id is present
schema_id is recognized
schema_version is present
schema_version is supported
required Base fields are present
field types are valid
field formats are valid
conditional Base constraints are satisfied
unapproved additional properties are absent
machine-readable Entry parses successfully
```

## PASS

PASS when the Entry conforms to the declared Base Schema Version.

## FAIL

FAIL when the Entry violates any blocking Base Schema requirement.

---

# CHR-VAL-003 — Event-Type Profile Conformance

## Rule

When an approved Event-Type Profile applies, the Chronicle Entry must conform to that Profile in addition to the Base Schema.

Conceptually:

```text
Chronicle Base Schema
        +
Applicable Event-Type Profile
        =
Specialized Entry Contract
```

Validation must confirm:

```text
correct Profile is selected
Profile identifier is correct
Profile Version is known
Profile-specific Required fields are present
Profile-specific field constraints are satisfied
Profile-specific Controlled Values are valid
Profile-specific authoritative-reference rules are satisfied
Profile-specific date restrictions are satisfied
Profile-specific Provenance requirements are satisfied
```

## PASS

PASS when the applicable Profile is correctly selected and all blocking Profile requirements are satisfied.

## FAIL

FAIL when:

* a required Profile is absent;
* the wrong Profile is used;
* Profile identity is invalid;
* Profile-specific requirements are not satisfied.

## Not Applicable

This rule may be Not Applicable when no approved Event-Type Profile governs the Entry.

---

# CHR-VAL-004 — Controlled Values

## Rule

Fields governed by Chronicle Controlled Values must use approved values.

Applicable value sets may include:

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

A free-form substitute must not be used when a governed value is required.

Deprecated values must not be silently converted into current values without following applicable migration, Correction, or Versioning rules.

## PASS

PASS when all governed fields contain approved values applicable to the Entry.

## FAIL

FAIL when any governed field contains:

* an unapproved value;
* a malformed value;
* an obsolete value used contrary to compatibility rules;
* free text where a Controlled Value is required.

---

# CHR-VAL-005 — Required and Conditional Fields

## Rule

Chronicle must distinguish:

```text
Required
Conditional
Optional
```

Required fields must always be present.

Conditional fields must be present whenever the condition requiring them applies.

Examples of Conditional fields include:

```text
event_type_profile
originating_system
authoritative_record_references
source_references
evidence_references
relationships
correction_references
prior_version_reference
published_at
updated_at
limitations
```

depending on the Entry and governing Profile.

## PASS

PASS when all Required fields and all applicable Conditional fields are present and valid.

## FAIL

FAIL when:

* a Required field is absent;
* a Conditional field is absent when its condition applies;
* a required field is present but empty or structurally invalid.

---

# CHR-VAL-006 — Authoritative References

## Rule

When Chronicle depends on an authoritative external or Suite-owned record, required authoritative references must be present and institutionally accurate.

Validation must confirm:

```text
required authoritative reference exists
referenced object is identifiable
owning institution or system is represented correctly where required
reference structure conforms to schema
reference does not imply transfer of authority
Profile-specific authority rules are satisfied
```

The governing principle is:

> Reference does not transfer authority.

For the Certification Event-Type Profile, at least one authoritative reference must explicitly contain:

```text
reference: <identifier>
system: certifier
```

## PASS

PASS when every required authoritative reference is structurally valid and correctly identifies the owning authority.

## FAIL

FAIL when:

* a required authoritative reference is missing;
* the referenced authority is ambiguous where explicit identification is required;
* the wrong system is presented as authoritative;
* the reference violates Profile requirements;
* Chronicle represents referenced authority as Chronicle-owned authority.

---

# CHR-VAL-007 — Date and Time Formatting

## Rule

Chronicle temporal fields must use valid formats and preserve their distinct meanings.

Applicable fields may include:

```text
event_date
entry_created_at
retrieved_at
published_at
updated_at
Correction date
Version date
```

Validation must confirm:

```text
formats are valid
required dates are present
Event Date represents the Occurrence
Entry creation time represents Chronicle creation
retrieval time represents acquisition / capture
publication time represents publication
Correction and Version dates remain distinguishable where applicable
Profile-specific date requirements are satisfied
```

The Base Schema may permit:

```text
event_date = null
```

when the Event Date cannot be determined.

An Event-Type Profile may strengthen this rule.

For example, the Certification Event-Type Profile does not permit a null Event Date.

## PASS

PASS when all applicable date and time values are valid and semantically coherent.

## FAIL

FAIL when:

* required date/time data is missing;
* format is invalid;
* one temporal concept is substituted for another;
* a Profile-specific date restriction is violated.

---

# CHR-VAL-008 — Relationship Integrity

## Rule

Chronicle Relationships must be structurally valid and semantically coherent.

Validation must confirm:

```text
Relationship Type is approved
target is identifiable
target system is represented where required
direction is correct
inverse relationship is coherent where represented
duplicate relationships are avoided
contradictions are resolved or documented
Relationship does not imply unsupported causation
Relationship does not transfer authority
```

Important distinctions include:

```text
Precedes ≠ Causes
Supersedes ≠ Deletes
References ≠ Owns
Related To ≠ Authoritative For
```

## PASS

PASS when all Relationships are valid, meaningful, and consistent with Chronicle Relationship rules.

## FAIL

FAIL when any material Relationship:

* uses an invalid type;
* lacks a required target;
* points in the wrong direction;
* contradicts another unresolved Relationship;
* falsely implies causation;
* falsely implies authority transfer.

## Not Applicable

This rule may be Not Applicable when the Entry has no Relationships and none are required.

---

# CHR-VAL-009 — Provenance

## Rule

Every production Chronicle Entry must preserve sufficient Provenance to explain how its information entered Chronicle.

Minimum Provenance requirements are:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference where required
Material Provenance Limitations where applicable
```

Where relevant, Chronicle may also preserve:

```text
transfer_history
transformation_history
preservation_path
integrity_metadata
```

Unknown Provenance must not be represented as known merely to obtain a PASS.

The governing principle is:

> Preserve origin. Preserve path. Preserve limitations.

## PASS

PASS when minimum Provenance requirements are satisfied and known limitations are represented honestly.

## FAIL

FAIL when:

* required Provenance fields are missing;
* Origin is materially ambiguous;
* acquisition or retrieval path is absent when required;
* required authoritative or Source linkage is missing;
* known Provenance limitations are concealed or contradicted.

---

# CHR-VAL-010 — Correction and Version Consistency

## Rule

When a Chronicle Entry has undergone material change, its Correction and Version lineage must conform to Chronicle rules.

Validation should confirm:

```text
canonical Entry identity remains stable
Entry Version is correct
prior Version is identifiable
formal Correction exists where required
Original information is preserved
Corrected information is preserved
Correction date is preserved
Reason is preserved
Affected fields are identified
Resulting Version is identified
Reverification occurred where required
Revalidation occurs where required
publication lineage remains traceable
```

The governing distinction is:

```text
Correction
  explains why Chronicle changed its record.

Version
  preserves the resulting state.
```

And:

> Correct forward. Preserve backward.

## PASS

PASS when all applicable Correction and Version requirements are satisfied.

## FAIL

FAIL when:

* a material change silently overwrites a prior state;
* Version lineage is broken;
* a required Correction is absent;
* Entry identity changes improperly;
* the resulting Version cannot be reconstructed;
* Reverification or Revalidation required by the change has not occurred.

## Not Applicable

This rule is Not Applicable to an initial Entry Version with no material Correction or prior Version.

---

# CHR-VAL-011 — Publication Readiness

## Rule

`CHR-VAL-011` is the final Validation-domain readiness test.

It determines whether the current Entry Version has satisfied the Validation prerequisites necessary to proceed to the separate Chronicle Publication Gate.

It does not itself approve the Entry for Publication and does not change `publication_state`.

Publication Readiness Validation must confirm:

```text
Identifier Validation = PASS
Base Schema Validation = PASS
Event-Type Profile Validation = PASS where applicable
Controlled Values Validation = PASS
Required / Conditional Field Validation = PASS
Authoritative Reference Validation = PASS where applicable
Date / Time Validation = PASS
Relationship Integrity Validation = PASS where applicable
Provenance Validation = PASS
Correction / Version Consistency = PASS where applicable
Verification State satisfies publication prerequisites
material limitations are visible where required
authority boundaries are represented correctly
no unresolved blocking failure remains
```

## PASS

PASS when the current Entry Version is eligible to proceed to the separate Chronicle Publication Gate.

The distinction is:

```text
CHR-VAL-011 — Publication Readiness
  tests readiness from a Validation standpoint.

Publication Gate
  makes the institutional approval decision.
```

A PASS under this rule does not itself mean `Approved for Publication` or `Published`.

## FAIL

FAIL when any blocking prerequisite remains unsatisfied.

A Publication Readiness PASS does not itself change:

```text
publication_state
```

Publication remains a separate institutional act.

---

# CHR-VAL-012 — Verification Dependency

## Rule

Chronicle Validation may depend on Verification results but must not duplicate or replace Verification.

Validation must confirm that:

```text
Verification has been performed when required
Verification State uses an approved value
Verification limitations are preserved when required
the Verification State satisfies publication prerequisites
```

Validation does not independently re-adjudicate every Source, Evidence item, or historical claim reviewed during Verification.

## PASS

PASS when the applicable Verification prerequisite is satisfied.

## FAIL

FAIL when required Verification:

* has not occurred;
* uses an invalid state;
* has unresolved blocking limitations;
* is insufficient for the intended publication state.

---

# CHR-VAL-013 — Authority Boundary Integrity

## Rule

Every Chronicle Entry must preserve the authority boundary between Chronicle and referenced institutions.

Validation must confirm that Chronicle does not claim ownership of determinations or authoritative records belonging to:

```text
Certifier
Registry
Anchor
Beacon
Attestor
Navigator
Atlas
or another external authority
```

Chronicle may preserve the historical Occurrence.

It may reference the authoritative object.

It may verify and validate its own historical representation.

It must not absorb the external authority.

## PASS

PASS when institutional ownership and reference relationships are represented accurately.

## FAIL

FAIL when the Entry:

* attributes another institution's authority to Chronicle;
* misidentifies the authoritative system;
* republishes an external determination as a Chronicle determination;
* otherwise collapses institutional boundaries.

---

# CHR-VAL-014 — Human and Machine Consistency

## Rule

Where Chronicle publishes both human-readable and machine-readable representations of the same Entry Version, material content must agree.

Validation should compare, where applicable:

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

## PASS

PASS when official representations are materially consistent.

## FAIL

FAIL when the official human-readable and machine-readable forms materially disagree.

## Not Applicable

This rule may be Not Applicable before both production representations exist.

---

# Blocking Rule Principle

Unless explicitly governed otherwise, a FAIL under any applicable rule in this document is a blocking Validation failure.

Conceptually:

```text
Any Applicable Blocking Rule = FAIL
        ↓
Overall Validation Result = FAIL
```

Only when all applicable blocking rules pass:

```text
All Applicable Blocking Rules = PASS
        ↓
Overall Validation Result = PASS
```

---

# No Numerical Confidence Score

Chronicle Validation must not reduce conformance to a generalized score such as:

```text
92% valid
8.7 / 10
High confidence
Validation score: 84
```

Such values obscure whether a blocking institutional requirement actually failed.

A Chronicle Entry either satisfies the applicable blocking Validation requirements or it does not.

Therefore:

```text
PASS
FAIL
```

remains the authoritative Validation outcome.

Warnings or informational notes may be preserved separately.

They do not replace PASS / FAIL.

---

# Warnings

Chronicle may preserve non-blocking warnings.

Examples include:

```text
reference availability concern
minor archival limitation
future maintenance note
non-material metadata concern
known external dependency
```

A warning is not a substitute for FAIL.

If the condition violates a blocking rule:

```text
FAIL
```

must be recorded.

---

# Validation Failure Handling

When Validation fails:

```text
Validation FAIL
        ↓
Identify Failed Rule
        ↓
Identify Affected Field / Requirement
        ↓
Return Entry to Appropriate Production Step
        ↓
Correct / Complete / Review
        ↓
Reverify if Required
        ↓
Revalidate
```

Failure routing may include:

```text
Identifier failure
  → Identifier review

Schema failure
  → Entry construction

Profile failure
  → Event-Type / Profile review

Controlled Value failure
  → classification correction

Authoritative Reference failure
  → reference review

Date / Time failure
  → temporal correction

Relationship failure
  → Relationship review

Provenance failure
  → Provenance review

Correction / Version failure
  → Correction / Versioning process

Verification prerequisite failure
  → Verification

Publication Readiness failure
  → publication preparation
```

Validation identifies the defect.

It does not necessarily perform the corrective action.

---

# Revalidation Rule

A corrected Entry must be revalidated whenever the correction could affect one or more Validation Rules.

Revalidation may be:

```text
Targeted
```

when only clearly isolated requirements changed.

Or:

```text
Full
```

when the effect of the change is broader or uncertain.

Material Entry changes should default toward full Revalidation when scope cannot be reliably bounded.

---

# Initial Production Validation Sequence

The operational order is:

```text
1. Entry Received for Validation
2. CHR-VAL-001 — Entry Identifier
3. CHR-VAL-002 — Base Schema Conformance
4. CHR-VAL-003 — Event-Type Profile Conformance
5. CHR-VAL-004 — Controlled Values
6. CHR-VAL-005 — Required and Conditional Fields
7. CHR-VAL-006 — Authoritative References
8. CHR-VAL-007 — Date and Time Formatting
9. CHR-VAL-008 — Relationship Integrity
10. CHR-VAL-009 — Provenance
11. CHR-VAL-010 — Correction and Version Consistency
12. CHR-VAL-012 — Verification Dependency
13. CHR-VAL-013 — Authority Boundary Integrity
14. CHR-VAL-014 — Human and Machine Consistency where applicable
15. CHR-VAL-011 — Publication Readiness
16. Record Overall PASS or FAIL
```

Publication Readiness is intentionally evaluated after the underlying Validation domains.

---

# Minimum Universal Validation Set

Every production Chronicle Entry must evaluate:

```text
CHR-VAL-001 — Entry Identifier
CHR-VAL-002 — Base Schema Conformance
CHR-VAL-004 — Controlled Values
CHR-VAL-005 — Required and Conditional Fields
CHR-VAL-007 — Date and Time Formatting
CHR-VAL-009 — Provenance
CHR-VAL-012 — Verification Dependency
CHR-VAL-013 — Authority Boundary Integrity
CHR-VAL-011 — Publication Readiness
```

The following are conditional:

```text
CHR-VAL-003 — Event-Type Profile Conformance
CHR-VAL-006 — Authoritative References
CHR-VAL-008 — Relationship Integrity
CHR-VAL-010 — Correction and Version Consistency
CHR-VAL-014 — Human and Machine Consistency
```

A conditional rule becomes blocking when its governing condition applies.

---

# Certification Event-Type Profile Minimum

A certification-related Chronicle Entry must additionally demonstrate:

```text
event_type_profile = certification-event-profile
originating_system = certifier
Event Type is one of the approved certification values
event_date is not null
authoritative_record_references exists
at least one structured authoritative reference identifies system: certifier
Certification-specific Provenance requirements are satisfied
```

The authoritative certification action remains owned by Certifier.

Chronicle validates only its own representation of that qualifying Occurrence.

---

# Validation Record Minimum

A completed Validation should preserve:

```text
Entry Identifier
Entry Version
Validation Date / Time
Overall Result
Rules Applied
Not Applicable Rules where material
Failed Rules
Governing Base Schema Version
Applicable Event-Type Profile Version
Validation Method
Revalidation Requirement
Supporting Validation Artifact Reference where applicable
```

The initial implementation does not require a separate canonical Validation Record object.

Chronicle may preserve the result through an institutional validation artifact until production experience demonstrates a need for a separately governed object.

---

# Guiding Rules

> Validate what the architecture claims.

> Validation tests conformance. Verification reviews representation.

> Reference does not transfer authority.

> Correct forward. Preserve backward.

> A blocking rule either passes or fails.

> Chronicle does not hide institutional failure behind a numerical confidence score.

---

# Status

**Chronicle Validation Rules established for Phase VIII.**

These rules define the normative Validation requirements applied by the Chronicle Entry Production Procedure.

The first end-to-end Phase VIII operational dry run using `SC-CERT-2026-0001` and simulated candidate `CHR-2026-0001` completed with an overall result of `PASS`.

The dry run identified no rule-set redesign requirement and clarified that `CHR-VAL-011 — Publication Readiness` is distinct from the separate Chronicle Publication Gate.
