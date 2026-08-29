# Integrity Reference Validation Procedure

## Purpose

This procedure governs formal institutional **Validation** of a Satoshium Anchor Integrity Reference.

Validation determines whether the current production candidate satisfies the requirements established by Anchor architecture, schemas, Controlled Values, Validation Rules, Versioning, Corrections, Verification readiness, Publication readiness, and human / machine consistency.

The governing principle is:

> Validate the institution before publishing the record.

---

## Validation Outcome

The overall Validation outcome is:

```text
PASS
```

or:

```text
FAIL
```

Individual rules may also be recorded as:

```text
NOT APPLICABLE
```

where the rule does not apply to the candidate.

`NOT APPLICABLE` is not a third overall Validation outcome.

Any blocking rule failure produces:

```text
FAIL
```

---

## Governing Rule Set

The initial Validation Rule Set is:

```text
VAL-001 through VAL-042
```

covering:

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

The applicable Validation Rule Set Version must be preserved with the execution result.

---

## Production Position

Validation is executed in two governed stages.

### Stage A — Structural / Institutional Validation

Occurs after:

```text
Integrity Reference constructed
Anchor Identifier assigned
Anchor Version assigned
```

and before Initial Verification.

Its purpose is to confirm that the candidate is sufficiently complete, coherent, and institutionally valid to proceed into Verification.

### Stage B — Publication-Readiness Validation

Occurs after:

```text
Initial Verification
Canonical HTML
Canonical JSON
```

and before the Publication Gate.

Its purpose is to confirm that the candidate remains Validation-compliant and now also satisfies Verification dependency, Publication readiness, and human / machine consistency requirements.

The full sequence is:

```text
Integrity Reference constructed
        ↓
Anchor Identifier assigned
        ↓
Anchor Version assigned
        ↓
Stage A — Structural / Institutional Validation
        ↓
Initial Verification
        ↓
Canonical HTML + Canonical JSON
        ↓
Stage B — Publication-Readiness Validation
        ↓
Human / Machine Consistency confirmed
        ↓
Publication Gate
        ↓
Publication
```

---

## Inputs

Validation requires the current production candidate and applicable institutional context, including:

```text
Anchor Identifier
Anchor Version
Schema Version
Source
Representation
Integrity Method(s)
Provenance
Relationships
Record State
Correction / Version lineage where applicable
Verification history where applicable
Canonical HTML and Canonical JSON for Stage B
```

---

## Procedure

### 1. Identify Candidate

Confirm the exact:

```text
Anchor Identifier
Anchor Version
Schema Version
```

Validation must evaluate the intended production Version.

---

### 2. Confirm Rule Set

Identify the applicable:

```text
Validation Rule Set
Validation Rule Set Version
```

Do not silently validate under an unspecified rule set.

---

### 3. Execute Stage A Rules

Evaluate the rules applicable before Initial Verification.

At minimum, confirm:

```text
production identity
Source authority and Source-System Identifier
Representation Type
Representation Boundary
canonicalization method
Integrity Method completeness
Integrity Value / proof readiness
Provenance
required Source relationship
record-state separation
Lifecycle State validity
Version continuity
Correction lineage where applicable
Verification inputs available
```

---

### 4. Record Rule-Level Results

For each applicable rule, record:

```text
Rule ID
PASS / FAIL / NOT APPLICABLE
material note where necessary
```

---

### 5. Determine Stage A Outcome

If any blocking Stage A rule fails:

```text
FAIL
→ STOP
→ return candidate for governed remediation
```

If Stage A passes:

```text
proceed to Initial Verification
```

---

### 6. Perform Initial Verification

Execute the Integrity Verification Procedure.

Validation does not replace Verification.

---

### 7. Prepare Canonical Publication Representations

Generate:

```text
Canonical HTML
Canonical JSON
```

under the applicable Schema Version.

---

### 8. Execute Stage B Publication-Readiness Rules

Confirm:

```text
Initial Verification completed
no blocking Verification issue
Canonical HTML exists
Canonical JSON exists
machine-readable schema conformance
human / machine consistency
published_at not assigned prematurely
no blocking Correction
Publication Gate inputs complete
appropriate Lifecycle State
no governance hold
```

This stage includes the publication-readiness requirements represented by the applicable VAL rules.

---

### 9. Determine Final Validation Outcome

If all blocking applicable rules pass:

```text
PASS
```

Otherwise:

```text
FAIL
```

Only a final:

```text
PASS
```

may proceed to the Publication Gate.

---

### 10. Preserve Validation Evidence

Preserve at least:

```text
Anchor Identifier
Anchor Version
Schema Version
validated_at
Validation Rule Set Version
rule-level results
overall Validation outcome
material notes / limitations
```

Whether Validation evidence eventually receives its own permanent identifier remains separately governed and is not required by this procedure.

---

## Failure Handling

Validation failure does not:

```text
delete the Integrity Reference
erase the Anchor Identifier
recycle the Anchor Identifier
reverse Source authority
create publication authority
```

Remediate the candidate under the applicable architecture and repeat the affected Validation stage.

If the defect reveals that the wrong integrity subject was selected:

```text
new Integrity Reference
→ new Anchor Identifier
```

under Versioning and Corrections architecture.

---

## Relationship to Verification

```text
Validation
→ Does the Integrity Reference satisfy Anchor's requirements?

Verification
→ Does the Reviewed Representation match the preserved integrity evidence?
```

Neither substitutes for the other.

---

## Relationship to Publication

```text
Validation PASS
≠
Publication Gate APPROVED
```

Validation establishes institutional readiness.

The Publication Gate makes the separate institutional decision to permit publication.

---

## Principle

> Validate the institution before publishing the record.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
