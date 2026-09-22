# Satoshium Atlas — Certification

**Path:** `/atlas/certification/`  
**Public page:** `index.html`  
**Role:** Atlas Certification Library  
**Status:** Active

## Purpose

The `/atlas/certification/` directory defines how **Satoshium Atlas records participate in the Satoshium Suite certification ecosystem**.

This library explains:

- how Atlas records become certification subjects;
- how certification scope is bounded;
- how supporting evidence is identified;
- how Atlas certification profiles are defined;
- how Certifier applies Suite Standards and Suite Methodology;
- how certification outputs relate to downstream Suite institutions.

Atlas remains authoritative for Atlas intelligence.

Certifier remains authoritative for certification.

## Institutional Boundary

Atlas and Certifier have separate responsibilities.

```text
Atlas
→ creates and maintains authoritative intelligence

Certifier
→ evaluates defined certification subjects
→ applies Suite Standards and Suite Methodology
→ produces Certification Packages and related certification artifacts
```

Certification does not transfer Atlas authority to Certifier.

Likewise, Atlas participation in certification does not make Atlas the certification authority.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Library Structure

The current Atlas Certification Library includes:

### Atlas Certification Framework

Defines how Atlas participates in the Suite certification ecosystem while preserving the separate responsibilities of Atlas, Certifier, and the broader Suite.

Path:

```text
/atlas/certification/atlas-certification-framework/
```

### Atlas Certification Profile

Documents the evaluation characteristics used to assess Atlas records, including:

- identity;
- structure;
- metadata;
- evidence;
- traceability;
- trust dimensions;
- signals;
- completeness;
- reproducibility.

Path:

```text
/atlas/certification/atlas-certification-profile/
```

### Atlas Certification Scope

Defines the certification boundary around an Atlas subject.

It also distinguishes the Atlas record from downstream objects owned by:

- Registry;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator.

Path:

```text
/atlas/certification/atlas-certification-scope/
```

### Atlas Certification Subjects

Defines which Atlas records may serve as certification subjects and distinguishes the complete intelligence record from supporting artifacts such as:

- evidence;
- metadata;
- signals;
- trust dimensions;
- change history.

Path:

```text
/atlas/certification/atlas-certification-subjects/
```

### Atlas Certification Evidence

Defines the role of supporting materials in Atlas certification, including:

- preserved source material;
- metadata;
- signals;
- trust dimensions;
- public pages;
- historical record context.

Path:

```text
/atlas/certification/atlas-certification-evidence/
```

## Suite Foundations

Atlas certification is governed by Suite-wide foundations.

```text
Suite Standards
→ define expectations

Suite Methodology
→ defines implementation approach

Certifier
→ performs certification
```

The relevant public foundations are:

```text
/suite/standards/
/suite/methodology/
```

Atlas certification documentation should not redefine Suite Standards or Suite Methodology locally.

## Certification Flow

The current public flow is:

```text
Atlas Record
↓
Certification Subject
↓
Profile
↓
Scope
↓
Evidence
↓
Certification Package
↓
SCPR · SCR · SCRD HTML / JSON
↓
Registry · Chronicle · Anchor · Attestor
```

This flow is a governed relationship path.

It is not an authority hierarchy.

## Canonical Responsibility

The governing institutional responsibilities remain:

```text
Atlas
→ authoritative intelligence

Certifier
→ Certification Package and certification determination

Registry
→ Satoshium Registry Record

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Beacon
→ Discovery Signal / Discovery Metadata

Attestor
→ Attestation + Rule-Constrained Evaluation + Trust Statement

Navigator
→ Workflow Definition / Orchestration
```

Each institution remains authoritative for its own canonical objects and processes.

## Supporting Artifacts vs. Certification Subject

An Atlas certification subject may be supported by multiple Atlas artifacts.

Supporting artifacts do not automatically become independent certification subjects.

Examples may include:

- evidence records;
- metadata;
- signals;
- trust dimensions;
- historical context;
- public representations.

The certification scope determines what is actually being evaluated.

## Downstream Relationships

Certification outputs may be referenced or consumed by other Suite institutions.

Examples include:

- Registry cataloging certified outputs;
- Chronicle preserving historical context;
- Anchor preserving integrity;
- Beacon supporting discovery;
- Attestor performing bounded attestation or evaluation;
- Navigator orchestrating workflows.

These relationships do not merge institutional identity.

**Connection ≠ Identity.**  
**Reference ≠ Derivation.**  
**Reference ≠ Support.**  
**Reference ≠ Authority Transfer.**

## Public Landing Page

`index.html` is the principal public entry point for the Atlas Certification Library.

Its purpose is to explain how the Framework, Profile, Scope, Subjects, Evidence, and Suite foundations relate before visitors enter the individual documentation pages.

## Maintenance

Repository maintenance for `/atlas/certification/` should:

- preserve Atlas authority over Atlas intelligence;
- preserve Certifier authority over certification;
- keep Framework, Profile, Scope, Subjects, and Evidence documentation aligned;
- avoid duplicating Suite Standards or Suite Methodology;
- ensure certification flow reflects current Suite architecture;
- keep downstream institutional relationships bounded;
- distinguish certification subjects from supporting artifacts;
- preserve historical certification evidence where applicable.

README reconciliation documents the certification architecture that exists. It does not redesign it.
