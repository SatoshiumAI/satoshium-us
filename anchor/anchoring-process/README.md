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

The production Anchoring Process is:

```text
Identify Authoritative Artifact
        ↓
Confirm Source Authority
        ↓
Define Canonical Representation
        ↓
Define Representation Boundary
        ↓
Select Integrity Method / Algorithm
        ↓
Generate Integrity Value
        ↓
Construct Integrity Reference Candidate
        ↓
Assign Anchor Identifier + Anchor Version
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
        ↓
Publication / Preservation
        ↓
Maintenance / Reverification / Lineage
```

This sequence is aligned with the completed Anchor Validation, Verification, Publication, Versioning, Procedures, and first-production architecture.

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

Determine the exact representation used to generate the Integrity Value.

For the first production candidate:

```text
Source Artifact
→ SCRD-SC-CERT-2026-0001

Representation Type
→ canonical_json

Canonicalization
→ RFC 8785 — JSON Canonicalization Scheme (JCS)

Encoding
→ UTF-8
```

Later representation types may use different governed canonicalization rules.

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

Select the governed integrity method and algorithm appropriate for the representation.

For IR #1:

```text
Integrity Method
→ cryptographic_digest

Algorithm
→ SHA-256

Digest Encoding
→ lowercase hexadecimal
```

Other integrity methods remain available for future governed production where they add durable value.

---

# Step 6 — Generate Integrity Value

Generate the Integrity Value from the governed Canonical Representation.

For IR #1:

```text
SCRD JSON
        ↓
RFC 8785 JCS
        ↓
UTF-8 canonical byte sequence
        ↓
SHA-256
        ↓
64-character lowercase hexadecimal Integrity Value
```

The value must remain interpretable together with its representation, algorithm, source, provenance, and Verification context.

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

# Step 8 — Construct Integrity Reference Candidate

Construct the Anchor-owned Integrity Reference candidate under the Base Schema.

The first production candidate uses:

```text
Anchor Identifier
→ ANCH-2026-0001

Anchor Version
→ 1

Source-System Identifier
→ SCRD-SC-CERT-2026-0001

Relationship Type
→ references_source

Representation Type
→ canonical_json

Integrity Method
→ cryptographic_digest
```

The Integrity Reference Base Schema defines the required production structure.

---

# Step 9 — Validate and Verify Construction

Construction now uses the staged production model:

```text
Stage A — Structural / Institutional Validation
        ↓
Initial Verification
        ↓
expected successful result → match
        ↓
Stage B — Publication-Readiness Validation
```

Validation tests institutional and schema requirements.

Verification tests whether the Reviewed Representation, reconstructed under the governed canonicalization rule, reproduces the stored Integrity Value.

---

# Step 10 — Publication Gate and Publish / Preserve

A candidate proceeds to publication only after:

```text
Stage B Validation PASS
        ↓
Human / Machine consistency confirmed
        ↓
Publication Gate
        ↓
APPROVED
        ↓
Publication
```

Publication changes the Anchor Publication State from:

```text
unpublished
```

to:

```text
published
```

for the approved Anchor Version.

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

The current Base Schema provides production structure for:

```text
Anchor Identifier
Anchor Version
Schema Version
Source
Representation
Integrity Methods
Provenance
Relationships
Record State
Verification History
Corrections
Publication
Maintenance
Notes
```

Production requirements are now governed through the Base Schema, Controlled Values, Validation Rules, and Procedures rather than remaining an architectural inventory.

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

The completed Versioning architecture now uses the integrity subject test:

```text
same Source Artifact identity
+
same Canonical Representation
+
same Representation Boundary
→ same integrity subject
→ governed Anchor change may create a new Anchor Version

different integrity subject
→ new Integrity Reference
→ new Anchor Identifier
```

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

# First Production Application — ANCH-2026-0001

```text
Source Institution
→ Satoshium Certifier

Source Artifact
→ SCRD-SC-CERT-2026-0001

Source Version
→ 1.1

Representation Boundary
→ complete SCRD JSON document

Representation Type
→ canonical_json

Canonicalization
→ RFC 8785 JCS

Encoding
→ UTF-8

Integrity Method
→ cryptographic_digest

Algorithm
→ SHA-256

Digest Encoding
→ lowercase hexadecimal

Relationship
→ references_source

Anchor Identifier
→ ANCH-2026-0001

Anchor Version
→ 1
```

`ANCH-2026-0001` is assigned but not yet published.

It must still complete:

```text
Stage A Validation
Initial Verification
Stage B Publication-Readiness Validation
Publication Gate
```

before entering public Anchor authority.

---

# Process Principle

The governing Anchoring Process principle is:

> Define the representation. Generate the integrity evidence. Preserve the reference. Make later verification possible.

---

## Status

**Post-Foundational Architecture · First-Production Process Reconciled**

The Anchoring Process is now aligned with the completed production architecture and the first assigned Integrity Reference candidate.

Production-defined elements include:

```text
Anchor Identifier → ANCH-2026-0001
Anchor Version → 1
Source Artifact → SCRD-SC-CERT-2026-0001
Representation Type → canonical_json
Canonicalization → RFC 8785 JCS
Encoding → UTF-8
Integrity Method → cryptographic_digest
Algorithm → SHA-256
Digest Encoding → lowercase hexadecimal
Relationship Type → references_source
Validation → Stage A + Stage B
Initial Verification → required
Publication Gate → required
```

The following remain intentionally future-facing:

```text
signature-specific procedure
timestamp-specific procedure
external commitment procedure
Bitcoin commitment procedure
composite-method procedure
later Integrity Reference production cases
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
