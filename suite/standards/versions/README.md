# Satoshium Versions Standard

**Path:** `/suite/standards/versions/`  
**Surface:** Satoshium Suite · Standards · Versions  
**Status:** Current repository documentation

## Purpose

This directory documents the **Satoshium Versions Standard**, the Suite-wide standards layer governing version numbering, revision history, compatibility, and historical preservation.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Standard Role

The Versions Standard defines how Satoshium standards, methodologies, schemas, specifications, and other governed artifacts evolve while preserving historical integrity.

Its purpose is to allow the Suite to change without losing the ability to determine:

- which version applied;
- what changed;
- when it changed;
- why it changed;
- what it superseded; and
- which earlier versions remain part of the institutional record.

Versioning must preserve history rather than rewrite it.

The Governance Review further establishes:

```text
VERSION
≠ DECISION

CORRECTION
≠ VERSION

SUPERSESSION
≠ MUTATION

CHANGED CONCLUSION
→ NEW GOVERNANCE DECISION
```

A version describes a governed edition or state.

A Governance Decision Record (GDR) records the decision that authorizes or establishes governance.

Version identity and decision identity must therefore remain distinct.

## Version Numbering

Version Numbering defines the conventions used to assign official version identifiers to governed artifacts.

Version identifiers should be:

- explicit;
- stable;
- traceable;
- consistently applied; and
- preserved with the record they identify.

A version identifier should distinguish materially different governed states without implying that every correction automatically creates a new version.

## Revision History

Revision History documents changes over time.

Revision records may include:

- corrections;
- enhancements;
- deprecations;
- supersession;
- migration notes;
- compatibility changes; and
- other governed revisions.

Revision history should preserve enough context for future reviewers to understand the relationship between versions.

Historical records should remain historically accurate.

## Compatibility

Compatibility defines expectations for how versions coexist and how later versions relate to earlier ones.

Compatibility guidance may address:

- backward compatibility;
- forward compatibility;
- migration;
- coexistence;
- interpretation of older records;
- schema compatibility; and
- implementation expectations.

Compatibility does not require mutation of older canonical records.

Where versions differ materially, those differences should remain explicit.

## Historical Preservation

Every official governed version should remain preserved and referenceable as part of the institutional record where the applicable architecture requires it.

Historical preservation supports:

- auditability;
- reproducibility;
- interpretation of earlier records;
- governance review;
- migration;
- correction history; and
- institutional memory.

A later version should not cause an earlier version to disappear or be rewritten as though the later rule had always existed.

## Correction and Versioning Discipline

The Versions Standard must preserve the distinction between correction and versioning.

In particular:

- correction is not deletion;
- correction is not automatically a version;
- correction is not itself a versioning decision;
- version is not decision;
- supersession is not mutation; and
- changed governance conclusion requires a new Governance Decision Record rather than silent revision of the prior decision.

Whether a correction produces a new version must be determined by the applicable governed process rather than assumed from the existence of the correction.

## Relationship to Governance

The **Governance Standard** defines how official Suite Standards are maintained, reviewed, approved, changed, and preserved.

The broader **Satoshium Suite Governance Model** governs constitutional authority, governance decisions, change control, supersession, correction, accountability, and historical preservation across the Suite.

The Versions Standard provides the version-control framework used within those governed processes.

The governing distinction is:

```text
Governance Decision
→ authorizes or establishes the change

Version
→ identifies the resulting governed edition or state
```

Therefore:

```text
VERSION
≠ DECISION
```

The current controlling Suite Governance decision is:

```text
GDR-2026-0026
→ Satoshium Suite Governance Model
→ APPROVED
→ EFFECTIVE
```

## Governance Decision Record Treatment

Governance Decision Records (GDRs) are not ordinary version labels.

Each GDR preserves the authoritative governance decision and its status.

Where governance evolves:

```text
prior GDR
→ remains historically attributable to its effective period

new GDR
→ becomes controlling prospectively when approved and effective
```

A changed governance conclusion requires a new GDR.

A prior GDR must not be silently rewritten merely to match later governance.

Versioning may describe editions of a governance artifact, but it does not replace decision identity.

```text
GDR IDENTITY
≠ DOCUMENT VERSION
```

The Governance Decision Register provides the authoritative current-state and historical-lineage index for governance decisions.

## Relationship to Standards and Methodology

Versioning applies across standards and methodology without collapsing their distinct roles.

Standards define expectations.

Methodology defines implementation.

Each may evolve under its applicable governance and versioning rules.

A methodology version should not silently redefine the historical meaning of a standard version, and a standard version should not retroactively rewrite methodology that was historically in force.

## Relationship to Schemas and Specifications

Schemas and specifications may require explicit version identifiers where structural or semantic changes affect interpretation.

Versioned schemas should preserve the ability to determine which structure governed a record at the time it was created or evaluated.

A record valid under one schema version should not be silently reinterpreted as though it had been produced under another version.

## Current-State and Historical-State Controls

Published governance and governed artifacts must make current standing clear without sacrificing historical truth.

Where applicable, current-state or superseded governance should expose enough metadata to determine:

- Status;
- Version;
- Decision Date;
- Effective Date;
- Effective Until, where applicable;
- Superseded By;
- Current Replacement; and
- the authoritative current-state pointer.

The governing rule is:

> **A preserved historical governance record must remain historically true while also being distinguishable from current operative governance.**

Therefore:

```text
CURRENT
≠ HISTORICAL

PRESERVED
≠ CURRENT

SUPERSEDED
≠ DELETED
```

A superseded record should remain accessible while clearly identifying the controlling replacement.

## Publication and Lifecycle Boundaries

Versioning must remain distinct from publication and lifecycle state.

A version may exist without being published.

Publication does not itself create a new version.

Lifecycle activation does not itself create a new version.

Canonical creation, lifecycle activation, publication, correction, and versioning are separate governed concepts.

## Repository Expectations

Changes to this directory should preserve:

1. explicit and stable version identifiers;
2. complete revision history;
3. compatibility guidance where needed;
4. historical preservation;
5. the distinction between correction and versioning;
6. the distinction between versioning, publication, and lifecycle state;
7. governance traceability; and
8. consistency with the governing Suite architecture;
9. separation of governance decision identity from document version identity;
10. GDR preservation and traceability where governance decisions are involved;
11. explicit current-vs-historical status controls; and
12. authoritative current-state pointers for superseded governance where applicable.

Changes that would redefine when a new canonical version is required, how supersession works, or how historical records are preserved require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**The Suite may evolve, but every governed version and governance decision must remain understandable in the context in which it existed, while current operative status remains explicit.**
