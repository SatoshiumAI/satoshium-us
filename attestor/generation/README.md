# Satoshium Attestor — Attestation Generation

**Path:** `/attestor/generation/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Architecture  
**Canonical Output:** `ATT-YYYY-NNNN` Attestation  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Attestation Generation defines the governed process by which a bounded trust-relevant matter and attributable assertion become a canonical Attestation.

Generation preserves:

- subject;
- assertion;
- scope;
- Attesting Authority / attribution;
- eligible governed references;
- provenance;
- relevant state;
- relationships;
- limitations and uncertainty where material; and
- institutional authority boundaries.

Generation does not determine whether the assertion is supported.

## Governing Model

`Bounded Matter + Attributable Assertion + Eligible Governed Inputs + Preserved Authority / Provenance → Canonical Attestation`

The resulting Attestation may then participate in:

`Attestation + Evaluation Basis + Applicable Rules → Rule-Constrained Evaluation`

## Canonical Generation Sequence

1. Establish bounded purpose and subject.
2. Define the assertion and scope.
3. Establish Attesting Authority / attribution.
4. Identify potential governed inputs.
5. Preserve source identity, provenance, relevant state, and authority context.
6. Determine Eligibility for the specific evaluation.
7. Associate eligible governed references with the assertion.
8. Preserve material limitations and uncertainty.
9. Create the canonical Attestation.
10. Assign the `ATT-YYYY-NNNN` identifier at canonical creation.
11. Preserve lifecycle, publication, version, provenance, and relationship metadata.
12. Pass the Attestation forward to Evaluation Basis / Rule-Constrained Evaluation.

## Identifier Assignment

The canonical Attestation identifier family is:

`ATT-YYYY-NNNN`

Identifiers are assigned only at canonical creation.

They are not:

- preallocated as production identity;
- assigned to tests or representative fixtures;
- reused;
- transferred from source objects; or
- retroactively substituted for another object's identity.

## Core Distinctions

`Source Object ≠ Attestation`

`Availability ≠ Eligibility`

`Authority ≠ Eligibility`

`Reference ≠ Eligibility`

`Eligibility ≠ Evaluation Outcome`

`Attestation ≠ Trust Statement`

`Canonical Creation ≠ Lifecycle Activation ≠ Publication`

`Reference ≠ Support`

**Reference does not transfer authority.**

## Source Authority

Generation may use eligible governed references to existing Suite or external objects without duplicating their canonical authority.

The source institution remains authoritative for its own object.

Attestor is authoritative for the Attestation it canonically creates.

## First Production Generation Demonstration

The first controlled production operation exercised Attestation Generation through `ATT-2026-0001`.

The governed matter concerned:

> The canonical identity, attributable Certifier origin, relevant certification state, and traceable Suite relationships of `SC-CERT-2026-0001`, the Operational Certification Package concerning the Satoshium Atlas Jurisdiction Record — El Salvador.

The production generation process established:

- bounded purpose and scope;
- potential governed inputs;
- completed Eligibility determinations;
- Attesting Authority / attribution;
- a bounded governed assertion;
- source provenance and authority context;
- traceable governed relationships;
- canonical creation of `ATT-2026-0001`; and
- initial state `Draft · Unpublished · V1.0`.

The Evaluation Outcome was **not predetermined at canonical creation**.

Rule-Constrained Evaluation occurred afterward and ultimately determined the outcome `supported`.

## Production Assertion

`ATT-2026-0001` asserted:

> SC-CERT-2026-0001 is the canonical Satoshium Certifier Certification Package for the Operational certification of the Satoshium Atlas Jurisdiction Record — El Salvador; it is attributable to Satoshium Certifier, is represented by its canonical Certifier source as Issued · Active, and has traceable governed relationships to SREG-2026-0001, CHR-2026-0001, ANCH-2026-0001, and BEAC-2026-0001, while each referenced Suite institution retains authority over its own object and institutional domain.

Canonical creation of this assertion did not establish that the assertion was supported.

Support was determined only through subsequent Rule-Constrained Evaluation.

## Production Authority Preservation

The first production generation preserved institutional boundaries:

- `SC-CERT-2026-0001` → Certifier authority
- `SREG-2026-0001` → Registry authority
- `CHR-2026-0001` → Chronicle authority
- `ANCH-2026-0001` → Anchor authority
- `BEAC-2026-0001` → Beacon authority
- `ATT-2026-0001` → Attestor authority

No source object became an Attestor-owned source record merely because it participated in Attestation Generation.

## Generation and Evaluation

Attestation Generation and Evaluation are distinct institutional acts.

`Generation → Creates the governed assertion`

`Evaluation → Determines what the eligible governed evidence supports`

Generation must not encode a desired Evaluation Outcome.

## Generation and Later Governance

Canonical creation begins the governed history of an Attestation.

Later actions remain separate:

- Validation;
- governed Review;
- Conformance;
- lifecycle activation;
- Publication;
- correction;
- supersession; and
- material-trigger review.

`Creation ≠ Activation ≠ Publication`

## Status

**Attestation Generation Architecture → Established**

**Production Attestation Generation → Operationally Demonstrated**

- canonical generation sequence → established
- Eligibility boundary → established and demonstrated
- attribution → established and demonstrated
- source provenance → preserved
- authority boundaries → preserved
- governed relationships → preserved
- canonical identifier assignment → demonstrated
- creation / Evaluation separation → demonstrated
- creation / activation / Publication separation → demonstrated
- `ATT-2026-0001` → first canonical production Attestation generated
- production generation proof → **ESTABLISHED**

## Continuing Generation Governance

The first production operation establishes a baseline for governed Attestation Generation.

It does not make future Attestations automatically eligible, valid, conformant, active, published, or supported.

Each future Attestation must be generated and governed according to its own purpose, scope, inputs, attribution, provenance, authority context, and applicable requirements.

## Landing-Page Integration

The Attestor landing page should include this page in its architecture/navigation surface:

`/attestor/generation/`

Recommended label:

**Attestation Generation**

## Files

- `index.html` — public Attestation Generation page.
- `README.md` — repository documentation.
