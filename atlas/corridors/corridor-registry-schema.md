# Corridor Registry Schema
## Satoshium Atlas — Multi-Jurisdiction Corridor Specification Standard

Defines the canonical structure for corridor registry files within the Atlas jurisdiction intelligence engine.

This version integrates Corridor Assignment Matrix alignment fields.

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
- corridor group classification
- foundation layer alignment
- topology completion layer alignment
- supporting signal continuity
- exclusions affecting participation
- evidence dependency boundaries
- metadata synchronization expectations

Corridor registry files must never introduce new signals.

---

## 🧱 Required Corridor File Structure

Each corridor registry file must include:

### 1. Corridor Title Block

# <corridor-name>
## Corridor Classification: <type>

---

### 2. Corridor Group

Primary structural corridor assignment as defined in:

/atlas/corridors/corridor-assignment-matrix.md

---

### 3. Foundation Layer

Specifies infrastructure or governance base layer supporting continuity.

Example:

Foundation Layer: Coastal Hyperscale & Global Infrastructure Layer

---

### 4. Topology Completion Layer

Specifies adjacency completion surface.

Example:

Topology Completion Layer: Pacific Edge Anchor Layer

---

### 5. Participating Jurisdictions

Alphabetical listing required.

---

### 6. Supporting Signal References

Signals must already exist inside jurisdiction signals.md files.

---

### 7. Evidence Dependency Boundary

Evidence must already exist inside jurisdiction evidence.md files.

---

### 8. Structural Exclusions

Document corridor continuity gaps.

---

### 9. Emergence Classification

Allowed values:

- established_corridor
- emergent_corridor_candidate
- partial_continuity_corridor

---

### 10. Metadata Synchronization Notes

Describe corridor membership metadata propagation.

---

### 11. Change-Log Interaction

Specify required jurisdiction change-log updates.

---

## 🔗 Cross-State Comparability Requirements

Corridor registry files must maintain:

- classification consistency
- signal-reference consistency
- matrix alignment consistency

across all corridor registry entries.

---

## 🤖 Machine-Readable Export Compatibility

Supports:

corridors.json
signals.json
metadata.json
trust-dimensions.json
