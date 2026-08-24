# Claims

## Overview

Within the current Satoshium Anchor architecture, **Claims** no longer represents a general claims system.

Anchor does not own claims as a universal canonical object.

Anchor's role is narrower:

> Preserve the integrity of a defined claim artifact or claim representation when that preservation has durable institutional value.

A claim may be created, evaluated, certified, registered, preserved historically, challenged, or trusted by another institution or process.

Anchor preserves only the integrity context associated with the representation it anchors.

The governing distinction is:

```text
Claim Meaning
≠
Claim Artifact Integrity
```

---

## Purpose

The Claims section exists to define how Anchor handles claim-related artifacts.

Anchor may need to preserve integrity for:

- a statement;
- a declaration;
- an assertion;
- a signed claim;
- a certification subject statement;
- a published claim record;
- a Trust Statement containing claim-like content;
- another governed assertion artifact.

The purpose is not to evaluate the claim.

The purpose is to preserve enough integrity context that the artifact can later be checked against the representation that was anchored.

---

# Claim Artifact

A **Claim Artifact** is a statement, declaration, assertion, record, or governed representation containing a claim.

Examples may include:

```text
signed statement
ownership declaration
authorship declaration
institutional assertion
certification subject statement
published claim record
credential-like statement
system-generated assertion
```

A Claim Artifact may become an Anchor candidate where its long-term integrity has institutional value.

---

# Claim Source

The **Claim Source** is the person, institution, system, process, or other authority that produced or governs the claim artifact.

Anchor should preserve enough Source information to answer:

```text
Who or what produced this claim artifact?
Which institution governs it?
Does it have a Source-System Identifier?
Which authoritative representation applies?
```

Anchor should prefer stable external references over duplicating the Source's identity or governance record.

---

# Claim Representation

Before anchoring a claim artifact, Anchor must define:

```text
Canonical Representation
Representation Boundary
```

This prevents ambiguity about what statement was actually anchored.

For example, Anchor may need to distinguish:

```text
the signed statement body
```

from:

```text
webpage navigation
site footer
dynamic interface elements
later comments
derived presentation
```

A later reviewer should be able to identify the exact representation covered by the Integrity Reference.

---

# Claim Integrity

Claim Integrity asks:

> Does the reviewed claim representation remain consistent with the representation governed by the Integrity Reference?

It does not ask:

> Is the claim true?

Therefore:

```text
Claim Integrity
≠
Claim Truth
```

A false claim can retain perfect integrity.

A true claim can be altered after publication.

Anchor preserves the representation relationship.

---

# Claim vs. Evidence

A claim is an assertion.

Evidence may support, challenge, qualify, or contextualize the claim.

Anchor may preserve Integrity References for:

```text
claim artifact
evidence artifact
both
```

where justified.

Anchor does not decide the evidentiary relationship merely by preserving integrity.

---

# Claim vs. Certification

Certifier may evaluate a claim or related artifact under Suite Standards and Suite Methodology.

A certification may produce:

```text
Certification Package
SCPR
SCR
SCRD
```

Anchor may preserve Integrity References for those outputs or for the underlying claim artifact.

Anchor does not become the certification authority.

---

# Claim vs. Registry

Registry may catalog an authoritative record that contains or relates to a claim.

The Registry Entry remains Registry-owned.

Anchor may preserve integrity context for the Registry representation.

Anchor does not create claim registration merely by anchoring the record.

---

# Claim vs. Chronicle

A claim may become historically significant.

Chronicle may preserve a qualifying historical Occurrence involving that claim through a canonical Chronicle Entry.

Anchor may preserve integrity for:

- the original Claim Artifact;
- a related authoritative record;
- the Chronicle Entry representation.

Anchor does not decide Preservation Eligibility or historical significance.

---

# Claim vs. Trust

Attestor may issue a Trust Statement concerning:

- a claim;
- a source;
- an artifact;
- an institution;
- another trust subject.

Anchor may preserve the integrity of the Trust Statement or claim representation.

Anchor does not determine whether the claim should be trusted.

---

# Claim Attribution

Claim integrity may require attribution.

Potential attribution may include:

- Source Institution;
- author;
- signer;
- signing key;
- producing system;
- repository;
- publication process;
- issuing role.

Anchor should preserve only attribution necessary for:

- accountability;
- verification;
- provenance of the integrity relationship;
- historical reconstruction.

The governing privacy principle remains:

> Preserve necessary attribution. Avoid unnecessary identity accumulation.

---

# Claim Artifact Lifecycle

A Claim Artifact may later be:

- revised;
- corrected;
- withdrawn;
- superseded;
- challenged;
- rejected;
- certified;
- registered;
- archived;
- historically preserved.

A later Source change does not erase the earlier Integrity Reference.

Conceptually:

```text
Earlier Claim Representation
        ↓
Earlier Integrity Reference

Later Claim Representation
        ↓
Later Anchor Version or New Integrity Reference
where required
```

The final Versioning rule remains unfrozen.

---

# Source Claim Correction vs. Anchor Correction

A **Source Claim Correction** changes the claim artifact or its meaning under the authority of the Source Institution.

An **Anchor Correction** changes Anchor's own record because Anchor recorded something incorrectly.

Examples of Anchor error may include:

- wrong Source Artifact;
- wrong Source-System Identifier;
- wrong Canonical Representation;
- wrong Representation Boundary;
- wrong digest;
- wrong algorithm;
- wrong timestamp;
- wrong signer reference;
- wrong verification metadata.

Therefore:

```text
Source Claim Correction
≠
Anchor Correction
```

---

# Claim Withdrawal

A claim may later be withdrawn by its Source.

Withdrawal does not erase the historical existence of the earlier anchored representation.

Anchor should preserve:

```text
what was anchored
when it was anchored
which representation applied
whether the Source later withdrew or replaced it
```

where that external status is materially relevant.

Anchor should not silently rewrite the original Integrity Reference.

---

# Claim Disputes

Claims may be disputed.

A dispute does not automatically change the integrity state of the anchored claim representation.

Anchor may preserve integrity context for:

- the original claim;
- a challenge or rebuttal artifact;
- later institutional findings;
- a Correction or superseding Source Artifact.

Anchor does not adjudicate the dispute.

---

# What Anchor Preserves

For a claim-related Integrity Reference, Anchor may preserve:

- Anchor Identifier;
- Source Institution;
- Source-System Identifier;
- Claim Artifact Type;
- Canonical Representation;
- Representation Boundary;
- Integrity Method;
- Integrity Value;
- algorithm metadata;
- timestamps;
- signature information;
- Verification Material;
- Anchor Version;
- Integrity State;
- Publication State;
- Lifecycle State;
- Correction lineage;
- later verification history.

The final schema remains unfrozen.

---

# What Anchor Does Not Do

Anchor does not:

- create a general claims registry;
- define universal claim semantics;
- determine whether a claim is true;
- determine whether a claim is false;
- score claim credibility;
- adjudicate claim disputes;
- certify claims;
- determine whether a claim should be accepted;
- build reputation from claims;
- issue trust conclusions;
- replace Source Institution authority.

These functions remain outside Anchor's institutional role.

---

# Relationship to Suite Institutions

The current Suite relationship is:

```text
Certifier
→ may evaluate claim-related artifacts

Registry
→ may catalog authoritative records

Chronicle
→ may preserve qualifying historical Occurrences

Attestor
→ may issue Trust Statements

Anchor
→ may preserve Integrity References for relevant artifacts
```

Each institution remains authoritative for its own canonical object.

> Reference does not transfer authority.

---

# Relationship to Anchor Identities

The `/anchor/identities/` section now concerns **Identity and Attribution References**.

Claim-related Integrity References may use that architecture to preserve:

- Source Institution;
- signer;
- signing key;
- producing system;
- reviewer;
- process attribution.

This supports integrity review without turning Claims or Identities into separate Anchor authority systems.

---

# Relationship to Anchor Integration

Anchor Integration defines how claim-related artifacts may be referenced from external Source Institutions.

The preferred model is:

```text
Source Institution
        ↓
Authoritative Claim Artifact
        ↓
Canonical Representation
        ↓
Anchor Integrity Reference
```

---

# Claims Principle

The governing principle is:

> Preserve the claim artifact's integrity. Do not become the claim authority.

Anchor should preserve claim-related integrity where it adds durable institutional value and stop before claim evaluation, certification, history, or trust judgment.

---

## Status

**Foundation Reconciliation**

This document replaces the pre-Suite model in which claims were treated as a foundational Anchor institutional layer.

The current model treats claims as **externally governed artifacts that may become subjects of Anchor integrity preservation**.

The following remain intentionally unfrozen:

```text
Claim Artifact Type Controlled Values
claim-source requirements
claim representation rules
claim-withdrawal handling
claim-dispute reference patterns
new Anchor Version vs. new Integrity Reference rule
claim-specific schema conditions
first production claim-related Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
