# Evaluation Criteria

**Path:** `/suite/methodology/evaluation-criteria/`  
**Surface:** Satoshium Suite · Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents the Satoshium Suite **Certification Evaluation Criteria** methodology surface.

The Evaluation Criteria define the objective measures used to assess **Certifier / certification-domain targets** consistently, transparently, and repeatably.

They are not universal Suite evaluation criteria and do not govern Attestor's Rule-Constrained Evaluation.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Methodology Role

Evaluation Criteria are part of the Satoshium Suite Methodology as a **certification-specific methodology surface**.

Their role is to provide the governed assessment framework used during **certification evaluation**. They support consistent application of Certifier methodology by defining the factors against which governed evidence and certification targets are assessed.

Evaluation Criteria may support scoring where scoring is explicitly adopted, as well as certification logic and certification determinations. They do not independently create a certification outcome, institutional authority, or a Trust Statement.

## Scope Boundary

This methodology surface governs **certification evaluation only**.

```text
Certification Evaluation Criteria
→ Certifier / certification-domain methodology

Attestor Rule-Constrained Evaluation
→ Attestor-owned governed evaluation

Other Institutional Evaluation
→ governed by the applicable institution
```

Therefore:

```text
CERTIFICATION EVALUATION
≠ ATTESTOR RULE-CONSTRAINED EVALUATION

CERTIFICATION CRITERIA
≠ UNIVERSAL SUITE EVALUATION CRITERIA

EVALUATION OUTCOME
≠ TRUST STATEMENT
```

Other Suite institutions may reference certification evaluation results where permitted, but they do not inherit these criteria automatically.

## Current Criteria

The current methodology surface identifies the following evaluation criteria.

### Accuracy

Assesses whether submitted information correctly represents the certification target without factual error or material misrepresentation.

### Completeness

Assesses whether all required information, evidence, and supporting documentation have been provided.

### Authenticity

Assesses whether submitted evidence is genuine, verifiable, and originates from reliable sources.

### Integrity

Assesses whether records and evidence remain unaltered, internally consistent, and free from unauthorized modification.

### Authority

Assesses whether evidence originates from individuals, organizations, or sources possessing appropriate authority over the relevant subject matter.

Authority must remain distinct from eligibility, evaluation outcome, institutional authority allocation, and downstream Attestor Trust Statements.

### Timeliness

Assesses whether evidence remains sufficiently current and relevant for the intended certification.

### Consistency

Assesses whether evidence, documentation, and certification records conflict with one another or with applicable previously verified records.

Consistency review must preserve historical accuracy and must not silently rewrite earlier canonical records.

### Transparency

Assesses whether the reasoning, evidence, and methodology supporting certification remain understandable and reviewable.

### Reproducibility

Assesses whether independent reviewers applying the same methodology to the same governed inputs would reasonably reach the same conclusion.

### Risk

Assesses the potential impact of uncertainty, missing evidence, conflicting information, or unresolved issues on certification confidence.

Risk assessment informs governed evaluation and does not independently determine truth, validity, publication state, or trust.

## Evaluation Boundaries

Evaluation Criteria must preserve the established Suite distinctions:

- authority is not eligibility;
- eligibility is not an evaluation outcome;
- validation is not evaluation;
- validation is not eligibility;
- validation is not conformance;
- valid does not mean true;
- valid does not mean supported;
- evaluation outcome is not a Trust Statement;
- certification evaluation is not Attestor Rule-Constrained Evaluation;
- certification criteria are not universal Suite criteria;
- score is not a certification determination;
- downstream use does not imply criteria adoption; and
- reference does not transfer authority.

The criteria help evaluate governed inputs. They do not collapse the separate responsibilities of Certifier, Registry, Chronicle, Anchor, Beacon, Attestor, or other Suite institutions.

## Relationship to Evidence

Evaluation Criteria operate on evidence that has entered the governed certification process under the applicable standards and methodology.

The existence, authenticity, integrity, or validity of evidence does not by itself establish a certification determination.

Evidence remains subject to the applicable evaluation process and decision logic.

## Relationship to Scoring and Certification Logic

Evaluation Criteria may provide the basis for scoring or structured assessment **where scoring is explicitly adopted by the governing certification methodology**.

Scoring and certification logic may consume the resulting evaluation information according to that governing methodology.

Neither scoring nor any individual criterion should be treated as a substitute for the complete governed certification decision process.

```text
Score
≠ Evaluation Outcome
≠ Certification Determination
≠ Trust Statement
```

## Relationship to Attestor

Attestor operates under its own canonical flow:

```text
Eligible Governed Inputs
→ Attestation
→ Rule-Constrained Evaluation
→ Trust Statement
```

Certification Evaluation Criteria do not become Attestor evaluation criteria merely because a certification record is later used as an Attestor input.

```text
Certification Evaluation
≠ Rule-Constrained Evaluation

Certification Evaluation Outcome
≠ Trust Statement
```

Any use of certification-derived information inside Attestor remains governed by Attestor's own rules, eligibility requirements, and authority.

## Relationship to Certifier

Satoshium Certifier is the Suite institution responsible for certification operations and the Certification Package.

Evaluation Criteria support Certifier by defining objective measures used within the certification methodology.

The criteria do not independently issue certifications, activate lifecycle state, publish records, or become the authoritative source of a certification object.

## Cross-Institution Boundary

Certification evaluation results may be:

- referenced by Registry;
- preserved by Chronicle;
- integrity-referenced by Anchor;
- discovered by Beacon;
- consumed as eligible governed inputs by Attestor; or
- used within Navigator-defined workflows.

Those interactions do not make Certification Evaluation Criteria a cross-institution authority layer.

```text
REFERENCE
≠ CRITERIA ADOPTION

DOWNSTREAM USE
≠ AUTHORITY TRANSFER

CERTIFICATION EVALUATION
≠ UNIVERSAL EVALUATION
```

## Review and Reproducibility

Evaluation should be documented well enough that an independent reviewer can understand:

- which criteria were applied;
- what evidence was considered;
- how the evidence was assessed;
- what uncertainties or risks were identified; and
- how the resulting evaluation contributed to the later certification determination.

Repeatability does not require ignoring context, provenance, applicable versions, or the governing conditions under which the evaluation occurred.

## Repository Expectations

Changes to this directory should preserve:

1. objective and reviewable evaluation criteria;
2. the distinction between evaluation and validation;
3. the distinction between criteria and final certification determinations;
4. evidence provenance and authority boundaries;
5. historical accuracy;
6. reproducibility under equivalent governing conditions; and
7. consistency with the governing Suite standards, methodology, and Certifier architecture;
8. explicit certification-domain scope;
9. separation of certification evaluation from Attestor Rule-Constrained Evaluation;
10. explicit scoring adoption where scoring is used;
11. downstream institutional independence; and
12. the distinction between evaluation outcomes and Trust Statements.

Changes that would redefine institutional authority, certification lifecycle semantics, or the relationship between certification evaluation and Attestor trust conclusions require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Consistent certification evaluation requires consistent criteria applied within Certifier's governed methodology; those criteria do not become universal Suite evaluation rules or Attestor trust logic.**
