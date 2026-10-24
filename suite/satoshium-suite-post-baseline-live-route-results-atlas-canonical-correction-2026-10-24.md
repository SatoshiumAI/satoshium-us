# Post-Baseline Review — Live Route Audit Findings and Targeted Atlas Canonical Correction

**Date:** October 24, 2026 (Pacific)  
**Source baseline:** `f13c931ff4a33d855eb75e8604a6c9f28499ca1d` (`phase004`)  
**Evidence job:** GitHub Actions Public Route Evidence Audit [run 40110655761](https://github.com/SatoshiumAI/satoshium-us/actions/runs/40110655761), job `120921484392`.  
**Disposition:** **LIVE ROUTE REVIEW COMPLETE — APPROVED (13 bounded HTTP GET observations); METADATA SOURCE CORRECTION COMPLETE — DEPLOYED READBACK TO BE CONFIRMED**.  
**Suite 1.0 documentary baseline:** ALREADY COMPLETE — APPROVED; actual integrated product release still NOT AUTHORIZED.

## Independent live HTTP evidence

The independent GitHub-hosted runner, Python 3.11 GET plus redirect capture, logged 13 route observations and completed successfully. Its raw log included `OBSERVATION_COMPLETE` and JSON line for each route; these are **actual HTTP observations** rather than inferences from GitHub Pages deploy success. The workflow also uploaded `public-route-evidence` JSON artifact.

| Tested request path relative to https://satoshium.us | HTTP | Declared canonical and key outcome |
|---|---|---|
| `/suite/` | **200** | Canonical `/suite/`, expected title |
| `/suite/status/` | **200** | Canonical `/suite/status/` |
| `/suite/interoperability/` | **200** | Canonical `/suite/interoperability/` |
| `/suite/governance/` | **200** | Canonical `/suite/governance/` |
| `/attestor/generation/` | **200** | Canonical `/attestor/generation/` |
| `/attestor/attestation-generation/` | **200** | Legacy URL **served directly with HTTP 200**, without HTTP redirect, declaring canonical `/attestor/generation/` |
| `/attestor/publication/` | **200** | Canonical `/attestor/publication/` |
| `/attestor/publication/index.html` | **200** | Canonical `/attestor/publication/` |
| `/attestor/publication/index.htm` | **200** | Canonical `/attestor/publication/` |
| `/atlas/media/orientation/global/countries/sweden/` | **200** | Source originally declared incorrect canonical `/atlas/media/orientation/global/sweden/` |
| `/atlas/media/orientation/global/sweden/` | **404** | GitHub Pages not-found page; no redirect |
| `/atlas/media/orientation/global/countries/saudia-arabia/` | **200** | Source originally declared incorrect canonical `/atlas/media/orientation/global/saudi-arabia/` |
| `/atlas/media/orientation/global/saudi-arabia/` | **404** | GitHub Pages not-found page; no redirect |

**Result:** 11 of 13 tested requests gave 200; 2 gave 404, both being Atlas Media **alternate URLs listed as canonicals**, rather than existing source-page URLs. The observed two broken alternate URLs may have inbound links and may warrant future redirected aliases, but no traffic or redirect policy evidence was collected here. No redirects were observed among the 13 tested routes.

**Attestor governance interpretation:** Current Generation and legacy aliases are HTTP 200 content, with a canonical tag pointing to the intended current URL, **not** HTTP redirects. Publication directory, `index.html` and `index.htm` all return HTTP 200 and consistent canonical tags. Thus `PR-OPEN-003` and `PR-OPEN-004` can be marked **HTTP SERVING VERIFIED** for the checked request set; stronger claim of redirect consolidation is **NOT** met (nor was it approved as a required policy). Browser/JS equivalence and hosted-file-precedence beyond observed content remain separate questions. Do not call the old URL redirected.

## Narrow source correction based on observed failures

Without changing routing, page title, source directory, substantive content, images or history, update **two** metadata values on each of the following existing pages:

- `atlas/media/orientation/global/countries/sweden/index.html`: canonical `rel=canonical` and `og:url` changed from nonexistent `.../global/sweden/` to observed working `.../global/countries/sweden/`.
- `atlas/media/orientation/global/countries/saudia-arabia/index.html`: canonical `rel=canonical` and `og:url` changed from nonexistent `.../global/saudi-arabia/` to observed working `.../global/countries/saudia-arabia/`.

The `saudia-arabia` filesystem segment is a preserved existing path spelling, not a recommendation to adopt that spelling as a new naming convention. Redirect policy, future migration to `saudi-arabia`, SEO backlinks or alias files require a separate deliberate decision.

**Release limitation:** HTTP GET, metadata and title verification do not establish browser JS/CORS/CSP/accessibility, production API semantics or generalized automated interoperability. The original existing 23 interoperability queue tasks remain unchanged; `PR-OPEN-002` remains closed only for B5 test scope.

## Follow-up

- Verify current commit and source readback of both canonical and OG values.
- Verify deployment workflow outcome of this correction.
- Independently re-probe *served* canonical and OG URLs after deployment to confirm the real public response changed, rather than merely trusting source.
- Later target the shared topbar's DOM/network/CSP/accessibility behavior and check which public capabilities an actual Suite 1.0 operational release will promise.
- Preserve `PR-OPEN-001`, `PR-OPEN-005`, `PR-OPEN-006` and the 23-item implementation queue; no implicit waiver.

**Scope conclusion:** Core public Suite/Attestor HTTP reachability established for these exact requests; Atlas Media wrong canonical claims source corrected. **Public integrated Suite 1.0 product release is still not authorized.**
