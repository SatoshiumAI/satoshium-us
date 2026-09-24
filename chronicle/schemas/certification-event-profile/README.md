# Satoshium Chronicle — Certification Event-Type Profile

**Path:** `/chronicle/schemas/certification-event-profile/`  
**Institution:** Satoshium Chronicle  
**Surface:** Production Event-Type Profile  
**Status:** Current repository documentation

## Purpose

This directory contains the production **Certification Event-Type Profile** for Satoshium Chronicle.

The Profile specializes the Chronicle Base Schema for Chronicle Entries that preserve qualifying certification-related Occurrences.

It does not create a separate canonical Certification Event object.

The governing relationship is:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        =
Certification-related Chronicle Entry
```

## Profile Role

The Certification Event-Type Profile adds only the minimum certification-specific requirements needed to preserve certification-related historical Occurrences accurately.

All Chronicle Entries governed by this Profile remain:

- Chronicle Entries;
- governed by the Chronicle Base Schema;
- subject to Chronicle lifecycle, Verification, Validation, Versioning, Publication, and Correction rules.

The Profile is a specialization layer, not a separate Chronicle object family.

## Authority Boundary

Satoshium Certifier remains authoritative for:

- certification determinations;
- Certification Packages;
- certification lifecycle;
- certification status;
- Certifier-owned evidence and findings;
- Certifier validation structures.

Satoshium Chronicle owns only the historical-preservation representation of the qualifying Occurrence.

Chronicle references Certifier authority.

It does not reproduce or replace that authority.

## Profile Version

**Profile Version:** `1.0.0`

The first production application of this Profile occurred with:

`CHR-2026-0001 Entry Version 1`

on August 22, 2026.

## Required Certification Constraints

In addition to universal Chronicle Base Schema requirements, the Profile requires or strengthens the following:

```text
event_type_profile = certification-event-profile
originating_system = certifier
event_type = approved Certification Event Type
event_date = non-null certification Occurrence date or timestamp
authoritative_record_references = minimum one authoritative Certifier reference
provenance = includes authoritative certification reference
```

These requirements preserve traceability to the authoritative certification record.

## Approved Certification Event Types

Current approved certification-related Event Types include:

- Certification Created
- Certification Renewed
- Certification Suspended
- Certification Revoked
- Certification Expired

Machine-readable values are governed through Chronicle Controlled Values.

## Authoritative Certification Reference

Every Chronicle Entry governed by this Profile must identify the authoritative Certifier record that established the represented Occurrence.

The core relationship is:

```text
Chronicle Entry
        ↓ references
Certification Package
```

This reference does not make Chronicle the certification authority.

## Originating System

For this Profile:

```text
originating_system: certifier
```

The field is conditional in the Chronicle Base Schema and becomes required because the Certification Event-Type Profile establishes the operational need.

## Registry Relationship

A related Registry reference becomes required when:

1. a corresponding Registry Entry exists; and
2. that Registry Entry is materially relevant to the Chronicle Entry.

Where present:

- Registry remains authoritative for the SREG;
- Chronicle preserves the historical relationship;
- the Registry Entry does not become the authoritative certification record.

## Historical Context

Historical Context explains why the certification Occurrence matters within Satoshium institutional history.

It should not restate or duplicate:

- Certifier-owned findings;
- certification evidence bodies;
- certification determination logic;
- Certification Package schema;
- Certifier lifecycle mechanics.

Chronicle preserves historical meaning around the Occurrence rather than reconstructing the Certifier process.

## Provenance

Certification-related Chronicle Entries should preserve provenance sufficient to explain how Chronicle established the historical representation.

Provenance may include:

- Certifier origin;
- acquisition or access method;
- retrieval or review date;
- authoritative Certification Package reference;
- material limitations.

Provenance supports historical traceability.

It does not transfer institutional authority.

## Verification

Chronicle Verification examines Chronicle's own historical representation.

Verification may review:

- identifiers;
- Event Date;
- Certifier origin;
- authoritative references;
- Registry relationships;
- provenance;
- limitations;
- temporal consistency;
- authority boundaries.

Verification does not re-adjudicate the certification determination.

## Validation

Certification-related Chronicle Entries are validated through the two-layer schema model:

```text
chronicle-base-schema.json
        +
certification-event-profile.json
        =
Certification-related Chronicle Entry Validation
```

Validation confirms conformance to the governing Chronicle requirements.

Verification remains a separate review activity.

Therefore:

```text
Validation ≠ Verification
```

Validation also does not itself approve Publication.

## What the Profile Does Not Duplicate

The Profile does not duplicate:

- certification findings;
- certification evidence bodies;
- Certification Package schema;
- certification determination logic;
- Certifier validation structures;
- certification lifecycle mechanics.

This preserves institutional boundaries and avoids creating a shadow Certifier inside Chronicle.

## Profile Artifacts

The Profile is published through:

- `certification-event-profile.md` — human-readable production specification
- `certification-event-profile.json` — machine-readable validation profile
- `index.html` — public explanatory surface
- `README.md` — repository and institutional documentation

The Markdown and JSON files define complementary human-readable and machine-readable representations of the same Profile.

## First Production Application

The first production precedent is:

`CHR-2026-0001 Entry Version 1`

which preserves the July 5, 2026 issuance of:

`SC-CERT-2026-0001`

The production application included:

```text
Event Type: certification_created
Originating System: certifier
Authoritative Reference: SC-CERT-2026-0001
Related Registry Entry: SREG-2026-0001
Subject: Atlas Jurisdiction Record — El Salvador
Base + Profile Conformance: PASS
Chronicle Validation: PASS
Publication Gate: APPROVED
Publication State: published
```

The production application required no change to the Profile's machine-readable validation semantics.

## Relationship to Chronicle Base Schema

The Base Schema defines the universal Chronicle Entry.

The Certification Event-Type Profile supplies only certification-specific requirements.

The governing principle is:

> **Base Schema defines the Chronicle Entry. The Certification Event-Type Profile supplies only the certification-specific requirements.**

## Relationship to Certifier

Certifier establishes certification authority.

Chronicle records that a qualifying certification-related Occurrence happened.

Chronicle does not:

- issue the certification;
- change certification status;
- reinterpret the certification decision;
- validate Certifier-owned objects as Certifier;
- replace the Certification Package.

## Relationship to Registry

Registry may provide related SREG context.

Chronicle may reference that context.

Registry remains authoritative for Registry-controlled objects.

## Relationship to Later Suite Institutions

Later Anchor, Beacon, and Attestor activity may become historical context for a Chronicle Entry, but those relationships do not alter the original certification Occurrence preserved by the Entry.

Where later Suite references are added, they should preserve:

- identity separation;
- provenance;
- authority boundaries;
- chronology;
- object-specific ownership.

## Authority Discipline

This directory should preserve the following distinctions:

- Chronicle Entry ≠ Certification Package
- Event-Type Profile ≠ Canonical Event Object
- Chronicle Verification ≠ Certifier Validation
- Chronicle Validation ≠ Verification
- Chronicle Validation ≠ Publication Approval
- Registry Reference ≠ Certification Authority
- Historical Context ≠ Certification Finding
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Considerations

No major architectural issue is evident in the current public Profile.

Later Suite Reconciliation may still review:

1. whether the approved certification Event Type vocabulary remains aligned with final Certifier lifecycle terminology;
2. whether every lifecycle-oriented event should remain represented as an Event Type versus a more general Chronicle occurrence classification; and
3. whether profile-version governance should be centralized further under Chronicle schema/version documentation.

These are limited consistency questions rather than current architectural defects.

## Repository Expectations

Changes to this directory should preserve:

1. one canonical Chronicle Entry model;
2. the Base Schema + Event-Type Profile specialization pattern;
3. Certifier authority over certification;
4. Chronicle authority over historical-preservation representation;
5. machine/human-readable Profile alignment;
6. Validation / Verification separation;
7. production precedent established by CHR-2026-0001; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Certifier establishes certification authority. Chronicle preserves the historical record of what occurred.**
