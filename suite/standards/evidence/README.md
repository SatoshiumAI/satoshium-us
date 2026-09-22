# Satoshium Evidence Standard

**Path:** `/suite/standards/evidence/`  
**Surface:** Satoshium Suite · Standards · Evidence  
**Status:** Current repository documentation

## Purpose

This directory documents the **Satoshium Evidence Standard**, the Suite-wide standards layer governing how evidence is recognized, described, preserved, evaluated, and used.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Standard Role

The Satoshium Evidence Standard defines Suite-wide expectations for evidence.

Within the Suite architecture:

- **Standards define expectations.**
- **Methodology defines implementation.**
- **Suite institutions perform their own governed operations.**

The Evidence Standard therefore defines the expectations under which evidence-related methodology and institutional processes operate. It does not independently evaluate evidence, issue certification decisions, create attestations, establish trust statements, or transfer source authority.

## Evidence Types

The current standards surface recognizes multiple categories of evidence, including:

- primary sources;
- secondary sources;
- institutional records;
- self-attestations;
- cryptographic records;
- metadata;
- screenshots;
- archives;
- media;
- receipts; and
- witness statements.

Evidence type alone does not determine evidentiary weight, authority, sufficiency, or evaluation outcome.

## Evidence Quality

Evidence may be assessed according to characteristics such as:

- authority;
- independence;
- completeness;
- authenticity;
- timeliness;
- reproducibility;
- traceability; and
- resistance to alteration or misinterpretation.

These characteristics support governed evaluation.

They do not independently establish truth, certification, conformance, publication, or trust.

## Evidence Requirements

The current standards surface links to:

- `/suite/methodology/evidence-requirements/`

That methodology surface defines how the Evidence Standard is operationalized in certification-related evidence handling.

Standards define the expectation.

Methodology defines how that expectation is implemented.

## Evidence Integrity

Evidence should preserve sufficient integrity and provenance so later reviewers can determine what was evaluated and from where it originated.

Integrity mechanisms may include governed use of:

- references;
- hashes;
- timestamps or time-associated information;
- version information;
- source metadata;
- preservation records; and
- supporting relationships.

Integrity does not transfer source authority.

An integrity reference does not become the underlying evidence object.

## Evidence Sufficiency

The Evidence Standard may define expectations for determining when available evidence is sufficient for a governed process and when additional evidence is required.

Sufficiency must remain bounded to the process applying it.

Evidence sufficient for one governed decision is not automatically sufficient for another institution, rule set, or canonical conclusion.

## Evidence Limitations

Uncertainty and evidentiary limitations should be disclosed rather than hidden.

Relevant limitations may include:

- incomplete records;
- conflicting sources;
- stale evidence;
- unverifiable materials;
- unsupported claims;
- missing provenance; and
- unresolved uncertainty.

Documentation of limitations supports transparency and reviewability.

## Evidence Record Structure

Evidence records may require common descriptive fields such as:

- source;
- evidence type;
- authority;
- date;
- relationship to the governed subject or assertion;
- preservation status;
- review notes; and
- public reference where appropriate.

A structured evidence record describes evidence.

It does not replace the source record or inherit source authority.

## Relationship to Certifier

Certifier applies governed evidence standards and methodology within certification operations.

Certifier may evaluate evidence for certification purposes, but the Evidence Standard itself does not make certification decisions.

Evidence referenced by Certifier retains its source authority.

## Relationship to Anchor

Anchor establishes integrity references according to its own institutional role.

Anchor does not become the source authority for evidence merely because evidence or an evidence-related object is referenced by an Anchor record.

Integrity reference is distinct from evidence ownership and substantive evaluation.

## Relationship to Registry

Registry may create canonical Registry objects that reference evidence or evidence-related source records.

Registry does not become the source authority for referenced evidence.

Reference does not transfer authority.

## Relationship to Beacon

Beacon provides discovery signals and discovery metadata.

Discovery of evidence-linked objects does not create evidentiary authority, derivation, or support.

## Relationship to Navigator

Navigator owns workflow definition and orchestration.

Navigator may coordinate or query governed evidence-related workflow information where appropriate.

Workflow orchestration does not transfer evidence authority.

## Relationship to Attestor

Attestor operates under its own canonical flow:

Eligible Governed Inputs  
→ Attestation  
→ Rule-Constrained Evaluation  
→ Trust Statement

Evidence may support Attestor operations where eligible and governed, but the Evidence Standard does not itself create an Attestation or Trust Statement.

An Attestor Trust Statement remains a bounded, attributable Attestor conclusion.

Evidence support and trust conclusion must not be collapsed into a single concept.

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
- reference does not equal derivation;
- reference does not equal support;
- connection does not equal identity; and
- reference does not transfer authority.

## Historical Discipline

Evidence-related standards and methodology may evolve over time, but earlier governed records should remain historically accurate.

Corrections, supersession, preservation, and versioning should follow the applicable governed process.

Correction is not deletion.

Supersession is not mutation.

## Repository Expectations

Changes to this directory should preserve:

1. the distinction between standards and methodology;
2. evidence provenance and source authority;
3. the distinction between evidence support and certification outcome;
4. the distinction between evidence support and Attestor Trust Statements;
5. institutional authority boundaries;
6. historical accuracy; and
7. consistency with the governing Suite architecture.

Changes that would redefine evidence-support semantics, institutional responsibilities, truth claims, or Attestor trust relationships require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Evidence makes governed claims reviewable, but evidence reference never transfers source authority.**
