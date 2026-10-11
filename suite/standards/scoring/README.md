# Satoshium Scoring Standard

**Path:** `/suite/standards/scoring/`  
**Surface:** Satoshium Suite · Standards · Scoring  
**Status:** Current repository documentation

## Purpose

This directory documents the **Satoshium Scoring Standard**, the Suite-wide standards surface governing how scoring is measured, weighted, calculated, interpreted, and communicated **only in governed contexts that explicitly adopt scoring**.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Standard Role

The Scoring Standard defines the expectations governing scoring where a Suite institution, standard, methodology, rule set, or governed process explicitly adopts a scoring model.

Its current primary application is certification-related evaluation.

It does **not** create generalized Suite-wide scoring authority.

Within the Suite architecture:

- **Standards define expectations.**
- **Methodology defines implementation.**
- **Certifier performs certification.**

Scoring may support governed evaluation and certification decision-making where the applicable governing framework explicitly adopts it.

Scoring is therefore **opt-in by governed context**, not automatically inherited by every Suite institution or canonical object.

A score does not independently create certification authority, certification status, lifecycle activation, publication state, or a Trust Statement.


The broader constitutional boundary is:

```text
Scoring Standard
≠ generalized Suite-wide scoring authority

Score
≠ institutional authority

Score
≠ Trust Statement

Score
≠ universal trust status
```

An institution's use of a score does not transfer that institution's authority to the Scoring Standard.

## Scoring Framework

The scoring framework defines the overall model under which scores are produced in a governed context that explicitly adopts scoring.

A governed scoring framework should make clear:

- what is being scored;
- which evaluation criteria apply;
- which inputs are permitted;
- how components are weighted;
- how uncertainty or missing evidence is handled;
- how results are calculated; and
- how scores relate to later certification determinations.

The framework should be transparent enough for independent review.

## Score Components

Score Components define the individual factors that contribute to a score within the applicable governed context.

Components may derive from governed evaluation criteria, evidence-related findings, or other methodology-defined inputs.

Each component should preserve:

- provenance;
- applicable criteria;
- weighting;
- calculation rules;
- interpretation boundaries; and
- relationship to the final certification decision.

A score component should not be treated as an independent certification conclusion.

## Score Interpretation

Score Interpretation defines how calculated results are understood within the applicable governing methodology, rule set, or institutional process.

Interpretation may inform a certification determination, but it must remain distinct from:

- eligibility;
- validation;
- conformance;
- lifecycle state;
- publication;
- and Attestor Trust Statements.

A numeric or categorical score does not become a certification decision merely by crossing a threshold unless the governing methodology explicitly defines that decision rule.

## Score Consistency

Scoring should remain repeatable, transparent, and comparable under equivalent governing conditions.

Consistency requires preservation of:

- applicable standard version;
- methodology version;
- evidence set;
- evaluation criteria;
- weighting rules;
- calculation logic; and
- any material contextual conditions.

Comparable scores should not be assumed to be equivalent when the underlying governing conditions differ.

## Relationship to Evaluation

Where scoring is adopted, it may consume governed evaluation information according to the applicable methodology or institutional rules.

Evaluation remains distinct from scoring.

Scoring may summarize, weight, or structure evaluation results, but it does not replace the evidentiary and evaluative reasoning that produced them.

## Adoption Boundary

The Scoring Standard is Suite-wide as a standards surface, but scoring itself is **not automatically Suite-wide in application**.

A scoring model applies only where its use is explicitly established by the applicable:

- Suite Standard;
- Suite Methodology;
- institution-specific Rule;
- institution-specific Policy;
- institution-specific Procedure; or
- other governed process.

Therefore:

```text
Suite-wide standard
≠ universal scoring requirement

Institutional adoption
→ explicit

Scoring authority
→ remains with the governing institution / governed subject
```

Absence of an explicitly adopted scoring model means no scoring requirement should be inferred.

## Relationship to Certification Logic

Certification Logic may consume scoring results where permitted by the governing methodology.

The relationship between score and certification outcome should remain explicit and reviewable.

A score should explain or support a certification decision—not replace it as the source of institutional authority.

## Relationship to Certifier

Satoshium Certifier is the Suite institution responsible for certification operations and the Certification Package.

The Scoring Standard defines expectations that Certifier and its applicable methodology may implement.

The standard does not independently issue certifications.

## Relationship to Attestor

Attestor operates under its own canonical flow:

Eligible Governed Inputs  
→ Attestation  
→ Rule-Constrained Evaluation  
→ Trust Statement

Certification scoring and Attestor trust conclusions are distinct.

A certification score is not a Trust Statement.

A score does not create universal trust status and does not become an Attestor Evaluation Outcome merely because it is referenced.

A Trust Statement should not be inferred solely from a certification score unless the applicable Attestor rules explicitly govern such use.

## Authority and Relationship Discipline

This directory must preserve the Suite's established distinctions:

- authority is not eligibility;
- eligibility is not evaluation outcome;
- validation is not evaluation;
- validation is not eligibility;
- validation is not conformance;
- valid does not mean true;
- valid does not mean supported;
- valid does not mean published;
- evaluation outcome is not a Trust Statement;
- scoring is not institutional authority;
- canonical creation is not lifecycle activation;
- lifecycle activation is not publication;
- reference does not equal derivation;
- reference does not equal support; and
- reference does not transfer authority.

## Historical Discipline

Changes to scoring models, weights, thresholds, or interpretation rules should be versioned and historically preserved.

Earlier scores should remain interpretable under the standard and methodology versions that produced them.

A later scoring model should not silently rewrite historical scoring results.

Supersession is not mutation.

## Repository Expectations

Changes to this directory should preserve:

1. transparent scoring rules;
2. explicit weighting and calculation logic;
3. separation between evaluation and scoring;
4. separation between scoring and certification authority;
5. separation between certification scoring and Attestor trust conclusions;
6. historical version discipline;
7. reproducibility under equivalent governing conditions; and
8. consistency with the governing Suite standards, methodology, and Certifier architecture;
9. explicit adoption before scoring is applied outside a governed certification context;
10. no generalized Suite-wide scoring authority; and
11. preservation of institutional authority over any scoring-dependent determination.

Changes that would redefine the relationship between scores and certification outcomes, lifecycle states, or Attestor Trust Statements require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Scores may support governed decisions where explicitly adopted; they do not create authority, universal status, or Suite-wide conclusions by themselves.**
