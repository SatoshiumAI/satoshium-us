# ATLAS Renderer Conventions v1

## 1. Purpose

This document defines the renderer contract for Atlas state pages.

Canonical markdown packages are authoritative.

Rendered HTML state pages are a deterministic interpretation surface derived from those canonical packages.

Renderer behavior must remain stable across jurisdictions so that:
- state pages are structurally comparable
- navigation behavior is predictable
- canonical meaning is preserved through rendering
- helper-layer behavior does not drift by state
- future Atlas governance can evaluate renderer compliance consistently

The renderer exists to improve readability, orientation, and navigability without replacing canonical package authority.

## 2. Canonical-to-Renderer Mapping

The renderer shall map the canonical state-package files to the following HTML sections:

- `metadata.md` -> `Topology Metadata`
- `evidence.md` -> `Evidence`
- `signals.md` -> `Signals`
- `trust-dimensions.md` -> `Trust Dimensions`
- `profile.md` -> `Profile`
- `builder-mode.md` -> `Builder Mode`
- `change-log.md` -> `Change Log Notes`

The renderer may expose helper layers that do not exist as standalone canonical files.

Permitted helper layers are:
- `Scope Boundary`
- `Structural Exclusions`
- `Evidence Gaps`

These helper layers are renderer additions.

They do not replace canonical files.

They exist to lift visibility, aggregate distributed canonical constraints, or improve interpretive framing for readers.

## 3. Renderer Section Order

The official renderer order for Atlas state pages is:

1. Hero
2. Topology Metadata
3. Scope Boundary
4. Evidence
5. Signals
6. Trust Dimensions
7. Profile
8. Builder Mode
9. Structural Exclusions
10. Evidence Gaps
11. Change Log Notes

This order differs intentionally from canonical file order.

Canonical package order remains authoritative at the markdown level.

Renderer order is a governed presentation sequence designed to:
- front-load orientation
- surface topology context early
- preserve the interpretation spine in the middle of the page
- place helper-layer constraint material after the core interpretive sequence
- keep change-log material at the end of the rendered surface

## 4. Core Interpretation Spine (Invariant)

The renderer shall preserve the following invariant sequence:

Evidence -> Signals -> Trust -> Profile -> Builder

This sequence is the core interpretation spine of every Atlas state page.

This ordering must never change.

Renderer-specific helper layers may appear before or after the spine only as permitted by this document.

No renderer variation may reorder, interleave, or fragment the core interpretation spine.

## 5. Section 9 Policy (Evidence Gaps)

`Evidence Gaps` is the universal Section 9 heading for Atlas state pages.

Permitted substructures inside Section 9 include:
- gap inheritance
- canonical narrowing
- derived scope limits

These substructures may appear as:
- subheads
- callouts
- summary paragraphs
- structured lists

Alternate Section 9 titles are not permitted.

Disallowed examples include:
- `Scope Boundaries`
- `Scope Boundaries & Canonical Narrowing`
- any state-specific replacement heading for Section 9

When narrowing or inheritance logic is present, it shall be rendered inside `Evidence Gaps`, not by replacing the section heading.

## 6. Scope Boundary Policy

Every Atlas state page may render a `Scope Boundary` section.

Scope Boundary rendering is universal at the renderer level.

Permitted derivation sources are limited to:
- explicit `## Scope` headings in canonical files
- boundary language present in `evidence.md`
- narrowing logic present in `change-log.md`

The renderer shall not create synthetic scope content.

The renderer may summarize or normalize canonical boundary language for readability, but it shall not introduce new scope restrictions, new scope expansions, or new interpretive claims not grounded in canonical package materials.

When explicit `## Scope` material is absent, the rendered Scope Boundary section must remain derived from existing canonical boundary language only.

## 7. Renderer Compression Rules

The renderer may apply controlled compression to improve readability and presentation consistency.

Allowed renderer behavior:
- heading normalization
- summary-first restructuring
- block merging
- absence-callouts
- change-log redistribution
- source-note normalization
- helper-layer aggregation where permitted by this document

Heading normalization means renderer-facing headings may be shorter or more presentation-oriented than canonical headings, provided semantic coverage is preserved.

Summary-first restructuring means the renderer may front-load concise summaries before detailed supporting blocks.

Block merging means adjacent canonical framing blocks may be combined when no meaning is lost.

Absence-callouts may be used to surface non-establishment, insufficiency, or structural constraint language already present in canonical materials.

Change-log redistribution is permitted only under the rules defined in Section 13.

Not allowed:
- signal invention
- evidence invention
- trust scoring
- scorecard rendering
- builder inference beyond canonical text
- state-specific section-order variation
- invention of new corridor roles
- invention of new metadata fields
- synthetic exclusions not grounded in canonical materials

Renderer compression must preserve canonical meaning even when canonical block boundaries are normalized.

## 8. Metadata Label Normalization

The renderer may normalize:

`Topology completion layer` -> `Completion Layer`

This is a semantic normalization rule.

It is not drift.

The canonical meaning must remain unchanged.

The renderer may also normalize capitalization and display form for metadata labels when needed for consistent presentation, provided the underlying metadata field identity remains intact.

The canonical metadata contract remains:
- Corridor Group
- Foundation Layer
- Topology completion layer

The rendered display contract remains:
- Corridor Group
- Foundation Layer
- Completion Layer

## 9. Corridor Classification Contract

The canonical corridor classification contract for state pages consists of the trio:
- Corridor Group
- Foundation Layer
- Completion Layer

This trio is the only canonical corridor-state metadata contract for renderer purposes.

Classification families such as:
- Energy–Compute
- Research
- Interconnection

are annotation only.

They are not metadata schema fields.

They are not alternate per-state classification assignments.

They may appear in corridor documentation as descriptive grouping language, but they shall not be rendered as if they were canonical state metadata unless a future schema explicitly authorizes them.

## 10. Hero Chip Schema

The renderer shall use a controlled hero-chip schema.

Required chips:
- Jurisdiction
- Completeness
- Surface assignment

Optional chips:
- Jurisdiction Lens, only if present canonically
- one approved context chip

Jurisdiction Lens may be rendered only when canonical metadata or approved canonical package materials provide that lens explicitly.

Empty Jurisdiction Lens placeholders are not permitted.

Only one optional context chip may be added.

That chip must come from an approved controlled set defined by renderer policy.

Freeform chip expansion is not permitted.

The hero layer shall not expand into an uncontrolled annotation surface.

The corridor trio shall not be rendered as three separate hero chips.

Full corridor classification belongs in `Topology Metadata`.

## 11. Helper Layers

Permitted helper layers are:
- Scope Boundary
- Structural Exclusions
- Evidence Gaps

These helper layers may function as:
- visibility lifts
- aggregation layers
- interpretive framing layers

Definitions:

A visibility lift makes embedded canonical material easier to see without changing its meaning.

An aggregation layer collects distributed canonical constraint material into a single reader-facing section.

An interpretive framing layer explains canonical constraints in a stable renderer-facing form without replacing canonical authority.

Helper layers are not canonical replacements.

They shall not:
- stand in for canonical files
- delete canonical meaning
- add unsupported factual material
- create new downstream authority beyond canonical content

## 12. Navigation Minimums

Every rendered Atlas state page shall include explicit upward navigation links to:
- the state index
- the U.S. layer
- the jurisdiction engine root
- the Atlas root

These links may appear as breadcrumbs, return links, or equivalent governed navigation elements.

Shared-shell navigation alone is not sufficient.

State pages must support local hierarchy recovery inside the page itself.

## 13. Change Log Rendering Rules

The renderer may apply controlled normalization to `change-log.md` content.

Allowed:
- heading compression
- gap inheritance redistribution
- summary narration

Heading compression means adjacent canonical change-log headings may be rendered under fewer visible headings when semantic coverage is preserved.

Gap inheritance redistribution means inheritance logic may appear inside `Evidence Gaps` rather than only inside `Change Log Notes`.

Summary narration means the renderer may introduce stable framing language that explains what the change log records.

Not allowed:
- policy reinterpretation
- new normalization claims
- content invention
- new scope claims not grounded in canonical materials
- new exclusions not grounded in canonical materials

The renderer may summarize change-log structure, but it shall not rewrite the meaning of the canonical record.

## 14. Renderer Compliance Definition

A rendered Atlas state page is renderer-compliant only when all of the following are true:

- all canonical sections are visibly surfaced
- the core interpretation spine is preserved as `Evidence -> Signals -> Trust -> Profile -> Builder`
- Section 9 is standardized as `Evidence Gaps`
- metadata is surfaced through the canonical trio display contract
- no synthetic signals are introduced
- no synthetic evidence is introduced
- no trust scoring is introduced
- builder interpretation does not exceed canonical text
- helper layers remain governed by this document
- the hero-chip schema is respected
- upward navigation minimums are present
- renderer order matches the official section order defined in this document

Non-compliance occurs when any of the following are true:
- canonical section visibility is lost
- the interpretation spine is reordered
- Section 9 is renamed or structurally replaced
- synthetic scope is introduced
- unsupported metadata fields are rendered as canonical state metadata
- freeform chip expansion is used
- scoring or unsupported inference appears in Trust or Builder rendering
- change-log rendering introduces new claims not present canonically

## Version

v1 — Initial Atlas renderer conventions specification
