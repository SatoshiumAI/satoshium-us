# Discovery Signal Schema

## Purpose

The **Discovery Signal Schema** defines the human-readable production structure of a Beacon-owned **Discovery Signal**.

A Discovery Signal is Beacon's canonical institutional object.

Canonical identity follows:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

This schema implements the architecture established through:

```text
Discovery Signal Entry Model
Discovery Signal Types
Discovery Signal Lifecycle
Beacon Identifier Standard
```

Formal machine-readable validation rules will be established separately through Beacon Validation.

---

## Canonical Object

```text
Institution → Beacon
Object Type → Discovery Signal
Canonical Responsibility → Discovery Signal / Metadata
Identifier → BEAC-YYYY-NNNN
```

A Discovery Signal records a governed discovery.

It does not absorb the authority of the information or canonical objects it references.

> **Reference does not transfer authority.**

---

# Canonical Structure

A Discovery Signal follows this architecture:

```text
Identity
→ Subject
→ Signal Type
→ Source
→ Provenance
→ Canonical References
→ Discovery Metadata
→ Timestamps
→ Version
→ Status
→ Relationships
```

---

# 1. Identity

Identity establishes the canonical Beacon object.

Expected fields include:

```text
identifier
object_type
title
institution
```

### Identifier

Canonical format:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

### Object Type

Canonical value:

```text
Discovery Signal
```

### Institution

Canonical owner:

```text
Beacon
```

### Title

Human-readable title describing the discovery.

Example:

```text
Texas Digital Asset Policy Change Observed
```

---

# 2. Subject

Subject identifies what the Discovery Signal concerns.

Expected subject information may include:

```text
name
description
subject_type
subject_identifier
jurisdiction
domain
```

The Subject does not establish authority.

A subject may be:

```text
jurisdiction
record
event
entity
artifact
system
relationship
external information
```

---

# 3. Signal Type

Signal Type identifies the primary discovery classification.

The initial governed architectural vocabulary is:

```text
Information
Jurisdiction
Certification
Registry
Historical
Integrity
Trust
Relationship
```

The Signal Type must describe the discovery itself.

It must not be inferred automatically from the referenced source object's type.

Example:

```text
signal_type: Integrity
```

does not convert the Discovery Signal into an Anchor Integrity Reference.

---

# 4. Source

Source preserves where the discovered information originated.

Expected source information may include:

```text
source_kind
source_name
source_institution
source_identifier
source_object_type
source_location
```

Source may represent:

```text
Suite institution
external source
public record
research source
government source
other attributable source
```

If the source already has a canonical identifier, Beacon should preserve that identifier rather than manufacture a replacement identity.

---

# 5. Provenance

Provenance explains how the discovery became known to Beacon.

Expected provenance information may include:

```text
observed_source
observation_method
observation_context
supporting_reference
discovery_actor
discovery_process
```

Exact production requirements will be established through:

```text
/beacon/provenance/
```

and:

```text
/beacon/validation/
```

Provenance is distinct from source identity.

```text
Source
→ where the information comes from

Provenance
→ how Beacon encountered and preserved the discovery
```

---

# 6. Canonical References

Canonical References preserve explicit links to governed objects owned by other institutions.

Potential references include:

```text
Atlas Authoritative Intelligence
Certifier Certification Package
Registry SREG
Chronicle Entry
Anchor Integrity Reference
Attestor Trust Statement
Navigator workflow reference
```

Each reference should preserve enough information to identify:

```text
source institution
canonical identifier
object type
relationship to the Discovery Signal
```

The referenced object remains owned by the originating institution.

---

# 7. Discovery Metadata

Discovery Metadata preserves contextual information useful for discovery, filtering, review, and interpretation.

Potential metadata may include:

```text
jurisdiction
domain
topic
classification
observed source status
search context
workflow context
keywords
tags
controlled values
relationship context
```

Discovery Metadata supports the signal.

It does not replace the primary Signal Type.

---

# 8. Timestamps

A Discovery Signal should preserve relevant time information.

Potential timestamps include:

```text
observed_at
created_at
updated_at
published_at
last_observed_at
```

The exact semantics and required combinations will be governed by Lifecycle, Publication, Versioning, and Validation.

### Creation Time

`created_at` records canonical Beacon object creation.

The year in:

```text
BEAC-YYYY-NNNN
```

must correspond to the canonical creation year.

---

# 9. Version

Version information is separate from the canonical identifier.

Potential fields include:

```text
version
previous_version
supersedes
superseded_by
```

The exact version model remains pending:

```text
/beacon/versioning/
```

The canonical identifier itself must not become:

```text
BEAC-2026-0001-v2
```

The identifier remains:

```text
BEAC-2026-0001
```

---

# 10. Status

Status contains two separate dimensions.

## Lifecycle State

Architectural values:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

## Publication State

Architectural values:

```text
Unpublished
Published
```

These dimensions must not be collapsed.

Example:

```text
lifecycle_state: Active
publication_state: Published
```

---

# 11. Relationships

Relationships preserve meaningful governed connections between the Discovery Signal and other objects or signals.

Potential relationship classes include:

```text
source relationship
canonical-object relationship
related-signal relationship
version relationship
supersession relationship
workflow relationship
other governed relationship
```

Relationship vocabulary remains subject to:

```text
/beacon/relationships/
```

Relationships should be attributable and reviewable.

---

# Conceptual YAML Representation

The following is an architectural example.

It is not yet a final machine-enforced production schema.

```yaml
identifier: BEAC-2026-0001
object_type: Discovery Signal
institution: Beacon
title: Texas Digital Asset Policy Change Observed

subject:
  name: Texas
  subject_type: Jurisdiction
  jurisdiction: Texas, United States

signal_type: Jurisdiction

source:
  source_kind: Suite Institution
  source_name: Satoshium Atlas
  source_institution: Atlas
  source_identifier: TEXAS-JIE-001
  source_object_type: Authoritative Intelligence
  source_location: /atlas/jurisdictions/united-states/texas/

provenance:
  observation_method: Manual Review
  observation_context: Phase II production example
  supporting_reference: TEXAS-JIE-001

canonical_references:
  - institution: Atlas
    identifier: TEXAS-JIE-001
    object_type: Authoritative Intelligence

discovery_metadata:
  jurisdiction: Texas
  topic: Digital Assets

timestamps:
  observed_at: 2026-09-05T00:00:00Z
  created_at: 2026-09-05T00:00:00Z

version:
  version: 1

status:
  lifecycle_state: Draft
  publication_state: Unpublished

relationships: []
```

The example demonstrates structure only.

It does not establish the first production Discovery Signal.

---

# Required Architectural Components

The following are expected to be core production concerns:

```text
Identity
Subject
Signal Type
Source
Provenance
Discovery Metadata
Timestamps
Version
Status
```

Canonical References and Relationships may be conditional when no such relationship exists.

Exact machine-required fields will be determined through Validation.

---

# Identifier Rules

Canonical Discovery Signal identifier:

```text
BEAC-YYYY-NNNN
```

Rules:

```text
BEAC prefix required
four-digit creation year required
four-digit zero-padded annual sequence required
identifier assigned at canonical object creation
identifier permanent
identifier never reused
Signal Type not encoded
Lifecycle State not encoded
Publication State not encoded
Version not encoded
```

Conceptual pattern:

```regex
^BEAC-[0-9]{4}-[0-9]{4}$
```

---

# Signal Type Rules

Architectural values:

```text
Information
Jurisdiction
Certification
Registry
Historical
Integrity
Trust
Relationship
```

A type classifies the discovery.

It does not establish:

```text
truth
source authority
certification
registration
historical significance
integrity verification
trust
publication eligibility
```

---

# Status Rules

Lifecycle State:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

Publication State:

```text
Unpublished
Published
```

Lifecycle and publication must remain separately interpretable.

---

# Source Authority

A Discovery Signal may reference a canonical Suite object.

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

Beacon preserves those identities.

Beacon does not replace them with:

```text
BEAC
```

identifiers.

Example:

```text
BEAC-2026-0001
→ references
ANCH-2026-0001
```

Both objects remain institutionally distinct.

---

# Confidence and Relevance

Legacy Beacon schema drafts included generalized:

```text
confidence
relevance
```

fields.

These are not currently established as canonical Discovery Signal semantics.

They should not be included as required production fields unless later Beacon architecture explicitly defines:

```text
meaning
authority
scale
methodology
validation
```

for them.

Trust-related meaning belongs to Attestor when a Trust Statement is required.

---

# Relationship to Source Reference Schema

The Source block may be represented using the reusable architecture documented in:

```text
source-reference-schema.md
```

That structure preserves source attribution without converting the source into a Beacon-owned canonical object.

---

# Relationship to Validation

This document defines the human-readable schema architecture.

Validation will determine:

```text
required fields
permitted field types
identifier conformance
Signal Type conformance
status conformance
reference requirements
provenance requirements
relationship conformance
publication prerequisites
```

---

# Status

```text
Schema Role → Canonical Production Schema
Canonical Object → Discovery Signal
Canonical Identifier → BEAC-YYYY-NNNN
Architecture → Defined
Machine-Readable Enforcement → Pending
Validation → Pending
Production Proof → Pending
```

---

## Last Updated

September 5, 2026
