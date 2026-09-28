# Satoshium Suite Reconciliation — Chronicle Position

**Date:** September 27, 2026  
**Phase:** Phase III — Whole-Suite Architecture  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record reconciles Chronicle's position within the mature Satoshium Suite.

The purpose is to preserve the governing principle:

> **Chronicle records when. It does not become the authoritative source for what another institution owns.**

Chronicle is therefore authoritative for governed historical preservation, not for the substantive source object owned by another institution.

---

# Formal Role

Chronicle's reconciled institutional role is:

> **Historical Preservation**

Its canonical object is:

> **Chronicle Entry**

The essential model is:

```text
Qualifying Occurrence
        ↓
Preservation Eligibility
        ↓
Chronicle Entry
```

Chronicle preserves the historical occurrence.

It does not absorb the source object's authority.

---

# Chronicle Records When

The core editorial rule remains:

> **Chronicle records when.**

This means Chronicle is concerned with:

- when a qualifying occurrence happened;
- what occurrence is being preserved;
- what source objects are associated with it;
- how the event is represented historically;
- when the Chronicle Entry itself was created, activated, corrected, superseded, or published.

Chronicle's contribution is temporal and historical preservation.

It is not the authoritative source for every substantive claim contained in or referenced by the Entry.

---

# Chronicle Does Not Become Source Authority

Example:

```text
SC-CERT-2026-0001
        ↓ occurrence preserved by
CHR-2026-0001
```

Chronicle may preserve the issuance or creation of the Certification Package.

But Certifier remains authoritative for:

- the Certification Package;
- the Certification Decision;
- certification evidence;
- certification lifecycle;
- the substantive certification meaning.

Therefore:

> **Chronicle authority over the Entry ≠ Certifier authority over the Certification Package.**

---

# Chronicle ≠ Certification

Chronicle may record:

> a certification was issued.

It does not thereby certify the subject.

Therefore:

```text
Chronicle records certification event
≠
Chronicle performs certification
```

And:

> **Historical preservation ≠ Certification**

A Chronicle Entry may reference a certification outcome, but the outcome remains Certifier-owned.

---

# Chronicle ≠ Registry

Chronicle and Registry may both relate to the same broader matter.

For example:

```text
SREG-2026-0001
→ registers SC-CERT-2026-0001

CHR-2026-0001
→ preserves the issuance / creation occurrence
```

These are distinct institutional functions.

Registry answers:

> **What source object has been canonically registered?**

Chronicle answers:

> **What qualifying occurrence has been preserved historically?**

Therefore:

> **Registration ≠ Historical Preservation**

And:

> **SREG ≠ Chronicle Entry**

---

# Chronicle ≠ Anchor

Chronicle preserves occurrences.

Anchor preserves representation integrity.

For the same broader matter:

```text
Chronicle
→ preserves when something happened

Anchor
→ preserves integrity of an artifact or representation
```

Chronicle does not become authoritative for:

- hashes;
- canonicalization;
- signatures;
- representation boundaries;
- integrity verification.

Therefore:

> **Historical preservation ≠ Integrity preservation**

---

# Chronicle ≠ Beacon

Chronicle preserves qualifying historical occurrences.

Beacon discovers relevant states, changes, conditions, or objects.

A Chronicle Entry may later be observed or referenced by Beacon.

Beacon may create a Discovery Signal concerning an event already preserved by Chronicle.

But:

```text
Chronicle Entry ≠ Discovery Signal
```

And:

> **Historical recording ≠ discovery authority**

Chronicle does not become Beacon merely because it contains information another institution later discovers.

---

# Chronicle ≠ Attestor

Attestor may reference Chronicle as part of a governed evidence set.

For example:

```text
Chronicle Entry
        ↓ referenced by
Attestation / Evaluation
```

But Chronicle does not perform:

- Attestor Eligibility;
- Rule-Constrained Evaluation;
- Evaluation Outcome determination;
- Trust Statement creation.

Therefore:

> **Historical preservation ≠ evaluation**

And:

> **Chronicle Entry ≠ Trust Statement**

---

# Chronicle Verification ≠ Source Verification

Chronicle may verify historical facts necessary to preserve an occurrence.

For example, Chronicle may verify:

```text
SC-CERT-2026-0001 existed
the relevant issuance occurred
the occurrence date is supportable
the source references are traceable
```

That does not mean Chronicle independently re-certifies or re-validates the source institution's substantive decision.

Therefore:

> **Chronicle Verification ≠ Certification Verification**

And:

> **Chronicle Verification ≠ source-institution authority**

---

# Chronicle Validation ≠ Source Validation

Chronicle may validate its own canonical object against Chronicle requirements.

Those requirements may include:

- required fields;
- event type;
- provenance;
- temporal data;
- historical source references;
- controlled vocabulary;
- lifecycle requirements;
- publication requirements.

That means:

> **the Chronicle Entry is valid under Chronicle rules.**

It does not mean the referenced source object inherits that validation.

Therefore:

> **Valid Chronicle Entry ≠ Valid source object by inheritance.**

---

# Chronicle Authority Is Real but Bounded

Chronicle's authority should not be weakened merely because it does not own source content.

Chronicle is authoritative for:

- Chronicle Entry identity;
- preservation eligibility;
- historical representation;
- event classification;
- temporal metadata;
- Chronicle provenance;
- Chronicle lifecycle;
- corrections;
- versioning;
- publication;
- preservation history.

That is genuine institutional authority.

It is simply a different authority domain from source ownership.

---

# Chronicle Can Preserve Events from Any Suite Institution

Chronicle is not limited to Certifier.

A qualifying historical occurrence may originate from:

```text
Atlas
Navigator
Certifier
Registry
Anchor
Beacon
Attestor
External authoritative sources
```

where Chronicle rules permit preservation.

Therefore:

> **Chronicle follows qualifying occurrences, not a fixed upstream institution.**

This preserves:

> **Sequence ≠ Dependency.**

---

# Registry Is Not a Universal Prerequisite

The first production lineage included Registry before Chronicle.

That is historical fact for that exercised lineage.

But the architecture should not infer:

> every Chronicle Entry requires a SREG.

The true dependency is:

> **Chronicle requires a qualifying occurrence and sufficient historical basis.**

Registry may be one useful source or reference.

It is not a universal prerequisite.

---

# Anchor Is Not a Universal Prerequisite

Likewise:

> **Integrity evidence may support preservation, but Anchor is not automatically required before Chronicle.**

Chronicle may preserve a historical occurrence before an Integrity Reference exists.

If a particular Chronicle profile requires integrity evidence, that would be an explicit scoped dependency.

It would not become a universal one.

---

# Chronicle and Time Semantics

Chronicle has a special relationship with time.

It may track multiple temporal concepts, including:

```text
occurrence time
source creation time
Chronicle Entry creation time
Chronicle activation time
Chronicle publication time
correction time
supersession time
```

These should remain distinct.

Chronicle's authority over temporal representation does not mean it controls another institution's lifecycle timestamps.

For example:

```text
Certifier publication date
≠
Chronicle publication date
```

Both may relate to the same broader history.

They remain institution-specific.

---

# Chronicle Does Not Rewrite Source History

If a source institution later:

- corrects;
- versions;
- withdraws;
- supersedes;

its object, Chronicle should not silently rewrite the earlier historical Entry as though the original occurrence never happened.

Instead, Chronicle should preserve historical continuity.

Conceptually:

```text
Original Occurrence
→ Chronicle Entry

Later Correction / Supersession
→ new qualifying occurrence or governed update
```

depending on Chronicle rules.

The governing principle is:

> **Historical preservation records change; it does not erase prior reality.**

---

# Correction in Chronicle

Chronicle may correct an error in its own Entry.

For example:

```text
CHR-2026-0001 V1.0
        ↓ correction
CHR-2026-0001 V1.1
```

if the same historical occurrence remains the subject.

But if the original Entry represented the wrong occurrence entirely, a new Chronicle Entry may be required.

Therefore:

> **Correction of historical representation ≠ rewriting the source event.**

---

# Chronicle Source References

A Chronicle Entry may reference source objects from multiple institutions.

For example:

```text
Chronicle Entry
    references
Certification Package
SREG
Integrity Reference
Discovery Signal
Attestation
Trust Statement
```

where relevant.

These references improve historical traceability.

They do not transfer authority to Chronicle.

Therefore:

> **Reference does not transfer authority.**

---

# Correct Architectural Position

The best conceptual model is:

```text
Institutional Action / Occurrence
            │
            ▼
     Qualifies for Preservation?
            │
            ▼
         Chronicle
   Historical Preservation
            │
            ▼
      Chronicle Entry
```

Chronicle sits alongside, not above, the source institutions.

Its authority is historical.

The source institution's authority remains substantive.

---

# Reconciled Chronicle Boundaries

Chronicle may:

- determine Preservation Eligibility;
- classify Event Types;
- create Chronicle Entries;
- verify historical basis;
- validate Chronicle Entries;
- maintain historical provenance;
- govern Chronicle lifecycle;
- correct and version Entries;
- publish preserved history;
- reference source objects.

Chronicle does **not**, merely by doing so:

- perform certification;
- register source objects;
- create integrity authority;
- create Discovery Signals;
- perform Attestor evaluation;
- issue Trust Statements;
- own source-object lifecycle;
- own source publication state;
- replace source provenance;
- become authoritative for the source's substantive conclusion.

---

# Governing Rules

1. **Chronicle = Historical Preservation.**
2. Chronicle's canonical object is the **Chronicle Entry**.
3. **Chronicle records when.**
4. Chronicle is authoritative for historical preservation, not for another institution's source object.
5. **Historical authority ≠ source authority.**
6. **Chronicle Entry ≠ Certification Package.**
7. **Chronicle Entry ≠ SREG.**
8. **Chronicle Entry ≠ Integrity Reference.**
9. **Chronicle Entry ≠ Discovery Signal.**
10. **Chronicle Entry ≠ Trust Statement.**
11. Chronicle Verification does not recreate source-institution verification or certification.
12. Chronicle Validation applies to the Chronicle Entry, not the source object.
13. Valid Chronicle Entry does not make the source object valid by inheritance.
14. Chronicle may preserve occurrences from any Suite institution where eligible.
15. Registry is not a universal prerequisite for Chronicle.
16. Anchor is not a universal prerequisite for Chronicle.
17. Chronicle time semantics remain distinct from source lifecycle timestamps.
18. Corrections preserve historical continuity rather than erase history.
19. References improve traceability but do not transfer authority.
20. Chronicle does not become the authoritative source for what another institution owns.

---

# Governing Formulation

> **CHRONICLE IS AUTHORITATIVE FOR THE HISTORICAL RECORD IT CREATES, NOT FOR THE SUBSTANTIVE SOURCE OBJECT IT PRESERVES.**

Short form:

> **CHRONICLE RECORDS WHEN. SOURCE INSTITUTIONS REMAIN AUTHORITATIVE FOR WHAT THEY OWN.**

---

## Final Disposition

# CHRONICLE POSITION RECONCILIATION — COMPLETE — APPROVED

Chronicle is formally positioned as the Suite's **Historical Preservation** institution.

It has strong authority over Chronicle Entries and preserved history while maintaining a strict boundary against certification, registration, integrity, discovery, Attestor evaluation, and source-object ownership.
