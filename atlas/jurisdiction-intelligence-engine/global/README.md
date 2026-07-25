# Atlas Global Jurisdiction Package

## Overview

The Atlas Global Jurisdiction Package is the international jurisdiction layer of the Satoshium Atlas Jurisdiction Intelligence Engine.

It organizes structured jurisdiction intelligence for **52 supported countries**, preserving human-readable canonical documentation together with complete machine-readable JSON representations and matched generation manifests.

The Global package supports:

- country-level jurisdiction intelligence
- evidence preservation
- signal identification
- trust-dimension analysis
- jurisdiction profiling
- metadata normalization
- builder-oriented interpretation
- dataset revision tracking
- corridor-aware organization
- future Registry, Navigator, Certifier, Chronicle, Attestor, and Suite interoperability

---

## Package Status

**Status:** Published · Complete

**Supported Countries:** 52

**Canonical Country JSON Files:** 52

**Matched Generation Manifests:** 52

**Machine-Readable JSON Files:** 104

**Canonical Markdown Source Files:** 364

Each country package includes seven canonical Markdown source layers, one consolidated jurisdiction JSON record, and one matched generation manifest.

---

## Directory Structure

```text
global/
├── README.md
├── index.html
└── countries/
    ├── argentina/
    │   ├── README.md
    │   ├── index.html
    │   ├── argentina.json
    │   ├── argentina.manifest.json
    │   ├── evidence.md
    │   ├── signals.md
    │   ├── trust-dimensions.md
    │   ├── profile.md
    │   ├── metadata.md
    │   ├── builder-mode.md
    │   └── change-log.md
    │
    ├── japan/
    │   ├── README.md
    │   ├── index.html
    │   ├── japan.json
    │   ├── japan.manifest.json
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

Every supported country follows the same package architecture:

```text
Canonical Markdown Source Layers
        │
        ▼
Consolidated Country JSON
        │
        ▼
Matched Generation Manifest
```

The canonical Markdown files remain the authoritative human-readable source layers.

The primary JSON file consolidates the contents of those source layers into a structured machine-readable jurisdiction record.

The matched manifest records generation and validation metadata associated with the primary JSON file.

---

## Canonical Markdown Layers

Each country package contains the following seven canonical Markdown files.

### `evidence.md`

Preserves official sources, documented infrastructure anchors, institutional references, supporting observations, and evidence boundaries.

### `signals.md`

Translates documented evidence into normalized jurisdiction intelligence signals without assigning unsupported ranking, readiness, routing, or topology conclusions.

### `trust-dimensions.md`

Evaluates institutional continuity and structural trust characteristics while avoiding comparative trust rankings or certification conclusions.

### `profile.md`

Synthesizes the jurisdiction's major infrastructure, coordination, institutional, regulatory, technological, and cross-border characteristics.

### `metadata.md`

Preserves structured jurisdiction identifiers, classifications, anchors, institutional categories, and normalization metadata.

### `builder-mode.md`

Describes visible participation surfaces, interaction environments, builder pathways, research access, infrastructure coordination, and implementation context.

### `change-log.md`

Records package initialization, layer construction, material updates, revisions, corrections, and dataset maintenance history.

---

## Machine-Readable Files

Each country package includes two machine-readable files.

### `<country-slug>.json`

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
countries/japan/japan.json
```

### `<country-slug>.manifest.json`

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
countries/japan/japan.manifest.json
```

---

## Global Country Index

The complete public country index is available at:

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/global/countries/
```

Each country name routes to its visual canonical jurisdiction page.

The visual page remains the primary public-facing presentation, while the Markdown, JSON, and manifest files remain available within the corresponding country folder.

---

## Supported Countries

The current Global package includes the following 52 jurisdictions:

1. Argentina
2. Armenia
3. Australia
4. Austria
5. Brazil
6. Canada
7. Chile
8. China
9. Costa Rica
10. Czech Republic
11. Denmark
12. El Salvador
13. Estonia
14. Finland
15. France
16. Georgia
17. Germany
18. Hong Kong
19. Iceland
20. India
21. Indonesia
22. Ireland
23. Israel
24. Italy
25. Japan
26. Kazakhstan
27. Kenya
28. Malaysia
29. Netherlands
30. New Zealand
31. Nigeria
32. Norway
33. Panama
34. Philippines
35. Poland
36. Portugal
37. Qatar
38. Russia
39. Rwanda
40. Saudi Arabia
41. Singapore
42. South Africa
43. South Korea
44. Spain
45. Sweden
46. Switzerland
47. Taiwan
48. Thailand
49. Turkey
50. United Arab Emirates
51. United Kingdom
52. Vietnam

---

## Corridor and Foundation Classification

The table below preserves the original Atlas corridor, tier, foundation-layer, and topology-completion classifications for the Global jurisdiction set.

| Country              | Tier | Corridor Group                                          | Foundation Layer | Topology Completion Layer          |
| -------------------- | ---- | ------------------------------------------------------- | ---------------- | ---------------------------------- |
| United Kingdom       | 1    | Northeast Financial Compute Corridor (Global Extension) | Financial        | Custody bridge                     |
| Germany              | 1    | European Regulatory Compute Corridor                    | Regulatory       | EU policy anchor                   |
| France               | 1    | European Regulatory Compute Corridor                    | Regulatory       | Sovereign AI precedent node        |
| Japan                | 1    | Indo-Pacific Advanced Compute Corridor                  | Compute          | Hardware supply stabilizer         |
| South Korea          | 1    | Indo-Pacific Semiconductor Corridor                     | Research         | Semiconductor node                 |
| Canada               | 1    | North American Energy-Compute Extension                 | Energy           | Mining stabilizer                  |
| Singapore            | 1    | Southeast Asia Financial Routing Corridor               | Financial        | Global custody bridge              |
| Switzerland          | 1    | Alpine Crypto-Legal Corridor                            | Regulatory       | Digital asset precedent anchor     |
| United Arab Emirates | 2    | Gulf Energy-Compute Corridor                            | Financial        | Capital routing hub                |
| Israel               | 2    | Eastern Mediterranean Innovation Corridor               | Research         | Security-tech anchor               |
| Netherlands          | 2    | European Connectivity Exchange Corridor                 | Connectivity     | Internet exchange anchor           |
| Sweden               | 2    | Nordic Renewable Compute Corridor                       | Energy           | Renewable compute stabilizer       |
| Norway               | 2    | Nordic Renewable Compute Corridor                       | Energy           | Hydropower mining anchor           |
| Finland              | 2    | Nordic Secure Infrastructure Corridor                   | Research         | Secure compute anchor              |
| Denmark              | 2    | Baltic-Nordic Connectivity Corridor                     | Connectivity     | Offshore infrastructure bridge     |
| Estonia              | 2    | Baltic Digital Governance Corridor                      | Regulatory       | e-government precedent node        |
| Saudi Arabia         | 3    | Gulf Energy-Compute Corridor                            | Energy           | Sovereign compute expansion anchor |
| Qatar                | 3    | Gulf Energy-Compute Corridor                            | Energy           | LNG compute stabilizer             |
| Kazakhstan           | 3    | Eurasian Mining Corridor                                | Energy           | Hashrate stabilization node        |
| Iceland              | 3    | Nordic Renewable Compute Corridor                       | Energy           | Zero-carbon compute anchor         |
| Australia            | 3    | Indo-Pacific Energy Corridor                            | Energy           | Southern hemisphere compute anchor |
| Chile                | 3    | Andean Renewable Corridor                               | Energy           | Solar compute stabilizer           |
| Brazil               | 3    | LATAM Infrastructure Corridor                           | Connectivity     | Regional anchor economy            |
| Argentina            | 3    | Southern Cone Energy Corridor                           | Energy           | Monetary experimentation node      |
| India                | 4    | South Asia Developer Growth Corridor                    | Developer        | Population-scale multiplier        |
| Indonesia            | 4    | Maritime Southeast Asia Corridor                        | Connectivity     | Archipelago routing anchor         |
| Vietnam              | 4    | ASEAN Manufacturing-Tech Corridor                       | Developer        | Supply chain compute expansion     |
| Philippines          | 4    | Pacific Remittance Corridor                             | Financial        | Lightning adoption bridge          |
| Thailand             | 4    | ASEAN Trade Infrastructure Corridor                     | Connectivity     | Regional logistics stabilizer      |
| Malaysia             | 4    | Strait of Malacca Infrastructure Corridor               | Connectivity     | Trade-routing node                 |
| Ireland              | 5    | Transatlantic Cloud Corridor                            | Compute          | Hyperscale hosting anchor          |
| Portugal             | 5    | Iberian Atlantic Connectivity Corridor                  | Connectivity     | Subsea cable landing hub           |
| Spain                | 5    | Iberian Renewable Corridor                              | Energy           | EU southern corridor stabilizer    |
| Italy                | 5    | Mediterranean Regulatory Corridor                       | Regulatory       | Southern EU governance bridge      |
| Austria              | 5    | Central European Transit Corridor                       | Connectivity     | Alpine routing stabilizer          |
| Czech Republic       | 5    | Central European Industrial Corridor                    | Research         | Manufacturing compute support      |
| Poland               | 5    | Eastern NATO Infrastructure Corridor                    | Connectivity     | Eastern EU security anchor         |
| Turkey               | 6    | Anatolian Interconnection Corridor                      | Connectivity     | Europe-Asia routing bridge         |
| Georgia              | 6    | Caucasus Transit Corridor                               | Connectivity     | Silk-road digital bridge           |
| Armenia              | 6    | Caucasus Innovation Corridor                            | Research         | Regional tech incubator            |
| El Salvador          | 6    | Bitcoin Legal Adoption Corridor                         | Financial        | Sovereign BTC precedent node       |
| Panama               | 6    | Canal Trade Routing Corridor                            | Connectivity     | Maritime logistics anchor          |
| Costa Rica           | 6    | Central America Stability Corridor                      | Research         | Democratic innovation node         |
| South Africa         | 7    | Southern Africa Infrastructure Corridor                 | Connectivity     | Continental anchor economy         |
| Kenya                | 7    | East Africa Mobile Finance Corridor                     | Financial        | Mobile payments precedent node     |
| Nigeria              | 7    | West Africa Population Corridor                         | Developer        | Adoption-scale multiplier          |
| Rwanda               | 7    | East Africa Digital Governance Corridor                 | Regulatory       | Policy experimentation node        |
| Taiwan               | 8    | Global Semiconductor Corridor                           | Research         | Advanced chip fabrication anchor   |
| Hong Kong            | 8    | Asia Financial Routing Corridor                         | Financial        | Capital gateway bridge             |
| New Zealand          | 8    | Pacific Stability Corridor                              | Regulatory       | Democratic southern anchor         |

---

## Classification Boundary

Corridor groups, tiers, foundation layers, and topology-completion descriptions are Atlas organizational and interpretive structures.

They do not independently constitute:

* certification outcomes
* trust rankings
* readiness scores
* legal classifications
* sovereign capability rankings
* routing assignments
* institutional endorsements

Canonical country packages preserve evidence and analysis boundaries within their own source layers.

---

## Relationship to the Satoshium Suite

The Global package serves as an intelligence source for the broader Satoshium Suite.

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

Atlas retains ownership of its jurisdiction intelligence records.

Other Suite institutions reference Atlas records without transferring or duplicating ownership.

---

## Future Integration

The completed Global machine-readable dataset provides a stable foundation for:

* Satoshium Registry entries
* Navigator queries and comparisons
* future Certifier workflows
* structured jurisdiction discovery
* historical change analysis
* trust-context references
* dataset exports
* versioned releases
* future APIs
* automated validation
* jurisdiction comparison tools
* Suite interoperability

---

## Canonical Principles

The Global package follows these enduring Atlas principles:

* Evidence before conclusions
* Structure before comparison
* Context before interpretation
* Transparency before assertion
* Human-readable sources remain authoritative
* Machine-readable representations must preserve source meaning
* Unsupported classifications must remain excluded
* Institutional ownership must remain clear
* Jurisdiction packages must remain independently reviewable
* Interoperability must not transfer authority

---

## Maintenance

Country package updates should preserve alignment across:

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

### Atlas Global Entry

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/global/
```

### Global Country Index

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/global/countries/
```

### Satoshium Atlas

```text
https://satoshium.us/atlas/
```

---

## Status

**Atlas Global Jurisdiction Package**

**Status:** Published · Complete

**Countries:** 52

**Canonical JSON Records:** 52

**Matched Generation Manifests:** 52

**Version:** 1.0

**Machine-Readable Foundation:** Complete

---

**Know the Jurisdictions. Navigate the Future.**
