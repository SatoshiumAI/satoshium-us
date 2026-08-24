# Governance

## Overview

**Anchor Governance** defines the authority, responsibility, decision-making, and change-control framework governing **Satoshium Anchor**.

Anchor Governance applies to Anchor-owned institutional matters such as:

- Integrity References;
- Anchor identifiers;
- Canonical Representation requirements;
- Representation Boundary requirements;
- Integrity Methods;
- cryptographic algorithms;
- signature methods;
- timestamp methods;
- external commitments;
- Verification;
- Validation where later adopted;
- Publication;
- Lifecycle;
- Versions;
- Corrections;
- Maintenance;
- schemas;
- Controlled Values;
- Anchor procedures.

Anchor Governance does not control the substantive authority of external Source Artifacts.

The governing rule is:

> Reference does not transfer authority.

---

## Governance Purpose

Governance exists so Anchor can make institutional decisions consistently and transparently.

It should answer questions such as:

```text
Who or what process may change Anchor requirements?
How are Integrity Methods approved?
How are algorithms deprecated?
How are Anchor schemas versioned?
How are Controlled Values changed?
When is Reverification required?
When is a new Anchor Version required?
When is a formal Correction required?
How is Publication controlled?
How are prior states preserved?
```

Governance translates standards into controlled institutional action.

---

# Governance Boundary

Anchor governs:

```text
Anchor
```

It does not govern:

```text
Certifier
Registry
Chronicle
Atlas
Beacon
Attestor
Navigator
external Source Institutions
```

Anchor may reference artifacts from those systems.

That relationship does not create governance authority over them.

> Reference does not transfer authority.

---

# Governance Hierarchy

The current governance relationship is:

```text
Suite Standards
        ↓
Anchor Standards
        ↓
Anchor Governance Decisions
        ↓
Anchor Policies / Rules where needed
        ↓
Anchor Procedures
        ↓
Schemas / Controlled Values
        ↓
Production Integrity References
        ↓
Maintenance / Corrections / Versions
```

Not every layer must become a separate public document.

The minimum-necessary-structure principle remains active.

---

# Institutional Authority

Anchor is authoritative for its own:

- Integrity References;
- Anchor identifiers;
- Anchor-controlled metadata;
- Integrity State;
- Verification Results;
- Publication State;
- Lifecycle State;
- Anchor Versions;
- Anchor Corrections;
- Anchor procedures;
- Anchor schemas;
- Anchor Controlled Values;
- Anchor maintenance records;
- Anchor-specific governance decisions.

The final production definitions for several of these remain intentionally unfrozen.

---

# Suite Authority Separation

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

Each institution governs its own canonical object.

Anchor Governance applies to the Integrity Reference and Anchor-controlled integrity operations.

It does not govern the referenced object.

---

# Governance Principles

## Authority Should Be Explicit

Anchor decisions should identify the governing requirement, procedure, or institutional basis where material.

Ambiguous authority weakens reproducibility and accountability.

---

## Material Change Should Be Visible

Substantive changes should not occur silently.

Material revisions should preserve:

```text
what changed
why it changed
when it changed
which Version applies
what prior state remains preserved
```

---

## Prior States Should Be Preserved

The governing principle is:

> Correct forward. Preserve backward.

Historical Integrity References, Versions, Validation artifacts, Publication decisions, and other material prior states should remain reconstructable.

---

## Governance Should Remain Narrow

Anchor Governance should not expand merely because a referenced artifact concerns identity, certification, history, trust, or workflow.

Anchor governs integrity preservation.

Other institutions retain their own authority.

---

## Governance Should Remain Technology-Neutral

Governance should control the institutional use of technology without defining the institution around one technology.

---

# Integrity Method Governance

Anchor Governance should determine which Integrity Methods are acceptable for production.

Potential method classes may include:

```text
cryptographic digest
digital signature
timestamp
Merkle commitment
external transparency commitment
Bitcoin commitment
other approved integrity method
```

Final Controlled Values remain unfrozen.

Governance should eventually define:

- approval criteria;
- minimum security expectations;
- method identification;
- compatibility;
- deprecation;
- migration;
- historical support;
- verification requirements.

---

# Algorithm Governance

Cryptographic algorithms age.

Anchor Governance should support:

```text
approved
deprecated for new use
historical-only
prohibited
```

or another future controlled model.

No final algorithm-state vocabulary is established here.

A deprecated algorithm does not automatically invalidate historical Integrity References.

The historical record should preserve:

- algorithm identity;
- Integrity Value;
- representation context;
- date of use;
- later governance status where relevant.

---

# Canonical Representation Governance

Governance should establish requirements for defining:

- Canonical Representation;
- Representation Boundary;
- canonicalization;
- serialization;
- encoding;
- excluded presentation elements;
- package boundaries;
- reproducibility.

Representation rules should evolve through controlled change.

A change to canonicalization rules should not silently reinterpret prior Integrity References.

---

# Schema Governance

Anchor schemas should be versioned explicitly.

Schema governance should eventually define:

```text
schema identity
schema Version
compatibility expectations
required fields
conditional fields
controlled vocabularies
migration expectations
deprecation
```

Schema Version remains distinct from Anchor Version.

---

# Controlled Value Governance

Potential Anchor Controlled Values may include:

- Integrity Method;
- Integrity State;
- Verification Result;
- Publication State;
- Lifecycle State;
- Correction Type;
- representation type;
- commitment method;
- algorithm status.

Controlled Values should be:

```text
documented
stable
version-aware
changed deliberately
```

Ad hoc vocabulary should be avoided in production records.

---

# Verification Governance

Governance should establish:

- what requires Verification;
- who or what process performs Verification;
- minimum Verification inputs;
- required Verification Material;
- possible Verification Results;
- mismatch behavior;
- Reverification triggers;
- recording requirements;
- distinction from Validation.

Integrity Verification remains narrower than certification, truth determination, or trust judgment.

---

# Validation Governance

Anchor has not yet finalized whether Validation should mirror the formal Chronicle model or use a narrower integrity-specific approach.

If Anchor adopts formal Validation, Governance should define:

```text
Validation purpose
rules
sequence
PASS / FAIL behavior
relationship to Verification
relationship to Publication
recording requirements
```

This remains intentionally unfrozen.

---

# Publication Governance

Governance should eventually define:

- when an Integrity Reference is publication-ready;
- whether a separate Publication Gate is required;
- who or what process approves publication;
- Publication State values;
- canonical public representation;
- machine-readable representation;
- withdrawal;
- republication;
- published_at behavior;
- preservation of publication lineage.

Publication architecture should be designed from production need rather than copied mechanically from Chronicle.

---

# Versioning Governance

Anchor Governance must distinguish:

```text
Source Artifact Version
≠
Anchor Version
≠
Schema Version
≠
Algorithm Version
≠
Signature Method Version
```

A Source Artifact may change while an earlier Anchor Integrity Reference remains historically valid.

Later architecture should determine when change requires:

```text
same Integrity Reference + new Anchor Version
```

versus:

```text
new Integrity Reference
```

---

# Correction Governance

Anchor corrects Anchor.

A formal Anchor Correction may be required when Anchor recorded:

- the wrong Source Artifact;
- the wrong Source-System Identifier;
- the wrong Canonical Representation;
- the wrong Representation Boundary;
- the wrong digest;
- the wrong algorithm;
- the wrong timestamp;
- incorrect signature metadata;
- incorrect Verification Material;
- another materially incorrect Anchor-owned field.

Anchor Correction does not rewrite the Source Artifact.

---

# Source Artifact Changes

A Source Institution may legitimately:

- revise;
- correct;
- supersede;
- revoke;
- withdraw;
- republish;
- migrate;
- archive;
- replace;

its own artifact.

Anchor Governance should decide the appropriate Anchor response.

Potential outcomes may include:

```text
No Anchor Action
Editorial Maintenance
Reference Maintenance
Reverification
New Anchor Version
Formal Anchor Correction
New Integrity Reference
Publication Review
Withdrawal Review
```

Final outcome names remain unfrozen.

---

# Decision Records

Material Governance decisions should be documented sufficiently to explain:

```text
Decision
Reason
Authority
Effective Date
Affected Version
Affected Rule / Schema / Method
Prior State
Resulting State
```

Not every routine operational decision requires a separate formal governance object.

Use structure only where it adds durable institutional value.

---

# Maintenance Governance

Governance should eventually define post-publication expectations for:

- broken Source references;
- missing verification material;
- algorithm deprecation;
- signature verification failure;
- timestamp reference failure;
- external commitment verification;
- human / machine consistency;
- Source Artifact change;
- Anchor Corrections;
- Anchor Versions;
- Reverification;
- Publication review.

Maintenance should preserve historical context.

---

# Bitcoin Governance

If Bitcoin becomes an Anchor commitment mechanism, Governance should define:

- when Bitcoin anchoring is appropriate;
- which method is approved;
- whether individual or batch commitments are used;
- Merkle construction rules where applicable;
- transaction / commitment references;
- verification procedure;
- fee / cost considerations;
- retry or failure handling;
- confirmation expectations;
- replacement or migration behavior;
- long-term verification support.

Bitcoin should remain:

```text
an integrity commitment mechanism
```

not:

```text
the source of institutional authority
```

for the artifact being referenced.

---

# Governance and Suite Standards

Anchor Governance operates beneath Suite Standards.

Suite Standards define shared expectations.

Anchor Governance controls how Anchor implements integrity-specific requirements within those shared boundaries.

Anchor must not establish a governance rule that silently contradicts Suite Standards.

---

# Governance and Anchor Standards

Anchor Standards define what integrity preservation requires.

Anchor Governance defines how material decisions about those requirements are controlled.

Conceptually:

```text
Anchor Standards
→ requirement

Anchor Governance
→ institutional decision authority

Procedure
→ repeatable implementation
```

---

# What Anchor Governance Does Not Govern

Anchor Governance does not govern:

- identity infrastructure;
- claim semantics;
- reputation;
- trust scoring;
- certification decisions;
- Registry classification;
- Chronicle Preservation Eligibility;
- Chronicle historical interpretation;
- Atlas jurisdiction intelligence;
- Beacon discovery significance;
- Attestor Trust Statement meaning;
- Navigator workflow authority.

Those remain outside Anchor's institutional authority.

---

# Governance Philosophy

The governing philosophy is:

> Govern Anchor's decisions. Preserve Source authority. Preserve prior states.

Anchor Governance should make change controlled, transparent, reviewable, and durable without turning Anchor into a general-purpose governance authority.

---

## Status

**Foundation Reconciliation**

This document replaces the earlier pre-Suite identity / authority / delegation governance model with Anchor-specific governance for integrity preservation.

The following remain intentionally unfrozen pending later production architecture:

```text
formal decision authority model
reviewer roles
Anchor identifier governance
Integrity Method Controlled Values
algorithm approval policy
Verification Result values
Integrity State values
Validation architecture
Publication architecture
Lifecycle State values
Versioning rules
Correction Types
Maintenance procedure
Bitcoin commitment policy
first production Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
