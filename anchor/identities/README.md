# Identities

## Overview

Within the current Satoshium Anchor architecture, **Identities** no longer defines a general-purpose identity system.

Anchor's institutional purpose is integrity preservation.

Identity information is relevant only where it supports:

- source attribution;
- signer attribution;
- key attribution;
- producing-system attribution;
- reviewer attribution;
- process accountability;
- later integrity verification.

The page is therefore retained for continuity at:

```text
/anchor/identities/
```

but its institutional meaning is now:

```text
Identity and Attribution References
```

rather than:

```text
Identity Infrastructure
```

The governing principle is:

> Attribute the integrity action. Do not absorb the identity authority.

---

## Identity Boundary

Anchor may reference an identity.

Anchor does not become the authoritative identity provider merely because it preserves the reference.

```text
Identity Reference
≠
Identity Authority
```

The broader Suite principle remains:

> Reference does not transfer authority.

---

# Purpose

Identity and attribution information helps Anchor answer questions such as:

```text
Who owns the Source Artifact?
Which system generated the Integrity Value?
Which signer or key produced a signature?
Which process performed Verification?
Which role approved a material Anchor action?
```

These questions support accountability and reproducibility.

They do not transform Anchor into an identity institution.

---

# Source Institution

The **Source Institution** is the institution or system that owns or maintains the Authoritative Artifact referenced by Anchor.

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

The Source Institution is a foundational attribution element because it preserves who owns the referenced artifact.

Anchor does not replace that authority.

---

# Producing System

A **Producing System** is the technical system, service, workflow, application, or process that generated an Anchor integrity artifact or integrity value.

Examples may include:

- hashing service;
- signature service;
- Anchor production workflow;
- automated publication process;
- external timestamping service;
- Bitcoin commitment process;
- future integrity service.

Producing System attribution may be useful where later review requires understanding how integrity material was created.

---

# Signer Reference

Where digital signatures are used, Anchor may preserve a reference identifying:

```text
signer
signing system
signing role
signing authority
```

as appropriate to the implementation.

The signer reference supports attribution.

It does not by itself establish substantive institutional authority.

---

# Key Reference

A **Key Reference** identifies cryptographic key information needed to interpret or verify a signature.

Potential information may include:

- key identifier;
- certificate identifier;
- public-key reference;
- fingerprint;
- algorithm;
- validity period;
- revocation reference;
- external key registry reference.

Final production requirements remain unfrozen.

A key reference supports cryptographic verification.

It does not establish truth or trustworthiness.

---

# Reviewer Attribution

Anchor may preserve reviewer attribution where institutional review requires it.

Potential contexts include:

- Integrity Verification;
- Validation where later adopted;
- Publication approval;
- Anchor Correction;
- Anchor Version review;
- governance decision;
- Maintenance review.

Attribution may identify:

```text
person
institutional role
automated process
system
review function
```

depending on what is sufficient for accountability.

---

# Role-Based Attribution

Anchor should prefer role-based or institutional attribution where it provides sufficient accountability.

Examples may include:

```text
Anchor Reviewer
Anchor Publication Process
Certifier Source Institution
Automated Integrity Generation Process
```

A personal identity should not be required merely because a human participated.

The purpose is accountable integrity preservation, not personal identity accumulation.

---

# External Identity Reference

Where identity information is governed by another authoritative system, Anchor should reference that external identity rather than reproduce it.

Potential external identity references may include:

- institutional identifier;
- certificate subject;
- public-key identifier;
- account identifier;
- repository identity;
- externally governed credential reference.

Anchor should preserve only the information needed to understand the integrity relationship.

---

# Attribution Model

The current model is:

```text
Source Institution
        ↓
Authoritative Artifact
        ↓
Integrity Reference
```

with additional integrity attribution where applicable:

```text
Producing System / Signer / Key
        ↓
Integrity Material
```

and:

```text
Reviewer / Process
        ↓
Verification / Publication / Correction / Other Anchor Action
```

Attribution provides context.

It does not create reputation or trust.

---

# Institution vs. Person

Anchor should not assume that every integrity action requires a named individual.

In many cases:

```text
institution
role
system
service
process
key
```

may provide more appropriate attribution.

This supports privacy, operational continuity, and institutional accountability.

---

# System and Agent Attribution

Automated systems, software agents, or AI-assisted processes may participate in Anchor operations.

Anchor may record:

- system identity;
- system Version;
- process role;
- execution context;
- responsible institution;
- applicable key or signature reference.

Anchor does not need to classify such systems as members of a general identity network.

The relevant question is their role in the integrity process.

---

# Signer vs. Authority

Anchor must preserve the distinction:

```text
Signer
≠
Institutional Authority
```

A signature may prove that a particular key signed a representation.

It does not automatically prove that:

- the signer owned the Source Artifact;
- the signer possessed legal authority;
- the content was true;
- the certification was valid;
- the artifact should be trusted.

Authority remains governed by the applicable institution.

---

# Attribution vs. Reputation

Attribution asks:

> Who or what participated in this integrity action?

Reputation asks:

> What is known or believed about that participant over time?

Anchor records the first where needed.

Anchor does not build the second.

---

# Attribution vs. Trust

Attribution can support later trust evaluation.

It does not itself create trust.

Therefore:

```text
Attribution
≠
Trust
```

Anchor may preserve evidence used by Attestor or another institution.

Anchor does not determine trustworthiness.

---

# Privacy and Minimum Necessary Identity Data

Anchor should preserve only identity information necessary for:

- integrity verification;
- institutional attribution;
- accountability;
- signature interpretation;
- Source authority;
- historical reconstruction.

Anchor should avoid unnecessary collection of personal identity information.

The preferred principle is:

> Preserve necessary attribution. Avoid unnecessary identity accumulation.

---

# Historical Attribution

Identity information may change after an Integrity Reference is created.

Examples include:

- employee departure;
- role change;
- institutional rename;
- system replacement;
- key rotation;
- certificate expiration;
- certificate revocation;
- account migration.

Anchor should preserve the attribution context applicable to the historical Integrity Reference.

Later change should not silently rewrite earlier attribution.

---

# Key Rotation

Signing keys may be rotated.

A later key should not replace the historical record of the key used for an earlier signature.

Anchor should preserve:

```text
which key was used
when it was used
which signature it governed
what representation was signed
```

where materially relevant.

---

# Key Revocation

A key may later be revoked or compromised.

Later revocation does not automatically prove that every historical signature using that key was invalid.

Anchor should preserve sufficient temporal context to support later evaluation.

The final key-revocation policy remains to be established through later signature governance.

---

# What Anchor Does Not Do

Anchor does not:

- issue personal identities;
- authenticate users;
- determine legal identity;
- create decentralized identity networks;
- issue credentials;
- manage identity wallets;
- create identity hierarchies;
- govern delegated identity relationships;
- build reputation profiles;
- score trustworthiness;
- determine whether an identity should be trusted.

These functions are outside Anchor's integrity-preservation authority.

---

# Relationship to Suite Institutions

Identity and attribution information remains subordinate to the canonical object and authority of the referenced institution.

For example:

```text
SC-CERT-2026-0001
```

remains Certifier-owned.

A signer reference associated with an Anchor Integrity Reference for that Certification Package does not replace Certifier authority.

Likewise:

```text
SREG-2026-0001
```

remains Registry-owned.

```text
CHR-2026-0001
```

remains Chronicle-owned.

```text
Trust Statement
```

remains Attestor-owned.

Anchor preserves only the attribution necessary for integrity review.

---

# Relationship to Anchor Governance

Governance may later define:

- approved identity-reference types;
- reviewer attribution requirements;
- signature identity requirements;
- key-reference requirements;
- privacy requirements;
- retention;
- key rotation behavior;
- revocation handling;
- automated-process attribution.

These requirements remain intentionally unfrozen until production architecture establishes what is actually necessary.

---

# Relationship to Anchor Standards

Anchor Standards should eventually define minimum attribution requirements for a production Integrity Reference.

Potential requirements may include:

```text
Source Institution required
Source-System Identifier required where available
Producing System optional / conditional
Signer Reference conditional
Key Reference conditional
Reviewer Attribution conditional
```

The final schema and conditional rules remain unfrozen.

---

# Identity and Attribution Principle

The governing principle is:

> Attribute the integrity action. Do not absorb the identity authority.

Anchor should know enough about identity to make its integrity records understandable and accountable.

It should stop before becoming an identity platform.

---

## Status

**Foundation Reconciliation**

This document replaces the pre-Suite model in which Anchor treated identity as its foundational institutional layer.

The current model treats identity as **supporting attribution metadata** for integrity preservation.

The following remain intentionally unfrozen:

```text
identity-reference types
reviewer-role vocabulary
signer-reference requirements
key-reference schema
key rotation policy
revocation policy
privacy requirements
automated-agent attribution
signature governance
first production identity / attribution fields
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
