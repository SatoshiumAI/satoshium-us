# Satoshium Certifier

# Certification Classes

**Version:** 1.0
**Status:** Draft
**Subsystem:** Satoshium Certifier
**Created:** July 2026
**Author:** Satoshium

---

# Overview

Certification Classes provide a standardized method for expressing the level of review, maturity, and confidence associated with a Certification Target.

While lifecycle states communicate a target's current status, Certification Classes communicate the nature and depth of certification that has been achieved.

Certification Classes are intended to be:

* Understandable
* Scalable
* Technology-neutral
* Applicable across target types
* Suitable for both human and machine interpretation

Certification Classes do not represent rankings, awards, or competitive achievements.

Instead, they describe increasing levels of operational maturity and review.

---

# Purpose

Certification Classes exist to answer a simple question:

> What level of certification has this target achieved?

A certification class provides context beyond a simple pass or fail determination.

For example:

* A documented concept may qualify as Informational.
* A functioning service may qualify as Operational.
* A reviewed and evidence-supported artifact may qualify as Verified.

This approach creates a common language that can be applied consistently across the Satoshium ecosystem.

---

# Class Hierarchy

The Version 1.0 certification hierarchy consists of three classes:

```text
Informational
      ↓
Operational
      ↓
Verified
```

Each class builds upon the requirements of the previous class.

Higher classes inherit the expectations of lower classes.

---

# Class: Informational

## Definition

Informational certification indicates that a target has been identified, documented, and structured according to applicable requirements.

The target exists and sufficient information has been provided to understand its purpose and characteristics.

---

## Purpose

Informational certification establishes awareness and documentation.

It answers the question:

> Does this thing exist and is it sufficiently documented?

---

## Characteristics

An Informational target typically possesses:

* Defined identity
* Documented purpose
* Basic metadata
* Structured description
* Classification information

---

## Examples

Examples may include:

* Draft specifications
* Design documents
* Policy documents
* Research concepts
* Proposed workflows
* Planned services

---

## Example Statement

> This target has been documented and satisfies the requirements for Informational certification.

---

# Class: Operational

## Definition

Operational certification indicates that a target not only exists, but is functioning according to its intended purpose.

Operational certification demonstrates practical implementation.

---

## Purpose

Operational certification answers the question:

> Does this thing work?

---

## Characteristics

An Operational target typically possesses:

* Informational requirements satisfied
* Functional implementation
* Demonstrated operation
* Defined inputs and outputs
* Repeatable execution

---

## Examples

Examples may include:

* Functioning websites
* Operational services
* Working workflows
* Active tools
* Executable processes

---

## Example Statement

> This target is operational and demonstrates functional implementation consistent with its stated purpose.

---

# Class: Verified

## Definition

Verified certification indicates that a target has undergone formal review and that supporting evidence has been examined against an established certification standard.

Verified represents the highest certification class defined in Version 1.0.

---

## Purpose

Verified certification answers the question:

> Has this target been reviewed and supported by evidence?

---

## Characteristics

A Verified target typically possesses:

* Informational requirements satisfied
* Operational requirements satisfied
* Formal review completed
* Evidence collected
* Certification record generated
* Determination documented

---

## Examples

Examples may include:

* Certified Atlas subsystems
* Certified workflows
* Certified datasets
* Certified services
* Certified reports

---

## Example Statement

> This target has been reviewed against an established certification standard and is supported by documented evidence.

---

# Relationship to Lifecycle States

Certification Classes and Lifecycle States serve different purposes.

Lifecycle States answer:

> What is the target's current status?

Examples:

* Created
* Reviewed
* Certified
* Expired
* Revoked
* Archived

Certification Classes answer:

> What level of certification has the target achieved?

Examples:

* Informational
* Operational
* Verified

A target may therefore possess both:

```text
Status: Certified
Class: Verified
```

or

```text
Status: Certified
Class: Operational
```

depending upon the applicable certification standard.

---

# Class Advancement

Certification Classes are intended to be progressive.

A target may advance through multiple classes over time.

Example progression:

```text
Informational
      ↓
Operational
      ↓
Verified
```

Advancement should be supported by documented review activities and evidence.

---

# Future Expansion

The Version 1.0 hierarchy intentionally remains simple.

Future versions may introduce additional classes if justified by operational needs.

Potential future classes may include:

```text
Informational
Operational
Verified
Attested
```

or

```text
Informational
Operational
Verified
Validated
```

No additional classes are defined at this time.

---

# Design Principles

Certification Classes should remain:

## Clear

Users should easily understand the meaning of each class.

## Stable

Classes should remain useful over long periods of time.

## Neutral

Classes should describe maturity and review, not prestige.

## Scalable

Classes should accommodate future technologies and target types.

## Interoperable

Classes should support integration with future Satoshium subsystems.

---

# Long-Term Vision

Certification Classes provide a common framework for communicating confidence and maturity across the Satoshium ecosystem.

As additional subsystems emerge, Certification Classes will allow users, contributors, auditors, AI agents, and future automation systems to quickly understand the level of review associated with a target.

The objective is not to rank artifacts.

The objective is to communicate trust through transparency.

---

# Revision History

| Version | Date      | Description                                     |
| ------- | --------- | ----------------------------------------------- |
| 1.0     | July 2026 | Initial Certification Classes document created. |

---

# Guiding Statement

> Information can exist.
>
> Systems can operate.
>
> Evidence can verify.
>
> Certification Classes provide a common language for describing that progression.
