# Integrity Verification Procedure

## Purpose

This procedure governs execution of Satoshium Anchor **Integrity Verification**.

The governing principle is:

> Reproduce faithfully. Compare precisely. Report only what the evidence proves.

---

## Inputs

Required inputs are:

```text
Integrity Reference
Reviewed Representation
```

The verifier must identify the applicable:

```text
Anchor Identifier
Anchor Version
Representation Boundary
Canonicalization method
Integrity Method
Integrity Value / proof material
Provenance
Verification Material
```

---

## Procedure

### 1. Identify the Integrity Reference

Confirm the exact:

```text
Anchor Identifier
Anchor Version
```

Do not silently substitute a newer Version.

---

### 2. Load Verification Context

Load the relevant:

```text
source
representation
integrity
provenance
relationships
```

from the governed Integrity Reference.

---

### 3. Confirm Reviewed Representation

Identify the representation being tested.

Confirm that it is suitable for evaluation under the original Representation Boundary.

---

### 4. Reconstruct Canonical Representation

Apply the governed canonicalization and transformation rules.

If the Canonical Representation cannot be reconstructed:

```text
do not guess
→ record non-comparison condition
```

---

### 5. Identify Applicable Integrity Method(s)

For each method, load:

```text
method_id
method_type
algorithm
parameters
integrity_value
verification_material
external_commitment
```

as applicable.

---

### 6. Reproduce or Validate Integrity Material

For deterministic methods:

```text
reproduce
```

For historical or external methods:

```text
validate
```

Examples:

```text
digest → reproduce
signature → validate
timestamp → validate historical proof
external commitment → validate proof / inclusion
```

---

### 7. Preserve Method-Level Outcomes

Where multiple methods exist, do not collapse them prematurely.

Record each method-level outcome separately where possible.

---

### 8. Compare Expected and Observed Material

Determine whether:

```text
comparison reached + agrees
comparison reached + disagrees
valid comparison not reached
```

---

### 9. Determine Verification Result

Use the currently governed Verification Result vocabulary.

Candidate architecture includes:

```text
match
mismatch
unable_to_verify
incomplete_material
method_unavailable
```

Only production-approved values may be used once frozen.

---

### 10. Record Verification Event

Record at least:

```text
verified_at
verification_result
method_id, where applicable
notes, where materially necessary
```

If a separately identified Verification Record is later adopted, use that model.

---

### 11. Investigate Non-Match Results

For `mismatch` or non-comparison outcomes, determine whether the cause is:

```text
Source change
wrong Reviewed Representation
corruption
canonicalization failure
external service failure
missing Verification Material
Anchor-owned error
```

Do not infer cause from result alone.

---

### 12. Route Governed Action

Possible routing includes:

```text
no action
Maintenance
Correction
new Anchor Version
Lifecycle review
new Integrity Reference
```

---

## Initial Verification

During production, Initial Verification occurs after Stage A Structural / Institutional Validation has passed and before Stage B Publication-Readiness Validation and Publication Gate approval.

```text
Stage A Validation
        ↓
Initial Verification
        ↓
Stage B Publication-Readiness Validation
        ↓
Publication Gate
```

---

## Reverification

Post-publication Verification is Reverification.

Reverification appends history.

It does not overwrite prior Verification events.

---

## Principle

> Reproduce faithfully. Compare precisely. Report only what the evidence proves.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
