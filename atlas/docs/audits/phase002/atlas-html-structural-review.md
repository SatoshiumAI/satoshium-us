# Atlas HTML Structural Review

## Executive Summary

The Atlas HTML surface is structurally strong at the top level and becomes weaker at the deepest navigation layer.

Atlas root, corridor, engine, U.S. entry, and state index pages all present a recognizable hierarchy and a consistent visual shell. The biggest structural weakness is the state-page layer, where all 50 pages lose visible return paths back to the state index, U.S. layer, and broader engine. A second recurring issue is taxonomy and labeling drift across surfaces, especially between corridor classification language and state-page section labels.

Overall structural condition: clear macro-hierarchy, good visual consistency, incomplete cross-surface navigation at the page-detail layer.

## Atlas Root Findings

- `atlas/index.html` clearly states that Atlas is the jurisdiction intelligence layer of Satoshium.
- The root page clearly exposes four primary entry points: Jurisdiction Intelligence Engine, Corridors Index, United States Package, and U.S. State Index.
- The page does explain that corridors connect normalized state packages into topology structures, so the relationship between Atlas, corridors, and state packages is present at a high level.
- Navigation is easy to understand from the root because the main options are card-based and visually separated.
- Missing framing layer: the root page does not explain the internal anatomy of a state package, so users do not learn what evidence, signals, trust dimensions, profile, and builder mode mean before entering deeper pages.
- Missing framing layer: the root page names corridor structures and state packages, but it does not clearly describe how the corridor index, the corridor matrix, and the jurisdiction engine differ from one another in user terms.
- Structural note: the Corridors card contains a small markup irregularity around the second CTA block, which may affect spacing or DOM cleanliness even if the page still renders.

## Corridor Layer Findings

### Corridor Index

- `atlas/corridors/index.html` explains the corridor layer clearly as the topology layer connecting normalized state packages.
- The page explains the relationship between corridors and states well at the structural level.
- The page also links back to Atlas and forward to U.S. state packages and the corridor matrix, so the layer is not isolated.
- Relationship to the jurisdiction engine is only partly visible. The corridor page points directly to U.S. state packages, but it does not offer a direct return path to the jurisdiction engine root.
- Taxonomy clarity is mixed. The page first presents the canonical structural trio, Corridor Group, Foundation Layer, and Topology Completion Layer, then introduces a second set of “Corridor Classification Families” such as Energy–Compute Corridors and Research Corridors.
- Because the page does not explicitly connect those two schemes, it creates a structural risk of taxonomy drift. Users can read the page as if there are two corridor systems instead of one corridor system described through two lenses.

### Corridor Assignment Matrix

- `atlas/corridors/corridor-assignment-matrix.html` has a strong structural introduction and clearly states the three matrix dimensions.
- Terminology is consistent with the corridor index and the Atlas topology language.
- The sticky-header table and explanatory cards improve readability on desktop.
- Structural density is high. The table is wide, uses a `min-width` layout, and depends on horizontal scrolling on narrow screens.
- The matrix is canonical but somewhat isolated. Rows are not linked directly to state pages, and corridor names are not linked to any corridor-detail surfaces.
- The matrix does explain how Atlas uses the assignments, but it does not provide a direct structural bridge from a row entry into state-level exploration.
- Alignment with corridor membership logic is conceptually stated, but not operationally surfaced through page-level cross-links.

## Jurisdiction Engine Findings

- `atlas/jurisdiction-intelligence-engine/index.html` is structurally clear as the engine entry page.
- The page explains its purpose well: national entry first, then routing into state indexes and other sub-surfaces.
- Hierarchy is visible from the layout. The two primary cards create a clear path to the U.S. layer and directly to the state index.
- The page uses badges and expansion cards effectively to show future scale without overloading the current navigation.
- Missing framing layer: the page says packages are “evidence-aligned,” but it does not actually explain the evidence-first structure of state pages.
- Missing framing layer: there is no explicit explanation of what signals interpretation or trust dimensions are, even though those layers are central to how state pages are organized.
- State package role is partly clear, but mostly through navigation language rather than through a concise structural explanation of the package stack.

## U.S. Layer Findings

- `atlas/jurisdiction-intelligence-engine/us/index.html` clearly functions as a national entry layer above the state index.
- The page explains its role as a U.S. routing surface and separates the national layer from the engine root cleanly.
- Entry into state packages is clear through the primary CTA to the U.S. state index.
- Hierarchy is visible, but lightly. The page communicates “engine root -> U.S. layer -> state index,” yet it does not provide a visible breadcrumb or return link back to the engine root.
- Structurally, this page is somewhat redundant with the engine root because both pages emphasize routing into states and future expansion.
- The U.S. page is still useful as a hierarchy layer, but its differentiation from the engine root depends more on page intent than on distinct navigation structure.

## State Index Findings

- `atlas/jurisdiction-intelligence-engine/us/states/index.html` is one of the stronger navigation surfaces in the stack.
- State discovery is easy because the page offers both a clickable tile map and an alphabetical index.
- Naming and state-link presentation are visually consistent within the page.
- Discovery flow is strong for users who already know they want a state.
- Structural issue: the A–Z letter nav includes letters with no corresponding section anchors. Missing targets were detected for `B`, `E`, `J`, `Q`, `X`, `Y`, and `Z`.
- Those dead anchor links create scan friction and weaken the otherwise clean state-index flow.
- Structural issue: the return link to the U.S. layer uses an absolute production URL, while most other internal navigation in the HTML surface is relative or root-relative. This creates link-style inconsistency across the reviewed pages.
- Missing framing layer: the page explains how to find a state, but not what users should expect once they land inside a state package.

## State Page Consistency Findings

The nine sampled pages, California, Texas, New York, Florida, Wyoming, Virginia, Illinois, Michigan, and Indiana, match the whole-surface consistency sweep closely.

### Strong consistency patterns across all 50 state pages

- All 50 state pages use the same overall shell, hero block, jump navigation, sidebar layout, and card-based section rendering.
- All 50 state pages contain a 10-link jump navigation block at the top.
- The section order is highly consistent across the full set.
- Titles follow a shared format: `<State> — Atlas: Jurisdiction Intelligence Engine | Satoshium`.
- The topology, scope, evidence, signals, trust, profile, builder-mode, exclusions, gaps, and change-log pattern is visually stable across the surface.

### Structural inconsistencies across the 50-page set

- No reviewed state page provides a visible breadcrumb, return-to-state-index link, return-to-U.S.-layer link, or return-to-engine link in the body content.
- The state pages therefore behave like terminal leaves with no local return path, even though they are part of a larger hierarchy.
- Hero metadata is inconsistent. Some pages display a populated “Jurisdiction lens” chip, while 20 pages display an empty `Jurisdiction lens` chip with no value.
- Section terminology drifts at section 9. Most state pages use `Evidence Gaps`, while a smaller set uses `Scope Boundaries & Canonical Narrowing`.
- Section labels for the middle layers use `Summary` wording, such as `Signals Summary` and `Trust Dimensions Summary`, which is structurally close to the canonical package layers but not identical.
- Card counts vary significantly by state page, which is acceptable as a content result, but it makes lower-page visual rhythm less uniform.

### Sample-page observations

- California, Texas, New York, Florida, and Wyoming all show the same main rendering architecture and section jump pattern.
- Indiana shows one of the observed label drifts at section 9.
- Virginia, Illinois, and Michigan fit the same overall shell, confirming that the sampled variation is minor compared with the core state-page template consistency.

## Cross-Surface Structural Issues

- **Missing local return paths at the state layer:** the deepest pages do not visibly connect back upward to the state index, U.S. layer, or engine root.
- **Dead anchor links on the state index:** the A–Z navigation includes letters without matching sections.
- **Taxonomy drift in the corridor layer:** the corridor index mixes canonical matrix dimensions with corridor-family language without clearly tying them together.
- **Label drift across state pages:** state-page sections are mostly aligned, but not fully uniform, especially at section 9 and in hero-chip population.
- **Matrix isolation:** the corridor matrix is structurally important but not connected to state pages or corridor detail surfaces through row-level links.
- **Hierarchy explanation gaps:** Atlas root and engine entry pages explain purpose well, but do not consistently explain the evidence-first package stack before users enter detailed state pages.
- **Navigation style inconsistency:** some pages use relative links, some root-relative links, and the state index includes an absolute production return link.
- **Shared-shell dependency:** topbar and footer navigation depend on externally fetched shared assets, so page-local navigation is lighter than it appears in source review.

## Priority Structural Improvements

### High

- Add visible upward navigation on all 50 state pages so each page clearly links back to the U.S. state index, U.S. layer, and engine root.
- Remove or resolve dead A–Z anchor links on the U.S. states index.
- Clarify the structural bridge between corridor pages, the corridor matrix, and state pages so users can move laterally and upward, not only downward.

### Medium

- Normalize state-page hero metadata so the jurisdiction-lens slot is either consistently populated or consistently omitted.
- Normalize section labeling across state pages, especially the section 9 variation.
- Clarify the relationship between corridor classification dimensions and corridor-family language on the corridor index.
- Add a clearer package-stack explanation on Atlas root and the jurisdiction engine entry so users understand the evidence-first architecture before entering state pages.
- Reduce matrix isolation by making its structural relationship to state pages more explicit in navigation terms.

### Low

- Normalize internal link style across the reviewed HTML surfaces.
- Tighten small markup irregularities on Atlas root and related pages where DOM structure is less clean than the broader page system.
- Reduce visual rhythm drift in long state pages where card counts create noticeably different page lengths and pacing.
