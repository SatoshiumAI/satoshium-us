# Archived Evidence

This directory contains historical evidence that has been retired from active certification use but remains preserved for reference, traceability, auditing, and historical recordkeeping.

Archived evidence remains part of the Certifier record system and should not be interpreted as deleted, invalid, or forgotten.

---

# Purpose

The purpose of the archived evidence directory is to preserve evidence that is no longer considered active while maintaining historical transparency.

Examples include:

* Superseded evidence
* Expired certification evidence
* Revoked certification evidence
* Replaced screenshots
* Replaced reports
* Historical evidence packages
* Legacy certification artifacts
* Retired evidence references

The objective is preservation rather than removal.

---

# Preservation Philosophy

Certifier is founded upon the principle that certification history should remain reviewable whenever practical.

Evidence that contributed to a certification decision may remain historically significant even after:

* A certification expires
* A certification is revoked
* A certification is replaced
* Standards evolve
* New evidence becomes available

Archiving preserves context.

Deletion removes context.

Whenever practical, Certifier favors preservation.

---

# What Belongs Here

Examples of archived evidence include:

## Superseded Evidence

Evidence replaced by newer versions.

Example:

```text
atlas-homepage-screenshot-v1.png
```

replaced by:

```text
atlas-homepage-screenshot-v2.png
```

---

## Expired Certification Evidence

Evidence associated with certifications that have reached an expired lifecycle state.

---

## Revoked Certification Evidence

Evidence associated with certifications that were previously granted but later revoked.

Historical evidence should remain available to support review of the revocation decision.

---

## Historical Evidence Packages

Complete evidence collections associated with significant certification events.

Examples:

```text
atlas-initial-build-certification/
```

```text
certifier-v1-launch/
```

---

## Legacy Records

Evidence generated under previous certification standards or prior Certifier versions.

---

# Suggested Structure

```text
archived/
├── expired/
├── revoked/
├── superseded/
├── legacy/
└── historical/
```

Additional categories may be introduced as operational needs evolve.

---

# Naming Conventions

Archived evidence should remain clearly identifiable.

Recommended format:

```text
target-name_status_YYYY-MM-DD
```

Examples:

```text
atlas-initial-build_expired_2028-07-25
```

```text
workflow-standard-v1_superseded_2029-03-01
```

```text
certification-report_revoked_2030-10-12
```

---

# Metadata Recommendations

Archived evidence should retain available metadata whenever practical.

Examples include:

* Original evidence identifier
* Certification record identifier
* Certification receipt identifier
* Certification report identifier
* Archive date
* Archive reason
* Original certification status
* Lifecycle state

Preservation of metadata improves future traceability.

---

# Relationship to Lifecycle States

Archived evidence may originate from any lifecycle state.

Common examples include:

| Lifecycle State | Archive Scenario                         |
| --------------- | ---------------------------------------- |
| Certified       | Certification superseded                 |
| Expired         | Certification validity period ended      |
| Revoked         | Certification withdrawn                  |
| Rejected        | Review preserved for historical purposes |
| Archived        | Final preservation state                 |

Archiving does not imply fault, failure, or invalidity.

Archiving indicates preservation.

---

# Relationship to Anchor

Future versions of the Satoshium ecosystem may integrate archived evidence with Anchor preservation systems.

Examples may include:

* Hash preservation
* Timestamp preservation
* Historical record anchoring
* Integrity verification

Archived evidence should therefore remain suitable for future preservation activities.

---

# Relationship to Chronicle

Major archival events may be recorded by Chronicle when they represent significant ecosystem milestones.

Examples include:

* Atlas certification retirement
* Major standards transitions
* Certifier version migrations

---

# Retention Philosophy

Certifier does not establish mandatory deletion schedules for archived evidence.

Retention periods should be determined according to:

* Certification requirements
* Preservation objectives
* Operational needs
* Storage considerations

Whenever practical, historically significant evidence should be preserved indefinitely.

---

# Long-Term Vision

The archived evidence directory exists to ensure that certification history remains understandable long after active certifications have changed.

Future reviewers should be able to understand:

* What evidence existed
* What certification decisions were made
* What standards were applied
* Why changes occurred

Historical transparency is a core component of trust.

Archived evidence helps preserve that transparency.

---

# Guiding Statement

> Active evidence supports current certification.
>
> Archived evidence preserves certification history.
>
> Trust is strengthened when the past remains reviewable.
