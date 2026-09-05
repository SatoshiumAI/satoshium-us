# Satoshium Beacon — Schemas

## Overview

The **Beacon Schemas** directory defines the public, human-readable schema architecture for machine-readable structures recognized and published by Satoshium Beacon.

Beacon is the Satoshium Suite institution for:

```text
Discovery & Signals
```

Its canonical production object is:

```text
Discovery Signal
```

with the canonical identifier:

```text
BEAC-YYYY-NNNN
```

The schema layer translates Beacon's institutional architecture into predictable, interoperable, validation-ready structures.

Schemas define structure.

They do not independently establish:

```text
truth
certification
registration
historical authority
integrity verification
trust
source ownership
publication eligibility
```

The Suite-wide governing principle remains:

> **Reference does not transfer authority.**

---

## Purpose

Beacon schemas exist to provide stable structures for:

```text
Discovery Signals
source attribution
discovery provenance
canonical-object references
Discovery Metadata
timestamps
status
version information
relationships
optional discovery outputs
optional query history
```

The schema architecture follows the institutional architecture already established during Beacon Phase II.

The dependency path is:

```text
Entry Model
→ Signal Types
→ Lifecycle
→ Identifier Standard
→ Schemas
→ Validation
```

---

# Canonical Schema Architecture

## Canonical Production Schema

The canonical Beacon production schema is:

```text
discovery-signal-schema.md
```

It represents the Beacon-owned canonical object:

```text
Discovery Signal
```

Conceptually:

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

The first production object will use:

```text
BEAC-2026-0001
```

---

## Supporting Schemas

Beacon may also use supporting structures that preserve discovery context without creating competing canonical institutional objects.

Current supporting schemas are:

```text
source-reference-schema.md
discovery-result-schema.md
query-log-schema.md
```

These structures do not become co-equal canonical Beacon objects merely because Beacon represents them.

---

## Legacy Schema

The previous:

```text
beacon-record-schema.md
```

predated the Phase II canonical object model.

It introduced a generic Beacon Record using:

```text
BEC-YYYY-NNNNNN
```

That model is now deprecated as a canonical production schema.

Beacon's canonical object is the Discovery Signal.

The legacy file is retained only to document the architectural transition and prevent accidental reuse of the old object model.

---

## Legacy Signal Record Schema

The former:

```text
signal-record-schema.md
```

used:

```text
SIG-YYYY-NNNNNN
```

and an older signal vocabulary.

It is now retained as a compatibility and migration note.

The canonical replacement is:

```text
discovery-signal-schema.md
```

---

# Current Directory

```text
/beacon/schemas/
├── README.md
├── discovery-signal-schema.md
├── signal-record-schema.md
├── source-reference-schema.md
├── discovery-result-schema.md
├── query-log-schema.md
└── beacon-record-schema.md
```

---

# Schema Roles

## discovery-signal-schema.md

**Role:** Canonical production schema.

Defines the human-readable structure of Beacon-owned Discovery Signals.

Canonical identifier:

```text
BEAC-YYYY-NNNN
```

---

## source-reference-schema.md

**Role:** Reusable supporting structure.

Defines how Beacon represents an attributable source or canonical source reference.

A Source Reference does not replace the source institution's own identifier or schema.

---

## discovery-result-schema.md

**Role:** Optional noncanonical discovery-output structure.

Defines a result returned through discovery activity.

A Discovery Result may reference:

```text
a Discovery Signal
a Suite canonical object
an external source
another governed reference
```

A Discovery Result is not automatically a Discovery Signal.

---

## query-log-schema.md

**Role:** Optional operational history structure.

Defines information associated with a discovery request or query activity when Beacon chooses to preserve that history.

It does not redefine Navigator's ownership of workflow definition or orchestration.

---

## signal-record-schema.md

**Role:** Deprecated compatibility document.

The older Signal Record architecture is replaced by:

```text
discovery-signal-schema.md
```

---

## beacon-record-schema.md

**Role:** Deprecated legacy document.

The former generic Beacon Record is no longer a canonical Beacon production object.

---

# Canonical Controlled Architecture

## Discovery Signal Types

The initial architectural Signal Type vocabulary is:

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

These describe the primary discovery meaning of a Beacon Discovery Signal.

They do not inherit the authority of the source object.

---

## Lifecycle States

Beacon Discovery Signals use the following architectural lifecycle states:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

---

## Publication States

Publication remains a separate dimension:

```text
Unpublished
Published
```

---

## Identifier Standard

Canonical Discovery Signal identity is:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

The identifier is assigned when the canonical Discovery Signal is created and enters Draft.

It remains permanent.

---

# Authority Boundaries

Beacon may reference canonical objects from other Suite institutions.

Examples include:

```text
Atlas → Authoritative Intelligence
Certifier → Certification Package
Registry → SREG
Chronicle → Chronicle Entry
Anchor → Integrity Reference
Attestor → Trust Statement
Navigator → Workflow Definition / Orchestration
```

Beacon may represent those references.

Beacon does not redefine their canonical schemas.

Conceptually:

```text
BEAC-2026-0001
        ↓ references
ANCH-2026-0001
```

The two identifiers remain separate institution-owned objects.

> **Reference does not transfer authority.**

---

# Schema vs. Validation

Schema answers:

```text
What structure should this object have?
```

Validation answers:

```text
Does this particular object conform to the required rules?
```

Therefore:

```text
Schema → structure
Validation → conformance
```

Formal enforcement belongs to:

```text
/beacon/validation/
```

---

# Schema vs. Methodology

Schema does not determine how Beacon decides that a Discovery Signal should exist.

That belongs to Beacon Discovery Methodology.

```text
Schema → representation
Methodology → process
```

---

# Machine-Readable Implementation Posture

This directory currently defines the public human-readable schema architecture.

The following remain intentionally unfrozen until later implementation and Validation work:

```text
exact JSON property names
JSON Schema dialect
required vs. optional machine constraints
schema URIs
schema version identifiers
machine enum spelling
$ref structure
public JSON Schema filenames
API behavior
```

The machine-readable implementation must preserve the institutional meaning established here.

---

# Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Entry Model → Defined
Signal Types → Defined
Lifecycle → Defined
Identifier Standard → Defined
Schema Architecture → Defined

Canonical Production Schema → discovery-signal-schema.md
Machine-Readable Enforcement → Pending
Validation Architecture → Next
Production Proof → Pending
Operational → No
```

---

## Last Updated

September 5, 2026
