"""
test_generator.py — Tests for src/generator.py

Verifies that:
  - generate_all_artifacts() creates exactly the 12 expected derived artifact files
  - Generated Markdown files reference the certification_id from the source package
  - Generated JSON files are valid JSON and reference the correct certification_id
  - SCRD HTML contains the certification_id
  - Evidence inventory item count matches the source package
  - Stub files contain the subject_id and certifier_id from the source package
  - Generator works with empty evidence_references (edge case)
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.generator import generate_all_artifacts  # noqa: E402
from src.models import EXPECTED_ARTIFACTS         # noqa: E402

# The 12 derived artifacts (all except certification_package.json itself)
DERIVED_ARTIFACTS = [a for a in EXPECTED_ARTIFACTS if a != "certification_package.json"]


def _minimal_package(cert_id: str = "SC-CERT-TEST-GEN-0001") -> dict:
    """Return a minimal valid package suitable for generation tests."""
    return {
        "certification_id": cert_id,
        "schema_version":   "1.0.0",
        "issued_date":      "2026-07-13",
        "effective_date":   "2026-07-13",
        "expiry_date":      "2027-07-13",
        "status":           "CERTIFIED",
        "certifier": {
            "id":      "CERTIFIER-GEN-001",
            "name":    "Generator Test Certifier",
            "role":    "Primary Certifier",
            "contact": "test@example.com",
        },
        "subject": {
            "id":          "SUBJECT-GEN-001",
            "name":        "Generator Test Subject",
            "type":        "Software Module",
            "description": "A subject used for generator unit tests.",
            "version":     "1.0.0",
            "repository":  "https://github.com/example/test",
        },
        "standard": {
            "id":            "STD-GEN-001",
            "name":          "Test Standard",
            "version":       "1.0",
            "reference_url": "https://example.com/standards/STD-GEN-001",
        },
        "methodology": {
            "id":          "METHOD-GEN-001",
            "name":        "Test Methodology",
            "version":     "1.0",
            "description": "Methodology for testing.",
        },
        "scope": {
            "summary":    "Full scope for generator testing.",
            "inclusions": ["Item A", "Item B"],
            "exclusions": ["Item C"],
        },
        "outcome": {
            "status":             "CERTIFIED",
            "summary":            "All criteria met in the generator test.",
            "determination_date": "2026-07-13",
            "conditions":         ["Re-certify on major version bump."],
        },
        "evidence_references": [
            {
                "evidence_id":    "EVD-GEN-001",
                "title":          "Source Code Review",
                "type":           "Review Report",
                "location":       "https://example.com/evidence/EVD-GEN-001",
                "hash":           "sha256:abc123",
                "collected_date": "2026-07-01",
            },
            {
                "evidence_id":    "EVD-GEN-002",
                "title":          "Test Suite Results",
                "type":           "Test Report",
                "location":       "https://example.com/evidence/EVD-GEN-002",
                "hash":           "sha256:def456",
                "collected_date": "2026-07-05",
            },
        ],
        "related_artifacts": {
            "scrd_id": "SCRD-GEN-0001",
            "sreg_id": "SREG-GEN-0001",
            "schr_id": "SCHR-GEN-0001",
            "anch_id": "ANCH-GEN-0001",
            "satr_id": "SATR-GEN-0001",
        },
        "notes": "Generator test package.",
        "metadata": {
            "created_by": "test-suite",
            "created_at": "2026-07-13T00:00:00Z",
        },
    }


class TestGeneratorCreatesAllArtifacts(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_all_derived_artifacts_are_created(self):
        pkg = _minimal_package()
        generate_all_artifacts(pkg, self.tmpdir)
        for artifact in DERIVED_ARTIFACTS:
            with self.subTest(artifact=artifact):
                self.assertTrue(
                    (self.tmpdir / artifact).exists(),
                    msg=f"{artifact} was not created"
                )

    def test_exactly_twelve_artifacts_generated(self):
        pkg = _minimal_package()
        generate_all_artifacts(pkg, self.tmpdir)
        generated = [f.name for f in self.tmpdir.iterdir() if f.is_file()]
        self.assertEqual(len(generated), 12)


class TestGeneratorMarkdownContent(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.cert_id = "SC-CERT-TEST-GEN-0002"
        self.pkg = _minimal_package(self.cert_id)
        generate_all_artifacts(self.pkg, self.tmpdir)

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def _read(self, filename: str) -> str:
        return (self.tmpdir / filename).read_text(encoding="utf-8")

    def test_certification_package_md_contains_cert_id(self):
        content = self._read("certification_package.md")
        self.assertIn(self.cert_id, content)

    def test_scpr_md_contains_cert_id(self):
        content = self._read("scpr.md")
        self.assertIn(self.cert_id, content)

    def test_scr_md_contains_cert_id(self):
        content = self._read("scr.md")
        self.assertIn(self.cert_id, content)

    def test_evidence_map_md_contains_evidence_ids(self):
        content = self._read("evidence_map.md")
        self.assertIn("EVD-GEN-001", content)
        self.assertIn("EVD-GEN-002", content)

    def test_release_checklist_contains_cert_id(self):
        content = self._read("release_checklist.md")
        self.assertIn(self.cert_id, content)

    def test_certification_package_md_contains_subject_name(self):
        content = self._read("certification_package.md")
        self.assertIn("Generator Test Subject", content)

    def test_scr_md_contains_certifier_name(self):
        content = self._read("scr.md")
        self.assertIn("Generator Test Certifier", content)


class TestGeneratorJsonContent(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.cert_id = "SC-CERT-TEST-GEN-0003"
        self.pkg = _minimal_package(self.cert_id)
        generate_all_artifacts(self.pkg, self.tmpdir)

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def _load(self, filename: str) -> dict:
        with open(self.tmpdir / filename, encoding="utf-8") as f:
            return json.load(f)

    def test_scrd_json_is_valid_json(self):
        data = self._load("scrd.json")
        self.assertIsInstance(data, dict)

    def test_scrd_json_certification_id_matches(self):
        data = self._load("scrd.json")
        self.assertEqual(data["certification_id"], self.cert_id)

    def test_scrd_json_outcome_status_matches(self):
        data = self._load("scrd.json")
        self.assertEqual(data["outcome"]["status"], "CERTIFIED")

    def test_evidence_inventory_is_valid_json(self):
        data = self._load("evidence_inventory.json")
        self.assertIsInstance(data, dict)

    def test_evidence_inventory_item_count_matches(self):
        data = self._load("evidence_inventory.json")
        self.assertEqual(data["total_items"], 2)
        self.assertEqual(len(data["items"]), 2)

    def test_evidence_inventory_certification_id_matches(self):
        data = self._load("evidence_inventory.json")
        self.assertEqual(data["certification_id"], self.cert_id)

    def test_sreg_stub_is_valid_json(self):
        data = self._load("sreg_stub.json")
        self.assertIsInstance(data, dict)

    def test_sreg_stub_subject_id_matches(self):
        data = self._load("sreg_stub.json")
        self.assertEqual(data["subject_id"], "SUBJECT-GEN-001")

    def test_schr_stub_certifier_id_matches(self):
        data = self._load("schr_stub.json")
        self.assertEqual(data["certifier_id"], "CERTIFIER-GEN-001")

    def test_anch_stub_certification_id_matches(self):
        data = self._load("anch_stub.json")
        self.assertEqual(data["certification_id"], self.cert_id)

    def test_satr_stub_subject_id_matches(self):
        data = self._load("satr_stub.json")
        self.assertEqual(data["subject_id"], "SUBJECT-GEN-001")

    def test_all_json_stubs_have_metadata_generated_by(self):
        for fname in ("scrd.json", "sreg_stub.json", "schr_stub.json",
                      "anch_stub.json", "satr_stub.json", "evidence_inventory.json"):
            with self.subTest(file=fname):
                data = self._load(fname)
                if "metadata" in data:
                    self.assertEqual(
                        data["metadata"]["generated_by"],
                        "satoshium-certifier-ops-toolkit"
                    )


class TestGeneratorHtmlContent(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.cert_id = "SC-CERT-TEST-GEN-0004"
        self.pkg = _minimal_package(self.cert_id)
        generate_all_artifacts(self.pkg, self.tmpdir)
        self.html = (self.tmpdir / "scrd.html").read_text(encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_scrd_html_is_non_empty(self):
        self.assertGreater(len(self.html), 100)

    def test_scrd_html_contains_cert_id(self):
        self.assertIn(self.cert_id, self.html)

    def test_scrd_html_contains_subject_name(self):
        self.assertIn("Generator Test Subject", self.html)

    def test_scrd_html_contains_doctype(self):
        self.assertIn("<!DOCTYPE html>", self.html)

    def test_scrd_html_contains_status_badge(self):
        self.assertIn("status-CERTIFIED", self.html)

    def test_scrd_html_html_escaping_on_special_chars(self):
        """Verify that html.escape is applied — inject a < char and confirm it is escaped."""
        pkg = _minimal_package("SC-CERT-ESCAPE-TEST")
        pkg["subject"]["name"] = "Module <v1.0>"
        tmpdir2 = Path(tempfile.mkdtemp())
        try:
            generate_all_artifacts(pkg, tmpdir2)
            html_content = (tmpdir2 / "scrd.html").read_text(encoding="utf-8")
            self.assertNotIn("<v1.0>", html_content)
            self.assertIn("&lt;v1.0&gt;", html_content)
        finally:
            shutil.rmtree(tmpdir2, ignore_errors=True)


class TestGeneratorEdgeCases(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_empty_evidence_references(self):
        """Generator should not crash with an empty evidence list."""
        pkg = _minimal_package()
        pkg["evidence_references"] = []
        generate_all_artifacts(pkg, self.tmpdir)
        inv_path = self.tmpdir / "evidence_inventory.json"
        self.assertTrue(inv_path.exists())
        with open(inv_path, encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["total_items"], 0)

    def test_missing_optional_related_artifacts(self):
        """Generator should not crash if related_artifacts is absent."""
        pkg = _minimal_package()
        del pkg["related_artifacts"]
        generate_all_artifacts(pkg, self.tmpdir)
        # sreg stub should still be created with a fallback ID
        sreg_path = self.tmpdir / "sreg_stub.json"
        self.assertTrue(sreg_path.exists())
        with open(sreg_path, encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("sreg_id", data)

    def test_missing_optional_scope_lists(self):
        """Generator should not crash if inclusions/exclusions lists are absent."""
        pkg = _minimal_package()
        pkg["scope"] = {"summary": "Scope without lists."}
        generate_all_artifacts(pkg, self.tmpdir)
        md_path = self.tmpdir / "certification_package.md"
        self.assertTrue(md_path.exists())


if __name__ == "__main__":
    unittest.main()
