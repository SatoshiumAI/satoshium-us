# Satoshium Beacon — Discovery Signal Lifecycle

**Path:** `/beacon/lifecycle/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Signal:** `BEAC-2026-0001`

## Purpose

The Discovery Signal Lifecycle defines the governed institutional states and transitions of a Beacon-owned Discovery Signal.

It distinguishes:

- pre-object discovery conditions
- canonical creation events
- review and validation processes
- lifecycle states
- publication state
- update and supersession actions

## Canonical Lifecycle

```text
Draft
→ Active
→ Superseded / Resolved / Withdrawn
```

Publication is separate:

```text
Unpublished / Published
```

`Identified` is a pre-object condition.

`Created` is the event that brings the canonical Discovery Signal into existence.

`Reviewed` is a process/event.

`Updated` is an action rather than a durable lifecycle state.

## Identifier Assignment

A permanent Beacon identifier is assigned at canonical Creation.

The object therefore enters its lifecycle as:

```text
BEAC identifier assigned
→ Draft
→ Unpublished
```

Creation does not mean validated, Active, or Published.

## First Production Lifecycle

`BEAC-2026-0001` exercised the lifecycle architecture on September 13, 2026.

```text
Candidate Discovery Identified
→ Canonical Discovery Signal Created
→ BEAC-2026-0001 assigned
→ Draft / Unpublished
→ Validation: Valid
→ Review: Approved to Proceed
→ Draft → Active
→ Publication Approved
→ Active / Published
```

Canonical creation occurred at:

**September 13, 2026 · 9:01:57 AM PDT**

Current state:

- Lifecycle: Active
- Publication: Published
- Version: 1.0

## Authority Boundary

A Beacon lifecycle transition changes only the institutional condition of the Beacon Discovery Signal.

```text
Beacon lifecycle change ≠ source lifecycle change
Beacon resolution ≠ source resolution
Beacon withdrawal ≠ source withdrawal
```

> **Reference does not transfer authority.**

## Remaining Open Implementation Details

The institutional lifecycle is defined and production-exercised. Remaining intentionally open matters include:

- exact machine-readable lifecycle serialization
- frozen schema constraints
- exact machine transition predicates
- future evidence refinements
- whether production ever demonstrates a distinct need for an Archived lifecycle state

## Current Status

```text
Beacon Status → Operational · September 2026
Lifecycle Architecture → Defined and production-exercised
Lifecycle States → Draft · Active · Superseded · Resolved · Withdrawn
Publication Dimension → Unpublished · Published
Identifier Assignment → At canonical Creation
Production Transition → Draft → Active exercised
First Production Discovery Signal → BEAC-2026-0001 · Active · Published
```

## Governing Principle

**Preserve the state. Preserve the transition. Preserve the reason.**
