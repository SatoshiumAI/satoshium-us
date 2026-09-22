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

Eligibility requirements for governed inputs are now established by Attestor's Eligibility architecture. External verification-related sources remain architecturally permissible when they satisfy applicable governed requirements, although the first production operation exercised a Suite-source Certification Package rather than an external verification source.

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

Applicable provenance and source-context requirements are now governed by Attestor's Provenance, Records / Reference Profiles, Schemas, Eligibility, and Validation architecture. Specialized requirements remain profile-specific.

## Status and Temporal Context

Verification and certification outcomes can change over time.

An outcome may later be:

- superseded;
- corrected;
- expired;
- withdrawn;
- otherwise changed or affected by new information.

Attestor should preserve the outcome considered at the time of its evaluation and distinguish it from later changes.

Lifecycle, Versioning, Corrections, and Publication now govern the applicable change mechanics. The first production operation preserved the evaluated Certifier state and explicitly bounded the Trust Statement against unsupported claims of unchanged state beyond the evidence reviewed.

## No Automatic Trust Effect

A successful verification or certification does not automatically produce a favorable Trust Statement.

Likewise, the absence or failure of verification does not automatically produce an unfavorable Trust Statement.

The significance of an outcome depends upon the specific assertion, scope, evidence, provenance, status, limitations, and applicable Attestor rules.

Attestor therefore does not treat verification as an automatic trust score.

## Relationship to Trust Signals

The pre-Suite page stated that verification outcomes may become Trust Signals.

That claim is not carried forward as established architecture.

The canonical Attestor output is the **Trust Statement**. A verification-related outcome may be relevant governed input or context without requiring creation of a separate Trust Signal object. The generic Trust Signal model is not the canonical production output.

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

## Operational Resolution of Former Deferrals

The former Advanced Architecture deferrals have now been substantially resolved:

- governed input eligibility → established by Eligibility;
- source classes and reference handling → governed by Records / Reference Profiles and Eligibility;
- provenance representation → governed by Provenance and applicable Schemas;
- source-authority representation → governed by Authority;
- lifecycle and source-state treatment → governed by Lifecycle, Versioning, Corrections, and Publication;
- verification-related Attestation classification → established as `verification-related`;
- sufficiency and conflicting-input treatment → governed by Evaluation and Evidence;
- Validation → operational through Validator v0.5;
- Conformance → operational;
- Trust Statement generation → exercised through the first production operation;
- Schemas → established and production-exercised for canonical ATT/TRST objects.

No universal verification weighting, confidence score, reputation score, or automatic source hierarchy has been adopted.

External verification-related source handling remains architecturally available but was not independently production-tested by the first operation.

## First Production Verification Demonstration

The first controlled production operation directly exercised the Verification architecture through `SC-CERT-2026-0001`, the canonical Satoshium Certifier Certification Package for the Operational certification of the Satoshium Atlas Jurisdiction Record — El Salvador.

The production Attestation was classified:

`ATT-2026-0001 → verification-related`

Attestor evaluated a bounded proposition concerning the Certification Package's canonical identity, attributable Certifier origin, relevant certification state, and traceable Suite relationships.

The production operation preserved:

- Certifier authority over `SC-CERT-2026-0001`;
- Atlas authority over the underlying jurisdiction intelligence;
- the Certifier source representation `Issued · Active` within the evaluated state and scope;
- the distinction between the July 5 certification decision, later package hardening, downstream Suite observations, and the September 19 Attestor evaluation;
- Anchor's integrity scope as applying to its defined SCRD representation rather than the entire Certification Package; and
- the limitation that Beacon's September 13 observation did not independently prove unchanged state through the September 19 evaluation.

The resulting Evaluation Outcome was `supported`, but the bounded Trust Statement did **not**:

- recertify the Certifier decision;
- establish the substantive truth of the underlying Atlas jurisdiction intelligence;
- extend Anchor integrity beyond its governed scope;
- establish unchanged state beyond the evidence reviewed; or
- create a generalized determination of trustworthiness.

`Certification Package → Eligible Governed Input → verification-related Attestation → Rule-Constrained Evaluation → Trust Statement`

**Verification Architecture → DEMONSTRATED IN PRODUCTION**

## Status

**Verification Architecture → Established and Production-Proven for the Certifier verification-related path exercised**

- verification as Attestor canonical responsibility → not adopted
- Certifier canonical responsibility → Certification Package
- Attestor canonical output → Trust Statement
- `verification-related` Attestation Type → production-exercised
- `SC-CERT-2026-0001` as governed verification/certification input → production-exercised
- source authority preservation → demonstrated
- source-state / temporal boundary → demonstrated
- no automatic trust effect → demonstrated
- recertification by Attestor → not performed
- external verification source path → established architecturally; not independently production-tested
- universal verification weighting / scoring → not adopted
- production proof → **ESTABLISHED for the exercised Certifier path**

## Continuing Verification Governance

`Verification ≠ Attestor Canonical Responsibility`

`Certification Package ≠ Trust Statement`

`Verification-Related ≠ Recertification`

`Successful Certification ≠ Automatic Favorable Trust Statement`

`Validation ≠ Evaluation`

`Reference ≠ Support`

**Reference does not transfer authority.**

## Files

- `index.html` — public Verification page.
- `README.md` — repository documentation for the Verification page.
