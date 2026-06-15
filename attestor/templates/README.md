# Templates

## Purpose

Templates provide standardized structures for creating attestations, evidence records, trust records, correction records, and related documentation within Attestor.

The purpose of templates is to promote consistency, transparency, interoperability, and traceability across trust-related records.

Templates help ensure that important information is documented in a predictable and understandable manner.

---

## Why Templates Matter

Trust systems rely upon clear and consistent information.

Without templates:

* Records may vary significantly.
* Important information may be omitted.
* Relationships may become difficult to interpret.
* Interoperability may be reduced.

Templates help create a shared structure for documentation.

---

## Template Philosophy

Templates provide structure.

Templates do not determine conclusions.

Templates help ensure that records include:

* Attribution
* Context
* Evidence references
* Timestamps
* Supporting information

Consistency improves transparency.

---

## Current Template Categories

The initial Attestor framework includes conceptual templates for:

```text
Attestation Templates
Evidence Templates
Trust Record Templates
Correction Templates
Retraction Templates
Relationship Templates
```

Additional templates may be introduced over time.

---

## Attestation Template

### Purpose

Used to document an attestation made by an attestor.

### Example Structure

```text
Attestation ID:
Date:
Attestor:
Subject:
Attestation Type:
Statement:
Supporting Evidence:
Sources:
Related Records:
Status:
Notes:
```

This template provides a consistent structure for documenting attestations.

---

## Evidence Template

### Purpose

Used to document evidence associated with an attestation or trust-related record.

### Example Structure

```text
Evidence ID:
Date:
Evidence Type:
Source:
Description:
Associated Record:
Supporting References:
Status:
Notes:
```

Evidence templates help preserve context and attribution.

---

## Trust Record Template

### Purpose

Used to document trust-related observations, relationships, or contextual information.

### Example Structure

```text
Trust Record ID:
Date:
Subject:
Trust Context:
Related Attestations:
Supporting Evidence:
Confidence Notes:
Sources:
Status:
```

Trust records help preserve trust-related information without imposing conclusions.

---

## Correction Template

### Purpose

Used to document corrections affecting existing records.

### Example Structure

```text
Correction ID:
Date:
Original Record:
Correction Type:
Description:
Reason:
Supporting Evidence:
Correcting Party:
Status:
```

Corrections help preserve transparency while improving understanding.

---

## Retraction Template

### Purpose

Used to document the withdrawal of an attestation.

### Example Structure

```text
Retraction ID:
Date:
Original Attestation:
Attestor:
Reason:
Supporting Information:
Status:
```

Retractions should remain visible as part of the historical record.

---

## Relationship Template

### Purpose

Used to document relationships among entities, records, attestations, or evidence.

### Example Structure

```text
Relationship ID:
Date:
Entity A:
Entity B:
Relationship Type:
Description:
Supporting References:
Status:
```

Relationship templates help preserve context and traceability.

---

## Template Design Principles

### Transparency

Templates should make important information visible.

### Attribution

Responsible parties should be identifiable whenever practical.

### Traceability

Templates should support investigation and review.

### Consistency

Records should be documented predictably.

### Interoperability

Templates should support cross-system compatibility.

---

## Relationship to Schemas

Templates and schemas serve different purposes.

A simplified distinction may be represented as:

```text
Schema   → Structure Definition
Template → Record Creation Format
```

Schemas define how information is organized.

Templates provide practical formats for creating records.

---

## Relationship to Records

Templates often produce records.

A simplified relationship may be represented as:

```text
Template → Record
```

Templates help ensure records contain important information.

---

## Relationship to Attestations

Attestation templates help standardize trust-related statements.

Consistent attestation structures improve:

* Transparency
* Reviewability
* Traceability
* Historical preservation

---

## Relationship to Registry

Registry may catalog records created using Attestor templates.

Consistent templates improve record management and interoperability.

---

## Relationship to Chronicle

Records created from templates may become part of the historical record preserved by Chronicle.

Structured records improve historical understanding.

---

## Relationship to Beacon

Beacon may help users discover records created using Attestor templates.

Structured records improve discoverability.

---

## Relationship to the Satoshium Suite

Templates help support consistency across:

```text
Atlas
Navigator
Beacon
Certifier
Registry
Chronicle
Anchor
Attestor
```

Shared structures improve interoperability throughout the ecosystem.

---

## Long-Term Vision

As Attestor evolves, templates may expand to support:

* Advanced attestation frameworks
* Reputation systems
* Trust networks
* Governance records
* Confidence models
* Interoperable trust standards

Future templates may become increasingly sophisticated while preserving transparency and traceability.

---

## Guiding Statement

The purpose of a template may be summarized as:

```text
Trust requires consistency.

Templates help create consistency.
```

---

## Status

Template standards are currently under development.

This document defines conceptual templates and guiding principles rather than finalized operational formats.
