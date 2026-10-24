#!/usr/bin/env python3
"""Observational public HTTP GET audit; no site modifications or release gate promotion."""
import json
import sys
from html.parser import HTMLParser
from urllib import request, error
from datetime import datetime, timezone

BASE = "https://satoshium.us"
ROUTES = [
    "/suite/", "/suite/status/", "/suite/interoperability/", "/suite/governance/",
    "/attestor/generation/", "/attestor/attestation-generation/",
    "/attestor/publication/", "/attestor/publication/index.html",
    "/attestor/publication/index.htm",
    "/atlas/media/orientation/global/countries/sweden/",
    "/atlas/media/orientation/global/sweden/",
    "/atlas/media/orientation/global/countries/saudia-arabia/",
    "/atlas/media/orientation/global/saudi-arabia/",
]

class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.canonical = None
        self.og_url = None
        self.description = None
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "link" and "canonical" in attributes.get("rel", "").lower().split():
            self.canonical = attributes.get("href")
        if tag == "meta" and attributes.get("property", "").lower() == "og:url":
            self.og_url = attributes.get("content")
        if tag == "meta" and attributes.get("name", "").lower() == "description":
            self.description = attributes.get("content")
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, value):
        if self.in_title:
            self.title += value

class Trace(request.HTTPRedirectHandler):
    def __init__(self):
        self.hops = []
        super().__init__()
    def redirect_request(self, req, fp, code, msg, hdrs, newurl):
        self.hops.append({"status": code, "from": req.full_url, "to": newurl})
        return super().redirect_request(req, fp, code, msg, hdrs, newurl)

def probe(path):
    trace = Trace()
    opener = request.build_opener(trace)
    req = request.Request(BASE + path, headers={"User-Agent": "Satoshium-Public-Route-Audit/1.0", "Accept": "text/html"})
    item = {"path": path, "requested_url": BASE + path}
    try:
        response = opener.open(req, timeout=18)
    except error.HTTPError as exc:
        response = exc
    except Exception as exc:
        item.update({"result": "NETWORK_ERROR", "error_type": type(exc).__name__, "error": str(exc)[:240], "hops": trace.hops})
        return item
    with response:
        content = response.read(400_000)
        charset = response.headers.get_content_charset() or "utf-8"
        meta = Metadata()
        try:
            meta.feed(content.decode(charset, errors="replace"))
        except Exception:
            pass
        item.update({
            "result": "HTTP_RESPONSE",
            "status": response.status,
            "effective_url": response.geturl(),
            "hops": trace.hops,
            "content_type": response.headers.get("Content-Type", ""),
            "title": meta.title.strip()[:180],
            "canonical": meta.canonical,
            "og_url": meta.og_url,
            "canonical_matches_served_url": meta.canonical == response.geturl(),
            "description": (meta.description or "")[:180],
            "body_sample_bytes": len(content),
        })
    return item

if __name__ == "__main__":
    output = {"observed_at_utc": datetime.now(timezone.utc).isoformat(), "method": "independent GitHub-hosted runner HTTP GET with redirects", "note": "No browser JavaScript evaluation or governance approval implied", "results": []}
    for route in ROUTES:
        r = probe(route)
        output["results"].append(r)
        print(json.dumps(r, ensure_ascii=False), flush=True)
    with open("public-route-audit-results.json", "w", encoding="utf-8") as out:
        json.dump(output, out, indent=2, ensure_ascii=False)
        out.write("\n")
    # Observational runner must complete even when one or more public routes fail.
    print("OBSERVATION_COMPLETE", flush=True)
