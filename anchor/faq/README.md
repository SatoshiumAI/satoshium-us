# Frequently Asked Questions (FAQ)

## What is Satoshium Anchor?

Satoshium Anchor is the Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Anchor preserves cryptographic, temporal, signature, and verification context so a later reviewer can determine whether a reviewed artifact representation remains consistent with the representation that was originally anchored.

The governing principle is:

> Preserve durable integrity context without absorbing the authority of the referenced record.

---

## What is Anchor's canonical object?

Anchor's canonical operational object is:

```text
Integrity Reference
```

An Integrity Reference is an Anchor-owned record that preserves governed integrity information for a defined representation of an authoritative artifact.

It may eventually include:

- Anchor Identifier;
- Source Institution;
- Source-System Identifier;
- artifact type;
- Canonical Representation;
- Representation Boundary;
- Integrity Method;
- Integrity Value;
- algorithm metadata;
- timestamps;
- signatures;
- Verification Material;
- Anchor Version;
- Integrity State;
- Publication State;
- Lifecycle State;
- Correction lineage;
- verification history.

The final production field set remains to be established.

---

## What does Anchor actually preserve?

Anchor preserves the **integrity context** needed to review an artifact later.

That may include:

```text
Source reference
Canonical Representation
Representation Boundary
Integrity Value
Hash Algorithm
Timestamp
Signature
Verification Material
External commitment reference
Anchor metadata
```

Anchor does not need to duplicate the complete Source Artifact merely to preserve integrity evidence about it.

---

## What is an Authoritative Artifact?

An **Authoritative Artifact** is a record, file, package, publication, statement, dataset, or other governed object whose substantive authority remains with the institution that created or maintains it.

Examples may include:

- a Certification Package;
- a Satoshium Registry Entry;
- a Chronicle Entry;
- a Trust Statement;
- an Atlas record;
- a Workflow Definition;
- another governed Suite artifact.

Anchor may preserve an Integrity Reference for such an artifact without becoming authoritative for its substantive meaning.

---

## What is a Source Institution?

The **Source Institution** is the institution or system that owns or maintains the Authoritative Artifact referenced by Anchor.

Examples include:

```text
Atlas
Certifier
Registry
Chronicle
Beacon
Attestor
Navigator
```

The Source Institution retains substantive authority.

Anchor owns only the Integrity Reference.

> Reference does not transfer authority.

---

## What is a Canonical Representation?

A **Canonical Representation** is the exact governed representation used to generate or verify an Integrity Value.

Examples may include:

- canonical JSON;
- a defined Markdown file;
- a specific HTML artifact;
- a serialized record;
- a package file;
- another reproducible representation.

Anchor must know exactly what representation was anchored before integrity material is meaningful.

---

## What is a Representation Boundary?

A **Representation Boundary** defines what content is included in the Integrity Reference and what is excluded.

For example, an anchored record may include:

```text
canonical record content
```

while excluding:

```text
site navigation
footer
dynamic interface elements
later comments
derived presentation
```

The purpose is reproducibility.

---

## Why doesn't Anchor simply hash a file?

A hash without context may have limited institutional value.

Anchor must first establish:

```text
Which artifact?
Which Source Institution?
Which representation?
Which Representation Boundary?
Which integrity method?
```

Only then should an Integrity Value be generated.

The governing rule is:

> Define the representation before generating the integrity value.

---

## What is an Integrity Value?

An **Integrity Value** is a machine-generated value derived from a defined artifact representation to support later comparison or verification.

A cryptographic digest is one common example.

The broader term allows Anchor to remain implementation-neutral.

---

## Is a cryptographic digest the same as an Integrity Reference?

No.

A digest may be one component of an Integrity Reference.

Conceptually:

```text
Canonical Representation
        ↓
Hash Algorithm
        ↓
Cryptographic Digest
```

The Integrity Reference preserves the surrounding institutional context needed to understand and later verify that digest.

---

## What is Integrity Verification?

**Integrity Verification** determines whether a reviewed artifact representation remains consistent with the Integrity Reference that governs it.

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

---

## Does a successful Integrity Verification prove that the content is true?

No.

A record can retain perfect cryptographic integrity and still contain incorrect information.

Therefore:

```text
Integrity
≠
Truth
```

Anchor verifies consistency of representation, not substantive truth.

---

## Is Integrity Verification the same as certification?

No.

Anchor asks:

> Does this representation remain consistent with its Integrity Reference?

Certifier performs certification under Suite Standards and Suite Methodology.

Therefore:

```text
Integrity Verification
≠
Certification
```

Anchor may preserve integrity for Certifier artifacts without becoming the certification authority.

---

## Is Anchor the historical authority for records it anchors?

No.

Chronicle remains authoritative for Chronicle Entries and historical-preservation representation.

Anchor may preserve an Integrity Reference for a Chronicle Entry.

That does not make Anchor the historical authority.

```text
Chronicle → Chronicle Entry
Anchor    → Integrity Reference
```

---

## Does Anchor determine trust?

No.

Attestor remains authoritative for:

```text
Trust Statement
```

Anchor may preserve the integrity of a Trust Statement representation.

It does not determine whether the statement should be trusted.

Therefore:

```text
Integrity
≠
Trust
```

---

## Does Anchor calculate reputation?

No.

Anchor does not:

- calculate reputation;
- assign reputation scores;
- rank people or institutions;
- maintain reputation profiles;
- aggregate reputation history.

Anchor may preserve the integrity of an externally governed reputation-related artifact.

---

## Is Anchor an identity system?

No.

The earlier pre-Suite Anchor concept treated identity as its foundational institutional layer.

That is no longer the current model.

Anchor may preserve identity-related **attribution metadata** such as:

- Source Institution;
- signer;
- signing key;
- producing system;
- reviewer;
- institutional role.

But Anchor does not issue personal identities, credentials, authentication services, or identity networks.

---

## What happened to the old Identities, Claims, Attestations, Reputation, and Trust pages?

Those routes are retained for continuity, but their institutional roles have been narrowed.

They now explain how Anchor may preserve integrity context for externally governed artifacts.

Conceptually:

```text
Identity
→ supporting attribution metadata

Claims
→ claim artifact integrity

Attestations
→ attestation artifact integrity

Reputation
→ reputation-related artifact integrity

Trust
→ trust-related artifact integrity
```

Anchor does not own the substantive authority of those concepts.

---

## How does Anchor relate to Certifier?

Certifier remains authoritative for:

- Certification Packages;
- certification determinations;
- certification lifecycle;
- certification status;
- generated certification artifacts.

Anchor may preserve Integrity References for Certifier artifacts.

For example:

```text
SC-CERT-2026-0001
```

remains Certifier-owned even if Anchor later preserves the integrity of one of its canonical representations.

---

## How does Anchor relate to Registry?

Registry remains authoritative for:

```text
Satoshium Registry Entry
```

including Registry metadata, classification, lifecycle, Versions, Corrections, and publication.

Anchor may preserve an Integrity Reference for a defined Registry representation.

For example:

```text
SREG-2026-0001
```

remains Registry-owned.

---

## How does Anchor relate to Chronicle?

Chronicle remains authoritative for:

```text
Chronicle Entry
```

and its historical-preservation representation.

Anchor may preserve an Integrity Reference for a defined Chronicle Entry representation.

For example:

```text
CHR-2026-0001
```

remains Chronicle-owned.

---

## How does Anchor relate to Attestor?

Attestor remains authoritative for:

```text
Trust Statement
```

and Attestor-controlled trust judgments, lifecycle, Versions, Corrections, and publication.

Anchor may preserve the Integrity Reference.

The trust conclusion remains Attestor-owned.

---

## How does Anchor relate to Atlas, Beacon, and Navigator?

The current Suite object model is:

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

Anchor may preserve integrity context for authoritative artifacts from these institutions without absorbing their authority.

---

## Does Anchor use blockchain technology?

Anchor is implementation-neutral.

Potential implementation mechanisms may include:

- cryptographic hashing;
- digital signatures;
- timestamping;
- transparency logs;
- Merkle structures;
- distributed systems;
- external commitments;
- Bitcoin commitments;
- future cryptographic mechanisms.

No single technology defines Anchor.

---

## Will Anchor use Bitcoin?

Possibly.

Bitcoin may eventually provide a useful external commitment layer for:

- proof-of-existence;
- timestamp anchoring;
- Merkle-root commitments;
- batch commitments;
- long-term public integrity checkpoints.

However, Bitcoin has not yet been adopted as a production Anchor commitment mechanism.

Anchor's institutional meaning must remain valid regardless of the implementation technology.

---

## Is Anchor a blockchain?

No.

Anchor is an integrity-preservation institution.

Blockchain or Bitcoin may become tools used by Anchor.

They are not the definition of Anchor.

The governing principle is:

> The institution is not blockchain. The institution is integrity preservation.

---

## What happens if the Source Artifact changes after anchoring?

A Source Artifact may legitimately change because of:

- a new Version;
- a Correction;
- supersession;
- withdrawal;
- revocation;
- republication;
- migration;
- a changed canonical representation.

A later change does not erase the earlier Integrity Reference.

Anchor should preserve enough lineage to distinguish:

```text
Earlier Source Representation
        ↓
Earlier Integrity Reference

Later Source Representation
        ↓
Later Anchor Version or New Integrity Reference
where required
```

The final Versioning rule remains to be established.

---

## What is the difference between a Source Correction and an Anchor Correction?

A **Source Correction** changes the external artifact under the authority of the Source Institution.

An **Anchor Correction** changes Anchor's own record because Anchor recorded something incorrectly.

Examples of Anchor errors may include:

- wrong Source Artifact;
- wrong Source-System Identifier;
- wrong Canonical Representation;
- wrong Representation Boundary;
- wrong digest;
- wrong algorithm;
- wrong timestamp;
- wrong signer metadata;
- wrong Verification Material.

The governing rule is:

> Correct forward. Preserve backward.

---

## What is Anchor's current development status?

Anchor is currently in:

```text
Foundation Reconciliation
```

The institutional model is substantially defined, but production architecture is not yet finalized.

No production Integrity Reference has been issued.

---

## Is Anchor in production?

No.

Anchor currently has a mature institutional foundation but not a completed production implementation.

The following remain to be finalized:

```text
Anchor Identifier format
Controlled Values
Integrity Reference schema
Integrity Verification procedure
Validation architecture
Publication architecture
Lifecycle architecture
Versioning rules
Correction procedure
Maintenance procedure
Bitcoin commitment policy
first production Integrity Reference
```

---

## What is the difference between project status and record state?

This FAQ and `/anchor/status/` describe the development status of the Anchor institution.

That is separate from the future state of an individual Integrity Reference.

```text
Project Development Status
≠
Integrity State
≠
Verification Result
≠
Publication State
≠
Lifecycle State
```

Those record-level vocabularies remain intentionally unfrozen.

---

## What comes next for Anchor?

After the remaining foundation work is complete, the expected production-development path is:

```text
Complete Foundation Reconciliation
        ↓
Define Identifier Architecture
        ↓
Define Controlled Values
        ↓
Define Integrity Reference Schema
        ↓
Define Verification / Validation
        ↓
Define Publication / Lifecycle
        ↓
Define Versioning / Corrections
        ↓
Define Maintenance
        ↓
Define Production Procedure
        ↓
Create First Production Integrity Reference
        ↓
Review and Refine Architecture
```

This order may change if production design reveals a better dependency sequence.

---

## What principle governs Anchor interoperability?

The central rule is:

> Reference does not transfer authority.

Anchor may strengthen another artifact by preserving its integrity context.

That relationship never makes Anchor the substantive authority for the referenced record.

---

## What principle governs Anchor production readiness?

The governing principle is:

> Define the institution. Prove the process. Then declare production.

Documentation alone is not sufficient.

Production readiness should follow successful end-to-end creation and verification of a real Integrity Reference.

---

## Status

**Status:** Foundation Reconciliation

**Version:** 1.0-draft

**Maintained By:** Satoshium
