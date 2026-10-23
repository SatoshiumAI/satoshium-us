# Satoshium Suite — Registry Public Resource Routing Review

**Date:** October 23, 2026  
**Branch:** `phase004`  
**Disposition:** COMPLETE — APPROVED (bounded local link/asset audit, with separately open FAQ correction)  
**Overall Suite Protocol Review:** ACTIVE

## Scope

All **31** Registry `index.html` entry files were fetched against an untruncated complete Git tree in three batches of 10, 10, and 11. **266** literal local `href`/`src` occurrences (89 + 80 + 97) were checked with normalized directory-index and relative-path existence rules. Fragment-only matches in these attributes: **0**. This is repository-level presence verification, not live HTTPS or executable validation.

## Asset finding and corrections

**56** missing local references were observed (16 + 18 + 22), all to two absent asset files: `/assets/favicon.ico` and `/assets/apple-touch-icon.png`. No other literal local `href`/`src` destination was unresolved within this scope.

The valid `/assets/favicon.svg` reference was preserved on all **28** newly corrected pages. The Registry root page and inaugural SREG production page had been corrected in a previous review unit.

- `c860c17082f3ee47598ad8d99f466c525765b62e` — 8 Registry pages.
- `365d1d7485b4457fb9a6bd466f6622cb6d3d35d7` — 9 Registry pages.
- `31bc535de288433dcf2d47c2acf3dc0967f2c4cd` — 11 Registry pages.

Post-commit re-fetch: **30/30 actual HTML pages** preserve SVG favicon reference and lack the missing fallback references. The remaining `registry/faq/index.html` contains Markdown rather than HTML and has no HTML head or icon links; it is excluded from the 30-page HTML icon-tag conformance result.

## Separate, verified finding — Registry FAQ content mismatch

**Classification:** CORRECT — OPEN; content/format defect requiring a separate bounded correction.

`registry/faq/index.html` starts with Markdown `# Frequently Asked Questions (FAQ)` and describes **Satoshium Certifier**, not Registry. Git history for that file shows commit `a04dc2c5f0a90203d28b6ad1279f2c0de908db11` on August 23, 2026, titled `Add FAQ page for Satoshium Certifier`. This is actual repository evidence of a mislocated/misformatted public entry file, not evidence of a Registry canonical or authority model defect.

`registry/faq/README.md` is a distinct Registry-specific FAQ document; it should be reviewed for source-aligned public HTML content. Preserve history; do not misrepresent the copied Certifier material as Registry doctrine. The `index.html` file was **not** modified during this resource audit.

**Gate:** Review the current Registry FAQ README, adjacent Registry public visual structure, and historical intent; then apply and verify a bounded public HTML correction. Do not automatically copy Certifier terminology or declare live route serving proven.

## Boundaries and status

This audit does not certify external destinations, canonical/redirect deployment, dynamic navigation, runtime scripts, CSS, served HTTP, nor generalized inter-institution production exchange. PR-OPEN and IQ implementation items remain separately governed.

**Disposition:** Missing icon links RESOLVED — VERIFIED; other scoped local path presence CONFIRM — PASS; Registry FAQ content/format CORRECT — OPEN. **Architecture change required: none.**

> Authority follows the governed subject. Reference does not transfer authority.

---

## October 23 follow-up — Registry FAQ public entry corrected

**Disposition of the previously open Registry FAQ finding:** **RESOLVED — VERIFIED (repository level)**.

At commit `627665bc6041fe02642171b00a03202acbc9eec1`, `registry/faq/index.html` was replaced with an actual Registry-specific HTML public page sourced from the pre-existing Registry FAQ `registry/faq/README.md`. The earlier misplaced Certifier Markdown remains recoverable in Git history, including original commit `a04dc2c5f0a90203d28b6ad1279f2c0de908db11`.

The replacement uses the existing Registry public-page design conventions: dark/gold styling, topbar loader, canonical `https://satoshium.us/registry/faq/`, SVG favicon, source README link, footer integration, and the same Cloudflare analytics token as neighboring Registry pages. All **49** Registry README FAQ questions were represented as section headings without importing the incorrect Certifier-only entry text. The content and authority boundaries remain grounded in the Registry README, not newly invented policy.

Independent post-commit HEAD and HTML re-fetch confirmed: valid HTML document envelope; all 49 FAQ headings included; no missing FAQ headings; Registry page title and canonical URL; SVG favicon; no missing ICO/Apple-touch PNG references; expected source README link and navigation/analytics references. **No browser or live deployment HTTP check is claimed.**

**Updated review disposition:** Registry resource/link audit COMPLETE — APPROVED; Registry FAQ repository-format/content correction RESOLVED — VERIFIED; live serving remains outside the scope of this review. The historical open-finding text above is preserved to document why the correction was made.
