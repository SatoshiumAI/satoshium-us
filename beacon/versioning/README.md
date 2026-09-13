# Satoshium Beacon — Versioning & Supersession

**Path:** `/beacon/versioning/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Signal:** `BEAC-2026-0001`

## Governing Principles

> **Discovery changes. History must not.**

> **Preserve the observation. Preserve the change. Preserve which representation is current.**

## Identity and Version

Canonical identity and version are separate:

```text
Canonical Identifier → BEAC-2026-0001
Version → governed revision of BEAC-2026-0001
```

The BEAC identifier remains stable across versions of the same Discovery Signal.

A new BEAC identifier is used when the later discovery is institutionally distinct rather than merely a revision.

## State Change vs. Version Change

Lifecycle and Publication changes do not automatically create a new version.

The first production signal demonstrates this:

```text
BEAC-2026-0001 · Version 1.0
Draft → Active
Unpublished → Published

Current Version → 1.0
```

Those were governed state transitions, not material revisions of the Discovery Signal representation.

## New Version

A new version is appropriate when the same canonical Discovery Signal changes materially, such as through:

- materially corrected or expanded Discovery Metadata
- materially corrected or expanded provenance
- corrected canonical reference
- changed relationship representation
- later observation that materially updates the same canonical discovery context

## New Discovery Signal

A new BEAC identifier is appropriate for:

- a new discovery subject
- a new independent occurrence
- a materially different discovered relationship
- a distinct observation requiring its own canonical record
- a different institutional discovery requiring independent lifecycle

## Supersession

Version supersession and signal supersession are distinct.

```text
Version supersession:
BEAC-2026-0001 v1
→ superseded by
BEAC-2026-0001 v2
```

```text
Signal supersession:
BEAC-2026-0001
→ superseded by
BEAC-2026-0002
```

`Resolved ≠ Superseded`

`Withdrawn ≠ Superseded`

`Correction ≠ Update`

## First Production Version

`BEAC-2026-0001` established Beacon's first governed version baseline.

```text
Canonical Identifier → BEAC-2026-0001
Initial Governed Version → 1.0
Created → September 13, 2026 · 9:01:57 AM PDT
Initial Lifecycle → Draft
Initial Publication → Unpublished
Current Lifecycle → Active
Current Publication → Published
Current Version → 1.0
Version Supersession → None
Signal Supersession → None
```

The first production operation did not require a later revision or supersession.

## Source Changes

A source change creates a later observation. It does not rewrite the earlier observation.

Beacon versions only its own Discovery Signal. Referenced institutions retain authority over their own objects and status changes.

> **Reference does not transfer authority.**

## No Silent Overwrite

Material institutional content must not be silently replaced in place.

Preserve:

- prior representation
- reason for change
- supporting provenance
- relevant timestamps
- current representation
- supersession relationship when applicable

## Remaining Open Implementation Details

The institutional Versioning & Supersession architecture is defined and production-exercised at the initial Version 1.0 baseline. Remaining intentionally open matters include:

- exact frozen version notation rules beyond the current `1.0` baseline
- machine-readable version property names
- machine-enforced materiality thresholds
- controlled change-reason vocabulary
- technical tracking of minor editorial revisions
- formal current-version pointer mechanics
- detailed version-publication rules
- correction-notice format
- supersession effective-time rules
- Signal Type-specific rules requiring a new BEAC identifier

## Current Status

```text
Beacon Status → Operational · September 2026
Versioning & Supersession → Defined and production-exercised
First Production Discovery Signal → BEAC-2026-0001
Current Version → 1.0
Current Lifecycle → Active
Current Publication → Published
Version Supersession → None
Signal Supersession → None
Publication Model → Defined and production-exercised
Future Version / Supersession Event → Not yet required
```
