# Corridor Registry Schema
## Satoshium Atlas — Multi‑Jurisdiction Corridor Specification Standard

Defines the canonical structure for corridor registry files within the Atlas jurisdiction intelligence engine.

This schema ensures that all corridor documents:

- remain evidence-derived
- remain signal-referenced
- remain jurisdiction-lens aligned
- remain cross-state comparable
- remain machine-export compatible
- do not introduce rankings or deployment prescriptions

Corridor registry files describe **topological continuity across jurisdictions**, not optimization guidance.

---

## 📁 Registry Location

All corridor registry files live under:

/atlas/corridors/

Example:

/atlas/corridors/energy-compute/rocky-mountain-energy-compute-corridor.md

---

## 🎯 Purpose

Each corridor registry file records:

- participating jurisdictions
- corridor classification type
- supporting signal continuity
- infrastructure alignment structure
- exclusions affecting participation
- evidence dependency boundaries
- metadata synchronization expectations

Corridor registry files must never introduce new signals.

They only reference signals already present in jurisdiction packages.

---

## 🧱 Required Corridor File Structure

Each corridor registry file must follow the structure below.

---

### 1. Corridor Title Block

Format:

# <corridor-name>
## Corridor Classification: <type>

Example:

# Rocky Mountain Energy–Compute Corridor
## Corridor Classification: Energy–Compute Corridor

---

### 2. Participating Jurisdictions

List all participating jurisdictions alphabetically.

Example:

Participating jurisdictions:

- Colorado
- Idaho
- Montana
- Utah
- Wyoming

Participation must reflect signal continuity already present in those states.

---

### 3. Corridor Type Definition

Specify the structural corridor class:

Possible values:

- Energy–Compute Corridor
- Research Corridor
- Interconnection Corridor
- Digital Asset Governance Corridor
- Institutional Alignment Corridor

Hybrid corridors may list multiple types if supported by evidence.

---

### 4. Structural Continuity Description

Describe the topology linking jurisdictions.

Examples:

- transmission backbone adjacency
- hyperscale siting continuity
- IX density alignment
- semiconductor research clustering
- custody-regime statutory compatibility

Descriptions must remain observational and non-comparative.

---

### 5. Supporting Signal References

List signals already present in participating jurisdictions that justify corridor recognition.

Example:

Supporting signals:

- interconnection_density_present
- transmission_backbone_alignment
- hyperscale_siting_environment_present

Signals must already exist inside jurisdiction signals.md files.

Corridor files must not introduce new signal categories.

---

### 6. Evidence Dependency Boundary

Describe what evidence types support corridor continuity.

Examples:

- federal infrastructure siting records
- statutory authorization frameworks
- research institution alignment
- grid topology continuity
- fiber backbone routing adjacency

Evidence must already exist inside:

evidence.md

for participating jurisdictions.

---

### 7. Structural Exclusions

Document exclusions affecting corridor completeness.

Examples:

Structural exclusions:

- absence of hyperscale siting in Wyoming
- absence of IX density alignment in Montana
- absence of custody authorization continuity in Idaho

Exclusions preserve normalization transparency.

---

### 8. Emergence Classification

Specify corridor maturity level.

Allowed values:

- established_corridor
- emergent_corridor_candidate
- partial_continuity_corridor

Classification must reflect evidence continuity across jurisdictions.

---

### 9. Lens Alignment Confirmation

Confirm corridor compatibility with jurisdiction instruction lenses.

Example:

This corridor remains aligned with participating jurisdiction instruction lenses and does not expand jurisdiction scope beyond documented infrastructure topology and governance posture.

This section prevents inference drift.

---

### 10. Metadata Synchronization Notes

Document metadata updates triggered by corridor recognition.

Example:

Metadata synchronization:

- energy_compute_corridor_member
- interconnection_corridor_member

Metadata tags remain descriptive only.

---

### 11. Change‑Log Interaction

Specify required updates for participating jurisdictions.

Example:

Change‑log updates required in:

- Colorado change-log.md
- Utah change-log.md
- Wyoming change-log.md

Entries must record corridor participation as a structural topology observation.

---

## 🔗 Cross‑State Comparability Requirements

Corridor registry files must maintain:

- terminology consistency
- signal-reference consistency
- classification consistency
- maturity classification consistency

across all corridor registry entries.

---

## 📊 Machine‑Readable Export Compatibility

Each corridor registry file must support future export formats:

corridors.json

Registry entries should remain:

- deterministic
- parseable
- jurisdiction-linked
- signal-referenced

Corridor registry schema aligns with:

signals.json
metadata.json
trust-dimensions.json

---

## 🧭 Corridor Integrity Checklist

Before creating a corridor registry file confirm:

- three or more jurisdictions participate
- adjacency continuity exists
- supporting signals already exist
- evidence already present in jurisdiction evidence.md files
- exclusions documented
- maturity classification assigned
- metadata synchronization identified
- change-log updates specified

Only then may a corridor registry file be added to:

/atlas/corridors/
