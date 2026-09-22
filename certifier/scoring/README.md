# Satoshium Certifier — Evaluation Philosophy

**Path:** `/certifier/scoring/`  
**Institution:** Satoshium Certifier  
**Surface:** Evaluation Philosophy  
**Status:** Current repository documentation

## Purpose

This directory documents the **Evaluation Philosophy** used by Satoshium Certifier.

Although the repository path is `/certifier/scoring/`, the current public surface explicitly rejects arbitrary numerical scoring in favor of evidence-based evaluation, documented reasoning, confidence posture, and defined certification determinations.

The public page for this directory is:

- `index.html`

This README documents the role of evaluation, the relationship among evidence, standards, methodology, reviewer reasoning, confidence, and certification determinations, and the boundaries that should be preserved during future reconciliation.

## Evaluation Philosophy

Satoshium Certifier evaluates evidence rather than assigning arbitrary numerical scores.

Certification determinations are intended to derive from:

- published Suite Standards;
- documented evidence;
- repeatable Suite Methodology;
- preserved reviewer reasoning; and
- the resulting certification record.

The governing relationship is:

```text
Suite Standards
        ↓
Evidence
        ↓
Suite Methodology
        ↓
Certifier Evaluation
        ↓
Certification Determination
        ↓
Certification Package
```

The Certification Package remains Certifier's canonical operational record.

## Evidence Weight

Not all evidence contributes equally to a certification review.

Evidence may differ in relevance, provenance, directness, integrity, corroboration, and applicability.

Examples may include:

- primary evidence;
- supporting evidence;
- integrity references;
- contextual observations; and
- reviewer notes.

Evidence weighting should remain reviewable and traceable to the applicable Certification Package.

## Confidence

Certifier uses confidence as a qualitative certification concept rather than an arbitrary numerical score.

Confidence may be strengthened through:

- corroboration;
- transparency;
- evidence quality;
- traceability;
- methodological consistency; and
- repeatable review.

Certifier confidence terminology must remain bounded to Certifier.

It is not automatically equivalent to an Attestor Trust Statement.

## Reviewer Judgment

Certifier combines structured standards with documented reviewer judgment.

Reviewer judgment should remain visible through:

- findings;
- assumptions;
- limitations;
- reasoning;
- evidence treatment; and
- certification conclusions.

The objective is not hidden discretion.

The objective is reviewable reasoning.

## Evaluation Role

Evaluation is the reasoning layer within Certifier.

The relationship is:

```text
Standards
→ define expectations

Evidence
→ provides factual support

Methodology
→ defines implementation

Evaluation
→ connects those elements through documented reasoning

Certification Decision
→ records the governed outcome
```

Evaluation does not replace Standards or Methodology.

## Determinations

The current public page identifies determinations such as:

- Pass;
- Conditional Pass;
- Fail;
- Expired; and
- Revoked.

This terminology should be treated cautiously until Suite Reconciliation confirms the governing distinction between:

- evaluation outcome;
- certification decision;
- certification status; and
- lifecycle state.

In particular, `Expired` and `Revoked` appear lifecycle-oriented rather than equivalent to an evaluation result.

This README therefore preserves the existing terminology without redefining those categories.

## Numerical Scoring

The current public surface rejects arbitrary percentages, stars, letter grades, and similar scoring models as the normal basis for Certifier decisions.

Historical prototype scores may still exist in earlier production records.

Where such historical scores are preserved, they should remain clearly identified as historical assessment data rather than current Certifier architecture.

## Relationship to Certification Classes

Evaluation may contribute to assignment of a Certification Class after the certification process is completed.

A Certification Class communicates the result of certification.

It should not be treated as:

- an arbitrary score;
- an Attestor Trust Statement;
- a universal ranking; or
- a value judgment.

## Relationship to Evidence

Evidence supports evaluation.

The governing distinction is:

```text
Evidence
≠
Evaluation

Evaluation
≠
Certification Decision
```

Evidence may support or constrain a conclusion, but the certification decision remains a governed Certifier action.

## Relationship to Suite Standards

Suite Standards define the expectations applied during certification.

Evaluation should not silently create new standards merely through reviewer judgment.

## Relationship to Suite Methodology

Suite Methodology defines the repeatable review process.

Evaluation applies reasoning within that governed process.

## Relationship to Attestor

Attestor is operational and institutionally distinct from Certifier.

The current Attestor flow is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Certifier evaluation and Attestor rule-constrained evaluation are distinct institutional processes.

A Certifier confidence posture or certification determination is not an Attestor Trust Statement.

## Authority Discipline

This directory should preserve the following distinctions:

- Evidence ≠ Evaluation
- Evaluation ≠ Certification Decision
- Certification Decision ≠ Lifecycle State
- Certification Outcome ≠ Trust Statement
- Confidence Posture ≠ Trust Statement
- Certification Class ≠ Trust Statement
- Historical Score ≠ Current Certification Architecture
- Validation ≠ Evaluation
- Reference ≠ Derivation
- Reference ≠ Support

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Considerations

The following matters should be resolved during Suite Reconciliation rather than redesigned in this README pass:

1. whether `Pass`, `Conditional Pass`, and `Fail` are formal evaluation outcomes, certification determinations, or another governed category;
2. whether `Expired` and `Revoked` belong exclusively to lifecycle/status rather than evaluation;
3. how Certifier confidence posture should be bounded from Attestor Trust Statements;
4. whether the repository path `/certifier/scoring/` should remain even though the current surface is Evaluation Philosophy; and
5. how historical prototype numerical assessment data should be represented alongside the non-numerical current model.

## Repository Expectations

Changes to this directory should preserve:

1. evidence-based rather than arbitrary numerical evaluation;
2. documented reviewer reasoning;
3. Suite Standards as the expectations layer;
4. Suite Methodology as the implementation layer;
5. separation among evidence, evaluation, decision, and lifecycle;
6. separation between Certifier confidence and Attestor trust conclusions;
7. historical assessment provenance; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Certifier evaluation should preserve visible evidence and reviewable reasoning rather than reduce certification to arbitrary numerical scoring.**
