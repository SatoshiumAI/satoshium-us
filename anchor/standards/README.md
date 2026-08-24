# Standards

## Overview

**Anchor Standards** define the institution-specific requirements governing integrity preservation within **Satoshium Anchor**.

Anchor does not maintain an independent Suite-wide standards system.

Shared institutional expectations remain governed by:

```text
Satoshium Suite Standards
```

Anchor Standards exist only to specialize those shared expectations where integrity-preservation operations require narrower or more explicit requirements.

The governing relationship is:

```text
Suite Standards
        ↓
Anchor-Specific Integrity Requirements
        ↓
Integrity Reference Production
```

---

## Standards Purpose

Anchor Standards exist to ensure that Integrity References are:

- consistently structured;
- reproducible where technically possible;
- independently reviewable;
- properly attributed to Source Institutions;
- explicit about Canonical Representation;
- explicit about Representation Boundary;
- supported by governed integrity material;
- temporally interpretable;
- verifiable;
- interoperable;
- versionable;
- correctable;
- preservable over time.

Anchor Standards define expectations.

They do not by themselves define the complete operational procedure.

---

# Standards Hierarchy

The current institutional hierarchy is:

```text
Suite Standards
        ↓
Anchor Standards / Anchor-Specific Requirements
        ↓
Anchor Rules / Policies where needed
        ↓
Anchor Procedures
        ↓
Schemas / Controlled Values
        ↓
Production Integrity Reference
```

Not every layer must exist as a separate public page.

Structure should be created only where it provides durable institutional value.

---

# Relationship to Suite Standards

Suite Standards remain the shared expectations layer for the entire Satoshium Suite.

Anchor should inherit Suite-wide requirements relating to:

- terminology;
- governance;
- schemas;
- interoperability;
- versioning;
- evidence;
- trust boundaries;
- publication consistency;
- institutional separation;
- other shared architectural expectations.

Anchor must not redefine a Suite-wide concept merely because integrity preservation uses it.

Where Anchor needs additional precision, Anchor may establish narrower requirements.

---

# Relationship to Suite Methodology

The distinction is:

```text
Standards
→ define expectations

Methodology
→ defines implementation principles

Procedures
→ define repeatable operational steps
```

For example:

```text
Anchor Standard:
Canonical Representation must be sufficiently defined
for later integrity review.

Anchor Methodological Principle:
Prefer reproducible, explicit representation boundaries.

Anchoring Procedure:
Identify artifact → define representation → define boundary
→ generate Integrity Value → construct Integrity Reference.
```

These layers should remain conceptually distinct.

---

# Relationship to Suite Interoperability

Anchor Standards operate within the current Suite object model:

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

Anchor Standards must preserve the independent authority of each institution.

> Reference does not transfer authority.

---

# Core Anchor Standards Areas

## Integrity Reference Requirements

Anchor Standards should define the minimum institutional requirements for a valid:

```text
Integrity Reference
```

Potential required domains include:

- Anchor identity;
- Source Institution;
- Source-System Identifier;
- artifact type;
- Canonical Representation;
- Representation Boundary;
- Integrity Method;
- Integrity Value;
- algorithm metadata;
- Temporal Context;
- Verification Material;
- Anchor Version;
- required state information;
- Correction or lineage references where applicable.

The final production field set remains subject to schema development and testing.

---

## Canonical Representation Requirements

Anchor must define what representation is actually being anchored.

A valid Integrity Reference should not rely on vague language such as:

```text
this page
this record
this package
this system
```

when later reproduction would be ambiguous.

Canonical Representation requirements should answer:

```text
What exact representation was processed?
How was it obtained?
Was canonicalization required?
Can a later reviewer reproduce or identify it?
```

---

## Representation Boundary Requirements

Anchor should define what is included and excluded from the integrity relationship.

Examples may include distinguishing:

```text
canonical record content
from
navigation / footer / dynamic site chrome
```

or:

```text
one artifact
from
the entire package directory
```

or:

```text
canonical JSON
from
a generated human-readable view
```

The boundary must support meaningful later verification.

---

## Cryptographic Requirements

Anchor Standards should eventually define requirements for:

- approved digest algorithms;
- algorithm identification;
- digest encoding;
- canonicalization;
- digital signatures;
- signature verification;
- key references;
- timestamping;
- external commitments;
- algorithm deprecation;
- migration to successor cryptographic methods.

The final algorithm policy remains unfrozen.

---

## Temporal Requirements

Different time concepts should remain distinct.

Potential Anchor timestamps include:

```text
observed_at
integrity_generated_at
anchored_at
published_at
verified_at
```

The exact field names remain subject to schema design.

The governing rule is that timestamps with materially different meanings should not be collapsed into one generic date.

---

## Verification Requirements

Anchor Standards should eventually define the minimum requirements for Integrity Verification.

Potential requirements include:

- correct Source Artifact identification;
- correct Canonical Representation;
- correct algorithm;
- reproducible Integrity Value;
- valid signature where applicable;
- valid external commitment where applicable;
- preserved Verification Material;
- authority-boundary consistency;
- human / machine consistency.

Verification must remain narrower than certification or trust judgment.

---

## Authority Boundary Requirements

Anchor Standards must distinguish:

```text
Source Institution
≠
Anchor

Source-System Identifier
≠
Anchor Identifier

Source Artifact Version
≠
Anchor Version

Source Status
≠
Anchor Integrity State
≠
Anchor Publication State
≠
Anchor Lifecycle State
```

Anchor should never represent external institutional state as though it were Anchor-owned state.

---

## Interoperability Requirements

Anchor should use references to authoritative external objects rather than duplicating them.

Potential integration requirements include:

- stable Source-System reference;
- canonical URL or repository reference where appropriate;
- Source Institution;
- artifact type;
- reciprocal reference where useful;
- preserved authority boundary;
- no invented external identifier;
- no transfer of Source status or lifecycle.

---

## Versioning Requirements

Anchor Standards should preserve the distinction between:

```text
Source Artifact Version
Anchor Version
Schema Version
Algorithm Version
Signature Method Version
```

A later Source Artifact change does not automatically invalidate an earlier Integrity Reference.

Earlier integrity state should remain reconstructable.

---

## Correction Requirements

Anchor corrects Anchor-owned records.

A Correction may be required when Anchor recorded:

- the wrong Source Artifact;
- the wrong digest;
- the wrong algorithm;
- the wrong timestamp;
- the wrong representation boundary;
- incorrect verification metadata;
- another materially incorrect Anchor-owned field.

Anchor Correction does not rewrite the external Source Artifact.

---

## Publication Consistency Requirements

Where Anchor later publishes both human-readable and machine-readable representations of the same Integrity Reference, they should agree on material fields such as:

- identifier;
- Source Institution;
- Source-System Identifier;
- artifact type;
- Anchor Version;
- Integrity Method;
- Integrity Value;
- algorithm;
- timestamps;
- Integrity State;
- Publication State;
- Lifecycle State;
- Correction lineage.

The exact production requirements remain to be formalized.

---

# Core Standards Principles

The current Anchor Standards principles are:

### Define the Representation First

Do not generate integrity material until the artifact and representation boundary are defined.

### Preserve Reproducibility

Preserve enough information that later reviewers can understand or reproduce the integrity relationship where technically possible.

### Preserve Authority Boundaries

> Reference does not transfer authority.

### Preserve State Separation

Integrity, Verification, Publication, Lifecycle, and external Source status remain distinct.

### Preserve Version Separation

Anchor Version is not Source Artifact Version.

### Preserve Material History

Material prior states should remain reconstructable.

### Prefer Minimum Necessary Structure

Do not create records, identifiers, schemas, or integrity artifacts solely for architectural symmetry.

### Remain Technology-Neutral

Institutional meaning should survive changes in cryptographic implementation.

---

# Technology Neutrality

Anchor Standards should not define Anchor around:

- one hash algorithm;
- one signature system;
- one timestamp provider;
- one blockchain;
- one distributed ledger;
- one Bitcoin commitment method.

Possible technologies may include:

```text
SHA-family hashing
digital signatures
trusted timestamping
transparency logs
Merkle structures
distributed commitments
Bitcoin commitments
future cryptographic systems
```

The technology may change.

The integrity-preservation requirement remains.

---

# Reproducibility

A high-quality Integrity Reference should preserve enough context to answer:

```text
What was anchored?
Which representation?
Which boundary?
Which method?
Which algorithm?
Which value?
When?
How can it be checked later?
```

Without that context, a stored hash alone may have limited institutional value.

---

# Minimum Necessary Structure

Anchor should resist creating separate objects merely because the Suite contains comparable structures elsewhere.

For example, Anchor should not automatically create:

```text
separate signature object
separate timestamp object
separate verification object
separate commitment object
```

unless production shows those structures provide durable independent value.

The default should remain:

> Use structure when structure adds durable institutional value.

---

# Forward Compatibility

Anchor Standards should permit controlled evolution.

Later architecture may need to support:

- algorithm deprecation;
- stronger successor algorithms;
- changed canonicalization;
- new signature systems;
- new timestamp methods;
- Bitcoin commitment adoption;
- schema upgrades;
- additional verification methods.

Evolution should preserve prior interpretation and lineage.

---

# What Anchor Standards Do Not Govern

Anchor Standards do not govern:

- identity infrastructure;
- claims;
- reputation;
- trust scoring;
- certification decisions;
- Registry classification;
- Chronicle Preservation Eligibility;
- Chronicle historical interpretation;
- Beacon discovery significance;
- Attestor Trust Statement meaning;
- Navigator workflow authority.

These concepts belong outside Anchor's institutional authority.

---

# Anchor-Specific Standards Still to Be Formalized

The following remain intentionally unfrozen:

```text
Anchor Identifier Specification
Integrity Method Controlled Values
approved digest algorithm policy
signature policy
timestamp policy
Canonical Representation rules
Representation Boundary rules
Integrity Reference schema
Verification Result vocabulary
Integrity State vocabulary
Publication State vocabulary
Lifecycle State vocabulary
Versioning rules
Correction rules
Validation requirements
Publication requirements
Bitcoin commitment policy
```

These should be formalized only after the foundation and production architecture provide sufficient operational evidence.

---

# Standards Philosophy

The governing philosophy is:

> Shared standards above. Integrity-specific requirements below. Authority preserved throughout.

Anchor Standards should make integrity preservation precise enough to be reproducible and interoperable while remaining narrow enough to avoid redefining the authority of the records Anchor protects.

---

## Status

**Foundation Reconciliation**

This document replaces the earlier pre-Suite identity / claims / attestations / reputation / trust standards model with the current Anchor integrity-preservation standards position.

**Version:** 1.0-draft

**Maintained By:** Satoshium
