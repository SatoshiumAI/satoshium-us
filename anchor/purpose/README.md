# Purpose

## Overview

Satoshium Anchor is the Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Anchor records cryptographic, temporal, signature, and verification context so a later reviewer can evaluate whether a referenced artifact corresponds to the representation that was originally anchored.

Anchor does **not** assume authority over:

- the referenced artifact;
- the meaning of the artifact;
- certification decisions;
- Registry cataloging;
- Chronicle historical interpretation;
- Attestor Trust Statements;
- identity relationships;
- reputation;
- trust conclusions.

The governing principle is:

> Reference does not transfer authority.

---

## Why Anchor Exists

Digital artifacts can be:

- copied;
- republished;
- reformatted;
- migrated;
- mirrored;
- exported;
- separated from their originating systems;
- altered without obvious visual evidence.

An authoritative record may remain institutionally valid while still requiring durable integrity context that allows later reviewers to determine whether the artifact they are examining corresponds to the representation that was originally referenced.

Anchor exists to preserve that integrity context.

The governing distinction is:

```text
Authority
  answers who owns the record.

Integrity
  answers whether the referenced representation
  remains consistent with the anchored representation.
```

---

## Canonical Anchor Object

Anchor's canonical operational object is:

```text
Integrity Reference
```

An Integrity Reference preserves governed integrity information associated with a defined artifact representation.

Depending on the applicable Anchor architecture, an Integrity Reference may preserve:

- referenced artifact identity;
- canonical representation boundary;
- cryptographic digest;
- digest algorithm;
- timestamp;
- anchoring time;
- observation time;
- signature information;
- verification metadata;
- integrity state;
- source-system reference;
- Anchor identifier;
- Anchor Version;
- publication information;
- lifecycle information;
- Corrections;
- later verification results.

The Integrity Reference is Anchor-owned.

The referenced artifact remains owned by its authoritative institution.

---

## Institutional Purpose

Anchor's purpose is to make integrity independently reviewable over time.

Conceptually:

```text
Authoritative Artifact
        ↓
Defined Canonical Representation
        ↓
Integrity Value Generated
        ↓
Integrity Reference Created
        ↓
Published / Preserved
        ↓
Later Integrity Verification
```

Anchor preserves the evidence needed to support that integrity evaluation.

It does not redefine the referenced record.

---

## Canonical Representation

Integrity is meaningful only when the representation being anchored is sufficiently defined.

Anchor therefore distinguishes between:

```text
the authoritative object
```

and:

```text
the exact artifact representation
used to generate the integrity value
```

Examples may include:

- a canonical JSON representation;
- a published HTML artifact;
- a Markdown source record;
- a Certification Package;
- a Registry Entry;
- a Chronicle Entry;
- a Trust Statement;
- another governed Suite artifact.

Anchor should not use vague or changing representation boundaries where the resulting integrity value could not later be reproduced or interpreted.

---

## Cryptographic Integrity

Anchor may preserve cryptographic integrity values such as:

- hashes;
- content digests;
- signatures;
- signature-verification material;
- tamper-evident commitments;
- future Bitcoin-based commitments;
- other governed cryptographic references.

The specific technology may evolve.

The institutional role remains stable.

---

## Temporal Integrity Context

Anchor may preserve temporal context such as:

- creation time;
- observation time;
- anchoring time;
- publication time;
- verification time;
- timestamp authority information where applicable.

Temporal context supports later interpretation of when an Integrity Reference was generated or verified.

---

## Verification Context

Anchor may preserve information required for later integrity verification.

Verification asks whether the referenced representation is consistent with the Integrity Reference.

It does **not** determine:

- whether the underlying claim is true;
- whether a certification is correct;
- whether a Registry Entry is authoritative;
- whether a Chronicle Entry is historically significant;
- whether a Trust Statement should be believed;
- whether an identity should be trusted.

Integrity verification remains narrower than substantive institutional judgment.

---

## What Anchor Owns

Anchor may own and govern:

- Integrity References;
- Anchor identifiers;
- Anchor-controlled metadata;
- integrity state;
- verification records;
- representation metadata;
- Anchor Versions;
- Corrections;
- publication state;
- lifecycle state;
- Anchor-specific procedures;
- Anchor-specific schemas;
- Anchor-specific Controlled Values;
- Anchor-specific governance.

These are Anchor-controlled institutional concepts.

---

## What Anchor References

Anchor may reference authoritative artifacts owned by:

- Satoshium Atlas;
- Satoshium Certifier;
- Satoshium Registry;
- Satoshium Chronicle;
- Satoshium Beacon;
- Satoshium Attestor;
- Satoshium Navigator;
- other authoritative systems.

A reference permits integrity context to be associated with an external artifact.

It does not transfer ownership or institutional authority.

> Reference does not transfer authority.

---

## What Anchor Does Not Do

Anchor does not:

- certify artifacts;
- replace Certifier determinations;
- catalog records on behalf of Registry;
- preserve historical Occurrences on behalf of Chronicle;
- issue Trust Statements on behalf of Attestor;
- determine reputation;
- establish identity infrastructure;
- issue credentials;
- authenticate users;
- determine the substantive truth of a referenced record;
- determine whether an institution should be trusted;
- reinterpret another institution's lifecycle or status.

Those functions remain with the institutions that own them.

---

## Relationship to Suite Standards

Anchor operates beneath the shared:

```text
Suite Standards
```

layer.

Suite Standards define common institutional expectations.

Anchor should not recreate a competing Suite-wide standards system.

Anchor-specific rules may implement or specialize Suite Standards where integrity-preservation operations require narrower institutional requirements.

---

## Relationship to Suite Methodology

Anchor operates beneath the shared:

```text
Suite Methodology
```

layer.

Suite Methodology establishes repeatable institutional approaches.

Anchor-specific procedures may define how an Integrity Reference is:

```text
identified
constructed
verified
published
maintained
corrected
versioned
preserved
```

without redefining the shared Suite methodological layer.

---

## Relationship to Suite Interoperability

Anchor participates in the Suite reference-first interoperability model.

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

Each institution retains authority over its own object.

Anchor may preserve integrity context for any of these objects without taking ownership of them.

---

## Institutional Boundary

Anchor's authority begins with:

```text
the Anchor Integrity Reference
```

and ends before:

```text
the substantive authority of the referenced artifact
```

For example:

```text
SC-CERT-2026-0001
```

remains authoritative because Satoshium Certifier issued and maintains the Certification Package.

An Anchor Integrity Reference associated with that package may preserve:

```text
what representation was anchored
which digest was generated
which algorithm was used
when the reference was created
how later verification may be performed
```

but Anchor does not become the certification authority.

The same rule applies across Registry, Chronicle, Atlas, Beacon, Attestor, Navigator, and future Suite systems.

---

## Implementation Neutrality

Anchor should remain institutionally stable even if its underlying implementation evolves.

Potential mechanisms may include:

- SHA-family hashes;
- alternative cryptographic digests;
- digital signatures;
- timestamping services;
- transparency logs;
- Merkle structures;
- Bitcoin commitments;
- future integrity technologies.

Anchor should define the institutional meaning of an Integrity Reference independently from one specific implementation.

---

## Purpose Principle

The governing Anchor purpose can be summarized as:

> Preserve durable integrity context without absorbing the authority of the referenced record.

---

## Status

Anchor's pre-Suite identity / claims / reputation / trust architecture is being reconciled with the current Satoshium Suite.

The current institutional direction is:

```text
Integrity Preservation
        ↓
Integrity Reference
        ↓
Cryptographic / Temporal Context
        ↓
Later Verification
```

rather than:

```text
Identity
→ Claim
→ Attestation
→ Reputation
→ Trust
```

This Purpose document establishes the constitutional baseline for the remaining Anchor reconciliation work.

---

**Status:** Foundation Reconciliation

**Version:** 1.0-draft

**Maintained By:** Satoshium
