# Satoshium Attestor — Evidence

## Page
`/attestor/evidence/`

## Purpose
This page defines the governed role of **Evidence** within Satoshium Attestor.

Evidence is supporting material or an authoritative reference used by Attestor to evaluate an Attestation and support formation of a **Trust Statement**.

Evidence remains distinct from:
- the Attestation;
- the Trust Statement;
- the canonical authority of any referenced source.

## Governing Principle
> **Reference does not transfer authority.**

## Canonical Context
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

Evidence may participate among the eligible governed inputs used in that process.

> **Evidence ≠ Attestation ≠ Trust Statement**

## Evidence Is a Role, Not a New Canonical Object Class
Attestor does not establish a generic canonical **Evidence Record** merely because information participates as evidence.

Evidence may be:
- source material;
- a governed reference;
- a document;
- a record;
- a dataset;
- media;
- an observation;
- an authoritative Suite object;
- another eligible governed source.

Where an Attestation specifically asserts something about evidence, the adopted Attestation Type `evidence` may be used.

That does not transform the underlying evidence into the Attestation.

## Eligibility
Evidence participates in a particular evaluation only after the applicable governed Eligibility determination.

> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

> **Eligible Here ≠ Eligible Everywhere**

Eligibility does not mean that the evidence is sufficient, correct, favorable, or determinative.

## Authoritative Suite References
Potential governed references include:
- Atlas Authoritative Intelligence;
- Navigator Workflow Definition / Orchestration context;
- Certifier Certification Packages;
- Satoshium Registry Records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals / Discovery Metadata;
- other eligible governed sources.

The originating institution retains canonical authority.

## Provenance
Evidence preserves applicable provenance using the adopted modes:
- `direct`
- `referenced`
- `derived`

Relevant provenance may include:
- source or origin;
- attribution;
- source relationship;
- derivation basis;
- relevant source state;
- material limitations.

> **Evaluation cannot become a provenance break.**

## Relevance and Scope
Evidence is evaluated relative to a particular assertion, purpose, and scope.

Evidence relevant to one bounded question does not silently establish a broader conclusion.

Conceptually:

`Evidence → Assertion → Scope → Evaluation Basis`

## Relationships
Evidence may participate through governed relationships such as:
- `supports`
- `references`
- `derived-from`
- `related-to`

Relationship vocabulary and Evaluation Outcome vocabulary are separate.

> **supports ≠ supported**

> **Reference ≠ Support**

> **Reference ≠ Derivation**

## Supporting, Limiting, and Conflicting Evidence
Attestor preserves material evidence that:
- supports;
- limits;
- qualifies;
- contextualizes;
- conflicts with

the assertion under evaluation.

Material conflicts, exclusions, uncertainty, and limitations remain visible in the Evaluation basis and Trust Statement where applicable.

Attestor does not discard conflicting evidence merely to obtain a favorable outcome.

## Relevant Source State
Evidence may change after an evaluation.

Attestor preserves the material source state relevant to the Evaluation so later changes do not silently rewrite the basis of an earlier Trust Statement.

> **Source State at Evaluation ≠ Later Source State**

A material later source-state change may trigger review.

> **Material Source-State Change → Review**

Review does not predetermine correction, withdrawal, supersession, or a new Trust Statement.

## Evaluation
Evidence contributes to Rule-Constrained Evaluation but does not independently determine the Evaluation Outcome.

Adopted Evaluation Outcomes:
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

Attestor does not establish a universal:
- evidence weighting system;
- confidence percentage;
- reputation score;
- majority-source rule;
- automatic source hierarchy.

Sufficiency is governed by the applicable purpose, rules, scope, eligible basis, conflicts, limitations, and methodology.

## Validation
Evidence-related Attestations and governed evidence/reference profiles remain subject to applicable Validation requirements.

Validation determines structural/rule compliance.

Evaluation determines substantive outcome.

> **Validation ≠ Evaluation**

Exact executable validation and final Validation Result vocabulary remain implementation work.

## Evidence Profile Architecture
The Attestor schema/template architecture includes an **Evidence Attestation** profile using the adopted Attestation Type:

`evidence`

This profile governs an Attestation about evidence. It does not create a separate canonical Evidence object.

## Retention and Publication
Historical traceability and relevant evidence context should be preserved according to applicable Attestor and source rules.

Publication is separately governed.

Evidence availability or technical accessibility does not automatically make an Attestor object Published.

## Status
**Evidence Architecture → Advanced Architecture reconciled.**

The former posture that evidence classes, eligibility, provenance, conflict treatment, and evaluation contribution were wholly deferred to Advanced Architecture is no longer current.

Remaining work concerns:
- exact machine serialization;
- executable evidence-profile validation;
- production-specific evidence handling;
- retention mechanics where required;
- production evidence and operational proof.

## Files
- `index.html` — public Evidence page.
- `README.md` — repository documentation.
