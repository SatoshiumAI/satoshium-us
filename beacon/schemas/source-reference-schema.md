# Source Reference Schema

## Purpose

The **Source Reference Schema** defines the supporting structure Beacon uses to represent an attributable information source referenced by a Discovery Signal or other permitted Beacon discovery structure.

A Source Reference exists to preserve:

```text
origin
identity
attribution
location
context
traceability
```

It does not create a new canonical Beacon-owned version of the source.

---

## Schema Role

```text
Role → Reusable Supporting Structure
Canonical Beacon Object → No
Beacon Identifier Required → No
```

A Source Reference supports a Beacon Discovery Signal.

It is not itself the canonical Beacon production object.

---

## Core Principle

Discovery without attribution creates uncertainty.

Beacon should preserve enough source information for a reviewer to determine:

```text
where the information originated
who or what institution owns it
what canonical identifier exists
where it can be reviewed
how it relates to the Discovery Signal
```

> **Reference does not transfer authority.**

---

# Source Categories

A Beacon source may be:

```text
Suite Institution
External Source
Public Record
Government Source
Research Source
Publication
Dataset
Other Attributable Source
```

These are source categories, not assertions of trust.

---

# Source Structure

Expected source-reference information may include:

```text
source_kind
source_name
source_institution
source_identifier
source_object_type
source_author
source_location
publication_date
last_updated
availability
topics
jurisdiction
metadata
```

Exact required fields remain subject to Validation.

---

## Source Kind

Describes the broad origin class.

Examples:

```text
Suite Institution
External Source
Government Source
Research Source
Public Record
```

---

## Source Name

Human-readable source name.

Example:

```text
Satoshium Atlas
```

or:

```text
Texas Legislature
```

---

## Source Institution

When the source is owned by a Satoshium Suite institution, preserve the institution explicitly.

Possible values include:

```text
Atlas
Certifier
Registry
Chronicle
Anchor
Attestor
Navigator
```

Beacon itself may also be a source for Beacon-owned objects when appropriate.

External sources should not be labeled as Suite institutions.

---

## Source Identifier

Preserve the source's own canonical identifier when one exists.

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

For external sources, this may be:

```text
record identifier
publication identifier
document number
dataset identifier
other source-native identity
```

Beacon should not replace a source-native identifier with a fabricated Beacon source identifier.

---

## Source Object Type

Preserves what the source object is.

Examples:

```text
Authoritative Intelligence
Certification Package
SREG
Chronicle Entry
Integrity Reference
Trust Statement
Workflow Definition
Public Record
Research Publication
```

Source Object Type must remain distinct from Beacon Signal Type.

---

## Source Author

When relevant and known, preserve the author, organization, agency, system, or responsible institution.

This field should be factual and attributable.

---

## Source Location

Preserve a stable location when available.

Examples:

```text
canonical URL
repository path
record page
document reference
public dataset location
```

A location helps retrieval.

It does not establish authority by itself.

---

## Publication Date

When known, preserve the source publication or creation date.

---

## Last Updated

When known, preserve the source's own most recent modification date.

This is source metadata.

It must not be confused with the Beacon Discovery Signal's `updated_at` timestamp.

---

## Availability

Potential descriptive values may include:

```text
Available
Restricted
Unavailable
Archived at Source
```

These values describe source accessibility.

They are not Beacon lifecycle states.

Exact controlled values remain unfrozen.

---

## Topics and Jurisdiction

Optional source context may include:

```text
topics
jurisdiction
domain
language
format
```

These fields support discovery and review.

---

# Canonical Suite Source Examples

## Certifier

```yaml
source_kind: Suite Institution
source_name: Satoshium Certifier
source_institution: Certifier
source_identifier: SC-CERT-2026-0001
source_object_type: Certification Package
```

## Registry

```yaml
source_kind: Suite Institution
source_name: Satoshium Registry
source_institution: Registry
source_identifier: SREG-2026-0001
source_object_type: SREG
```

## Chronicle

```yaml
source_kind: Suite Institution
source_name: Satoshium Chronicle
source_institution: Chronicle
source_identifier: CHR-2026-0001
source_object_type: Chronicle Entry
```

## Anchor

```yaml
source_kind: Suite Institution
source_name: Satoshium Anchor
source_institution: Anchor
source_identifier: ANCH-2026-0001
source_object_type: Integrity Reference
```

These are separate institution-owned objects.

Beacon may reference them without changing their identity.

---

# Conceptual External Source Example

```yaml
source_kind: Government Source
source_name: Example Government Agency
source_institution: null
source_identifier: DOC-2026-1042
source_object_type: Public Record
source_location: https://example.gov/records/DOC-2026-1042
publication_date: 2026-09-01
availability: Available
topics:
  - Digital Assets
```

This example demonstrates structure only.

---

# What This Schema Does Not Establish

A Source Reference does not independently establish:

```text
truth
verification
certification
trustworthiness
endorsement
integrity
source authority beyond what the source actually possesses
```

Beacon documents the source and its relationship to discovery.

---

# Verification Status

The previous Source Reference Schema contained a generalized:

```text
Verification Status
```

field.

That field is removed from the core architecture.

Reason:

```text
verification semantics require institutional definition
```

A generic Beacon `Verified` value could improperly imply Certifier, Anchor, or other authority.

If a source has an authoritative verification state, Beacon should preserve that state as attributed source metadata or reference the institution-owned canonical object responsible for it.

---

# Source Status

The previous schema also contained a Beacon-managed:

```text
Source Status
```

with values such as Active, Archived, Superseded, and Deprecated.

That concept is not retained as a core Beacon lifecycle field.

Beacon does not own the lifecycle of an external or institution-owned source.

Beacon may preserve:

```text
observed source status
availability
source-native status
```

with clear attribution.

---

# Relationship to Discovery Signal Schema

A Discovery Signal should preserve a primary source reference.

Conceptually:

```yaml
source:
  source_kind: Suite Institution
  source_name: Satoshium Anchor
  source_institution: Anchor
  source_identifier: ANCH-2026-0001
  source_object_type: Integrity Reference
```

Additional supporting sources may be preserved through relationships or supporting-reference structures if required.

---

# Relationship to Provenance

Source and Provenance are distinct.

```text
Source
→ Where did the information originate?

Provenance
→ How did Beacon encounter, observe, and preserve the discovery?
```

The later Discovery Provenance architecture will define provenance requirements.

---

# Status

```text
Schema Role → Supporting Structure
Canonical Object → No
Architecture → Revised for Phase II
Machine Validation → Pending
```

---

## Last Updated

September 5, 2026
