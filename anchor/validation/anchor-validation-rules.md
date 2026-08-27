# Anchor Validation Rules

## Status

**Architecture Stage:** Post-Foundational Validation Architecture  
**Rule Set Status:** 1.0-draft  
**Applies To:** Integrity Reference production candidates and later governed Anchor Versions  
**Maintained By:** Satoshium

---

## Purpose

Anchor Validation determines whether an Integrity Reference satisfies the structural, institutional, provenance, relationship, state, Versioning, Correction, and publication-readiness requirements established by Anchor architecture.

Validation answers:

> Does this Integrity Reference satisfy Anchor's requirements?

Verification answers:

> Does the Reviewed Representation match the preserved integrity evidence?

Therefore:

```text
Validation
≠
Verification
```

---

## Validation Outcome

Each formal Validation produces one overall outcome:

```text
PASS
FAIL
```

### PASS

`PASS` means all required Validation rules applicable to the reviewed Anchor Version were satisfied.

### FAIL

`FAIL` means one or more required Validation rules applicable to the reviewed Anchor Version were not satisfied.

Validation does not use partial success to authorize publication.

```text
one blocking FAIL
→ overall FAIL
```

---

## Rule Behavior

Every applicable rule produces:

```text
PASS
```

or:

```text
FAIL
```

A rule that does not apply should be recorded as:

```text
NOT APPLICABLE
```

only if the Validation record or procedure later requires explicit non-applicability tracking.

`NOT APPLICABLE` is not a third overall Validation outcome.

---

# Validation Sequence

Formal Anchor Validation should occur after the Integrity Reference has:

```text
Anchor Identifier
Anchor Version
Source object
Representation object
Integrity object
Provenance
Relationships
Record State
```

and before Publication Gate approval.

The production sequence is therefore:

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
Canonical HTML / JSON consistency review
        ↓
Publication Gate
```

Initial Verification may be repeated after Validation if Validation remediation changes any integrity-relevant field.

---

# Identifier Assignment Rule

Formal Validation requires an Anchor Identifier because:

1. `anchor_identifier` is required by the Integrity Reference Base Schema.
2. Relationships and Version lineage depend on stable identity.
3. Validation must evaluate the actual production candidate, not a placeholder object.

Therefore:

```text
Anchor Identifier assignment
→ before formal Validation
```

Assignment does not make the record publicly authoritative.

```text
Anchor Identifier assigned
≠
published
≠
Publication Gate APPROVED
```

Once a production Anchor Identifier is assigned, it should not be recycled for another Integrity Reference even if Validation fails or publication never occurs.

This prevents identity reuse from obscuring failed or abandoned production history.

---

# Rule Families

The initial Validation architecture contains these rule families:

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

---

# VAL-001 — Anchor Identifier Present

### Requirement

The Integrity Reference must contain a non-empty Anchor Identifier assigned under current Identifier Architecture.

### PASS

A valid Anchor Identifier is present.

### FAIL

No Anchor Identifier is present, or a Source-System Identifier has been substituted as the Anchor Identifier.

---

# VAL-002 — Anchor Version Valid

### Requirement

The Integrity Reference must contain a valid sequential Anchor Version.

For a new Integrity Reference:

```text
anchor_version = 1
```

For an existing Integrity Reference:

```text
next production Version
= prior production Version + 1
```

where a new Version is required.

---

# VAL-003 — Schema Version Identified

### Requirement

The applicable Schema Version must be identified for a production candidate.

This converts `schema_version` from optional Base-Schema architecture into a production Validation requirement.

---

# VAL-004 — Source Institution Identified

### Requirement

The Source Institution authoritative for the Source Artifact must be identified.

Anchor must not represent itself as Source authority unless Anchor itself is genuinely the Source Institution for that artifact type.

---

# VAL-005 — Source-System Identifier Preserved

### Requirement

The Source-System Identifier must be present where the Source Artifact has one.

The Source-System Identifier must remain distinct from the Anchor Identifier.

---

# VAL-006 — Source Artifact Type Identified

### Requirement

The Source Artifact type must be identified sufficiently to understand what external object the Integrity Reference preserves.

---

# VAL-007 — Source Authority Coherent

### Requirement

The Source Institution, Source-System Identifier, Source Artifact type, and Source context must be internally coherent.

Validation must fail if the record appears to attribute authority to the wrong Suite institution or external Source.

---

# VAL-008 — Representation Type Present

### Requirement

The Integrity Reference must identify its Representation Type.

The exact production Controlled Value enumeration remains governed separately.

---

# VAL-009 — Representation Boundary Explicit

### Requirement

The Representation Boundary must be explicit enough to determine what content is included in the integrity subject.

A vague statement such as:

```text
the page
```

is insufficient if dynamic or excluded content materially affects reconstruction.

---

# VAL-010 — Canonicalization Method Identified

### Requirement

The canonicalization or serialization method must be identified.

If no transformation occurs, the record must still make clear how the Canonical Representation is derived.

---

# VAL-011 — Canonical Representation Reconstructable

### Requirement

The production record must preserve enough information to reconstruct or obtain the Canonical Representation used to generate integrity evidence.

If reconstruction depends on undocumented assumptions:

```text
FAIL
```

---

# VAL-012 — Integrity Subject Coherent

### Requirement

The combination of:

```text
Source Artifact identity
+
Canonical Representation
+
Representation Boundary
```

must describe one coherent integrity subject.

---

# VAL-013 — At Least One Integrity Method Present

### Requirement

The Integrity Reference must contain at least one Integrity Method.

This matches the Base Schema structural requirement.

---

# VAL-014 — Integrity Method Sufficiently Defined

### Requirement

Each Integrity Method must preserve enough information to support later Verification.

Potentially required method information includes:

```text
method_id
method_type
algorithm
parameters
Integrity Value
Verification Material
external commitment evidence
```

depending on method type.

---

# VAL-015 — Integrity Value or Proof Material Present

### Requirement

Each method must preserve the integrity evidence required by that method.

A digest method without a digest value fails.

A signature or external commitment method without required proof material fails.

---

# VAL-016 — Method / Algorithm Use Permitted

### Requirement

The Integrity Method and algorithm must not be prohibited for the intended production use under current Anchor Standards or Governance.

Historical-only methods may remain valid for Verification of older records without being valid for new production.

---

# VAL-017 — Source Provenance Present

### Requirement

Source Provenance must be sufficient to establish where the Source Artifact came from and which authority governed it.

---

# VAL-018 — Representation Provenance Present

### Requirement

Representation Provenance must explain how the Source Artifact became the Canonical Representation.

Material transformations must be documented.

---

# VAL-019 — Generation Provenance Present

### Requirement

Integrity-generation Provenance must explain how the Integrity Value or proof material was produced.

---

# VAL-020 — Provenance Supports Reproducibility

### Requirement

The combined Provenance must be sufficient for later reproduction or historical validation of the integrity process.

---

# VAL-021 — Required Source Relationship Present

### Requirement

The Integrity Reference must preserve its relationship to the Source Artifact.

The final production Relationship Type token remains governed by Relationships architecture.

---

# VAL-022 — Relationship Targets Coherent

### Requirement

Relationship identifiers and target systems must be internally coherent and must not knowingly point to the wrong object.

---

# VAL-023 — No Prohibited Self-Relationship

### Requirement

Relationships must not contain logically invalid self-reference.

Example:

```text
Integrity Reference A
→ supersedes
→ Integrity Reference A
```

fails.

Legitimate same-identity Version lineage is not prohibited merely because the Anchor Identifier remains the same.

---

# VAL-024 — Required Supersession Lineage Present

### Requirement

If Lifecycle State is:

```text
superseded
```

the record must preserve sufficient supersession lineage to identify the later Integrity Reference.

---

# VAL-025 — Record States Kept Separate

### Requirement

The Integrity Reference must preserve distinct:

```text
Integrity State
Publication State
Lifecycle State
```

No generic `status` field may substitute for all three.

---

# VAL-026 — Lifecycle State Valid

### Requirement

Lifecycle State must use the frozen initial vocabulary:

```text
draft
active
superseded
withdrawn
archived
```

---

# VAL-027 — Lifecycle Transition Valid

### Requirement

Where Validation evaluates a Version containing a lifecycle transition, the transition must conform to allowed Lifecycle architecture.

Initial allowed transitions are:

```text
draft → active
active → superseded
active → withdrawn
active → archived
superseded → archived
withdrawn → archived
```

No silent reverse transition is allowed.

---

# VAL-028 — Anchor Version Continuity Valid

### Requirement

A new Anchor Version must preserve the same integrity subject.

If the integrity subject changed:

```text
FAIL
→ new Integrity Reference required
```

---

# VAL-029 — New Integrity Reference Used for New Subject

### Requirement

A materially different integrity subject must not be hidden as a new Version of an existing Integrity Reference.

---

# VAL-030 — Prior Production Versions Preserved

### Requirement

A new production Version must not erase prior production Versions.

---

# VAL-031 — Correction Lineage Complete

### Requirement

If the Version contains a Correction, Validation must be able to identify:

```text
affected prior Version
error or condition
prior state
corrected state
Correction reason
resulting Version
```

as applicable.

---

# VAL-032 — Source Change Not Misclassified as Anchor Correction

### Requirement

A legitimate Source Artifact change must not be represented as an Anchor-owned Correction unless Anchor itself recorded something incorrectly.

---

# VAL-033 — Subject-Invalidating Error Uses New Identity

### Requirement

If a Correction reveals that the original Integrity Reference preserved the wrong integrity subject:

```text
new Integrity Reference
→ required
```

Ordinary Versioning is insufficient.

---

# VAL-034 — Verification Inputs Available

### Requirement

Before Initial Verification, the Integrity Reference must contain enough information to execute the Integrity Verification Procedure.

---

# VAL-035 — Initial Verification Completed

### Requirement

For Publication readiness, Initial Verification must have been completed against the production Version being proposed for publication.

A Validation pass may be recorded before this step if the Validation process is deliberately staged, but Publication readiness cannot pass without Initial Verification.

For the first production architecture, the preferred model is:

```text
Structural / Institutional Validation
→ Initial Verification
→ Publication-readiness Validation confirmation
```

---

# VAL-036 — Blocking Verification Issue Absent

### Requirement

A Version proposed for publication must not contain an unresolved Verification condition that makes the integrity claim materially unsupported.

The exact acceptable Verification Result vocabulary remains governed by Verification architecture.

---

# VAL-037 — Canonical HTML Candidate Present

### Requirement

Before Publication Gate approval, a canonical human-readable representation must exist.

---

# VAL-038 — Canonical JSON Candidate Present

### Requirement

Before Publication Gate approval, a canonical machine-readable representation must exist and conform to the applicable Schema Version.

---

# VAL-039 — Human / Machine Consistency

### Requirement

Canonical HTML and canonical JSON must agree on material institutional facts.

At minimum:

```text
Anchor Identifier
Anchor Version
Source identity
Representation Boundary
Integrity Method
Integrity Value / proof context
Lifecycle State
material Correction notice
```

---

# VAL-040 — Publication Timestamp Not Premature

### Requirement

A record that has not yet crossed the Publication Gate must not claim a production `published_at` timestamp.

`published_at` is assigned only when the Version enters public Anchor authority.

---

# VAL-041 — No Blocking Correction

### Requirement

A Version proposed for publication must not have an unresolved blocking Anchor Correction.

---

# VAL-042 — Publication Gate Inputs Complete

### Requirement

Before the Publication Gate is applied, the record must have:

```text
Validation PASS
Initial Verification completed
canonical HTML
canonical JSON
human / machine consistency
appropriate Lifecycle State
no blocking Correction
no governance hold
```

---

# Overall Outcome

The overall result is:

```text
PASS
```

only when every applicable required rule passes.

Otherwise:

```text
FAIL
```

---

# Validation Record

A formal Validation execution should eventually preserve:

```text
Anchor Identifier
Anchor Version
Schema Version
validated_at
rule-set Version
rule results
overall outcome
notes / exceptions where required
```

Whether Validation receives its own permanent identifier remains unfrozen.

---

# Validation and Publication Gate

Validation does not publish the record.

```text
Validation PASS
≠
Publication Gate APPROVED
```

Validation provides evidence used by the Publication Gate.

---

# Validation and Verification

Validation and Verification remain independent:

```text
Validation
→ institutional / structural conformity

Verification
→ integrity-evidence comparison
```

A record can theoretically:

```text
pass Validation
and fail Verification
```

or:

```text
Verify successfully
and fail Validation
```

Neither condition is sufficient for publication.

---

# First Production Use

The first production Integrity Reference should treat this rule set as a test.

After production, review:

```text
Which rules were necessary?
Which were redundant?
Which were ambiguous?
Which requirements were missing?
Which rules should become machine-enforced?
Which rules should remain procedural?
```

The rule set should be refined from evidence rather than assumed complete.

---

# Validation Principle

> Validate the institution before publishing the record.

Validation ensures that an Integrity Reference is not merely syntactically valid, but institutionally coherent enough to proceed toward public Anchor authority.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
