# Satoshium Suite — Non-Index HTML and Script Coverage Inventory

**Date:** October 23, 2026  
**Branch:** `phase004`  
**Fixed tree:** `2dbae138740f90d55e551a93a54d37b32834ebc8` (complete; `truncated=false`)  
**Status:** INVENTORY COMPLETE — REVIEW OF EXECUTABLE / NON-INDEX CONTENT OPEN  
**Suite Protocol Review:** ACTIVE

## Population

Of 2,517 blob paths, **11** match the bounded inventory predicate: extension `.html`, `.htm`, or `.js`, excluding paths ending in `/index.html`. This deliberately includes the repository-root `index.html` (which does not end in `/index.html`) and makes **no deployment/public exposure assertion**. No `.css` paths matched this population. Counts: **9 HTML**, **1 HTM**, **1 JS**.

## Exact candidate paths

| Path | Review classification (preliminary, by directory only) |
|---|---|
| `anchor/anchored-items/ANCH-2026-0001/canonical-index.html` | Object-specific HTML |
| `atlas/corridors/corridor-assignment-matrix.html` | Atlas reference HTML |
| `atlas/docs/framework/federal-overlay-model.html` | Atlas framework documentation HTML |
| `atlas/docs/framework/global-adjacency-model.html` | Atlas framework documentation HTML |
| `atlas/docs/framework/signals-update-protocol.html` | Atlas framework documentation HTML |
| `atlas/media/orientation/us/states/temp.html` | Atlas temporary-looking path — exposure/intention unknown |
| `attestor/publication/index.htm` | Legacy alternate publication entry point |
| `certifier/tools/ops-toolkit/tests/fixtures/complete-certification/scrd.html` | Toolkit test fixture; not assumed deployed |
| `components/topbar-loader.js` | Script-generated navigation/resource candidate |
| `index.html` | Repository-root homepage |
| `registry/registered-items/SREG-2026-0001/registry-entry.html` | Object-specific HTML |

## Boundaries and next gate

This is a **tree enumeration only**, not an `href`/`src`, CSS `url(...)`, JavaScript navigation or deployed HTTP audit. Do not assume that test fixtures, documentation pages or temporary paths constitute public release claims. Next inspect source semantics and actual static references for the intended public subset; independently classify any issues before small corrections. Preserve the existing 223-page Atlas and 24-page Suite static-index closures, the canonical/deployment open findings and all institutional authority boundaries.

> Authority follows the governed subject. Reference does not transfer authority.
