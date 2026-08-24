# Attestations

## Overview

Within the current Satoshium Anchor architecture, **Attestations** no longer represents a general attestation or trust system.

Satoshium Attestor remains authoritative for:

```text
Trust Statements
```

and other Attestor-owned trust artifacts.

Anchor's role is narrower:

> Preserve the integrity of a defined attestation artifact or Trust Statement representation when that preservation has durable institutional value.

The governing distinction is:

```text
Attestation Meaning
≠
Attestation Artifact Integrity
```

---

## Purpose

The Attestations section defines how Anchor handles artifacts that contain or represent attestations.

Potential examples include:

- Trust Statements;
- signed endorsements;
- signed challenges;
- witness statements;
- institutional declarations;
- qualification statements;
- relationship assertions;
- support statements;
- dispute statements;
- externally governed attestation records.

Anchor does not evaluate what the attestation means.

Anchor preserves integrity context for the representation that was anchored.

---

# Attestation Artifact

An **Attestation Artifact** is a statement, endorsement, challenge, declaration, Trust Statement, or other governed representation containing an attestation.

An Attestation Artifact may become an Anchor candidate where:

- the artifact has durable institutional value;
- later verification is useful;
- the Source Institution is identifiable;
- the Canonical Representation can be defined;
- the Representation Boundary can be made reproducible.

---

# Attestation Source

The **Attestation Source** is the institution, system, signer, role, or other authority that produced or governs the attestation artifact.

Anchor may preserve:

- Source Institution;
- Source-System Identifier;
- signer reference;
- signing-key reference;
- issuing role;
- producing system;
- canonical Source location;
- temporal context.

Anchor should preserve only what is necessary for integrity review and accountability.

---

# Relationship to Attestor

Satoshium Attestor remains authoritative for:

- Trust Statements;
- trust judgments;
- Attestor identifiers;
- Attestor publication;
- Attestor lifecycle;
- Attestor Versions;
- Attestor Corrections;
- Attestor-controlled metadata.

Anchor may preserve an Integrity Reference for a defined Trust Statement representation.

Conceptually:

```text
Attestor
        ↓
Trust Statement
        ↓
Canonical Representation
        ↓
Anchor Integrity Reference
```

Anchor does not become the trust authority.

---

# Attestation Representation

Before anchoring, Anchor must define:

```text
Canonical Representation
Representation Boundary
```

The representation may be:

- canonical JSON;
- signed statement file;
- published human-readable artifact;
- structured trust record;
- another governed representation.

Anchor should not use vague representation language if later reproduction would be ambiguous.

---

# Attestation Integrity

Attestation Integrity asks:

> Does the reviewed attestation representation remain consistent with the representation governed by the Integrity Reference?

It does not ask:

> Is the attestation correct?

Therefore:

```text
Attestation Integrity
≠
Attestation Truth
```

and:

```text
Attestation Integrity
≠
Trustworthiness
```

---

# Attestation vs. Claim

A claim is an assertion.

An attestation may:

- support a claim;
- challenge a claim;
- witness a claim;
- qualify a claim;
- contextualize a claim;
- respond to a claim;
- make an independent assertion.

Anchor may preserve integrity for either artifact.

It does not adjudicate their relationship.

---

# Attestation vs. Evidence

An attestation may itself function as evidence.

It may also reference other evidence.

Anchor preserves the attestation artifact's integrity.

It does not determine evidentiary weight.

Therefore:

```text
Integrity Preservation
≠
Evidence Evaluation
```

---

# Attestation vs. Certification

Certifier may evaluate an attestation-related artifact under Suite Standards and Suite Methodology.

Anchor may preserve Integrity References for:

- the underlying attestation;
- resulting Certification Package;
- related certification artifacts.

Anchor does not become the certification authority.

---

# Attestation vs. Trust

A Trust Statement may contain an attestation-like judgment.

The trust judgment remains Attestor-owned.

Anchor may verify that the Trust Statement representation remains consistent with its Integrity Reference.

Anchor does not decide whether the statement should be believed.

---

# Attribution and Signatures

Attestation artifacts commonly require attribution.

Anchor may preserve:

- Source Institution;
- signer;
- signing role;
- signing key;
- certificate reference;
- producing system;
- issuance process.

The governing distinctions are:

```text
Signature
≠
Institutional Authority
```

and:

```text
Attribution
≠
Trust
```

---

# Attestation Artifact Lifecycle

An attestation artifact may later be:

- withdrawn;
- corrected;
- revoked;
- superseded;
- challenged;
- replaced;
- reissued;
- archived.

A later Source change does not erase the earlier Integrity Reference.

Conceptually:

```text
Earlier Attestation Representation
        ↓
Earlier Integrity Reference

Later Attestation Representation
        ↓
Later Anchor Version or New Integrity Reference
where required
```

The final Versioning rule remains unfrozen.

---

# Source Attestation Correction vs. Anchor Correction

A **Source Attestation Correction** changes the attestation under the authority of Attestor or another Source Institution.

An **Anchor Correction** changes Anchor's own record because Anchor recorded something incorrectly.

Potential Anchor errors include:

- wrong Source Artifact;
- wrong Source-System Identifier;
- wrong Canonical Representation;
- wrong Representation Boundary;
- wrong digest;
- wrong algorithm;
- wrong timestamp;
- wrong signer reference;
- wrong key reference;
- wrong verification metadata.

Therefore:

```text
Source Attestation Correction
≠
Anchor Correction
```

---

# Attestation Withdrawal

Withdrawal does not erase the historical existence of the earlier attestation representation.

Anchor should preserve:

```text
what was anchored
when it was anchored
which representation applied
which Source Institution governed it
whether the Source later withdrew or replaced it
```

where materially relevant.

Anchor should not silently rewrite the original Integrity Reference.

---

# Attestation Disputes

An attestation may be challenged or disputed.

A dispute does not automatically change the integrity state of the attestation representation.

Anchor may preserve integrity for:

- original attestation;
- challenge artifact;
- response artifact;
- later institutional finding;
- superseding Trust Statement.

Anchor does not adjudicate the dispute.

---

# What Anchor Preserves

For an attestation-related Integrity Reference, Anchor may preserve:

- Anchor Identifier;
- Source Institution;
- Source-System Identifier;
- Attestation Artifact Type;
- Canonical Representation;
- Representation Boundary;
- Integrity Method;
- Integrity Value;
- algorithm metadata;
- timestamps;
- signer information;
- key information;
- Verification Material;
- Anchor Version;
- Integrity State;
- Publication State;
- Lifecycle State;
- Correction lineage;
- verification history.

The final schema remains unfrozen.

---

# What Anchor Does Not Do

Anchor does not:

- issue attestations;
- issue Trust Statements;
- determine endorsement strength;
- score credibility;
- determine evidentiary weight;
- resolve disputes;
- assign reputation;
- determine trustworthiness;
- govern Attestor publication;
- govern Attestor lifecycle;
- replace Attestor authority.

---

# Relationship to Claims

The `/anchor/claims/` section now concerns claim artifact integrity.

Claims and attestations may reference one another, but Anchor should not create a new claim-attestation authority model.

The preferred architecture is:

```text
Externally Governed Claim Artifact
        ↓
optional Anchor Integrity Reference

Externally Governed Attestation Artifact
        ↓
optional Anchor Integrity Reference
```

Their meanings remain externally governed.

---

# Relationship to Suite Institutions

The current relationship is:

```text
Claims
→ may provide assertions

Certifier
→ may evaluate artifacts or evidence

Registry
→ may catalog authoritative records

Chronicle
→ may preserve qualifying historical Occurrences

Attestor
→ owns Trust Statements

Anchor
→ may preserve Integrity References
```

Each institution retains authority over its own canonical object.

> Reference does not transfer authority.

---

# Relationship to Anchor Identities

Attestation artifacts may use `/anchor/identities/` attribution concepts such as:

- Source Institution;
- signer;
- signing key;
- producing system;
- reviewer;
- institutional role.

These remain supporting metadata.

Anchor does not establish a general identity framework.

---

# Attestations Principle

The governing principle is:

> Preserve the attestation artifact's integrity. Do not become the attestation authority.

Anchor should preserve attestation-related integrity where it provides durable value and stop before trust judgment, evidentiary evaluation, certification, or dispute resolution.

---

## Status

**Foundation Reconciliation**

This document replaces the pre-Suite model in which attestations were treated as a foundational Anchor trust layer.

The current model treats attestations as **externally governed artifacts that may become subjects of Anchor integrity preservation**.

The following remain intentionally unfrozen:

```text
Attestation Artifact Type Controlled Values
Trust Statement anchoring requirements
signer-reference requirements
signature policy
attestation-withdrawal handling
attestation-dispute reference patterns
new Anchor Version vs. new Integrity Reference rule
attestation-specific schema conditions
first production attestation-related Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
