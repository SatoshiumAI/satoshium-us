# Satoshium Certifier

# Status Definitions

**Version:** 1.0
**Status:** Draft
**Subsystem:** Satoshium Certifier
**Created:** July 2026
**Author:** Satoshium

---

# Overview

Status Definitions establish the possible outcomes of a certification review.

A status communicates the determination reached after evidence has been evaluated against an applicable certification standard.

Status values are used to record findings, communicate review outcomes, and support future reporting, auditing, and interoperability across the Satoshium ecosystem.

Status values do not describe the lifecycle state of a Certification Target.

Instead, they describe the outcome of a certification determination.

---

# Purpose

The purpose of Status Definitions is to answer a single question:

> What was the result of the review?

Every certification determination should be assigned one status value.

Status values provide:

* Consistency
* Transparency
* Traceability
* Reporting support
* Registry compatibility
* Future automation support

---

# Relationship to Lifecycle States

Status values and Lifecycle States serve different functions.

Lifecycle States answer:

> Where is the certification record in its lifecycle?

Examples:

* Created
* Reviewed
* Certified
* Expired
* Revoked
* Archived

Status values answer:

> What determination was reached?

Examples:

* Pass
* Conditional Pass
* Fail
* Revoked

Both may exist simultaneously.

Example:

```text
Lifecycle State: Certified
Status: Pass
```

Example:

```text
Lifecycle State: Certified
Status: Conditional Pass
```

Example:

```text
Lifecycle State: Revoked
Status: Revoked
```

---

# Status Hierarchy

Version 1.0 defines four certification statuses:

```text
Pass
Conditional Pass
Fail
Revoked
```

These statuses are intended to be simple, durable, and broadly applicable across all Certification Target categories.

---

# Status: Pass

## Definition

Pass indicates that the Certification Target satisfied the applicable certification standard without material deficiencies.

The target successfully met required criteria based upon the evidence reviewed.

---

## Meaning

A Pass determination indicates:

* Required criteria were satisfied.
* Evidence was considered sufficient.
* No material deficiencies were identified.
* Certification may be granted.

---

## Typical Outcome

A Pass determination normally supports:

```text
Lifecycle State:
Certified
```

---

## Example Statement

> The target satisfied all applicable certification requirements and is granted certification status of Pass.

---

# Status: Conditional Pass

## Definition

Conditional Pass indicates that the Certification Target substantially satisfied the applicable certification standard but contains identified limitations, deficiencies, exceptions, or outstanding items that do not prevent certification.

Certification may be granted subject to documented conditions.

---

## Meaning

A Conditional Pass determination indicates:

* Most requirements were satisfied.
* Minor deficiencies may exist.
* Corrective actions may be recommended.
* Certification remains appropriate despite identified conditions.

---

## Purpose

Conditional Pass exists because real-world systems are rarely perfect.

A target should not automatically fail certification because of minor issues that do not materially affect its purpose, functionality, or reliability.

---

## Typical Examples

Examples may include:

* Minor documentation gaps
* Incomplete metadata
* Non-critical formatting issues
* Recommended future improvements
* Temporary limitations

---

## Typical Outcome

A Conditional Pass determination normally supports:

```text
Lifecycle State:
Certified
```

with documented conditions.

---

## Example Statement

> The target satisfied certification requirements with minor exceptions documented within the certification record.

---

# Status: Fail

## Definition

Fail indicates that the Certification Target did not satisfy the applicable certification standard.

Material deficiencies were identified that prevent certification from being granted.

---

## Meaning

A Fail determination indicates:

* Required criteria were not satisfied.
* Evidence was insufficient.
* Material deficiencies were identified.
* Certification cannot be granted at this time.

---

## Purpose

Fail exists to preserve transparency and integrity within the certification process.

A certification framework must be capable of documenting unsuccessful outcomes as clearly as successful ones.

---

## Typical Examples

Examples may include:

* Missing required components
* Significant functionality failures
* Incomplete review evidence
* Non-compliance with certification requirements
* Inability to validate key claims

---

## Typical Outcome

A Fail determination normally supports:

```text
Lifecycle State:
Rejected
```

---

## Example Statement

> The target did not satisfy certification requirements and certification was not granted.

---

# Status: Revoked

## Definition

Revoked indicates that a previously granted certification has been withdrawn.

Revocation occurs after certification was previously awarded.

---

## Meaning

A Revoked determination indicates:

* Certification once existed.
* Certification is no longer valid.
* Historical records remain preserved.
* Certification should no longer be relied upon.

---

## Purpose

Revocation preserves trust in the certification framework by allowing previously granted certifications to be withdrawn when circumstances justify doing so.

---

## Typical Causes

Examples may include:

* Material errors discovered
* False or misleading evidence
* Significant changes to the target
* Standard violations
* Administrative review findings
* Integrity concerns

---

## Typical Outcome

A Revoked determination normally supports:

```text
Lifecycle State:
Revoked
```

---

## Example Statement

> Certification previously granted to this target has been revoked and should no longer be considered active.

---

# Status Selection Principles

Status determinations should follow several principles.

## Evidence-Based

Determinations should be supported by evidence.

## Consistent

Equivalent situations should produce equivalent outcomes.

## Transparent

The basis for the determination should be documented.

## Proportionate

The severity of findings should align with the status selected.

## Reviewable

Future reviewers should be able to understand why the determination was made.

---

# Determination Matrix

| Status           | Certification Granted | Typical Lifecycle State |
| ---------------- | --------------------- | ----------------------- |
| Pass             | Yes                   | Certified               |
| Conditional Pass | Yes                   | Certified               |
| Fail             | No                    | Rejected                |
| Revoked          | Previously Granted    | Revoked                 |

---

# Future Expansion

Version 1.0 intentionally maintains a minimal determination model.

Future versions may introduce additional status values if operational needs require them.

Examples may include:

* Pending
* Deferred
* Suspended
* Under Review

No additional status values are defined at this time.

---

# Long-Term Vision

Status Definitions provide a durable language for communicating certification outcomes across all present and future Satoshium subsystems.

Whether the target is a page, report, workflow, service, dataset, tool, or future artifact category, status values should allow reviewers, users, auditors, AI agents, and future systems to quickly understand the result of a certification determination.

The goal is not complexity.

The goal is clarity.

---

# Revision History

| Version | Date      | Description                                  |
| ------- | --------- | -------------------------------------------- |
| 1.0     | July 2026 | Initial Status Definitions document created. |

---

# Guiding Statement

> Certification should communicate more than approval.
>
> It should communicate the outcome of review.
>
> Status Definitions provide the language through which those outcomes are preserved, understood, and trusted.
