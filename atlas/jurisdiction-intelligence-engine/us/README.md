# Atlas United States Jurisdiction Package

## Overview

The Atlas United States Jurisdiction Package is the national jurisdiction layer of the Satoshium Atlas Jurisdiction Intelligence Engine.

It organizes structured jurisdiction intelligence for all **50 U.S. states**, preserving human-readable canonical documentation together with complete machine-readable JSON representations and matched generation manifests.

The United States package supports:

- state-level jurisdiction intelligence
- evidence preservation
- signal identification
- trust-dimension analysis
- jurisdiction profiling
- metadata normalization
- builder-oriented interpretation
- dataset revision tracking
- corridor-aware organization
- regional and federal continuity
- future Registry, Navigator, Certifier, Chronicle, Attestor, and Suite interoperability

---

## Package Status

**Status:** Published · Complete

**Supported States:** 50

**Canonical State JSON Files:** 50

**Matched Generation Manifests:** 50

**Machine-Readable JSON Files:** 100

**Canonical Markdown Source Files:** 350

Each state package includes seven canonical Markdown source layers, one consolidated jurisdiction JSON record, and one matched generation manifest.

---

## Directory Structure

```text
us/
├── README.md
├── index.html
└── states/
    ├── california/
    │   ├── README.md
    │   ├── index.html
    │   ├── california.json
    │   ├── california.manifest.json
    │   ├── evidence.md
    │   ├── signals.md
    │   ├── trust-dimensions.md
    │   ├── profile.md
    │   ├── metadata.md
    │   ├── builder-mode.md
    │   └── change-log.md
    │
    ├── texas/
    │   ├── README.md
    │   ├── index.html
    │   ├── texas.json
    │   ├── texas.manifest.json
    │   ├── evidence.md
    │   ├── signals.md
    │   ├── trust-dimensions.md
    │   ├── profile.md
    │   ├── metadata.md
    │   ├── builder-mode.md
    │   └── change-log.md
    │
    └── ...
```

---

## Canonical Package Model

Every supported state follows the same package architecture:

```text
Canonical Markdown Source Layers
        │
        ▼
Consolidated State JSON
        │
        ▼
Matched Generation Manifest
```

The canonical Markdown files remain the authoritative human-readable source layers.

The primary JSON file consolidates the contents of those source layers into a structured machine-readable jurisdiction record.

The matched manifest records generation and validation metadata associated with the primary JSON file.

---

## Canonical Markdown Layers

Each state package contains the following seven canonical Markdown files.

### `evidence.md`

Preserves official sources, documented infrastructure anchors, institutional references, supporting observations, and evidence boundaries.

### `signals.md`

Translates documented evidence into normalized jurisdiction intelligence signals without assigning unsupported ranking, readiness, routing, or topology conclusions.

### `trust-dimensions.md`

Evaluates institutional continuity and structural trust characteristics while avoiding comparative trust rankings or certification conclusions.

### `profile.md`

Synthesizes the state's major infrastructure, coordination, institutional, regulatory, technological, and regional characteristics.

### `metadata.md`

Preserves structured jurisdiction identifiers, classifications, anchors, institutional categories, and normalization metadata.

### `builder-mode.md`

Describes visible participation surfaces, interaction environments, builder pathways, research access, infrastructure coordination, and implementation context.

### `change-log.md`

Records package initialization, layer construction, material updates, revisions, corrections, and dataset maintenance history.

---

## Machine-Readable Files

Each state package includes two machine-readable files.

### `<state-slug>.json`

The consolidated canonical jurisdiction record.

The primary JSON contains:

* jurisdiction identity
* schema version
* generation metadata
* builder-mode content
* profile content
* metadata content
* signals content
* trust-dimensions content
* evidence content
* change-log content
* source-document references

Example:

```text
states/california/california.json
```

### `<state-slug>.manifest.json`

The matched generation manifest.

The manifest records:

* jurisdiction slug
* generation date
* generation status
* source-file count
* validation result
* generated JSON size
* generation warnings

Example:

```text
states/california/california.manifest.json
```

---

## U.S. State Index

The complete public state index is available at:

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/us/states/
```

Each state name or map entry routes to its visual canonical jurisdiction page.

The visual page remains the primary public-facing presentation, while the Markdown, JSON, and manifest files remain available within the corresponding state folder.

---

## Supported States

The United States package includes all 50 states:

1. Alabama
2. Alaska
3. Arizona
4. Arkansas
5. California
6. Colorado
7. Connecticut
8. Delaware
9. Florida
10. Georgia
11. Hawaii
12. Idaho
13. Illinois
14. Indiana
15. Iowa
16. Kansas
17. Kentucky
18. Louisiana
19. Maine
20. Maryland
21. Massachusetts
22. Michigan
23. Minnesota
24. Mississippi
25. Missouri
26. Montana
27. Nebraska
28. Nevada
29. New Hampshire
30. New Jersey
31. New Mexico
32. New York
33. North Carolina
34. North Dakota
35. Ohio
36. Oklahoma
37. Oregon
38. Pennsylvania
39. Rhode Island
40. South Carolina
41. South Dakota
42. Tennessee
43. Texas
44. Utah
45. Vermont
46. Virginia
47. Washington
48. West Virginia
49. Wisconsin
50. Wyoming

---

## Corridor and Foundation Classification

The table below preserves the original Atlas corridor, foundation-layer, and topology-completion classifications for the United States jurisdiction set.

| State          | Corridor Group                                    | Foundation Layer                                        | Topology Completion Layer            |
| -------------- | ------------------------------------------------- | ------------------------------------------------------- | ------------------------------------ |
| California     | Pacific Coastal Hyperscale Corridor               | Coastal Hyperscale & Global Infrastructure              | Pacific Edge Anchor Layer            |
| Texas          | National Energy & Logistics Spine Corridor        | National Logistics Spine & Energy Coordination Layer    | Southern Interior Completion Layer   |
| New York       | Atlantic Financial & Global Gateway Corridor      | Coastal Hyperscale & Global Infrastructure              | Northeast Anchor Completion Layer    |
| Virginia       | Federal Interface Governance Corridor             | Federal Interface Governance Layer                      | Mid-Atlantic Completion Layer        |
| Florida        | Southeast Coastal Access & Maritime Corridor      | Coastal Hyperscale & Global Infrastructure              | Southeast Coastal Completion Layer   |
| Wyoming        | Interior Western Statutory Flex Corridor          | Statutory Wrapper / Experimental Governance Layer       | Western Interior Completion Layer    |
| Arizona        | Southwest Transition Infrastructure Corridor      | Southwest Transition Infrastructure Layer               | Desert–Interior Transition Layer     |
| Colorado       | Mountain West Research Corridor                   | Mountain West Research & Federal Lab Transition Layer   | Western Interior Completion Layer    |
| New Mexico     | Southwest Transition Infrastructure Corridor      | Southwest Transition Infrastructure Layer               | Desert–Interior Transition Layer     |
| Nevada         | Basin & Range Interior Transition Corridor        | Mountain Corridor Structural Continuity Layer           | Desert–Interior Transition Layer     |
| Utah           | Mountain Interior Continuity Corridor             | Mountain Corridor Structural Continuity Layer           | Western Interior Completion Layer    |
| Oklahoma       | Central Interior Logistics Spine Corridor         | Interior Corridor Logistics Spine                       | Central Plains Completion Layer      |
| Kansas         | Central Interior Logistics Spine Corridor         | Interior Corridor Logistics Spine                       | Central Plains Completion Layer      |
| Louisiana      | Gulf Port & Energy Export Corridor                | Gulf Corridor Layer                                     | Gulf Coast Completion Layer          |
| Arkansas       | Mississippi Valley Transit & Distribution Corridor | Gulf Corridor Layer                                    | Central Interior Completion Layer    |
| Missouri       | Central Interior Structural Continuity Corridor   | Central Interior Continuity Layer                       | Central Plains Completion Layer      |
| Tennessee      | Southeast Interior Structural Corridor            | Southeast Interior Completion Layer                     | Central Interior Completion Layer    |
| Kentucky       | Ohio Valley Transition Corridor                   | Southeast Interior Completion Layer                     | Central Interior Completion Layer    |
| Illinois       | Great Lakes Industrial Core Corridor              | Great Lakes Industrial Core Layer                       | Great Lakes Completion Layer         |
| Michigan       | Great Lakes Industrial Core Corridor              | Great Lakes Industrial Core Layer                       | Great Lakes Completion Layer         |
| Indiana        | Great Lakes Industrial Core Corridor              | Great Lakes Industrial Core Layer                       | Great Lakes Completion Layer         |
| Ohio           | Great Lakes Industrial Core Corridor              | Great Lakes Industrial Core Layer                       | Great Lakes Completion Layer         |
| Pennsylvania   | Northeast Institutional Mesh Corridor             | Northeast Institutional Mesh Layer                      | Mid-Atlantic Completion Layer        |
| Wisconsin      | Great Lakes Industrial Core Corridor              | Great Lakes Industrial Core Layer                       | Great Lakes Completion Layer         |
| Minnesota      | Upper Midwest Continuity Corridor                 | Great Lakes Industrial Core Layer                       | Northern Interior Completion Layer   |
| Connecticut    | Northeast Institutional Mesh Corridor             | Northeast Institutional Mesh Layer                      | Northeast Completion Layer           |
| Delaware       | Mid-Atlantic Institutional Bridge Corridor        | Northeast Institutional Mesh Layer                      | Mid-Atlantic Completion Layer        |
| Massachusetts  | Northeast Research Mesh Corridor                  | Northeast Institutional Mesh Layer                      | Northeast Completion Layer           |
| New Jersey     | Northeast Institutional Mesh Corridor             | Northeast Institutional Mesh Layer                      | Mid-Atlantic Completion Layer        |
| Maryland       | Chesapeake Federal Interface Corridor             | Federal Interface Governance Layer                      | Mid-Atlantic Completion Layer        |
| Rhode Island   | Northeast Institutional Support Corridor          | Northeast Completion Layer                              | Northeast Completion Layer           |
| Vermont        | Northeast Institutional Support Corridor          | Northeast Completion Layer                              | Northeast Completion Layer           |
| New Hampshire  | Northeast Institutional Support Corridor          | Northeast Completion Layer                              | Northeast Completion Layer           |
| Maine          | Northeast Terminal Edge Corridor                  | Northeast Completion Layer                              | Northeast Terminal Completion Layer  |
| Alabama        | Southeast Interior Support Corridor               | Southeast Interior Completion Layer                     | Southeast Interior Completion Layer  |
| Georgia        | Atlantic Industrial Growth Corridor               | Southeast Interior Completion Layer                     | Southeast Interior Completion Layer  |
| Mississippi    | Lower Mississippi River Corridor                  | Southeast Interior Completion Layer                     | Gulf Interior Completion Layer       |
| North Carolina | Southeast Research & Defense Corridor             | Southeast Research Corridor Layer                       | Southeast Interior Completion Layer  |
| South Carolina | Atlantic Industrial & Port Support Corridor       | Southeast Interior Completion Layer                     | Southeast Coastal Completion Layer   |
| Montana        | Northern Plains Sparse-Node Corridor              | Northern Plains Sparse-Node Layer                       | Northern Interior Completion Layer   |
| North Dakota   | Northern Plains Sparse-Node Corridor              | Northern Plains Sparse-Node Layer                       | Northern Interior Completion Layer   |
| South Dakota   | Northern Plains Sparse-Node Corridor              | Northern Plains Sparse-Node Layer                       | Northern Interior Completion Layer   |
| Nebraska       | Central Interior Structural Continuity Corridor   | Central Interior Continuity Layer                       | Central Plains Completion Layer      |
| Iowa           | Central Interior Agricultural Continuity Corridor | Central Interior Continuity Layer                       | Central Plains Completion Layer      |
| Oregon         | Pacific Northwest Coordination Corridor           | Pacific Northwest Coordination Layer                    | Pacific Northwest Completion Layer   |
| Washington     | Pacific Northwest Coordination Corridor           | Pacific Northwest Coordination Layer                    | Pacific Northwest Completion Layer   |
| Idaho          | Northern Mountain Transition Corridor             | Mountain Transition Layer                               | Northern Interior Completion Layer   |
| Alaska         | Arctic Strategic Access Corridor                  | Non-Contiguous Strategic Layer                          | Non-Contiguous Completion Layer      |
| Hawaii         | Pacific Strategic Projection Corridor             | Non-Contiguous Strategic Layer                          | Non-Contiguous Completion Layer      |
| West Virginia  | Appalachian Energy Transition Corridor            | Mid-Atlantic Governance Layer                           | Appalachian Completion Layer         |

---

## Classification Boundary

Corridor groups, foundation layers, and topology-completion descriptions are Atlas organizational and interpretive structures.

They do not independently constitute:

* certification outcomes
* trust rankings
* readiness scores
* legal classifications
* state capability rankings
* routing assignments
* institutional endorsements
* federal classifications

Canonical state packages preserve evidence and analysis boundaries within their own source layers.

---

## Relationship to the Satoshium Suite

The United States package serves as an intelligence source for the broader Satoshium Suite.

```text
Atlas
Organizes jurisdiction intelligence

Navigator
Explores and compares Atlas intelligence

Certifier
Evaluates defined Atlas certification subjects

Registry
Catalogs authoritative Atlas and Certifier records

Chronicle
Preserves relevant historical continuity

Anchor
Preserves integrity and reference relationships

Beacon
Supports discovery

Attestor
Preserves accountable trust context
```

Atlas retains ownership of its state-level jurisdiction intelligence records.

Other Suite institutions reference Atlas records without transferring or duplicating ownership.

---

## Future Integration

The completed United States machine-readable dataset provides a stable foundation for:

* Satoshium Registry entries
* Navigator queries and comparisons
* future Certifier workflows
* regional and corridor analysis
* structured state discovery
* historical change analysis
* trust-context references
* dataset exports
* versioned releases
* future APIs
* automated validation
* state comparison tools
* Suite interoperability

---

## Canonical Principles

The United States package follows these enduring Atlas principles:

* Evidence before conclusions
* Structure before comparison
* Context before interpretation
* Transparency before assertion
* Human-readable sources remain authoritative
* Machine-readable representations must preserve source meaning
* Unsupported classifications must remain excluded
* Institutional ownership must remain clear
* State packages must remain independently reviewable
* Interoperability must not transfer authority

---

## Maintenance

State package updates should preserve alignment across:

```text
Canonical Markdown Sources
Primary Jurisdiction JSON
Matched Generation Manifest
Visual Jurisdiction Page
Package README
```

When a canonical Markdown source changes, the corresponding JSON and manifest should be regenerated and validated.

Material changes should be documented in the jurisdiction's `change-log.md`.

---

## Public Resources

### Atlas United States Entry

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/us/
```

### U.S. State Index

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/us/states/
```

### Satoshium Atlas

```text
https://satoshium.us/atlas/
```

---

## Status

**Atlas United States Jurisdiction Package**

**Status:** Published · Complete

**States:** 50

**Canonical JSON Records:** 50

**Matched Generation Manifests:** 50

**Version:** 1.0

**Machine-Readable Foundation:** Complete

---

**Know the Jurisdictions. Navigate the Future.**
