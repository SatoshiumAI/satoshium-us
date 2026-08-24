# Definitions

## Overview

This document defines the core terminology used by **Satoshium Anchor**.

Anchor is the Satoshium Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Definitions exist to preserve consistent meaning across:

- Anchor documentation;
- Integrity References;
- schemas;
- procedures;
- anchoring;
- verification;
- publication;
- lifecycle;
- Corrections;
- Versions;
- maintenance;
- Suite interoperability.

The governing principle is:

> Reference does not transfer authority.

---

# Definition Principle

Anchor terminology should describe integrity precisely without absorbing the authority, meaning, certification, historical interpretation, identity, reputation, or trust conclusions of the referenced artifact.

---

# Core Definitions

## Authoritative Artifact

A record, file, package, publication, statement, dataset, or other governed object whose substantive authority remains with the institution or system that created and maintains it.

Examples may include:

```text
Atlas jurisdiction record
Certification Package
Satoshium Registry Entry
Chronicle Entry
Trust Statement
Workflow Definition
```

Anchor may preserve an Integrity Reference for an Authoritative Artifact.

Anchor does not become authoritative for the artifact merely by referencing it.

---

## Source Institution

The institution or system that owns or maintains the Authoritative Artifact referenced by Anchor.

Examples may include:

```text
Satoshium Atlas
Satoshium Certifier
Satoshium Registry
Satoshium Chronicle
Satoshium Beacon
Satoshium Attestor
Satoshium Navigator
```

The Source Institution retains substantive authority.

---

## Canonical Representation

The exact governed representation of an artifact used to generate or verify an integrity value.

The Canonical Representation defines what is actually being anchored.

It may identify:

```text
specific bytes
canonical JSON
published HTML
Markdown source
serialized record
defined package artifact
other governed representation
```

A vague reference to a changing system is not sufficient where later integrity reproduction would be impossible.

---

## Representation Boundary

The explicit scope identifying which artifact representation is covered by an Integrity Reference.

The Representation Boundary also helps identify what is not covered.

Examples may include distinguishing:

```text
record content
from
navigation / shared footer / presentation shell
```

or:

```text
canonical machine-readable record
from
generated display representation
```

The exact rules should be established through later Anchor schema and process architecture.

---

## Integrity Reference

The **canonical operational object of Satoshium Anchor**.

An Integrity Reference preserves governed integrity information associated with a defined artifact representation.

It may contain or reference information such as:

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

The Integrity Reference is Anchor-owned.

The referenced artifact remains owned by its Source Institution.

---

## Integrity Value

A machine-generated value derived from a defined artifact representation and used to support later integrity comparison or verification.

A cryptographic digest is one common form of Integrity Value.

Integrity Value is the broader institutional concept.

---

## Cryptographic Digest

A deterministic fixed-length value produced by applying a cryptographic hash function to a defined representation.

A digest supports later comparison between:

```text
the anchored representation
```

and:

```text
a reviewed representation
```

A matching digest supports integrity consistency.

It does not establish substantive truth.

---

## Hash Algorithm

The cryptographic function used to generate a digest.

The algorithm should be identified sufficiently to permit later reproduction and verification.

Examples may eventually include:

```text
SHA-256
other approved algorithms
```

Final algorithm policy is not frozen by this Definitions document.

---

## Timestamp

A recorded date and time associated with an Anchor action or referenced condition.

Examples may include:

- artifact observation time;
- integrity generation time;
- anchoring time;
- publication time;
- verification time.

A timestamp records temporal context.

It does not automatically prove external-world occurrence unless supported by the applicable timestamping method.

---

## Temporal Context

The set of governed time-related facts needed to interpret when an Integrity Reference, artifact representation, or verification action existed or occurred.

Temporal Context may include multiple timestamps with distinct meanings.

Those meanings should not be collapsed into one generic date.

---

## Signature

Cryptographic signature material associated with a defined artifact representation or Integrity Reference.

A signature may support:

```text
integrity verification
origin verification
key-based accountability
```

depending on the governing implementation.

A signature does not itself transfer institutional authority.

---

## Verification Material

Cryptographic, procedural, or descriptive information needed to reproduce, compare, or validate an Integrity Reference.

Verification Material may include:

- digest algorithm;
- digest value;
- signature;
- public-key reference;
- canonicalization instructions;
- representation metadata;
- timestamp information;
- external commitment reference;
- other governed verification context.

---

## Anchoring

The governed Anchor process of creating or recording an Integrity Reference for a defined artifact representation.

Conceptually:

```text
Authoritative Artifact
        ↓
Canonical Representation
        ↓
Integrity Value
        ↓
Integrity Reference
```

Anchoring does not change the substantive authority of the referenced artifact.

---

## Integrity Verification

The process of determining whether a reviewed artifact representation is consistent with the Integrity Reference governing that representation.

Conceptually:

```text
Reviewed Artifact Representation
        ↓
Reproduce Integrity Value
        ↓
Compare with Integrity Reference
        ↓
Verification Result
```

Integrity Verification is narrower than certification, truth determination, historical verification, or trust evaluation.

---

## Verification Result

The recorded outcome of an Anchor Integrity Verification action.

A Verification Result describes integrity comparison.

It does not determine:

- certification correctness;
- historical significance;
- reputation;
- trustworthiness;
- substantive truth.

Final Verification Result Controlled Values remain unfrozen until operational design.

---

## Integrity State

An Anchor-controlled state describing the current integrity condition of an Integrity Reference or its relationship to the artifact representation it covers.

Integrity State is a candidate production state system.

Final values should be established only after operational review.

Integrity State remains distinct from:

```text
Verification Result
Publication State
Lifecycle State
Source-System Status
```

---

## Anchor Identifier

A stable identifier assigned by Anchor to an Anchor-owned Integrity Reference.

The final production identifier format is not yet established.

The identifier architecture should later define:

```text
format
assignment
sequence behavior
year behavior
reuse prohibition
Version relationship
human / machine use
```

---

## Anchor Version

The preserved Version of an Anchor-owned Integrity Reference or Anchor representation.

Anchor Version remains distinct from:

```text
Source Artifact Version
Schema Version
Algorithm Version
Signature Method Version
```

A Source Institution may update its own artifact without automatically changing Anchor's historical Version lineage.

---

## Source-System Identifier

An identifier assigned by the external authoritative institution to the artifact referenced by Anchor.

Examples include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
```

The Source-System Identifier remains controlled by the Source Institution.

Anchor must not replace it with an Anchor identifier.

---

## Publication State

An Anchor-controlled state describing whether an Integrity Reference has entered, remains in, or has been withdrawn from public production.

Final Publication State Controlled Values should be established through later Anchor Publication architecture.

Publication State remains distinct from Lifecycle State and Verification Result.

---

## Lifecycle State

An Anchor-controlled state describing the institutional condition of an Integrity Reference over time.

Lifecycle State may eventually govern conditions such as:

```text
draft
active
superseded
withdrawn
preserved
```

but no final Anchor lifecycle vocabulary is frozen here.

Lifecycle State remains distinct from:

- Integrity State;
- Verification Result;
- Publication State;
- Source-System lifecycle or status.

---

## Correction

A governed change made to Anchor's own record because Anchor's prior representation, metadata, integrity context, or procedural record was incorrect or materially incomplete.

A Correction applies to Anchor.

It does not rewrite the authoritative Source Artifact.

A later change made by the Source Institution is not automatically an Anchor Correction.

---

## Maintenance

Post-publication review and upkeep of Anchor-owned records and integrity infrastructure.

Maintenance may include:

- broken reference review;
- representation consistency;
- algorithm compatibility;
- signature verification support;
- timestamp reference continuity;
- publication review;
- Corrections;
- Versions;
- lifecycle review;
- preservation.

Maintenance should not silently rewrite prior integrity states.

---

## Integrity Preservation

Anchor's continuing institutional function of preserving durable integrity context so a later reviewer can understand and verify the relationship between an Integrity Reference and the artifact representation it covers.

Integrity Preservation may include long-term retention of:

- Anchor identifiers;
- Integrity Values;
- algorithms;
- representation metadata;
- timestamps;
- signatures;
- Versions;
- Corrections;
- verification history;
- publication history;
- external commitment references.

---

# Critical Distinctions

Anchor depends on several permanent conceptual separations.

```text
Authoritative Artifact
≠
Integrity Reference
```

The external artifact is owned by its authoritative institution.

The Integrity Reference is owned by Anchor.

---

```text
Source-System Identifier
≠
Anchor Identifier
```

Each identifies a different institutional object.

---

```text
Artifact Version
≠
Anchor Version
```

A change to the Source Artifact and a change to Anchor's record are separate institutional events.

---

```text
Integrity Verification
≠
Certification
```

Anchor verifies integrity.

Certifier performs certification.

---

```text
Integrity Verification
≠
Chronicle Verification
```

Anchor asks whether a representation matches its Integrity Reference.

Chronicle asks whether Chronicle's historical representation is sound.

---

```text
Integrity State
≠
Publication State
≠
Lifecycle State
```

These state systems describe different institutional conditions.

---

```text
Signature
≠
Institutional Authority
```

A cryptographic signature may support verification.

It does not automatically establish institutional ownership or substantive authority.

---

```text
Integrity
≠
Truth
≠
Trust
```

A record can have intact integrity and still contain incorrect information.

A record can be cryptographically authentic without being trustworthy.

Anchor's function remains integrity preservation.

---

# Integrity vs. Truth

Integrity asks:

> Does this reviewed representation correspond to the representation governed by the Integrity Reference?

Truth asks a different substantive question.

Anchor does not determine truth merely by confirming integrity.

---

# Integrity vs. Certification

Anchor preserves and verifies integrity context.

Satoshium Certifier performs certification under Suite Standards and Suite Methodology.

An Integrity Reference may support certification review.

It does not replace the Certification Package or Certifier authority.

---

# Integrity vs. History

Anchor preserves integrity context.

Satoshium Chronicle preserves qualifying historical Occurrences through canonical Chronicle Entries.

An Integrity Reference may preserve the integrity of a Chronicle Entry.

It does not become the historical record.

---

# Integrity vs. Trust

Anchor may provide integrity evidence useful to trust evaluation.

Satoshium Attestor owns Trust Statements.

Anchor does not determine:

```text
reputation
trustworthiness
institutional trust
identity credibility
```

---

# Suite Object Context

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

> Reference does not transfer authority.

---

# Unfrozen Terms

This Definitions document intentionally does **not** yet freeze final vocabularies for:

```text
Integrity State values
Verification Result values
Publication State values
Lifecycle State values
Anchor identifier format
anchoring method categories
algorithm policy
signature policy
Bitcoin commitment method
maintenance cadence
```

These should be established only after Anchor's:

```text
Purpose
Definitions
Integrity Preservation
Anchoring Process
Integration
Standards
Governance
Identifier architecture
Schema architecture
Validation
Publication
Production Procedure
First production Integrity Reference
```

have been sufficiently designed and tested.

---

# Definitions Principle

The governing Definitions principle is:

> Define integrity precisely. Preserve authority boundaries. Freeze vocabulary only when production requires it.

---

## Status

**Foundation Reconciliation**

This Definitions document establishes the current canonical terminology baseline for Anchor's post-Suite architectural reconciliation.

**Version:** 1.0-draft

**Maintained By:** Satoshium
