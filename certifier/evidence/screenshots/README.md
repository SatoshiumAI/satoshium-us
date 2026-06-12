# Screenshot Evidence

This directory contains screenshots used as certification evidence within the Satoshium Certifier framework.

Screenshots provide visual documentation of a target at a specific point in time and serve as one of the primary evidence types recognized by Certifier.

Screenshots help preserve the observable state of pages, services, workflows, interfaces, records, and other certification targets.

---

# Purpose

The purpose of the screenshots directory is to preserve visual evidence supporting certification activities.

Screenshots may document:

* Public webpages
* Published reports
* User interfaces
* Service outputs
* Workflow completion
* Registry entries
* Certification records
* Evidence packages
* Historical milestones

Screenshots provide a visual record of what existed when certification occurred.

---

# Screenshot Philosophy

Certifier seeks to preserve evidence that future reviewers can inspect and understand.

Screenshots serve an important role because they capture information that may change over time.

Examples include:

* Page layouts
* Navigation structures
* Published content
* Visual indicators
* Interface states
* Completion milestones

A screenshot creates a visual snapshot of a moment in time.

---

# What Belongs Here

Examples of screenshot evidence include:

## Public Pages

Screenshots of publicly accessible pages.

Examples:

```text id="d41j3v"
atlas-homepage.png
certifier-homepage.png
registry-homepage.png
```

---

## Certification Targets

Screenshots documenting the target being reviewed.

Examples:

```text id="pf5xj1"
atlas-california-page.png
atlas-new-hampshire-page.png
```

---

## Certification Records

Screenshots of generated certification outputs.

Examples:

```text id="m29wpt"
certification-report.png
certification-receipt.png
```

---

## Workflow Evidence

Screenshots demonstrating workflow completion or operational processes.

Examples:

```text id="dt1r8r"
atlas-publication-workflow.png
certifier-review-workflow.png
```

---

## Milestone Evidence

Screenshots documenting significant events or accomplishments.

Examples:

```text id="bgd7ls"
atlas-initial-build-complete.png
certifier-v1-launch.png
```

---

# Suggested Structure

```text id="oj3t0q"
screenshots/
├── atlas/
├── certifier/
├── registry/
├── workflows/
├── milestones/
└── archive/
```

Additional categories may be introduced as the ecosystem expands.

---

# Screenshot Quality Principles

Screenshots should be:

## Relevant

The screenshot should directly support the certification activity.

---

## Legible

Important content should be visible and readable.

Avoid screenshots that are:

* Cropped excessively
* Blurry
* Incomplete
* Obscured

---

## Accurate

Screenshots should accurately represent the reviewed target at the time they were captured.

Screenshots should not be modified in ways that alter the meaning of the evidence.

---

## Traceable

Screenshots should be identifiable and linked to a certification record whenever practical.

---

## Preserved

Screenshots should remain accessible for future review whenever practical.

---

# Recommended Metadata

Each screenshot should be accompanied by metadata whenever practical.

Suggested fields include:

```text id="v83c6k"
evidence_id:
target_name:
target_type:
captured_at:
captured_by:
source_url:
related_record_id:
description:
notes:
```

---

# Naming Conventions

Screenshots should use descriptive filenames.

Recommended format:

```text id="1ryux8"
target-name_YYYY-MM-DD.png
```

Examples:

```text id="3hjcjc"
atlas-homepage_2026-07-25.png
atlas-initial-build_2026-07-25.png
certifier-launch_2026-07-31.png
```

For versioned screenshots:

```text id="m6k5l2"
atlas-homepage-v1.png
atlas-homepage-v2.png
```

Avoid generic filenames such as:

```text id="7ndp4v"
image1.png
screenshot.png
new-image-final.png
```

---

# Relationship to Certification Records

Screenshots may be referenced by:

* Certification Records
* Certification Reports
* Certification Receipts
* Registry Entries
* Attestation Records
* Historical Records

Screenshots should be treated as supporting evidence rather than standalone certification artifacts.

---

# Relationship to Reports

Screenshots frequently support report findings.

Typical relationship:

```text id="h0g4m2"
Screenshot
      ↓
Observation
      ↓
Finding
      ↓
Certification Report
```

The screenshot provides visual evidence.

The report provides interpretation and context.

---

# Relationship to Notes

Screenshots and notes often work together.

Example:

```text id="9yoc92"
Screenshot:
Atlas homepage displaying completed navigation structure.

Note:
All required navigation elements defined by the Atlas standard were present and functional at the time of review.
```

Together they provide stronger evidence than either alone.

---

# Relationship to Hashes

Screenshots may be hashed to support integrity verification.

Example workflow:

```text id="cykbhi"
Screenshot
      ↓
SHA-256 Hash
      ↓
Hash Record
      ↓
Future Verification
```

Hash records should be preserved within:

```text id="rv9g1g"
evidence/hashes/
```

whenever integrity verification is desired.

---

# Relationship to Chronicle

Screenshots may become important historical artifacts.

Examples include:

* Atlas completion
* Certifier launch
* First certification issued
* Registry launch
* Major ecosystem milestones

Such screenshots may later support Chronicle entries documenting the history of the ecosystem.

---

# Relationship to SOU Activities

Screenshots may play an important role in supporting future Statement of Use activities.

Examples may include:

* Public service availability
* Operational interfaces
* Published reports
* Certification outputs
* User-facing functionality

Screenshots can help demonstrate real-world use of services and systems.

---

# Retention

Screenshots should generally be preserved for as long as the associated certification record remains relevant.

Significant screenshots should be considered candidates for long-term preservation.

Historical screenshots may be moved to:

```text id="yj33xk"
screenshots/archive/
```

rather than deleted.

---

# Long-Term Vision

The screenshots directory serves as the visual memory of Certifier.

Evidence records may explain what existed.

Reports may explain why certification occurred.

Screenshots show what was actually seen.

As the Satoshium ecosystem evolves, screenshots may become some of the most valuable historical artifacts associated with certification events.

For that reason, screenshots should be preserved thoughtfully and documented clearly.

---

# Guiding Statement

> Reports explain.
>
> Notes provide context.
>
> Hashes preserve integrity.
>
> Screenshots preserve visibility.
>
> The screenshots directory exists to capture what existed at the moment certification occurred.
