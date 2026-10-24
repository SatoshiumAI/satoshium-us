# Satoshium Suite — Shared Dynamic Topbar Navigation Source Review

**Date:** October 23, 2026  
**Subject:** `components/topbar-loader.js` and cross-repository navigation templates  
**Satoshium U.S. evidence commit:** `be09d6e48478081533ca853dae3e054046581e60`  
**Satoshium Link evidence commit:** `e5f041cd15ef77de721cd05e1d9361d9ad9d4e68` (branch `phase004`)  
**Disposition:** **COMPLETE — APPROVED (bounded static source/contract inspection)**; live-fetch, browser execution and cross-repository normalization **OPEN**.  
**Overall Suite Protocol Review:** ACTIVE.

## Reviewed assets and selection contract

The U.S. loader checks for `#topbar-slot`; reads its `data-topbar` mode; selects `topbar-universe.html` for `universe`, otherwise `topbar-ai.html`; fetches the selected HTML from `https://satoshium.link/components/`, retrying a GitHub Pages fallback at `https://satoshiumai.github.io/satoshium-link/components/`; then inserts HTML and applies the current-path/hostname active-key class. Both referenced template source files exist in the separate public `SatoshiumAI/satoshium-link` repository on `phase004`. Its default branch is `phase004`, not `main`. The templates use `<nav class="nav">` and matching `data-nav` attributes, consistent with `.topbar .nav a[data-nav="..."]`. Sampled U.S. pages (`/`, Suite, Atlas Corridors, Anchor record and Attestor Publication) specify `data-topbar="universe"`.

## Confirmed source-level observations

1. **Primary/fallback template references exist in GitHub's current source tree.** Their actual live HTTPS responses, redirect behavior, CORS acceptance, CSP compatibility, and DOM rendering were **not independently verified**. Public URL fetch attempts in the available browsing environment returned access errors rather than usable HTTP responses, so no public outage is asserted.
2. **Active-key mismatch (both copies):** the Universe template's Satoshium AI link uses `data-nav="platform"`; both reviewed loader copies call `setActive("main-site")` when hostname is `satoshium.ai` / `www.satoshium.ai`. Thus on a Universe-mode page hosted there, this particular key cannot select the platform anchor. This is a static selector mismatch, not evidence that the destination itself fails.
3. **Version divergence:** U.S. and Link repositories have different `components/topbar-loader.js` implementations. The Link version recognizes `mentor`, `manifesto`, `connect` and `satoshium.games`, while the U.S. version lacks those branches. Consequence depends on which repository's loader is actually served on each hostname, and on each page's topbar mode. Avoid treating version difference alone as a global failure.
4. **Successful primary/fallback rendering remains untested.** The source correctly uses an `ok` check and a sequential fallback. If both requests reject, it logs an error without inserting a replacement navigation; consider a graceful local fallback only after determining shared-component ownership, desired accessibility/availability and tests.
5. **Remote fragment embeds:** retrieved template HTML contains an inline `<style>` block, external anchor destinations and a logo URL. No comprehensive live/CSS/browser audit has been completed; adding HTML with `innerHTML` is not proof that fetched styles render under the deployed site's CSP.

## Recommended next acceptance unit

Coordinate the authoritative shared loader version between the Satoshium Link and U.S. repositories; specifically correct the `main-site` / `platform` mismatch through a narrowly scoped change and verify existing host/mode contracts. Use deterministic unit/DOM tests (Universe mode on each recognized domain, Platform mode on relevant paths, missing `#topbar-slot`, primary fetch success/failure, fallback success/failure, navigation aria/active semantics). Test on deployed HTTPS in a browser where accessible, including CORS, CSP and small-screen rendering, before declaring runtime completion. The source-only inspection itself is **COMPLETE — APPROVED** and does not reopen institutional governance, previously completed HTML literal-resource audits, or production readiness claims.

> Authority follows the governed subject. Reference does not transfer authority.
