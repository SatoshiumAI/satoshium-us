# Corridor Membership Tags
## Satoshium Atlas — Corridor Metadata Tag Vocabulary

Defines the canonical metadata tag system used to represent jurisdiction participation in Atlas corridor topology.

These tags are **structural classification metadata**, not rankings or deployment guidance.

They support:

- cross-state comparability
- corridor registry consistency
- metadata.md synchronization
- machine-readable export layers
- corridor-aware Atlas navigation surfaces

---

## 🎯 Purpose

Corridor membership tags provide a deterministic vocabulary describing jurisdiction participation in:

- Corridor Groups
- Foundation Layers
- Topology Completion Layers

These tags appear inside:

metadata.md
metadata.json (future)
corridors.json (future)
atlas-index.json (future)

Tags must remain:

- evidence-consistent
- lens-aligned
- structurally descriptive
- non-hierarchical

---

## 🧱 Corridor Group Tags

Each jurisdiction receives **one primary corridor-group membership tag**.

Format:

<snake_case_corridor_name>_member

Examples:

pacific_coastal_hyperscale_corridor_member
national_energy_logistics_spine_corridor_member
federal_interface_governance_corridor_member
great_lakes_industrial_core_corridor_member
central_interior_logistics_spine_corridor_member
northeast_institutional_mesh_corridor_member
pacific_northwest_coordination_corridor_member
southwest_transition_infrastructure_corridor_member
northern_plains_sparse_node_corridor_member
non_contiguous_strategic_corridor_member

---

## 🏗 Foundation Layer Tags

Each jurisdiction receives one **foundation-layer structural alignment tag**.

Format:

<foundation_layer_name>_foundation_layer

Examples:

coastal_hyperscale_global_infrastructure_foundation_layer
federal_interface_governance_foundation_layer
statutory_wrapper_experimental_governance_foundation_layer
mountain_west_research_foundation_layer
gulf_corridor_foundation_layer
central_interior_continuity_foundation_layer
great_lakes_industrial_core_foundation_layer
northeast_institutional_mesh_foundation_layer
pacific_northwest_coordination_foundation_layer
non_contiguous_strategic_foundation_layer

Foundation-layer tags describe base topology continuity surfaces.

They do not indicate readiness or advantage.

---

## 🌐 Topology Completion Layer Tags

Each jurisdiction receives one **topology completion-layer tag** describing adjacency integration.

Format:

<completion_layer_name>_completion_layer

Examples:

pacific_edge_anchor_completion_layer
southern_interior_completion_layer
northeast_anchor_completion_layer
mid_atlantic_completion_layer
desert_interior_transition_completion_layer
central_plains_completion_layer
great_lakes_completion_layer
northern_interior_completion_layer
southeast_coastal_completion_layer
appalachian_completion_layer
non_contiguous_completion_layer

Completion-layer tags describe how jurisdictions connect into regional topology structures.

They remain descriptive only.

---

## 🔗 Tag Placement Rules

Tags appear inside:

metadata.md

Example:

Corridor membership:

- pacific_coastal_hyperscale_corridor_member

Foundation layer:

- coastal_hyperscale_global_infrastructure_foundation_layer

Completion layer:

- pacific_edge_anchor_completion_layer

Tags must remain synchronized with:

/atlas/corridors/corridor-assignment-matrix.md

---

## 🧭 Multi-Corridor Participation (Rare Cases)

Most jurisdictions receive:

one corridor group tag  
one foundation layer tag  
one completion layer tag  

If structural continuity supports multiple memberships:

secondary corridor participation may be recorded as:

secondary_<corridor_name>_member

Example:

secondary_interconnection_corridor_member

Secondary tags must remain evidence-supported.

---

## 🧾 Change-Log Interaction

When corridor membership changes:

change-log.md must record:

- corridor-group adjustment
- foundation-layer adjustment
- completion-layer adjustment
- matrix alignment confirmation

These adjustments remain structural observations only.

---

## 🤖 Machine-Readable Export Compatibility

Tags must remain compatible with future export surfaces:

metadata.json
corridors.json
atlas-index.json

Tag strings must remain:

- lowercase
- snake_case
- deterministic
- parseable

---

## ✅ Corridor Membership Tag Integrity Checklist

Before assigning or modifying tags confirm:

- alignment with corridor-assignment-matrix.md
- signal consistency preserved
- exclusions respected
- metadata.md updated
- change-log.md updated

Only then may corridor membership tags be applied.
