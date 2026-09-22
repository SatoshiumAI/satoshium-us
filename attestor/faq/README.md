# Satoshium Attestor — FAQ

## Page
`/attestor/faq/`

## Purpose
This page provides concise explanatory answers about the established architecture and current implementation status of **Satoshium Attestor**.

The FAQ reflects adopted architecture. It does not independently create canonical objects, controlled values, lifecycle states, or machine rules.

## Canonical Responsibility
**Attestor → Trust Statement**

A Trust Statement is a governed, attributable, bounded Attestor conclusion produced through Rule-Constrained Evaluation of an Attestation against eligible governed inputs.

## Governing Principle
> **Reference does not transfer authority.**

## Canonical Model
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Core Answers

### What is Attestor?
Attestor is the Satoshium Suite institution responsible for producing governed, attributable, bounded Trust Statements through Rule-Constrained Evaluation.

### What is an Attestation?
A governed, attributable assertion.

### What is a Trust Statement?
Attestor's canonical institutional output: a governed, attributable, bounded conclusion.

### Does Attestor determine universal truth?
No.

A Trust Statement is authoritative as an Attestor conclusion within its defined scope. It is not a declaration of universal truth.

### What role does Evidence play?
Evidence provides supporting material or authoritative references used during evaluation. Evidence retains its own provenance, relevant state, scope, limitations, and source authority.

### What is a Trust Signal?
Trust Signal is historical/descriptive Attestor terminology only. It is not a current canonical Attestor object, reputation score, confidence percentage, or automatic trust indicator.

It must remain distinct from:

**Beacon → Discovery Signal / Discovery Metadata**

## Authority and Suite Relationships
- **Atlas → Authoritative Intelligence**
- **Navigator → Workflow Definition / Orchestration**
- **Certifier → Certification Package**
- **Registry → Satoshium Registry Record**
- **Chronicle → Chronicle Entry**
- **Anchor → Integrity Reference**
- **Beacon → Discovery Signal / Discovery Metadata**
- **Attestor → Trust Statement**

Attestor may reference eligible governed outputs from these institutions without assuming their canonical authority.

## Identifiers
- Attestation → `ATT-YYYY-NNNN`
- Trust Statement → `TRST-YYYY-NNNN`

Canonical identity and version identity are distinct.

## Attestation Types
Adopted values:
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

## Evaluation Outcomes
Adopted values:
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## Lifecycle
Adopted Lifecycle States:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Review and correction are activities rather than lifecycle states.

## Corrections and Versioning
Attestor corrects Attestor-owned objects.

A bounded correction may preserve canonical identity when essential institutional meaning remains intact.

A materially changed Attestation assertion requires a new `ATT-YYYY-NNNN`.

A materially changed Trust Statement conclusion requires a new `TRST-YYYY-NNNN`.

> **A changed conclusion is a changed canonical statement.**

## Publication
Adopted Publication States:
- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

A canonical Trust Statement is not automatically public.

## Validation, Evaluation, and Conformance
These are distinct institutional concepts.

- **Evaluation** → determines an Evaluation Outcome and supports formation of a bounded conclusion.
- **Validation** → determines whether an Attestor object satisfies applicable normative requirements.
- **Conformance** → determines whether a declared target satisfies an applicable requirements set using required validation and evidence.

> **Validation ≠ Evaluation**

> **Validation ≠ Conformance**

> **Valid ≠ Published**

## Reputation and Trust Scores
Attestor does not establish:
- a generic reputation framework;
- a canonical reputation object;
- a reputation score;
- a confidence percentage;
- a universal trust score.

Attestor produces bounded Trust Statements.

## Operational Status
Attestor is **Operational**.

The first controlled production operation completed the governed path from eligible Suite-source inputs through canonical Attestation, Rule-Constrained Evaluation, canonical Trust Statement, Validation, Governed Review, Conformance, lifecycle activation, Publication, final-state revalidation, evidence preservation, post-operation institutional review, and Operational Proof.

First production canonical objects:
- `ATT-2026-0001` — **Active · Published · V1.0**
- `TRST-2026-0001` — **Active · Published · V1.0**

Production Evaluation Outcome:
- `supported`

Production Validation:
- `ATT-2026-0001` → `valid`
- `TRST-2026-0001` → `valid`
- mandatory `not-tested` → `0`

Governed Review:
- `25 / 25` → `SATISFIED`

Production Conformance:
- `ATT-2026-0001` → `conformant`
- `TRST-2026-0001` → `conformant`

Post-operation institutional review:
- `11 PASS / 0 FAIL / 0 UNRESOLVED`

Operational Proof:
- **ESTABLISHED**

## What Remains Open?
Attestor's institutional architecture and first operational proof are established.

Future work is continuing governance rather than a prerequisite to claiming operational status. Future Attestations, Evaluations, Trust Statements, corrections, source classes, specialized profiles, and implementation paths remain separately governed and must earn their own applicable Validation, Review, Conformance, lifecycle, and publication determinations.

The first operation does not imply that:
- every Attestation Type has been production-tested;
- every Evaluation Outcome has been exercised;
- every lifecycle or relationship value has been exercised;
- external-source handling has been independently production-tested;
- every specialized schema or template profile has been production-proven;
- future operations inherit the first operation's conclusions.

## Status
**FAQ → Operationally Reconciled**

The FAQ now reflects Attestor's established operational state and first production proof rather than the former Implementation & Validation posture.

**Attestor → Operational**

**Production proof → ESTABLISHED**

## Files
- `index.html` — public FAQ page.
- `README.md` — repository documentation.
