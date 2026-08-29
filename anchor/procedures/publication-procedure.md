# Publication Procedure

## Purpose

This procedure governs the transition from completed Integrity Reference to publicly authoritative Anchor record.

The governing principle is:

> Publish only what Anchor can preserve, explain, verify, and version.

---

## Procedure

### 1. Confirm Production Identity

Confirm:

```text
Anchor Identifier
Anchor Version
```

---

### 2. Confirm Final Validation PASS

Confirm that the Integrity Reference has completed the formal **Integrity Reference Validation Procedure** for the Version being proposed for publication.

Required:

```text
Stage A Structural / Institutional Validation completed
Initial Verification completed
Stage B Publication-Readiness Validation completed
Final Validation outcome = PASS
```

Validation PASS is required before the Publication Gate.

---

### 3. Confirm Initial Verification

Confirm that Initial Verification has been completed for the exact Anchor Version being proposed for publication and that no blocking Verification issue remains.

---

### 4. Confirm Canonical Representations and No Blocking Condition

Check for:

```text
unresolved Correction
governance hold
invalid relationship
missing provenance
unclear Representation Boundary
unresolved Verification issue
```

---

### 5. Confirm Canonical HTML

Confirm that the human-readable canonical representation has been generated.

---

### 6. Confirm Canonical JSON

Confirm that the machine-readable canonical representation has been generated under the applicable Schema Version.

---

### 7. Confirm Human / Machine Consistency

Confirm that HTML and JSON agree on all material institutional facts and that this consistency was included in Publication-Readiness Validation.

At minimum:

```text
Anchor Identifier
Anchor Version
Source identity
Representation Boundary
Integrity Method
Integrity Value / proof context
Lifecycle State
Correction notice
```

---

### 8. Apply Publication Gate

The Gate decision is:

```text
APPROVED
```

or:

```text
NOT APPROVED
```

---

### 9. If NOT APPROVED

Do not create a public production publication event.

Return the record for governed remediation.

---

### 10. If APPROVED

Assign:

```text
published_at
```

representing when the Version enters public Anchor authority.

---

### 11. Publish Canonical Representations

Publish:

```text
Canonical HTML
Canonical JSON
```

---

### 12. Update Current-Version Resolution

The stable Anchor Identifier should resolve to the current canonical Version.

---

### 13. Preserve Historical Versions

Prior production Versions must remain preserved and distinguishable.

---

### 14. Publish Correction / Lifecycle Notices

Where applicable, expose:

```text
Correction notice
supersession notice
withdrawal notice
archival notice
```

without erasing prior history.

---

### 15. Update Integrity Reference Index

Ensure the published Integrity Reference appears in the governed public index when appropriate.

---

## Public Authority Boundary

Publication makes Anchor authoritative for the Anchor record.

It does not make Anchor authoritative for the Source Artifact's substantive meaning.

> Reference does not transfer authority.

---

## Principle

> Publish only what Anchor can preserve, explain, verify, and version.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
