# ATLAS Rendering Layers v1

## 1. Purpose

This document defines the rendering-layer model used by Atlas presentation systems.

Rendering layers organize how Atlas packages are displayed.

Rendering layers preserve canonical interpretation authority.

Rendering layers enable compression without classification drift.

Rendering layers support multi-interface export compatibility.

Rendering layers must not modify topology classification.

Rendering layers control visibility, compression, and export behavior without altering what Atlas means.

## 2. Rendering Layer Taxonomy

Atlas defines three rendering layers:
- canonical layer
- helper layer
- derived layer

Each layer has different authority constraints.

Only canonical layers define classification meaning.

Helper and derived layers may improve readability, navigability, and export usability, but they must remain subordinate to canonical interpretation authority.

## 3. Canonical Layer Definition

The canonical layer includes:
- `metadata.md`
- `evidence.md`
- `signals.md`
- `trust-dimensions.md`
- topology fields
- corridor roles
- foundation domains

The canonical layer defines interpretation authority.

The renderer must not alter canonical meaning.

The renderer must not suppress canonical constraints.

The canonical layer is the governing source for classification, topology, adjacency limits, lifecycle boundaries, and evidence-based interpretation.

## 4. Helper Layer Definition

The helper layer includes:
- `profile.md`
- `builder-mode.md`
- `change-log.md` normalization summaries
- adjacency explanations
- corridor continuity summaries

The helper layer improves interpretability.

The helper layer must remain traceable to canonical sources.

The helper layer must not introduce classification authority.

Helper material may summarize, translate, or organize canonical meaning, but it must not exceed canonical boundaries.

## 5. Derived Layer Definition

The derived layer includes:
- visual summaries
- maps
- corridor overlays
- foundation overlays
- deployment-readiness views
- trajectory highlights

The derived layer is renderer-generated.

The derived layer must remain canonically grounded.

The derived layer must not introduce new interpretation claims.

Derived material may improve accessibility and interface utility, but it must remain subordinate to canonical and helper authority.

## 6. Rendering Authority Hierarchy

Rendering authority follows this order:
- canonical layer
- helper layer
- derived layer

If conflict appears:
- canonical layer governs interpretation
- helper layer may clarify
- derived layer must adjust

Derived outputs must defer to canonical sources.

Helper outputs may not overrule canonical meaning.

No rendering layer may create authority above the canonical layer.

All helper-layer and derived-layer outputs must remain traceable to at least one canonical-layer source.

Renderer-generated summaries must not introduce interpretation that cannot be mapped back to canonical package materials.

## 7. Compression Rules

The renderer may compress:
- signal lists
- trust summaries
- foundation stacks
- corridor role explanations
- adjacency descriptions

The renderer must preserve:
- interpretation boundaries
- constraint visibility
- anchor placement clarity
- adjacency dependence visibility

Compression must not weaken classification meaning.

Compression is permitted only when semantic coverage and visible limits remain intact.

## 8. Constraint Preservation Rule

Rendering systems must preserve visibility of:
- deployment absence
- policy exclusions
- adjacency reliance
- federal reliance
- resource constraints
- scope limits

Constraint removal creates non-compliant renderings.

A rendering that improves readability by hiding material constraints is not Atlas-compliant.

## 9. Boundary Preservation Rule

The renderer must preserve:
- non-establishment language
- scope narrowing statements
- corridor-role limits
- foundation-dependence visibility
- lifecycle maturity boundaries

Boundary removal creates interpretation drift.

Boundary language may be compressed or regrouped.

It may not be erased, softened, or replaced with stronger implied claims.

## 10. Topology Preservation Rule

The renderer must not:
- reinterpret topology trio
- merge corridor roles
- promote adjacency to anchor status
- collapse expansion-edge into anchor placement
- create inferred corridor attachment

Topology meaning must remain canonical.

Display-oriented normalization may change label form or visual grouping.

It may not change topology authority.

## 11. Signal Rendering Rules

The renderer may:
- group signals by category
- collapse redundant signals
- highlight trajectory direction

The renderer must not:
- upgrade signals to evidence
- convert signals into corridor placement
- remove absence signals

Trajectory visibility must remain accurate.

Signal compression must preserve both directional and limiting signal content.

## 12. Trust Rendering Rules

The renderer may:
- summarize trust posture
- highlight constraint visibility
- group boundary clarity indicators

The renderer must not:
- introduce scoring
- introduce ranking
- convert trust posture into classification strength

Trust remains interpretive, not evaluative.

Trust rendering may increase readability.

It may not turn trust into a scorecard or ranking surface.

## 13. Foundation Rendering Rules

The renderer may:
- display stacked foundation participation
- highlight dominant foundation domains
- group foundation overlays visually

The renderer must not:
- merge foundation types implicitly
- convert foundation presence into corridor-role authority
- remove domain distinctions

Foundation domains must remain separable.

Visual simplification must not erase the difference between domain participation and topology role.

## 14. Corridor Rendering Rules

The renderer may:
- display corridor chains
- highlight anchor segments
- visualize adjacency-supported continuity
- identify expansion-edge direction

The renderer must not:
- obscure anchor origin visibility
- collapse transit into terminus roles
- remove distance sensitivity
- infer corridor participation without evidence

Corridor structure must remain topology-faithful.

A renderer may visualize corridor continuity aggressively only when anchor basis, traversal limits, and role distinctions remain visible.

## 15. Lifecycle Rendering Rules

The renderer may:
- display lifecycle maturity indicators
- highlight normalization completeness
- group historical participation visibility

The renderer must not:
- promote lifecycle stage
- infer lifecycle advancement
- override metadata lifecycle status

Lifecycle authority remains canonical.

Any lifecycle display must remain traceable to the authoritative metadata status carrier.

## 16. Export Compatibility Surfaces

Rendering layers must support export into:
- HTML views
- JSON topology structures
- map overlays
- API-readable package summaries
- notebook-compatible analysis layers

Exports must remain canonically traceable.

Derived export formats must not introduce interpretation drift.

If an export requires compression, the same rendering-layer authority rules apply.

Export convenience does not justify classification drift.

Different rendering interfaces (maps, tables, summaries, overlays, or API exports) must present classification-consistent interpretations.

Interface-specific formatting differences must not produce topology-role variation across views.

## 17. Rendering Compliance Definition

A rendering system is Atlas-compliant when all of the following are true:
- canonical layer remains unchanged
- helper layer remains traceable
- derived layer remains bounded
- constraint visibility is preserved
- topology trio is preserved
- foundation distinctions are preserved
- corridor origin visibility is preserved

Non-compliance occurs when any of the following are true:
- derived layers introduce classification meaning
- signals are upgraded to evidence
- adjacency is upgraded to anchor status
- constraints are removed during compression
- foundation domains are merged implicitly
- the renderer modifies lifecycle authority

## Version

v1 — Initial Atlas rendering-layer specification
