# Atlas HTML ↔ Canonical Content Drift Report

## Executive Summary

The HTML state pages preserve canonical meaning much better than they preserve canonical structure.

Across the full 50-state surface, the core renderer behavior is paraphrastic compression, not wholesale reinterpretation. Evidence, signals, trust dimensions, profile, builder mode, metadata, and change-log content are generally carried forward into HTML with strong semantic continuity. The repeated drift is in packaging: headings are normalized, some framing blocks are merged, exclusions and gaps are aggregated, and change-log logic is redistributed into dedicated renderer sections.

The strongest content alignment appears in Evidence, Signals, Metadata, and most Builder Mode sections. The most repeated renderer transformation appears in Trust Dimensions, Profile, and Change-Log Notes, where canonical blocks are frequently reorganized into summary-first HTML patterns. The clearest synthesis behavior remains concentrated in Scope Boundary Statement, Evidence Gaps, and Scope Boundaries & Canonical Narrowing.

Overall result: repeated renderer summarization and aggregation are present, but repeated factual invention inside the core layer sections was not detected.

## Evidence Coverage Findings

- Major evidence-category coverage is strong across the full surface.
- Evidence-category count is preserved on 49 of 50 pages at the renderer level, with one hybrid outlier that expands a category into an extra rendered block rather than dropping one.
- The dominant renderer behavior is one evidence block per canonical evidence category.
- A secondary renderer behavior packages evidence in denser summary blocks with embedded bullets and explicit source scaffolding, but still tracks the canonical category set.
- Source handling is normalized by the renderer rather than drifted semantically. Some pages use inline “Sources cited by evidence.md” notes, while others use dedicated source blocks.
- No repeated pattern of omitted evidence categories was detected.
- No repeated pattern of synthesized evidence claims beyond the canonical evidence layer was detected.

## Signals Coverage Findings

- Signal coverage is strong and usually remains one rendered unit per canonical signal.
- Signal-unit parity is retained on 47 of 50 pages.
- The remaining small subset does not show a repeated pattern of invented signals. Instead, the renderer adds framing or non-establishment context around the existing signal set.
- Two main renderer patterns appear:
  - compact signal detail-list rendering
  - one subhead plus paragraph per signal cluster
- 29 pages add explicit absence or non-establishment callouts in the Signals section. These function as visibility lifts for signal constraints and exclusions, not as inferred new signals.
- No repeated pattern of signal scoring, ranking, or synthetic inference language was detected.

## Trust Dimension Coverage Findings

- Trust-dimension logic is always surfaced, but often not block-for-block.
- The dominant renderer transformation is summary-first restructuring.
- Two repeated HTML trust patterns appear:
  - compact detail-item summaries for one subset of states
  - expanded trust-matrix rendering for another subset, using fields such as Current interpretation, Supporting basis, Constraint basis, and Atlas reading
- In the expanded pattern, the canonical `Trust interpretation summary` is usually absorbed into an introductory summary block and then followed by the dimension-specific readings.
- This means the renderer frequently partially summarizes trust structure rather than reproducing the canonical trust file heading-for-heading.
- No repeated conversion of trust logic into numeric scoring, ranking, or scorecard language was detected.
- The repeated behavior is reformatting and controlled paraphrase, not trust-model reinvention.

## Profile Coverage Findings

- Profile framing is mostly preserved, but some pages compress profile structure.
- 42 of 50 pages retain the same number of profile content units after rendering.
- 8 pages compress one profile framing block by folding Jurisdiction summary, Profile synthesis, or Profile synthesis statement together rather than preserving each as a separate visible unit.
- Two main renderer patterns appear:
  - direct rendering of canonical profile keys as compact profile items
  - narrative profile rendering through Jurisdiction summary, synthesis bullets, and a closing synthesis statement
- The repeated renderer behavior is to preserve profile meaning while simplifying block boundaries.
- No repeated pattern of added profile interpretation beyond the canonical profile layer was detected.

## Builder Mode Coverage Findings

- Builder Mode is largely preserved as a strategy-interpretation layer.
- Once renderer-normalized intro handling is accounted for, Builder Mode remains one of the more faithful HTML sections.
- 38 of 50 pages preserve the same number of builder content units after rendering normalization.
- Repeated renderer transformations include:
  - moving canonical intro or interpretive-read framing into an HTML scope or role-summary paragraph
  - collapsing scenario guidance into a smaller set of pattern headings
  - adding an explicit HTML Scope paragraph on 10 pages
- A small subset of pages compresses one builder framing block, while another subset adds one renderer-facing framing block without changing the underlying builder meaning.
- No repeated pattern of inferred builder positioning beyond canonical builder-mode content was detected.

## Metadata Coverage Findings

- Metadata coverage is strong and consistent.
- All 50 pages visibly surface the core topology fields from `metadata.md`.
- Repeatedly preserved metadata elements include:
  - Corridor Group
  - Foundation Layer
  - Topology completion field, rendered as `Completion Layer`
  - Classification source
  - Interpretation boundary
  - Metadata status
- `metadata.md` contains a canonical `Jurisdiction lens` heading in 30 states, and the HTML Topology Metadata section surfaces that field in all 30 corresponding cases.
- The remaining 20 states do not lose a canonical metadata field because none exists there; the renderer mismatch is instead the empty hero-chip placeholder outside the Topology Metadata section.
- The main repeated metadata transformation is label normalization: HTML uses `Completion Layer` instead of the canonical heading `Topology completion layer`.
- No repeated metadata-field omission was detected.

## Change Log Coverage Findings

- Change-log meaning is mostly preserved, but change-log structure is the most repeatedly compressed part of the renderer.
- 41 of 50 pages preserve the same number of visible change-log blocks.
- 9 pages collapse one or more canonical change-log headings into fewer rendered subheads.
- The most repeated redistribution pattern is `Gap inheritance` movement:
  - 18 canonical packages contain a distinct `Gap inheritance` heading in `change-log.md`
  - the HTML surface moves that logic into Section 9 rather than keeping it as a standalone Change-Log Notes block
- The HTML renderer also standardizes narration with phrases like “The change-log records that...”, but this appears to be renderer voice rather than added normalization claims.
- The repeated behavior is change-log compression and redistribution, not repeated change-log invention.

## Renderer Synthesis Behavior

### Scope Boundary Statement without canonical scope heading

- Detected in 12 states.
- Classification: visibility lift with renderer synthesis.
- In these cases, HTML creates a standalone Scope Boundary Statement even though `evidence.md` does not contain an explicit `## Scope` heading.
- The added material appears to be derived from existing evidence-layer boundary language rather than from new factual claims.
- This is not strong evidence drift, but it is renderer-added interpretive structure.

### Evidence Gaps without canonical gaps section

- Detected in 1 clear case: `michigan`.
- Classification: aggregation layer.
- HTML renders `Evidence Gaps` even though `evidence.md` does not contain an explicit evidence-gaps heading.
- The page explains that the gap structure is carried by downstream layers instead.
- This is synthesized visibility, not repeated factual drift.

### Scope Boundaries & Canonical Narrowing derived from change-log logic

- Detected in 5 states: `indiana`, `minnesota`, `ohio`, `pennsylvania`, `wisconsin`.
- Classification: interpretation layer.
- Here the renderer does more than lift visibility. It repackages change-log or narrowed-scope logic into a dedicated explanatory section that replaces the standard Evidence Gaps presentation.
- This is the strongest repeated synthesis pattern in the HTML renderer.
- It remains grounded in canonical material, but it is not a direct file-level rendering.

### Overall synthesis assessment

- Core layer sections mostly behave as semantic paraphrases of canonical files.
- Repeated synthesis is concentrated in helper layers, especially scope and gap presentation.
- Repeated true factual drift inside Evidence, Signals, Trust Dimensions, Profile, Builder Mode, or Metadata was not detected.

## Priority Alignment Targets

### High

- Normalize Section 9 behavior so Evidence Gaps, Gap inheritance, and Scope Boundaries & Canonical Narrowing follow one explicit renderer rule.
- Decide whether Scope Boundary Statement should be rendered only when a canonical `## Scope` heading exists, or whether universal boundary rendering is intentional.
- Reduce change-log redistribution when direct traceability from canonical headings to rendered headings is important.

### Medium

- Normalize trust, profile, and builder framing so renderer compression does not vary as much between direct-list and summary-first templates.
- Normalize metadata label presentation, especially `Topology completion layer` versus `Completion Layer`.
- Standardize how evidence-source scaffolding is shown so source visibility is consistent without changing evidence meaning.

### Low

- Harmonize renderer narrator voice across sections so paraphrase style is more uniform.
- Reduce small template-family drift where some pages add role-summary or scope blocks while others keep the equivalent framing inside canonical-style subsection headings.
