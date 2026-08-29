# Satoshium Anchor Integrity Reference Base Schema

## Status

**Architecture Stage:** Post-Foundational Schema Architecture  
**Schema Status:** 1.0-draft  
**Canonical Object:** Integrity Reference  
**Maintained By:** Satoshium

---

## Purpose

The **Integrity Reference Base Schema** is the first formal machine-readable structure for Satoshium Anchor's canonical object:

```text
Integrity Reference
```

It converts Anchor's conceptual architecture into a structured production object while preserving the distinction between:

```text
structure that must exist
```

and:

```text
vocabulary or policy that is not yet frozen
```

The JSON Schema companion file is:

```text
integrity-reference-base-schema.json
```

---

## Governing Principle

> Structure the record now. Freeze policy only when downstream architecture proves it necessary.

The Base Schema therefore defines:

- required object groups;
- structural relationships;
- data types;
- repeatability;
- nesting;
- URI and date-time formats;
- separation of Source authority and Anchor authority;

without prematurely freezing:

- Anchor Identifier syntax;
- most Controlled Value enumerations;
- final Verification Result values;
- final Integrity State values;
- final Publication State values;
- final Relationship Type values;
- final Integrity Method values;
- Bitcoin-specific policy;
- other method-specific or production-specific policy not yet proven necessary.

One downstream Controlled Value enumeration is now frozen and enforced:

```text
Lifecycle State
→ draft
→ active
→ superseded
→ withdrawn
→ archived
```

This freeze was established by the completed Lifecycle architecture and is now reflected in both Anchor Validation and the machine-readable Base Schema.

---

# Top-Level Structure

A conforming Integrity Reference has this conceptual structure:

```text
Integrity Reference
├── anchor_identifier
├── anchor_version
├── schema_version
├── source
├── representation
├── integrity
├── provenance
├── relationships
├── record_state
├── verification_history
├── corrections
├── publication
├── maintenance
└── notes
```

The required core is:

```text
anchor_identifier
anchor_version
source
representation
integrity
provenance
relationships
record_state
```

Optional sections may become conditionally required by later architecture.

---

# 1. Anchor Identity

## `anchor_identifier`

Identifies the Anchor-owned Integrity Reference.

```text
Anchor Identifier
→ Integrity Reference
```

The final syntax remains governed by `/anchor/identifiers/`.

This schema requires only a non-empty string.

It deliberately does not impose:

- namespace token;
- year;
- sequence width;
- prefix;
- checksum;
- URL pattern.

---

## `anchor_version`

Integer beginning at `1`.

This field identifies the governed Version of the Integrity Reference representation.

```text
Anchor Identifier
≠
Anchor Version
```

The completed Versioning architecture defines when a change remains the same Integrity Reference and when it requires a new Anchor Identifier.

---

## `schema_version`

Optional in the 1.0-draft base structure.

Records which schema Version validated the record.

Anchor Validation now requires the applicable Schema Version to be identified for a production candidate, even though `schema_version` remains structurally optional in this 1.0-draft Base Schema pending a later schema-requirement decision.

---

# 2. Source Object

The `source` object identifies the authoritative external object.

Required:

```text
source_institution
source_artifact_type
source_system_identifier
```

Optional:

```text
source_version
source_location
```

The governing distinction remains:

```text
Source-System Identifier
≠
Anchor Identifier
```

---

## `source_institution`

Institution authoritative for the Source Artifact.

Examples may include:

```text
Certifier
Registry
Chronicle
Atlas
Beacon
Attestor
Navigator
external institution
```

No production enumeration is frozen.

---

## `source_artifact_type`

Describes the type of Source Artifact.

Examples may include:

```text
Certification Package
Satoshium Registry Entry
Chronicle Entry
Trust Statement
Workflow Definition
Atlas record
```

Final Controlled Values remain unfrozen.

---

## `source_system_identifier`

Identifier assigned by the Source Institution.

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
```

Anchor preserves this value.

Anchor does not replace it.

---

# 3. Representation Object

The `representation` object defines exactly what was anchored.

Required:

```text
representation_type
representation_boundary
canonicalization
```

Optional:

```text
canonical_representation_location
media_type
encoding
```

---

## `representation_type`

Classifies the representation.

Candidate values may include:

```text
structured_record
document
package
binary_file
canonical_json
canonical_text
published_web_representation
```

No enumeration is frozen.

---

## `representation_boundary`

Defines what content is included in the integrity-preserved representation.

This is intentionally explicit because:

```text
Artifact
≠
every possible presentation of the Artifact
```

---

## `canonicalization`

Required structured object containing:

```text
method
version
parameters
```

Only `method` is currently mandatory.

This object exists so transformations affecting integrity are reproducible.

---

# 4. Integrity Object

The `integrity` object contains one or more Integrity Methods.

Required:

```text
methods
```

Optional:

```text
composite_order
```

At least one Integrity Method is required.

---

## Integrity Method Object

Each method contains a required:

```text
method_id
method_type
```

and may contain:

```text
algorithm
algorithm_version
parameters
integrity_value
generated_at
signer_reference
key_reference
verification_material
external_commitment
```

`method_id` is a record-local identifier.

It allows multiple integrity mechanisms to coexist without requiring each method to become an Anchor-owned institutional record.

---

## `method_type`

Controlled Value category:

```text
Integrity Method
```

Candidate values are not schema-enumerated yet.

This allows the schema to support future methods without pretending that the method policy is already complete.

---

## `integrity_value`

Stores the generated value where the method produces one directly.

Examples may eventually include:

- cryptographic digest;
- Merkle root;
- signature-derived value;
- other governed integrity value.

The schema does not prescribe encoding yet.

---

# 5. External Commitment

An Integrity Method may contain an `external_commitment` object.

Required if present:

```text
system
external_identifier
```

Optional:

```text
committed_at
proof_material
```

Potential systems include:

- trusted timestamp service;
- transparency log;
- future Bitcoin commitment system;
- other external commitment mechanism.

The external identifier never becomes the Anchor Identifier.

---

# 6. Provenance Object

Required provenance layers:

```text
source_provenance
representation_provenance
generation_provenance
```

Optional:

```text
anchor_record_provenance
```

These objects are deliberately structurally open in 1.0-draft.

That allows the next production design steps to determine which provenance fields must become rigidly typed.

The schema formalizes the provenance layers without pretending the final provenance event model is known.

---

# 7. Relationships

`relationships` is a required array.

It may be empty during drafting, but its existence is structurally required.

Each relationship requires:

```text
relationship_type
target_identifier
```

Optional:

```text
target_system
target_location
effective_at
context
```

No Relationship Type enumeration is frozen.

Potential later values may include:

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

---

# 8. Record State

The required `record_state` object separates three different state dimensions:

```text
integrity_state
publication_state
lifecycle_state
```

The schema preserves the architectural rule:

```text
Integrity State
≠
Publication State
≠
Lifecycle State
```

The initial `lifecycle_state` enumeration is now frozen as:

```text
draft
active
superseded
withdrawn
archived
```

`integrity_state` and `publication_state` remain unfrozen.

Verification Result remains separate and belongs to Verification history.

---

# 9. Verification History

`verification_history` is optional.

Each event requires:

```text
verified_at
verification_result
```

Optional:

```text
verification_identifier
method_id
notes
```

This is intentionally a lightweight embedded structure.

The future `/anchor/verification/` architecture may determine that Verification becomes a separately identified object.

If so, this schema can evolve without collapsing Verification identity into the Integrity Reference itself.

---

# 10. Corrections

`corrections` is an optional array.

Each Correction reference requires:

```text
correction_identifier
```

Optional:

```text
correction_type
applied_in_anchor_version
```

The schema does not yet define a Correction object.

That belongs to `/anchor/corrections/`.

---

# 11. Publication

The optional `publication` object may contain:

```text
canonical_html
canonical_json
published_at
```

This is enough to support later publication architecture without prematurely defining a Publication Gate or Publication record.

---

# 12. Maintenance

The optional `maintenance` object may contain:

```text
last_reviewed_at
next_review_due
maintenance_notes
```

These are provisional structural fields.

The future Maintenance architecture may revise this object.

---

# Additional Properties

At the top level and most governed sub-objects:

```text
additionalProperties: false
```

This prevents silent schema drift.

However, method-specific structures such as:

```text
parameters
verification_material
proof_material
provenance sub-objects
```

remain open where future method-specific extensions are expected.

This balances:

```text
institutional rigidity
```

with:

```text
implementation extensibility
```

---

# Required vs. Optional

The Base Schema intentionally requires only the structural minimum necessary to identify:

1. the Anchor record;
2. the Source Artifact;
3. the Canonical Representation;
4. the integrity-generation method;
5. the provenance chain;
6. the relationships container;
7. the record's separate state dimensions.

Later architecture may introduce conditional requirements.

Examples:

```text
if method_type requires signature
→ signer_reference may become required

if external commitment is Bitcoin
→ Bitcoin-specific proof fields may become required

if record is published
→ canonical publication location may become required

if Correction exists
→ Correction lineage may become required
```

Those conditions are not frozen in the Base Schema.

---

# Schema Philosophy

The Base Schema is intentionally not method-specific.

It should remain valid if Anchor later uses:

- SHA-family cryptographic digests;
- digital signatures;
- timestamp services;
- transparency logs;
- Merkle trees;
- Bitcoin commitments;
- composite methods;
- future integrity technologies.

The institution must outlive any single mechanism.

---

# Relationship to Identifiers

Identifiers established what Anchor identifies.

The Base Schema now creates the field where that identity lives:

```text
anchor_identifier
```

The schema does not freeze its syntax.

---

# Relationship to Controlled Values

Controlled Values established governed categories.

The Base Schema creates locations for those values:

```text
method_type
representation_type
relationship_type
integrity_state
verification_result
publication_state
lifecycle_state
correction_type
```

The schema does not enumerate most of them yet.

The first exception is:

```text
lifecycle_state
```

which now enforces the frozen initial Lifecycle State vocabulary:

```text
draft
active
superseded
withdrawn
archived
```

---

# Relationship to Relationships

Relationships established what kinds of connections Anchor must preserve.

The Base Schema creates a repeatable `relationships` array capable of connecting:

- internal Anchor records;
- Source Artifacts;
- external Suite records;
- external commitment systems.

---

# Relationship to Provenance

Provenance established the integrity-origin chain.

The Base Schema formalizes four provenance layers:

```text
source_provenance
representation_provenance
generation_provenance
anchor_record_provenance
```

The internal field structure remains intentionally extensible pending production evidence.

---

# Next Dependency: Verification

With the Base Schema established, Anchor can now define exactly how a conforming Integrity Reference is used during Verification.

Verification architecture should answer:

```text
What input is verified?
Which schema fields are consumed?
How is Canonical Representation reconstructed?
How is Integrity Method selected?
How is Verification Result recorded?
What happens on mismatch?
What happens when material is unavailable?
```

---

# Current Freeze Decisions

### Production Structure Defined

```text
Anchor identity
Source object
Representation object
Integrity methods
Provenance layers
Relationships
Record state separation
Verification history container
Correction references
Publication container
Maintenance container
```

### Production-Frozen Downstream Constraint

```text
Lifecycle State
→ draft
→ active
→ superseded
→ withdrawn
→ archived
```

The machine-readable Base Schema now enforces this enumeration.

### Still Unfrozen

```text
Anchor Identifier syntax
most Controlled Value enumerations
Relationship Type tokens
Integrity Method enumeration
Integrity Value encoding
canonicalization method enumeration
Verification Result enumeration
Integrity State enumeration
Publication State enumeration
conditional method requirements
Bitcoin-specific schema
Correction schema
method-specific policy
```

---

# Schema Principle

> Structure the record now. Freeze policy only when downstream architecture proves it necessary.

The Integrity Reference Base Schema is the first formal production-oriented expression of Anchor's canonical object.

---

## Version

**Schema Version:** 1.0-draft  
**Maintained By:** Satoshium
