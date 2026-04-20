# ATLAS Package Lifecycle v1

## 1. Purpose

This document defines the lifecycle governance model for Atlas jurisdiction packages.

Jurisdiction packages evolve over time.

Lifecycle status controls interpretation authority, renderer eligibility, and corridor attachment stability.

Lifecycle state does not change canonical schema structure.

The canonical package schema remains stable across lifecycle stages.

Lifecycle state instead governs how strongly a package may be interpreted across Atlas and how confidently it may participate in topology, corridor, and renderer surfaces.

Renderer behavior must respect lifecycle state.

No renderer may imply a higher interpretation authority than the package lifecycle permits.

## 2. Lifecycle Model Overview

Atlas package lifecycle is a monotonic maturity ladder:
- Draft
- Evidence-Attached
- Corridor-Attached
- Complete
- Canonical
- Superseded
- Deprecated

Packages normally move forward through increasing maturity.

Packages do not normally move backward.

A package that has reached a mature state may later become superseded or deprecated.

Supersession does not invalidate historical package existence.

Deprecation removes a package from active interpretive use.

## 3. Draft State

### Definition

A Draft package has a recognizable package structure, but evidence coverage remains incomplete.

### Characteristics

A Draft package may contain:
- placeholder sections
- provisional corridor classification
- incomplete signals
- provisional trust interpretation
- preliminary profile language
- exploratory builder-mode language

Draft packages should still preserve the canonical file structure when they are present on active Atlas surfaces.

### Restrictions

Draft packages must not be treated as corridor-stable.

Draft packages must not be treated as topology-authoritative.

Draft packages must not be used as baseline interpretive anchors for adjacent jurisdictions.

### Renderer handling

Draft packages may render with a completeness indicator.

Draft packages may appear on controlled renderer surfaces.

The renderer must not imply deployment posture stability, corridor stability, or anchor-grade interpretive authority.

## 4. Evidence-Attached State

### Definition

An Evidence-Attached package has an established core evidence layer.

### Characteristics

An Evidence-Attached package shows that:
- legal anchors are identified
- infrastructure presence is documented
- negative evidence is recorded where relevant
- scope boundaries are visible

### Restrictions

Corridor classification remains provisional at this stage.

Signals may still be preliminary.

Trust interpretation must remain bounded by incomplete package maturity.

Evidence-Attached packages must not be treated as corridor-stable or topology-final.

### Renderer handling

The renderer may treat evidence as authoritative.

Signals remain preliminary.

Trust remains bounded.

The renderer may expose the package as evidence-forward, but must not imply corridor attachment stability.

## 5. Corridor-Attached State

### Definition

A Corridor-Attached package has a stabilized corridor trio classification.

### Required

A Corridor-Attached package shall contain:
- `Corridor Group`
- `Foundation Layer`
- `Topology completion layer`

### Characteristics

A Corridor-Attached package shall also show that:
- classification source is documented
- interpretation boundary is defined
- topology attachment is explicit enough for renderer use

### Restrictions

Profile and Builder Mode may still evolve.

Corridor attachment is stable, but not yet reference-grade in the same way as a Canonical package.

### Renderer handling

The renderer may treat topology as authoritative for display purposes.

Corridor placement is stable unless the package is later superseded.

The package may participate in corridor interpretation surfaces, but its full interpretive maturity may still remain below Canonical.

## 6. Complete State

### Definition

A Complete package contains all canonical files and shows internal consistency across the package layers.

### Required

A Complete package shall satisfy all of the following:
- all seven canonical files exist
- constraint language is preserved
- scope boundaries are explicit
- gap structure is normalized

### Characteristics

A Complete package should show that:
- signals align with evidence
- trust aligns with signals
- profile aligns with trust
- builder-mode aligns with upstream layers

### Renderer handling

A Complete package is eligible for the full interpretation surface.

The renderer may expose the complete governed state-page model.

Complete status does not automatically imply reference-baseline authority across Atlas.

## 7. Canonical State

### Definition

A Canonical package is a stabilized package eligible for Atlas-wide reference use.

### Required

A Canonical package shall satisfy all of the following:
- classification source is confirmed
- change-log normalization is complete
- gap inheritance is resolved
- scope narrowing is recorded where applicable
- no unresolved structural ambiguity remains

### Characteristics

A Canonical package may be used as a reference baseline for adjacent jurisdiction interpretation, corridor comparison, and stable topology reasoning.

Canonical status represents the highest active interpretation authority in this lifecycle model.

### Renderer handling

A Canonical package may be treated as a topology-stable anchor package.

The renderer may expose it as reference-grade within active Atlas interpretation surfaces.

## 8. Superseded State

### Definition

A Superseded package has been replaced by a newer authoritative interpretation.

### Causes

Supersession may occur because of:
- classification revision
- evidence expansion
- scope correction
- corridor reassignment
- topology refinement

### Characteristics

A Superseded package remains historically valid for traceability.

The newer package becomes the authoritative current surface.

Superseded status does not mean the older package was invalid at the time it was active.

### Renderer handling

A Superseded package may remain accessible.

It must be clearly marked as non-current.

It must not be treated as the current baseline interpretation for active corridor, topology, or comparison surfaces.

## 9. Deprecated State

### Definition

A Deprecated package is withdrawn from the active Atlas interpretation surface.

### Causes

Deprecation may occur because of:
- jurisdiction restructuring
- classification invalidation
- schema migration
- framework replacement

### Characteristics

A Deprecated package is retained for archival traceability only.

It no longer participates in active interpretive governance.

### Renderer handling

A Deprecated package must not appear in active corridor interpretation flows.

It must not appear in active navigation surfaces unless explicitly surfaced through archival access patterns.

## 10. Lifecycle Transition Rules

### Allowed forward transitions

The normal forward lifecycle path is:
- Draft -> Evidence-Attached
- Evidence-Attached -> Corridor-Attached
- Corridor-Attached -> Complete
- Complete -> Canonical

### Exceptional transitions

The following exceptional transitions are allowed:
- Canonical -> Superseded
- Any state -> Deprecated

### Disallowed transitions

Backward transitions are not allowed except through explicit supersession logic.

Examples of disallowed direct backward movement include:
- Canonical -> Complete
- Complete -> Corridor-Attached
- Corridor-Attached -> Evidence-Attached
- Evidence-Attached -> Draft

If package maturity must be replaced by a better interpretation, supersession is the governed mechanism.

## 11. Corridor Classification Authority by Lifecycle Stage

Corridor classification reliability by stage is:
- Draft -> provisional
- Evidence-Attached -> provisional
- Corridor-Attached -> stable
- Complete -> stable
- Canonical -> authoritative

Renderer implications:
- provisional classification must not be treated as corridor-stable
- stable classification may be rendered as active topology placement
- authoritative classification may be used as Atlas-wide baseline interpretation

Superseded packages are historically informative but non-current.

Deprecated packages have no active corridor classification authority.

## 12. Renderer Eligibility by Lifecycle Stage

Renderer permissions by lifecycle stage are:

- Draft -> limited interpretive surface
- Evidence-Attached -> evidence-forward rendering
- Corridor-Attached -> topology-visible rendering
- Complete -> full renderer surface
- Canonical -> reference-grade rendering

### Superseded

Superseded packages may remain visible, but must be marked non-current.

They must not be used as active baseline interpretation surfaces.

### Deprecated

Deprecated packages must be hidden from active navigation and active corridor interpretation surfaces.

They may remain accessible only through archival or governance-specific access paths.

## 13. Change-Log Role in Lifecycle Movement

The change log records lifecycle-relevant normalization material.

It may record:
- normalization decisions
- scope narrowing
- gap inheritance
- classification adjustments
- package revision reasoning tied to lifecycle advancement

The change log supports lifecycle interpretation.

It does not independently move lifecycle state.

Lifecycle movement requires an explicit package-status update.

That update must be carried through the authoritative lifecycle-state carrier defined in metadata.

A change log may justify or explain lifecycle movement.

It may not perform lifecycle movement by narration alone.

## 14. Metadata Status Field Contract

The authoritative lifecycle-state carrier is `Metadata status` in `metadata.md`.

Allowed metadata status values are:
- `draft`
- `evidence-attached`
- `corridor-attached`
- `complete`
- `canonical`
- `superseded`
- `deprecated`

The renderer must read lifecycle status from `metadata.md`.

Lifecycle state shall not be inferred solely from:
- file count
- hero chips
- change-log narration
- renderer heuristics

Lifecycle state must be explicitly declared in metadata.

## 15. Lifecycle Compliance Definition

A package is lifecycle-compliant when all of the following are true:
- `Metadata status` is present
- lifecycle status matches package structure
- classification stability matches lifecycle level
- constraint language is preserved
- change-log content supports the normalization record appropriate to lifecycle maturity

Non-compliance occurs when any of the following are true:
- lifecycle status is missing
- lifecycle status is inconsistent with file structure
- classification is treated as canonical without corridor attachment
- scope narrowing is required but undocumented
- gap inheritance remains unresolved at Canonical stage
- renderer behavior implies a lifecycle authority higher than the package status allows

## Version

v1 — Initial Atlas package lifecycle specification
