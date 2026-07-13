"""
test_validator.py — Tests for src/validator.py

Verifies that:
  - A fully populated package passes validation
  - Fields containing placeholder markers produce errors
  - Missing required fields produce errors
  - An invalid status value produces an error
  - An empty evidence_references list produces a warning (not an error)
  - The _instructions key produces a warning (not an error)
"""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.validator import validate_certification_package  # noqa: E402


def _valid_package():
    """Return a minimal but fully valid certification package dict."""
    return {
        "certification_id": "SC-CERT-2026-0099",
        "schema_version":   "1.0.0",
        "issued_date":      "2026-07-13",
        "status":           "CERTIFIED",
        "certifier": {
            "id":   "CERTIFIER-001",
            "name": "Test Certifier",
            "role": "Primary Certifier",
        },
        "subject": {
            "id":          "SUBJECT-001",
            "name":        "Test Subject",
            "type":        "Software Module",
            "description": "A test subject for unit testing.",
        },
        "standard": {
            "id":      "STD-001",
            "name":    "Test Standard",
            "version": "1.0",
        },
        "methodology": {
            "id":   "METHOD-001",
            "name": "Test Methodology",
        },
        "scope": {
            "summary": "Full scope for testing purposes.",
        },
        "outcome": {
            "status":  "CERTIFIED",
            "summary": "All criteria met.",
        },
        "evidence_references": [
            {
                "evidence_id": "EVD-001",
                "title":       "Test Evidence",
                "type":        "Test Report",
                "location":    "https://example.com/evidence/EVD-001",
            }
        ],
        "metadata": {
            "created_by": "test-suite",
            "created_at": "2026-07-13T00:00:00Z",
        },
    }


class TestValidatorPassesCleanPackage(unittest.TestCase):

    def test_valid_package_passes(self):
        result = validate_certification_package(_valid_package())
        self.assertTrue(result.is_valid, msg=result.summary())

    def test_valid_package_has_no_errors(self):
        result = validate_certification_package(_valid_package())
        self.assertEqual(len(result.errors), 0)

    def test_valid_package_has_no_warnings(self):
        result = validate_certification_package(_valid_package())
        self.assertEqual(len(result.warnings), 0)


class TestValidatorDetectsPlaceholders(unittest.TestCase):

    def test_placeholder_in_top_level_field(self):
        pkg = _valid_package()
        pkg["issued_date"] = "YYYY-MM-DD"
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("issued_date" in e for e in result.errors))

    def test_placeholder_in_certifier_name(self):
        pkg = _valid_package()
        pkg["certifier"]["name"] = "CERTIFIER-NAME-PLACEHOLDER"
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("certifier.name" in e for e in result.errors))

    def test_placeholder_in_subject_description(self):
        pkg = _valid_package()
        pkg["subject"]["description"] = "SUBJECT-DESCRIPTION-PLACEHOLDER"
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("subject.description" in e for e in result.errors))

    def test_placeholder_in_evidence_location(self):
        pkg = _valid_package()
        pkg["evidence_references"][0]["location"] = "EVIDENCE-LOCATION-URL-PLACEHOLDER"
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(
            any("evidence_references" in e and "location" in e for e in result.errors)
        )


class TestValidatorDetectsMissingFields(unittest.TestCase):

    def test_missing_certification_id(self):
        pkg = _valid_package()
        del pkg["certification_id"]
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("certification_id" in e for e in result.errors))

    def test_missing_certifier_role(self):
        pkg = _valid_package()
        del pkg["certifier"]["role"]
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("certifier.role" in e for e in result.errors))

    def test_missing_scope_summary(self):
        pkg = _valid_package()
        del pkg["scope"]["summary"]
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("scope.summary" in e for e in result.errors))

    def test_missing_metadata_created_by(self):
        pkg = _valid_package()
        del pkg["metadata"]["created_by"]
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("metadata.created_by" in e for e in result.errors))


class TestValidatorStatusValues(unittest.TestCase):

    def test_invalid_status_produces_error(self):
        pkg = _valid_package()
        pkg["status"] = "APPROVED"  # not a valid enum value
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("status" in e and "APPROVED" in e for e in result.errors))

    def test_invalid_outcome_status_produces_error(self):
        pkg = _valid_package()
        pkg["outcome"]["status"] = "PASSED"
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)
        self.assertTrue(
            any("outcome.status" in e and "PASSED" in e for e in result.errors)
        )

    def test_all_valid_statuses_accepted(self):
        for status in ("PENDING", "CERTIFIED", "REJECTED", "SUSPENDED", "WITHDRAWN"):
            pkg = _valid_package()
            pkg["status"] = status
            pkg["outcome"]["status"] = status
            result = validate_certification_package(pkg)
            # Status value itself should not produce a status-enum error
            status_enum_errors = [
                e for e in result.errors
                if ("must be one of" in e and status in e)
            ]
            self.assertEqual(
                len(status_enum_errors), 0,
                msg=f"Status {status!r} should be valid but got error: {result.errors}"
            )


class TestValidatorWarnings(unittest.TestCase):

    def test_empty_evidence_references_is_warning_not_error(self):
        pkg = _valid_package()
        pkg["evidence_references"] = []
        result = validate_certification_package(pkg)
        self.assertTrue(result.is_valid, "Empty evidence should be a warning, not an error")
        self.assertTrue(
            any("evidence" in w.lower() for w in result.warnings)
        )

    def test_instructions_key_is_warning_not_error(self):
        pkg = _valid_package()
        pkg["_instructions"] = "Remove me"
        result = validate_certification_package(pkg)
        self.assertTrue(result.is_valid, "_instructions key should be a warning, not an error")
        self.assertTrue(
            any("_instructions" in w for w in result.warnings)
        )

    def test_evidence_references_not_a_list_is_error(self):
        pkg = _valid_package()
        pkg["evidence_references"] = "not a list"
        result = validate_certification_package(pkg)
        self.assertFalse(result.is_valid)


class TestValidationResult(unittest.TestCase):

    def test_summary_contains_pass_message_when_valid(self):
        result = validate_certification_package(_valid_package())
        self.assertIn("passed", result.summary().lower())

    def test_summary_contains_fail_message_when_invalid(self):
        pkg = _valid_package()
        del pkg["certification_id"]
        result = validate_certification_package(pkg)
        self.assertIn("failed", result.summary().lower())


if __name__ == "__main__":
    unittest.main()
