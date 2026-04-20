# Atlas State Page Structural Consistency Report

## Executive Summary

Overall uniformity status: mostly consistent.

All 50 state HTML pages share the same outer rendering shell: hero overview, 10-item jump navigation, two-column content grid, numbered card sections, and a consistent visual system. The strongest consistency is in macro layout. The main structural drift appears in section naming, hero-metadata density, internal card-module composition, and the total absence of page-local return navigation.

The state pages do clearly present themselves as structured jurisdiction packages rather than generic informational pages. At the same time, the HTML rendering order does not match the expected canonical package order. Across the full set, metadata and scope are front-loaded before evidence, and additional structural sections are surfaced before the change log.

---

## Section Ordering Findings

Report: mostly consistent.

- All 50 pages include the same 10-item jump navigation and the same 10 numbered section targets.
- The shared HTML order across the surface is:
  - state overview in the hero block
  - 1. Topology Metadata
  - 2. Scope Boundary Statement
  - 3. Evidence Summary
  - 4. Signals Summary
  - 5. Trust Dimensions Summary
  - 6. Profile Summary
  - 7. Builder Mode Summary
  - 8. Structural Exclusions
  - 9. Evidence Gaps or Scope Boundaries / Scope Boundaries & Canonical Narrowing
  - 10. Change-Log Notes & Normalization Notes
- This means the state HTML pages are structurally consistent with one another, but they do not follow the expected canonical package order literally. Metadata is placed first on all 50 pages rather than after Builder Mode, and Scope Boundary plus Structural Exclusions are surfaced as full sections on all pages.
- No repeated missing-section pattern was detected.
- No repeated extra numbered-section pattern was detected.

Deviations present:

- 45 pages use `9. Evidence Gaps` as the section-9 heading.
- 5 pages use `9. Scope Boundaries & Canonical Narrowing`: `indiana`, `minnesota`, `ohio`, `pennsylvania`, `wisconsin`.
- 4 pages also expose that drift directly in the jump navigation as `9. Scope Boundaries`: `minnesota`, `ohio`, `pennsylvania`, `wisconsin`.

---

## Card Layout Findings

- The outer card structure is highly consistent across all 50 pages.
- Evidence, signals, trust, profile, and builder sections all use the same numbered card shell and heading hierarchy.
- The dominant hierarchy is stable across the set:
  - hero `h1`
  - numbered section `h2`
  - subsection `h3` or equivalent sub-block labels inside cards
- Visual grouping is consistent at the page level because every page uses the same hero, sidebar grid, anchor-target card pattern, and shared styling system.
- Ordering of the major cards is consistent across all 50 pages.

Repeated variations:

- Internal module composition is not fully uniform, even though the outer card shell is.
- A repeated subset of pages uses dashed absence-state callouts inside sections, while others rely more on stacked detail cards and dense summary blocks.
- Repeated support-module drift is visible across the set:
  - 36 pages include `absence-callout` blocks
  - 33 pages include `sources-block` boxes
  - 30 pages include `scope-block` style sub-blocks
  - 20 pages include `detail-list` / `detail-item` stacks
- This produces a mostly consistent layout surface with uneven internal density and grouping inside the middle package sections.

---

## Terminology Findings

- Core package terminology is consistent at the navigation level across all 50 pages:
  - Evidence
  - Signals
  - Trust Dimensions
  - Profile
  - Builder Mode
  - Metadata
- Section naming is consistent in style, but not identical to the expected raw package labels.
- Repeated rendered labels are:
  - `Topology Metadata`
  - `Evidence Summary`
  - `Signals Summary`
  - `Trust Dimensions Summary`
  - `Profile Summary`
  - `Builder Mode Summary`
- This means the HTML surface uses summary-oriented presentation labels rather than exposing the package layer names in their bare form.
- Repeated terminology drift is concentrated in section 9:
  - most pages use `Evidence Gaps`
  - five pages use `Scope Boundaries & Canonical Narrowing`
  - four jump-nav labels shorten that further to `Scope Boundaries`
- No repeated drift was detected toward labels such as `Signal indicators`, `Trust scoring`, `Package metrics`, or `Jurisdiction summary`.

---

## Navigation Findings

- All 50 pages provide strong intra-page navigation through the 10-item jump navigation block.
- No state page includes a page-local return path to the state index.
- No state page includes a page-local return path to the U.S. layer.
- No state page includes a page-local return path to the jurisdiction engine root.
- No state page includes a page-local return path to Atlas root.
- The repeated navigation pattern is therefore downward and intra-page only.
- Broader hierarchy recovery appears to depend on the shared shell rather than explicit links inside the state page source itself.

---

## Corridor Visibility Findings

- Corridor membership is visible across all 50 state pages.
- Every page surfaces corridor placement directly inside `1. Topology Metadata`.
- The recurring visible fields are:
  - Corridor Group
  - Foundation Layer
  - Completion Layer
- Corridor visibility is therefore visible, not merely implied.
- Visibility prominence is not fully uniform:
  - 36 pages include at least one additional hero chip beyond the core four-chip pattern, making corridor or sibling-surface context more prominent on that subset
  - 14 pages keep the more minimal four-chip pattern
- The drift is in emphasis, not in corridor presence.

---

## Package Model Visibility Findings

- The package model is clearly visible across all 50 pages.
- Every page explicitly frames itself as a rendering of a canonical Atlas jurisdiction package.
- Every page also presents a numbered package-style structure rather than a flat article or generic profile page.
- The package model is reinforced by repeated source-of-truth framing in the hero area and by the stable multi-section layout.
- At the same time, the repeated use of `Summary` labels in the middle layers gives the pages a rendered-summary feel rather than a direct package-file feel.

Overall pattern:

- structured jurisdiction package visibility: clear
- informational-summary appearance: partially present through summary-style section labels

---

## Repeated Structural Deviations

- The full HTML state surface uses a shared order that front-loads metadata and scope before evidence, rather than following the expected canonical order directly.
- Section 9 naming drifts across a five-page subset: `indiana`, `minnesota`, `ohio`, `pennsylvania`, `wisconsin`.
- Hero metadata is not structurally uniform:
  - 30 pages populate the `Jurisdiction lens` chip
  - 20 pages leave the chip present but empty
  - 36 pages use a five-chip hero pattern, while 14 pages use four chips
- No page-local upward return navigation is present on any of the 50 pages.
- Internal card-module composition varies across repeated subsets, especially through absence callouts, source blocks, scope blocks, and stacked detail-list rendering.
- No repeated missing-core-section pattern was detected.
- No repeated extra-numbered-section pattern was detected.

---

## Priority Structural Improvements

### High

- Add page-local return paths on every state page to the state index, U.S. layer, jurisdiction engine root, and Atlas root.
- Normalize section-9 presentation so the same structural label appears across all 50 pages.
- Decide whether the HTML rendering should continue to foreground metadata and scope before evidence, or whether it should be reorganized to teach the expected package sequence more directly.

### Medium

- Normalize hero metadata structure so the jurisdiction-lens chip is either consistently populated or consistently omitted.
- Reduce repeated variation in internal card-module composition so evidence, signals, trust, and profile sections feel more uniformly grouped.
- Make corridor emphasis more uniform across the pages that currently use a fifth hero chip and the pages that do not.

### Low

- Reduce minor presentation drift between summary-style labels and the underlying package-layer model.
- Tighten supportive component density so pages with more callout modules do not feel structurally different from pages that rely on denser prose blocks.
