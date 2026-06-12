# Satoshium Certifier

# Workflow Diagram

**Version:** 1.0
**Status:** Draft
**Subsystem:** Satoshium Certifier
**Created:** July 2026
**Author:** Satoshium

---

# Overview

The Certifier Workflow defines the standard process by which a Certification Target moves from initial submission or identification through review, evidence collection, certification determination, receipt generation, and Registry publication.

The workflow is designed to be simple, repeatable, and adaptable.

Version 1.0 defines the core Certifier sequence:

```text
Input
  ↓
Review
  ↓
Evidence
  ↓
Certification
  ↓
Receipt
  ↓
Registry
```

This sequence represents the minimum complete workflow for a certification event.

---

# Purpose

The purpose of the Certifier Workflow is to create a repeatable process for certification activities.

The workflow exists to answer:

* What enters the certification process?
* How is it reviewed?
* What evidence is collected?
* How is certification determined?
* What public proof is generated?
* Where is the certified record cataloged?

A clear workflow ensures that Certifier can be performed consistently by humans, AI systems, automated tools, or hybrid review teams.

---

# Core Workflow

```text
┌──────────┐
│  Input   │
└────┬─────┘
     ↓
┌──────────┐
│  Review  │
└────┬─────┘
     ↓
┌──────────┐
│ Evidence │
└────┬─────┘
     ↓
┌────────────────┐
│ Certification  │
└────┬───────────┘
     ↓
┌──────────┐
│ Receipt  │
└────┬─────┘
     ↓
┌──────────┐
│ Registry │
└──────────┘
```

---

# Stage 1: Input

## Definition

Input is the entry point into the certification process.

At this stage, a Certification Target is identified and prepared for review.

---

## Purpose

The Input stage establishes:

* What is being reviewed
* Why it is being reviewed
* What category it belongs to
* What standard may apply
* Where the target can be found

---

## Typical Inputs

Examples include:

* A web page
* A report
* A service
* A workflow
* A dataset
* A tool
* A subsystem
* A public record
* A GitHub repository
* A service specimen

---

## Output of Stage

The output of the Input stage is a registered Certification Target.

---

# Stage 2: Review

## Definition

Review is the process of evaluating the Certification Target against an applicable certification standard.

---

## Purpose

The Review stage determines whether the target satisfies required criteria.

---

## Review Methods

Review may be performed through:

* Human review
* AI-assisted review
* Human-AI-assisted review
* Automated review

---

## Typical Review Activities

Examples include:

* Reading documentation
* Checking required sections
* Reviewing functionality
* Validating links
* Comparing against standards
* Identifying gaps
* Recording observations

---

## Output of Stage

The output of the Review stage is a set of preliminary findings.

---

# Stage 3: Evidence

## Definition

Evidence is the collection and documentation of materials supporting the certification review.

---

## Purpose

The Evidence stage ensures that review determinations are supported by traceable materials.

---

## Evidence Types

Core evidence types include:

* Screenshots
* Reports
* URLs
* Hashes
* Notes

---

## Typical Evidence Activities

Examples include:

* Capturing screenshots
* Recording URLs
* Generating review notes
* Preparing reports
* Creating hash values
* Preserving file references

---

## Output of Stage

The output of the Evidence stage is an evidence package supporting the review.

---

# Stage 4: Certification

## Definition

Certification is the determination stage.

At this stage, the reviewer evaluates the review findings and evidence package to assign a certification outcome.

---

## Purpose

The Certification stage determines whether certification should be granted, denied, conditioned, revoked, or otherwise recorded.

---

## Possible Determinations

Version 1.0 defines the following determination statuses:

* Pass
* Conditional Pass
* Fail
* Revoked

---

## Certification Classes

Version 1.0 defines the following certification classes:

* Informational
* Operational
* Verified

---

## Output of Stage

The output of the Certification stage is a certification record and determination.

---

# Stage 5: Receipt

## Definition

The Receipt stage generates a public-facing certification receipt.

---

## Purpose

The receipt provides concise proof that certification occurred.

A receipt summarizes:

* Certification Target
* Certification Class
* Determination Status
* Certification Date
* Certification Standard
* Evidence Summary
* Report Reference

---

## Output of Stage

The output of the Receipt stage is a Certification Receipt.

---

# Stage 6: Registry

## Definition

The Registry stage records the certification event in a catalog or index.

---

## Purpose

Registry publication makes certified records discoverable, searchable, and referenceable.

The Registry may be public, private, or subsystem-specific.

---

## Registry Record May Include

Examples include:

* Certification Record ID
* Receipt ID
* Report ID
* Target Name
* Target Type
* Certification Class
* Status
* Date Certified
* Reference URLs

---

## Output of Stage

The output of the Registry stage is a discoverable Registry entry.

---

# Workflow Outputs

A complete certification workflow may produce:

* Certification Target record
* Review notes
* Evidence package
* Certification record
* Certification report
* Certification receipt
* Registry entry
* Historical Chronicle entry
* Future Anchor reference

---

# Standard Workflow Summary

```text
Input
  ↓
Target is identified and registered.

Review
  ↓
Target is evaluated against applicable standards.

Evidence
  ↓
Supporting materials are collected and documented.

Certification
  ↓
Determination is made and certification record is created.

Receipt
  ↓
Public proof of certification is generated.

Registry
  ↓
Certified record is cataloged for future discovery.
```

---

# Workflow Relationship to Lifecycle

The Certifier Workflow and Certification Lifecycle are related but separate.

Workflow describes the operational process.

Lifecycle describes the current state of the certification record.

Example relationship:

| Workflow Stage | Typical Lifecycle State |
| -------------- | ----------------------- |
| Input          | Created                 |
| Review         | Reviewed                |
| Certification  | Certified or Rejected   |
| Receipt        | Certified               |
| Registry       | Certified or Archived   |

---

# Workflow Relationship to Future Subsystems

The Certifier Workflow is designed to support future integration with other Satoshium subsystems.

| Subsystem | Relationship                             |
| --------- | ---------------------------------------- |
| Atlas     | Provides targets for certification       |
| Registry  | Catalogs certification records           |
| Chronicle | Records certification milestones         |
| Anchor    | Preserves hashes and evidence references |
| Beacon    | Signals certified records publicly       |
| Attestor  | Supports future independent verification |

---

# Failure and Exception Paths

Not every workflow results in certification.

Possible exception paths include:

```text
Input
  ↓
Review
  ↓
Fail
  ↓
Rejected Record
```

or:

```text
Certified
  ↓
Issue Discovered
  ↓
Revoked
  ↓
Registry Updated
```

or:

```text
Certified
  ↓
Validity Period Ends
  ↓
Expired
  ↓
Re-Review
```

Exception paths should be documented to preserve transparency.

---

# Minimum Complete Workflow

For Version 1.0, a minimum complete certification workflow should include:

* Identified target
* Applicable standard
* Review performed
* Evidence documented
* Determination assigned
* Certification record created
* Receipt generated

Registry publication is preferred but may be deferred until the Registry subsystem is operational.

---

# Long-Term Vision

The Certifier Workflow is intended to evolve from a manual or semi-manual process into a repeatable, AI-assisted, and eventually automatable certification pipeline.

Future versions may support:

* Automated evidence capture
* Structured review forms
* Certification dashboards
* Registry APIs
* Anchor integration
* Attestor validation
* AI agent certification workflows

The workflow should remain understandable even as implementation becomes more advanced.

---

# Revision History

| Version | Date      | Description                                          |
| ------- | --------- | ---------------------------------------------------- |
| 1.0     | July 2026 | Initial Certifier Workflow Diagram document created. |

---

# Guiding Statement

> Certifier begins with an input and ends with a record others can find.
>
> The workflow exists to transform review into evidence, evidence into certification, and certification into discoverable trust.
