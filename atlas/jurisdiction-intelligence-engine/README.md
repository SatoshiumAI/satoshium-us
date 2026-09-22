# Satoshium Atlas — Jurisdiction Intelligence Engine

**Path:** `/atlas/jurisdiction-intelligence-engine/`  
**Institution:** Satoshium Atlas  
**Surface:** Jurisdiction Intelligence Engine  
**Status:** Current repository documentation

## Purpose

This directory contains the **Satoshium Atlas Jurisdiction Intelligence Engine (JIE)** entry surface.

The Jurisdiction Intelligence Engine organizes jurisdiction-level intelligence packages and provides durable navigation into country, state, subnational, corridor-aware, and related Atlas jurisdiction surfaces.

The public page for this directory is:

- `index.html`

This README documents the repository role, navigation model, jurisdiction-package boundaries, and relationship of the JIE to the broader Atlas architecture. It does not replace the public presentation in `index.html`.

## JIE Role

The Jurisdiction Intelligence Engine is Atlas's jurisdiction-navigation layer.

It provides the structured entry path from Atlas into jurisdiction packages.

Conceptually:

```text
Satoshium Atlas
        ↓
Jurisdiction Intelligence Engine
        ↓
Country Entry Surface
        ↓
Subnational / State / Province Layers
        ↓
Evidence-Aligned Jurisdiction Packages
```

The JIE organizes access to Atlas jurisdiction intelligence.

It does not replace the underlying jurisdiction records or become a separate Suite institution.

## Current Entry Surfaces

The current public page exposes several primary entry paths.

### United States

The United States entry surface routes into the U.S. jurisdiction package and supports state-level, corridor-aware, and future federal or regional navigation.

### Global Countries

The global entry surface routes into international Atlas country packages outside the United States.

### U.S. State Index

The state index provides direct navigation into published U.S. state packages.

### Global Country Index

The global country index provides direct navigation into international country packages.

These are navigation surfaces over Atlas jurisdiction records.

They do not create separate source authority.

## Country Package Model

Country packages serve as top-level national jurisdiction entry points.

They may anchor:

- national record context;
- subnational structures;
- evidence;
- metadata;
- signals;
- trust-related dimensions;
- corridor participation; and
- related Atlas navigation.

Country packages remain Atlas-owned jurisdiction structures.

## Subnational Layers

Subnational layers may include:

- U.S. states;
- provinces;
- regions;
- territories; or
- comparable jurisdiction subdivisions.

Each subnational package should preserve the Atlas record model applicable to that jurisdiction type.

The public page currently references profile, evidence, trust-dimensions, and corridor-aware routing as part of the subnational package model.

## Jurisdiction Package Boundary

The JIE is a navigation and organization surface.

It should preserve the distinction between:

- JIE navigation;
- the jurisdiction record itself;
- supporting evidence;
- metadata;
- signals;
- corridor relationships; and
- downstream Suite institutional records.

Navigation does not transfer authority.

## Relationship to Atlas

Atlas remains authoritative for:

- jurisdiction intelligence records;
- jurisdiction-package structure;
- Atlas-owned metadata;
- Atlas signals;
- Atlas trust-related dimensions;
- Atlas corridor relationships; and
- Atlas change history.

The JIE organizes those surfaces but does not create independent authority over them.

## Relationship to Corridors

The JIE supports corridor-aware navigation.

Corridors provide cross-jurisdiction topology context.

A corridor relationship may help visitors navigate from a jurisdiction package into regional topology, but corridor membership does not replace the underlying jurisdiction record.

Jurisdiction records remain the source structures for jurisdiction-specific intelligence.

## Relationship to Evidence

Jurisdiction packages may contain or reference evidence supporting Atlas claims, signals, and structural interpretation.

Evidence remains supporting material.

It should remain traceable to the jurisdiction record and should not be converted into independent authority merely because it is navigated through the JIE.

## Relationship to Signals

Jurisdiction signals remain derived from the applicable Atlas evidence and jurisdiction context.

The JIE may expose or route to signals.

It should not independently create signals.

## Trust-Related Context

The public page references **trust-dimensions** as part of subnational jurisdiction packages.

That terminology should remain bounded to Atlas.

Atlas trust-related dimensions are not equivalent to Attestor Trust Statements.

The JIE should therefore preserve this distinction:

```text
Atlas Trust-Related Context
≠
Attestor Trust Statement
```

## Relationship to Suite Institutions

The JIE belongs to Atlas.

It is not a Suite-wide orchestration or Registry surface.

Other Suite institutions may later reference jurisdiction records or Atlas outputs according to their own governed roles.

Those relationships must preserve institutional authority.

Examples include:

- Certifier may certify an eligible Atlas subject.
- Registry may create a Registry Entry / SREG referencing an Atlas or certification object.
- Chronicle may record governed chronology.
- Anchor may preserve an Integrity Reference.
- Beacon may publish Discovery Signals / Discovery Metadata.
- Attestor may consume eligible governed inputs and issue Attestations / Trust Statements.
- Navigator may define or orchestrate workflows.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Expansion Model

The JIE is designed to support expansion beyond a single country.

The current navigation model is intended to accommodate future jurisdiction growth while preserving stable URL and repository structure.

Potential future expansion may include:

- additional country packages;
- additional subnational layers;
- regional navigation;
- corridor-aware navigation; and
- richer map or UI surfaces.

These are expansion capabilities, not automatic statements that every future jurisdiction or layer is already established.

## URL and Navigation Stability

One of the JIE's important repository roles is preserving stable paths as Atlas grows.

New map or navigation surfaces should not unnecessarily break existing jurisdiction-package links.

Stable paths support:

- durable references;
- historical continuity;
- machine-readable exports;
- cross-document linking; and
- external references to Atlas records.

## Repository Expectations

Changes to this directory should preserve:

1. the JIE as the Atlas jurisdiction-navigation layer;
2. jurisdiction records as Atlas-owned source structures;
3. country and subnational package boundaries;
4. evidence and signal provenance;
5. corridor-aware navigation without authority transfer;
6. separation between Atlas trust-related dimensions and Attestor Trust Statements;
7. stable URL and navigation structure; and
8. compatibility with future jurisdiction expansion.

Changes that would redefine jurisdiction ownership, create new Suite-wide authority, alter trust semantics, or change the canonical jurisdiction-package model require governed architectural review rather than a documentation-only edit.

## Governing Principle

**The Jurisdiction Intelligence Engine organizes access to Atlas jurisdiction intelligence without replacing the authority of the jurisdiction records it exposes.**
