# Satoshium Atlas — U.S. States Index

**Path:** `/atlas/jurisdiction-intelligence-engine/us/states/`  
**Institution:** Satoshium Atlas  
**Surface:** U.S. States Index  
**Status:** Current repository documentation

## Purpose

This directory contains the **U.S. States Index** for the Satoshium Atlas Jurisdiction Intelligence Engine.

It provides the primary state-level navigation surface for the United States Atlas package and routes visitors into all 50 state jurisdiction packages.

The public page for this directory is:

- `index.html`

This README documents the repository role, navigation model, state-package boundary, and relationship of this index to the broader Atlas architecture. It does not replace the public presentation in `index.html`.

## Index Role

The U.S. States Index is a navigation surface.

It provides:

- a clickable state tile map;
- an alphabetical state directory; and
- stable state-level URLs.

Conceptually:

```text
Satoshium Atlas
        ↓
Jurisdiction Intelligence Engine
        ↓
United States
        ↓
U.S. States Index
        ↓
Individual State Packages
```

The index routes to state records.

It does not itself replace or become the authoritative source for those records.

## Current Coverage

The current index provides direct navigation to all 50 U.S. state packages.

Each state is available through:

- the clickable tile map; and
- the alphabetical directory.

The index therefore serves as the stable routing layer above the individual state-package directories.

## State Package Boundary

Each state package remains an Atlas-owned jurisdiction structure.

The index should preserve the distinction between:

- state navigation;
- the state record itself;
- supporting evidence;
- metadata;
- signals;
- trust-related dimensions;
- corridor relationships;
- canonical machine-readable representations; and
- downstream Suite institutional records.

Navigation does not transfer authority.

## Relationship to the United States Package

The U.S. States Index sits beneath the United States national jurisdiction package.

The national package defines the broader U.S. Atlas structure.

This index provides the direct state-level entry surface.

The relationship is:

```text
United States Jurisdiction Package
        ↓
U.S. States Index
        ↓
State Package
```

## Relationship to Atlas

Atlas remains authoritative for:

- state jurisdiction intelligence;
- state-package structure;
- Atlas-owned metadata;
- Atlas signals;
- Atlas trust-related dimensions;
- corridor classifications;
- Atlas change history; and
- canonical Atlas jurisdiction representations.

The U.S. States Index is an access layer over those records.

## Relationship to Evidence

Individual state packages may contain or reference evidence supporting their Atlas claims and structural interpretation.

The index may route users into those packages but does not itself establish evidence authority.

## Relationship to Signals

State signals remain derived from the applicable state evidence and Atlas record context.

The index should not independently create or redefine signals.

## Trust-Related Context

Where state packages include Atlas trust-related dimensions, that terminology remains bounded to Atlas.

Atlas trust-related dimensions are not equivalent to Attestor Trust Statements.

The following distinction should remain explicit:

```text
Atlas Trust-Related Context
≠
Attestor Trust Statement
```

## Relationship to Corridors

State packages may participate in Atlas corridor structures.

Corridor classifications provide cross-state topology context.

They do not replace the state package as the authoritative jurisdiction record.

The U.S. States Index may later expose richer corridor-aware or geographic navigation, but those navigation layers should preserve state-package identity.

## Map and Navigation Model

The current page uses a linked tile map as a practical navigation surface.

The page also preserves the option to replace that tile map with a future geographic SVG or interactive map without changing the underlying state URLs.

That design choice supports:

- stable routing;
- future UI upgrades;
- durable references;
- accessibility; and
- separation between presentation and record identity.

The map presentation may evolve.

The state paths should remain stable unless a governed repository change requires otherwise.

## Relationship to Suite Institutions

The U.S. States Index belongs to Atlas.

Other Suite institutions may reference state records or Atlas-derived outputs under their own governed responsibilities.

Examples include:

- Certifier may certify eligible Atlas subjects.
- Registry may create a Registry Entry / SREG referencing an Atlas or certification object.
- Chronicle may preserve governed chronology.
- Anchor may preserve an Integrity Reference.
- Beacon may publish Discovery Signals / Discovery Metadata.
- Attestor may consume eligible governed inputs and issue Attestations / Trust Statements.
- Navigator may define or orchestrate workflows.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Repository Expectations

Changes to this directory should preserve:

1. the index as a navigation layer rather than source authority;
2. stable state paths;
3. complete routing to all 50 state packages;
4. separation between presentation and state-record identity;
5. evidence and signal provenance;
6. separation between Atlas trust-related dimensions and Attestor Trust Statements;
7. corridor-aware navigation without authority transfer; and
8. compatibility with future geographic or interactive map surfaces.

Changes that would redefine state-package authority, canonical jurisdiction structure, trust semantics, or cross-Suite object relationships require governed architectural review rather than a documentation-only edit.

## Governing Principle

**The U.S. States Index provides durable navigation to Atlas state records while preserving each state package as the authoritative jurisdiction surface.**
