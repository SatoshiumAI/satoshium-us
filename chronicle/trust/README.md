# Trust

## Overview

Within the current Satoshium Anchor architecture, **Trust** is not an Anchor-owned institutional function.

Anchor does not determine trustworthiness.

Anchor does not issue Trust Statements.

Anchor does not calculate trust scores or maintain trust relationships.

Within the Satoshium Suite:

```text
Attestor
→ Trust Statement

Anchor
→ Integrity Reference
```

Anchor's role is narrower:

> Preserve the integrity of a defined Trust Statement or other trust-related artifact when that preservation has durable institutional value.

The governing distinction is:

```text
Trust Judgment
≠
Trust Artifact Integrity
```

---

## Purpose

The `/anchor/trust/` route is retained for continuity.

Its current purpose is to define how Anchor handles trust-related artifacts without becoming the trust authority.

Potential trust-related artifacts include:

- Trust Statements;
- trust signals;
- confidence statements;
- trust assessments;
- warnings;
- recommendations;
- trust scores;
- trust methodology documents;
- decision frameworks;
- trust-related governance records.

Anchor may preserve Integrity References for these artifacts.

Anchor does not adopt their conclusions.

---

# Relationship to Attestor

Satoshium Attestor remains authoritative for:

- Trust Statements;
- trust judgments;
- Attestor identifiers;
- Attestor-controlled metadata;
- Attestor Versions;
- Attestor Corrections;
- Attestor lifecycle;
- Attestor publication.

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

> Reference does not transfer authority.

---

# Trust Artifact

A **Trust Artifact** is a statement, score, signal, warning, recommendation, assessment, methodology, or other governed representation containing trust-related information.

Potential examples include:

```text
Trust Statement
confidence assessment
trust score
warning
recommendation
risk judgment
trust framework
evaluation methodology
decision rule
```

A Trust Artifact may become an Anchor candidate where later integrity verification provides durable value.

---

# Source Authority

The Source Institution remains authoritative for:

- trust meaning;
- trust methodology;
- trust conclusion;
- publication;
- lifecycle;
- Correction;
- Versioning;
- withdrawal;
- replacement.

Anchor owns only the Integrity Reference and Anchor-controlled integrity metadata.

---

# Canonical Representation

Before anchoring a trust-related artifact, Anchor must define:

```text
Canonical Representation
Representation Boundary
```

This may require distinguishing:

```text
canonical Trust Statement
```

from:

```text
dynamic user interface
current dashboard state
later comments
derived presentation
live scoring visualization
unrelated surrounding content
```

The Integrity Reference should identify the representation clearly enough for later review.

---

# Trust Artifact Integrity

Trust Artifact Integrity asks:

> Does the reviewed trust-related representation remain consistent with the representation governed by the Integrity Reference?

It does not ask:

> Should this trust judgment be accepted?

Therefore:

```text
Trust Artifact Integrity
≠
Trustworthiness
```

---

# Integrity of a Trust Statement vs. Validity of the Trust Judgment

A Trust Statement may retain perfect integrity while being:

- disputed;
- outdated;
- context-specific;
- incomplete;
- based on weak methodology;
- based on incorrect information;
- superseded;
- inappropriate for a later context.

Anchor can verify the integrity relationship.

Anchor cannot infer the correctness of the trust judgment merely from integrity.

The governing distinction is:

```text
Integrity of a Trust Statement
≠
Validity of the Trust Judgment
```

---

# Trust vs. Verification

Anchor Integrity Verification asks whether an artifact representation remains consistent with its Integrity Reference.

Attestor or another trust process may ask whether confidence should be placed in the artifact, subject, source, or conclusion.

Therefore:

```text
Integrity Verification
≠
Trust Evaluation
```

A successful Anchor Verification does not mean:

```text
trusted
approved
recommended
safe
credible
```

unless the Source Institution separately states that conclusion.

---

# Trust vs. Certification

Certifier may issue a certification determination.

Certification may inform a later trust judgment.

Anchor may preserve integrity for:

- Certification Package;
- Trust Statement;
- both.

Anchor does not convert certification into trust.

---

# Trust vs. Reputation

Reputation may inform trust.

Trust may incorporate reputation, history, certification, evidence, context, or other signals.

Anchor calculates neither reputation nor trust.

Anchor may preserve the integrity of artifacts produced by systems that do.

Therefore:

```text
Integrity
≠
Reputation
≠
Trust
```

---

# Trust vs. History

Chronicle preserves qualifying historical memory through Chronicle Entries.

Historical facts may influence a Trust Statement.

Anchor may preserve:

- Chronicle Entry integrity;
- Trust Statement integrity;
- both.

It does not determine how history should affect trust.

---

# Trust vs. Evidence

Evidence may influence trust.

Anchor may preserve Integrity References for evidence artifacts.

Anchor does not determine evidentiary weight simply by confirming artifact integrity.

Therefore:

```text
Evidence Integrity
≠
Evidence Weight
```

---

# Trust Methodology Artifacts

A trust methodology may itself become an Anchor candidate.

Examples may include:

- evaluation rubric;
- scoring methodology;
- confidence model;
- trust framework;
- decision rule;
- weighting model;
- governance procedure;
- risk-assessment specification.

In that case, Anchor preserves the integrity of the methodology artifact.

Anchor does not endorse the methodology.

---

# Trust Artifact Lifecycle

A Trust Artifact may later be:

- revised;
- corrected;
- superseded;
- withdrawn;
- revoked;
- replaced;
- reissued;
- archived.

A later Source change does not erase the earlier Integrity Reference.

Conceptually:

```text
Earlier Trust Representation
        ↓
Earlier Integrity Reference

Later Trust Representation
        ↓
Later Anchor Version or New Integrity Reference
where required
```

The final Versioning rule remains unfrozen.

---

# Source Trust Change vs. Anchor Correction

A **Source Trust Change** occurs when Attestor or another Source Institution changes:

- the trust judgment;
- Trust Statement;
- trust score;
- methodology;
- warning;
- recommendation;
- lifecycle;
- publication status.

An **Anchor Correction** occurs when Anchor incorrectly recorded its own integrity information.

Examples may include:

- wrong Source Artifact;
- wrong Source-System Identifier;
- wrong Canonical Representation;
- wrong Representation Boundary;
- wrong digest;
- wrong algorithm;
- wrong timestamp;
- wrong signer reference;
- wrong Verification Material.

Therefore:

```text
Source Trust Change
≠
Anchor Correction
```

---

# Trust Withdrawal or Revocation

A Trust Statement may later be withdrawn or revoked.

Withdrawal does not erase the historical existence of the earlier representation.

Anchor should preserve enough context to identify:

```text
what was anchored
when it was anchored
which representation applied
which Source Institution governed it
what later Source change occurred
```

where materially relevant.

Anchor should not silently rewrite the original Integrity Reference.

---

# Trust Disputes

A trust judgment may be disputed.

Anchor may preserve Integrity References for:

- original Trust Statement;
- challenge artifact;
- supporting evidence;
- rebuttal;
- replacement Trust Statement;
- later institutional finding.

Anchor does not adjudicate the dispute.

---

# Privacy and Judgment Boundary

Trust artifacts may contain sensitive evaluative information about:

- individuals;
- organizations;
- systems;
- communities;
- agents;
- institutions.

Anchor should not amplify trust judgments merely because cryptographic anchoring is technically possible.

The minimum-necessary-data principle remains active.

Potentially preferable designs may preserve:

- Source references rather than copied personal data;
- institutional roles rather than unnecessary personal identifiers;
- integrity material rather than complete evaluative profiles;
- externally governed canonical locations rather than duplicated trust databases.

The governing principle is:

> Preserve necessary integrity context. Do not amplify unnecessary trust judgments.

---

# What Anchor Preserves

For a trust-related Integrity Reference, Anchor may preserve:

- Anchor Identifier;
- Source Institution;
- Source-System Identifier;
- Trust Artifact Type;
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

The final production schema remains unfrozen.

---

# What Anchor Does Not Do

Anchor does not:

- issue Trust Statements;
- determine trustworthiness;
- calculate trust scores;
- rank trusted entities;
- maintain trust relationships;
- aggregate trust history;
- adjudicate trust disputes;
- determine credibility;
- define universal trust semantics;
- endorse trust methodologies;
- replace Attestor authority.

---

# Relationship to Anchor Attestations

The `/anchor/attestations/` section now concerns attestation artifact integrity.

A Trust Statement may contain attestation-like content.

Anchor may preserve the Trust Statement representation without creating a separate Anchor trust or attestation authority.

---

# Relationship to Anchor Reputation

The `/anchor/reputation/` section now concerns reputation-related artifact integrity.

A reputation artifact may influence trust.

A Trust Statement may reference reputation.

Anchor may preserve both artifacts without performing either calculation.

---

# Relationship to Anchor Claims

Claim-related artifacts may influence trust.

Anchor may preserve Integrity References for:

```text
Claim Artifact
Trust Statement
Evidence Artifact
Certification Package
Chronicle Entry
```

where justified.

The presence of multiple Integrity References does not merge their institutional meanings.

---

# Relationship to Anchor Integration

The preferred interoperability model is:

```text
Source Institution
        ↓
Authoritative Trust Artifact
        ↓
Canonical Representation
        ↓
Anchor Integrity Reference
```

The Source Institution retains responsibility for trust meaning and judgment.

---

# Trust Principle

The governing principle is:

> Preserve trust artifacts. Do not become the trust authority.

Anchor should preserve trust-related integrity where it adds durable value and stop before trust scoring, trust judgment, recommendation, ranking, or dispute resolution.

---

## Status

**Foundation Reconciliation**

This document replaces the pre-Suite model in which trust was treated as an evolving Anchor institutional layer.

The current model treats trust as **externally governed judgment represented in artifacts that may become subjects of Anchor integrity preservation**.

The following remain intentionally unfrozen:

```text
Trust Artifact Type Controlled Values
Trust Statement anchoring requirements
trust-related privacy requirements
methodology-artifact anchoring rules
trust withdrawal / revocation handling
trust-dispute reference patterns
new Anchor Version vs. new Integrity Reference rule
trust-specific schema conditions
first production Trust Statement Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
