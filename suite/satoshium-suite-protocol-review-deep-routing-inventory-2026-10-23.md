# Satoshium Suite — Deeper Public Routing Inventory (Bounded Pass)

**Date:** October 23, 2026  
**Branch:** `phase004`  
**Current routing-inventory status (October 23 follow-up):** COMPLETE — APPROVED (defined repository-level nested index.html scope)  
**Initial bounded pass:** 84 pages; historically partial — preserved below  
**Disposition for checked pages:** CONFIRM — PASS (repository-level link resolution only)  
**Governance baseline:** Suite Reconciliation, September 30, 2026; Suite Governance Model, October 11, 2026 (`GDR-2026-0026`).

## Purpose

Extend the already-approved 200-page first-level repository link inventory into nested public record, standard, methodology, Atlas jurisdiction, and Atlas orientation pages.

The review checks literal HTML `href` destinations against the complete, untruncated `phase004` Git tree. It is **not** a live deployment, browser, execution, or comprehensive link certification.

## Coverage actually completed

| Nested page class | Pages checked | Unresolved root-relative repository destinations |
|---|---:|---:|
| Published production and institutional profile pages — Certifier, Registry, Chronicle, Anchor, Beacon, Attestor | 11 | 0 |
| Nested Suite methodology and standards | 17 | 0 |
| Atlas nested jurisdiction, certification, and orientation pages — bounded samples | 56 | 0 |
| **Total** | **84** | **0** |

Of the 218 deeper Atlas `index.html` files enumerated, **56** have been checked. The **remaining 162 Atlas pages have not been checked** in this unit. Atlas sampled ranges comprised the first 42 paths in lexicographic tree order, plus 7 around the U.S. jurisdiction section and 7 from the global orientation section. This is non-random sampling and does not support a claim about every remaining Atlas page.

## Additional relative-link check for published institutional pages

The 11 published institutional record/profile pages contained **213 `href` occurrences** divided into:

- 113 root-relative links;
- 5 relative links;
- 95 external HTTP(S) links.

The five relative links resolved to repository paths that exist. External HTTP(S) destination status was **not tested**.

## Bounded method

1. Fetch the current `phase004` branch and its recursive Git tree; require `truncated=false`.
2. Select nested `index.html` files by exact repository paths.
3. Fetch each selected page and extract literal root-relative `href` values.
4. Test each against a Git tree file, or corresponding directory `index.html` / `index.htm`.
5. For published record/profile pages, additionally resolve ordinary relative `href` paths against their parent directory and test repository existence.
6. Report failures rather than assuming redirects, hosting rewrites, or dynamic behavior.

Shared `/assets/` resource paths were excluded from the page-route check.

## Limitations / remaining gates

**OPEN — COVERAGE:** 162 Atlas deep-page entry files remain, together with other non-`index.html` public files and deeper linked content not included here. A full static-link audit would also check query strings, fragment targets, relative links everywhere, canonical URL tags, static images/scripts/assets, case sensitivity, and percent-encoding behaviors.

**OPEN — DEPLOYMENT VERIFICATION:** Serving of `/attestor/generation/`, `/attestor/publication/`, and `/suite/governance/` requires live HTTPS/redirect/content checks. Repository existence is not deployment proof.

**OPEN — EXTERNAL DESTINATIONS:** No external websites or API endpoints were tested in this pass.

**NOT AN ARCHITECTURAL CHANGE:** Nothing in this inventory transfers institution-owned canonical authority or establishes a universal mandatory cross-Suite workflow.

## Disposition

**84 nested public pages: CONFIRM — PASS for scoped repository destination existence.**

**Overall deeper routing inventory: ACTIVE — PARTIAL COVERAGE, not COMPLETE.**

**Code or public-page correction required in this bounded pass:** None.

**Architectural CHANGE required:** None.

> Authority follows the governed subject. Reference does not transfer authority.

---

## October 23, 2026 follow-up — Outstanding Atlas coverage closed

**Disposition:** COMPLETE — APPROVED for the defined nested public `index.html` **repository root-relative href destination** inventory. The initial 84-page bounded pass above is preserved as the historical first stage and was **not** a complete result when issued.

All **162 Atlas nested pages** that were previously outstanding have now been fetched and checked against the untruncated `phase004` Git tree at `de1fb7ee988bd2a5c50fc738d5578a52279b4267`.

### Consolidated current coverage

| Nested page class | Initial pages | Additional pages | Total checked | Unresolved root-relative repository destinations |
|---|---:|---:|---:|---:|
| Published institutional production/profile pages | 11 | 0 | 11 | 0 |
| Nested Suite methodology and standards pages | 17 | 0 | 17 | 0 |
| Atlas nested jurisdiction, certification, and orientation pages | 56 | 162 | 218 | 0 |
| **Total** | **84** | **162** | **246** | **0** |

The initial Atlas set covered path indices 0–41, 60–66, and 155–161 in the 218-file lexicographic nested-Atlas `index.html` set. The continuation covered indices 42–59, 67–154, and 162–217. These disjoint sets cover every enumerated nested Atlas page (218/218).

**Current disposition:** first-level repository `href` inventory: 200/200 PASS (separate record); this deeper nested `index.html` inventory: 246/246 PASS. No additional HTML correction or architectural change was required to close the remaining Atlas coverage.

### Still outside this certification

Repository destination existence is not deployed HTTP/HTTPS verification. The exclusions above remain in force: live serving, redirects, external URLs, CSS/JavaScript/assets, dynamically generated links, untested relative references outside the five checked institutional-record links, fragments, browser behavior, and non-`index.html` public files. In particular, the Attestor Generation, Attestor Publication, and Suite Governance deployed URLs remain **OPEN — DEPLOYMENT VERIFICATION**.

**Suite Protocol Review as a whole remains ACTIVE**; completion of this scoped routing inventory does not resolve unrelated executable interoperability, implementation, or deployment gates.

> Authority follows the governed subject. Reference does not transfer authority.
