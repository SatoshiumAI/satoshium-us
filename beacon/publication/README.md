# Satoshium Beacon — Publication Model

**Path:** `/beacon/publication/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Published Signal:** `BEAC-2026-0001`

## Governing Principle

> **Publication makes discovery public. It does not make discovery authoritative beyond Beacon's own institutional role.**

Canonical existence, Validation, lifecycle state, and Publication are separate institutional dimensions.

## Publication Sequence

```text
Candidate Discovery Identified
→ Discovery Signal Created
→ BEAC Identifier Assigned
→ Draft / Unpublished
→ Review & Validation
→ Active / Unpublished
→ Publication Decision
→ Active / Published
```

Publication does not create the canonical Discovery Signal. The signal exists before public release.

## Publication State

```text
Unpublished
Published
```

Publication State remains separate from Lifecycle State:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

## Publication Eligibility

Publication eligibility requires:

- canonical identity
- conforming BEAC identifier
- required Entry Model components
- applicable Validation passed
- lifecycle state permitting publication
- sufficient public provenance
- preserved authority boundaries
- attributable references and relationships
- no governing restriction preventing release

Eligibility permits a publication decision. It does not itself publish the signal.

## Beacon Records

Published Discovery Signals are surfaced through:

```text
/beacon/records/
```

This is **Beacon Records**, the human-facing index of published Discovery Signals.

An individual published signal is represented through:

```text
/beacon/records/BEAC-2026-0001/
```

A **Beacon Record** is the public representation of a Discovery Signal. It is not a separate canonical object type.

## First Production Publication

`BEAC-2026-0001` completed Beacon's first governed publication.

```text
Canonical Object → BEAC-2026-0001
Lifecycle Before Publication → Active
Publication Before Decision → Unpublished
Validation Outcome → VALID
Review Outcome → APPROVED TO PROCEED
Publication Eligibility → PASS
Publication Decision → APPROVED
Current Lifecycle → Active
Current Publication → Published
Version → 1.0
Publication Date → September 13, 2026
Public Record → /beacon/records/BEAC-2026-0001/
Beacon Records Listing → Published
```

The exact publication clock time is not asserted because it was not preserved in the available production record. The known canonical Creation time is separate and must not be substituted for `published_at`.

## Public Representation

A published Beacon Record normally exposes sufficient information to identify, understand, attribute, and trace the Discovery Signal, including its:

- BEAC identifier
- subject
- Signal Type
- lifecycle state
- publication state
- current version
- discovery statement or summary
- source identity
- publishable provenance
- canonical references
- publishable relationships
- relevant timestamps
- later supersession or resolution information when applicable

## No Silent Unpublication

A later institutional change should not silently erase the historical fact of publication. Supersession, resolution, withdrawal, and correction should preserve reviewable history where governance permits.

## Remaining Open Implementation Details

The institutional Publication Model and first governed publication are complete. Remaining intentionally open matters include:

- future formalization or automation of publication-approval roles and mechanisms
- machine-readable publication property names
- formal publication-basis vocabulary
- public provenance minimum refinements by Signal Type
- restriction classifications
- withdrawal-display mechanics
- correction-notice format
- historical-version public navigation
- public indexing behavior for Superseded / Resolved / Withdrawn signals
- whether any valid future Signal Types are non-public by default

## Authority Boundary

Publication exposes Beacon's Discovery Signal. It does not replace the source object or transfer its authority.

> **Reference does not transfer authority.**

## Current Status

```text
Beacon Status → Operational · September 2026
Publication Model → Defined and production-exercised
First Publication Decision → APPROVED
First Published Discovery Signal → BEAC-2026-0001
Lifecycle → Active
Publication → Published
Version → 1.0
Publication Date → September 13, 2026
Beacon Records → Operational public index
Individual Beacon Record → Published
Exact Published-At Clock Time → Not recorded
```
