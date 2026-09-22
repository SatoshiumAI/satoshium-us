# Satoshium Certifier — Certified Record

**Path:** `/certifier/certifications/SC-CERT-2026-0001/records/certified-record/`  
**Institution:** Satoshium Certifier  
**Surface:** Satoshium Certified Record (SCRD)  
**Status:** Current repository documentation

## Purpose

This directory contains the human-readable **Satoshium Certified Record (SCRD)** for certification `SC-CERT-2026-0001`.

The SCRD communicates the certification result in a durable public form while remaining traceable to the canonical Certification Package and related Certifier artifacts.

The public page for this directory is:

- `index.html`

The corresponding machine-readable representation is:

- `scrd_json.json`

This README documents the Certified Record's repository role, canonical hierarchy, authority boundary, representation model, and Suite relationships.

## Record Identity

The current Certified Record identifies:

- **Certification ID:** `SC-CERT-2026-0001`
- **Certification Subject:** Atlas Jurisdiction Record — El Salvador
- **Subject System:** Satoshium Atlas
- **Subject Type:** Jurisdiction Intelligence Engine Record
- **Certification Date:** July 5, 2026
- **Record Version:** 1.1

## Canonical Relationship

The SCRD is generated from the canonical Certification Package.

The governing hierarchy is:

```text
Certification Package
        ↓
Certification Decision
        ↓
Generated Certifier Artifacts
        ↓
Certified Record (SCRD)
```

The Certification Package remains Certifier's canonical operational record.

The SCRD communicates the certification result but does not supersede or replace the Certification Package.

## Certification Result

The Certified Record preserves the public certification result:

- **Certification Outcome:** Certified
- **Certification Status:** Issued · Active
- **Certification Class:** Operational
- **Confidence Posture:** Supported
- **Decision Authority:** Satoshium Certifier
- **Applicable Standards:** Satoshium Suite Standards v1.0
- **Applicable Methodology:** Satoshium Suite Methodology v1.0

These values should remain synchronized with the canonical Certification Package.

## Historical Assessment Data

The record preserves historical prototype assessment information including:

- numerical prototype assessment;
- prototype trust level; and
- operational confidence posture.

The numerical score and prototype trust level are historical assessment data.

They do not replace the authoritative current classification:

**Operational Certification Class**

Historical assessment data should remain preserved as historical evidence rather than silently converted into current Suite trust semantics.

## Scope and Limitations

This certification applies only to the Atlas Jurisdiction Intelligence Engine record for El Salvador as it existed within the certification boundary on July 5, 2026 and to the Evidence Records identified by the Certification Package.

Future changes to the underlying Atlas record may require review or recertification.

The SCRD does not independently certify every supporting file.

It also does not transfer authority over the underlying jurisdiction intelligence away from Satoshium Atlas.

## Representation Model

The Certified Record has two representations:

```text
SCRD
├── SCRD HTML
└── SCRD JSON
```

The HTML and JSON are representations of the same Certified Record.

Neither representation independently outranks the Certification Package.

If a discrepancy exists between either SCRD representation and the Certification Package:

**the Certification Package governs.**

## Relationship to the Certification Receipt

The Certification Receipt (SCR) and Certified Record (SCRD) are distinct Certifier artifacts.

```text
SCR
→ concise public confirmation that certification occurred

SCRD
→ durable structured representation of the certified result
```

Both remain downstream from the Certification Package.

## Relationship to the Certification Process Report

The Certification Process Report (SCPR) documents the certification process.

The SCRD communicates the resulting certified record.

These are related but distinct artifacts.

## Relationship to Atlas

The certification subject belongs to Satoshium Atlas.

Certifier evaluates the defined certification subject under Suite Standards and Suite Methodology.

Certification does not transfer ownership or authority over the underlying Atlas jurisdiction record to Certifier.

Atlas remains authoritative for the underlying jurisdiction intelligence.

## Relationship to Registry

Registry may create a Registry Entry / SREG referencing the Certified Record or related governed source records.

That reference does not make Registry the source authority for the SCRD.

## Relationship to Chronicle

Chronicle may preserve governed chronology associated with the certification.

Chronicle records when.

It does not replace the Certified Record or Certification Package.

## Relationship to Anchor

Anchor may preserve an Integrity Reference associated with the SCRD or related certification artifact.

Anchor preserves integrity and reference relationships without becoming the certification authority.

## Relationship to Beacon

Beacon may publish Discovery Signals / Discovery Metadata that help surface governed Suite records.

Discovery does not alter certification authority.

## Relationship to Attestor

Attestor may consume eligible governed certification outputs as inputs under its own rules.

The current Attestor architecture is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

The SCRD is not an Attestation.

It is not a Trust Statement.

An Attestor record that references the SCRD remains institutionally distinct.

## Authority Discipline

This directory should preserve the following distinctions:

- Certification Package ≠ Certified Record
- SCR ≠ SCRD
- SCRD HTML ≠ separate canonical object from SCRD JSON
- Certification Decision ≠ Attestation
- Certification Decision ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity
- Supported ≠ universal truth
- Historical trust terminology ≠ current Attestor Trust Statement

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Version and Historical Discipline

The current record preserves:

- original record date: July 5, 2026;
- architecture hardening: July 17, 2026;
- record version: 1.1.

Historical prototype scoring and trust terminology should remain identifiable as historical assessment data.

Current-state documentation should not present legacy assessment terminology as the governing Attestor model.

## Repository Expectations

Changes to this directory should preserve:

1. the Certification Package as the canonical operational record;
2. the SCRD as a downstream Certified Record;
3. parity between SCRD HTML and SCRD JSON;
4. Certifier as certification authority;
5. Atlas authority over the underlying jurisdiction record;
6. historical assessment provenance;
7. separation between Certifier and Attestor objects;
8. current Suite object terminology; and
9. the rule that reference does not transfer authority.

Changes that would alter the certification result, canonical hierarchy, representation identity, or cross-institution authority require governed architectural review rather than a documentation-only edit.

## Governing Principle

**The Certified Record preserves the durable public certification result while the Certification Package remains Certifier's canonical operational record.**
