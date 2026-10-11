# Satoshium Suite Governance Review — Governance Proposal, Decision, Implementation & Documentation Distinction

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 3 of 4 — Governance Process, Decisions, Versioning & Accountability  
**Step:** 4 — Distinguish Governance Proposal, Governance Decision, Implementation Action, and Documentation Update  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record formally distinguishes four governance concepts that must remain separate throughout the Satoshium Suite governance process:

- governance proposal;
- governance decision;
- implementation action;
- documentation update.

The distinction is necessary because each carries a different governance meaning.

The governing rule is:

> **A proposal requests change. A decision authorizes or rejects change. Implementation executes authorized change. Documentation records and communicates the resulting state.**

---

# 1. Governance Proposal

## Definition

A **Governance Proposal** is a formal request to consider a change, interpretation, correction, exception, or governance action.

It introduces a matter into the governance process.

A Proposal may identify:

- a problem;
- a proposed future state;
- an authority question;
- a standards change;
- a methodology change;
- an institutional change;
- a canonical-object change;
- a constitutional issue;
- an exception request;
- a correction request.

## Governance Status

A Proposal has no independent authority merely because it exists.

Therefore:

```text
PROPOSAL
≠
DECISION

PROPOSAL
≠
APPROVAL

PROPOSAL
≠
AUTHORITY TO IMPLEMENT
```

## Example

```text
Proposal:
Move ownership of Object X
from Institution A to Institution B.
```

Until governed and approved:

```text
ownership remains unchanged
```

## Rule

> **A Proposal creates a question for governance; it does not create the answer.**

---

# 2. Governance Decision

## Definition

A **Governance Decision** is the authorized outcome of the governance process.

It reflects:

```text
Proposal
→ Review
→ Determination
→ Approval
```

and records what has been formally decided.

A Governance Decision may:

- approve;
- reject;
- conditionally approve;
- defer;
- require revision;
- reclassify;
- supersede;
- preserve the current state.

## Authority

A Decision becomes authoritative only when approved by the correct governance authority.

Therefore:

```text
DETERMINATION
+
VALID APPROVAL
=
GOVERNANCE DECISION
```

## Decision Content

A formal Decision should identify:

- governed subject;
- classification;
- authority;
- conclusion;
- approval;
- effective date;
- affected objects or institutions;
- version implications;
- implementation obligations;
- preservation requirements.

## Rule

> **The Governance Decision is the authoritative statement of what governance has concluded and authorized.**

---

# 3. Implementation Action

## Definition

An **Implementation Action** is an operational act taken to execute an approved Governance Decision.

Examples include:

- changing code;
- modifying schema;
- changing configuration;
- updating workflow behavior;
- migrating records;
- changing publication logic;
- implementing a new Procedure;
- activating a successor institution;
- retiring a service endpoint;
- applying an approved interoperability change.

## Authority Boundary

Implementation authority derives from the approved Decision.

Therefore:

```text
IMPLEMENTATION AUTHORITY
≤
APPROVED DECISION
```

The implementer may not broaden the decision.

If implementation reveals the need for a broader change:

```text
STOP
→ NEW OR REVISED GOVERNANCE PROPOSAL
```

## Critical Rule

> **Implementation executes governance; it does not create governance.**

Therefore:

```text
CODE CHANGE
≠
GOVERNANCE DECISION

DEPLOYMENT
≠
APPROVAL

REPEATED PRACTICE
≠
AUTHORIZED POLICY
```

---

# 4. Documentation Update

## Definition

A **Documentation Update** changes the written or published representation of a governed state.

Examples include:

- README update;
- governance page update;
- Standard revision;
- architecture page correction;
- status page change;
- changelog entry;
- Governance Decision Record publication;
- lifecycle documentation update.

## Two Documentation Classes

### A. Descriptive Documentation Update

Records an already-authorized state.

Example:

```text
Governance Decision:
Beacon role clarified.

Documentation Update:
Beacon README updated to reflect approved role.
```

This is documentation following governance.

### B. Documentation Correction

Corrects wording that is stale, inaccurate, or inconsistent with an already-settled authoritative state.

Example:

```text
Page says Beacon is "in development"
but approved Suite state is "Operational"

→ documentation correction
```

No new governance authority is created.

---

# Documentation Boundary

Documentation may:

- describe;
- clarify;
- record;
- publish;
- correct;
- preserve.

Documentation may not independently:

- create institutional authority;
- transfer canonical ownership;
- create a new Suite institution;
- establish constitutional dependency;
- change institutional role;
- supersede an approved governance decision.

Therefore:

> **Documentation records governed reality; it does not manufacture governed reality.**

---

# 5. The Four-Way Distinction

The concepts can be summarized as:

```text
GOVERNANCE PROPOSAL
→ asks what should change

GOVERNANCE DECISION
→ determines what is authorized

IMPLEMENTATION ACTION
→ makes the authorized change operational

DOCUMENTATION UPDATE
→ records and communicates the resulting state
```

---

# 6. Standard Sequence

The normal sequence is:

```text
Proposal
↓
Review
↓
Determination
↓
Approval
↓
Governance Decision
↓
Publication
↓
Implementation Action
↓
Documentation Update
↓
Preservation
```

Publication may itself include documentation of the Decision.

Additional operational documentation may follow Implementation.

The controlling principle is:

```text
AUTHORITY FLOWS FROM DECISION
NOT FROM IMPLEMENTATION OR DOCUMENTATION
```

---

# 7. Why the Distinction Matters

Without this separation, several governance failures become possible.

## Proposal Mistaken for Decision

```text
Someone proposes a new authority
→ documentation begins describing it as current
→ de facto architecture appears to change
```

Prohibited.

---

## Implementation Mistaken for Decision

```text
Code begins enforcing a dependency
→ dependency treated as constitutionally required
```

Prohibited.

---

## Documentation Mistaken for Decision

```text
README assigns new canonical ownership
→ ownership treated as transferred
```

Prohibited.

---

## Decision Without Implementation

This is legitimate during transition.

```text
Decision
→ APPROVED

Implementation
→ PENDING
```

The approved state exists as a governance commitment even if operational rollout is incomplete.

The implementation status must remain visible.

---

# 8. Status Distinction

Each concept should carry its own state.

## Proposal States

```text
PROPOSED
UNDER REVIEW
WITHDRAWN
REVISED
```

## Decision States

```text
DETERMINED
APPROVED
REJECTED
SUPERSEDED
```

## Implementation States

```text
NOT STARTED
IN PROGRESS
IMPLEMENTED
PARTIALLY IMPLEMENTED
ROLLED BACK
```

## Documentation States

```text
PENDING UPDATE
UPDATED
CORRECTED
SUPERSEDED
ARCHIVED
```

These states should not be collapsed into one generic "status."

---

# 9. Decision vs. Effective State

A Decision may be approved before it takes effect.

Therefore:

```text
APPROVAL DATE
≠
EFFECTIVE DATE
```

Likewise:

```text
EFFECTIVE DATE
≠
IMPLEMENTATION COMPLETION DATE
```

The record must clearly distinguish them when relevant.

---

# 10. Documentation Cannot Backdate Authority

If documentation is updated late, the authoritative date remains the approved governance date or effective date—not the date the page happened to be edited.

Similarly, early documentation cannot make a not-yet-approved proposal authoritative.

Therefore:

```text
DOCUMENTATION TIMESTAMP
≠
GOVERNANCE AUTHORITY DATE
```

---

# 11. Implementation Drift Rule

If implementation differs from the approved Decision:

```text
IMPLEMENTATION DRIFT
```

must be identified.

The response depends on significance:

```text
minor non-substantive deviation
→ correct implementation

material deviation
→ governance review

authority / ownership / role deviation
→ constitutional escalation if applicable
```

The implementation may not redefine the Decision.

---

# 12. Documentation Drift Rule

If documentation differs from the approved Decision:

```text
DOCUMENTATION DRIFT
```

exists.

The correct response is to reconcile documentation to the authoritative governance state unless review establishes that the governance state itself requires amendment.

Therefore:

```text
documentation inconsistency
→ does not automatically reopen architecture
```

---

# 13. Governance Precedence Rule

When the four conflict, precedence is:

```text
APPROVED GOVERNANCE DECISION
↓
AUTHORIZED IMPLEMENTATION
↓
CURRENT DOCUMENTATION
```

A pending Proposal does not outrank an existing approved Decision.

Therefore:

```text
CURRENT APPROVED DECISION
remains controlling
until
NEW APPROVED DECISION takes effect
```

---

# 14. Formal Classification Table

| Concept | Purpose | Creates Authority? | May Change Architecture? | Primary Record |
|---|---|---:|---:|---|
| Governance Proposal | Request consideration | No | No | Proposal record |
| Governance Decision | Authorize / reject governed outcome | Yes | Yes, if properly classified and approved | Governance Decision Record |
| Implementation Action | Execute approved outcome | No independent authority | Only within approved scope | Implementation record |
| Documentation Update | Record / communicate governed state | No | No independent authority | Published documentation |

---

# Governing Doctrine

> **Proposal asks. Decision authorizes. Implementation executes. Documentation records.**

Expanded:

> **No Proposal becomes binding merely by being written. No implementation action becomes governance merely by being deployed. No documentation update creates authority merely by being published. Governance authority resides in the approved Decision issued by the proper authority.**

---

## Final Disposition

```text
Governance Proposal
→ DEFINED

Governance Decision
→ DEFINED

Implementation Action
→ DEFINED

Documentation Update
→ DEFINED

Authority precedence
→ ESTABLISHED

Implementation drift
→ ESTABLISHED

Documentation drift
→ ESTABLISHED

Status distinctions
→ ESTABLISHED

Proposal / Decision / Implementation / Documentation distinction
→ COMPLETE — APPROVED
```

# GOVERNANCE PROPOSAL / DECISION / IMPLEMENTATION / DOCUMENTATION DISTINCTION — COMPLETE — APPROVED
