# Comparison Schema

**A standardized structure for comparative analysis within Navigator.**

The Comparison Schema defines the organizational framework used to compare jurisdictions, records, signals, trust dimensions, and related resources within Satoshium Navigator.

This schema establishes a consistent structure for conducting, documenting, and presenting comparisons while preserving transparency, traceability, and methodological consistency.

---

## Purpose

Comparisons become more useful when they follow repeatable and understandable structures.

Without a standardized framework, comparison outputs may become inconsistent, difficult to interpret, or challenging to reproduce.

The Comparison Schema exists to support consistent comparative analysis throughout Navigator.

---

## Core Mission

The mission of the Comparison Schema is to provide a common framework for evaluating similarities, differences, relationships, and distinctions between records.

The schema seeks to improve consistency, transparency, comparability, and usability.

---

## Schema Structure

A comparison record may include the following components.

---

### Comparison Metadata

Information describing the comparison itself.

**Fields**

```text
Comparison ID
Comparison Type
Creation Date
Last Updated
Status
Version
```

---

### Comparison Targets

The records, jurisdictions, or subjects being evaluated.

**Fields**

```text
Primary Subject
Secondary Subject
Additional Subjects
Subject Type
```

**Examples**

```text
Texas vs Florida

Singapore vs Hong Kong

Country A vs Country B vs Country C
```

---

### Comparison Scope

Defines what is included within the comparison.

**Fields**

```text
Categories Reviewed
Included Records
Included Signals
Included Time Periods
Filters Applied
```

---

### Comparison Criteria

Defines the characteristics used during evaluation.

**Fields**

```text
Criterion Name
Criterion Description
Methodology Reference
Weighting (Optional)
```

**Examples**

```text
Economic Signals
Technology Signals
Trust Dimensions
Historical Context
Infrastructure Indicators
```

---

### Supporting Records

References to records utilized during the comparison.

**Fields**

```text
Atlas Records
Registry Records
Chronicle Records
Certifier Records
Attestor Records
Additional References
```

---

### Comparative Findings

Documents observed similarities, differences, and relationships.

**Fields**

```text
Observations
Differences
Similarities
Relationships
Supporting Notes
```

---

### Comparative Summary

Provides a concise overview of findings.

**Fields**

```text
Summary Statement
Key Observations
Notable Differences
Additional Context
```

---

### References

Supporting materials associated with the comparison.

**Fields**

```text
Source References
Cross References
Related Records
Supporting Documentation
```

---

## Example Structure

```text
Comparison ID:
COMP-001

Comparison Type:
Jurisdiction Comparison

Primary Subject:
Texas

Secondary Subject:
Florida

Criteria:
Economic Signals
Governance Signals
Trust Dimensions

Supporting Records:
Atlas-TX
Atlas-FL

Summary:
Comparison completed.
```

---

## Comparison Categories

The schema may support:

### Jurisdiction Comparisons

Comparisons involving countries, states, territories, provinces, or other jurisdictions.

---

### Signal Comparisons

Comparisons involving observable indicators and trends.

---

### Trust Dimension Comparisons

Comparisons involving structured trust-related categories.

---

### Historical Comparisons

Comparisons involving records across different time periods.

---

### Record Comparisons

Comparisons involving individual records and associated resources.

---

## Relationship to Navigator

The Comparison Schema supports one of Navigator's primary analytical functions.

Navigator uses this schema to ensure comparative outputs remain consistent and understandable.

---

## Relationship to Atlas

Atlas provides many of the underlying records used during comparison activities.

The Comparison Schema helps organize and present those records within comparative workflows.

---

## Relationship to the Satoshium Ecosystem

The Comparison Schema may reference information originating from:

* Atlas
* Certifier
* Registry
* Chronicle
* Anchor
* Beacon
* Attestor

when relevant records are available.

---

## Design Principles

The Comparison Schema is built upon several foundational principles:

* Consistency over ambiguity
* Transparency over opacity
* Context over isolation
* Traceability over uncertainty
* Evidence over assumption
* Understanding over confusion
* Repeatability over improvisation

---

## Validation Objectives

Comparison records should strive to:

* Identify comparison targets clearly.
* Document comparison criteria.
* Preserve supporting references.
* Distinguish observations from conclusions.
* Maintain methodological transparency.
* Support independent review.

These objectives improve reliability and usability.

---

## Future Extensions

Future versions may support:

* Multi-Jurisdiction Comparisons
* Dynamic Comparison Frameworks
* Advanced Weighting Models
* Comparative Scoring Systems
* Visualization Structures
* Automated Comparative Outputs

Additional capabilities may be introduced as Navigator evolves.

---

## Disclaimer

The Comparison Schema provides a structural framework for organizing comparative information.

The schema itself does not determine conclusions, rankings, recommendations, or outcomes.

Comparative outputs depend upon available records, methodologies, and supporting information.

---

## Guiding Statement

> Information can be organized.
>
> Records can be compared.
>
> Differences can be understood.
>
> Context can be revealed.
>
> The Comparison Schema exists to make that possible.

---

**Version:** 1.0

**Maintainer:** Satoshium
