# Satoshium Certifier — Definitions

**Path:** `/certifier/definitions/`  
**Institution:** Satoshium Certifier  
**Surface:** Definitions  
**Status:** Current repository documentation

## Purpose

This directory contains the **Satoshium Certifier Definitions** surface.

It establishes the shared terminology used by Certifier for certification subjects, Certification Packages, generated artifacts, evidence records, and governed Suite relationships.

The public page for this directory is:

- `index.html`

This README documents the terminology role, canonical Certifier terms, cross-institution object boundaries, and terminology-governance expectations for this directory.

## Definitions Role

Definitions provide Certifier's terminology layer.

They support consistency across:

- certification records;
- reports;
- receipts;
- evidence references;
- schemas;
- generated artifacts; and
- governed Suite integrations.

Definitions do not independently create certification authority.

They preserve shared meaning so Certifier can apply Suite Standards and Suite Methodology consistently.

## Governing Relationship

The current Certifier foundation remains:

```text
Suite Standards
        ↓
Suite Methodology
        ↓
Certification Subject
        ↓
Certification Package
        ↓
Generated Certifier Artifacts
        ↓
Governed Suite References
```

The established rule remains:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

## Certification Package

The **Certification Package** is Certifier's canonical operational record.

It preserves the governed certification context including:

- Certification Subject;
- Profile;
- Scope;
- Evidence inventory;
- applicable Suite Standards;
- applicable Suite Methodology;
- evaluation;
- certification decision;
- generated artifacts; and
- certification history.

## Generated Artifacts

Generated Certifier artifacts include:

- **SCPR** — Satoshium Certification Process Report;
- **SCR** — Satoshium Certification Receipt;
- **SCRD HTML** — human-readable Certified Record representation; and
- **SCRD JSON** — machine-readable Certified Record representation.

These artifacts are generated from the Certification Package.

They do not replace the Certification Package as the canonical operational record.

## Evidence Record

An **Evidence Record** preserves factual material supporting certification review.

Evidence may include URLs, screenshots, reports, hashes, notes, supporting documentation, evidence mappings, and other governed review artifacts.

Evidence supports certification evaluation.

Evidence does not itself create the certification decision.

## Certification Subject

A **Certification Subject** is the operational object selected for certification.

It becomes the focus of a Certification Package after its Profile, Scope, and Evidence have been defined under Suite Standards and Suite Methodology.

Certification does not transfer authority over the underlying subject away from the originating institution.

## Current Core Term Map

### SCPKG

**Certification Package** — Certifier's canonical operational record for a certification.

### SCPR

**Satoshium Certification Process Report** — the detailed process and reasoning report generated from the Certification Package.

### SCR

**Satoshium Certification Receipt** — the concise public verification summary generated from the Certification Package.

### SCRD

**Satoshium Certified Record** — the Certified Record represented in HTML and JSON forms.

### SEV

**Satoshium Evidence Record** — preserved evidence supporting certification review.

### SREG

**Satoshium Registry Entry** — the Registry's canonical operational record referencing governed source records where applicable.

Registry references do not transfer source authority.

### CHR

**Chronicle Entry** — the governed Chronicle record preserving chronology.

Chronicle records when.

### ANCH

**Integrity Reference** — Anchor's canonical integrity-preservation object.

Anchor preserves integrity without becoming source authority for the referenced record.

### ATT

**Attestation** — a governed, attributable assertion produced by Satoshium Attestor.

### TRST

**Trust Statement** — a governed, attributable, bounded conclusion produced by Attestor through rule-constrained evaluation.

## Attestor Boundary

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

Legacy `SATR / Satoshium Attestation Record` terminology is no longer the current Attestor object model.

Current-state Certifier documentation should therefore use `ATT` and `TRST` where Attestor objects are referenced.

Historical artifacts that accurately preserve earlier terminology may remain historical.

## Suite Reference Relationships

Certifier outputs may participate in governed relationships with other Suite institutions.

Examples include:

- Registry → SREG
- Chronicle → CHR
- Anchor → ANCH
- Beacon → Discovery Signal / Discovery Metadata
- Attestor → ATT / TRST
- Navigator → workflow definition / orchestration

These are cross-institution relationships.

They should not be described as if Certifier owns the downstream institution's canonical object.

## Authority Discipline

This directory should preserve the following distinctions:

- Definition ≠ authority
- Certification Package ≠ generated artifact
- SCR ≠ SCRD
- SCRD HTML ≠ separate canonical object from SCRD JSON
- SREG ≠ source record
- CHR ≠ certification record
- ANCH ≠ certification authority
- ATT ≠ certification decision
- TRST ≠ certification class
- Reference ≠ derivation
- Reference ≠ support
- Connection ≠ identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Relationship to Suite Standards

Suite Standards remain the Suite-wide expectations layer.

Certifier Definitions should remain aligned with Suite terminology but should not silently redefine Suite-wide standards.

Where a term is Suite-wide rather than Certifier-specific, the governing Suite source should remain authoritative.

## Relationship to Suite Methodology

Suite Methodology defines implementation and repeatable process.

Certifier Definitions should describe terms used by that process without replacing the Methodology itself.

## Terminology Governance

Current-state terminology should remain synchronized across:

- Certifier Definitions;
- Certifier Schema;
- Certification Packages;
- SCPR;
- SCR;
- SCRD;
- Suite Standards;
- Suite Methodology; and
- governed downstream references.

Stale object names should be corrected when the current canonical object model is already established.

Historical names should remain identifiable as historical where they are preserved for provenance.

## Suite Reconciliation Considerations

The following should be reviewed during Suite Reconciliation rather than redesigned in this documentation pass:

1. whether Certifier Definitions should continue to be described as Certifier's **canonical language layer** when Suite-wide terminology is also governed by Suite Standards;
2. whether `SCPKG` should remain the preferred abbreviation for Certification Package;
3. how Certifier-specific evidence terms such as `SEV` relate to broader Suite evidence terminology; and
4. how Suite reference terminology should distinguish direct object identity from references to external institutional records.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier terminology consistency;
2. the Certification Package as Certifier's canonical operational record;
3. distinction between generated artifacts and canonical package;
4. current Suite object names;
5. separation of institutional authority;
6. historical terminology provenance;
7. alignment with Suite Standards and Methodology; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Definitions preserve shared meaning; they do not create institutional authority or collapse distinct Suite objects into one terminology layer.**
