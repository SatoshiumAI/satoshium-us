# Integrity Preservation

## Overview

**Integrity Preservation** defines the enduring institutional function of **Satoshium Anchor**.

Anchor exists to preserve durable evidence that an authoritative artifact existed in a defined representation and can later be evaluated for integrity.

Anchor may use:

- cryptographic digests;
- hashes;
- timestamps;
- signatures;
- verification metadata;
- public logs;
- external commitments;
- future Bitcoin-based commitments;
- other governed integrity mechanisms.

These are implementation tools.

They are not the institutional definition of Anchor.

The governing principle is:

> The institution is not blockchain. The institution is integrity preservation.

---

## Institutional Purpose

Anchor preserves **Integrity References**.

An Integrity Reference allows a later reviewer to evaluate whether a reviewed artifact representation remains consistent with the representation that was originally anchored.

Conceptually:

```text
Authoritative Artifact
        ↓
Defined Canonical Representation
        ↓
Integrity Value
        ↓
Integrity Reference
        ↓
Later Integrity Verification
```

Anchor does not replace the authoritative artifact.

It preserves the integrity context associated with that artifact.

---

## Integrity Reference

Anchor's canonical operational object is:

```text
Integrity Reference
```

An Integrity Reference may preserve:

- Anchor identifier;
- Source Institution;
- Source-System Identifier;
- artifact type;
- Canonical Representation;
- Representation Boundary;
- Integrity Value;
- cryptographic digest;
- hash algorithm;
- timestamp;
- signature;
- verification material;
- Anchor Version;
- Publication State;
- Lifecycle State;
- Correction lineage;
- later verification information.

The Integrity Reference belongs to Anchor.

The referenced artifact remains authoritative within its Source Institution.

> Reference does not transfer authority.

---

## Canonical Representation

Integrity preservation depends on knowing exactly what was anchored.

Anchor therefore distinguishes between:

```text
the authoritative object
```

and:

```text
the exact representation used
to generate the Integrity Value
```

Examples may include:

- canonical JSON;
- published HTML;
- Markdown source;
- a Certification Package;
- a Registry Entry;
- a Chronicle Entry;
- a Trust Statement;
- another governed Suite artifact.

The Representation Boundary should be sufficiently clear that later verification is reproducible.

---

## Integrity

For Anchor, integrity means that a reviewed artifact representation can be compared against a preserved Integrity Reference.

The central question is:

> Does the artifact representation being reviewed remain consistent with the representation governed by the Integrity Reference?

Integrity does not mean:

- the artifact is substantively true;
- the artifact is certified;
- the artifact should remain active;
- the artifact is historically significant;
- the artifact should be trusted.

Those questions belong to other institutional functions.

---

## Immutability

Anchor does not require every artifact to become permanently immutable.

Instead, Anchor preserves enough integrity evidence to make later alteration:

```text
detectable
reviewable
attributable where possible
historically understandable
```

An artifact may legitimately change over time.

Anchor preserves the integrity relationship between:

```text
a particular artifact representation
```

and:

```text
the Integrity Reference created for that representation
```

---

## Tamper Evidence

Tamper evidence allows reviewers to determine whether an artifact representation appears to differ from the representation originally anchored.

A changed artifact does not automatically imply wrongdoing.

Possible explanations may include:

- legitimate Version changes;
- Corrections;
- republication;
- migration;
- canonicalization changes;
- encoding changes;
- unauthorized modification;
- corruption;
- incomplete retrieval.

Anchor's responsibility is to preserve and expose the integrity evidence.

It should not invent the reason for a mismatch.

---

## Cryptographic Preservation

Cryptographic preservation may include:

```text
hashes
content digests
digital signatures
signature-verification material
Merkle structures
external commitments
other governed cryptographic references
```

The specific mechanism may evolve.

Anchor should preserve sufficient metadata to allow a later reviewer to understand:

```text
what algorithm was used
what representation was processed
what value was generated
when the Integrity Reference was created
how verification may be reproduced
```

---

## Cryptographic Digest

A cryptographic digest is a deterministic value generated from a defined artifact representation.

Conceptually:

```text
Canonical Representation
        ↓
Hash Algorithm
        ↓
Cryptographic Digest
```

A later reviewer may reproduce the digest from the reviewed representation and compare the result.

```text
Reviewed Representation
        ↓
Same Governed Algorithm
        ↓
Reproduced Digest
        ↓
Compare with Integrity Reference
```

A matching digest supports integrity consistency.

A mismatching digest requires investigation.

---

## Temporal Context

Anchor may preserve:

- observation time;
- digest-generation time;
- anchoring time;
- publication time;
- verification time;
- external timestamp evidence.

These should not automatically be collapsed into one generic timestamp.

Each timestamp should preserve its own institutional meaning.

---

## Signatures

Digital signatures may support integrity and origin verification.

A signature may help answer questions such as:

```text
Was this representation signed with the expected key?
Was the signature valid for the representation?
Which key or signer reference was associated with the action?
```

A valid signature does not automatically establish:

```text
truth
certification
institutional authority
trustworthiness
reputation
```

The governing distinction remains:

```text
Signature
≠
Institutional Authority
```

---

## Verification Material

Verification Material may include:

- digest algorithm;
- digest value;
- signature;
- public-key reference;
- canonicalization instructions;
- representation metadata;
- timestamp information;
- external commitment reference;
- other governed integrity context.

This material allows later integrity verification to be reproduced.

---

## Integrity Verification

Integrity Verification compares a reviewed artifact representation against the Integrity Reference that governs it.

Conceptually:

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

It does not automatically establish tampering, wrongdoing, or substantive invalidity.

---

## Integrity Verification vs. Certification

Anchor asks:

> Does this representation remain consistent with its Integrity Reference?

Certifier performs certification under Suite Standards and Suite Methodology.

Therefore:

```text
Integrity Verification
≠
Certification
```

An Integrity Reference may support certification review.

It does not replace Certifier authority.

---

## Integrity Verification vs. Chronicle Verification

Chronicle Verification reviews Chronicle's historical representation.

Anchor Integrity Verification reviews the relationship between an artifact representation and its Integrity Reference.

Therefore:

```text
Anchor Integrity Verification
≠
Chronicle Verification
```

---

## Integrity vs. Truth

A record can have perfect cryptographic integrity and still contain incorrect information.

Therefore:

```text
Integrity
≠
Truth
```

Anchor does not determine substantive truth merely by confirming integrity.

---

## Integrity vs. Trust

A record can be authentic and unchanged without being trustworthy.

Therefore:

```text
Integrity
≠
Trust
```

Anchor may provide integrity evidence useful to trust evaluation.

Anchor itself does not determine trustworthiness or reputation.

---

## What Integrity Preservation Supports

Anchor may preserve Integrity References for authoritative artifacts across the Suite.

Examples include:

```text
Atlas records
Certification Packages
SCPRs
SCRs
SCRDs
Satoshium Registry Entries
Chronicle Entries
Discovery artifacts
Trust Statements
Workflow Definitions
other governed Suite artifacts
```

The exact artifact selected for anchoring should be governed by the applicable Representation Boundary.

Not every derived artifact requires its own Integrity Reference.

Minimum necessary structure remains preferred.

---

## What Integrity Preservation Does Not Do

Integrity Preservation does not determine:

- whether a claim is true;
- whether a certification is correct;
- whether a certification should remain active;
- whether a Registry Entry should remain registered;
- whether a Chronicle Entry is historically significant;
- whether a Trust Statement should be accepted;
- whether an identity is legitimate;
- whether an institution is reputable;
- whether an artifact should be trusted.

Anchor preserves integrity context.

Other institutions retain their own authority.

---

## Suite Authority Boundary

Anchor operates within the current Suite object model:

```text
Atlas
→ authoritative intelligence

Certifier
→ Certification Package

Registry
→ Satoshium Registry Entry

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Beacon
→ Discovery Signal / Metadata

Attestor
→ Trust Statement

Navigator
→ Workflow Definition
```

Anchor may preserve Integrity References for any of these objects.

It does not absorb their institutional authority.

> Reference does not transfer authority.

---

## Source Artifact Changes

An authoritative artifact may legitimately change after an Integrity Reference is created.

Examples include:

- new Source Artifact Version;
- formal Correction;
- lifecycle transition;
- republished machine-readable form;
- new canonical representation;
- superseding artifact.

A later Source Artifact change does not make the earlier Integrity Reference invalid.

Anchor should preserve enough lineage to identify:

```text
which representation was anchored
which Integrity Reference covered it
which later representation changed
whether a new Integrity Reference was created
```

---

## Anchor Corrections

Anchor corrects Anchor-owned records.

A formal Anchor Correction may be appropriate when:

- Anchor referenced the wrong artifact;
- the recorded digest was incorrect;
- the algorithm metadata was wrong;
- the timestamp was recorded incorrectly;
- representation metadata was wrong;
- verification metadata was materially incorrect;
- another Anchor-owned field requires substantive correction.

Anchor should not use Correction to rewrite the external Source Artifact.

---

## Integrity Preservation and Versions

A materially new artifact representation may require a new Integrity Reference or a new Anchor Version depending on the final production architecture.

That distinction is intentionally not frozen here.

The later Versioning architecture should determine when:

```text
same Integrity Reference identity
+
new Anchor Version
```

is appropriate versus:

```text
new Integrity Reference
```

The governing requirement is preservation of prior material states.

---

## Implementation Neutrality

Anchor is implementation-neutral.

Possible implementation mechanisms may include:

- SHA-family hashing;
- digital signatures;
- trusted timestamping;
- transparency logs;
- Merkle trees;
- distributed ledgers;
- Bitcoin commitments;
- OpenTimestamps-style mechanisms;
- future cryptographic tools.

No single implementation defines the institution.

The governing principle is:

> Tools may change. Integrity preservation remains the purpose.

---

## Bitcoin and Anchor

Bitcoin may eventually provide a valuable external commitment layer for Anchor.

Potential future uses may include:

```text
timestamp anchoring
Merkle-root commitments
proof-of-existence
batch integrity commitments
long-term independently verifiable references
```

However, Anchor should not be designed so that Bitcoin is required merely to make the architecture conceptually valid.

The institutional architecture should first define:

```text
what is being anchored
how the representation is defined
what Integrity Value is generated
what the Integrity Reference means
how verification works
```

Bitcoin can then serve as an implementation or commitment mechanism where useful.

---

## Long-Term Preservation

Integrity Preservation should support later reconstruction of:

- what artifact was referenced;
- who owned the authoritative artifact;
- which representation was anchored;
- which algorithm was used;
- which digest or signature was recorded;
- when anchoring occurred;
- which Anchor Version applied;
- whether Corrections occurred;
- whether later verification succeeded;
- whether a later Integrity Reference superseded or complemented the earlier one.

Long-term preservation is therefore not limited to preserving a hash.

It preserves the context required to understand the hash.

---

## Relationship to Anchor Purpose

The Anchor Purpose establishes:

> Satoshium Anchor preserves durable cryptographic and temporal Integrity References for authoritative artifacts so later reviewers can evaluate integrity without transferring authority away from the institution that owns the referenced record.

Integrity Preservation is the institutional function that implements that purpose over time.

---

## Relationship to Anchor Definitions

Canonical terminology for this architecture is defined through:

```text
/anchor/definitions/
```

including:

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
- Integrity State;
- Anchor Identifier;
- Anchor Version;
- Publication State;
- Lifecycle State;
- Correction;
- Maintenance;
- Integrity Preservation.

---

## Integrity Preservation Principle

The governing principle is:

> Preserve enough information that integrity can still be independently reviewed after the original moment has passed.

A shorter operational expression is:

> Integrity is preserved when change becomes visible.

---

## Status

**Foundation Reconciliation**

This document establishes the current institutional Integrity Preservation model for Anchor.

Final production details concerning:

```text
Anchor identifiers
Integrity State values
Verification Result values
Lifecycle State
Publication State
Versioning
Validation
Publication
Bitcoin commitment methods
```

remain to be established through later Anchor architectural and production work.

**Version:** 1.0-draft

**Maintained By:** Satoshium
