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

**Post-Foundational Architecture · Pre-Production Reconciled**

The initial production procedure set is now defined, including formal staged Validation.

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

The first production Integrity Reference should be used to test and refine these procedures.

**Version:** 1.0-draft

**Maintained By:** Satoshium
