# Satoshium Anchor — Integrity Reference Lifecycle

**Path:** `/anchor/lifecycle/`  
**Institution:** Satoshium Anchor  
**Institutional Role:** Integrity Preservation  
**Canonical Object:** Integrity Reference  
**Status:** Operational  
**Review Alignment:** October 23, 2026

## Purpose

This directory documents the governed **Lifecycle State of the Integrity Reference**, as presented in `index.html`. Lifecycle describes Anchor's institutional treatment of its own canonical Integrity Reference, not the lifecycle of the external Source Artifact, public visibility, Integrity State, or a Verification Result.

## Initial Lifecycle State Vocabulary

The currently documented initial governed tokens are:

- `draft` — under construction, before active institutional use;
- `active` — current active Anchor record for its governed integrity subject;
- `superseded` — replaced for current use by a later Integrity Reference while preserved historically;
- `withdrawn` — removed from normal active use without erasure of prior identity;
- `archived` — retained primarily for historical, evidentiary, or institutional continuity.

These five tokens are described by the current public `index.html` as the initial frozen Lifecycle State set. Do not interpret this as a statement that every conceivable transition, restoration path, or future extension is implemented.

## Separation of Institutional Dimensions

```text
Source Artifact Lifecycle ≠ Anchor Integrity Reference Lifecycle
Anchor Lifecycle State ≠ Publication State
Anchor Lifecycle State ≠ Integrity State
Anchor Lifecycle State ≠ Verification Result
Anchor Version ≠ Lifecycle State
```

A source may be withdrawn or superseded without automatically erasing the existing Integrity Reference. A Verification mismatch does not itself decide institutional lifecycle. Publication and lifecycle are independently governed. An Integrity Reference's historical identity, provenance, versions, corrections, relationships, and Verification history are preserved according to applicable Anchor rules.

## Governed Transitions and History

The current public lifecycle model discusses progression from `draft` to `active`, and potential later `superseded`, `withdrawn`, or `archived` conditions. Transitions are governed events rather than an unconditional universal chain. Reversal to active use should not be inferred or performed silently.

Lifecycle history should preserve the prior state, new state, reason, effective time, and related governing context, consistent with the applicable operational procedure.

## Verification Is Separate

Integrity **Verification** belongs to `/anchor/verification/`. It assesses whether a reviewed representation matches the integrity evidence preserved by an Integrity Reference; it is not Anchor's lifecycle specification.

The preceding content of this README was a draft-era **Integrity Verification** document mistakenly situated in the Lifecycle directory. Its original text is preserved without alteration as `README-verification-historical-2026-10-23.md` for traceability. This replacement corrects directory documentation against the existing lifecycle public page; it does not redesign the architecture.

## Current Operational Evidence

Anchor is Operational, and `ANCH-2026-0001` is its first published production Integrity Reference, as described in `/anchor/status/README.md`. A source-level description here does not independently demonstrate deployed HTTPS behavior.

> **Authority follows the governed subject. Reference does not transfer authority.**
