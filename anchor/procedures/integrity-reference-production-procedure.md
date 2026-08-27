# Integrity Reference Production Procedure

## Purpose

This procedure governs the production of a new Satoshium Anchor **Integrity Reference**.

It converts the conceptual Anchoring Process into an executable institutional workflow.

The governing principle is:

> Define the representation. Generate the integrity evidence. Preserve the reference. Make later Verification possible.

---

## Preconditions

Before production begins, the operator or governed process must be able to identify:

```text
Source Institution
Authoritative Artifact
Source-System Identifier
Source Artifact Version, where applicable
intended Canonical Representation
Representation Boundary
applicable Integrity Method
```

Production must not begin by merely hashing whatever artifact happens to be available.

---

## Procedure

### 1. Identify the Source Institution

Confirm which institution is authoritative for the Source Artifact.

Record:

```text
source_institution
```

Anchor does not assume Source authority.

---

### 2. Identify the Authoritative Artifact

Identify the specific Source Artifact that will become the integrity subject.

Record:

```text
source_artifact_type
source_system_identifier
source_version, where applicable
source_location, where applicable
```

Confirm:

```text
Source-System Identifier ≠ Anchor Identifier
```

---

### 3. Confirm Source Authority

Confirm that the selected artifact is an authoritative Source representation or an accepted authoritative Source copy.

If Source authority is unclear:

```text
STOP
→ resolve Source authority before production continues
```

---

### 4. Define the Canonical Representation

Determine the exact representation Anchor will preserve.

Record:

```text
representation_type
canonicalization.method
canonicalization.version, where applicable
media_type, where applicable
encoding, where applicable
```

---

### 5. Define the Representation Boundary

Explicitly define what is included and excluded.

Examples of potentially excluded presentation material include:

```text
navigation
ads
dynamic interface elements
comments
display-only timestamps
analytics
```

The Representation Boundary must be sufficient for later reconstruction.

---

### 6. Construct the Canonical Representation

Apply the governed canonicalization or serialization process.

If transformation occurs, preserve transformation provenance.

Do not silently normalize or alter Source content.

---

### 7. Determine the Integrity Subject

Confirm that the integrity subject is:

```text
Source Artifact identity
+
Canonical Representation
+
Representation Boundary
```

This decision is foundational to later Versioning.

---

### 8. Select Integrity Method

Select one or more applicable Integrity Methods.

Record for each method:

```text
method_id
method_type
algorithm, where applicable
algorithm_version, where applicable
parameters, where applicable
```

The selected method must be permitted by current Anchor Standards and Governance.

---

### 9. Generate Integrity Material

Generate or obtain the required integrity evidence.

Potential outputs include:

```text
Integrity Value
digital signature
trusted timestamp
Merkle commitment
transparency commitment
external commitment
Verification Material
```

Preserve generation provenance.

---

### 10. Record Temporal and Attribution Context

Where applicable, record:

```text
generated_at
signer_reference
key_reference
producing_system
timestamp reference
external commitment reference
```

Use minimum necessary attribution.

---

### 11. Construct Provenance

Preserve the required provenance layers:

```text
Source Provenance
Representation Provenance
Integrity-Generation Provenance
Anchor Record Provenance, where applicable
```

The provenance must be sufficient for later Verification.

---

### 12. Construct Relationships

Create required machine-readable relationships.

At minimum, the Integrity Reference must preserve its Source relationship.

Where applicable, also preserve relationships to:

```text
prior Anchor Version
Correction
superseding Integrity Reference
external commitment
Verification record
Publication representation
```

---

### 13. Assign Anchor Identifier

Assign the Anchor Identifier under the active Identifier Architecture.

Do not reuse a Source-System Identifier as the Anchor Identifier.

If final production identifier syntax has not yet been adopted:

```text
STOP
→ production identifier policy must be resolved before first public production
```

---

### 14. Assign Anchor Version

For a new Integrity Reference:

```text
anchor_version = 1
```

For an update to the same integrity subject, use the Versioning Procedure instead of creating a new Integrity Reference.

---

### 15. Populate Record State

Set:

```text
integrity_state
publication_state
lifecycle_state
```

using current Controlled Values.

These state dimensions must remain separate.

---

### 16. Serialize the Integrity Reference

Generate the machine-readable Integrity Reference using the applicable Schema Version.

The Base Schema currently requires:

```text
anchor_identifier
anchor_version
source
representation
integrity
provenance
relationships
record_state
```

---

### 17. Perform Structural Review

Confirm:

```text
required fields present
identifiers coherent
relationships well-formed
provenance sufficient
representation boundary explicit
integrity methods complete
state dimensions separate
```

Formal Validation rules may supplement this step.

---

### 18. Perform Initial Verification

Run the **Integrity Verification Procedure** against the newly created Integrity Reference and its Canonical Representation.

If Initial Verification does not produce an acceptable publication outcome:

```text
STOP
→ investigate before Publication Gate
```

---

### 19. Prepare Canonical Publication Representations

Generate:

```text
Canonical HTML
Canonical JSON
```

Confirm that both represent the same Anchor Identifier, Version, Source identity, integrity subject, integrity material, lifecycle information, and Correction state.

---

### 20. Apply Publication Procedure

Submit the completed Integrity Reference to the **Publication Procedure**.

A production Integrity Reference does not become publicly authoritative merely because its files exist.

---

## Production Outcome

Successful completion produces:

```text
Integrity Reference
+
Anchor Identifier
+
Anchor Version 1
+
Canonical HTML
+
Canonical JSON
+
Initial Verification evidence
+
Publication decision
```

---

## Failure Handling

If a defect is found before publication:

```text
correct draft
→ repeat affected production steps
```

If a defect is found after publication:

```text
do not edit in place
→ use Correction Procedure / Versioning
```

---

## Principle

> Define the representation. Generate the integrity evidence. Preserve the reference. Make later Verification possible.

**Version:** 1.0-draft  
**Maintained By:** Satoshium
