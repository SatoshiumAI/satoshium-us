# Satoshium Suite — Certification Logic

## Path

`/suite/methodology/certification-logic/`

## Repository Role

This directory documents **Certification Logic** within the Satoshium Suite Methodology.

Certification Logic defines the governed decision logic used to convert **Certifier / certification-domain inputs** — including eligible evidence, certification evaluation results, and scoring where explicitly adopted — into consistent certification outcomes.

Its purpose is to make certification determinations reviewable, repeatable, and capable of structured implementation without replacing the authority of the governing standards, certification methodology, or Certifier.

It is not Suite Governance decision logic and does not govern Attestor Rule-Constrained Evaluation.

## Architectural Position

Certification Logic belongs to the **Suite Methodology** layer as a **certification-specific methodology surface**.

The governing separation is:

- **Standards define expectations.**
- **Methodology defines how those expectations are applied.**
- **Certification Logic defines the decision rules used within that methodology.**
- **Certifier performs certification and produces the Certification Package.**

Certification Logic therefore supports certification execution; it does not itself become the Certifier and does not create a Certification Package independently of the Certifier institution.

```text
Certification Logic
→ Certifier / certification-domain decision logic

Suite Governance Decision Logic
→ governed separately under Suite Governance

Attestor Rule-Constrained Evaluation
→ governed separately by Attestor
```

## Scope Boundary

This methodology surface governs **certification decision logic only**.

```text
CERTIFICATION LOGIC
≠ SUITE GOVERNANCE DECISION LOGIC

CERTIFICATION LOGIC
≠ ATTESTOR RULE-CONSTRAINED EVALUATION

CERTIFICATION OUTCOME
≠ TRUST STATEMENT

CERTIFICATION DECISION
≠ GOVERNANCE DECISION
```

Certification Logic may consume certification-domain inputs and produce a governed certification determination.

It does not create cross-institution approval authority or universal Suite decision rules.

If certification logic exposes a proposed change to institutional role, canonical ownership, Suite membership, authority allocation, or another constitutional boundary, the issue must move to the applicable **Suite Governance / Architecture Reconciliation** process.

## Core Responsibilities

Certification Logic may define or document rules governing:

- eligibility to enter formal certification evaluation;
- evidence sufficiency and applicable evidence requirements;
- application of evaluation criteria;
- transformation of certification evaluation results into certification determinations;
- consistency across equivalent evaluations;
- treatment of incomplete, conflicting, corrected, appealed, or exceptional inputs;
- structured expression of certification decision logic for human and software implementation.

These responsibilities must remain bounded by the authority of the governing certification standards, methodology, and Certifier implementation.

Where scoring is used, it must be explicitly adopted by the applicable governing certification framework.

## Decision Discipline

Certification Logic should preserve clear distinctions between the stages and meanings involved in certification.

In particular:

- **Authority is not eligibility.**
- **Eligibility is not an evaluation outcome.**
- **Validation is not evaluation.**
- **Validation is not eligibility.**
- **Validation is not conformance.**
- **Valid is not published.**
- **Valid is not true.**
- **Valid is not supported.**
- **Canonical creation is not lifecycle activation.**
- **Lifecycle activation is not publication.**
- **Evaluation Outcome is not a Trust Statement.**
- **Score is not a Certification Determination.**
- **Certification Decision is not a Governance Decision.**
- **Reference does not transfer authority.**

A certification result must follow the applicable governed rules rather than subjective judgment or undocumented interpretation.

## Relationship to Suite Governance

Suite Governance follows its own governed lifecycle:

```text
Proposal
→ Classification
→ Review
→ Determination
→ Approval
→ Governance Decision Record (GDR)
→ Publication
→ Implementation
→ Preservation
```

Certification Logic does not replace or abbreviate that governance lifecycle.

```text
Certification Determination
≠ Governance Determination

Certification Record
≠ Governance Decision Record
```

## Relationship to Attestor

Attestor applies its own canonical flow:

```text
Eligible Governed Inputs
→ Attestation
→ Rule-Constrained Evaluation
→ Trust Statement
```

Certification Logic does not become Attestor evaluation logic merely because a Certification Package later becomes an eligible governed Attestor input.

```text
Certification Logic
≠ Attestor Rule-Constrained Evaluation

Certification Outcome
≠ Trust Statement
```

## Determinism and Reproducibility

Where the same governed inputs, standards, methodology, evidence, and decision rules apply, Certification Logic should support reproducible outcomes.

The logic should be documented clearly enough that an independent reviewer — or a conforming software implementation — can inspect the decision path and determine how the certification outcome was reached.

Reproducibility does not authorize a reviewer or implementation to change the governing standards, methodology, evidence, or institutional authority.

## Machine-Readable Direction

The public page identifies structured and eventual software execution as an intended direction for Certification Logic.

Machine execution should preserve the same institutional and authority boundaries that govern human review. Automation may implement governed certification logic; it does not create new certification authority, governance authority, or Attestor evaluation authority.

## Relationship to `index.html`

`index.html` is the public-facing explanation of Certification Logic.

This `README.md` documents the repository and architectural role of the directory. It should remain aligned with the public page while avoiding simple duplication of presentation content.

## Maintenance Expectations

Update this README when the established Suite architecture changes the documented role, boundaries, or implementation status of Certification Logic.

Do not use README maintenance to introduce new certification architecture, new authority relationships, universal Suite decision rules, or new Suite responsibilities. Architectural or constitutional changes belong in the appropriate governed review before repository documentation is reconciled to them.

## Governing Principle

**Certification Logic documents and implements governed certification decision rules; it does not become Suite Governance decision logic, Attestor evaluation logic, or an independent source of authority.**
