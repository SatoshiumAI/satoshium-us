# ATLAS Package Schema v1

## 1. Purpose

This document defines the canonical jurisdiction package contract for Atlas.

Canonical packages are the Atlas source-of-truth layer.

The renderer consumes canonical packages but does not redefine their meaning.

Schema stability enables:
- cross-jurisdiction comparability
- renderer consistency
- governance reviewability
- future package portability across Atlas surfaces
- controlled extension without schema drift

Every jurisdiction package is a governed interpretation bundle.

Its files work together as a layered canonical system.

## 2. Package Directory Structure

The expected canonical jurisdiction package structure is:

- `metadata.md`
- `evidence.md`
- `signals.md`
- `trust-dimensions.md`
- `profile.md`
- `builder-mode.md`
- `change-log.md`

All files are canonical interpretation inputs.

No file is decorative.

Each file contributes a distinct layer of package meaning.

Together they define the canonical state package consumed by Atlas renderers and related governance tooling.

## 3. Required vs Optional Files

### Required files

The following files are required for a schema-compliant jurisdiction package:
- `metadata.md`
- `evidence.md`
- `signals.md`
- `trust-dimensions.md`
- `profile.md`
- `builder-mode.md`
- `change-log.md`

### Optional future extensions

The following files are reserved for possible future schema adoption:
- `adjacency.md`
- `corridor-overrides.md`
- `federal-overlays.md`
- `international-interfaces.md`

These extension files are reserved but inactive unless explicitly adopted by a later schema version.

They are not part of the required v1 package contract.

No renderer or governance layer should assume their existence unless a future framework document formally activates them.

## 4. metadata.md Schema

`metadata.md` defines the package topology contract and metadata boundary conditions.

### Required fields

`metadata.md` shall contain the following required fields:
- `Corridor Group`
- `Foundation Layer`
- `Topology completion layer`
- `Classification source`
- `Interpretation boundary`
- `Metadata status`

### Optional field

`metadata.md` may contain:
- `Jurisdiction lens`

### Contract requirements

The corridor trio is the only canonical topology contract:
- Corridor Group
- Foundation Layer
- Topology completion layer

`Classification source` shall explain the provenance of topology classification.

`Interpretation boundary` shall define what metadata does not do.

`Metadata status` shall record attachment or package-status state relevant to metadata governance.

`Jurisdiction lens` appears only when explicitly present in canonical metadata.

No inferred lens is permitted.

## 5. evidence.md Schema

`evidence.md` defines the canonical evidentiary layer of the jurisdiction package.

### Responsibilities

`evidence.md` may contain and organize:
- establishment status
- legal anchors
- infrastructure presence
- policy instruments
- negative evidence
- boundary conditions

### Permitted structural elements

`evidence.md` may include:
- `Scope` headings
- `Evidence gaps` headings
- constrained documentary subsections
- explicit exclusions grounded in evidence boundaries

### Constraints

`evidence.md` shall not introduce:
- interpretive scoring
- ranking language
- unsupported deployment conclusions
- synthetic signals

Evidence is the canonical establishment layer.

It records what is supported, what is not established, and where package boundaries must remain narrow.

## 6. signals.md Schema

`signals.md` defines the directional and structural signal layer derived from canonical evidence.

### Responsibilities

`signals.md` may contain:
- forward indicators
- pipeline signals
- structural readiness indicators
- non-establishment language
- absence-oriented signal framing

### Canonical expectations

Signals must remain derived from canonical package evidence.

Signals may describe movement, direction, visibility, adjacency, pipeline conditions, or readiness-relevant tendencies.

Signals do not create establishment claims.

Signals do not independently establish evidence, classification, or deployment authorization.

When absence or insufficiency language is present canonically, the renderer may surface it through absence-callouts, but the canonical source remains `signals.md` and related package materials.

## 7. trust-dimensions.md Schema

`trust-dimensions.md` defines the stability-interpretation layer of the package.

### Responsibilities

`trust-dimensions.md` may contain:
- interpretation stability statements
- constraint basis
- support basis
- Atlas reading
- trust interpretation summaries
- dimension-specific interpretive blocks

Trust dimensions translate evidence and signals into bounded interpretive stability readings.

### Constraints

`trust-dimensions.md` shall not contain:
- numeric scoring
- ranked evaluation tables
- unsupported comparative rankings
- scorecard logic

Trust is interpretive but bounded.

It must remain grounded in upstream evidence and signals.

## 8. profile.md Schema

`profile.md` defines the jurisdiction synthesis layer.

### Responsibilities

`profile.md` may contain:
- jurisdiction synthesis
- capability posture
- corridor positioning
- interpretive summary
- synthesis statements derived from upstream layers

Profile is the characterization layer of the package.

It describes how the jurisdiction reads within Atlas after evidence, signals, and trust interpretation have been established.

### Constraint

`profile.md` does not introduce new signals.

It may restate or synthesize upstream signals, but it shall not create additional signal claims not already grounded canonically.

## 9. builder-mode.md Schema

`builder-mode.md` defines the builder-facing interpretation layer.

### Responsibilities

`builder-mode.md` may contain:
- deployment posture
- strategy surface
- builder-relevant constraints
- entry pathways
- builder-facing interpretation summaries

Builder Mode translates canonical package meaning into a bounded builder-facing reading.

### Constraint

`builder-mode.md` is interpretive but bounded by canonical evidence, signals, trust, and profile.

It shall not:
- exceed canonical evidence
- create new builder authorization claims
- invent deployment readiness
- override upstream package constraints

Entry pathways, where present, must remain interpretive and conditional rather than authoritative approval statements.

## 10. change-log.md Schema

`change-log.md` defines the canonical normalization record for the package.

### Responsibilities

`change-log.md` may contain:
- normalization explanations
- scope narrowing
- gap inheritance
- classification adjustments
- package revision reasoning
- canonical cleanup notes tied to package interpretation integrity

### Authority boundary

`change-log.md` does not introduce new evidence.

It may explain:
- why classification changed
- why scope was narrowed
- how gaps propagate through downstream layers
- how normalization decisions preserve package discipline

But it shall not serve as a substitute evidence file.

Any new evidence must be reflected in the appropriate canonical upstream file rather than created only through change-log narration.

## 11. Constraint Language Requirements

Canonical package files shall preserve constraint language as a first-class part of schema meaning.

Required constraint vocabulary classes include:
- non-establishment
- exclusions
- scope limitations
- evidentiary uncertainty
- pipeline status

These classes may appear in different files for different reasons, but they must remain preservable through schema usage and rendering.

Interpretive layers may restate constraint language.

They may not erase it.

Constraint language is part of canonical package meaning, not optional prose.

## 12. Corridor Classification Contract

The canonical corridor classification contract consists of:
- Corridor Group
- Foundation Layer
- Topology completion layer

This trio is the only canonical topology contract for jurisdiction packages in schema v1.

Classification families such as:
- Energy–Compute
- Research
- Interconnection

are annotation-only.

They are not canonical schema fields.

They may appear in documentation or corridor-level explanatory material, but not as package-schema replacements or competing metadata fields.

## 13. Jurisdiction Lens Contract

A jurisdiction lens appears only when explicitly present in `metadata.md`.

The renderer may surface a canonical lens.

The renderer may not infer a lens.

The absence of a lens field in `metadata.md` means no canonical lens is present for that package.

No placeholder or derived lens should be treated as canonical schema content.

## 14. Evidence Gaps Contract

Evidence gaps may appear in:
- `evidence.md`
- `change-log.md`

`evidence.md` may define explicit evidentiary gaps.

`change-log.md` may explain gap inheritance, narrowing logic, or how gap structure was normalized across downstream layers.

The renderer may aggregate gaps into a unified `Evidence Gaps` section.

The renderer may not invent gaps not grounded in canonical package materials.

Gap handling remains canonical only when it can be traced to explicit package content.

## 15. Schema Compliance Definition

A jurisdiction package is schema-compliant when all of the following are true:
- all required files exist
- the corridor trio is present in `metadata.md`
- required metadata governance fields are present
- constraint language is preserved
- no scoring is introduced
- no synthetic signals are added
- `change-log.md` remains grounded in canonical normalization rather than evidence invention
- `Jurisdiction lens`, if present, is explicit rather than inferred
- evidence-gap handling remains grounded in canonical files

A package is non-compliant when any of the following are true:
- a required file is missing
- the canonical trio is incomplete
- interpretive scoring replaces bounded interpretation
- synthetic signals appear without upstream grounding
- change-log content invents evidence rather than recording normalization
- a jurisdiction lens is treated as canonical without explicit presence in `metadata.md`

## Version

v1 — Initial Atlas jurisdiction package schema specification
