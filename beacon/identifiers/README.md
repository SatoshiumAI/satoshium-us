# Satoshium Beacon — Beacon Identifier Standard

## Overview

The **Beacon Identifier Standard** establishes the canonical identifier convention for Beacon-owned **Discovery Signals**.

This is the fourth component of:

```text
Beacon Phase II — Production Architecture
```

The canonical Beacon Discovery Signal identifier is:

```text
BEAC-YYYY-NNNN
```

The first production Discovery Signal will therefore use:

```text
BEAC-2026-0001
```

This gives Beacon a stable institutional identifier comparable to the existing production-proven Suite objects:

```text
Certifier → SC-CERT-2026-0001
Registry → SREG-2026-0001
Chronicle → CHR-2026-0001
Anchor → ANCH-2026-0001
Beacon → BEAC-2026-0001
```

---

## Purpose

A production Discovery Signal must be independently identifiable across:

```text
public pages
schemas
indexes
relationships
canonical references
version history
cross-Suite references
future machine-readable interfaces
```

The identifier provides persistent identity even when other characteristics of the signal change.

A Discovery Signal may later become:

```text
Active
Superseded
Resolved
Withdrawn
```

or move between:

```text
Unpublished
Published
```

without changing its canonical identifier.

---

## Canonical Decision

The Beacon institutional prefix is:

```text
BEAC
```

The canonical format is:

```text
BEAC-YYYY-NNNN
```

where:

```text
BEAC
→ Satoshium Beacon institutional prefix

YYYY
→ four-digit calendar year of canonical Discovery Signal creation

NNNN
→ four-digit zero-padded sequence within that creation year
```

Example:

```text
BEAC-2026-0001
```

---

## 1. Institutional Prefix — BEAC

The prefix:

```text
BEAC
```

identifies the object as institutionally owned by Satoshium Beacon.

The prefix was selected to preserve institutional clarity.

It is:

```text
short
human-readable
recognizable
distinct from other Suite identifiers
stable across Signal Types
```

The identifier should communicate:

```text
who owns the object
```

rather than attempt to encode every characteristic of the object.

Therefore:

```text
BEAC
→ institutional identity

Discovery Signal
→ canonical object type

Signal Type
→ discovery classification
```

These remain separate concerns.

---

## Why BEAC?

Beacon owns Discovery Signals, but the institutional identifier should remain centered on the institution rather than a particular Signal Type.

Using:

```text
BEAC
```

avoids embedding classifications such as:

```text
CERT
TRUST
INTEGRITY
HISTORICAL
```

into permanent identity.

This preserves flexibility if Beacon's governed discovery architecture evolves while maintaining stable institutional identity.

The identifier says:

```text
This object belongs to Beacon.
```

The Entry Model says:

```text
This object is a Discovery Signal.
```

The Signal Type says:

```text
This is the kind of discovery the signal represents.
```

---

## 2. Year Component — YYYY

The year component is the four-digit calendar year in which the canonical Discovery Signal is created.

Example:

```text
2026
```

The year is determined at canonical object creation.

It does not change if the signal is later:

```text
updated
published
superseded
resolved
withdrawn
```

Therefore:

```text
BEAC-2026-0001
```

remains a 2026 identifier even if the object continues to exist or change institutional standing in later years.

The year is part of identity.

It is not a statement of current status.

---

## 3. Sequence Component — NNNN

The sequence component is:

```text
NNNN
```

a four-digit, zero-padded sequential number assigned within the creation year.

Examples:

```text
0001
0002
0003
...
```

The first canonical Discovery Signal created in 2026 is:

```text
BEAC-2026-0001
```

The second is:

```text
BEAC-2026-0002
```

The first canonical Discovery Signal created in 2027 is:

```text
BEAC-2027-0001
```

The annual sequence therefore begins again with:

```text
0001
```

for each new creation year.

---

## Canonical Identifier Grammar

Human-readable grammar:

```text
BEAC-[four-digit year]-[four-digit sequence]
```

Conceptual validation pattern:

```regex
^BEAC-[0-9]{4}-[0-9]{4}$
```

Formal machine-readable enforcement remains subject to:

```text
/beacon/schemas/
/beacon/validation/
```

---

## Assignment Point

The Discovery Signal Lifecycle established the distinction between:

```text
Identified
→ pre-object condition

Created
→ canonical object creation event

Draft
→ initial lifecycle state
```

The permanent Beacon identifier is assigned when the canonical Discovery Signal is:

```text
Created
```

and enters:

```text
Draft
```

Therefore:

```text
Candidate Discovery Identified
→ permanent identifier not required

Discovery Signal Created
→ BEAC identifier assigned

Draft
→ canonical Beacon object exists
```

This prevents candidate observations that never become institutional objects from consuming canonical Beacon identifiers unnecessarily.

---

## Identifier Permanence

Once assigned, a Beacon identifier is permanent.

It does not change because of:

```text
review
publication
update
version change
lifecycle transition
supersession
resolution
withdrawal
```

The identifier remains associated with the historical object.

Therefore:

```text
Identity persists
even when institutional standing changes.
```

---

## Non-Reuse

A Beacon identifier must never be reassigned to another Discovery Signal.

This remains true if the original object becomes:

```text
Superseded
Resolved
Withdrawn
```

A withdrawn identifier remains consumed.

A superseded identifier remains consumed.

A resolved identifier remains consumed.

Sequence gaps should not be repaired by reusing identifiers.

The governing principle is:

> **Gaps are preferable to identity reuse.**

---

## Sequence Governance

Each canonical Discovery Signal receives one sequence number at creation.

Expected sequence principles are:

```text
unique within the creation year
monotonically increasing
zero-padded to four digits
never reused
never reassigned
```

The implementation mechanism for sequence assignment remains pending.

Later production architecture may determine whether assignment is managed through:

```text
a controlled production process
a Beacon identifier ledger
a machine-readable registry
another governed issuance mechanism
```

The identifier meaning is established here.

The issuance mechanism is not yet frozen.

---

## Signal Type Is Not Encoded

Signal Type must remain separate from the permanent identifier.

Correct:

```text
Identifier → BEAC-2026-0001
Signal Type → Certification
```

Not:

```text
BEAC-CERT-2026-0001
```

The latter improperly embeds a classification into permanent identity.

Signal classifications may evolve independently of identifier syntax.

---

## Lifecycle State Is Not Encoded

Lifecycle State must remain separate from the identifier.

Correct:

```text
Identifier → BEAC-2026-0001
Lifecycle State → Active
```

Not:

```text
BEAC-ACTIVE-2026-0001
```

Lifecycle state changes.

Identity does not.

---

## Publication State Is Not Encoded

Publication State also remains separate.

Correct:

```text
Identifier → BEAC-2026-0001
Publication State → Published
```

Publication status may change according to later Publication architecture without changing the object's identity.

---

## Version Is Not Encoded

Version information must not become part of the canonical identifier.

Correct:

```text
Canonical Identifier → BEAC-2026-0001
Version → separate governed field
```

Not:

```text
BEAC-2026-0001-v2
```

as a replacement for the canonical identifier.

The later:

```text
/beacon/versioning/
```

architecture will determine how versions are represented and referenced.

The canonical object identity remains stable.

---

## Source Identity Remains Separate

A Beacon Discovery Signal may reference another Suite canonical object.

Example:

```text
Beacon Discovery Signal
→ BEAC-2026-0001

Referenced Anchor Integrity Reference
→ ANCH-2026-0001
```

These identifiers represent separate institution-owned objects.

Beacon preserves the relationship between them.

It does not merge them.

Conceptually:

```text
BEAC-2026-0001
        ↓ references
ANCH-2026-0001
```

not:

```text
BEAC-ANCH-2026-0001
```

---

## Suite Identifier Context

Beacon now joins the production identifier architecture established across the Suite:

```text
Certifier
→ SC-CERT-2026-0001

Registry
→ SREG-2026-0001

Chronicle
→ CHR-2026-0001

Anchor
→ ANCH-2026-0001

Beacon
→ BEAC-2026-0001
```

These identifiers identify different institution-owned objects.

They do not imply that one canonical object moves from institution to institution.

For example:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
BEAC-2026-0001
```

may participate in governed relationships while remaining distinct objects.

---

## Valid Examples

```text
BEAC-2026-0001
BEAC-2026-0002
BEAC-2026-0125
BEAC-2027-0001
```

Each follows:

```text
BEAC-YYYY-NNNN
```

---

## Invalid Examples

### Short Year

```text
BEAC-26-0001
```

Invalid because the year must contain four digits.

### Non-Padded Sequence

```text
BEAC-2026-1
```

Invalid because the sequence must contain four zero-padded digits.

### Embedded Signal Type

```text
BEAC-CERT-2026-0001
```

Invalid because Signal Type is not part of canonical identity.

### Embedded Version

```text
BEAC-2026-0001-v2
```

Invalid as a canonical identifier because Version remains a separate governed field.

### Embedded Lifecycle State

```text
BEAC-ACTIVE-2026-0001
```

Invalid because lifecycle state is not part of canonical identity.

---

## Human-Readable Identity

The identifier is intended to remain usable by both people and machines.

Potential uses include:

```text
public citation
canonical public pages
cross-Suite references
Discovery Signal indexes
schemas
validation
relationship mappings
version history
provenance records
future APIs
machine discovery
```

The identifier should therefore remain concise, stable, and predictable.

---

## Canonical Public Path

The eventual public representation of a production Discovery Signal should be addressable by its identifier.

Conceptually:

```text
/beacon/records/BEAC-2026-0001/
```

This establishes a predictable relationship between:

```text
canonical identity
```

and:

```text
canonical public representation
```

The exact public record architecture will be determined during:

```text
/beacon/records/
```

and the later Individual Discovery Signal phase.

---

## Relationship to the Entry Model

The Entry Model established:

```text
Identity
```

as the first structural component of a Discovery Signal.

The Identifier Standard now defines the canonical institutional identifier within that identity:

```text
identity:
  identifier → BEAC-YYYY-NNNN
  object type → Discovery Signal
  institution → Beacon
```

Exact schema field names remain subject to later Schema architecture.

---

## Relationship to Lifecycle

The Lifecycle architecture establishes:

```text
Identified
→ pre-object

Created
→ event

Draft
→ first canonical lifecycle state
```

The Identifier Standard establishes:

```text
Created
→ canonical identifier assigned
```

Therefore:

```text
Identified
        ↓
Created
        ↓
BEAC identifier assigned
        ↓
Draft
```

Once assigned, the identifier survives every later lifecycle transition.

---

## Relationship to Versioning

Identifier and Version answer different questions.

```text
Identifier
→ Which canonical Beacon object is this?

Version
→ Which governed state of that object is being represented?
```

The canonical identifier remains:

```text
BEAC-2026-0001
```

while Version is preserved separately.

The exact version model remains pending.

---

## Relationship to Schemas

The next Phase II architecture will define Beacon Schemas.

Those schemas should eventually enforce:

```text
identifier presence
identifier data type
BEAC prefix
four-digit year
four-digit sequence
permitted identifier pattern
```

The Identifier Standard defines the meaning.

The Schema architecture will define the machine-readable representation.

---

## Authority Boundary

A Beacon identifier establishes the identity of a Beacon-owned Discovery Signal only.

For example:

```text
BEAC-2026-0001
```

does not rename, replace, absorb, or transfer ownership of:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

or any future Attestor canonical object.

A Beacon identifier identifies Beacon's object.

Referenced identifiers continue to identify their own institution-owned objects.

Therefore:

> **Reference does not transfer authority.**

---

## What Is Now Frozen

The following architectural decisions are established:

```text
Institutional Prefix → BEAC

Canonical Pattern → BEAC-YYYY-NNNN

Year → four-digit canonical creation year

Sequence → four-digit zero-padded annual sequence

Assignment → canonical Discovery Signal creation

Permanence → identifier does not change

Reuse → prohibited

Signal Type in identifier → prohibited

Lifecycle State in identifier → prohibited

Publication State in identifier → prohibited

Version in identifier → prohibited
```

These define the canonical meaning of Beacon Discovery Signal identity.

---

## What Remains Unfrozen

Downstream implementation details remain pending:

```text
machine-readable schema enforcement
sequence-assignment mechanism
collision-prevention implementation
identifier issuance ledger or registry
public routing implementation
API behavior
version-reference syntax
production tooling
```

These should be determined through their respective Phase II architecture and production work.

---

## Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Discovery Signal Entry Model → Defined
Discovery Signal Types → Defined
Discovery Signal Lifecycle → Defined
Beacon Identifier Standard → Defined

Canonical Prefix → BEAC
Canonical Pattern → BEAC-YYYY-NNNN
First Production Identifier → BEAC-2026-0001

Schema Enforcement → Pending
Identifier Issuance Mechanism → Pending
Production Proof → Pending
First Production Discovery Signal → Not yet created
Operational → No
```

---

## Phase II Progress

```text
1. Discovery Signal Entry Model
   → COMPLETE

2. Discovery Signal Types
   → COMPLETE

3. Discovery Signal Lifecycle
   → COMPLETE

4. Beacon Identifier Standard
   → COMPLETE

5. Beacon Schemas
   → NEXT

6. Validation

7. Discovery Provenance

8. Authority & Reference Model

9. Relationship Model

10. Versioning & Supersession

11. Publication Model

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

## Governing Principles

The Beacon Identifier Standard follows these principles:

```text
Identify the institution-owned object.

Keep identity stable.

Keep classification separate from identity.

Keep lifecycle separate from identity.

Keep publication state separate from identity.

Keep version separate from identity.

Never reuse an issued identifier.

Preserve relationships between distinct canonical identifiers.

Prefer gaps over identity reuse.
```

The identifier principle is:

> **Identity should remain stable even when everything around it changes.**

The Suite-wide authority principle remains:

> **Reference does not transfer authority.**

---

## Next Phase II Step

The next production-architecture page is:

```text
/beacon/schemas/
```

Its purpose is to define the public machine-readable schema architecture for Beacon Discovery Signals and related Beacon-owned structures.

---

## Last Updated

September 5, 2026
