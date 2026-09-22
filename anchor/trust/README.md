# Satoshium Anchor — Trust

**Path:** `/anchor/trust/`  
**Role:** Trust-Related Artifact Integrity  
**Institution:** Satoshium Anchor  
**Status:** Active bounded integrity-preservation surface

## Overview

The `/anchor/trust/` directory defines how Satoshium Anchor may preserve the integrity of externally governed **Trust Statements** and other trust-related artifacts without determining trustworthiness or becoming the trust authority.

Anchor does not:

- issue Trust Statements;
- determine trustworthiness;
- calculate trust scores;
- rank trusted entities;
- maintain trust relationships;
- aggregate trust history;
- define universal trust semantics;
- adjudicate trust disputes;
- endorse trust methodologies.

Within the Satoshium Suite, **Attestor remains authoritative for Trust Statements**.

Anchor's role begins only when the integrity of a Trust Statement or another trust-related artifact should be preserved through an **Integrity Reference**.

## Trust Boundary

Trust is a judgment or assessment made by a person, institution, community, system, or governed Attestor process.

Anchor does not make that judgment.

Anchor may preserve the integrity of the artifact in which that judgment is expressed.

```text
Trust Judgment
≠
Trust Artifact Integrity
```

## Trust Statement

A Trust Statement is an Attestor-owned canonical object expressing a governed trust-related conclusion or assessment.

```text
Attestor
→ Trust Statement

Anchor
→ Integrity Reference
```

Attestor remains authoritative for:

- meaning;
- trust conclusion;
- lifecycle;
- Versioning;
- Correction;
- publication.

Anchor may preserve integrity context for a defined Trust Statement representation without becoming the trust authority.

## Trust Artifact

A trust-related artifact may include:

- Trust Statement;
- trust signal;
- assessment;
- recommendation;
- warning;
- confidence statement;
- trust methodology;
- evaluation framework;
- scoring model;
- decision rule;
- governance document;
- other governed trust representation.

Anchor may preserve an Integrity Reference for such an artifact where durable integrity preservation has value.

## Canonical Representation

Before Anchor generates integrity material, it should define:

- the exact artifact representation;
- the Representation Boundary;
- the Source Institution;
- the Source-System Identifier where available;
- the trust-artifact type;
- the integrity method;
- the integrity value;
- temporal context;
- signature or other Verification Material where applicable.

Anchor preserves the defined representation.

It does not preserve an undefined concept of trust.

## Trust Artifact Integrity

Anchor may preserve an Integrity Reference that allows later reviewers to determine whether a trust-related representation remains consistent with the representation originally anchored.

That question is bounded:

```text
Integrity
→ Has the anchored representation changed?

Trust
→ Should confidence be placed in the subject,
  statement, source, or conclusion?
```

Anchor answers only the integrity question.

## Trust vs. Verification

Anchor Integrity Verification may confirm consistency with an Integrity Reference.

It does **not** determine whether the underlying Trust Statement should be accepted.

A successful Verification establishes only what the integrity evidence supports.

## Trust vs. Certification

Certification may inform trust, but Certifier remains authoritative for certification decisions.

Anchor does not turn certification into a trust judgment.

## Trust vs. Reputation

Reputation may influence trust, but Anchor calculates neither trust nor reputation.

Anchor may preserve Integrity References for artifacts produced by systems that do.

## Integrity of a Trust Statement

A Trust Statement may retain perfect cryptographic integrity while remaining:

- disputable;
- contextual;
- outdated;
- incomplete;
- methodologically weak;
- superseded.

Therefore:

```text
Integrity of a Trust Statement
≠
Validity of the Trust Judgment
```

Anchor may confirm that the representation has not changed.

It does not prove that the trust conclusion is correct.

## Trust Artifact Lifecycle

A Trust Statement or other trust-related artifact may later be:

- superseded;
- withdrawn;
- corrected;
- revoked;
- replaced;
- reissued.

Anchor should preserve the integrity lineage of the representation it actually anchored rather than silently rewriting the earlier state.

```text
Earlier Trust Representation
→ Earlier Integrity Reference

Later Trust Representation
→ Later Anchor Version
  or New Integrity Reference where required
```

## Source Trust Change vs. Anchor Correction

A change by Attestor or another Source Institution to:

- the trust judgment;
- Trust Statement;
- methodology;
- lifecycle;
- publication state;

is a **Source Artifact change**.

An Anchor error involving:

- wrong Source Artifact;
- wrong representation;
- wrong digest;
- wrong timestamp;
- wrong signer metadata;
- other Anchor-owned information;

may require an **Anchor Correction**.

```text
Source Trust Change
≠
Anchor Correction
```

## Privacy and Judgment Boundary

Trust-related artifacts may contain sensitive or evaluative information.

Anchor should preserve only the integrity context needed for the governed purpose.

The minimum-necessary-data principle remains active.

> **Preserve necessary integrity context. Do not amplify unnecessary trust judgments.**

## Relationship to the Suite

Relevant institutional relationships include:

```text
Atlas
→ may provide authoritative intelligence

Certifier
→ may provide certification determinations

Registry
→ may catalog authoritative records

Chronicle
→ may preserve qualifying historical memory

Attestor
→ may issue Trust Statements

Anchor
→ may preserve Integrity References for the relevant artifacts
```

These systems may inform one another while retaining separate authority.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

**Connection ≠ Identity.**  
**Reference ≠ Derivation.**  
**Reference ≠ Support.**  
**Reference ≠ Authority Transfer.**

## Current Institutional Position

The older Anchor model treated trust as part of Anchor's conceptual identity/trust framework.

That model is superseded.

The current institutional role is narrower:

```text
Anchor
→ preserves integrity of trust-related artifacts

Attestor
→ owns Trust Statements and trust-related conclusions
```

Trust remains a bounded reference domain for Anchor, not an Anchor-owned authority domain.

## Trust Principle

> **Preserve trust artifacts. Do not become the trust authority.**

README reconciliation documents the current Anchor trust boundary. It does not redesign it.
