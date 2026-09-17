# Correction Attestation Template — Foundational Candidate

## Purpose
This candidate template preserves the June correction structure without prematurely establishing **Correction Attestation** as a separate canonical object class.

The foundational architecture has left open whether correction is an Attestation Type, lifecycle/versioning operation, governed-change profile, or some combination.

## Foundational Boundary
**Attestor corrects Attestor-owned objects.**

Attestor does not correct another institution's canonical object.

## Candidate Template
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

## Historical Integrity
`Prior State → Governed Change → Current State`

The prior state should remain traceable rather than silently overwritten.

## Candidate Semantics
Administrative correction, clarification, amendment, evidence update, attribution update, historical update, and retraction remain candidate concepts only.

## Status
Foundational candidate template. The final correction/lifecycle architecture remains Advanced Architecture.
