# Satoshium Suite Reconciliation — Interoperability Review Candidates

**Date:** September 29, 2026  
**Phase:** IV-B — Adversarial Consistency Review  
**Purpose:** Identify matters that belong to the upcoming Interoperability Review rather than Suite Reconciliation  
**Status:** COMPLETE — APPROVED

---

## Governing Boundary

Suite Reconciliation determines:

- institutional roles;
- canonical responsibilities;
- authority boundaries;
- object ownership;
- terminology;
- relationship semantics;
- Suite architecture;
- conceptual sequence; and
- distinctions among institutions.

The upcoming Interoperability Review should instead examine:

- detailed cross-institution technical interoperability;
- interfaces;
- implementation behavior;
- handoffs;
- compatibility; and
- exchange mechanics.

The architectural questions are now substantially settled. The remaining interoperability questions concern **how independently governed institutions exchange and consume governed information without losing meaning, provenance, version context, state, or authority**.

---

## Interoperability Review Candidates

### IR-001 — Cross-Institution Reference Contract

Determine the minimum machine-usable context that must accompany a cross-institution reference.

Candidate context already established in Attestor includes:

```text
Identifier
Source
Provenance
Type
Status
Scope
Relationship
Authority
```

with relevant:

```text
Version Identity
State
Limitations
Source-Specific Context
```

The Interoperability Review should determine whether a common Suite-level reference envelope or equivalent compatibility rule is needed.

**Why this belongs to Interoperability Review:**  
The semantic rule is already settled. The remaining question is technical exchange structure.

---

### IR-002 — Machine Serialization & Schema Compatibility

Review how the eight institutions' machine-readable representations interoperate.

Questions include:

```text
Which fields are shared?
Which fields remain institution-specific?
How are identifiers represented?
How are authority and provenance represented?
How are relationships serialized?
How are lifecycle and publication states exchanged?
How are unknown or unsupported fields handled?
```

Exact machine serialization has deliberately remained implementation work in portions of the Suite architecture.

**Why this belongs to Interoperability Review:**  
Canonical object ownership is settled; representation compatibility is not a Suite Reconciliation question.

---

### IR-003 — Stable Identifier & Reference Resolution

Review how one institution resolves another institution's canonical object or public representation.

Test:

```text
Canonical identifier
→ public representation

Version-specific identifier / reference
→ correct version

Superseded object
→ preserved historical resolution

Moved public path
→ durable reference behavior
```

Also test whether matching numeric suffixes across institutional identifier families can ever be mistaken for technical linkage.

**Why this belongs to Interoperability Review:**  
Identity semantics are settled; resolution mechanics are implementation behavior.

---

### IR-004 — Source-State & Version Change Propagation

Review what happens when an upstream object changes after a downstream institution referenced or consumed it.

Examples:

```text
Certification Package changes
→ Registry / Beacon / Attestor review behavior?

Source object superseded
→ downstream reference behavior?

Source lifecycle changes
→ discovery / attestation / historical context behavior?

Version changes
→ whether downstream object remains valid for its original evaluated state?
```

The architecture already establishes:

```text
Source State at Evaluation ≠ Later Source State
```

and a material source-state change may trigger review.

The Interoperability Review should determine how such changes are detected, communicated, and represented across systems.

---

### IR-005 — Navigator Workflow Handoffs

Review technical handoffs between Navigator and participating institutions.

Questions include:

```text
What does a Workflow Definition pass to an institution?

What does the institution return?

How are institutional results represented without becoming Navigator-owned outcomes?

How are failures, incomplete operations, or unavailable institutions represented?

How are workflow-local states separated from canonical institutional states?
```

**Why this belongs to Interoperability Review:**  
Navigator's authority boundary is resolved. The handoff contract is an implementation matter.

---

### IR-006 — Registry Source-Object Exchange Mechanics

Review the technical relationship between an SREG and the source object it registers.

Questions include:

```text
How is source identity resolved?

How is source version represented?

How are source corrections or supersession reflected?

What Registry metadata may be updated independently?

How does Registry avoid accidentally duplicating the source object?
```

The governing rule remains:

```text
Registry creates the SREG.
Registry does not create the registered source object.
```

**Why this belongs to Interoperability Review:**  
Authority is settled; synchronization and representation mechanics are not.

---

### IR-007 — Beacon Discovery Exchange Mechanics

Review how Beacon exchanges Discovery Signals and discovery metadata with other institutions.

Questions include:

```text
How does Beacon encode stable references?

How does Beacon preserve source provenance and state?

How are Discovery Signals returned to Navigator workflows?

How does a Beacon signal point to Registry, Chronicle, Anchor, Certifier, Atlas, or Attestor objects consistently?

How are source changes reflected in discovery metadata?
```

**Why this belongs to Interoperability Review:**  
Beacon's role is settled. Cross-system discovery exchange mechanics remain technical interoperability.

---

### IR-008 — Attestor Governed-Input Ingestion

Review how objects from Atlas, Certifier, Registry, Chronicle, Anchor, Beacon, and external sources enter Attestor as governed references.

Questions include:

```text
How is the source object mapped into the Attestor Reference Profile?

Which source fields are authoritative?

Which values are copied versus referenced?

How is provenance preserved?

How is relevant source state frozen for Evaluation?

How are source changes detected after Evaluation?
```

The governing rule remains:

```text
Source Object
→ Governed Reference
→ Eligibility Determination
→ Attestation / Evaluation Basis
→ Rule-Constrained Evaluation
→ Trust Statement
```

**Why this belongs to Interoperability Review:**  
Attestor's architecture is resolved; governed ingestion and cross-system compatibility are implementation concerns.

---

### IR-009 — Common Relationship Serialization

The Suite-level relationship vocabulary is already settled:

```text
references
derived-from
supports
evaluates
results-in
supersedes
corrects
related-to
```

The Interoperability Review should determine how those relationships are represented consistently across institutional schemas and whether all institutions need a common minimum relationship structure.

**Why this belongs to Interoperability Review:**  
Relationship meaning is reconciled; technical representation and compatibility remain.

---

### IR-010 — External-System Interoperability Boundary

Where relevant, review how external governed information enters Suite institutions.

Potential questions include:

```text
How is external source identity represented?

How is external authority preserved?

What provenance is mandatory?

How is permitted use recorded?

How are external versions or state changes handled?

Are APIs, protocols, or transport standards necessary, optional, or institution-specific?
```

No particular external protocol, API, or transport is currently required by the institutional architecture.

**Why this belongs to Interoperability Review:**  
This is an exchange-mechanics question, not a Suite institutional-architecture question.

---

## Matters That Do NOT Need to Move Forward

The following are already reconciled and should **not** be reopened merely because they affect interoperability:

```text
Institutional roles
Canonical object ownership
Authority boundaries
Reference ≠ Derivation
Reference ≠ Support
Reference does not transfer authority
Connection ≠ Identity
Canonical Creation ≠ Lifecycle Activation ≠ Publication
Validation ≠ Conformance
Valid ≠ True
Conceptual Sequence ≠ Mandatory Pipeline
Exercised Lineage ≠ Mandatory Architecture
```

The Interoperability Review should implement and test these rules, not redefine them.

---

## Handoff Summary

```text
Suite-level architectural questions requiring Interoperability Review
→ NONE

Detailed technical interoperability matters identified
→ YES

Primary focus
→ References · Schemas · Serialization · Resolution · Handoffs · State/Version Propagation · Compatibility

Authority redesign
→ NOT REQUIRED

Canonical-object redesign
→ NOT REQUIRED

Relationship-semantic redesign
→ NOT REQUIRED
```

The upcoming Interoperability Review therefore begins from a stable architectural foundation rather than from unresolved Suite design.

**Disposition:** COMPLETE — APPROVED
