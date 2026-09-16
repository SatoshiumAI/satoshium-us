# Satoshium Attestor — Evidence

## Page

`/attestor/evidence/`

## Purpose

This page defines the role of **Evidence** within Satoshium Attestor.

Evidence is supporting material or an authoritative reference used by Attestor to evaluate an Attestation and support a **Trust Statement**.

Evidence remains distinct from the Attestation, the Trust Statement, and the authority of any referenced source.

## Governing Principle

> **Reference does not transfer authority.**

Attestor may use or reference evidence without becoming the canonical authority for that evidence.

A Suite object referenced as evidence remains authoritative within its originating institution.

## Evidence Model

At the current foundational stage, evidence may conceptually include:

- documents;
- records;
- datasets;
- media;
- source materials;
- observations;
- authoritative Suite objects;
- other information later determined eligible under Attestor rules.

This list is descriptive, not a final controlled taxonomy.

The advanced Attestor architecture must determine the actual evidence classes and eligibility rules.

## Authoritative Suite References

Attestor may reference authoritative Suite objects when relevant to an Attestation or Trust Statement.

Examples include:

- Certifier Certification Packages;
- Satoshium Registry records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals or Discovery Metadata;
- Atlas intelligence;
- Navigator workflow context;
- other governed Suite inputs.

Their use as evidence does not transfer their authority to Attestor.

## Provenance

Evidence should preserve sufficient provenance for a reviewer to determine, as applicable:

- source or origin;
- attribution;
- relationship to the subject;
- relationship to the Attestation;
- status when evaluated;
- relevant changes;
- limitations;
- applicable source authority.

The exact required provenance fields are deferred to advanced architecture.

## Relevance and Scope

Evidence is meaningful in relation to a specific assertion and scope.

Evidence that supports one bounded assertion should not automatically be treated as supporting a broader conclusion.

Attestor should therefore preserve the relationship among:

`Evidence → Assertion → Scope → Evaluation`

## Supporting and Conflicting Evidence

The architecture should not preserve only evidence favorable to a conclusion.

Attestor must be capable of representing evidence that:

- supports;
- limits;
- qualifies;
- contextualizes;
- conflicts with

an assertion, subject to the eventual controlled evidence model and evaluation rules.

## Evidence Status

Evidence may change over time.

Availability, authority, validity, interpretation, provenance, or relevance may later differ from what existed when an Attestation was evaluated.

Attestor should preserve enough context to explain what evidence was considered when a Trust Statement was produced without rewriting the original evaluation merely because later information changes.

The exact lifecycle and historical treatment remain to be defined.

## Evidence Is Not an Attestation

The reconciled architecture explicitly separates evidence from Attestations.

- **Evidence** supplies support or context.
- **Attestation** expresses a governed Attestor assertion.
- **Trust Statement** is Attestor's canonical institutional output.

Conceptually:

`Evidence / Authoritative References → Attestation Evaluation → Trust Statement`

## Reconciliation Notes

This revision updates the June-era pre-Suite Evidence page.

Major changes include:

- replacing the broad “trust context” framing with Attestor's Suite-specific Trust Statement function;
- removing the assumption that Attestor will necessarily create independent “Evidence Records”;
- removing “Evidence Attestations” as an already planned architectural object because the Attestation Types taxonomy remains under review;
- strengthening source authority and provenance requirements;
- distinguishing evidence from Attestations;
- adding relevance and scope as explicit architectural concerns;
- adding support for conflicting or qualifying evidence;
- adding evidence status and temporal context as lifecycle concerns;
- distinguishing authoritative Suite references from Attestor-owned objects;
- preserving the principle that evidence does not automatically establish truth;
- avoiding premature evidence schemas, controlled values, identifiers, or validation rules.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- canonical evidence taxonomy;
- evidence eligibility rules;
- required and optional evidence fields;
- evidence identifiers, if any;
- whether Attestor creates evidence-reference objects;
- provenance schema;
- evidence status vocabulary;
- evidence validation rules;
- conflicting-evidence treatment;
- weighting or sufficiency rules, if appropriate;
- evidence retention and availability requirements;
- evidence-to-Attestation relationship schema;
- evidence-to-Trust-Statement generation rules;
- conformance tests and reference vectors.

## Files

- `index.html` — public Evidence page.
- `README.md` — repository documentation for the Evidence page.
