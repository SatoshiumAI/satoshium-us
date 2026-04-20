# Atlas Normalization Priority Plan

## Executive Summary

The completed Atlas audits point to one clear conclusion: the state-page system is already stable enough to normalize by policy and shared template rules, not by 50 separate manual redesigns.

The strongest parts of the current system are:
- consistent 50-state rendering shell
- strong file-level visibility of canonical package content
- exact corridor-trio alignment across matrix, metadata, and HTML topology fields
- strong semantic preservation inside Evidence, Signals, Trust, Profile, Builder Mode, and Metadata

The weakest parts are not core data accuracy. They are renderer policy gaps:
- undocumented section-order drift from canonical package order
- inconsistent Section 9 behavior
- undocumented universal Scope Boundary rendering
- hero-chip schema drift
- corridor-family language that reads as taxonomy but behaves as annotation
- missing framework documentation for renderer conventions

Recommended normalization strategy:
- keep one fixed renderer model across all state pages
- document that model explicitly
- normalize the small number of repeated drift points that appear across the whole surface
- avoid page-by-page exception growth

## Renderer Policy Decisions

### Decision 1: Should Atlas preserve canonical package order in HTML?

**Recommendation: no literal one-to-one package-order mirroring.**

Instead, Atlas should formalize a documented renderer order.

Reason:
- the current metadata-first HTML pattern is already consistent across all 50 pages
- front-loading topology and scope improves orientation before evidence-heavy sections
- the bigger problem is not that the order is different, but that the difference is undocumented

Recommended renderer order:
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
11. Change-Log Notes

Policy note:
- the canonical middle block must remain stable as `Evidence -> Signals -> Trust -> Profile -> Builder`
- the metadata-first preface and post-core helper layers should be treated as renderer structure, not canonical file order

### Decision 2: Should Section 9 behavior be standardized?

**Recommendation: yes, immediately.**

Recommended rule:
- use `Evidence Gaps` as the universal Section 9 heading on all state pages
- place `gap inheritance`, `scope boundaries`, and `canonical narrowing` inside Section 9 as subheads or callouts when needed
- do not allow state-specific replacement of the section heading

Reason:
- current five-state drift creates unnecessary template branching
- Section 9 is the clearest repeated renderer divergence across the 50-state set
- a stable heading with controlled sub-variants preserves nuance without fragmenting the layout model

### Decision 3: Should Scope Boundary Statement rendering be universalized?

**Recommendation: yes, but only as an explicit renderer convention.**

Recommended rule:
- every state page may render a Scope Boundary section
- when `evidence.md` contains an explicit `## Scope`, render it directly
- when it does not, the renderer may derive the section only from approved boundary language already present in canonical package materials
- no new scope claims should be synthesized beyond those approved boundary sources

Reason:
- Scope Boundary is already universal across the state surface
- the section is useful for reader orientation
- the real issue is lack of derivation rules, not the section’s existence

### Decision 4: Core renderer rule set

The renderer conventions should explicitly state:
- no scoring language
- no synthetic signal invention
- no inferred builder positioning beyond canonical files
- no state-specific section order exceptions without framework justification
- summary compression is allowed only when semantic coverage is preserved

## Navigation Policy Decisions

### Decision 1: State-page upward navigation

**Recommendation: add explicit page-local return paths on every state page.**

Minimum required links:
- back to state index
- back to U.S. layer
- back to jurisdiction engine root
- back to Atlas root

Reason:
- all 50 state pages currently depend too heavily on shared-shell recovery
- the pages are strong for intra-page navigation but weak for hierarchy recovery

### Decision 2: Entry-layer hierarchy teaching

**Recommendation: strengthen layer framing at the top of Atlas.**

Required clarifications:
- Atlas root should teach the layer model more directly
- corridor index should show how corridor navigation relates to jurisdiction-engine navigation
- jurisdiction engine and U.S. layer should be more clearly differentiated
- state directory should explain what a state package contains before entry

### Decision 3: State-directory navigation cleanup

**Recommendation: fix dead A-Z anchors immediately.**

Reason:
- this is a visible navigation defect on one of the strongest entry surfaces
- it is easy to correct and improves trust in the navigation system

### Decision 4: Matrix navigation

**Recommendation: add direct matrix-to-state exploration paths.**

Reason:
- the corridor assignment matrix is structurally strong but operationally isolated
- users should be able to move from a matrix row into the corresponding state package without manual lookup

## Corridor Taxonomy Decisions

### Decision 1: Are classification families taxonomy or annotation?

**Recommendation: formalize them as annotation for now.**

That includes:
- Energy–Compute
- Research
- Interconnection
- and related corridor-family language on the corridor index

Reason:
- the canonical state system is the trio only: Corridor Group, Foundation Layer, Completion Layer
- the family labels are not encoded in state metadata or HTML topology fields
- presenting them as taxonomy today creates ambiguity about which system is authoritative

Policy note:
- if Atlas later wants a second corridor-family classification layer, it should be added as an explicit canonical field set, not implied through corridor-index prose alone

### Decision 2: Corridor trio authority

**Recommendation: keep the trio as the only canonical corridor-state classification contract.**

Authoritative trio:
- Corridor Group
- Foundation Layer
- Topology completion layer / Completion Layer

### Decision 3: Corridor vocabulary precision

**Recommendation: normalize corridor-index example labels to exact canonical labels where precision matters.**

Reason:
- the current example-level simplification around the Mountain West research foundation label shows how vocabulary can loosen even when the underlying matrix is stable

## Hero Chip Decisions

### Decision 1: Should Atlas expose the corridor trio in hero chips?

**Recommendation: no, not as three separate hero chips.**

Reason:
- the hero layer is already drifting through optional fifth-chip behavior
- adding all three topology fields there would increase density and duplication
- the full trio is already clearly available in Section 1 Topology Metadata

Preferred approach:
- keep the full trio in Topology Metadata
- keep the hero layer focused on identity and high-level package state

### Decision 2: Standard hero-chip schema

**Recommendation: replace the current semi-open chip pattern with a controlled schema.**

Required hero chips:
- Jurisdiction
- Completeness
- Surface assignment

Optional hero chips:
- Jurisdiction lens, only when canonical metadata contains a lens
- one approved context chip, only if the renderer policy explicitly allows it

This means:
- remove empty `Jurisdiction lens` placeholders
- stop mixing uncontrolled extras such as adjacency-bounded, sibling, evidence-absence, package-status, and cross-foundation chips unless they are formalized into an approved enum

### Decision 3: Optional context-chip policy

**Recommendation: if a fifth chip is retained, it should come from a documented finite set.**

Possible sanctioned classes could include:
- sibling relationship
- adjacency-bounded package
- evidence-absence package

But only if those classes are formally defined and used consistently.

## Section Ordering Decisions

### Decision 1: Adopt one fixed renderer order

**Recommendation: yes.**

Policy:
- all state pages should use the same ordered renderer model
- no per-state section-order branching
- no state-specific Section 9 heading replacement

### Decision 2: Preserve canonical sequence inside the core interpretation block

**Recommendation: yes.**

Required invariant:
- `Evidence -> Signals -> Trust Dimensions -> Profile -> Builder Mode`

This block should remain the interpretive spine of every rendered state page.

### Decision 3: Helper-layer placement

**Recommendation: formalize helper-layer placement rather than allowing drift.**

Recommended placement:
- Topology Metadata and Scope Boundary before the core interpretation block
- Structural Exclusions and Evidence Gaps after the core block
- Change-Log Notes last

This preserves the current high-level reading flow while making it explicit.

## Framework Documentation Decisions

### Decision 1: Should Atlas create a renderer conventions framework document?

**Recommendation: yes, immediately.**

This is the highest-leverage normalization action.

Suggested document purpose:
- define how canonical files become HTML state pages
- define which transformations are allowed
- define which helper layers are permitted
- define chip policy, label policy, and section-order policy

### Decision 2: What the framework document must cover

Minimum required sections:
- renderer order versus canonical file order
- Section 9 policy
- Scope Boundary derivation rules
- Structural Exclusions policy
- gap inheritance handling
- canonical narrowing handling
- hero-chip schema
- label normalization rules, including `Topology completion layer` -> `Completion Layer`
- corridor-family status: taxonomy or annotation
- navigation minimums for state pages
- allowed compression rules for trust, profile, builder, and change-log rendering

### Decision 3: Resolve source-path drift

**Recommendation: restore or replace the missing named framework source intentionally.**

The audits found that `signals-update-protocol.md` was not present at the referenced path, while nearby framework documents do exist.

Required action:
- either create the expected renderer-conventions document at the referenced location
- or clearly supersede that reference with a renamed framework file and update all tasking and documentation accordingly

## Implementation Priority Roadmap

### Immediate

- Create the renderer conventions framework document.
- Formalize the state-page renderer order as a documented policy.
- Standardize Section 9 to universal `Evidence Gaps` with controlled sub-variants inside the section.
- Formalize universal Scope Boundary rendering and its derivation rules.
- Declare corridor classification families to be annotation, not canonical taxonomy.
- Define the hero-chip schema and remove empty Jurisdiction Lens placeholders.

### Near-term

- Add page-local upward navigation on all state pages.
- Fix dead A-Z anchors on the U.S. state directory.
- Add matrix-to-state navigation links.
- Normalize corridor-index example vocabulary to canonical trio values where precision matters.
- Normalize optional fifth-chip usage, if retained at all.
- Document label normalization, especially `Topology completion layer` -> `Completion Layer`.

### Later

- Harmonize internal section-template density across evidence, signals, trust, profile, and builder blocks.
- Reduce template-family drift between compact-list and summary-first render modes where consistency improves readability.
- Tighten narrator-voice consistency in rendered summary text.
- Consider whether future corridor-family taxonomy should become a real canonical layer, but only after explicit schema design rather than documentation drift.
