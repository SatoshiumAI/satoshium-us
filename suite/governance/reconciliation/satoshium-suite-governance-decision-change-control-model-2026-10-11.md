# Satoshium Suite Governance — Decision & Change-Control Model

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 3 of 4 — Governance Process, Decisions, Versioning & Accountability  
**Principal Artifact:** Decision & Change-Control Model  
**Status:** COMPLETE — APPROVED

---

## Purpose

This principal artifact consolidates Day 3 of the Satoshium Suite Governance Review.

It defines how governance decisions are:

- proposed;
- reviewed;
- determined;
- approved;
- published;
- implemented;
- versioned;
- superseded;
- corrected;
- recorded;
- indexed;
- made transparent;
- and historically preserved.

The governing objective is:

> **Allow governance to change deliberately, visibly, and accountably without losing the ability to reconstruct what governed before, why it changed, and under whose authority.**

---

# I. Governance Decision Lifecycle

The standard governance lifecycle is:

```text
Proposal
→ Review
→ Determination
→ Approval
→ Publication
→ Implementation
→ Preservation
```

Classification remains an intake control applied before and during Review:

```text
Routine
→ Institution-Level

Material
→ Institution + Suite Review

Constitutional
→ Formal Suite Governance Decision
```

The process is sequential in authority.

Therefore:

```text
Proposal
≠ Decision

Review
≠ Approval

Publication
≠ Approval

Implementation
≠ Governance Authority
```

---

# II. Standard Governance Process

The governing process is:

## Proposal

Introduces a governance question.

It must identify:

- current state;
- proposed state;
- governed subject;
- rationale;
- affected institutions;
- affected canonical objects;
- expected authority impact;
- expected interoperability impact.

## Review

Tests the Proposal against applicable governance.

Review may include:

- institution-level review;
- Suite-level review;
- interoperability review;
- architecture reconciliation.

## Determination

Records the governance conclusion.

Typical outcomes:

```text
SUPPORTED
SUPPORTED WITH CONDITIONS
REQUIRES REVISION
REJECTED
ESCALATED
NO CHANGE REQUIRED
```

## Approval

Creates authorized governance state.

Approval authority follows classification and governed subject.

## Publication

Makes the approved governance state reviewable.

Publication records authority; it does not create authority.

## Implementation

Executes the approved Decision.

Implementation authority must remain within approved scope.

## Preservation

Maintains the decision history, version history, correction history, and supersession lineage.

---

# III. Governance Decision Roles & Decision Rights

Decision rights follow:

```text
governed subject
+
change classification
+
affected authority
```

The role model is:

| Stage | Responsible Authority |
|---|---|
| Propose | Authorized stakeholder with legitimate governance interest |
| Review | Owning institution and affected governance authorities |
| Determine | Authority responsible for the governed subject at the required level |
| Approve | Institution for Routine; institution + Suite where Material; Formal Suite Governance for Constitutional |
| Implement | Responsible operator or designated institution |
| Publish | Steward of the authoritative governance surface |

The core separation rules are:

```text
PROPOSER
≠ APPROVER

REVIEWER
≠ DECISION OWNER

IMPLEMENTER
≠ GOVERNANCE AUTHORITY

PUBLISHER
≠ APPROVER
```

For Routine matters, one actor may perform multiple roles where appropriate.

For Material and Constitutional matters, separation should increase with significance.

---

# IV. Proposal / Decision / Implementation / Documentation Distinction

The Suite formally distinguishes:

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

The governing doctrine is:

> **Proposal asks. Decision authorizes. Implementation executes. Documentation records.**

When these differ, precedence is:

```text
APPROVED GOVERNANCE DECISION
↓
AUTHORIZED IMPLEMENTATION
↓
CURRENT DOCUMENTATION
```

A pending Proposal never overrides a current approved Decision.

---

# V. Governance Review Thresholds

A governance matter must receive every category of review implicated by its actual effect.

## Institution-Level Review

Required when the matter affects an institution's own governed domain.

## Suite-Level Review

Required when the matter materially affects:

- another institution;
- shared Standards;
- shared Methodology;
- shared governance;
- canonical architecture;
- Suite-wide coherence.

## Interoperability Review

Required when the matter materially affects:

- interfaces;
- schemas;
- serialization;
- identifiers;
- references;
- provenance;
- lifecycle propagation;
- correction propagation;
- version propagation;
- compatibility.

## Architecture Reconciliation

Required when the matter:

- contradicts settled architecture;
- reopens canonical ownership;
- alters institutional role;
- creates unclear authority;
- creates mandatory constitutional dependency;
- conflicts with settled Suite semantics.

The governing doctrine is:

> **Institution review protects institutional authority. Suite review protects shared coherence. Interoperability review protects exchange and meaning across boundaries. Architecture reconciliation protects the settled architecture itself.**

---

# VI. Governance Versioning

Governance versioning is:

> **The controlled issuance, identification, supersession, correction, preservation, and historical linking of authoritative governance states over time.**

Core distinctions:

```text
VERSION
≠ DECISION

CORRECTION
≠ VERSION

SUPERSESSION
≠ MUTATION

CHANGED CONCLUSION
=
NEW GOVERNANCE DECISION
```

Recommended version model:

```text
MAJOR.MINOR
```

with optional:

```text
MAJOR.MINOR.PATCH
```

Version numbering describes editions.

Governance classification controls review.

---

# VII. Supersession

Supersession is:

> **The governed replacement of a prior decision's current operative standing by a later approved governance decision, while preserving the prior decision as an intact historical record.**

The model is:

```text
Prior Decision
→ historically valid for its effective period

New Decision
→ controlling prospectively

Relationship
→ SUPERSEDES
```

The governing rule is:

```text
SUPERSESSION
≠ MUTATION
```

Supersession may be:

- partial;
- complete;
- institutional;
- constitutional.

The prior Decision remains preserved and linked bidirectionally to its successor.

---

# VIII. Governance Correction Procedures

Four correction classes are established:

```text
ERRONEOUS GOVERNANCE TEXT
→ valid governance, wrong written representation

INCORRECT IMPLEMENTATION
→ valid governance, nonconforming execution

OBSOLETE GOVERNANCE
→ formerly valid governance that is no longer current

CONFLICTING GOVERNANCE
→ incompatible authoritative claims
```

Conflicts follow the established decision ladder:

```text
CONFIRM
→ CLARIFY
→ RECONCILE
→ CORRECT
→ CHANGE
```

The governing doctrine is:

> **Correct the thing that is wrong. Do not alter valid governance merely because documentation, implementation, age, or another governance instrument creates inconsistency.**

---

# IX. Governance Decision Record Model

The Governance Decision Record (GDR) is:

> **The authoritative record of a governance determination and its approved operative effect, including provenance, classification, scope, approval, implementation, versioning, supersession, and preservation metadata.**

Recommended identifier:

```text
GDR-YYYY-NNNN
```

Example:

```text
GDR-2026-0001
```

The GDR preserves one governance decision.

---

# X. Minimum Required GDR Fields

Every formal GDR must include:

```text
Decision ID
Decision Date
Subject
Scope
Authority
Rationale
Decision
Affected Institutions
Affected Canonical Objects
Effective State
Version
Supersession / Correction History
```

Where applicable:

```text
Effective Date
```

is also required.

No required field should be silently omitted.

If no applicable value exists:

```text
None
```

or:

```text
Not Applicable
```

must be stated.

The governing rule is:

> **A GDR is incomplete if a later reviewer cannot reconstruct the authority, scope, rationale, operative effect, and historical relationship of the decision from the record itself.**

---

# XI. Governance Decision Register

The Suite requires a formal **Governance Decision Register**.

The distinction is:

```text
GDR
→ authoritative record of one governance decision

Governance Decision Register
→ authoritative index of governance decisions
```

The Register should include:

- all Material decisions;
- all Constitutional decisions;
- selected significant Routine decisions.

Minimum Register fields should include:

```text
Decision ID
Decision Date
Subject
Classification
Decision Type
Affected Institutions
Affected Canonical Objects
Status
Effective State
Version
Supersedes
Superseded By
GDR Location
```

The Register does not create authority.

It makes governance discoverable and traceable.

---

# XII. Transparency Rules

Governance transparency must make current governance understandable without sacrificing historical integrity.

The following rules are established.

## 1. Current Governance Must Be Identifiable

Every authoritative governance surface should make clear:

```text
what is current
what is effective
what is superseded
what is pending
```

Where a current governing version exists, it should be discoverable without requiring users to infer status from chronology.

---

## 2. Authority Must Be Visible

Material and Constitutional governance decisions must identify:

- responsible authority;
- decision classification;
- approval status;
- effective state;
- affected institutions;
- affected canonical objects.

Governance should not require readers to infer authority from repository placement, authorship, or implementation behavior.

---

## 3. Decision Lineage Must Be Visible

Where governance has changed, current surfaces should identify:

```text
Supersedes
Superseded By
Corrects
Corrected By
```

as applicable.

Readers should be able to move both:

```text
forward
→ to current governance
```

and:

```text
backward
→ to prior governance
```

---

## 4. Material Change Must Be Explainable

Material and Constitutional decisions should preserve enough rationale to explain:

- why change occurred;
- what problem was addressed;
- what authority supported the change;
- what alternatives or constraints mattered.

Transparency means more than publishing the final sentence.

It requires preserving the governed reason for change.

---

## 5. Governance Status Must Be Explicit

Governance records should use explicit states such as:

```text
PROPOSED
UNDER REVIEW
APPROVED
PUBLISHED
EFFECTIVE
IMPLEMENTED
SUPERSEDED
REJECTED
WITHDRAWN
ARCHIVED
```

A reader should not need to infer whether a document is current merely because it is publicly accessible.

---

## 6. Proposal Must Not Masquerade as Current Governance

A Proposal must be visibly distinguished from:

```text
approved
effective
current
```

governance.

Likewise, draft wording must not be presented in a way that implies authority.

---

## 7. Implementation Status Must Be Visible Where Material

If a Decision is approved but not fully implemented, the governance record should state:

```text
APPROVED
→ IMPLEMENTATION IN PROGRESS
```

rather than implying that implementation is complete.

---

## 8. Public Accessibility Should Be Proportionate

Material and Constitutional governance should be publicly reviewable when appropriate.

Routine operational governance may use proportionate documentation, provided the authoritative state remains traceable.

Transparency should support accountability without forcing every internal operational detail into a public constitutional surface.

---

# XIII. Historical-Preservation Rules

Current governance may evolve only if prior governance remains historically reconstructable.

The following preservation rules are established.

## 1. No Silent Overwrite

A formally published governance decision may not be silently replaced.

Prohibited:

- overwrite without preservation;
- substantive conclusion changed in place;
- prior approval erased;
- prior effective date changed silently;
- superseded authority removed from history.

---

## 2. Preserve Every Formal Governance State

Every published Material or Constitutional governance state must remain preserved.

This includes:

- prior versions;
- superseded decisions;
- rejected decisions where historically material;
- correction history;
- effective dates;
- approval records;
- implementation transitions.

---

## 3. Preserve Historical Truth

The preservation rule is:

```text
CURRENT GOVERNANCE
→ may change

HISTORICAL GOVERNANCE
→ must remain true
```

Therefore:

> **Change prospectively. Preserve retrospectively.**

---

## 4. Superseded Does Not Mean Invalid History

A superseded Decision remains valid evidence of what governed during its effective period.

Therefore:

```text
SUPERSEDED
≠
NEVER VALID
```

---

## 5. Correction Must Preserve the Error Record When Material

When a material correction occurs, the record should preserve:

- what was incorrect;
- what replaced it;
- why correction occurred;
- correction date;
- authority for correction.

This prevents governance history from becoming artificially clean.

---

## 6. Architecture History Must Remain Preserved

If a future Constitutional Decision changes settled Suite architecture:

```text
Prior Architecture
→ preserved as historical governing state

New Architecture
→ becomes controlling prospectively
```

The earlier Suite Reconciliation remains historically valid for the architecture it documented.

---

## 7. Preservation Must Be Discoverable

Preservation is not complete merely because old files still exist somewhere.

Historical records should remain:

- identifiable;
- referenceable;
- linked;
- status-marked;
- discoverable from current governance where relevant.

---

## 8. Provenance Must Be Preserved

Historical governance records should preserve:

- originating authority;
- approval authority;
- decision date;
- effective date;
- version;
- supersession relationship;
- correction lineage.

Without provenance, preserved files do not constitute reliable governance history.

---

# XIV. Transparency & Preservation Combined Rule

Transparency governs:

```text
what readers can understand now
```

Historical preservation governs:

```text
what future readers can reconstruct later
```

Both are required.

Therefore:

> **Current governance must be clear enough to act upon and historical governance must be preserved well enough to audit.**

---

# XV. Current-State / Historical-State Model

The Suite should maintain two simultaneous views.

## Current-State View

Shows:

```text
current effective governance
current versions
current authorities
current institutional status
current decision standing
```

## Historical-State View

Preserves:

```text
prior decisions
superseded versions
former authorities
former architecture
corrections
transitions
```

The current-state view must not destroy the historical-state view.

The historical-state view must not confuse readers about what currently governs.

---

# XVI. Preservation Responsibilities

The governing authority for a decision remains responsible for ensuring its governance history is preserved.

Supporting Suite institutions may assist without absorbing authority.

Examples:

```text
Chronicle
→ may preserve historically significant governance occurrences

Registry
→ may catalog governance records

Anchor
→ may preserve integrity references

Beacon
→ may improve discoverability
```

But:

```text
Preservation support
≠ Governance ownership
```

The GDR remains the governance authority record.

---

# XVII. Accountability Rule

Governance accountability requires that later reviewers be able to answer:

```text
Who proposed?
Who reviewed?
Who determined?
Who approved?
What changed?
When did it become effective?
Who implemented?
What did it supersede?
What remains preserved?
```

If those questions cannot be answered, the governance record is insufficient.

---

# XVIII. Day 3 Governing Model

The complete Day 3 model is:

```text
PROPOSAL
↓
REVIEW
↓
DETERMINATION
↓
APPROVAL
↓
GOVERNANCE DECISION RECORD
↓
PUBLICATION
↓
IMPLEMENTATION
↓
VERSIONING / CORRECTION / SUPERSESSION AS REQUIRED
↓
GOVERNANCE DECISION REGISTER
↓
PRESERVATION
```

Transparency surrounds the entire process.

Historical preservation protects the entire process through time.

---

# XIX. Day 3 Governing Doctrine

> **Governance must be explicit enough to authorize action, structured enough to assign accountability, versioned enough to evolve, transparent enough to review, and preserved enough to reconstruct.**

Expanded:

> **Proposal creates the question. Review tests it. Determination states the conclusion. Approval creates authority. Publication exposes the decision. Implementation executes it. Versioning manages change. Supersession replaces current standing without rewriting history. Correction repairs defects. The Governance Decision Record preserves the decision. The Governance Decision Register preserves discoverability. Transparency explains current governance. Historical preservation ensures prior governance remains true.**

---

# XX. Formal Day 3 Determination

```text
Governance Decision Lifecycle
→ ESTABLISHED

Standard Governance Process
→ ESTABLISHED

Decision Roles & Rights
→ ESTABLISHED

Proposal / Decision / Implementation / Documentation Distinction
→ ESTABLISHED

Review Escalation Thresholds
→ ESTABLISHED

Governance Versioning
→ ESTABLISHED

Governance Supersession
→ ESTABLISHED

Governance Correction Procedures
→ ESTABLISHED

Governance Decision Record Model
→ ESTABLISHED

Minimum Required GDR Fields
→ ESTABLISHED

Governance Decision Register
→ REQUIRED

Transparency Rules
→ ESTABLISHED

Historical-Preservation Rules
→ ESTABLISHED

Day 3 Principal Artifact
→ COMPLETE — APPROVED
```

# SATOSHIUM SUITE GOVERNANCE — DECISION & CHANGE-CONTROL MODEL  
# COMPLETE — APPROVED
