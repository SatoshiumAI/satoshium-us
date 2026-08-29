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

The Publication architecture now governs the public surface and requires enough provenance to support independent review without transferring Source authority.

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

Maintenance architecture governs how later provenance observations or additions are preserved without silently rewriting prior production history.

---

# Provenance Fields

The Integrity Reference Base Schema now provides structured provenance containers:

```text
source_provenance
representation_provenance
generation_provenance
anchor_record_provenance
```

Exact internal field structure remains intentionally extensible where production has not yet proven that tighter typing is necessary.

Production provenance should preserve, at minimum where applicable:

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

---

# Provenance Object Structure

The Base Schema has resolved the primary structural question by using structured provenance objects:

```text
source_provenance
representation_provenance
generation_provenance
anchor_record_provenance
```

Whether more detailed ordered provenance events are later required remains a production-driven question.

That decision should be based on actual operational complexity rather than pre-production speculation.

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

Formal Anchor Validation now confirms that required provenance is present and coherent.

Applicable checks include:

```text
Source Institution present
Source-System Identifier valid where required
Canonical Representation identified
Representation Boundary defined
transformation documented where required
Integrity Method identified
algorithm identified where required
Integrity Value present where required
required timestamps present
required signer / commitment material present where applicable
Version references coherent
```

Missing or contradictory required provenance may produce Validation failure or block progression until governed remediation is complete.

The governing Validation Rule Set is maintained separately under `/anchor/validation/`.

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

The Integrity Reference Base Schema now implements the core Provenance architecture through structured provenance containers.

Schema evolution should continue to use production evidence to determine:

- which internal provenance fields become required;
- which remain conditional;
- which become repeatable;
- whether ordered provenance events are necessary;
- which Controlled Values require machine enforcement;
- how composite integrity methods should be constrained;
- how external commitments should be represented.

---

# First Production Application — SCRD JSON

Anchor's first production candidate applies this Provenance architecture to the machine-readable Satoshium Certified Record generated by Satoshium Certifier.

```text
Source Institution
→ Satoshium Certifier

Source Artifact
→ SCRD-SC-CERT-2026-0001

Source Artifact Type
→ Satoshium Certified Record (SCRD JSON)

Source Version
→ 1.1

Source Package
→ SC-CERT-2026-0001

Source Location
→ /certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json
```

The intended Representation Boundary is:

```text
the complete SCRD JSON document
```

The following remain outside that Representation Boundary unless separately anchored:

```text
Certification Package
SCPR
SCR
SCRD HTML
Atlas records
Registry records
Chronicle records
other linked or referenced artifacts
```

The exact canonicalization or serialization method remains a downstream production decision.

Before integrity material is generated, Provenance must preserve that decision explicitly.

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

### Production Provenance Structure

```text
Base Schema provenance containers
→ defined

Internal provenance field structure
→ intentionally extensible

First-production canonicalization / serialization rule
→ not yet frozen
```

---

# Provenance Principle

> Preserve origin. Preserve process. Preserve authority boundaries.

Anchor Provenance should make the integrity-preservation chain reconstructable without turning Anchor into the authority for the Source Artifact.

---

## Status

**Post-Foundational Architecture · Pre-Production Reconciled**

The provenance chain, provenance layers, Base Schema containers, Validation relationship, and first-production application are now defined.

The following remain intentionally unfrozen or production-driven:

```text
internal provenance field requirements
ordered provenance event model
first-production canonicalization / serialization rule
transformation-specific requirements
timestamp-specific requirements
signer / key-specific requirements
external commitment provenance structure
Bitcoin provenance structure
method-specific provenance constraints
first production Integrity Reference provenance instance
```

These should now be tightened only where the first production Integrity Reference demonstrates that additional structure is necessary.

**Version:** 1.0-draft

**Maintained By:** Satoshium
