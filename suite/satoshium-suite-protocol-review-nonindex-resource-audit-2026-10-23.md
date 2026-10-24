# Satoshium Suite — Non-Index HTML Literal Resource Review

**Date:** October 23, 2026  
**Branch:** `phase004`  
**Scope:** The 11 non-`/index.html` `.html`, `.htm`, `.js` candidates recorded in the companion non-index inventory.  
**Disposition:** **COMPLETE — APPROVED (bounded literal static `href`/`src` inspection and correction)**; deeper code/served-content checks remain OPEN.  
**Protocol Review:** ACTIVE.

## Verification and corrections

The complete tree at pre-correction HEAD `d768984dd1e5265a963358526fa44a0af274fa97` reported `truncated=false`. Inspected all 11 candidates individually at this fixed commit, including 9 `.html`, 1 `.htm`, 1 `.js`. The eight pages listed below carried two absent repository-local optional icon fallbacks each, despite correctly including `/assets/favicon.svg`:

1. `anchor/anchored-items/ANCH-2026-0001/canonical-index.html`
2. `atlas/corridors/corridor-assignment-matrix.html`
3. `atlas/docs/framework/federal-overlay-model.html`
4. `atlas/docs/framework/global-adjacency-model.html`
5. `atlas/docs/framework/signals-update-protocol.html`
6. `attestor/publication/index.htm`
7. `index.html` (repository-root homepage)
8. `registry/registered-items/SREG-2026-0001/registry-entry.html`

The correction removed precisely **16** absent fallback references, preserved all 8 valid SVG favicon tags and otherwise preserved page semantics. **Correction commit:** `68e7027394f40010531641a34d39a15e5e76cb67`. Independently re-fetched all **11** candidates from that correction commit: the eight fixed HTML pages have **zero** obsolete local fallback icon tags and retain valid SVG links. The other 3 candidates were not changed.

All local literal `href`/`src` paths outside the corrected icon fallbacks resolved to repository files or directory indexes when checked against the complete tree, treating the site-root `/` as repository `index.html`. Absolute HTTPS references were excluded from repository-local resolution, including links to the project's own hostname; they require distinct deployed verification. `components/topbar-loader.js` contains runtime-generated navigation and needs semantic/runtime checking beyond literal HTML attribute inspection. The toolkit fixture has no literal `href`/`src` attributes.

## Follow-up findings explicitly NOT silently fixed

- **Homepage ID correction:** Source review determined that `main-content` occurs once in an actual HTML element and once in a comment; it was not a duplicate element ID. The original HTML did have two actual `heading-why` IDs. The first (`Satoshium Suite`) was preserved and the second (`Why This Layer Exists`) was changed to `heading-why-this-layer` in a narrowly bounded follow-up; see subsequent correction commit history. The new ID is unique within the page.
- **Atlas `atlas/media/orientation/us/states/temp.html`:** favicon URLs point to absolute `https://satoshium.info/assets/...` paths, not repository-local paths. Public purpose, deployment status and those external asset responses are unverified. Do not assume the path is a currently published page or that external assets fail.
- **Attestor `publication/index.htm`:** coexistence with `publication/index.html` is confirmed, but live index precedence is not demonstrated by the Git tree.
- **External absolute HTTPS references, CSS `url(...)`, JavaScript-computed paths, dynamic DOM, browser performance, live routing and response status** remain outside this bounded static literal attribute audit. The topbar loader's generated targets need an explicit separate check.

**Next:** assess script-generated navigation as bounded follow-ups; retain Atlas Media canonical conflicts and four deployed route verifications as OPEN. Keep all eight Suite institutions Operational and their approved canonical boundaries unchanged.

> Authority follows the governed subject. Reference does not transfer authority.
