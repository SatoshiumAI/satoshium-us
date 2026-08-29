# Controlled Values

## Overview

**Controlled Values** define the governed vocabulary Satoshium Anchor uses in production records.

Controlled Values exist so that machine-readable and human-readable Anchor records use consistent terminology for:

- methods;
- states;
- outcomes;
- classifications;
- lifecycle conditions;
- representation types;
- governance status.

The governing principle is:

> Govern vocabulary. Avoid ambiguity. Freeze only what production proves necessary.

---

## Why Controlled Values Matter

Without Controlled Values, production records may drift into inconsistent language.

For example:

```text
verified
valid
confirmed
passed
matching
good
```

might all be used to describe similar but not identical concepts.

Controlled Values require Anchor to define what each category actually means and which terms are permitted.

---

## Core Rule

Anchor should distinguish:

```text
Category
→ what kind of thing is being described

Controlled Value
→ which governed value applies within that category
```

For example:

```text
Verification Result
→ category

match
→ possible future value
```

The category may be architecturally necessary before its final production values are known.

---

# Current Controlled Value Categories

The current post-foundational architecture identifies these likely categories:

```text
Integrity Method
Integrity State
Verification Result
Publication State
Lifecycle State
Representation Type
Method Status
Algorithm Status
Correction Type
Relationship Type
```

Not all of these are ready for production freezing.

---

# State Separation

Anchor must preserve distinct state dimensions.

```text
Integrity State
≠
Verification Result
≠
Publication State
≠
Lifecycle State
```

These concepts answer different questions.

```text
Integrity State
→ What is the current integrity condition?

Verification Result
→ What happened during a defined Verification?

Publication State
→ Is and how is the record published?

Lifecycle State
→ Where is the Integrity Reference in its institutional lifecycle?
```

These should not be collapsed into one generic `status` field.

---

# Integrity Method

**Integrity Method** describes the method used to generate or preserve integrity evidence for a Canonical Representation.

Current architectural candidates include:

```text
cryptographic_digest
digital_signature
trusted_timestamp
merkle_commitment
transparency_commitment
bitcoin_commitment
composite_integrity_method
```

The first production value is now frozen as:

```text
cryptographic_digest
```

The remaining candidate values stay unfrozen until production requires them.

---

# Why Integrity Method Is Needed

Anchor is implementation-neutral.

A single Integrity Reference may eventually use:

- a cryptographic digest only;
- a digest plus timestamp;
- a digital signature;
- a Merkle commitment;
- an external transparency commitment;
- a Bitcoin commitment;
- multiple combined methods.

The architecture therefore needs a governed way to describe the integrity mechanism without defining Anchor around one technology.

---

# Representation Type

**Representation Type** classifies the kind of Canonical Representation governed by an Integrity Reference.

Current architectural candidates include:

```text
structured_record
document
package
binary_file
canonical_json
canonical_text
published_web_representation
other_governed_representation
```

The first production value is now frozen as:

```text
canonical_json
```

This value is required by the first production candidate:

```text
SCRD-SC-CERT-2026-0001
```

whose intended Representation Boundary is the complete SCRD JSON document.

Other representation values remain provisional until later production artifacts prove their need.

---

# Verification Result

**Verification Result** records the outcome of a defined Integrity Verification process.

The category is necessary, and the completed Verification architecture now supports the first production freeze.

The first frozen value is:

```text
match
```

Definition:

```text
comparison reached
+
observed integrity material agrees with expected integrity material
```

Other candidate results remain unfrozen until a real production condition requires them:

```text
mismatch
unable_to_verify
incomplete_material
method_unavailable
```

---

# Integrity State

**Integrity State** describes the current integrity-related condition of an Integrity Reference.

It should not duplicate Verification Result.

The first production value is now frozen as:

```text
current
```

Definition:

```text
the Integrity Reference has no known integrity condition
requiring escalation under the evidence presently available
```

Other conceptual values remain unfrozen until production proves their need:

```text
attention_required
compromised
historical
```

---

# Publication State

**Publication State** describes the publication condition of the Integrity Reference.

The completed Publication architecture and first production workflow now require two initial production values:

```text
unpublished
published
```

Definitions:

```text
unpublished
→ the Anchor Version has not entered public Anchor authority

published
→ the Anchor Version has entered public Anchor authority
  following Publication Gate approval
```

Publication Gate decisions remain separate:

```text
APPROVED / NOT APPROVED
≠
Publication State
```

Additional Publication State values should be frozen only when production requires them.

---

# Lifecycle State

**Lifecycle State** describes the institutional lifecycle position of the Integrity Reference itself.

The critical distinction is:

```text
Source Lifecycle
≠
Anchor Lifecycle
```

The initial production enumeration is frozen as:

```text
draft
active
superseded
withdrawn
archived
```

These values are governed by the completed Lifecycle architecture and are already enforced by the Integrity Reference Base Schema.

---

# Method Status

Anchor may need a governed vocabulary describing whether an Integrity Method remains suitable for use.

Possible conceptual states may eventually include:

```text
approved
deprecated
historical_only
prohibited
```

These are not frozen.

Method governance must preserve the ability to interpret historical Integrity References even after a method is no longer acceptable for new production.

---

# Algorithm Status

Cryptographic algorithms may require a separate status model.

For example, a hash algorithm may become unsuitable for new use while historical records using it remain meaningful.

Possible conceptual categories may eventually include:

```text
approved_for_new_use
deprecated_for_new_use
historical_verification_only
prohibited
```

The actual vocabulary should be defined only when algorithm governance is operationalized.

---

# Correction Type

A future **Correction Type** category may describe different classes of Anchor-owned error.

Possible areas may include:

- Source reference error;
- representation error;
- Integrity Value error;
- algorithm metadata error;
- timestamp error;
- signer metadata error;
- publication metadata error.

No controlled values should be created until `/anchor/corrections/` defines the actual correction model.

---

# Relationship Type

**Relationship Type** governs machine-readable connections between Anchor records and related objects.

The first production token is now frozen as:

```text
references_source
```

For IR #1, this relationship connects the Anchor Integrity Reference to:

```text
SCRD-SC-CERT-2026-0001
```

without transferring Certifier authority to Anchor.

Additional relationship tokens remain unfrozen until production requires them.

---

# Controlled Value Governance

Every production Controlled Value should eventually have at least:

```text
Machine Token
Human Label
Definition
Category
Allowed Usage
Introduction Version
Deprecation Status
Replacement Value, if applicable
```

This allows Anchor to preserve stable machine behavior while improving human-readable explanations over time.

---

# Machine Token

A **Machine Token** is the stable serialized value used in machine-readable records.

Example:

```text
bitcoin_commitment
```

Machine tokens should be:

- stable;
- lowercase or otherwise consistently normalized;
- schema-safe;
- unambiguous;
- resistant to cosmetic renaming.

The exact serialization convention should be confirmed during Schema architecture.

---

# Human Label

A **Human Label** is the readable presentation of a Controlled Value.

Example:

```text
Machine Token:
bitcoin_commitment

Human Label:
Bitcoin Commitment
```

Human labels may improve without changing the underlying token.

---

# Adding a New Controlled Value

A new production Controlled Value should be added only when:

1. A real production condition exists.
2. Existing values cannot accurately represent it.
3. The category is correct.
4. The new value has a clear definition.
5. Governance approves its use.
6. Schema and documentation are updated.

Conceptually:

```text
Production Need
        ↓
Architecture Review
        ↓
Value Definition
        ↓
Governance Approval
        ↓
Schema / Documentation Update
        ↓
Production Use
```

---

# Changing a Controlled Value

A production token should not be silently redefined.

If meaning changes materially, Anchor should prefer:

```text
deprecate old value
        ↓
introduce replacement
        ↓
preserve historical meaning
```

rather than:

```text
reuse old token with new meaning
```

The principle is:

> Preserve historical meaning. Change vocabulary forward.

---

# Deprecation

A deprecated value may remain valid for interpreting historical records.

Deprecation should not automatically make prior Integrity References invalid.

A future Controlled Values registry may need to preserve:

```text
introduced_in
deprecated_in
replacement
historical_definition
```

The exact implementation remains unfrozen.

---

# Unknown / Other / Miscellaneous

Anchor should avoid fallback values such as:

```text
unknown
other
miscellaneous
```

unless they are proven necessary.

Generic fallback values can hide incomplete architecture or poor data quality.

If one is adopted, its meaning must be tightly governed.

---

# Null vs. Not Applicable vs. Unknown

Later Schema architecture should distinguish situations such as:

```text
field absent because not required
field intentionally not applicable
field expected but not known
field value unavailable
```

These should not be collapsed casually into a generic Controlled Value.

This distinction belongs partly to Schema architecture rather than Controlled Values alone.

---

# Controlled Values and Identifiers

Identifiers define identity.

Controlled Values define governed characteristics.

```text
Anchor Identifier
→ Which Integrity Reference?

Controlled Value
→ Which governed property or state applies?
```

Mutable state should not be embedded into the Anchor Identifier.

---

# Controlled Values and Schemas

The Integrity Reference Base Schema provides the structural fields that Controlled Values populate.

Lifecycle State is already schema-enforced.

The newly frozen minimum production values should now be reconciled into schema constraints before IR #1 is constructed:

```text
representation_type → canonical_json
method_type → cryptographic_digest
integrity_state → current
verification_result → match
publication_state → unpublished | published
relationship_type → references_source
```

Future schema changes should continue to follow production evidence rather than speculative vocabulary expansion.

---

# Controlled Values and Governance

Anchor Governance controls:

- category creation;
- value introduction;
- value revision;
- deprecation;
- replacement;
- removal from future production use.

Controlled Values should not be created informally by individual production records.

---

# Controlled Values and Versioning

A Controlled Value may evolve independently from the Version of an Integrity Reference.

For example:

```text
Integrity Reference Version 1
→ uses value valid at time of publication

Later Controlled Values revision
→ does not silently rewrite Version 1
```

Historical records should remain interpretable under the vocabulary that governed them.

---

# Minimum Necessary Vocabulary

Anchor should prefer the smallest vocabulary that accurately expresses production reality.

Too many values create ambiguity.

Too few values create loss of meaning.

The target is:

```text
minimum necessary governed vocabulary
```

not:

```text
maximum possible classification
```

---

# Current Freeze Decisions

The first production candidate has now proven the minimum vocabulary Anchor needs to freeze.

### Production-Frozen Values

```text
Lifecycle State
→ draft
→ active
→ superseded
→ withdrawn
→ archived

Representation Type
→ canonical_json

Integrity Method
→ cryptographic_digest

Integrity State
→ current

Verification Result
→ match

Publication State
→ unpublished
→ published

Relationship Type
→ references_source
```

### Still Unfrozen

```text
additional Integrity Method values
additional Representation Type values
additional Integrity State values
additional Verification Result values
additional Publication State values
additional Relationship Type values
Method Status values
Algorithm Status values
Correction Type values
machine-token serialization rules beyond current adopted tokens
Controlled Values versioning model
deprecation procedure
```

---

# Why These Values Are Frozen Now

These values were not frozen merely because they appeared plausible during design.

They are now required by the first production Integrity Reference candidate:

```text
SCRD-SC-CERT-2026-0001
```

Production has therefore supplied the evidence needed to move them from architectural candidates into governed vocabulary.

The rule remains:

> Freeze only what production proves necessary.

---

# Controlled Values Principle

> Govern vocabulary. Avoid ambiguity. Freeze only what production proves necessary.

Anchor should use Controlled Values where stable vocabulary creates durable institutional value and remain flexible where architecture is still developing.

---

## Status

**Post-Foundational Architecture · First-Production Vocabulary Reconciled**

Controlled Value categories are defined, and the minimum production vocabulary required by the first SCRD JSON Integrity Reference candidate is now frozen.

Additional values remain intentionally unfrozen until later production conditions prove they are necessary.

**Version:** 1.0-draft

**Maintained By:** Satoshium
