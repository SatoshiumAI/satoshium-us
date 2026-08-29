# Maintenance Procedure

## Purpose

This procedure governs post-publication Maintenance of Satoshium Anchor Integrity References.

The governing principle is:

> Observe continuously. Preserve history. Escalate governed change.

---

## Triggers

Maintenance may be:

```text
scheduled
```

or:

```text
event-triggered
```

Potential triggers include:

```text
Source change
Source relocation
broken relationship
publication outage
algorithm deprecation
key rotation
key compromise
external commitment concern
failed Reverification
Correction
governance request
```

---

## Procedure

### 1. Identify Maintenance Trigger

Record why the review is occurring.

---

### 2. Load Current Record and History

Load:

```text
current Anchor Version
prior Versions
Verification history
Corrections
Relationships
Lifecycle State
Publication State
```

---

### 3. Check Publication Health

Confirm:

```text
canonical HTML resolves
canonical JSON resolves
current-Version pointer is correct
historical Versions remain accessible
required notices remain visible
```

---

### 4. Check Relationship Health

Review critical Source, Version, Correction, supersession, and external commitment relationships.

---

### 5. Check Source Health

Determine whether the Source Artifact:

```text
remains reachable
moved
changed
was withdrawn
was superseded
became unavailable
```

---

### 6. Apply Integrity Subject Test to Source Changes

If the Source changed, determine whether the integrity subject remains the same.

Route to:

```text
no action
Reverification
new Anchor Version
new Integrity Reference
```

as appropriate.

---

### 7. Review Method and Algorithm Health

Check:

```text
method still supported
algorithm still acceptable
historical Verification still possible
replacement evidence desirable
```

---

### 8. Review Key Health

Check:

```text
key rotation
key expiration
key compromise
historical key availability
```

Preserve historical key references.

---

### 9. Review External Commitment Health

Check availability and historical verifiability of:

```text
timestamp proofs
transparency-log entries
Merkle commitments
future Bitcoin commitments
other external evidence
```

---

### 10. Perform Reverification Where Required

Use the Integrity Verification Procedure.

Preserve the result.

If Maintenance leads to a changed canonical Anchor Version, route that Version through the current Validation procedure before renewed Publication.

---

### 11. Record Maintenance Observations

Record:

```text
reviewed_at
trigger
scope
observations
Reverification result
action required
```

where the Maintenance model supports it.

---

### 12. Determine Governed Action

Possible outcomes:

```text
no action
next review only
Reverification
Correction
new Anchor Version
Validation review
Lifecycle review
Publication repair
new Integrity Reference
```

---

### 13. Route Anchor Errors to Correction

Do not silently patch canonical records.

---

### 14. Route Canonical Changes to Versioning

Do not create a new Version merely because Maintenance occurred.

Create a Version only when the canonical Anchor record changes.

---

### 15. Route Lifecycle Questions to Lifecycle Governance

Maintenance may trigger lifecycle review.

It does not silently change Lifecycle State.

---

### 16. Preserve Maintenance History

Do not overwrite prior Maintenance observations or Reverification results.

---

### 17. Set Next Review

Where applicable, set:

```text
next_review_due
```

under the current Maintenance cadence policy.

---

## Long-Term Preservation Requirement

Maintenance should preserve:

```text
Anchor Identifier
all production Versions
Source references
Canonical Representation context
Integrity Material
Verification Material
Provenance
Relationships
Corrections
Lifecycle history
Publication history
```

---

## Principle

> Observe continuously. Preserve history. Escalate governed change.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
