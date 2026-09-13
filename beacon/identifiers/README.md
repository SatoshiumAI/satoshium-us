# Satoshium Beacon — Beacon Identifier Standard

**Path:** `/beacon/identifiers/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Identifier:** `BEAC-2026-0001`

## Canonical Identifier

Beacon-owned Discovery Signals use:

```text
BEAC-YYYY-NNNN
```

Components:

- `BEAC` — Satoshium Beacon institutional prefix
- `YYYY` — four-digit canonical creation year
- `NNNN` — zero-padded annual sequence

Conceptual conformance pattern:

```text
^BEAC-[0-9]{4}-[0-9]{4}$
```

## Assignment Point

The permanent identifier is assigned when the canonical Discovery Signal is **Created**.

```text
Identified → no permanent BEAC identifier required
Created → permanent BEAC identifier assigned
Draft → canonical object exists
```

Creation does not mean validated, Active, or Published.

## Permanence

Once assigned, the identifier:

- does not change with publication
- does not change with lifecycle transition
- does not change with version
- is never reused
- remains attached to the historical object after supersession, resolution, or withdrawal

Version, Signal Type, lifecycle, and publication state are separate governed fields and are not encoded in the identifier.

## First Production Identifier

`BEAC-2026-0001` was assigned at canonical Creation on:

**September 13, 2026 · 9:01:57 AM PDT**

Initial state:

- Lifecycle: Draft
- Publication: Unpublished
- Version: 1.0

Current state:

- Lifecycle: Active
- Publication: Published
- Version: 1.0

Public Beacon Record:

```text
/beacon/records/BEAC-2026-0001/
```

The Beacon Record is the public representation of the Discovery Signal, not a separate canonical object type.

## Suite Identifier Context

```text
Certifier → SC-CERT-2026-0001
Registry → SREG-2026-0001
Chronicle → CHR-2026-0001
Anchor → ANCH-2026-0001
Beacon → BEAC-2026-0001
```

These identifiers remain institution-specific. Reference does not merge their canonical objects.

## Remaining Open Implementation Details

Institutional identifier meaning and use are established and production-exercised. Remaining intentionally open matters include:

- frozen machine-schema enforcement
- automated sequence assignment
- automated collision prevention
- future ledger/service mechanism for issued identifiers
- API behavior
- exact machine version-reference syntax

## Current Status

```text
Beacon Status → Operational · September 2026
Identifier Standard → Defined and production-exercised
Canonical Prefix → BEAC
Canonical Pattern → BEAC-YYYY-NNNN
Assignment Point → Canonical Creation
First Production Identifier → BEAC-2026-0001
Public Routing → Exercised
Frozen Machine-Schema Enforcement → Not yet adopted
```

## Governing Principle

**Identity should remain stable even when everything around it changes.**
