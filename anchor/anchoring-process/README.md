# Anchoring Process

## Overview

The **Anchoring Process** defines the repeatable institutional procedure by which an authoritative artifact becomes associated with a durable **Satoshium Anchor Integrity Reference**.

Anchor does not begin with hashing.

Anchor begins by determining:

```text
What artifact is being referenced?
Who owns it?
Which exact representation is being anchored?
What representation boundary applies?
Which integrity method is appropriate?
```

Only after those questions are answered should integrity material be generated.

The governing principle is:

> Define the representation before generating the integrity value.

---

## Process Purpose

The Anchoring Process exists to create a durable, reproducible, and later-verifiable integrity relationship between:

```text
an authoritative artifact representation
```

and:

```text
an Anchor-owned Integrity Reference
```

The process preserves integrity context without transferring authority away from the Source Institution.

> Reference does not transfer authority.

---

## Process Boundary

Anchor does not create the substantive Source Artifact.

Anchor does not determine:

- what the artifact means;
- whether its claims are true;
- whether a certification should be issued;
- whether a Registry Entry should remain active;
- whether a Chronicle Entry is historically significant;
- whether a Trust Statement should be accepted;
- whether an identity should be trusted.

Anchor begins when a candidate artifact has been identified for integrity preservation.

---

# Anchoring Sequence

The current institutional Anchoring Process is:

```text
Identify Authoritative Artifact
        ↓
Confirm Source Authority
        ↓
Define Canonical Representation
        ↓
Define Representation Boundary
        ↓
Select Integrity Method
        ↓
Generate Integrity Value
        ↓
Record Temporal / Signature / Verification Material
        ↓
Construct Integrity Reference
        ↓
Verify Construction
        ↓
Publish / Preserve
        ↓
Maintain / Reverify when required
        ↓
Preserve Lineage
```

This sequence establishes the conceptual process.

Final production procedures may later add formal Validation, Publication Gate, identifier assignment, schema conformance, or other operational requirements where production demonstrates a need.

---

# Step 1 — Identify Authoritative Artifact

Identify the record, package, file, publication, dataset, statement, or other governed object whose integrity should be preserved.

Examples may include:

```text
Atlas record
Certification Package
SCPR
SCR
SCRD
Satoshium Registry Entry
Chronicle Entry
Discovery artifact
Trust Statement
Workflow Definition
other governed Suite artifact
```

Not every available artifact should automatically receive an Integrity Reference.

Anchor should preserve integrity where the reference provides durable institutional value.

---

# Step 2 — Confirm Source Authority

Confirm the Source Institution responsible for the Authoritative Artifact.

Record or identify, where available:

- Source Institution;
- Source-System Identifier;
- artifact type;
- artifact Version;
- canonical public or repository location;
- applicable source status or lifecycle context where materially relevant.

This step preserves the distinction between:

```text
Source Artifact
```

and:

```text
Anchor Integrity Reference
```

Anchor does not replace source authority.

---

# Step 3 — Define Canonical Representation

Determine the exact representation that will be used to generate the Integrity Value.

Examples may include:

- canonical JSON;
- defined Markdown source;
- a specific HTML artifact;
- a serialized package;
- a stable exported file;
- a governed canonical byte sequence;
- another reproducible representation.

The Canonical Representation should be clear enough that a later reviewer can understand what was processed.

---

# Step 4 — Define Representation Boundary

Define what content is included in the Integrity Reference.

The Representation Boundary may need to distinguish:

```text
record content
from
site-wide navigation / footer / dynamic presentation
```

or:

```text
canonical record
from
generated derivative artifact
```

or:

```text
one file
from
an entire package
```

The goal is reproducibility.

A later reviewer should be able to determine what the Integrity Reference covers and what it does not cover.

---

# Step 5 — Select Integrity Method

Select the governed integrity method appropriate for the representation.

Potential mechanisms may include:

```text
cryptographic digest
digital signature
timestamping method
Merkle structure
external commitment
Bitcoin commitment
other approved integrity mechanism
```

The final controlled vocabulary for Integrity Methods remains unfrozen.

The method should be selected because it supports the integrity requirement, not because a particular technology is available.

---

# Step 6 — Generate Integrity Value

Generate the Integrity Value from the defined Canonical Representation.

A common initial pattern is:

```text
Canonical Representation
        ↓
Hash Algorithm
        ↓
Cryptographic Digest
```

The generated value should not be interpreted independently from:

- the representation definition;
- algorithm metadata;
- source reference;
- temporal context;
- other required verification information.

A hash without context is not a complete Integrity Reference.

---

# Step 7 — Record Temporal / Signature / Verification Material

Record the material needed to interpret and later reproduce or validate the integrity result.

This may include:

- digest algorithm;
- digest value;
- anchoring timestamp;
- observation timestamp;
- signature;
- signer or key reference;
- canonicalization instructions;
- representation metadata;
- external commitment reference;
- Bitcoin commitment reference;
- verification instructions;
- material limitations.

Different timestamps should retain their distinct meanings.

---

# Step 8 — Construct Integrity Reference

Construct the Anchor-owned **Integrity Reference**.

The Integrity Reference should connect:

```text
Anchor identity
+
Source Institution
+
Source-System Identifier
+
Canonical Representation
+
Representation Boundary
+
Integrity Value
+
Verification Material
+
Temporal Context
```

The final required field set remains subject to later Anchor schema architecture.

---

# Step 9 — Verify Construction

Before public production use, confirm that the constructed Integrity Reference actually corresponds to the intended artifact representation.

Verification may include:

- regenerating the digest;
- validating a signature;
- checking Source-System Identifier consistency;
- reviewing timestamps;
- confirming representation instructions;
- checking human / machine consistency;
- verifying external commitment references;
- confirming authority boundaries.

The exact production Verification and Validation separation remains to be established through later Anchor architecture.

---

# Step 10 — Publish / Preserve

When production requirements are satisfied, the Integrity Reference may proceed into public or preserved institutional state.

Later Anchor architecture should determine:

```text
Publication State
Lifecycle State
Publication procedure
Validation requirements
Publication Gate, if required
canonical public package
machine-readable representation
```

This Anchoring Process intentionally does not prematurely freeze those mechanisms.

---

# Step 11 — Maintain / Reverify

An Integrity Reference may require later review when:

- the Source Artifact changes;
- a Source reference breaks;
- a Canonical Representation changes;
- an algorithm becomes unsuitable;
- a signature becomes unverifiable;
- a timestamp reference changes;
- external commitment verification fails;
- Anchor discovers a recording error;
- later institutional verification is required.

Maintenance does not automatically mean the earlier Integrity Reference was wrong.

---

# Step 12 — Preserve Lineage

Anchor should preserve enough lineage to reconstruct:

- which artifact representation was anchored;
- which Source Artifact Version applied;
- which Integrity Reference covered it;
- which Anchor Version applied;
- whether a Correction occurred;
- whether later verification succeeded;
- whether a later Integrity Reference was created;
- whether a later representation superseded the earlier one.

The governing preservation principle is:

> Correct forward. Preserve backward.

---

# What the Process Produces

The Anchoring Process produces an Anchor-owned:

```text
Integrity Reference
```

A production Integrity Reference may eventually include:

```text
Anchor Identifier
Source Institution
Source-System Identifier
Artifact Type
Artifact Version
Canonical Representation
Representation Boundary
Integrity Method
Integrity Value
Hash Algorithm
Timestamp(s)
Signature information
Verification Material
Integrity State
Anchor Version
Publication State
Lifecycle State
Correction lineage
Verification history
```

This is an architectural inventory, not yet the final production schema.

---

# Canonical Representation Comes Before Hashing

The most important operational correction from the pre-Suite Anchor model is:

```text
Do not begin with:
Hash the artifact.
```

Instead begin with:

```text
Which artifact?
        ↓
Which Source Institution?
        ↓
Which exact representation?
        ↓
Which Representation Boundary?
        ↓
Which governed integrity method?
        ↓
Generate Integrity Value
```

This prevents integrity records from becoming ambiguous or irreproducible.

---

# Hashes

Hashing is a mechanism within Anchor.

It is not Anchor itself.

A digest may be useful only if later reviewers know:

- the exact input representation;
- the algorithm;
- the digest value;
- any canonicalization rules;
- the Source Artifact identity;
- applicable time context.

---

# Timestamps

Timestamps preserve temporal context.

Potential meanings include:

```text
artifact observed at
digest generated at
Integrity Reference created at
anchored at
published at
verified at
```

These should not be collapsed unless the production architecture explicitly defines them as equivalent.

---

# Signatures

Signatures may support:

- origin verification;
- integrity verification;
- process accountability;
- key-based verification.

A signature does not automatically establish:

```text
truth
certification
Source Institution authority
reputation
trustworthiness
```

The governing distinction is:

```text
Signature
≠
Institutional Authority
```

---

# External Commitments

Anchor may later support external commitment mechanisms.

Potential examples include:

- transparency logs;
- third-party timestamping;
- Merkle roots;
- distributed commitments;
- Bitcoin commitments;
- OpenTimestamps-style mechanisms.

An external commitment may strengthen independent verifiability.

It does not replace the Integrity Reference or the Source Artifact.

---

# Bitcoin Commitments

Bitcoin may eventually serve as an external commitment layer for Anchor.

Possible future patterns include:

```text
single-artifact commitment
Merkle-root batch commitment
proof-of-existence timestamp
long-term public integrity checkpoint
```

The Anchoring Process should remain valid even when Bitcoin is not used.

The sequence should therefore be:

```text
Define Anchor integrity meaning first
        ↓
Use Bitcoin where it adds durable verification value
```

rather than:

```text
Use Bitcoin first
        ↓
Invent institutional meaning afterward
```

---

# Source Artifact Changes

A Source Artifact may legitimately change after anchoring.

Examples include:

- new Version;
- Correction;
- lifecycle change;
- republishing;
- migration;
- canonical representation change;
- superseding artifact.

A later change does not erase the earlier Integrity Reference.

The earlier Integrity Reference remains evidence about the representation it originally covered.

---

# New Integrity Reference vs. New Anchor Version

A later Source Artifact change may eventually require either:

```text
new Anchor Version
```

or:

```text
new Integrity Reference
```

The distinction is not yet frozen.

It should be established through later Anchor Versioning and production architecture.

The governing question should be whether the same Anchor identity continues to represent the same integrity relationship or whether a distinct integrity object now exists.

---

# Verification After Anchoring

Later verification follows the conceptual process:

```text
Integrity Reference
        +
Reviewed Artifact Representation
        ↓
Reproduce / Validate Integrity Material
        ↓
Compare
        ↓
Verification Result
```

A matching result supports integrity consistency.

A mismatch requires investigation.

Possible causes include:

- legitimate Source Artifact change;
- wrong artifact selected;
- wrong representation;
- canonicalization mismatch;
- encoding difference;
- algorithm mismatch;
- corruption;
- unauthorized alteration;
- incomplete retrieval;
- Anchor recording error.

Anchor should record evidence.

It should not invent the explanation.

---

# Authority Boundary

The Source Institution owns the Authoritative Artifact.

Anchor owns the Integrity Reference.

For example:

```text
SC-CERT-2026-0001
```

remains Certifier-owned.

An Anchor Integrity Reference may preserve the integrity of a defined representation of that Certification Package.

Anchor does not become the certification authority.

Likewise:

```text
SREG-2026-0001
```

remains Registry-owned.

```text
CHR-2026-0001
```

remains Chronicle-owned.

> Reference does not transfer authority.

---

# Relationship to Anchor Purpose

Anchor Purpose defines why Anchor exists:

> Preserve durable integrity context without absorbing the authority of the referenced record.

The Anchoring Process defines how that purpose begins to be operationalized.

---

# Relationship to Anchor Definitions

Canonical terminology is defined through:

```text
/anchor/definitions/
```

The Anchoring Process relies especially on:

- Authoritative Artifact;
- Source Institution;
- Canonical Representation;
- Representation Boundary;
- Integrity Reference;
- Integrity Value;
- Cryptographic Digest;
- Hash Algorithm;
- Timestamp;
- Signature;
- Verification Material;
- Anchoring;
- Integrity Verification;
- Verification Result;
- Anchor Version.

---

# Relationship to Integrity Preservation

Integrity Preservation defines the continuing institutional function.

The Anchoring Process defines the creation path that begins that preservation relationship.

Conceptually:

```text
Anchoring Process
        ↓
Integrity Reference Created
        ↓
Integrity Preservation
        ↓
Later Verification / Maintenance / Lineage
```

---

# Process Principle

The governing Anchoring Process principle is:

> Define the representation. Generate the integrity evidence. Preserve the reference. Make later verification possible.

---

## Status

**Foundation Reconciliation**

This document establishes the current institutional Anchoring Process.

The following remain intentionally unfrozen pending later architecture and production testing:

```text
Anchor identifier format
Integrity Method Controlled Values
Integrity State values
Verification Result values
required production field set
machine-readable schema
Validation architecture
Publication architecture
Lifecycle vocabulary
Versioning rules
Bitcoin commitment procedure
first production Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
