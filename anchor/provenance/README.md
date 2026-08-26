# Provenance

## Overview

**Provenance** defines the chain of origin behind a Satoshium Anchor Integrity Reference.

The current provenance chain is:

```text
Source Institution
        ↓
Authoritative Artifact
        ↓
Canonical Representation
        ↓
Integrity-Generation Process
        ↓
Integrity Reference
```

Provenance explains:

- where the Source Artifact came from;
- which representation was used;
- whether transformations occurred;
- how integrity material was generated;
- which method and algorithm applied;
- which system, signer, or process participated;
- how the result became an Anchor Integrity Reference.

The governing principle is:

> Preserve origin. Preserve process. Preserve authority boundaries.

---

## Provenance vs. Source Authority

Provenance records origin and transformation.

It does not transfer or recreate institutional authority.

```text
Provenance
≠
Source Authority
```

For example:

```text
SC-CERT-2026-0001
→ Certifier-owned Certification Package
```

may be part of Anchor provenance.

Certifier still governs the Certification Package.

Anchor governs only its Integrity Reference.

> Reference does not transfer authority.

---

## Provenance vs. Relationships

Relationships answer:

> What is connected to what?

Provenance answers:

> Where did this integrity material come from, and through what chain was it produced?

For example:

```text
Integrity Reference
→ Source Artifact
```

is a relationship.

But:

```text
Source Institution
→ Authoritative Artifact
→ Canonical Representation
→ Integrity Method
→ Integrity Value
→ Integrity Reference
```

is provenance.

The relationship graph may support provenance without being identical to it.

---

# Source Provenance

**Source Provenance** identifies the authoritative origin of the artifact.

Potential elements include:

```text
Source Institution
Source-System Identifier
Source Artifact type
Source Version
canonical Source location
retrieval context
```

The exact required fields remain unfrozen.

The goal is to preserve enough source context to answer:

```text
Where did this artifact come from?
Which institution governed it?
Which Source record was used?
Which Version applied?
```

---

# Source-System Identifier

Where available, the Source-System Identifier should be preserved as part of provenance.

Examples include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
```

The Source-System Identifier remains external authority metadata.

It must not be replaced by the Anchor Identifier.

---

# Authoritative Artifact

The provenance chain should identify the specific Authoritative Artifact that became the subject of integrity preservation.

Potential artifact types may include:

- Certification Package;
- Satoshium Registry Entry;
- Chronicle Entry;
- Trust Statement;
- Atlas record;
- Discovery artifact;
- Workflow Definition;
- external institutional record.

The Source Institution retains authority over the artifact.

---

# Representation Provenance

**Representation Provenance** records how Anchor moved from the Authoritative Artifact to the exact Canonical Representation used for integrity generation.

Conceptually:

```text
Authoritative Artifact
        ↓
representation selection
        ↓
canonicalization / serialization
        ↓
Representation Boundary
        ↓
Canonical Representation
```

This provenance is necessary because integrity applies to a representation, not an abstract idea of the artifact.

---

# Canonical Representation Provenance

Anchor should preserve enough information to explain:

- which representation was selected;
- which serialization applied;
- which encoding applied;
- whether transformation occurred;
- which Representation Boundary applied;
- whether excluded content existed;
- whether the representation was reproducible.

The exact schema structure remains unfrozen.

---

# Transformation Provenance

Some Source Artifacts may need transformation before integrity material can be generated.

Potential transformations include:

```text
JSON canonicalization
deterministic serialization
whitespace normalization
encoding normalization
package manifest generation
defined file ordering
dynamic-content exclusion
```

Transformations must not occur silently.

Where transformation materially affects the Integrity Value, it should be documented.

---

# Transformation Rule

The governing rule is:

> If transformation changes what is hashed, signed, timestamped, or committed, the transformation belongs in provenance.

This ensures later reviewers can reproduce the same Canonical Representation.

---

# Integrity-Generation Provenance

**Integrity-Generation Provenance** records how integrity material was created.

Conceptually:

```text
Canonical Representation
        ↓
Integrity Method
        ↓
algorithm / method parameters
        ↓
Integrity Value
        ↓
timestamp / signature / commitment material
```

Potential provenance elements include:

- Integrity Method;
- algorithm;
- algorithm Version where relevant;
- parameters;
- producing system;
- generation timestamp;
- signer reference;
- signing-key reference;
- timestamp service;
- external commitment reference.

---

# Producing System

A **Producing System** may be recorded where materially relevant.

Examples may include:

- Anchor production workflow;
- hash-generation service;
- signature service;
- timestamp service;
- Bitcoin commitment process;
- automated build system.

The producing system supports reproducibility and accountability.

It does not become the Source authority.

---

# Process Attribution

Provenance may preserve attribution for:

```text
producing system
institutional role
signer
signing key
reviewer
automated process
```

Attribution should follow the minimum-necessary-data principle.

Anchor should not collect unnecessary personal information merely because a human participated.

---

# Temporal Provenance

Time may be part of provenance where sequence matters.

Potential timestamps include:

```text
source_retrieved_at
representation_generated_at
integrity_generated_at
signed_at
timestamped_at
externally_committed_at
anchor_created_at
published_at
```

These field names are conceptual only.

Not every timestamp should become mandatory.

The production schema should require only times that materially support later reconstruction.

---

# Temporal Order

Where multiple integrity steps occur, order may matter.

Example:

```text
Canonical Representation
        ↓
digest
        ↓
signature
        ↓
trusted timestamp
        ↓
Bitcoin commitment
```

If order affects Verification, Provenance must preserve that order.

---

# External Commitment Provenance

If Anchor later uses external commitments, provenance should preserve:

```text
Integrity Value
        ↓
commitment preparation
        ↓
external commitment
        ↓
external identifier / proof material
```

Potential external systems may include:

- Bitcoin;
- timestamp services;
- transparency logs;
- Merkle commitment systems;
- signature infrastructure;
- future public commitment systems.

These remain external evidence systems.

---

# Bitcoin Provenance

If Bitcoin is adopted, Provenance may need to preserve:

- commitment input;
- Merkle root, where applicable;
- transaction identifier;
- output / commitment location;
- confirmation context;
- commitment timestamp;
- proof material;
- Verification instructions.

No Bitcoin provenance schema is frozen yet.

The later Bitcoin commitment policy should define it.

---

# Composite Provenance

An Integrity Reference may use multiple integrity mechanisms.

Example:

```text
Canonical Representation
        ↓
cryptographic digest
        +
digital signature
        +
trusted timestamp
        +
Bitcoin commitment
```

Composite provenance must preserve:

- which mechanisms were used;
- their dependency order;
- which output fed the next step;
- which evidence belongs to each mechanism.

---

# Provenance Completeness

Provenance is complete when a later reviewer can understand and reconstruct the integrity-preservation path sufficiently to verify the record.

Complete provenance does not mean:

```text
record every operational event
record every system log
record every human interaction
```

The target is:

```text
minimum necessary reconstruction context
```

---

# Provenance and Reproducibility

Useful provenance should support reproducibility.

Conceptually:

```text
same governed Source representation
+
same canonicalization rules
+
same Integrity Method
=
reproducible integrity material
```

Where exact reproduction is impossible because a mechanism is stateful or time-dependent, Provenance should preserve enough historical evidence to validate the original operation.

---

# Provenance and Verification

Verification depends on Provenance.

```text
Provenance
→ explains how integrity material was produced

Verification
→ tests whether that integrity material can still be reproduced or validated
```

Missing provenance may make otherwise valid cryptographic material impossible to interpret.

---

# Provenance and Versioning

Provenance must preserve the applicable Versions of different objects.

These may include:

```text
Source Artifact Version
Canonicalization Rule Version
Anchor Version
Schema Version
Algorithm Version
Integrity Method Version
```

These Versions must remain distinct.

---

# Provenance and Corrections

A Correction may be required if Anchor recorded provenance incorrectly.

Examples include:

- wrong Source-System Identifier;
- wrong Source Version;
- wrong canonicalization method;
- wrong Representation Boundary;
- wrong algorithm;
- wrong timestamp;
- wrong signer reference;
- wrong external commitment reference.

A Correction should preserve the prior provenance state.

> Correct forward. Preserve backward.

---

# Provenance and Publication

Publication should not erase or flatten provenance.

A public Integrity Reference should expose enough provenance for independent review while respecting privacy and minimum-necessary-data principles.

The exact publication surface remains to be defined.

---

# Provenance and Maintenance

Maintenance may add later provenance information without rewriting the original record.

Examples may include:

- new Verification event;
- algorithm deprecation context;
- Source migration;
- external commitment migration;
- repaired resolution location;
- later archival location.

Later Maintenance architecture should define how additions are recorded.

---

# Provenance Fields

The future Integrity Reference Schema may need structured provenance fields or a provenance object.

Conceptual fields may include:

```text
source_institution
source_system_identifier
source_artifact_type
source_version
source_location
representation_type
canonicalization_method
representation_boundary
producing_system
integrity_method
algorithm
generated_at
signer_reference
key_reference
timestamp_reference
external_commitment_reference
```

Exact names and nesting remain unfrozen.

---

# Provenance Object vs. Flat Fields

Schema architecture should determine whether provenance is represented as:

```text
flat fields
```

or:

```text
structured provenance object
```

or:

```text
multiple provenance events
```

The decision should be based on actual production complexity.

---

# Provenance Events

Anchor may eventually need ordered provenance events for composite or multi-step integrity processes.

Conceptual example:

```text
Event 1
→ Canonical Representation created

Event 2
→ digest generated

Event 3
→ signature produced

Event 4
→ timestamp obtained

Event 5
→ external commitment created

Event 6
→ Integrity Reference published
```

Whether this event model is necessary remains unfrozen.

---

# Provenance Validation

Later Validation architecture should confirm that required provenance is present and coherent.

Potential checks include:

```text
Source Institution present
Source-System Identifier valid where required
Canonical Representation identified
Representation Boundary defined
transformation documented where required
Integrity Method identified
algorithm identified where required
Integrity Value present
required timestamps present
required signer / commitment material present
Version references coherent
```

No formal Validation rule numbers are defined here.

---

# Provenance Integrity

Provenance itself may become part of the Anchor record's integrity-preserved representation.

That means later changes to provenance metadata may require:

- a new Anchor Version;
- a Correction;
- a Maintenance event;
- another governed action.

The correct behavior will be defined later.

---

# Provenance Privacy

Provenance should not become an excuse to collect excessive identity or operational data.

Prefer:

- institutional role over unnecessary personal identity;
- key reference over copied private information;
- process identifier over full internal logs;
- canonical reference over duplicated external data.

The governing principle is:

> Preserve enough provenance for accountability and reproducibility, but no more than necessary.

---

# Relationship to Identifiers

Identifiers establish stable identity for the objects participating in provenance.

```text
Identifiers
→ who / what object?

Provenance
→ where did it come from and how was it produced?
```

---

# Relationship to Controlled Values

Controlled Values may eventually govern:

- Integrity Method;
- Representation Type;
- Algorithm Status;
- Method Status;
- Provenance Event Type, if needed.

No Provenance-specific Controlled Value category is frozen yet.

---

# Relationship to Relationships

Relationships provide the graph edges used by Provenance.

Provenance gives those relationships process and origin context.

Conceptually:

```text
Relationship
→ Integrity Reference references Source Artifact

Provenance
→ explains how Source Artifact became the anchored representation
```

---

# Relationship to Schemas

The next major architectural step is the Integrity Reference Schema.

Schema design should use Provenance to determine:

- which fields are required;
- which are conditional;
- which are repeatable;
- which are nested;
- which Controlled Values are needed;
- how composite integrity methods are represented;
- how external commitments are represented.

---

# Minimum Necessary Provenance

Anchor should preserve:

```text
enough provenance
to reconstruct origin, representation, integrity generation, and lineage
```

without attempting to preserve:

```text
every internal action
every transient system state
every operational log
```

The minimum-necessary-structure principle remains active.

---

# Current Freeze Decisions

### Architecturally Required Provenance Layers

```text
Source Provenance
Representation Provenance
Integrity-Generation Provenance
Anchor Record Provenance
```

### Likely Conditional Provenance

```text
Transformation Provenance
Signer / Key Provenance
Timestamp Provenance
External Commitment Provenance
Composite Method Provenance
```

### Production Provenance Schema Frozen

```text
No
```

This is intentional.

---

# Provenance Principle

> Preserve origin. Preserve process. Preserve authority boundaries.

Anchor Provenance should make the integrity-preservation chain reconstructable without turning Anchor into the authority for the Source Artifact.

---

## Status

**Post-Foundational Architecture**

The provenance chain and provenance layers are now defined.

The following remain intentionally unfrozen:

```text
final provenance field names
provenance object structure
flat fields vs. event model
required vs. conditional provenance
canonicalization provenance requirements
transformation provenance rules
timestamp provenance requirements
signer / key provenance requirements
external commitment provenance structure
Bitcoin provenance structure
provenance Validation rules
provenance Versioning behavior
first production provenance record
```

These should be finalized through the next architecture—especially Schemas, Verification, Validation, Versioning, Publication, and the first production Integrity Reference.

**Version:** 1.0-draft

**Maintained By:** Satoshium
