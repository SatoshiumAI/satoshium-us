# Integrity Verification

## Overview

**Integrity Verification** defines how Satoshium Anchor determines whether a Reviewed Representation remains consistent with the Canonical Representation governed by an Integrity Reference.

The canonical Verification model is:

```text
Integrity Reference
        +
Reviewed Representation
        ↓
Reproduce / Validate Integrity Material
        ↓
Compare
        ↓
Verification Result
```

The governing principle is:

> Reproduce faithfully. Compare precisely. Report only what the evidence proves.

---

## Purpose

Verification operationalizes the Integrity Reference.

Without Verification, an Integrity Reference would preserve integrity material without a governed way to use it later.

Verification defines:

- required inputs;
- representation reconstruction;
- method selection;
- Integrity Value reproduction;
- proof validation;
- comparison behavior;
- failure modes;
- result recording;
- later Reverification.

---

# What Verification Proves

A successful Integrity Verification supports the conclusion that:

> The Reviewed Representation remains consistent with the representation governed by the Integrity Reference under the verified Integrity Method.

Conceptually:

```text
Successful Verification
→ representation consistency
```

---

# What Verification Does Not Prove

Integrity Verification does not establish:

```text
Truth
Certification
Trust
Reputation
Historical Interpretation
Source Authority
```

Therefore:

```text
Integrity Verification
≠
Truth

Integrity Verification
≠
Certification

Integrity Verification
≠
Trust
```

A perfectly preserved artifact may still contain incorrect, disputed, obsolete, incomplete, or low-quality information.

---

# Verification Inputs

A Verification process should be able to identify:

```text
Anchor Identifier
Anchor Version
Source Artifact
Source-System Identifier
Representation Type
Representation Boundary
Canonicalization method
Integrity Method
Integrity Value or proof material
Provenance
Verification Material
```

Missing required inputs may prevent Verification.

---

# Integrity Reference Input

The Integrity Reference provides the governed verification context.

Relevant schema sections include:

```text
source
representation
integrity
provenance
relationships
record_state
```

The Verification process must use the Version of the Integrity Reference actually being reviewed.

---

# Reviewed Representation

A **Reviewed Representation** is the representation currently being tested.

It may come from:

- the current Source location;
- an archive;
- a local preserved copy;
- a replicated Suite artifact;
- another authorized source.

The location is less important than whether the representation can be reconstructed under the governed Representation Boundary and canonicalization rules.

---

# Representation Boundary

Verification must honor the original Representation Boundary.

Example:

```text
Canonical record content
→ included

navigation
footer
ads
dynamic interface
later comments
display timestamps
→ excluded
```

If excluded presentation content changes, that does not necessarily produce an integrity mismatch.

---

# Canonical Reconstruction

Verification may require converting the Reviewed Representation back into the Canonical Representation.

Conceptually:

```text
Reviewed Representation
        ↓
apply governed canonicalization
        ↓
Reconstructed Canonical Representation
```

The canonicalization process must use the rules and Version recorded in provenance.

Anchor must not silently improvise missing rules.

---

# Reproduction

For methods that produce deterministic integrity material, Verification reproduces the expected process.

Example:

```text
Reconstructed Canonical Representation
        ↓
recorded hash algorithm
        ↓
Reproduced Digest
```

The reproduced value is then compared with the Integrity Value preserved by the Integrity Reference.

---

# Validation of Non-Reproducible Evidence

Some integrity evidence cannot simply be regenerated later.

Examples may include:

- historical trusted timestamps;
- signatures;
- transparency-log entries;
- Bitcoin commitments;
- third-party proofs.

These are validated rather than recreated.

Conceptually:

```text
stored proof material
+
historical external evidence
        ↓
validate
        ↓
method-level result
```

---

# Single-Method Verification

A single-method Integrity Reference may follow:

```text
Canonical Representation
        ↓
Integrity Method
        ↓
Reproduced / validated material
        ↓
Compare
        ↓
Verification Result
```

---

# Composite Verification

A composite Integrity Reference may use multiple methods.

Example:

```text
digest
+
signature
+
trusted timestamp
+
external commitment
```

Verification should preserve method-level outcomes.

One method may:

```text
match
```

while another may be:

```text
unable_to_verify
```

The overall result model must not hide these distinctions.

---

# Method-Level Verification

Each integrity method instance should be independently reviewable.

The Base Schema already supports:

```text
method_id
method_type
algorithm
parameters
integrity_value
verification_material
external_commitment
```

Verification should identify which `method_id` was evaluated.

---

# External Commitment Verification

External commitment Verification may involve:

```text
Integrity Value
        ↓
proof material
        ↓
external system
        ↓
external commitment result
```

Potential external systems include:

- timestamp services;
- transparency logs;
- public ledgers;
- future Bitcoin commitment infrastructure.

External-system unavailability must remain distinguishable from a mismatch.

---

# Bitcoin Verification

If Bitcoin commitments are later adopted, Verification may eventually need to confirm:

- transaction existence;
- commitment location;
- commitment payload or Merkle root;
- inclusion proof;
- confirmation context;
- correspondence between the committed value and the Integrity Reference.

No Bitcoin-specific Verification procedure is frozen yet.

---

# Comparison

Comparison asks whether observed integrity material agrees with expected integrity material.

Conceptually:

```text
Expected Integrity Material
        vs.
Observed / Reproduced Integrity Material
```

Comparison behavior may vary by method.

For a digest:

```text
exact equality
```

For a signature:

```text
signature validation
```

For a timestamp:

```text
historical proof validation
```

For an external commitment:

```text
external proof / inclusion validation
```

---

# Verification Result

**Verification Result** records the governed outcome of a Verification event.

The architecture now demonstrates that a simple boolean may be insufficient.

The first production-frozen value is:

```text
match
```

Definition:

```text
comparison reached
+
observed integrity material agrees with expected integrity material
```

The remaining candidate values stay unfrozen until a real production condition requires them:

```text
mismatch
unable_to_verify
incomplete_material
method_unavailable
```

---

# Match

`match` is now a production-frozen Verification Result.

It means that a valid comparison was reached and the Reviewed Representation, reconstructed under the governed Representation Boundary and canonicalization rules, reproduced the integrity material expected by the Integrity Reference.

A match supports:

```text
representation consistency
```

It does not support:

```text
truth
trustworthiness
certification
```

unless another institution separately establishes those conclusions.

---

# Mismatch

Conceptually:

```text
mismatch
```

means Verification completed but observed integrity material did not agree with expected integrity material.

Possible causes include:

- legitimate Source change;
- wrong Source representation;
- corruption;
- wrong Representation Boundary;
- incorrect canonicalization;
- wrong Integrity Value;
- incorrect algorithm;
- Anchor metadata error.

Mismatch identifies a condition requiring investigation.

It does not identify the cause automatically.

---

# Unable to Verify

Conceptually:

```text
unable_to_verify
```

means a valid comparison could not be reached.

Possible causes include:

- Source Artifact unavailable;
- external system unavailable;
- unsupported historical method;
- missing proof material;
- missing public key;
- incomplete provenance;
- unrecoverable canonicalization rules.

This must remain distinct from `mismatch`.

---

# Incomplete Material

A distinct result may be useful when required Verification Material is missing.

Conceptual example:

```text
incomplete_material
```

This may later be merged into `unable_to_verify` if production proves the distinction unnecessary.

---

# Method Unavailable

A distinct result may be useful when the required method can no longer be executed.

Conceptual example:

```text
method_unavailable
```

Examples may include:

- unavailable legacy verification software;
- unsupported signature scheme;
- inaccessible external network;
- deprecated mechanism without retained verifier.

This remains provisional.

---

# Verification Result vs. Integrity State

A Verification Result records one event.

Integrity State describes the broader current condition of the Integrity Reference.

Therefore:

```text
Verification Result
≠
Integrity State
```

Example:

```text
Verification Event 1
→ match

Verification Event 2
→ unable_to_verify

Integrity State
→ determined later by Maintenance / Lifecycle policy
```

The state transition policy remains unfrozen.

---

# Verification Event

The Base Schema currently supports a lightweight Verification event:

```text
verification_identifier
verified_at
verification_result
method_id
notes
```

Only:

```text
verified_at
verification_result
```

are structurally required when an event is recorded.

This architecture now establishes the meaning of those fields.

---

# Separately Identified Verification Records

Anchor may later determine that important Verification events should become separately identified records.

Potential architecture:

```text
Integrity Reference
        ↓
verified_by
        ↓
Verification Record
```

No Verification Identifier format or Verification Record schema is frozen.

Production testing should determine whether separate records create enough value to justify the added object type.

---

# Initial Verification

**Initial Verification** occurs during Integrity Reference production.

Its purpose is to demonstrate that the integrity material recorded by Anchor correctly corresponds to the intended Canonical Representation before publication.

The production order is now explicitly staged:

```text
Integrity Reference constructed
        ↓
Stage A — Structural / Institutional Validation
        ↓
Initial Verification
        ↓
Canonical HTML + Canonical JSON
        ↓
Stage B — Publication-Readiness Validation
        ↓
Publication Gate
```

Initial Verification therefore occurs after Stage A Validation and before Stage B Publication-Readiness Validation.

---

# Reverification

**Reverification** occurs after the initial production moment.

Potential triggers include:

- scheduled Maintenance;
- Source migration;
- algorithm review;
- external commitment review;
- suspected corruption;
- Correction investigation;
- Source Artifact update;
- manual review.

Reverification should append history rather than overwrite prior results.

---

# Verification History

Verification events should remain historically preserved.

Conceptually:

```text
Verification 1
→ result preserved

Verification 2
→ result preserved

Verification 3
→ result preserved
```

A later result does not erase the earlier result.

---

# Source Change

A Source Artifact may legitimately change after anchoring.

Verification must test the Source representation governed by the Integrity Reference.

It should not silently substitute a newer Source Version.

Conceptually:

```text
Integrity Reference A
→ Source Version 1

Source Version 2
→ separate integrity decision
```

A later Source Version may require:

- new Anchor Version;
- new Integrity Reference;
- no Anchor action;

depending on later Versioning architecture.

---

# Verification and Corrections

A Verification mismatch may reveal an Anchor-owned error.

Examples include:

- wrong digest;
- wrong Source-System Identifier;
- wrong Representation Boundary;
- wrong canonicalization method;
- wrong algorithm metadata;
- wrong timestamp;
- wrong signer reference.

If Anchor recorded incorrect information:

```text
Verification finding
        ↓
Correction review
        ↓
Correct forward
        ↓
preserve prior state
```

Anchor must not silently rewrite the original record.

---

# Verification and Provenance

Provenance explains how the integrity evidence was generated.

Verification uses that provenance to repeat or validate the process.

```text
Provenance
→ production explanation

Verification
→ production test
```

Missing provenance may make Verification impossible.

---

# Verification and Relationships

Relationships may connect:

```text
Integrity Reference
→ Source Artifact

Integrity Reference
→ Verification Record

Integrity Reference
→ external commitment
```

Verification consumes these relationships where necessary.

---

# Verification and Controlled Values

Verification proves the need for a governed:

```text
Verification Result
```

category.

Production has now frozen `match` as the first Verification Result value. Failure and non-comparison values remain intentionally unfrozen until production demonstrates which distinctions are necessary.

---

# Verification and Validation

Verification and Validation answer different questions.

```text
Verification
→ Does the representation match the preserved integrity evidence?

Validation
→ Does the Integrity Reference satisfy Anchor's institutional and schema requirements?
```

A record may:

```text
pass Validation
but fail Verification
```

or:

```text
Verify successfully
but fail an institutional Validation rule
```

The Validation architecture and formal Procedures now define the staged production sequence.

---

# Verification Procedure

The formal Integrity Verification Procedure now operationalizes this architecture.

The production sequence is:

```text
1. Confirm Stage A Validation PASS.
2. Identify Anchor Identifier and Anchor Version.
3. Load the Integrity Reference.
4. Confirm Source and Representation context.
5. Obtain the Reviewed Representation.
6. Reconstruct the Canonical Representation using the recorded canonicalization rule.
7. Identify the applicable Integrity Method and algorithm.
8. Reproduce or validate Integrity Material.
9. Compare expected and observed material.
10. Record the method-level outcome.
11. Determine the Verification Result.
12. Preserve the Verification event.
13. Proceed to Stage B only when the required Initial Verification condition is satisfied.
```

Mismatch or non-comparison conditions route to governed investigation, Correction, Maintenance, or other applicable handling rather than silent publication.

---

# Verification Failure Handling

Verification should never silently convert uncertainty into success or failure.

Conceptually:

```text
comparison reached + values agree
→ match

comparison reached + values disagree
→ mismatch

valid comparison not reached
→ non-comparison result
```

This three-way distinction is foundational.

---

# Verification Evidence

A Verification event may need to preserve evidence such as:

- reproduced Integrity Value;
- compared expected value;
- method identifier;
- verification tool or implementation;
- proof validation result;
- external-system response;
- reviewer or process attribution;
- timestamp.

The minimum required evidence remains unfrozen.

---

# Verification Reproducibility

Where possible, another independent verifier should be able to reproduce the same result using:

```text
Integrity Reference
+
Reviewed Representation
+
governed method
+
provenance
+
Verification Material
```

This is a central quality target.

---

# Verification Privacy

Verification records should preserve only necessary operational detail.

Do not collect excessive personal data merely because a reviewer was involved.

Prefer:

- institutional role;
- process identifier;
- verifier software Version;
- key reference;
- verification timestamp;

over unnecessary personal profile information.

---

# First Production Application — SCRD JSON

Anchor's first production candidate uses:

```text
Source Artifact
→ SCRD-SC-CERT-2026-0001

Representation Type
→ canonical_json

Representation Boundary
→ complete SCRD JSON document

Integrity Method
→ cryptographic_digest

Expected successful Verification Result
→ match
```

Verification therefore requires a deterministic transformation from the reviewed JSON data to the exact Canonical Representation used for digest generation.

Conceptually:

```text
Reviewed JSON
        ↓
governed deterministic JSON canonicalization / serialization
        ↓
Canonical Representation
        ↓
recorded digest algorithm
        ↓
Reproduced Integrity Value
        ↓
exact comparison
```

For this first production case, the canonical representation should be independent of:

```text
indentation
insignificant whitespace
object-member presentation order
```

provided the underlying JSON data is equivalent under the governed canonicalization rule.

This avoids making cosmetic formatting changes look like substantive integrity changes.

The exact named canonicalization standard and digest algorithm remain the next production decisions and must be recorded before integrity material is generated.

---

# Current Freeze Decisions

### Architecture Defined

```text
Verification inputs
Reviewed Representation
Canonical reconstruction
method-level Verification
comparison
Verification event
Initial Verification
Reverification
Verification history
staged Validation relationship
formal Verification Procedure
distinction between match, mismatch, and non-comparison conditions
```

### Production-Frozen Verification Result

```text
match
```

### Still Unfrozen

```text
mismatch
unable_to_verify
incomplete_material
method_unavailable
method-level result schema beyond current need
overall composite-result logic
Verification Record identifier
Verification Record schema
Initial Verification / Reverification type tokens
required Verification evidence beyond current production need
Verifier attribution requirements
external-service failure handling
Bitcoin-specific Verification procedure
Verification-to-Integrity-State transition rules beyond current
```

### First-Production Representation Decision

```text
deterministic JSON canonicalization / serialization required
exact named canonicalization standard → next decision
digest algorithm → next decision
```

---

# Verification Principle

> Reproduce faithfully. Compare precisely. Report only what the evidence proves.

Anchor Verification should preserve the distinction between demonstrated consistency, demonstrated mismatch, and situations where a valid comparison cannot be reached.

---

## Status

**Post-Foundational Architecture · First-Production Verification Reconciled**

Integrity Verification semantics, staged Validation relationship, formal procedure relationship, and the first production SCRD JSON application are now defined.

The first production-frozen Verification Result is:

```text
match
```

The next production decisions are:

```text
exact named JSON canonicalization / serialization standard
digest algorithm
Integrity Value encoding
```

Failure-result vocabulary and more complex Verification structures remain intentionally unfrozen until production proves they are necessary.

**Version:** 1.0-draft

**Maintained By:** Satoshium
