# Chronicle Schemas

## Purpose

Satoshium Chronicle Schemas define the machine-readable structures used to represent canonical Chronicle Entries and supporting Chronicle-owned records.

Schemas provide the structural language required for:

* Consistency
* Validation
* Interoperability
* Provenance
* Traceability
* Versioning
* Publication readiness
* Long-term historical preservation

The canonical historical-preservation object of Chronicle is the **Chronicle Entry**.

Chronicle schemas exist to support that object and the supporting records required to preserve its context, evidence, verification, corrections, relationships, provenance, and lineage.

Chronicle schemas should organize information without dictating historical conclusions or absorbing authority that belongs to another Satoshium Suite system.

---

## Suite Alignment

Chronicle Schemas operate within the broader Satoshium Suite architecture.

They should align with Suite-wide expectations for:

* Stable objects
* Canonical terminology
* Common record models
* Required and conditional fields
* Controlled values
* Durable identifiers and references
* Reference-based interoperability
* Provenance and traceability
* Validation-ready records
* Schema versioning and evolution
* Historical preservation of prior schema states
* Documented and repeatable procedures
* Clear institutional authority boundaries

Chronicle should not redefine or duplicate the schemas of authoritative objects owned by Certifier, Registry, Atlas, Anchor, Beacon, Attestor, Navigator, or another Suite system.

---

## Why Schemas Matter

Historical preservation becomes more reliable when records follow explicit, stable structures.

Without consistent schemas:

* Information becomes difficult to compare
* Relationships become ambiguous
* Provenance becomes harder to reconstruct
* Verification becomes inconsistent
* Validation becomes unreliable
* Cross-system references become fragile
* Corrections and version lineage become difficult to preserve
* Historical records become harder to interpret across time and technology

Schemas provide the structural foundation needed to keep Chronicle Entries and supporting records durable, reviewable, machine-readable, and interoperable.

---

## Canonical Schema Model

Chronicle uses one canonical historical-preservation object:

> Chronicle Entry

The structural model should therefore center on one common **Chronicle Base Schema**.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Base Schema
    +
Applicable Event-Type Profile
    ↓
Chronicle Entry
```

Supporting Chronicle schemas exist only where a distinct operational function requires them.

They do not create competing canonical Chronicle objects.

---

## Chronicle Base Schema

The **Chronicle Base Schema** defines the universal structure shared by production Chronicle Entries.

The Base Schema should support, at minimum, the architectural concepts necessary for:

* Entry identity
* Schema version
* Title and summary
* Event or occurrence classification
* Preservation Eligibility
* Historical Significance where applicable
* Event date
* Entry creation date
* Publication date
* Originating system
* Authoritative record references
* Historical context
* Sources
* Evidence
* Provenance
* Relationships
* Verification state
* Validation state
* Entry lifecycle state
* Publication state
* Correction lineage
* Version lineage

The final field names, identifier format, required/conditional/optional designations, and controlled values remain subject to Chronicle operational development.

Legacy examples should not be treated as canonical merely because they appeared in earlier draft schema files.

---

## Event-Type Profiles

Chronicle should use **Event-Type Profiles** to specialize the Base Schema for specific classes of preserved occurrences.

Conceptually:

```text
Chronicle Base Schema
        +
Event-Type Profile
        =
Specialized Chronicle Entry
```

An Event-Type Profile may define:

* Additional required fields
* Additional conditional fields
* Event-Type-specific controlled values
* Required authoritative references
* Relationship constraints
* Evidence expectations
* Provenance requirements
* Verification requirements
* Validation requirements

An Event-Type Profile extends the Base Schema.

It does not create a separate canonical Chronicle object.

The first anticipated operational profile is the **Certification Event-Type Profile**.

---

## Current Schema Architecture

The current Chronicle schema architecture includes:

### Chronicle Base Schema

File:

```text
chronicle-entry-schema.md
```

This file now serves as the architectural specification for the Chronicle Base Schema.

It defines the common structure for canonical Chronicle Entries and explicitly distinguishes:

* Event occurrence from Chronicle Entry
* Base Schema from Event-Type Profile
* Verification from Validation
* Event date from record-maintenance dates
* Schema version from Entry version
* Authoritative Suite references from Chronicle-owned records

### Source Record Schema

File:

```text
source-record-schema.md
```

Defines supporting Chronicle-owned structures for documenting where information originated.

The Source Record Schema distinguishes:

* Source
* Evidence
* Provenance
* Source type
* Source role
* Creator
* Publisher
* Creation date
* Publication date
* Access date
* Capture date
* Archival state
* Source limitations
* Verification
* Validation
* Version lineage

A Source Record does not become the authority for an external Suite object merely because Chronicle references it.

### Evidence Record Schema

File:

```text
evidence-record-schema.md
```

Defines supporting Chronicle-owned structures for representing evidence relevant to Chronicle Entries or claims.

Evidence Records may describe material that:

* Supports
* Challenges
* Contradicts
* Clarifies
* Corroborates
* Contextualizes
* Limits confidence

The Evidence Record Schema preserves distinctions among:

* Evidence
* Source
* Provenance
* Authoritative records
* Evidence quality
* Evidence limitations
* Integrity
* Preservation status
* Verification
* Validation

Evidence does not determine institutional authority by itself.

### Correction Record Schema

File:

```text
correction-record-schema.md
```

Defines supporting Chronicle-owned structures for documenting corrections to Chronicle's own records.

The Correction Record Schema supports:

* Issue identification
* Affected Chronicle record
* Correction classification
* Substantive vs. non-substantive scope
* Previous state
* Corrected state
* Prior-version linkage
* Resulting-version linkage
* Evidence
* Authoritative references
* Provenance
* Verification
* Validation
* Publication
* Historical correction lineage

Chronicle Correction Records do not modify authoritative objects maintained by another Suite system.

---

## Supporting Schema Categories

Additional supporting schemas may be introduced where a distinct Chronicle function requires formal structure.

Potential future categories may include:

* Verification Record Schema
* Provenance Schema
* Relationship Schema
* Version Record Schema
* Publication Record Schema
* Validation Record Schema

These should be created only when operational requirements justify separate records.

Schema proliferation should be avoided.

---

## Controlled Values

Controlled values should be governed separately from structural schema definitions where practical.

Schemas may reference approved vocabularies for concepts such as:

* Event Type
* Entry Status
* Publication State
* Verification State
* Validation State
* Relationship Type
* Evidence Type
* Evidence Relationship
* Source Type
* Source Role
* Correction Type
* Correction Scope
* Preservation Status
* Originating System

Separating vocabularies from structural schemas allows terminology to evolve under controlled governance without requiring unnecessary schema redesign.

---

## Required, Conditional, and Optional Fields

Chronicle schemas should distinguish clearly among:

### Required Fields

Fields that must be present for a record to conform to the schema.

### Conditional Fields

Fields required when a defined condition applies.

Examples may include:

* Event-Type-specific fields
* Authoritative references where an authoritative object exists
* Correction lineage for substantive corrections
* Evidence limitations when material limitations exist
* Publication timestamps when a record is published

### Optional Fields

Fields that enhance discovery, context, or usability but are not universally necessary.

Final designations should be specified in machine-readable schema definitions and validation rules.

---

## Relationships Between Schemas

Chronicle schema relationships should form a layered architecture rather than a simple chain of co-equal record types.

Conceptually:

```text
Chronicle Base Schema
        ↓
Chronicle Entry
        ├── Source Records
        ├── Evidence Records
        ├── Verification Records
        ├── Correction Records
        ├── Provenance Structures
        ├── Relationship Structures
        └── Version Structures
```

A Chronicle Entry may reference authoritative Suite objects directly while also relating to supporting Chronicle records.

A Source Record may relate to multiple Entries.

An Evidence Record may relate to multiple Entries or claims.

A Correction Record may affect one Chronicle Entry or supporting Chronicle record.

These relationships should preserve context without transferring institutional authority.

---

## Reference-Based Interoperability

Chronicle schemas should support durable references to authoritative objects maintained by other Suite systems.

Examples may include:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Discovery Metadata
* Trust Statements
* Workflow Definitions
* Atlas records

Chronicle should not copy those objects' internal schema structures into Chronicle unless a specific interoperable representation is formally required.

Reference does not transfer ownership.

Reference does not transfer lifecycle control.

Reference does not transfer institutional authority.

---

## Schema and Authority Boundaries

Chronicle schemas define Chronicle-owned objects only.

For example:

* The Chronicle Base Schema defines Chronicle Entry.
* The Correction Record Schema defines Chronicle Correction Records.
* The Evidence Record Schema defines Chronicle Evidence Records.
* The Source Record Schema defines Chronicle Source Records.

Chronicle does **not** redefine:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record
* Other authoritative Suite objects

Those objects remain governed by their originating systems.

---

## Schema, Validation, Verification, and Publication

These concepts should remain distinct.

### Schema

Defines structure.

### Validation

Determines whether a Chronicle record conforms to the applicable schema, controlled values, identifiers, relationships, provenance requirements, versioning rules, and publication prerequisites.

### Verification

Reviews the support, consistency, sources, evidence, provenance, references, relationships, and historical representation of a Chronicle record.

Verification does not necessarily determine structural conformance.

### Publication

Determines whether a valid Chronicle record is approved for public production use.

Conceptually:

```text
Schema ≠ Verification ≠ Validation ≠ Publication
```

Each function has a distinct institutional purpose.

---

## Schema Versioning

Every production Chronicle record should remain associated with the schema version that governed it.

Schema evolution should define:

* Schema identity
* Version numbers
* Backward compatibility
* Breaking changes
* Deprecation
* Migration
* Validation behavior
* Historical preservation
* Prior-version documentation

Older Chronicle records should remain interpretable under the schema version that originally governed them.

Schema updates should not silently rewrite historical structures.

---

## Record Versioning vs. Schema Versioning

Schema versioning and record versioning are separate concepts.

### Schema Version

Identifies the structural specification governing a record.

Example concept:

```text
schema_version
```

### Record Version

Identifies a preserved state or lineage of a Chronicle-owned record.

Examples may include:

```text
entry_version
source_record_version
evidence_record_version
```

A record may advance to a new version without changing its governing schema version.

A schema may advance while an older record remains preserved under its original schema.

---

## Validation Expectations

Production Chronicle records should ultimately be validated against:

* Applicable schema
* Applicable Event-Type Profile
* Identifier rules
* Required and conditional fields
* Controlled Values
* Relationship rules
* Provenance requirements
* Authoritative-reference requirements
* Versioning requirements
* Publication requirements

Validation should be machine-readable wherever practical.

A record may be historically meaningful yet fail structural validation.

A structurally valid record may also contain limited or disputed evidence.

---

## Schema Evolution Philosophy

Chronicle schemas should be extensible without becoming unstable.

Changes may include:

* New fields
* New Event-Type Profiles
* New controlled values
* Stronger validation requirements
* Expanded relationship structures
* Improved provenance requirements
* New versioning mechanisms

Whenever practical:

* Prior schema versions remain documented
* Migration paths remain visible
* Historical compatibility remains preserved
* Breaking changes are explicit
* Older records remain interpretable
* Schema lineage remains traceable

---

## Design Principles

### Canonical Object First

Schema architecture should center on Chronicle Entry.

### Minimum Necessary Structure

Supporting schemas should exist only where they perform a distinct institutional function.

### Consistency

Similar concepts should use consistent structures and terminology.

### Flexibility

Schemas should support Chronicle evolution without constant redesign.

### Transparency

Fields, relationships, versions, and authority boundaries should remain understandable and reviewable.

### Interoperability

Schemas should support durable cross-system references without duplicating external authority.

### Longevity

Schema design should favor long-term readability and durability over short-term convenience.

### Validation Readiness

Schema fields should be explicit enough to support automated validation.

### Historical Compatibility

Schema evolution should preserve the ability to interpret older Chronicle records.

---

## Machine-Readable Specifications

The Markdown files in this folder currently define the architectural schema model.

Future production implementation should include formal machine-readable schema definitions where appropriate.

Possible forms may include:

* JSON Schema
* Structured JSON definitions
* YAML schema representations
* Controlled-value catalogs
* Relationship vocabularies
* Validation rule files

The exact production format should be chosen according to Suite Standards and implementation requirements.

---

## Future Development

Future Chronicle schema development may include:

* Final Chronicle Identifier Architecture
* Formal Chronicle Base Schema
* Certification Event-Type Profile
* Additional Event-Type Profiles
* Controlled Values
* Verification Record Schema
* Provenance Schema
* Relationship Schema
* Version Record Schema
* Publication structures
* Validation rule definitions
* Automated validation
* Cryptographic integrity metadata
* Cross-system reference validation
* Public schema documentation

Future development should preserve Chronicle Entry as the canonical object and maintain clear Suite authority boundaries.

---

## Current Files

The current reconciled schema specifications include:

```text
chronicle-entry-schema.md
source-record-schema.md
evidence-record-schema.md
correction-record-schema.md
README.md
```

The exact filenames may remain stable even where the architectural role has evolved.

In particular:

```text
chronicle-entry-schema.md
```

now serves as the architectural **Chronicle Base Schema** specification.

---

## Status

**Architectural draft — not yet a frozen production schema family.**

This README has been reconciled with the revised Chronicle Schemas public page and the current Chronicle Base Schema, Source Record Schema, Evidence Record Schema, Correction Record Schema, Chronicle Records architecture, and Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The final identifier formats, controlled values, required/conditional/optional field designations, Event-Type Profiles, machine-readable schema definitions, validation rules, versioning conventions, provenance structures, relationship vocabularies, and publication requirements must be settled through the remaining Chronicle operational-development steps before the schema family becomes production authoritative.
