# Correction Procedure

## Purpose

This procedure governs repair of Anchor-owned production errors.

The governing principle is:

> Correct forward. Preserve backward.

---

## Trigger

A potential Correction may be triggered by:

```text
Verification
Maintenance
human review
publication review
relationship review
governance review
external notice
```

---

## Procedure

### 1. Preserve Current State

Before changing anything, preserve the current production Version.

Never edit the historical production state in place.

---

### 2. Determine Source Change vs. Anchor Error

Ask:

```text
Did the Source Artifact legitimately change?
or
Was Anchor's own record incorrect?
```

If only the Source changed:

```text
not an Anchor Correction
```

Route to Maintenance / Versioning as appropriate.

---

### 3. Confirm Anchor Ownership of Error

Examples may include:

```text
Source reference metadata
Representation Boundary metadata
Integrity Value
algorithm metadata
provenance
relationship
signer / key reference
publication metadata
lifecycle metadata
```

---

### 4. Apply Integrity Subject Test

Determine whether the original integrity subject remains valid.

```text
Source Artifact identity
+
Canonical Representation
+
Representation Boundary
```

If the subject remains the same:

```text
Correction + new Anchor Version
```

If the subject was wrong:

```text
new Integrity Reference
```

---

### 5. Classify Correction

Use a governed Correction Type if the production enumeration is available.

Do not invent ad hoc tokens.

---

### 6. Record Prior State

Preserve:

```text
affected Anchor Identifier
affected Anchor Version
affected field / condition
prior value
```

---

### 7. Record Corrected State

Preserve:

```text
corrected value
Correction reason
effective time
```

---

### 8. Create New Anchor Version

For same-subject Corrections:

```text
Version N
→ preserved

Correction
→ recorded

Version N+1
→ corrected state
```

---

### 9. Create New Integrity Reference if Required

If the original record anchored the wrong integrity subject:

```text
new Anchor Identifier
anchor_version = 1
```

Apply Lifecycle review to the flawed record.

---

### 10. Preserve Correction Lineage

Preserve relationships equivalent to:

```text
corrects
corrected_by
applied_in
```

where governed.

---

### 11. Reverify

Integrity-affecting Corrections should normally be Reverified.

---

### 12. Apply Lifecycle Consequence

Where appropriate, determine whether the flawed record remains:

```text
active
superseded
withdrawn
archived
```

under Lifecycle rules.

---

### 13. Republish

If the canonical public Anchor record changes:

```text
run Publication Procedure
```

Ensure the current record exposes the material Correction and prior Version history.

---

## Principle

> Correct forward. Preserve backward.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
