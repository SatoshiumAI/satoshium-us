# Procedures

## Overview

The Satoshium Anchor **Production Procedures** translate Anchor architecture into executable institutional workflows.

The public route:

```text
/anchor/procedures/
```

serves as the institutional landing page.

Individual procedures are maintained as governed Markdown artifacts rather than separate public HTML pages unless future operational need proves otherwise.

---

## Current Procedures

```text
Integrity Reference Production Procedure
Integrity Reference Validation Procedure
Integrity Verification Procedure
Correction Procedure
Publication Procedure
Maintenance Procedure
```

Files:

```text
integrity-reference-production-procedure.md
integrity-reference-validation-procedure.md
integrity-verification-procedure.md
correction-procedure.md
publication-procedure.md
maintenance-procedure.md
```

---

## Procedure Architecture

The procedures form an operational sequence:

```text
Integrity Reference Production
        ↓
Stage A — Structural / Institutional Validation
        ↓
Initial Verification
        ↓
Canonical HTML + Canonical JSON
        ↓
Stage B — Publication-Readiness Validation
        ↓
Publication Gate
        ↓
Publication
        ↓
Maintenance
        ↓
Reverification / Correction / Versioning / Lifecycle action as required
```

Corrections may re-enter the workflow:

```text
Correction
        ↓
new Anchor Version
        ↓
Stage A Validation
        ↓
Reverification
        ↓
Stage B Publication-Readiness Validation
        ↓
Publication Gate
        ↓
Publication
```

---

## Authority

Procedures govern Anchor-owned institutional actions.

They do not transfer Source authority.

> Reference does not transfer authority.

---

## Procedure Principle

> Architecture defines what Anchor means. Procedures define what Anchor does.

---

## Status

**Operational · First Production Exercised**

The initial production procedure set, including formal staged Validation, has been exercised in the first published Anchor Integrity Reference, `ANCH-2026-0001`. This production record is bounded to the defined `SCRD-SC-CERT-2026-0001` canonical JSON representation. The production exercise does not imply that all correction, maintenance, extension, or failure paths have been exercised.

The following remain intentionally unfrozen:

```text
operator roles
approval roles
automation permissions
procedure identifiers
procedure execution record identifiers
procedure-specific forms
first-production checklist refinements
Bitcoin-specific procedures
```

The first production Integrity Reference has established an operational precedent. Future cases should continue to test and refine these procedures without changing their authority boundaries or silently expanding the representation covered by an Integrity Reference.

**Version:** 1.0-draft

**Maintained By:** Satoshium
