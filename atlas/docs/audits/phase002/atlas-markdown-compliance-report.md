# Atlas Markdown Compliance Report

## Executive Summary

- Overall compliance status: Mostly compliant, medium-priority structural exceptions detected.
- Canonical scan root: `/home/claw-admin/claw-labs/atlas-export/jurisdictions/us/states`
- States detected: 50 / 50 expected
- States with all 7 required files present: 50
- States with missing required files: 0
- States with filename issues: 0
- Alternate non-canonical copies of required markdown filenames detected: 378

---

## State Coverage

- Number of states detected: 50
- Missing states: none
- Unexpected extra states after normalized comparison: none
- State directory naming notes: new-york

---

## File Presence Findings

- All detected state directories contain the 7 required files.

---

## Naming Compliance Findings

- No incorrect filenames or duplicate required filename patterns detected inside the canonical state directories.

---

## Path Compliance Findings

- Canonical location confirmed: `/home/claw-admin/claw-labs/atlas-export/jurisdictions/us/states`
- Required markdown filenames were also detected outside the canonical state path in these locations:

  - `satoshium-atlas-core`: 378 files
    - `satoshium-atlas-core/jurisdictions/us/arizona/builder-mode.md`
    - `satoshium-atlas-core/jurisdictions/us/arizona/change-log.md`
    - `satoshium-atlas-core/jurisdictions/us/arizona/evidence.md`
    - `satoshium-atlas-core/jurisdictions/us/arizona/profile.md`
    - `satoshium-atlas-core/jurisdictions/us/arizona/signals.md`
    - `satoshium-atlas-core/jurisdictions/us/arizona/trust-dimensions.md`
    - `satoshium-atlas-core/jurisdictions/us/california/builder-mode.md`
    - `satoshium-atlas-core/jurisdictions/us/california/change-log.md`
    - `... 370 more`

### Additional markdown files inside canonical state directories

- None detected.

---

## Framework File Findings

- Primary framework file `/atlas/docs/framework/signals-update-protocol.md`: present
- Additional copies detected: none

---

## Priority Corrections

### High

- None.

### Medium

- Required markdown filenames also appear outside the canonical atlas-export state path

### Low

- State directory naming uses hyphenated variants in: new-york
