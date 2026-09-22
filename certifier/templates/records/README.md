# Satoshium Certifier — Record Templates

**Path:** `/certifier/templates/records/`  
**Institution:** Satoshium Certifier  
**Surface:** Record Template Documentation  
**Status:** Current repository documentation

## Purpose

This directory contains record-oriented templates used by **Satoshium Certifier** and related interoperability documentation.

The directory currently contains:

- `attestation-template.md`
- `certification-receipt-template.md`
- `certification-record-template.json`
- `certification-report-template.md`
- `registry-entry-template.md`

This README serves as the repository entry point for the record-template set.

## Role of the Record Template Layer

Record templates define expected structures for recurring Certifier outputs and interoperability artifacts.

Templates may support:

- consistent field naming;
- repeatable document structure;
- repository implementation;
- machine-readable serialization;
- public artifact generation;
- cross-institution references; and
- future versioned evolution.

A template does not create institutional authority by itself.

## Certification Receipt Template

`certification-receipt-template.md` documents the expected structure of the **Certification Receipt (SCR)**.

The SCR is a concise public confirmation generated from the canonical Certification Package.

The template should remain subordinate to the Certification Package.

## Certification Record Template

`certification-record-template.json` documents a structured representation for the **Certified Record (SCRD)**.

Where HTML and JSON represent the same Certified Record, they should remain synchronized as representations of one governed object.

The JSON template should not create a second canonical certification object.

## Certification Report Template

`certification-report-template.md` documents the expected structure of the **Certification Process Report (SCPR)**.

The SCPR preserves the reasoning and review process associated with the certification decision.

The report template does not replace the canonical Certification Package.

## Registry Entry Template

`registry-entry-template.md` documents interoperability with the Satoshium Registry.

The current Registry architecture is:

```text
Registry
        ↓
Registry Entry / SREG
        ↓
Registry Record Type
        ↓
Source Record
```

A Registry Entry is owned by Registry.

Certifier may prepare or document information needed for Registry integration, but Certifier does not own the canonical SREG object.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Attestation Template

`attestation-template.md` should be treated carefully because Attestor is now operational and its current canonical architecture is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

The current Attestor canonical objects include:

- **ATT** — Attestation
- **TRST** — Trust Statement

Any Certifier-side template related to Attestor should support governed interoperability without redefining Attestor's object model or authority.

Legacy `SATR` terminology should not be treated as the current Attestor architecture.

## Canonical Certifier Boundary

The Certification Package remains Certifier's canonical operational record.

Record templates may help produce or document:

- SCPR;
- SCR;
- SCRD;
- evidence-related records; and
- governed interoperability references.

Templates remain downstream from the governing certification architecture.

## Cross-Institution Boundaries

This directory touches multiple Suite institutions, so boundaries must remain explicit.

### Registry

Registry owns SREG.

Certifier may prepare data or references suitable for Registry consumption.

### Attestor

Attestor owns ATT and TRST.

Certifier should not create those objects merely by filling out a local template unless operating through the governed Attestor process.

### Chronicle

Chronicle owns Chronicle Entries.

Certifier templates may preserve chronology references but do not create Chronicle authority.

### Anchor

Anchor owns Integrity References.

Hashes or integrity fields inside Certifier records do not automatically become Anchor objects.

### Beacon

Beacon owns Discovery Signals / Discovery Metadata.

Certifier templates may expose discoverable metadata without creating Beacon objects.

### Navigator

Navigator owns workflow definition / orchestration responsibilities.

Templates may be consumed by Navigator without changing Certifier authority.

## Template Versioning

Templates should be versioned when substantive structural changes occur.

Versioning should preserve:

- field meaning;
- object identity;
- historical interpretability;
- schema compatibility; and
- provenance.

A revised template should not silently redefine previously issued records.

## Authority Discipline

This directory should preserve the following distinctions:

- Template ≠ Canonical Record
- Template ≠ Certification Decision
- SCR Template ≠ SCR instance
- SCRD Template ≠ SCRD instance
- Report Template ≠ SCPR instance
- Registry Template ≠ SREG authority
- Attestation Template ≠ ATT authority
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Reconciliation Note

This README documents the directory structure visible in the repository and the currently established Suite architecture.

The five individual template files have not yet been independently reconciled in this directory-level pass.

Later file-by-file review should check for:

- legacy `SATR` terminology;
- stale Chronicle or Anchor object names;
- outdated Attestor status language;
- Registry ownership ambiguity;
- template fields that imply canonical authority;
- outdated lifecycle language;
- duplicate-object assumptions across HTML / JSON / Markdown forms; and
- obsolete Suite institution relationships.

## Repository Expectations

Changes to this directory should preserve:

1. the Certification Package as Certifier's canonical operational record;
2. templates as structural aids rather than authority;
3. current Registry and Attestor object boundaries;
4. object identity across representations;
5. historical template versioning;
6. cross-institution ownership boundaries; and
7. the rule that reference does not transfer authority.

## Governing Principle

**Templates define expected structure; they do not create institutional authority or redefine the canonical objects they describe.**
