# Atlas Corridor + Framework Consistency Report

## Executive Summary

The canonical corridor trio is internally consistent across the Corridor Assignment Matrix, all 50 `metadata.md` files, and all 50 rendered HTML Topology Metadata sections.

No value mismatches were detected for:
- Corridor Group
- Foundation Layer
- Topology completion / Completion Layer

The main drift is not in the trio itself. It appears in three other places:

1. the corridor index exposes additional “classification family” language that is not encoded as canonical state metadata
2. the HTML renderer normalizes `Topology completion layer` to `Completion Layer`
3. state hero chips omit the corridor trio entirely and instead use a separate annotation layer with inconsistent fifth-chip behavior

Framework alignment is only partial. The requested framework file `signals-update-protocol.md` was not present at the specified path. The closest available framework documents support general scope discipline and upstream signal authority, but they do not define the renderer conventions now visible in the HTML state pages, especially absence-callouts, gap inheritance presentation, canonical narrowing, or universal scope-boundary rendering.

## Corridor Trio Alignment Findings

- The Corridor Assignment Matrix contains 50 state rows.
- All 50 matrix rows map cleanly to canonical `metadata.md` files and rendered HTML state pages.
- Matrix values match canonical metadata exactly across all 50 states.
- Canonical metadata values match rendered HTML Topology Metadata values exactly across all 50 states.
- No trio-level classification mismatches were detected between:
  - `atlas/corridors/corridor-assignment-matrix.html`
  - `atlas-export/jurisdictions/us/states/*/metadata.md`
  - `html-mirror/atlas/jurisdiction-intelligence-engine/us/states/*/index.html`

The corridor index also uses the same three-part model conceptually:
- Corridor Group
- Foundation Layer
- Topology Completion Layer

So the operative trio schema is stable.

The only visible corridor-index drift is at the example-label level, not at the schema level. The clearest example is:
- corridor index example: `Mountain West Research Layer`
- canonical matrix / metadata value: `Mountain West Research & Federal Lab Transition Layer`

That is a simplified public-facing label, not a state-level mismatch, but it does create vocabulary looseness around the foundation layer set.

## Classification Family Findings

The corridor index introduces a separate public grouping under `Corridor Classification Families`, including:
- Energy–Compute Corridors
- Research Corridors
- Interconnection Corridors

These do not currently function as a canonical per-state classification system.

Findings:
- `Energy–Compute` appears in the corridor index, but not as an exact matrix value, metadata value, or HTML topology field.
- `Interconnection` appears in the corridor index, but not as an exact matrix value, metadata value, or HTML topology field.
- `Research` appears in the corridor index and also appears lexically inside some canonical trio values, but only as part of named corridor or foundation labels, not as a separate family tag.

Interpretation:
- these families are framed like taxonomy
- but operationally they behave as an annotation layer
- they are not an alternate active classification system inside state metadata

So the best classification is:

**Current status: annotation layer with taxonomy-like presentation**

That matters because the corridor index makes these families look structurally authoritative, while the actual canonical state system remains the trio only.

## Completion Layer Label Findings

The completion-layer label is semantically stable but textually normalized across surfaces.

Observed forms:
- corridor index heading: `Topology Completion Layer`
- corridor matrix column: `Topology Completion Layer`
- canonical metadata heading: `Topology completion layer`
- rendered HTML field label: `Completion Layer`

Counts:
- `metadata.md` uses `Topology completion layer` on 50 of 50 states
- HTML uses `Completion Layer` on 50 of 50 states
- HTML uses `Topology Completion Layer` on 0 of 50 states

Interpretation:
- this is a consistent renderer normalization rule
- it is not a semantic mismatch
- it does reduce exact phrase traceability from canonical markdown to HTML

So the behavior is best described as:

**stable semantic mapping, undocumented label shortening**

## Hero Chip Consistency Findings

The state hero blocks do not surface the corridor trio.

Across all 50 state pages:
- Corridor Group chip: 0 of 50
- Foundation Layer chip: 0 of 50
- Completion Layer chip: 0 of 50
- Jurisdiction Lens chip present with actual value: 30 of 50
- Jurisdiction Lens chip present as placeholder only: 20 of 50
- Jurisdiction Lens chip missing entirely: 0 of 50

This means:
- the trio is consistently omitted from the hero layer
- the hero layer depends on the Topology Metadata section for corridor classification visibility
- Jurisdiction Lens is the only requested field that appears in hero chips at all

Hero baseline chips are consistent on all 50 pages:
- Jurisdiction
- Jurisdiction lens
- Completeness
- Surface assignment

But overall hero-chip behavior is not fully uniform:
- 14 pages use only the 4-chip baseline
- 36 pages add a fifth chip

That fifth chip is not standardized. Repeated variants include:
- `Adjacency-bounded package` on 25 pages
- `State: evidence-absence package` on 4 pages
- sibling chips on 5 pages, such as Great Lakes or Northeast sibling labels
- `Package status: COMPLETE (canonical)` on 1 page
- `Cross-foundation placement` on 1 page

Interpretation:
- hero chips are using a separate annotation layer
- that layer is not aligned to the canonical trio fields
- the extra fifth chip introduces visible presentation drift between otherwise structurally similar state pages

The Jurisdiction Lens behavior is internally consistent with canonical metadata:
- 30 states have a canonical `Jurisdiction lens` heading in `metadata.md`
- those same 30 states surface the lens in HTML Topology Metadata and as a populated hero chip
- the remaining 20 states use a placeholder hero chip instead of omitting the field

So lens handling is structurally consistent, but the placeholder presentation is visibly incomplete.

## Framework Alignment Findings

The exact requested framework source was not present:
- missing path: `/home/claw-admin/claw-labs/atlas-export/docs/framework/signals-update-protocol.md`

Closest available framework documents included:
- `ATLAS_UPDATE_PROTOCOL_v1.md`
- `ATLAS_SIGNAL_TYPES_v1.md`
- `ATLAS_SCOPE_BOUNDARIES_v1.md`

These available framework files support general Atlas discipline:
- signals remain upstream to downstream interpretation
- scope boundaries matter
- updates should remain structural, not reactive
- classifications should not drift unpredictably

That high-level intent matches the renderer direction.

However, the specific renderer behaviors requested for validation are not defined in the available framework files.

Detected HTML behaviors across the 50-state surface:
- absence-callouts appear on 29 pages
- gap inheritance language appears on 19 pages
- canonical narrowing appears on 5 pages
- `Scope Boundary Statement` appears on all 50 pages
- `2. Scope Boundary` appears in the section nav on all 50 pages

Framework coverage of those behaviors:
- no available framework file defines `absence-callout`
- no available framework file defines `gap inheritance` as a renderer rule
- no available framework file defines `canonical narrowing`
- scope boundaries are only documented at the general Atlas-mission level, not as a universal per-state renderer convention

Interpretation:
- the renderer is aligned with framework intent
- but it is not fully aligned with explicit framework specification
- there is a documentation-layer gap between framework and renderer behavior

This is the most important framework result.

There is also a source-path drift problem:
- the task referenced `signals-update-protocol.md`
- the available framework corpus instead exposes `ATLAS_UPDATE_PROTOCOL_v1.md`

That suggests either:
- the named framework file was moved or renamed
- or renderer conventions were implemented without an updated public framework file at the expected location

## Priority Normalization Targets

### High

- Create or restore a canonical framework document that explicitly defines renderer conventions for:
  - absence-callouts
  - gap inheritance presentation
  - canonical narrowing
  - state-level scope boundary rendering
- Decide whether corridor classification families are official taxonomy or documentation-only annotation. Right now they read as taxonomy but do not function canonically that way.
- Decide whether hero blocks should surface the corridor trio directly or remain intentionally limited to the separate hero annotation layer.

### Medium

- Normalize corridor-index example vocabulary to exact canonical trio labels where precision matters, especially around the Mountain West research foundation label.
- Document the `Topology completion layer` → `Completion Layer` renderer normalization rule.
- Normalize fifth-chip usage in hero blocks so optional annotation chips do not drift by state.

### Low

- Decide whether empty Jurisdiction Lens hero chips should remain as placeholders or disappear when no canonical lens exists.
- Reduce hero-chip presentation variance between 4-chip and 5-chip states unless that variance is intentionally meaningful.
