# Evaluation Criteria

**Path:** `/suite/methodology/evaluation-criteria/`  
**Surface:** Satoshium Suite · Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents the Satoshium Suite **Evaluation Criteria** methodology surface.

Evaluation Criteria define the objective measures used to assess certification targets consistently, transparently, and repeatably.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Methodology Role

Evaluation Criteria are part of the Satoshium Suite Methodology.

Their role is to provide the governed assessment framework used during certification evaluation. They support consistent application of the methodology by defining the factors against which eligible evidence and certification targets are assessed.

Evaluation Criteria support scoring, certification logic, and certification decisions, but they do not independently create a certification outcome.

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

Authority must remain distinct from eligibility, evaluation outcome, and downstream trust conclusions.

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
- evaluation outcome is not a Trust Statement; and
- reference does not transfer authority.

The criteria help evaluate governed inputs. They do not collapse the separate responsibilities of Certifier, Registry, Chronicle, Anchor, Beacon, Attestor, or other Suite institutions.

## Relationship to Evidence

Evaluation Criteria operate on evidence that has entered the governed certification process under the applicable standards and methodology.

The existence, authenticity, integrity, or validity of evidence does not by itself establish a certification determination.

Evidence remains subject to the applicable evaluation process and decision logic.

## Relationship to Scoring and Certification Logic

Evaluation Criteria may provide the basis for scoring or structured assessment.

Scoring and certification logic may consume the resulting evaluation information according to the governing methodology.

Neither scoring nor any individual criterion should be treated as a substitute for the complete governed certification decision process.

## Relationship to Certifier

Satoshium Certifier is the Suite institution responsible for certification operations and the Certification Package.

Evaluation Criteria support Certifier by defining objective measures used within the certification methodology.

The criteria do not independently issue certifications, activate lifecycle state, publish records, or become the authoritative source of a certification object.

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
7. consistency with the governing Suite standards, methodology, and Certifier architecture.

Changes that would redefine institutional authority, certification lifecycle semantics, or the relationship between certification evaluation and Attestor trust conclusions require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Consistent evaluation requires consistent criteria, applied within the authority and methodology that govern the certification process.**
