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

Production has now frozen the first machine-readable Relationship Type token:

```text
references_source
```

Additional relationship tokens remain unfrozen until production proves they are necessary.

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

Every production Integrity Reference must preserve a direct relationship to the Source Artifact whose representation is anchored.

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

The Source relationship is represented through the Base Schema relationship structure:

```text
relationship_type
target_identifier
target_system
target_location
effective_at
context
```

For production IR #1, the required relationship is:

```text
relationship_type
→ references_source

target_identifier
→ SCRD-SC-CERT-2026-0001

target_system
→ Satoshium Certifier

target_location
→ https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json
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

The Versioning architecture is now defined, but these tokens remain candidates only until a real multi-Version production case proves which direction and storage model are necessary.

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

**Relationship Type** is a governed Controlled Value category.

The first production-frozen token is:

```text
references_source
```

Definition:

```text
connects an Anchor Integrity Reference
to the Source Artifact whose governed representation
the Integrity Reference preserves
```

Candidate future tokens remain:

```text
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

These remain unfrozen until production requires them.

---

# Relationship Record Structure

The Integrity Reference Base Schema now defines the machine-readable relationship structure:

```text
relationship_type
target_identifier
target_system
target_location
effective_at
context
```

The `relationships` array is required.

Production records must contain at least one:

```text
references_source
```

relationship.

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

Formal Anchor Validation now checks relationship structure and required Source linkage.

Relevant checks include:

```text
required Source relationship present
Relationship Type allowed
target identifier present
direction semantically valid
target system coherent where provided
prohibited self-reference absent
contradictory duplicate relationship absent
```

Production IR #1 must contain a valid:

```text
references_source
```

relationship to:

```text
SCRD-SC-CERT-2026-0001
```

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

The first production-frozen token is:

```text
references_source
```

Additional tokens remain unfrozen until production proves they are necessary.

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
→ Integrity Reference construction
```

is provenance.

The Provenance architecture is now defined and uses the Source relationship as one component of the larger origin and generation chain.

---

# Relationship to Schemas

The Integrity Reference Base Schema now supports:

- internal Anchor relationships;
- external Suite relationships;
- external commitment relationships;
- one-to-one links;
- one-to-many links;
- target-system identification.

The schema provides:

```text
relationships[]
relationship_type
target_identifier
target_system
target_location
effective_at
context
```

and requires at least one `references_source` relationship for production.

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

# First Production Relationship Set

The first production Integrity Reference is:

```text
ANCH-2026-0001
```

Its initial relationship set contains exactly one required relationship:

```text
relationship_type
→ references_source

target_identifier
→ SCRD-SC-CERT-2026-0001

target_system
→ Satoshium Certifier

target_location
→ https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json
```

No Version, Correction, Supersession, Verification, Publication, Maintenance, or external-commitment relationship is required for Anchor Version 1 at initial construction.

This is intentional minimum-necessary structure.

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

### Production-Frozen Relationship Token

```text
references_source
```

### First Production Relationship

```text
ANCH-2026-0001
→ references_source
→ SCRD-SC-CERT-2026-0001
```

### Still Unfrozen

```text
previous_version
next_version
corrects
corrected_by
supersedes
superseded_by
commits_to
verified_by
published_as
reciprocal storage rules
relationship record identifiers
additional cardinality rules
Bitcoin-specific relationship tokens
```

---

# Relationships Principle

> Connect records precisely. Preserve lineage completely. Transfer no authority.

Anchor Relationships should make source reference, internal lineage, and external integrity evidence explicit while preserving the independent authority of every connected system.

---

## Status

**Post-Foundational Architecture · First-Production Relationships Reconciled**

Relationship categories, the Base Schema relationship structure, formal Validation relationship checks, the first production Relationship Type token, and IR #1's initial Source relationship are now defined.

Production-frozen:

```text
Relationship Type → references_source
```

First production relationship:

```text
ANCH-2026-0001
→ references_source
→ SCRD-SC-CERT-2026-0001
```

Additional relationship tokens remain intentionally unfrozen until later production cases require them.

**Version:** 1.0-draft

**Maintained By:** Satoshium
