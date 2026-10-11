# Satoshium Suite Governance Review — Governance Decision Record Model

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 3 of 4 — Governance Process, Decisions, Versioning & Accountability  
**Step:** 9 — Establish the Governance Decision Record Model  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record establishes the standard **Governance Decision Record (GDR)** model for the Satoshium Suite.

The GDR is the durable record of a governed decision.

It is intended to preserve:

- what was proposed;
- what was reviewed;
- what was determined;
- who approved it;
- when it became effective;
- what it changed;
- how it was implemented;
- what it superseded;
- and how the historical record is preserved.

The governing principle is:

> **A governance decision should be reconstructable from its record without relying on memory, implementation behavior, or later documentation.**

---

# I. Definition

A **Governance Decision Record (GDR)** is:

> **The authoritative record of a governance determination and its approved operative effect, including provenance, classification, scope, approval, implementation, versioning, supersession, and preservation metadata.**

A GDR is not:

- merely a proposal;
- merely a meeting note;
- merely a changelog entry;
- merely an implementation ticket;
- merely documentation.

It is the formal governance record.

---

# II. GDR Identifier

Every formal Governance Decision Record should receive a stable identifier.

Recommended pattern:

```text
GDR-YYYY-NNNN
```

Example:

```text
GDR-2026-0001
```

The identifier should remain stable across the life of the decision record.

If the GDR itself is versioned:

```text
GDR-2026-0001
Version: 1.1
```

The Decision ID and document version remain distinct.

---

# III. Minimum Required Fields

Every Material or Constitutional GDR should contain at minimum:

```text
Decision ID:
Title:
Status:
Classification:
Governed Subject:
Decision Type:
Proposer:
Reviewing Authority:
Determining Authority:
Approving Authority:
Decision Date:
Publication Date:
Effective Date:
Current State:
Proposed State:
Determination:
Approval:
Affected Institution(s):
Affected Canonical Object(s):
Authority Impact:
Interoperability Impact:
Implementation Requirements:
Version:
Supersedes:
Superseded By:
Correction History:
Preservation Location:
```

Routine matters may use a reduced record where appropriate, but the same concepts should remain traceable.

---

# IV. Core Record Sections

## 1. Identity

```text
Decision ID
Title
Version
Status
Classification
Decision Type
```

Purpose:

```text
identify the decision unambiguously
```

---

## 2. Governance Context

Record:

- governed subject;
- background;
- reason for review;
- current state;
- proposed state;
- triggering issue.

Purpose:

```text
explain why governance was invoked
```

---

## 3. Proposal

Record:

- proposer;
- proposal date;
- requested change;
- justification;
- evidence or source basis;
- expected impact.

Purpose:

```text
preserve what was actually requested
```

The Proposal section must not be rewritten later to match the final Decision.

---

## 4. Classification

Record:

```text
Routine
Material
Constitutional
```

Also record:

- classification rationale;
- whether reclassification occurred;
- prior classification if changed.

Purpose:

```text
show why the matter received its level of review
```

---

## 5. Review

Record:

- reviewing authority;
- affected institutions consulted;
- Suite review, if required;
- interoperability review, if required;
- architecture reconciliation, if required;
- evidence considered;
- material findings;
- conflicts;
- limitations;
- unresolved issues.

Purpose:

```text
show how the proposal was tested
```

---

## 6. Determination

Record the substantive governance conclusion.

Examples:

```text
SUPPORTED

SUPPORTED WITH CONDITIONS

REQUIRES REVISION

REJECTED

ESCALATED

NO CHANGE REQUIRED
```

The determination should explain:

- what governance concluded;
- why;
- what conditions apply;
- what scope is covered.

Purpose:

```text
separate review findings from the final governance conclusion
```

---

## 7. Approval

Record:

- approving authority;
- approval status;
- approval date;
- conditions;
- limitations;
- delegated authority, if any.

Purpose:

```text
establish that the determination became authorized
```

The record must make clear that:

```text
DETERMINATION
≠
APPROVAL
```

---

## 8. Operative Effect

Record exactly what the Decision changes.

Examples:

- Standard requirement;
- institutional Procedure;
- governance rule;
- canonical-object architecture;
- authority boundary;
- institutional membership;
- constitutional relationship.

The operative effect should distinguish:

```text
what changes
from
what remains unchanged
```

Purpose:

```text
prevent scope expansion during implementation
```

---

## 9. Affected Authority & Ownership

Record:

- affected institution(s);
- authority gained;
- authority lost;
- authority preserved;
- canonical ownership impact;
- lifecycle impact;
- correction impact;
- versioning impact.

If none:

```text
No authority or canonical ownership change.
```

Purpose:

```text
make authority effects explicit
```

---

## 10. Interoperability Impact

Record whether the Decision affects:

- identifiers;
- references;
- schemas;
- serialization;
- provenance;
- lifecycle propagation;
- correction propagation;
- version propagation;
- compatibility;
- external systems.

Possible value:

```text
None
Minor
Material
Requires Interoperability Review
```

Purpose:

```text
preserve cross-institution implementation consequences
```

---

## 11. Implementation Requirements

Record:

- implementing authority;
- required actions;
- implementation scope;
- transition plan;
- migration requirements;
- validation requirements;
- completion status.

Purpose:

```text
separate authorized governance from operational execution
```

---

## 12. Publication

Record:

- publication location;
- publication date;
- authoritative surface;
- related Standards / Methodology / institutional documents updated;
- changelog entry.

Purpose:

```text
show where the decision became reviewable
```

---

## 13. Effective Date

The GDR must identify when the Decision becomes controlling.

Possible relationships:

```text
Approval Date
→ 2026-10-11

Publication Date
→ 2026-10-12

Effective Date
→ 2026-10-15
```

Purpose:

```text
separate authorization, publication, and operative effect
```

---

## 14. Versioning

Record:

```text
GDR Version:
Prior GDR Version:
Current GDR Version:
Version Change Summary:
```

If the Decision instrument changes without changing the conclusion, the record may be versioned.

If the substantive conclusion changes:

```text
NEW GDR REQUIRED
```

unless the governance model explicitly treats the later action as a separate superseding decision.

---

## 15. Supersession

Record:

```text
Supersedes:
Superseded By:
Supersession Scope:
Supersession Effective Date:
```

If none:

```text
None
```

Purpose:

```text
preserve decision lineage
```

---

## 16. Correction History

Record:

- correction date;
- correction type;
- prior text/state;
- corrected text/state;
- authority for correction;
- whether conclusion changed.

If conclusion changed:

```text
NEW GOVERNANCE DECISION REQUIRED
```

Purpose:

```text
prevent silent rewriting
```

---

## 17. Preservation

Record:

- canonical repository path;
- archived prior versions;
- related decision records;
- Chronicle reference if applicable;
- preservation status.

Purpose:

```text
ensure long-term governance traceability
```

---

# V. Recommended Decision Types

The GDR should identify the kind of governance decision being made.

Suggested controlled values:

```text
STANDARD
METHODOLOGY
GOVERNANCE
INSTITUTIONAL
INTEROPERABILITY
CANONICAL_OBJECT
AUTHORITY
MEMBERSHIP
CORRECTION
SUPERSESSION
EXCEPTION
CONSTITUTIONAL
```

A decision may carry more than one type if necessary, but one should be designated primary.

---

# VI. Recommended Status Model

Suggested GDR states:

```text
PROPOSED
UNDER REVIEW
DETERMINED
APPROVED
PUBLISHED
EFFECTIVE
IMPLEMENTATION IN PROGRESS
IMPLEMENTED
SUPERSEDED
REJECTED
WITHDRAWN
ARCHIVED
```

These states should not be conflated.

Example:

```text
APPROVED
≠
IMPLEMENTED
```

---

# VII. Governance Classification Field

Every GDR should identify:

```text
ROUTINE
MATERIAL
CONSTITUTIONAL
```

with a short rationale.

Example:

```text
Classification:
MATERIAL

Rationale:
Changes a shared Suite Methodology requirement and
affects Registry and Attestor interoperability,
but does not alter institutional role, ownership,
membership, or sovereignty.
```

---

# VIII. Decision Authority Fields

The record should identify distinct actors for:

```text
Proposer
Reviewer
Determiner
Approver
Implementer
Publisher
```

Where the same actor performs multiple roles, that is acceptable if governance permits it.

The record should still list each role separately.

Purpose:

```text
preserve accountability by function
```

---

# IX. GDR Relationship Fields

A GDR may link to:

```text
references
supersedes
superseded-by
corrects
corrected-by
implements
implemented-by
depends-on
related-to
```

Relationships must not transfer authority.

The established Suite rule remains:

```text
REFERENCE DOES NOT TRANSFER AUTHORITY
```

---

# X. GDR Decision Scope

Every GDR should state:

```text
IN SCOPE
```

and:

```text
OUT OF SCOPE
```

This prevents implementation from expanding the Decision beyond what was approved.

Example:

```text
In Scope:
→ Certification Standard review threshold

Out of Scope:
→ Certifier canonical object ownership
→ Registry lifecycle
→ Suite membership
```

---

# XI. GDR Template

Recommended standard structure:

```text
# Governance Decision Record

Decision ID:
Title:
Version:
Status:
Classification:
Decision Type:

## Governance Context

## Proposal

## Classification

## Review

## Determination

## Approval

## Operative Effect

## Scope

### In Scope

### Out of Scope

## Affected Institutions

## Affected Canonical Objects

## Authority Impact

## Interoperability Impact

## Implementation Requirements

## Publication

## Effective Date

## Versioning

## Supersession

## Correction History

## Preservation

## Related Governance Records

## Final Disposition
```

---

# XII. Routine GDR Lite

Routine matters may use a lighter record when the governance impact is narrow.

Minimum Routine record:

```text
Decision ID:
Title:
Classification:
Governed Subject:
Decision:
Approver:
Effective Date:
Implementation:
Publication / Documentation Update:
Preservation Location:
```

Routine simplification must not be used for Material or Constitutional matters.

---

# XIII. Material GDR

A Material GDR should always include:

- full Review;
- Suite impact;
- interoperability impact;
- classification rationale;
- approval;
- implementation;
- versioning;
- preservation.

---

# XIV. Constitutional GDR

A Constitutional GDR must additionally include:

- affected Suite membership;
- institutional role impact;
- canonical ownership impact;
- sovereignty impact;
- architecture reconciliation result;
- constitutional approval authority;
- transition plan;
- predecessor/successor treatment where applicable;
- historical architecture preservation.

No Constitutional Decision is complete without a formal GDR.

---

# XV. GDR Immutability Rule

Once a GDR is approved and published, its substantive historical record must not be silently overwritten.

Permitted later actions:

```text
correction metadata
new version
supersession
status update
implementation update
```

Prohibited:

```text
silent rewriting of original conclusion
silent removal of prior approval
silent alteration of effective date
silent alteration of authority
```

The rule is:

> **Approved GDR history is append-preserved, not rewritten away.**

---

# XVI. Current-State vs Historical Fields

The GDR should distinguish between:

```text
historical decision facts
```

and:

```text
current status metadata
```

Example:

Historical fact:

```text
Approved: 2026-10-11
```

Current status:

```text
Status: SUPERSEDED
Superseded By: GDR-2027-0004
```

This allows the record to remain historically true while still showing present standing.

---

# XVII. Relationship to Chronicle

Chronicle may preserve a historically significant governance occurrence through a Chronicle Entry where Chronicle's Preservation Eligibility criteria are satisfied.

However:

```text
GDR
→ governance authority record

Chronicle Entry
→ historical preservation record
```

The Chronicle record does not replace the GDR.

---

# XVIII. Relationship to Registry

Registry may catalog a GDR or governance instrument through a Satoshium Registry Entry where registrability requirements are satisfied.

However:

```text
GDR
→ remains governed by its governance authority

SREG
→ catalogs / references the GDR
```

Registration does not transfer governance authority.

---

# XIX. Relationship to Anchor

Anchor may create an Integrity Reference for a published GDR.

That can preserve integrity evidence for the artifact.

However:

```text
Integrity Reference
≠ governance approval

Integrity Preservation
≠ governance authority
```

---

# XX. Relationship to Beacon

Beacon may emit Discovery Signals associated with published governance records.

That supports discoverability.

It does not determine governance validity.

---

# XXI. Relationship to Attestor

Attestor may evaluate governed inputs and issue Attestations or Trust Statements concerning a GDR where applicable.

That does not make Attestor the owner of the Decision.

---

# XXII. Governing Doctrine

> **A Governance Decision Record is the durable proof of what governance decided, under whose authority, with what scope, from what date, and with what relationship to prior and future governance.**

Expanded:

> **The GDR separates proposal, review, determination, approval, implementation, publication, versioning, supersession, correction, and preservation into one traceable record so that current authority and historical governance can both remain clear.**

---

## Final Disposition

```text
Governance Decision Record
→ DEFINED

GDR identifier model
→ ESTABLISHED

Required fields
→ ESTABLISHED

Decision roles
→ ESTABLISHED

Status model
→ ESTABLISHED

Classification field
→ ESTABLISHED

Scope model
→ ESTABLISHED

Versioning fields
→ ESTABLISHED

Supersession fields
→ ESTABLISHED

Correction history
→ ESTABLISHED

Preservation requirements
→ ESTABLISHED

Routine GDR Lite
→ ESTABLISHED

Material GDR
→ ESTABLISHED

Constitutional GDR
→ ESTABLISHED

Silent overwrite
→ PROHIBITED

Governance Decision Record Model
→ COMPLETE — APPROVED
```

# GOVERNANCE DECISION RECORD MODEL — COMPLETE — APPROVED
