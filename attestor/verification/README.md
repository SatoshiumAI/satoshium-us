# Satoshium Attestor — Verification

## Page

`/attestor/verification/`

## Purpose

This page defines how **verification, validation, certification, and review outcomes** relate to Satoshium Attestor.

Verification is not Attestor's canonical responsibility.

Attestor may reference governed verification-related outcomes when they are relevant to evaluating an Attestation and producing a **Trust Statement**.

## Canonical Boundary

The reconciled page replaces the pre-Suite shorthand:

`Certifier → Verification`
`Attestor → Trust`

with the current canonical responsibilities:

**Certifier → Certification Package**

**Attestor → Trust Statement**

This distinction matters because “verification” is an activity or outcome that may exist in multiple governed contexts. It should not be treated as Attestor's object, nor should Certifier's canonical responsibility be reduced to a generic verification label.

## Governing Principle

> **Reference does not transfer authority.**

When Attestor references a verification, validation, certification, or review outcome, that outcome retains the meaning, scope, provenance, status, and authority established by its originating process.

## Relationship to Certifier

Certifier owns its Certification Packages and the certification process that produces them.

Attestor may use a Certification Package as an authoritative input when relevant, but Attestor does not:

- issue the Certification Package;
- recertify the subject;
- redefine the certification;
- inherit Certifier's authority;
- convert certification automatically into a Trust Statement.

Conceptually:

`Certification Package → Attestor Evaluation → Trust Statement`

## Verification Beyond Certifier

The page intentionally does not claim that every verification-related input must originate with Certifier.

External or other governed processes may eventually provide eligible verification, validation, or review outcomes.

Advanced Attestor architecture must determine the eligibility requirements for such sources.

Their inclusion does not transfer their authority to Attestor.

## Evidence and Provenance

A verification-related outcome may depend upon:

- evidence;
- standards;
- procedures;
- records;
- source attribution;
- defined scope;
- an originating authority.

Attestor should preserve enough provenance to understand the outcome being referenced and the boundary in which it applies.

The exact required fields remain deferred.

## Status and Temporal Context

Verification and certification outcomes can change over time.

An outcome may later be:

- superseded;
- corrected;
- expired;
- withdrawn;
- otherwise changed or affected by new information.

Attestor should preserve the outcome considered at the time of its evaluation and distinguish it from later changes.

The exact lifecycle mechanics remain part of advanced architecture.

## No Automatic Trust Effect

A successful verification or certification does not automatically produce a favorable Trust Statement.

Likewise, the absence or failure of verification does not automatically produce an unfavorable Trust Statement.

The significance of an outcome depends upon the specific assertion, scope, evidence, provenance, status, limitations, and applicable Attestor rules.

Attestor therefore does not treat verification as an automatic trust score.

## Relationship to Trust Signals

The pre-Suite page stated that verification outcomes may become Trust Signals.

That claim is not carried forward as established architecture.

The reconciled Trust Signals page treats “trust signal” only as descriptive trust-relevant evaluation context pending advanced architectural review. A verification outcome may therefore be relevant context without requiring creation of a separate Trust Signal object.

## Reconciliation Notes

This revision updates the June-era pre-Suite Verification page.

Major changes include:

- removing the broad comparison of “verification” versus “trust” as two parallel evaluation systems;
- establishing verification-related outcomes as possible **inputs** to Attestor rather than Attestor-owned outputs;
- replacing `Certifier → Verification` with the canonical `Certifier → Certification Package`;
- replacing `Attestor → Trust` with `Attestor → Trust Statement`;
- removing the claim that verification outcomes become Trust Signals;
- removing reputation as part of Attestor's established verification architecture;
- adding explicit source-authority boundaries;
- adding scope, provenance, status, and temporal context;
- allowing for eligible verification-related outcomes outside Certifier without assigning their authority to Attestor;
- establishing that verification has no automatic favorable or unfavorable effect on a Trust Statement;
- avoiding premature verification scoring, weighting, eligibility rules, or machine vocabulary.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- eligibility rules for external verification outcomes;
- recognized verification or validation source classes;
- required provenance fields;
- source-authority representation;
- status vocabulary;
- expiration and supersession treatment;
- relationship between verification outcomes and Attestation Types;
- sufficiency rules;
- weighting, if any;
- conflicting verification outcomes;
- validation of referenced outcomes;
- Trust Statement generation rules;
- schemas;
- conformance tests and reference vectors.

## Files

- `index.html` — public Verification page.
- `README.md` — repository documentation for the Verification page.
