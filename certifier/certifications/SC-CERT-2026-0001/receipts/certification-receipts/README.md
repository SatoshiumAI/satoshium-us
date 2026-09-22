# Satoshium Certifier — Certification Receipt

**Path:** `/certifier/certifications/SC-CERT-2026-0001/receipts/certification-receipts/`  
**Institution:** Satoshium Certifier  
**Surface:** Certification Receipt (SCR)  
**Status:** Current repository documentation

## Purpose

This directory contains the public **Satoshium Certification Receipt (SCR)** for certification `SC-CERT-2026-0001`.

The Certification Receipt provides concise public confirmation that Satoshium Certifier issued the certification.

The public page for this directory is:

- `index.html`

This README documents the receipt's repository role, authority boundary, relationship to the Certification Package, and verification function. It does not replace the public receipt.

## Receipt Identity

The current receipt confirms:

- **Certification ID:** `SC-CERT-2026-0001`
- **Certification Subject:** Atlas Jurisdiction Record — El Salvador
- **Certification Class:** Operational
- **Certification Status:** Issued · Active
- **Certification Date:** July 5, 2026
- **Receipt Version:** 1.1

The receipt is an SCR representation generated from the canonical Certification Package.

## Canonical Relationship

The governing relationship is:

```text
Certification Package
        ↓
Certification Decision
        ↓
Certification Receipt (SCR)
        ↓
Public Verification
```

The Certification Package remains Certifier's canonical operational record.

The receipt provides concise public confirmation that certification occurred.

It does not replace the full Certification Package.

## Certifier Authority

Satoshium Certifier is the issuing and decision authority for the certification.

The receipt records the certification result but does not create independent certification authority.

The established Suite relationship remains:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

## Certification Confirmation

The receipt records the current certification confirmation as:

- **Certification Outcome:** Certified
- **Certification Status:** Issued · Active
- **Certification Class:** Operational
- **Confidence Posture:** Supported
- **Decision Authority:** Satoshium Certifier
- **Applicable Standards:** Satoshium Suite Standards v1.0
- **Applicable Methodology:** Satoshium Suite Methodology v1.0

These values should remain synchronized with the canonical Certification Package.

## Verification Role

The receipt supports public verification of the fact that the certification was issued.

It should be interpreted together with the Certification Package, which preserves the complete:

- evidence review;
- evaluation;
- findings;
- limitations;
- reasoning; and
- certification decision.

The receipt is therefore a verification surface, not a substitute decision record.

## Relationship to the Certification Package

The Certification Package is authoritative for the certification.

The receipt is downstream from that package.

If any discrepancy exists between the receipt and the Certification Package:

**the Certification Package governs.**

## Related Certifier Artifacts

The receipt references and links to related Certifier artifacts including:

- Certification Package;
- Certification Process Report (SCPR);
- Certified Record (SCRD HTML);
- Certified Record (SCRD JSON);
- Suite Standards;
- Suite Methodology; and
- the Atlas Jurisdiction Record — El Salvador.

These supporting resources help users inspect the certification context.

## Relationship to the Certified Record

The Certified Record / SCRD is a Certifier-produced record associated with the certification.

The Certification Receipt should not be confused with the SCRD.

The distinction is:

```text
SCR
→ concise public confirmation of certification

SCRD
→ structured certified record representation
```

Both remain downstream from the canonical Certification Package.

## Relationship to Suite Architecture

The receipt may be referenced by other Suite institutions where appropriate.

Such references do not transfer Certifier authority.

For example:

- Registry may reference the certification or certified record through a Registry Entry / SREG.
- Chronicle may preserve certification chronology.
- Anchor may preserve an Integrity Reference.
- Beacon may support discovery.
- Attestor may consume eligible governed certification outputs as inputs to Attestation and rule-constrained evaluation.
- Navigator may define or orchestrate workflows involving the certification.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Attestor Boundary

The receipt is not an Attestation.

It is not a Trust Statement.

It is not an Attestor evaluation outcome.

If Attestor later references this receipt or the underlying certification:

```text
Certification Receipt
→ eligible governed input or referenced artifact where permitted

Attestation
→ governed Attestor assertion

Trust Statement
→ bounded Attestor conclusion
```

Those records remain institutionally distinct.

## Version and Historical Discipline

The receipt records:

- original receipt date: July 5, 2026;
- architecture hardening: July 17, 2026;
- receipt version: 1.1.

Historical metadata should remain preserved where accurate.

Current-state edits should not erase the receipt's provenance or version history.

## Repository Expectations

Changes to this directory should preserve:

1. the Certification Package as the canonical operational record;
2. Certifier as the certification authority;
3. the receipt as a public verification surface;
4. synchronization between receipt values and the canonical package;
5. distinction between SCR and SCRD;
6. provenance and version history;
7. separation between certification and Attestor objects; and
8. the rule that reference does not transfer authority.

Changes that would alter the certification outcome, canonical package hierarchy, Certifier authority, or cross-institution object identity require governed architectural review rather than a documentation-only edit.

## Governing Principle

**The Certification Receipt confirms that certification occurred; the Certification Package remains the authoritative certification record.**
