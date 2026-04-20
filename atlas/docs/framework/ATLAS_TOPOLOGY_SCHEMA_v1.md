# ATLAS Topology Schema v1

## 1. Purpose

This document defines the topology schema used by Atlas corridor classification.

The topology schema defines how jurisdictions attach to Atlas corridors.

Corridor classification is structural.

It is not interpretive scoring.

It is not deployment ranking.

It is not a maturity score.

Topology classification must remain stable across renderer surfaces.

The topology schema is independent from lifecycle maturity.

Lifecycle status affects the authority level of topology classification, but it does not change the underlying topology field model.

## 2. Corridor Classification Model Overview

The canonical topology attachment contract consists of the trio:
- Corridor Group
- Foundation Layer
- Topology completion layer

This trio forms the complete topology attachment contract for schema v1.

No additional metadata fields participate in corridor placement authority.

Other descriptive language may appear in canonical packages or corridor documentation, but the topology trio alone carries canonical topology attachment meaning.

## 3. Corridor Group Definition

`Corridor Group` identifies the primary infrastructure or system domain in which a jurisdiction participates.

Corridor Group answers the question:

What primary corridor structure is this jurisdiction attached to?

Examples of participation domains may include:
- compute infrastructure
- energy infrastructure
- research infrastructure
- industrial infrastructure
- interconnection infrastructure

Corridor Group describes structural participation domain.

It does not indicate:
- capability ranking
- deployment completeness
- lifecycle maturity
- national importance hierarchy

A Corridor Group is a topology classification, not a quality judgment.

## 4. Foundation Layer Definition

`Foundation Layer` describes the structural layer at which corridor participation occurs.

Foundation Layer answers the question:

At what underlying structural layer does this jurisdiction participate in the corridor?

Examples of foundation semantics may include:
- production
- research
- grid
- transport
- policy-anchor
- interconnection

Foundation Layer distinguishes participation mode.

Multiple jurisdictions may share a Corridor Group while differing in Foundation Layer.

Foundation Layer does not imply readiness maturity, deployment maturity, or corridor strength.

It describes the substrate of participation, not the success of participation.

## 5. Topology Completion Layer Definition

`Topology completion layer` describes how a jurisdiction contributes to corridor continuity.

Topology completion answers the question:

What continuity role does this jurisdiction play inside the corridor structure?

Examples of completion-layer semantics may include:
- anchor
- connector
- bridge
- terminus
- expansion-edge
- support-node

Completion-layer semantics describe network role.

They do not describe:
- capability strength
- deployment scale
- policy authority
- lifecycle maturity

Completion-layer meaning is topological rather than evaluative.

## 6. Corridor Trio Authority Contract

The trio:
- Corridor Group
- Foundation Layer
- Topology completion layer

forms the only canonical topology attachment schema for Atlas jurisdiction packages.

Classification families must not override this trio.

The renderer must surface the trio consistently.

Packages must not infer additional topology fields and treat them as equivalent to the trio.

Topology authority rests in the trio together with the required provenance and boundary fields recorded in `metadata.md`.

## 7. Classification Source Requirement

Topology classification source must be recorded in `metadata.md`.

Classification source may include evidence such as:
- statutory infrastructure presence
- federal designation
- grid attachment
- research infrastructure role
- transport attachment
- corridor adjacency continuity

Classification must remain evidence-grounded.

Signals alone cannot establish corridor classification.

Signals may support interpretation, refinement, or anticipated change, but they may not independently create canonical topology placement.

## 8. Interpretation Boundary Requirement

Every topology classification must be bounded by an interpretation boundary.

Interpretation boundary constrains corridor classification authority.

Boundary language must specify relevant limits such as:
- establishment limits
- deployment limits
- scope exclusions
- adjacency dependence
- federal reliance where applicable

The interpretation boundary defines what the topology classification does not authorize.

Renderer surfaces must preserve interpretation boundary visibility.

Topology classification without visible boundary language is incomplete governance.

## 9. Adjacency Interpretation Rules

Adjacency allows corridor participation through neighboring-jurisdiction infrastructure continuity.

Adjacency is a valid basis for corridor participation only when it is explicitly documented.

Adjacency must not imply:
- anchor status
- independent corridor control
- corridor origin authority
- topology equivalence to a direct infrastructure anchor

Adjacency must not override completion-layer semantics.

If a jurisdiction participates through adjacency, the topology role must still be expressed through the canonical trio and bounded by the interpretation boundary.

Adjacency is a structural relation, not a shortcut to stronger corridor authority.

## 10. Cross-Foundation Placement Rules

A jurisdiction may participate in multiple Corridor Groups.

A jurisdiction may participate in multiple Foundation Layers.

However, the primary topology classification must identify the dominant placement.

That dominant placement is the canonical trio carried in `metadata.md`.

Secondary placements may be documented explicitly in canonical materials, but they remain non-primary unless a future schema adds governed support for multiple canonical topology assignments.

Secondary placements should remain documented through:
- evidence
- signals
- profile
- change-log explanation
- approved future extension files, if adopted later

The renderer must not merge cross-foundation placements implicitly.

Implicit synthesis of multiple placements into a new unstated topology role is not permitted.

## 11. Completion Layer Semantics

Allowed completion-layer meanings include:

- `anchor` -> origin or primary corridor stabilization node
- `connector` -> continuity-preserving attachment node
- `bridge` -> cross-corridor linkage node
- `terminus` -> corridor endpoint node
- `expansion-edge` -> emerging corridor frontier node
- `support-node` -> indirect infrastructure support participant

These are topology-role semantics.

They are not lifecycle labels.

They are not readiness labels.

They are not intensity labels.

Completion layer must remain lifecycle-independent.

A package may move from Draft to Canonical without changing completion-layer meaning if the underlying corridor role remains the same.

## 12. Classification Families (Annotation Layer Only)

Classification families may include labels such as:
- Energy–Compute
- Research
- Interconnection
- Industrial
- Transport

These families are annotation layers.

They assist interpretation and documentation.

They do not replace topology trio fields.

They must not appear as canonical metadata schema fields unless a future schema explicitly adopts them.

Classification families may organize corridor discourse.

They may not compete with or override the canonical topology attachment contract.

## 13. Lifecycle Interaction with Topology Classification

Lifecycle status affects topology authority as follows:
- Draft -> provisional topology classification
- Evidence-Attached -> provisional topology classification
- Corridor-Attached -> stable topology classification
- Complete -> stable topology classification
- Canonical -> authoritative topology classification baseline
- Superseded -> historically informative topology classification
- Deprecated -> inactive topology classification

Lifecycle does not redefine topology fields.

It changes how strongly the trio may be relied upon.

Renderer surfaces must respect lifecycle classification authority limits.

A provisional topology classification may be rendered as provisional.

Only Canonical packages may be treated as authoritative topology baselines across Atlas.

## 14. Renderer Topology Responsibilities

The renderer must:
- surface the topology trio consistently
- preserve interpretation boundary visibility
- preserve classification source visibility
- avoid synthesizing new topology roles
- avoid promoting adjacency to anchor status
- avoid merging cross-foundation placements implicitly
- avoid turning annotation families into schema-equivalent metadata

The renderer may normalize display labels for presentation, but it must not change canonical topology meaning.

## 15. Topology Compliance Definition

A jurisdiction package is topology-compliant when all of the following are true:
- Corridor Group is present
- Foundation Layer is present
- Topology completion layer is present
- classification source is recorded
- interpretation boundary is recorded
- adjacency is clearly defined where applicable
- classification families are used only as annotation layers

Non-compliance occurs when any of the following are true:
- the topology trio is incomplete
- classification is inferred without evidence support
- adjacency is treated as anchor equivalence
- classification families are used as schema fields
- completion-layer semantics are undefined

## Version

v1 — Initial Atlas topology schema specification
