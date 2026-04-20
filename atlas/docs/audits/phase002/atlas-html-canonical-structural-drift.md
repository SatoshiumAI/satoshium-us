# Atlas HTML ↔ Canonical Structural Drift Report

## Executive Summary

The HTML state pages retain strong file-level coverage of the canonical Atlas packages, but they do not preserve canonical package order.

Across all 50 states, the HTML surface exposes mapped sections for `metadata.md`, `evidence.md`, `signals.md`, `trust-dimensions.md`, `profile.md`, `builder-mode.md`, and `change-log.md`. At that level, structural visibility is strong and repeated omissions were not detected.

The main drift is systematic ordering drift. The HTML renderer front-loads topology metadata, inserts standalone helper layers such as Scope Boundary Statement and Structural Exclusions, and only then moves through the core evidence → signals → trust → profile → builder sequence. That means the HTML surface is structurally aligned by component presence, but not by canonical package sequence.

A second drift layer appears in Section 9 handling. Most states use an HTML Evidence Gaps section, but a smaller subset replaces that with Scope Boundaries & Canonical Narrowing, and Michigan keeps an HTML Evidence Gaps section even though its `evidence.md` does not include an explicit Evidence gaps heading.

## Section Mapping Findings

Core section mapping is consistent across all 50 states.

50 / 50 state pages expose these file-level mappings:

- `Topology Metadata` → `metadata.md`
- `Evidence Summary` → `evidence.md`
- `Signals Summary` → `signals.md`
- `Trust Dimensions Summary` → `trust-dimensions.md`
- `Profile Summary` → `profile.md`
- `Builder Mode Summary` → `builder-mode.md`
- `Change-Log Notes` → `change-log.md`

Additional structural evidence of stable mapping:

- all 50 HTML pages include visible source references to `metadata.md`
- all 50 include visible source references to `evidence.md`
- all 50 include visible source references to `signals.md`
- all 50 include visible source references to `trust-dimensions.md`
- all 50 include visible source references to `profile.md`
- all 50 include visible source references to `builder-mode.md`
- all 50 include visible source references to `change-log.md`

Mapping mismatches are concentrated in renderer naming and helper-section behavior, not in loss of file visibility:

- `Topology Metadata` is a renderer-facing name for `metadata.md`, not a direct file-name match.
- `Evidence Summary`, `Signals Summary`, `Trust Dimensions Summary`, `Profile Summary`, and `Builder Mode Summary` all surface the canonical files as rendered summary sections rather than as direct file-name labels.
- Section 9 is not mapped one-to-one across the whole surface:
  - 44 states have `## Evidence gaps` in `evidence.md` and also render an HTML `Evidence Gaps` section.
  - 5 states render `Scope Boundaries & Canonical Narrowing` instead: `indiana`, `minnesota`, `ohio`, `pennsylvania`, `wisconsin`.
  - `michigan` renders `Evidence Gaps` in HTML even though its `evidence.md` does not contain an explicit `## Evidence gaps` heading.

## Ordering Alignment Findings

Report: systematically differs.

Canonical expected sequence:

1. `evidence.md`
2. `signals.md`
3. `trust-dimensions.md`
4. `profile.md`
5. `builder-mode.md`
6. `metadata.md`
7. `change-log.md`

Observed HTML sequence across all 50 state pages:

1. hero overview
2. `Topology Metadata`
3. `Scope Boundary Statement`
4. `Evidence Summary`
5. `Signals Summary`
6. `Trust Dimensions Summary`
7. `Profile Summary`
8. `Builder Mode Summary`
9. `Structural Exclusions`
10. `Evidence Gaps` or `Scope Boundaries & Canonical Narrowing`
11. `Change-Log Notes`

Structural alignment result:

- the canonical core sequence is partially preserved as a middle block inside the HTML renderer
- the HTML surface does not match canonical order directly
- metadata is systematically moved from near the end of the package sequence to the front of the page
- Scope Boundary Statement, Structural Exclusions, and Section 9 helper layers are inserted between canonical file mappings
- this pattern is consistent across all 50 states, so the drift is renderer-wide rather than isolated

## HTML-Only Structural Layers

These sections are present in HTML as standalone layers but do not exist as standalone canonical package files.

### Scope Boundary Statement

Primary classification: rendering helper with structural-drift potential.

- In 38 states, `evidence.md` contains an explicit `## Scope` heading, so the HTML section acts as a direct renderer lift of that canonical framing.
- In 12 states, `evidence.md` does not contain an explicit `## Scope` heading, but the HTML renderer still creates a Scope Boundary Statement section.
- That makes this layer a useful renderer helper, but also a structural drift point because it is universalized in HTML beyond its canonical heading availability.

### Structural Exclusions

Primary classification: rendering helper / aggregation layer.

- Structural exclusions are present in canonical package materials, especially in `evidence.md`, and are often reinforced in downstream layers or `change-log.md`.
- The HTML renderer elevates exclusions into a standalone top-level section instead of leaving them embedded inside the canonical files.
- This is not a file-level omission problem. It is a renderer-level reorganization of canonical exclusion material.

### Evidence Gaps

Primary classification: rendering helper.

- In 44 states, `evidence.md` includes an explicit `## Evidence gaps` heading, so the HTML section is a straightforward visibility lift.
- In `michigan`, HTML still renders `Evidence Gaps` even though `evidence.md` lacks an explicit evidence-gaps section. The HTML page states that the gap structure is carried by downstream layers instead.
- This means the HTML Evidence Gaps layer is mostly canonical visibility, but with at least one synthesized cross-layer case.

### Scope Boundaries & Canonical Narrowing

Primary classification: interpretation layer with subset-specific structural drift.

- This layer appears in 5 states: `indiana`, `minnesota`, `ohio`, `pennsylvania`, `wisconsin`.
- It replaces the standard HTML Evidence Gaps section for that subset.
- It does not correspond to a standalone canonical package file.
- In `indiana`, it clearly reflects `change-log.md` scope-refinement behavior.
- In the other four states, it functions as a renderer-level explanation that the package uses scope constraints or canonical narrowing rather than a standard evidence-gap section.
- This is the clearest repeated subset drift between canonical package shape and HTML rendering shape.

## Missing Canonical Visibility

No repeated file-level omission of canonical package components was detected.

Across all 50 states:

- `metadata.md` is surfaced in HTML
- `evidence.md` is surfaced in HTML
- `signals.md` is surfaced in HTML
- `trust-dimensions.md` is surfaced in HTML
- `profile.md` is surfaced in HTML
- `builder-mode.md` is surfaced in HTML
- `change-log.md` is surfaced in HTML

The repeated visibility mismatch is therefore not absence, but transformation:

- canonical files are surfaced under renderer-oriented section labels
- canonical order is changed
- embedded canonical substructures are promoted into standalone renderer layers

Additional visibility note:

- `metadata.md` includes an explicit `## Jurisdiction lens` heading in 30 states
- the HTML surface visibly reflects that populated lens in those cases
- the remaining 20 pages still render the lens chip slot as an empty placeholder, which is a renderer-shape mismatch but not a canonical omission

## Cross-State Drift Patterns

### Consistent across all 50 states

- all seven canonical files are structurally visible in HTML
- canonical package order is not preserved directly
- metadata is front-loaded before evidence
- Scope Boundary Statement is rendered as a standalone section
- Structural Exclusions is rendered as a standalone section
- Change-Log is surfaced at the end of the page

### Present in subsets

- 38 states have a direct `Scope Boundary Statement` lift from `evidence.md ## Scope`
- 12 states still render Scope Boundary Statement even though `evidence.md` has no explicit `## Scope` heading
- 44 states align HTML `Evidence Gaps` with `evidence.md ## Evidence gaps`
- 5 states replace that with `Scope Boundaries & Canonical Narrowing`
- 30 states have a canonical `Jurisdiction lens` heading in `metadata.md`
- 20 states do not, but still render an empty lens chip position in HTML

### Isolated or near-isolated cases

- `michigan` is the clearest hybrid case: HTML renders `Evidence Gaps` even though `evidence.md` lacks an explicit evidence-gap section, and the page explains that the gap structure comes from downstream layers
- `indiana` is the clearest explicit change-log-driven case: HTML section 9 visibly reflects corridor-scope refinement from `change-log.md`

## Priority Structural Alignment Targets

### High

- Decide whether HTML should preserve canonical package order or continue using a renderer-specific order. Right now the drift is systematic across all 50 states.
- Normalize Section 9 behavior across the HTML surface so Evidence Gaps and Scope Boundaries & Canonical Narrowing follow one explicit rendering rule.
- Decide whether Scope Boundary Statement should remain universal in HTML when only 38 of 50 `evidence.md` files expose an explicit `## Scope` heading.

### Medium

- Clarify whether Structural Exclusions is intended to be a canonical visibility lift or a renderer-level aggregation layer.
- Normalize the metadata-lens presentation so missing canonical lens fields do not appear as empty placeholder structure in HTML.
- Reduce the gap between canonical file names and renderer-facing labels if direct structural traceability is a priority.

### Low

- Tighten subset-specific jump-nav and heading behavior around Section 9 so the navigation label and rendered heading do not drift from one another.
- Reduce helper-layer proliferation if the goal is for HTML to mirror canonical package structure more literally.
