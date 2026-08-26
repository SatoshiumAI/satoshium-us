# Relationships

## Overview

**Relationships** define how Satoshium Anchor connects Integrity References to:

- Source Artifacts;
- Source-System Identifiers;
- prior Anchor Versions;
- Corrections;
- superseding Integrity References;
- external commitments;
- Verification artifacts;
- Publication artifacts;
- other governed records.

Anchor is inherently reference-heavy.

Those references must therefore be explicit, directional, machine-readable, and authority-preserving.

The governing principle is:

> Connect records precisely. Preserve lineage completely. Transfer no authority.

---

## Core Relationship Model

The current architecture requires relationships equivalent to:

```text
Integrity Reference
→ Source Artifact

Integrity Reference
→ prior Anchor Version

Integrity Reference
→ Correction

Integrity Reference
→ superseding Integrity Reference

Integrity Reference
→ external commitment
```

These are architectural requirements.

The final machine-readable relationship tokens remain unfrozen.

---

# Relationship vs. Authority

A relationship expresses a connection between two objects.

It does not transfer institutional authority.

For example:

```text
Integrity Reference
→ references
→ SC-CERT-2026-0001
```

does not make Anchor authoritative for:

```text
SC-CERT-2026-0001
```

Certifier remains authoritative for the Certification Package.

> Reference does not transfer authority.

---

# Primary Source Relationship

Every production Integrity Reference should preserve a direct relationship to the Source Artifact whose representation is anchored.

Conceptually:

```text
Anchor Identifier
        ↓
Integrity Reference
        ↓
Source Institution
        +
Source-System Identifier
        ↓
Authoritative Artifact
```

This relationship answers:

> Which authoritative object is this Integrity Reference about?

---

# Source Relationship Requirements

A Source relationship should eventually preserve enough information to identify:

```text
Source Institution
Source-System Identifier
Source Artifact type
canonical Source location, where applicable
Source Version, where applicable
Canonical Representation
Representation Boundary
```

The relationship must not replace the Source Artifact's own identity.

---

# Directionality

Relationships should be directional whenever direction changes meaning.

Examples:

```text
Integrity Reference
→ references Source Artifact

Later Anchor Version
→ follows prior Anchor Version

Correction
→ corrects prior Anchor state

Later Integrity Reference
→ supersedes earlier Integrity Reference
```

Direction should be explicit in machine-readable records.

---

# Reciprocal Relationships

Some relationships naturally have reciprocal forms.

Examples:

```text
supersedes
↔
superseded_by
```

```text
corrects
↔
corrected_by
```

```text
previous_version
↔
next_version
```

Later schema design should determine whether:

1. both directions are stored;
2. one direction is stored and the inverse is derived;
3. both are published for navigation while one remains canonical.

That decision remains unfrozen.

---

# Version Relationships

Where multiple Anchor Versions remain the same Integrity Reference, Version lineage should preserve order.

Conceptually:

```text
Anchor Version 1
        ↓
Anchor Version 2
        ↓
Anchor Version 3
```

Potential relationship semantics may include:

```text
previous_version
next_version
```

These tokens are candidates only.

The final Versioning architecture should determine:

- whether Versions are separate addressable artifacts;
- whether both forward and backward links are required;
- whether Version relationships are embedded or external;
- whether a new Integrity Reference is required for material changes.

---

# Correction Relationships

Corrections require preserved lineage.

Conceptually:

```text
Earlier Anchor State
        ↓
Correction
        ↓
Corrected Anchor State
```

The relationship must make it possible to reconstruct:

- what was wrong;
- what was corrected;
- which Integrity Reference was affected;
- which Version carried the error;
- which later Version or record contains the correction.

The governing principle remains:

> Correct forward. Preserve backward.

---

# Supersession Relationships

A later Integrity Reference may supersede an earlier Integrity Reference.

Conceptually:

```text
Earlier Integrity Reference
        ↓
superseded_by
        ↓
Later Integrity Reference
```

The reciprocal view is:

```text
Later Integrity Reference
        ↓
supersedes
        ↓
Earlier Integrity Reference
```

Supersession must not erase earlier identity.

Both Anchor Identifiers should remain persistent.

---

# Supersession vs. Versioning

Supersession and Versioning are not automatically the same.

Potential architecture:

```text
same Integrity Reference
→ new Anchor Version
```

versus:

```text
new Integrity Reference
→ supersedes prior Integrity Reference
```

The Versioning architecture must define the boundary.

Relationships must support both possibilities.

---

# External Commitment Relationships

Anchor may later connect an Integrity Reference to external integrity evidence.

Examples include:

- Bitcoin transaction identifiers;
- trusted timestamp identifiers;
- transparency-log entries;
- Merkle proof references;
- external signature references;
- certificate references;
- other external commitment identifiers.

Conceptually:

```text
Anchor Identifier
→ identifies Integrity Reference

External Commitment Identifier
→ identifies external integrity evidence
```

The external identifier does not become an Anchor Identifier.

---

# Bitcoin Relationships

If Bitcoin commitments are later adopted, a relationship may conceptually look like:

```text
Integrity Reference
        ↓
committed through
        ↓
Bitcoin commitment
        ↓
Bitcoin transaction identifier
```

The transaction identifier is evidence of the external commitment.

It does not identify the Integrity Reference.

Bitcoin relationship tokens remain unfrozen until Bitcoin commitment policy is adopted.

---

# Verification Relationships

Later architecture may treat Verification results as separately addressable records.

If so, Anchor may require relationships such as:

```text
Integrity Reference
→ verified_by
→ Verification Record
```

or:

```text
Verification Record
→ verifies
→ Integrity Reference Version
```

Whether Verification becomes a separately identified object remains to be decided by `/anchor/verification/`.

---

# Validation Relationships

If Validation produces separately preserved records, relationships may include:

```text
Integrity Reference
→ validated_by
→ Validation Record
```

or an equivalent model.

This remains provisional until `/anchor/validation/` is designed.

---

# Publication Relationships

Publication architecture may create relationships such as:

```text
Integrity Reference
→ published_as
→ canonical public representation
```

Potential targets may include:

- canonical HTML page;
- canonical JSON record;
- public index entry;
- archival representation.

Whether these require explicit Relationship records remains unfrozen.

---

# Many-to-One Relationships

One Source Artifact may legitimately have multiple Integrity References.

Examples may include:

```text
one Source Artifact
→ human-readable representation
→ Integrity Reference A

one Source Artifact
→ canonical JSON representation
→ Integrity Reference B
```

or:

```text
one Source Artifact
→ different governed Representation Boundaries
→ multiple Integrity References
```

The architecture must not assume one Source Artifact equals one Anchor Identifier.

---

# One-to-Many Relationships

One Integrity Reference may connect to multiple external objects.

Examples:

```text
one Integrity Reference
→ digest
→ timestamp
→ signature
→ Bitcoin commitment
```

or:

```text
one Integrity Reference
→ multiple Verification records
```

Relationship structure must support multiplicity.

---

# Relationship Multiplicity

Later schema architecture should be able to distinguish:

```text
required single relationship
optional single relationship
required multiple relationships
optional multiple relationships
ordered relationships
unordered relationships
```

Not all relationship categories will use the same cardinality.

---

# Relationship Type

**Relationship Type** is a likely Controlled Value category.

Candidate machine tokens include:

```text
references_source
previous_version
next_version
corrects
corrected_by
supersedes
superseded_by
commits_to
verified_by
published_as
```

These are not production-frozen.

The final vocabulary should be established only after:

- Provenance;
- Versioning;
- Corrections;
- Verification;
- Validation;
- Publication;

define the relationships production actually requires.

---

# Relationship Record Structure

A machine-readable relationship may eventually require fields conceptually equivalent to:

```text
relationship_type
source_identifier
target_identifier
target_system
effective_at
relationship_version
context
```

Exact schema names are not frozen.

The schema should be designed after Provenance clarifies which relationship context belongs inside an Integrity Reference versus a separate supporting record.

---

# Internal vs. External Relationships

Anchor relationships may target:

### Internal Anchor Objects

Examples:

```text
Anchor Version
Correction
superseding Integrity Reference
Verification Record
Publication Record
```

### External Suite Objects

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
Trust Statement
Workflow Definition
Atlas record
```

### External Integrity Evidence

Examples:

```text
Bitcoin transaction
timestamp service record
transparency-log entry
certificate
signature reference
```

The schema must distinguish target systems without conflating their authority.

---

# Relationship Validation

Later Validation architecture should check relationship structure.

Potential checks may include:

```text
relationship type allowed
source identifier valid
target identifier valid
direction valid
target system recognized
required relationship present
prohibited self-reference absent
duplicate relationship absent
relationship multiplicity valid
```

No Validation rule numbers are defined here.

---

# Self-Relationships

Some self-references should likely be prohibited.

For example:

```text
Integrity Reference A
→ supersedes
→ Integrity Reference A
```

would normally be invalid.

Other relationships may legitimately point between Versions of the same Integrity Reference.

The exact rules belong to later Validation and Versioning architecture.

---

# Broken or Unresolvable Targets

A relationship may remain historically valid even if a target can no longer be reached at its former location.

Anchor should distinguish:

```text
relationship invalid
target unavailable
target moved
target withdrawn
target superseded
target archived
```

A broken URL does not necessarily invalidate the historical relationship.

Maintenance should govern response behavior.

---

# Target Resolution

Where possible, relationships should prefer stable identifiers over raw URLs.

Conceptually:

```text
Identifier
→ identity

URL
→ current location
```

A canonical URL may help resolve an object.

It should not be mistaken for the object's institutional identifier.

---

# Relationship History

Material relationship changes should preserve prior state.

Examples:

- Source Artifact replacement;
- Correction;
- supersession;
- commitment migration;
- Verification record addition;
- Publication change.

The historical relationship graph should remain reconstructable.

---

# Relationship to Identifiers

Identifiers make relationships possible.

```text
Identifiers
→ define stable identity

Relationships
→ connect those identities
```

This dependency is why `/anchor/identifiers/` precedes `/anchor/relationships/`.

---

# Relationship to Controlled Values

Controlled Values provide the governed tokens used to express Relationship Type.

The relationship architecture defines meaning first.

Controlled Values later freeze only the tokens that production proves necessary.

---

# Relationship to Provenance

Relationships answer:

> What is connected to what?

Provenance answers:

> Where did this integrity material come from, and through what process was it produced?

For example:

```text
Integrity Reference
→ Source Artifact
```

is a relationship.

But:

```text
Source Artifact
→ Canonical Representation
→ digest generation
→ timestamp
→ Integrity Reference construction
```

is provenance.

The next post-foundational page should formalize that chain.

---

# Relationship to Schemas

The Integrity Reference Schema must support:

- internal Anchor relationships;
- external Suite relationships;
- external commitment relationships;
- one-to-one links;
- one-to-many links;
- ordered lineage;
- reciprocal semantics;
- target-system identification.

The schema should not assume all relationships have the same structure.

---

# Relationship to Governance

Anchor Governance should eventually control:

- Relationship Type adoption;
- Relationship Type deprecation;
- relationship direction rules;
- cardinality rules;
- target-system rules;
- invalid relationship handling;
- migration behavior.

These operational rules remain unfrozen.

---

# Minimum Necessary Relationships

Anchor should preserve only relationships that add durable institutional value.

Not every nearby concept needs an explicit relationship.

The goal is:

```text
enough relationship structure
to reconstruct authority, lineage, and integrity context
```

without:

```text
turning every record into an unrestricted graph
```

---

# Current Freeze Decisions

### Architecturally Required Relationship Categories

```text
Source
Version
Correction
Supersession
External Commitment
```

### Provisional Relationship Categories

```text
Verification
Validation
Publication
Maintenance
```

### Production Relationship Tokens Frozen

```text
None yet
```

This is intentional.

---

# Relationships Principle

> Connect records precisely. Preserve lineage completely. Transfer no authority.

Anchor Relationships should make source reference, internal lineage, and external integrity evidence explicit while preserving the independent authority of every connected system.

---

## Status

**Post-Foundational Architecture**

Relationship categories and semantics are now defined.

The following remain intentionally unfrozen:

```text
final Relationship Type tokens
relationship serialization
reciprocal storage rules
relationship record identifiers
cardinality rules
Version relationship rules
Correction relationship rules
supersession rules
Verification relationship rules
Validation relationship rules
Publication relationship rules
external commitment relationship rules
Bitcoin relationship tokens
broken-target handling
first production relationship set
```

These should be finalized progressively as Provenance, Schemas, Versioning, Corrections, Verification, Validation, Publication, and Maintenance define actual production behavior.

**Version:** 1.0-draft

**Maintained By:** Satoshium
