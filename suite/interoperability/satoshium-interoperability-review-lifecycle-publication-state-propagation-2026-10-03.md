# Satoshium Suite Interoperability Review — Lifecycle & Publication-State Propagation Review

**Date:** October 3, 2026  
**Review:** Satoshium Suite Interoperability Review  
**Step:** 7 — Review Lifecycle and Publication-State Propagation  
**Status:** COMPLETE — APPROVED

---

## Purpose

This review determines how a consuming Satoshium Suite institution should respond when a referenced object changes lifecycle state, publication state, version, correction status, or canonical identity.

The review preserves the settled Suite distinction:

> **CANONICAL CREATION ≠ LIFECYCLE ACTIVATION ≠ PUBLICATION**

And the governing lifecycle rule:

> **CREATION DEFINES EXISTENCE. ACTIVATION DEFINES OPERATIVE STATE. PUBLICATION DEFINES ACCESSIBILITY.**

This review does not redefine any institution's lifecycle.

It defines interoperability behavior when source-state changes cross institutional boundaries.

---

# 1. Propagation Principle

A downstream institution must not silently rewrite its historical basis merely because an upstream object changes later.

The governing distinction is:

> **SOURCE STATE AT USE ≠ LATER SOURCE STATE**

Therefore, interoperability must preserve both:

```text
Historical Source State
→ what the consuming institution actually observed / used

Current Source State
→ what the source institution declares now
```

These may differ legitimately.

A later source change may trigger:

```text
refresh
review
reevaluation
republishing
correction
supersession
new downstream object
no action
```

depending on the receiving institution's own rules.

It does not automatically mutate the downstream object.

---

# 2. Minimum State-Propagation Context

When a source object is referenced across institutions, the consuming institution should be able to preserve:

```text
source_identifier
source_institution
source_object_type
source_version_at_use
source_lifecycle_state_at_use
source_publication_state_at_use
source_state_observed_at
source_provenance
relationship_type
authority_context

current_source_version
current_source_lifecycle_state
current_source_publication_state
current_source_checked_at
change_detected
change_classification
downstream_action
```

Not every field must be embedded in every canonical object.

The minimum requirement is that enough context exists to distinguish historical state from current state and to explain any downstream action.

---

# 3. Consuming-Institution Action Vocabulary

For interoperability purposes, downstream handling is classified as:

## OBSERVE

Detect or receive the upstream state change.

```text
observe
→ recognize that source state changed
```

Observation alone does not change the downstream object.

---

## STORE

Preserve the new source-state information and the prior state used historically.

```text
store
→ retain current source-state metadata
→ retain historical source-state-at-use
```

Storage does not imply republication or reevaluation.

---

## REFRESH

Update a non-canonical or current-facing representation, pointer, cache, discovery view, catalog display, or workflow context to reflect the source's current state.

```text
refresh
→ update current source-state representation
```

Refresh must not silently rewrite the historical state on which a prior determination was based.

---

## REPUBLISH

Publish an updated downstream representation or downstream object version where the receiving institution's own rules require publication after a material update.

```text
republish
→ governed publication action
```

Republishing is not automatic.

---

## FLAG

Create an explicit review condition because the upstream change may materially affect the downstream object, conclusion, integrity context, discovery result, registration, or workflow.

```text
flag
→ requires institution-specific review
```

A flag is not itself a lifecycle transition.

---

## IGNORE

Take no downstream action where the upstream change is irrelevant to the receiving institution's governed purpose.

```text
ignore
→ no material downstream consequence
```

Ignoring must be a governed determination, not an accidental failure to observe.

---

# 4. Test Case — Active → Superseded

## Source Event

```text
Source Object
Active
→ Superseded
```

The source object's prior identity remains historically valid.

The source institution may identify a successor object or version.

## Consuming Institution Must

### Observe

**YES**

Detect that the source's operative standing changed.

### Store

**YES**

Preserve:

```text
source state at original use → Active
later source state → Superseded
superseding identifier / version → where declared
effective time → where available
```

### Refresh

**YES, where the consumer presents current source status**

Examples:

```text
Registry catalog view
Beacon current discovery presentation
Navigator current workflow context
Attestor source-status review surface
```

### Flag

**YES when operative standing matters to downstream meaning**

Examples:

- active certification referenced by Beacon;
- current Registry source condition;
- Attestor evaluation basis that depended on active source status.

### Republish

**CONDITIONAL**

Republish only where the receiving institution's own object or public representation must change.

### Ignore

**ONLY if source supersession is immaterial to the downstream object's governed purpose**

## Rule

> **SUPERSESSION ≠ MUTATION**

The prior source identity and historical downstream basis remain preserved.

---

# 5. Test Case — Active → Withdrawn

## Source Event

```text
Source Object
Active
→ Withdrawn
```

Withdrawal changes operative standing.

It does not mean:

```text
deleted
unpublished
invalid
nonexistent
```

unless separately governed.

## Consuming Institution Must

### Observe

**YES**

### Store

**YES**

Preserve both prior Active state and later Withdrawn state.

### Refresh

**YES where current source status is displayed**

### Flag

**PRESUMPTIVELY YES**

Withdrawal is a high-significance source-state change for most downstream uses.

Potential consequences include:

```text
Registry
→ update source-status representation

Chronicle
→ preserve withdrawal as possible qualifying historical occurrence

Anchor
→ no automatic integrity failure; source lifecycle change is distinct from integrity

Beacon
→ current discovery may need state refresh or new signal

Attestor
→ reevaluation may be required if source state was material to evaluation

Navigator
→ workflow may require rerouting or review
```

### Republish

**CONDITIONAL**

Only according to receiving-institution rules.

### Ignore

**RARE**

Only where withdrawal is demonstrably irrelevant to the receiving institution's purpose.

## Rule

> **WITHDRAWN ≠ UNPUBLISHED**

---

# 6. Test Case — Unpublished → Published

## Source Event

```text
Publication State
Unpublished
→ Published
```

This is a publication transition, not lifecycle activation.

## Consuming Institution Must

### Observe

**YES where publication/accessibility matters**

### Store

**YES**

Preserve:

```text
prior publication state → Unpublished
current publication state → Published
publication time / representation → where available
```

### Refresh

**YES for current-facing public-resolution or accessibility metadata**

### Flag

**CONDITIONAL**

Flag only if publication materially changes the receiving institution's ability to rely on, expose, or resolve the source.

### Republish

**NOT AUTOMATIC**

A source becoming public does not force downstream republication.

### Ignore

**PERMITTED**

If downstream semantics do not depend on source accessibility.

## Rule

> **ACTIVE ≠ PUBLISHED**

And:

> **PUBLICATION ≠ AUTHORITY TRANSFER**

---

# 7. Test Case — New Version

## Source Event

```text
Source Identifier
→ same canonical identity
→ new version
```

A new version does not automatically imply:

```text
new identity
activation
publication
supersession
correction
material semantic change
```

Those must be determined separately.

## Consuming Institution Must

### Observe

**YES where version continuity is tracked**

### Store

**YES**

Preserve:

```text
version used historically
new version
version change time
change description / classification where available
```

### Refresh

**YES if current-facing representation should point to latest source version**

### Flag

**CONDITIONAL ON MATERIALITY**

If the change is non-material to the downstream use:

```text
store / refresh
→ sufficient
```

If material:

```text
flag
→ downstream review
```

### Republish

**CONDITIONAL**

Only if the receiving institution changes its own representation or canonical object/version.

### Ignore

**PERMITTED for immaterial version changes**

## Rule

> **VERSION ≠ LIFECYCLE STATE**

And:

> **NEW VERSION ≠ AUTOMATIC NEW CANONICAL IDENTITY**

---

# 8. Test Case — Correction

## Source Event

```text
Source Object / Version
→ corrected
```

Correction repairs an error or defect.

It does not itself define whether the resulting source representation receives:

```text
same identity
new version
new identity
```

The source institution governs that determination.

## Consuming Institution Must

### Observe

**YES**

### Store

**YES**

Preserve:

```text
prior source state
correction reason
corrected state
source correction identifier/version where available
effective time
```

### Refresh

**YES if the consumer exposes current source metadata**

### Flag

**YES if corrected matter was used materially**

The downstream institution must determine whether its own output remains supportable.

### Republish

**CONDITIONAL**

A receiving institution may need:

```text
new downstream version
correction notice
superseding object
new canonical identity
```

depending on the effect of the corrected source matter.

### Ignore

**ONLY if the correction is demonstrably irrelevant to downstream meaning**

## Rule

> **CORRECTION ≠ VERSION**

> **CORRECTION ≠ DELETION**

---

# 9. Test Case — Material Replacement

## Source Event

A source change is sufficiently material that the source institution creates a new canonical identity.

```text
Old Source Object
→ materially replaced by
New Source Object
```

This is not merely a new version.

## Consuming Institution Must

### Observe

**YES**

### Store

**YES**

Preserve both identities and the declared relationship:

```text
old source identifier
new source identifier
supersedes / corrects / related relationship as governed
change time
change reason where available
```

### Refresh

**YES where current source targeting matters**

### Flag

**YES**

Material replacement requires downstream review because the consuming institution's historical reference may point to an object that no longer holds current operative standing.

### Republish

**POSSIBLE / OFTEN REQUIRED**

Institution-specific consequences may include:

```text
Registry
→ SREG version or new SREG depending on whether registered subject changed

Chronicle
→ new Chronicle Entry if a distinct qualifying Occurrence exists

Anchor
→ new Integrity Reference if Integrity Subject / protected representation materially changes

Beacon
→ new Discovery Signal if the discovery is materially different

Attestor
→ new Attestation for materially changed assertion
→ new Trust Statement for changed conclusion
```

### Ignore

**NO where replacement changes the referenced subject materially**

## Rule

> **MATERIAL CHANGE MAY REQUIRE NEW IDENTITY**

And for Attestor:

> **CHANGED CONCLUSION = CHANGED CANONICAL STATEMENT**

---

# 10. Institution-Specific Propagation Behavior

## Atlas

When referenced Atlas intelligence changes:

```text
observe
→ source version / package change

store
→ prior and current intelligence context

flag
→ where downstream use depended on changed intelligence

republish
→ only under receiving institution's own rules
```

Atlas remains authoritative for its governed intelligence.

---

## Navigator

Navigator should preserve:

```text
workflow-local source snapshot
current source state where refreshed
handoff trace
completion state
```

A later source change may affect workflow continuation or retry logic.

Navigator must not mutate another institution's canonical state.

---

## Certifier

If a referenced source changes after certification:

```text
observe
store
assess materiality
flag if certification basis may be affected
```

A source update does not automatically change an existing Certification Package.

Certifier determines whether recertification, correction, new version, or new certification identity is required.

---

## Registry

Registry should preserve:

```text
source identity
source version
source lifecycle state
source publication state
source reference health
historical source context
```

Registry may refresh Registry metadata.

It must not overwrite the source institution's history or authority.

---

## Chronicle

Chronicle preserves historical truth about what occurred and what source state existed at the relevant time.

Later source changes may themselves become qualifying Occurrences.

Chronicle must not rewrite the earlier Chronicle Entry merely to match current source state.

---

## Anchor

Source lifecycle/publication changes do not automatically imply integrity failure.

Anchor distinguishes:

```text
source semantic/lifecycle change
≠ representation integrity change
```

A new protected representation may require a new Anchor version or new Integrity Reference depending on whether the Integrity Subject changed.

---

## Beacon

Beacon may need to refresh current discovery state when a discovered source changes.

If the later change is materially different from the prior discovery:

```text
new Discovery Signal
→ may be required
```

Beacon must preserve prior Discovery Signals historically.

---

## Attestor

Attestor must preserve the evaluation basis that existed at evaluation time.

If an upstream source changes later:

```text
observe
store later state
compare with evaluation basis
determine materiality
flag where material
reevaluate where rules require
```

A changed conclusion requires a new Trust Statement identity.

A materially changed assertion requires a new Attestation.

---

# 11. Downstream Action Matrix

| Upstream Change | Observe | Store Historical + Current | Refresh Current View | Flag Review | Republish Automatically? | Ignore Permitted? |
|---|---:|---:|---:|---:|---:|---:|
| Active → Superseded | Yes | Yes | Usually | If material | No | Sometimes |
| Active → Withdrawn | Yes | Yes | Usually | Presumptively | No | Rarely |
| Unpublished → Published | When relevant | Yes | Usually | Sometimes | No | Yes |
| New Version | Yes | Yes | Often | If material | No | Yes if immaterial |
| Correction | Yes | Yes | Often | If used materially | No | Only if immaterial |
| Material Replacement | Yes | Yes | Yes | Yes | No, but often requires governed downstream change | No if subject materially changed |

---

# 12. Non-Automatic Propagation Rule

The Suite adopts:

> **SOURCE CHANGE DOES NOT AUTOMATICALLY MUTATE DOWNSTREAM CANONICAL OBJECTS.**

A source change may trigger review.

The receiving institution decides, under its own governance, whether the proper response is:

```text
no action
metadata refresh
new version
correction
supersession
withdrawal
new canonical identity
reevaluation
republication
```

This preserves institutional independence.

---

# 13. Historical-State Preservation Rule

Every downstream object that depends materially on source state should preserve enough information to reconstruct:

```text
which source object
which version
which lifecycle state
which publication state
when observed
how obtained
what relationship applied
what authority applied
```

Later state should be added as later state.

It must not overwrite the historical basis.

---

# 14. Current-State Refresh Rule

Current-facing surfaces may be refreshed to reflect latest source state.

Examples:

```text
catalog display
discovery presentation
workflow dashboard
reference-health report
current source-status panel
```

But:

> **REFRESHING CURRENT DISPLAY ≠ REWRITING HISTORICAL RECORD.**

---

# 15. Republishing Rule

Republishing is governed by the receiving institution.

Source change alone does not create an automatic republication obligation.

Republishing is appropriate only where:

```text
receiving object changed
receiving representation changed materially
receiving institution's publication rules require a new release
```

---

# 16. Flagging Rule

A downstream review flag should be raised where source change may affect:

```text
authority context
operative standing
evaluation basis
certification basis
registered source representation
discovery relevance
historical interpretation
integrity subject
workflow outcome
```

A flag is a review condition.

It is not:

```text
FAIL
INVALID
WITHDRAWN
SUPERSEDED
UNSUPPORTED
```

unless the receiving institution later makes that determination.

---

# 17. Unknown / Unavailable State Propagation

If the consuming institution cannot determine the source's current state:

```text
current state → unknown / unavailable
```

The prior known state remains historical evidence.

The consumer must not infer:

```text
still active
still published
still valid
still supported
```

without current evidence.

> **UNKNOWN ≠ SUCCESS**

---

# 18. Findings

## LPP-01 — Historical state vs current state

**APPROVED**

Every materially used source reference must preserve state-at-use separately from later state.

---

## LPP-02 — Active → Superseded

**APPROVED**

Observe, store, refresh where current-facing, and flag where operative standing matters.

Do not mutate history.

---

## LPP-03 — Active → Withdrawn

**APPROVED**

Treat as significant, preserve prior state, refresh current state, and presumptively flag downstream review.

---

## LPP-04 — Unpublished → Published

**APPROVED**

Publication change may update accessibility metadata without changing lifecycle or authority.

---

## LPP-05 — New Version

**APPROVED**

Store version lineage; flag only where material; do not equate version creation with activation/publication.

---

## LPP-06 — Correction

**APPROVED**

Preserve prior state and correction lineage; review downstream impact if corrected matter was material.

---

## LPP-07 — Material Replacement

**APPROVED**

Preserve old/new identities and governed relationship; require downstream review; new receiving identity may be required under institution-specific rules.

---

## LPP-08 — Automatic propagation

**REJECTED**

Source-state change must not automatically mutate downstream canonical objects.

---

## LPP-09 — Current display refresh

**APPROVED**

Current-facing representations may refresh without rewriting historical source state.

---

## LPP-10 — Republishing

**APPROVED AS RECEIVING-INSTITUTION DECISION**

No universal auto-republish rule is adopted.

---

# Review Determination

The Suite can propagate lifecycle and publication-state changes without collapsing institutional independence.

The correct interoperability model is:

```text
Observe Source Change
        ↓
Preserve Historical State-at-Use
        ↓
Record Current Source State
        ↓
Classify Materiality
        ↓
Receiving Institution Decides Action
```

Possible actions:

```text
ignore
store
refresh
flag
review
reevaluate
version
correct
supersede
republish
create new canonical object
```

No source-state change silently determines the downstream action.

No architecture conflict was identified.

---

# FINAL DISPOSITION

# LIFECYCLE & PUBLICATION-STATE PROPAGATION REVIEW — COMPLETE — APPROVED

Governing distinctions:

> **CANONICAL CREATION ≠ LIFECYCLE ACTIVATION ≠ PUBLICATION**

> **SOURCE STATE AT USE ≠ LATER SOURCE STATE**

> **SOURCE CHANGE DOES NOT AUTOMATICALLY MUTATE DOWNSTREAM CANONICAL OBJECTS.**

The Suite should preserve historical source-state snapshots, detect later changes, and allow each receiving institution to determine the governed downstream consequence.
