# Satoshium Attestor — Executable Validator v0.3

> **VERSIONED IMPLEMENTATION RECORD — NOT CURRENT PRODUCTION VALIDATOR**  
> This v0.3 directory preserves an earlier executable rule-coverage milestone. The first production ATT and TRST final-state validation reports identify Validator **v0.5** and record aggregate outcome `valid`. Do not attribute v0.5 behavior to this v0.3 code, or treat this historical coverage result as a new production validation. Compare versions only using their own executable code, reports, and governed Review evidence.  
> **Not-tested ≠ pass; machine validation ≠ governed Review ≠ substantive Evaluation ≠ Conformance ≠ Publication.**

## Step 9 — Final Focused Coverage Closure

Validator v0.3 explicitly accounts for the complete canonical 91-rule `VAL-*` catalog.

This does **not** mean all 91 rules are machine-passable. It means each rule now has an explicit executable disposition: tested, not applicable, not tested because governed Review is required, or not tested because authoritative external/process context is required.

### Governing discipline

`Explicitly accounted ≠ Automatically passed`

`not-tested ≠ pass`

`Review ≠ Machine adjudication`

The validator does not invent institutional facts in order to force a `valid` result.

## New boundary fixtures

- `boundary-derived-attestation.yaml`
- `boundary-supersedes-attestation.yaml`
- `boundary-referenced-attestation.yaml`

These exercise provenance and relationship applicability boundaries in addition to the v0.2 fixture suite.

## Status

**Canonical rule accounting → complete**

**Machine adjudication → bounded by available object/context**

**Representative-object authorization → requires post-v0.3 reconciliation**
