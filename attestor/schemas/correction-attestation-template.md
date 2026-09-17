# Correction Attestation Template — Foundational Candidate Profile

## Purpose
This document preserves the June concept for documenting a correction to an Attestor-owned Attestation while reconciling it with the current Corrections architecture.

The foundational architecture has **not yet decided** whether correction is:
- an Attestation Type;
- a lifecycle/versioning operation;
- a governed change profile/object;
- or a combination of these.

Accordingly, this is a candidate structural profile, not an adopted object class.

## Foundational Principle
**Attestor corrects Attestor-owned objects.**

A correction must not be used to modify the canonical object of another Suite institution.

## Candidate Structural Concepts
```yaml
change_identifier:
change_type:
status:

target_attestation:
responsible_authority:
subject:

change_summary:
prior_assertion:
revised_assertion:
reason:

evidence_references:
source_references:
governed_references:
provenance:

change_date:
effective_date:

limitations:
notes:
```

Exact field names are provisional.

## Historical Preservation
A governed correction should preserve enough information to distinguish:

`Prior State → Governed Change → Current State`

The prior state should remain traceable rather than silently overwritten.

## Candidate Change Semantics
The June template proposed concepts such as:
- administrative correction;
- clarification;
- amendment;
- evidence update;
- attribution update;
- historical update;
- retraction.

These remain candidate semantics, not adopted controlled values.

## Authority Boundary
If the underlying problem belongs to Registry, Chronicle, Certifier, Anchor, Beacon, Atlas, Navigator, or another source authority, that institution must govern its own correction.

Attestor may subsequently review whether its own Attestation or Trust Statement requires governed change.

## Deferred
Advanced architecture must determine:
- correction object model;
- identifier model;
- lifecycle states;
- supersession;
- withdrawal/retraction semantics;
- effective-time rules;
- provenance requirements;
- validation;
- Trust Statement correction relationships.

## Status
Foundational candidate profile only.
