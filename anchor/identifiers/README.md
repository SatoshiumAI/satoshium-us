# Identifiers

## Overview

**Identifier Architecture** defines how Satoshium Anchor gives stable identity to its canonical object:

```text
Integrity Reference
```

The fundamental rule is:

```text
Anchor Identifier
→ identifies the Integrity Reference

Source-System Identifier
→ identifies the Source Artifact
```

Therefore:

```text
Source-System Identifier
≠
Anchor Identifier
```

These identifiers represent different institutional objects and must remain independently meaningful.

---

## Purpose

Identifiers are foundational to post-foundational Anchor architecture.

Stable identity is required before Anchor can reliably define:

- relationships;
- provenance;
- schemas;
- Verification records;
- Validation records;
- Publication records;
- Lifecycle;
- Versioning;
- Corrections;
- Maintenance;
- external commitments;
- production indexes.

The Identifier Architecture must therefore be established before those later systems are frozen.

---

## Anchor Identifier

An **Anchor Identifier** is the stable identifier assigned by Satoshium Anchor to an Anchor-owned Integrity Reference.

It identifies:

```text
Integrity Reference
```

It does not identify:

```text
Source Institution
Source Artifact
Source-System Identifier
Source Artifact Version
Trust Statement meaning
Certification determination
Chronicle historical meaning
external commitment transaction
```

Those may be referenced by the Integrity Reference but retain separate identity and authority.

---

## Source-System Identifier

A **Source-System Identifier** is the identifier assigned by the Source Institution to the authoritative artifact referenced by Anchor.

Examples include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
```

These identifiers remain governed by their Source Institutions.

Conceptually:

```text
SC-CERT-2026-0001
→ Certifier-owned Certification Package

SREG-2026-0001
→ Registry-owned Satoshium Registry Entry

CHR-2026-0001
→ Chronicle-owned Chronicle Entry
```

If Anchor later preserves Integrity References for these artifacts, Anchor must preserve the Source-System Identifier as source metadata.

Anchor must not replace it.

---

## Cross-System Identity Model

```text
Source Institution
        ↓
Source-System Identifier
        ↓
Authoritative Artifact
        ↓
Canonical Representation
        ↓
Integrity Reference
        ↓
Anchor Identifier
```

Each layer answers a different question:

```text
Source Institution
→ Who governs the external artifact?

Source-System Identifier
→ Which external artifact is referenced?

Canonical Representation
→ Which exact representation is covered?

Integrity Reference
→ Which Anchor integrity record preserves the context?

Anchor Identifier
→ Which stable Anchor record is this?
```

---

## Identifier Authority

Anchor governs:

```text
Anchor Identifier
```

Anchor does not govern identifiers owned by:

```text
Certifier
Registry
Chronicle
Atlas
Beacon
Attestor
Navigator
external Source Institutions
```

> Reference does not transfer authority.

---

## Identifier Stability

Once assigned to a production Integrity Reference, an Anchor Identifier should remain stable.

Ordinary later events should not silently change its identity.

Potential later events include:

- Verification;
- Reverification;
- Publication;
- Maintenance;
- Source link repair;
- metadata enrichment;
- Correction;
- Anchor Version creation;
- Source Artifact supersession.

Whether a material change remains the same Integrity Reference or requires a new one will be governed later by Versioning and Corrections architecture.

---

## Identifier Uniqueness

Every production Anchor Identifier must uniquely identify one Anchor-owned Integrity Reference within the Anchor namespace.

The architecture should prevent:

```text
one Anchor Identifier
→ multiple unrelated Integrity References
```

and accidental duplicate Integrity References.

Duplicate-prevention rules may later be addressed through Validation and production procedure.

---

## Identifier Immutability

An Anchor Identifier should not be reassigned to a different Integrity Reference after production assignment.

An identifier may remain resolvable even if the Integrity Reference is later:

- superseded;
- corrected;
- withdrawn from publication;
- archived;
- deprecated;
- migrated.

Historical identity should remain preserved.

---

## Identifier Persistence

Anchor Identifiers should remain usable across:

- publication;
- archival;
- storage migration;
- software replacement;
- domain changes;
- schema Versions;
- algorithm changes;
- external commitment changes;
- long-term preservation.

The identifier architecture should therefore avoid unnecessary dependency on implementation details.

---

## Identifier vs. Version

An Anchor Identifier identifies the Integrity Reference.

An Anchor Version identifies a governed Version of that Integrity Reference.

```text
Anchor Identifier
≠
Anchor Version
```

A future Versioning model may allow:

```text
one Anchor Identifier
→ multiple preserved Anchor Versions
```

where those Versions remain the same underlying Integrity Reference.

A materially different integrity subject may instead require:

```text
new Integrity Reference
→ new Anchor Identifier
```

The exact boundary remains intentionally unfrozen until Versioning architecture is developed.

---

## Source Artifact Version vs. Anchor Version

```text
Source-System Identifier
≠
Source Artifact Version
≠
Anchor Identifier
≠
Anchor Version
```

A Source Artifact may change without changing an existing Anchor Identifier.

The existing Integrity Reference continues to represent the Source representation it originally covered.

A later Source representation may require:

- Reverification;
- a new Anchor Version;
- a new Integrity Reference;
- no Anchor action;

depending on later production rules.

---

## Identifier Format

The final production syntax for Anchor Identifiers is intentionally **not frozen** on this page.

The architecture should define what the identifier means before defining how it is spelled.

The eventual format should be evaluated against:

```text
uniqueness
readability
namespace clarity
stable parsing
long-term durability
human recognition
machine interoperability
Version independence
Correction safety
publication stability
```

The syntax should be tested against the Integrity Reference Schema and the first production Integrity Reference before adoption.

---

## Why the Format Remains Unfrozen

A premature identifier format could accidentally encode assumptions that later architecture disproves.

Examples include:

- assuming one Source Artifact can have only one Integrity Reference;
- encoding mutable state;
- encoding Version incorrectly;
- tying identifiers to one cryptographic method;
- tying identifiers to Bitcoin before Bitcoin policy exists;
- tying identifiers to publication sequence before Publication architecture exists;
- forcing one-to-one relationships that later become one-to-many.

> Define identifier meaning first. Freeze identifier syntax only after production dependencies are understood.

---

## What the Identifier Should Not Encode Prematurely

The Anchor Identifier should avoid embedding mutable or interpretive values unless later architecture demonstrates that they are necessary.

```text
Integrity State
Verification Result
Publication State
Lifecycle State
Source Artifact status
Certification outcome
trust judgment
reputation state
mutable Version metadata
algorithm
hash value
Bitcoin transaction identifier
```

These values may change while the identity of the Integrity Reference remains stable.

---

## Identifier Assignment

A later Production Procedure must define exactly when an Anchor Identifier is permanently assigned.

Possible boundaries include:

```text
Integrity Reference construction
successful Validation
Publication approval
first canonical persistence
```

No assignment point is frozen yet.

This decision should be made after Validation, Publication, Lifecycle, and production procedure have been defined.

---

## Draft vs. Production Identity

Anchor may need temporary development identifiers or internal working references before production assignment.

Such temporary values must not be confused with permanent Anchor Identifiers.

Potential architecture:

```text
Working Reference
        ↓
Validation / Review
        ↓
Production Anchor Identifier
```

Whether a formal Working Reference is needed should be determined by real production workflow rather than assumed now.

---

## Corrections and Identifiers

A Correction does not automatically require a new Anchor Identifier.

Later Corrections and Versioning architecture must determine whether an error is corrected through:

```text
same Integrity Reference
→ new Anchor Version
```

or:

```text
new Integrity Reference
→ new Anchor Identifier
```

> Correct forward. Preserve backward.

---

## Supersession and Identifiers

A later Integrity Reference may supersede an earlier Integrity Reference.

If so, both identifiers should remain preserved.

```text
Earlier Anchor Identifier
        ↓
superseded_by
        ↓
Later Anchor Identifier
```

Supersession must not erase earlier identity.

The exact relationship vocabulary belongs to the later Relationships architecture.

---

## External Commitment Identifiers

Anchor may later reference external commitment identifiers such as:

- Bitcoin transaction identifiers;
- transparency-log entries;
- timestamp-service identifiers;
- Merkle proof identifiers;
- external signature references.

These are not Anchor Identifiers.

```text
Anchor Identifier
→ identifies Integrity Reference

External Commitment Identifier
→ identifies external commitment evidence
```

Both may appear in the same Integrity Reference.

---

## Identifier Relationships

Stable identifiers will support later relationships such as:

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

Integrity Reference
→ Verification record

Integrity Reference
→ Publication record
```

This dependency is why Identifiers precede Relationships and Provenance in the developmental arc.

---

## Human-Readable vs. Machine-Stable Identity

The final identifier should ideally serve both humans and machines.

Human-readable features may improve:

- inspection;
- debugging;
- publication;
- cross-Suite recognition.

Machine-stable features may improve:

- parsing;
- validation;
- API use;
- relationship resolution;
- archival durability.

The final design should balance both without overloading the identifier with semantics.

---

## Namespace

Anchor requires its own identifier namespace because the Integrity Reference is an Anchor-owned canonical object.

The final namespace token is intentionally unfrozen.

A production identifier should make it possible to determine that:

```text
this identifier belongs to Anchor
```

without confusing it with:

```text
SC-CERT
SREG
CHR
```

or another Suite namespace.

---

## Example Without Freezing Syntax

```text
SC-CERT-2026-0001
        ↓
Certification Package
        ↓
defined Canonical Representation
        ↓
Integrity Reference
        ↓
[future Anchor Identifier]
```

Likewise:

```text
SREG-2026-0001
        ↓
Satoshium Registry Entry
        ↓
defined Canonical Representation
        ↓
Integrity Reference
        ↓
[future Anchor Identifier]
```

and:

```text
CHR-2026-0001
        ↓
Chronicle Entry
        ↓
defined Canonical Representation
        ↓
Integrity Reference
        ↓
[future Anchor Identifier]
```

This demonstrates architecture without prematurely declaring syntax.

---

## Identifier Requirements

A future production Anchor Identifier should be:

- **Unique**
- **Stable**
- **Persistent**
- **Namespace-Clear**
- **Version-Independent**
- **Technology-Neutral**
- **Authority-Preserving**
- **Machine-Compatible**
- **Human-Usable**

---

## Relationship to Controlled Values

Identifiers define identity.

Controlled Values define governed vocabulary.

```text
Anchor Identifier
→ Which Integrity Reference?

Integrity State
→ What is its integrity state?

Publication State
→ What is its publication state?

Lifecycle State
→ Where is it in its lifecycle?
```

This separation allows state to change while identity remains stable.

---

## Relationship to Schemas

The future Integrity Reference Schema will likely require conceptual fields equivalent to:

```text
Anchor Identifier
Source Institution
Source-System Identifier
```

Exact machine-readable field names are not frozen here.

Identifier Architecture establishes their conceptual roles before schema syntax is defined.

---

## Relationship to Publication

Publication may expose the Anchor Identifier through:

- human-readable pages;
- canonical URLs;
- JSON records;
- indexes;
- cross-Suite references.

The final URL architecture should be designed after identifier syntax is settled.

A canonical URL may contain an Anchor Identifier without the URL itself becoming the identifier.

---

## Relationship to Governance

Anchor Governance controls the Anchor identifier namespace.

Governance should eventually define:

- identifier assignment authority;
- identifier syntax adoption;
- identifier deprecation policy;
- namespace changes;
- collision handling;
- malformed identifier handling;
- migration behavior.

The operational rules remain intentionally unfrozen.

---

## Identifier Architecture Principle

> Identify the Anchor record. Preserve the Source identifier. Never confuse the two.

Anchor Identifiers should provide stable identity for Integrity References while preserving the independent identity, Versioning, lifecycle, and authority of every Source Artifact.

---

## Status

**Post-Foundational Architecture**

Identifier meaning is now defined.

The following remain intentionally unfrozen:

```text
Anchor namespace token
production identifier syntax
year / sequence structure
sequence width
assignment point
draft identifier behavior
collision procedure
canonical URL pattern
identifier Controlled Values, if any
same Identifier vs. new Identifier rules under Versioning
first production Anchor Identifier
```

These should be finalized only after subsequent architecture—especially Controlled Values, Relationships, Schemas, Validation, Versioning, and Publication—provides enough production evidence.

**Version:** 1.0-draft

**Maintained By:** Satoshium
