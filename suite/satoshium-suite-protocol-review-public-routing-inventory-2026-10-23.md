# Satoshium Suite — First-Level Public Routing Inventory

**Date:** October 23, 2026  
**Branch:** `phase004`  
**Classification:** CONFIRM — PASS (scoped repository-level link inventory)  
**Protocol Review:** ACTIVE  
**Governance baseline:** September 30, 2026 Suite Reconciliation; October 11, 2026 Suite Governance Review (`GDR-2026-0026`)

## Purpose and scope

Record a bounded, reproducible inventory of the **first-level institutional and Suite public entry pages** in the repository. This checks internal **root-relative HTML `href`** destinations against the Git tree; it does **not** assert live hosting, link behavior, or operational implementation.

The nine institutional/Suite homepage pages were separately reviewed for root-relative navigation links in this Protocol Review. The present inventory concentrates on `<institution>/<section>/index.html` and `suite/<section>/index.html`.

## Inventory — first-level `index.html` pages

| Repository area | Pages checked | Unresolved root-relative href paths |
|---|---:|---:|
| Atlas | 4 | 0 |
| Navigator | 20 | 0 |
| Certifier | 19 | 0 |
| Registry | 29 | 0 |
| Chronicle | 29 | 0 |
| Anchor | 29 | 0 |
| Beacon | 28 | 0 |
| Attestor | 36 | 0 |
| Suite | 6 | 0 |
| **Total** | **200** | **0** |

**Method:** Fetch the live `phase004` branch tree, confirm that the recursive listing is not truncated, fetch each listed first-level `index.html` page, extract literal root-relative HTML `href` targets, and test that each destination exists as a repository file or has a corresponding `index.html` / `index.htm` entry point. Common shared `/assets/` paths are excluded from this page-routing test.

## Identified and corrected entry point

The Suite homepage linked to `/suite/governance/`, but the Governance directory originally contained only governance records. The repository now has:

- `suite/governance/index.html` — public navigation surface for the **Suite Governance Model**, not the distinct Standards Governance framework.
- `suite/governance/README.md` — documents the controlling model, decision register, institutional boundaries, and required live route check.

**Verified correction commit:** `2ac5dabcce9078a17d692ab09859139bc8a7137a`.

No governance model, GDR, institutional role, canonical object, or authority boundary was changed.

## Explicit exclusions and outstanding checks

A repository `href` target resolving to an existing file is **not proof** of a successful deployed public route.

This pass does **not** test:

- live HTTPS response codes, redirects, or hosting rewrites;
- JavaScript-generated, fragment-only, query-dependent, or relative navigation;
- cross-site links, external URLs, dynamic APIs, or client-side `fetch` resources;
- links and entry points in nested second-level-or-deeper production, evidence, toolkit, schema, or archive directories;
- accessibility, browser functionality, content accuracy, and canonical URL correctness across the site.

Missing `index.html` in an evidence, schema, toolkit, or archive directory is not itself a broken public route without an intended public link and a defined public-entry requirement.

**Deployment remains OPEN** for the Attestor Generation and Publication routes and for the newly created Suite Governance landing page until their live responses are independently tested.

## Disposition

**First-level public `href` repository destinations: CONFIRM — PASS (200 / 200 pages checked; 0 unresolved root-relative targets).**

**Suite Governance repository entry point: RESOLVED — VERIFIED.**

**Live deployment / deeper link verification: OPEN — OUTSIDE THIS BOUNDED PASS.**

**Architectural CHANGE: NONE.**

> **Authority follows the governed subject. Reference does not transfer authority.**

This review inventories the architecture that exists. It does not redesign it.
