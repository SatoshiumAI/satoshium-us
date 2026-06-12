# Satoshium Certifier

# Certification Lifecycle

**Version:** 1.0
**Status:** Draft
**Subsystem:** Satoshium Certifier
**Created:** July 2026
**Author:** Satoshium

---

# Overview

The Certification Lifecycle defines the states through which a Certification Target may progress during its existence within the Satoshium Certifier framework.

The lifecycle provides a standardized method for tracking certification status, preserving review history, and documenting changes over time.

Every certification record should exist in exactly one lifecycle state at any given moment.

Lifecycle states enable:

* Status tracking
* Review management
* Certification governance
* Registry integration
* Historical preservation
* Auditability
* Future automation

The lifecycle is designed to remain stable over time even as certification standards and technologies evolve.

---

# Lifecycle Philosophy

Certification is not a single event.

Certification is a process.

A target is created, reviewed, evaluated, potentially certified, and eventually preserved as part of the historical record.

The lifecycle exists to answer fundamental questions:

* What is the current status?
* What actions have occurred?
* What actions remain possible?
* What historical events have occurred?
* Can the certification history be reconstructed later?

The lifecycle provides those answers through clearly defined states.

---

# Lifecycle Diagram

```text
Created
   ↓
Reviewed
   ↓
Certified
   ↓
Expired
   ↓
Archived
```

Alternative path:

```text
Created
   ↓
Reviewed
   ↓
Rejected
   ↓
Archived
```

Alternative path:

```text
Certified
   ↓
Revoked
   ↓
Archived
```

---

# State: Created

## Definition

Created represents the initial registration of a Certification Target.

The target has been identified and entered into the certification process but has not yet undergone formal review.

---

## Purpose

The Created state establishes:

* Target identity
* Initial metadata
* Ownership information
* Registration date
* Classification

---

## Typical Activities

Examples include:

* Target registration
* Metadata creation
* Initial documentation
* Classification assignment
* Review scheduling

---

## Allowed Next States

```text
Reviewed
Archived
```

---

# State: Reviewed

## Definition

Reviewed indicates that a certification evaluation has been performed.

Evidence has been examined and applicable standards have been applied.

A determination has been reached but final lifecycle outcomes may vary.

---

## Purpose

The Reviewed state establishes that evaluation activities occurred.

This state serves as the decision point for certification outcomes.

---

## Typical Activities

Examples include:

* Evidence collection
* Validation activities
* Checklist completion
* Standard application
* Determination recording

---

## Allowed Next States

```text
Certified
Rejected
Archived
```

---

# State: Certified

## Definition

Certified indicates that the Certification Target successfully satisfied the applicable certification standard.

Certification has been granted and recorded.

---

## Purpose

The Certified state serves as the primary success outcome of the certification process.

---

## Typical Activities

Examples include:

* Certification approval
* Receipt generation
* Report publication
* Registry registration
* Status publication

---

## Characteristics

A Certified target:

* Passed review
* Satisfied applicable standards
* Possesses certification records
* Possesses supporting evidence

---

## Allowed Next States

```text
Expired
Revoked
Archived
```

---

# State: Expired

## Definition

Expired indicates that a previously Certified target has exceeded its certification validity period or requires re-evaluation.

Expiration does not imply failure.

Expiration indicates that certification status is no longer considered current.

---

## Purpose

The Expired state encourages periodic review and prevents indefinite reliance on outdated certifications.

---

## Examples

Examples include:

* Time-based certifications
* Version-specific certifications
* Certifications requiring periodic renewal

---

## Characteristics

An Expired target:

* Was previously Certified
* Retains historical certification records
* May be eligible for re-certification

---

## Allowed Next States

```text
Reviewed
Archived
```

---

# State: Revoked

## Definition

Revoked indicates that a previously Certified target has had its certification withdrawn.

Revocation occurs when certification is determined to no longer be valid.

---

## Purpose

The Revoked state preserves historical transparency while clearly indicating that certification should no longer be relied upon.

---

## Possible Causes

Examples include:

* Material errors discovered
* False evidence identified
* Standard violations identified
* Significant changes to target content
* Administrative action

---

## Characteristics

A Revoked target:

* Was previously Certified
* Retains certification history
* Retains evidence records
* No longer holds active certification status

---

## Allowed Next States

```text
Reviewed
Archived
```

---

# State: Rejected

## Definition

Rejected indicates that a Certification Target was reviewed but did not satisfy the applicable certification standard.

---

## Purpose

The Rejected state provides transparency regarding unsuccessful certification attempts.

Certification systems must preserve both successful and unsuccessful outcomes.

---

## Characteristics

A Rejected target:

* Completed review
* Failed to satisfy required standards
* Retains review records
* May be eligible for future resubmission

---

## Allowed Next States

```text
Reviewed
Archived
```

---

# State: Archived

## Definition

Archived represents the final preservation state of a certification record.

No further lifecycle activity is expected.

---

## Purpose

The Archived state ensures long-term preservation of certification history.

---

## Characteristics

An Archived target:

* Remains historically accessible
* Retains associated records
* Retains evidence references
* Retains lifecycle history

---

## Allowed Next States

```text
None
```

Archived is considered a terminal state.

---

# Lifecycle Events

Lifecycle state transitions should generate records whenever practical.

Examples include:

* Creation event
* Review event
* Certification event
* Expiration event
* Revocation event
* Rejection event
* Archival event

These events support future auditing and historical reconstruction.

---

# Re-Certification

Certification Targets may re-enter the lifecycle following:

* Expiration
* Revocation
* Rejection

Re-certification should generate new review records while preserving prior certification history.

Historical records should never be destroyed solely because a new certification occurs.

---

# Lifecycle Integrity

Lifecycle states should satisfy several principles:

## Clarity

Current status should be unambiguous.

## Traceability

Transitions should be documented.

## Preservation

Historical states should remain recoverable.

## Consistency

Equivalent situations should produce equivalent state transitions.

## Transparency

Certification history should remain understandable.

---

# Long-Term Vision

The Certification Lifecycle establishes the foundation upon which future Certifier capabilities will operate.

As Certifier expands to support additional targets, automation, AI-assisted review, Registry integration, and historical preservation systems, lifecycle states will remain the common language through which certification status is communicated.

The lifecycle therefore serves not merely as a workflow, but as the operational history of trust.

---

# Revision History

| Version | Date      | Description                                       |
| ------- | --------- | ------------------------------------------------- |
| 1.0     | July 2026 | Initial Certification Lifecycle document created. |

---

# Guiding Statement

> Certification is not a moment.
>
> It is a documented journey from creation, through review, to historical preservation.
>
> The Certification Lifecycle exists to preserve that journey.
