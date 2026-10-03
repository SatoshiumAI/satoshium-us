# Satoshium Suite Interoperability Review — Validation & Conformance Expectations Across Boundaries

**Date:** October 3, 2026  
**Review:** Satoshium Suite Interoperability Review  
**Step:** 13 — Review Validation and Conformance Expectations Across Boundaries  
**Status:** COMPLETE — APPROVED

---

## Purpose

This review defines what a receiving Satoshium Suite institution must establish before consuming another institution's object and separates five distinct questions:

```text
Source-Object Validity
Reference Validity
Schema Conformity
Eligibility
Institutional Evaluation
```

The governing rule is:

> **VALIDATION ≠ ELIGIBILITY ≠ CONFORMANCE ≠ INSTITUTIONAL EVALUATION.**

And:

> **SOURCE VALIDATION ≠ DOWNSTREAM INSTITUTIONAL DETERMINATION.**

This review does not create a universal Suite-wide "valid" status.

It defines boundary behavior.

---

# 1. Consumption Principle

A receiving institution may not assume that a source object is consumable merely because:

```text
it exists
it resolves
it is published
it is valid in its source institution
it is conformant to its source schema
it has an authoritative identifier
```

Before governed consumption, the receiving institution must distinguish:

```text
Can I resolve it?
Is the reference itself well-formed?
Is the source object valid under its own governing rules?
Does the received representation conform to the declared exchange/schema contract?
Is it eligible for my specific institutional purpose?
What does my own institution determine after consuming it?
```

These are separate gates.

---

# 2. Five-Layer Boundary Model

## 2.1 Source-Object Validity

Question:

```text
Does the source institution regard this object as valid under its own rules?
```

Examples:

```text
Certifier validation of a Certification Package
Registry validation of a SREG
Chronicle validation of a Chronicle Entry
Anchor validation of an Integrity Reference
Beacon validation of a Discovery Signal
Attestor validation of an Attestation / Trust Statement
```

This validity belongs to the source institution.

A receiving institution may record or rely on it where permitted.

It does not inherit or recreate the source institution's validation authority.

> **SOURCE VALIDATION ≠ RECEIVING-INSTITUTION VALIDATION.**

---

## 2.2 Reference Validity

Question:

```text
Is the cross-institution reference itself usable and interpretable?
```

Reference validity requires, at minimum:

```text
identifier present
source institution identified
object type known
relationship semantics known
authority context preserved
provenance sufficient
accessibility/resolution condition known
version/state information present where material
```

A valid source object may still be unusable if the reference is malformed or incomplete.

Therefore:

> **VALID SOURCE OBJECT ≠ VALID REFERENCE.**

---

## 2.3 Schema Conformity

Question:

```text
Does the received machine representation conform to the declared schema/profile/contract version?
```

Schema conformity may apply to:

```text
canonical source schema
interoperability envelope
reference profile
handoff contract
institution-specific input profile
```

A representation can be structurally conformant while still being:

```text
irrelevant
ineligible
unsupported
stale
superseded
substantively unfavorable
```

Therefore:

> **SCHEMA CONFORMITY ≠ ELIGIBILITY.**

And:

> **CONFORMANT ≠ PUBLISHED.**

---

## 2.4 Eligibility

Question:

```text
May this otherwise identifiable and interpretable object legitimately enter this receiving institution's governed process?
```

Eligibility is institution-specific and purpose-specific.

Examples:

```text
Registry → Registrability
Chronicle → Preservation Eligibility
Attestor → Evaluation Eligibility
Certifier → certification-scope / subject admission rules
Anchor → representation / integrity-subject suitability
Beacon → discovery-significance / signal admission rules
Navigator → workflow precondition / routing eligibility
```

Eligibility is not inherited from source validity.

Therefore:

> **SOURCE VALID ≠ DOWNSTREAM ELIGIBLE.**

---

## 2.5 Institutional Evaluation

Question:

```text
What substantive determination does the receiving institution make after consuming the eligible object?
```

Examples:

```text
Certifier → Certification Decision
Registry → Registry-owned admission / registration decision
Chronicle → Preservation decision / historical treatment
Anchor → Verification Result / integrity determination
Beacon → Discovery Signal determination
Attestor → Evaluation Outcome / Trust Statement
Navigator → workflow progression / branch result
```

Institutional evaluation remains owned by the receiving institution.

> **SOURCE RESULT ≠ RECEIVING-INSTITUTION RESULT.**

---

# 3. Minimum Pre-Consumption Validation Sequence

The adopted boundary sequence is:

```text
1. Resolve Reference
2. Validate Reference Envelope
3. Check Source Object / Source State as required
4. Check Schema / Contract Conformity
5. Apply Receiving-Institution Eligibility Rules
6. Perform Receiving-Institution Evaluation / Action
```

This sequence is conceptual.

It does not require every institution to expose identical implementation steps.

> **CONCEPTUAL SEQUENCE ≠ MANDATORY PIPELINE.**

---

# 4. Required Validation Before Consumption

A receiving institution must not consume another institution's object blindly.

At minimum it should determine:

```text
identity known
source institution known
object type known
relationship known
provenance sufficient
authority context known
representation parsable / interpretable
schema or contract version supported
source version/state known where material
accessibility condition known
```

Then the receiving institution applies its own eligibility/admission rules.

Only after that should substantive institutional processing occur.

---

# 5. Source-Object Validity Handling

A source may declare its own object:

```text
valid
invalid
not-tested
unknown
historically valid
superseded
withdrawn
```

The receiving institution must preserve that source declaration accurately.

It must not convert:

```text
source valid
→ downstream approved

source invalid
→ downstream institutional failure automatically

source not-tested
→ pass
```

The receiving institution decides whether source validity is:

```text
required
advisory
contextual
irrelevant
```

for its own use case.

---

# 6. Reference Validity Handling

A reference is invalid for interoperability use when critical exchange semantics are missing or contradictory.

Examples:

```text
identifier absent
source institution unknown
object type ambiguous
relationship missing
authority context absent
provenance absent
version required but missing
resolution target contradictory
```

The receiving institution should:

```text
reject
flag
or hold for review
```

according to its rules.

It must not silently repair or infer material semantics unless such repair is explicitly governed.

---

# 7. Schema Conformity Handling

A representation may be:

```text
conformant
non-conformant
unsupported schema version
partially parseable
unknown profile
```

The receiving institution should distinguish:

```text
payload structurally invalid
from
payload structurally valid but semantically ineligible
```

A non-conformant representation may still be historically meaningful, but it should not enter an automated governed process as if conformant.

---

# 8. Invalid Input

## Meaning

```text
invalid
→ fails applicable validation requirements
```

This may refer to:

```text
source-object validation failure
reference validation failure
receiving-object validation failure
```

The type must be explicit.

## Receiving Behavior

Default:

```text
do not treat as successfully consumable
preserve failure reason
flag
reject or route to review
```

Potential exception:

A historically invalid object may still be eligible for Chronicle preservation or another explicitly contextual purpose.

Therefore:

> **INVALID ≠ NONEXISTENT.**

And:

> **INVALID FOR ONE PURPOSE ≠ INELIGIBLE FOR EVERY PURPOSE.**

---

# 9. Non-Conformant Input

## Meaning

```text
non-conformant
→ fails a declared schema/profile/specification
```

## Receiving Behavior

Default automated behavior:

```text
do not process as conformant
record conformance failure
attempt governed alternate profile only if explicitly supported
otherwise reject / quarantine / manual review
```

Do not silently coerce to a local schema if that would change meaning.

A non-conformant source object may still be:

```text
historically relevant
discoverable
reviewable
```

depending on institutional purpose.

---

# 10. Unavailable Input

## Meaning

```text
identifier/reference known
but representation cannot currently be retrieved or reached
```

## Receiving Behavior

```text
preserve known identifier
preserve prior provenance
record unavailable state
do not infer withdrawal
do not infer invalidity
do not infer continued active state
retry or defer where governed
```

Therefore:

```text
UNAVAILABLE ≠ INVALID
UNAVAILABLE ≠ WITHDRAWN
UNAVAILABLE ≠ SUCCESS
```

---

# 11. Unknown Input State

## Meaning

The institution cannot determine a material property such as:

```text
validity
current version
current lifecycle state
publication state
authority
provenance completeness
relationship interpretation
```

## Receiving Behavior

```text
preserve unknown explicitly
do not normalize into pass
do not infer favorable state
flag where material
hold / defer / manual review according to institutional rules
```

> **UNKNOWN ≠ SUCCESS.**

> **NOT-TESTED ≠ PASS.**

---

# 12. Unsupported Input

## Meaning

The receiving institution recognizes the object or representation but does not support:

```text
schema version
object type
relationship type
profile
transport
controlled value
institution-specific extension
```

## Receiving Behavior

```text
record unsupported condition
preserve original source value where possible
do not coerce into nearest supported value
do not silently map to related-to
do not treat as invalid source object unless source itself is invalid
```

Preferred outcomes:

```text
unsupported
manual review
alternate supported representation
future compatibility work
```

---

# 13. Superseded Input

## Meaning

The referenced object remains historically meaningful but no longer holds current operative standing.

## Receiving Behavior

```text
preserve superseded identifier
resolve successor where declared
preserve source state at use
distinguish historical from current use
flag if current operative standing matters
```

The receiving institution may still consume a superseded object for:

```text
historical analysis
audit
provenance
comparison
reconstruction
```

but must not silently treat it as current.

> **SUPERSEDED ≠ INVALID.**

> **SUPERSEDED ≠ DELETED.**

---

# 14. Boundary Matrix

| Input Condition | Can Resolve? | Can Be Historically Preserved? | Can Enter Automated Current-State Processing? | Requires Flag / Review? | May Be Eligible for Some Purpose? |
|---|---:|---:|---:|---:|---:|
| Valid + Conformant | Usually | Yes | Yes, subject to eligibility | Maybe | Yes |
| Invalid | Maybe | Yes | Usually No | Yes | Sometimes |
| Non-conformant | Maybe | Yes | Usually No | Yes | Sometimes |
| Unavailable | No / temporarily | Yes, from prior evidence | No | Yes | Sometimes |
| Unknown | Maybe | Yes | Not without policy | Yes | Sometimes |
| Unsupported | Maybe | Yes | No under unsupported profile | Yes | Sometimes |
| Superseded | Yes | Yes | Not as current without explicit rule | Often | Yes |

---

# 15. Institution-Specific Examples

## Registry

Registry may require:

```text
source identity
source authority
source reference validity
required metadata
schema/profile conformity
Registrability
```

A valid Certifier object is not automatically registrable.

---

## Chronicle

Chronicle may preserve:

```text
invalid
withdrawn
superseded
non-conformant
failed
```

objects or events if historically significant and preservation-eligible.

Therefore Chronicle is a strong example of:

```text
source invalid
≠ Chronicle ineligible automatically
```

---

## Anchor

Anchor may preserve integrity context for an artifact without validating the substantive truth or authority of its contents.

Therefore:

```text
integrity-valid representation
≠ substantively valid source assertion
```

---

## Beacon

Beacon may discover an unavailable, superseded, withdrawn, or invalid object as a fact of discovery.

But Beacon must represent that source condition accurately.

Discovery does not convert source state.

---

## Attestor

Attestor requires explicit separation among:

```text
source validity
reference validity
schema conformity
eligibility
evaluation outcome
Trust Statement
```

A valid and conformant source can still be ineligible.

An eligible source can still contribute to a contradicted or indeterminate evaluation.

---

## Navigator

Navigator may route an object whose institutional state is:

```text
invalid
unknown
superseded
unavailable
```

only if the Workflow Definition explicitly permits that condition.

Workflow handling does not redefine the object's source state.

---

# 16. Source Validation Evidence

Where source validation matters, the reference should preserve:

```text
validation authority
validation result
validation version / rule set where material
validation timestamp where material
source version validated
```

The receiving institution may rely on this evidence only within its own rules.

It must not rebrand source validation as its own determination.

---

# 17. Schema / Contract Validation Evidence

Where interoperability automation is used, the receiving institution should preserve:

```text
schema/profile identifier
schema/profile version
validation result
validation timestamp
validator / implementation identity where material
unsupported fields / warnings
```

This allows later reconstruction of why the payload was accepted or rejected.

---

# 18. Eligibility Evidence

Where eligibility is a governed gate, preserve:

```text
eligibility rule/profile
input identity
scope
decision
reason
decision time
deciding institution
```

Eligibility evidence is not a Trust Statement, Certification Decision, or source validity result.

---

# 19. Institutional Evaluation Evidence

The receiving institution should preserve enough evidence to reconstruct:

```text
what inputs were accepted
under which rules
with which versions/states
what outcome was determined
what limitations applied
```

This keeps evaluation attributable and reviewable.

---

# 20. Findings

## VCE-01 — Source validity

**APPROVED**

Source-object validity belongs to the originating institution and must remain distinct from downstream processing.

---

## VCE-02 — Reference validity

**APPROVED**

A valid source object may still have an invalid interoperability reference.

---

## VCE-03 — Schema conformity

**APPROVED**

Conformity is structural/profile compliance and must not be conflated with eligibility or substantive evaluation.

---

## VCE-04 — Eligibility

**APPROVED**

Eligibility remains receiving-institution and purpose-specific.

---

## VCE-05 — Institutional evaluation

**APPROVED**

The receiving institution retains authority over its own substantive determination.

---

## VCE-06 — Invalid inputs

**APPROVED**

Reject / flag for automated current-state use by default, while permitting institution-specific historical or contextual handling.

---

## VCE-07 — Non-conformant inputs

**APPROVED**

Do not process as conformant; preserve original meaning; allow manual / alternate-profile handling only where governed.

---

## VCE-08 — Unavailable inputs

**APPROVED**

Unavailable must not be interpreted as invalid, withdrawn, or successful.

---

## VCE-09 — Unknown inputs

**APPROVED**

Unknown conditions remain explicit.

---

## VCE-10 — Unsupported inputs

**APPROVED**

Unsupported must not be silently coerced into supported semantics.

---

## VCE-11 — Superseded inputs

**APPROVED**

Superseded objects remain historically resolvable and may remain eligible for bounded historical/contextual purposes.

---

# Review Determination

Cross-institution consumption requires layered validation, not one universal PASS/FAIL concept.

The adopted model is:

```text
Source Object Validity
        ↓
Reference Validity
        ↓
Schema / Contract Conformity
        ↓
Receiving-Institution Eligibility
        ↓
Receiving-Institution Evaluation
```

Each layer answers a different question.

No layer transfers authority to another.

No institutional architecture requires reopening.

---

# FINAL DISPOSITION

# VALIDATION & CONFORMANCE EXPECTATIONS ACROSS BOUNDARIES — COMPLETE — APPROVED

Governing rules:

> **VALID SOURCE OBJECT ≠ VALID REFERENCE.**

> **VALIDATION ≠ ELIGIBILITY.**

> **VALIDATION ≠ CONFORMANCE.**

> **SCHEMA CONFORMITY ≠ ELIGIBILITY.**

> **SOURCE VALIDATION ≠ DOWNSTREAM INSTITUTIONAL DETERMINATION.**

> **UNKNOWN ≠ SUCCESS.**

> **NOT-TESTED ≠ PASS.**

The Suite should reject semantic collapse and preserve each boundary determination independently.
