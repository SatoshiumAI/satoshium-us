"""
test_new_certification.py — Tests for scripts/new_certification.py

Verifies that:
  - A new certification folder is created at OUTPUT_ROOT/<cert_id>
  - certification_package.json is written into the folder
  - The certification_id field is set to the requested ID
  - Attempting to initialize an already-existing folder exits with an error
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Make the repo root importable regardless of where tests are invoked from
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import scripts.new_certification as new_cert_mod  # noqa: E402


class TestNewCertification(unittest.TestCase):

    def setUp(self):
        """Redirect OUTPUT_ROOT to a fresh temp directory for each test."""
        self.tmpdir = Path(tempfile.mkdtemp())
        self._original_output_root = new_cert_mod.OUTPUT_ROOT
        new_cert_mod.OUTPUT_ROOT = self.tmpdir

    def tearDown(self):
        new_cert_mod.OUTPUT_ROOT = self._original_output_root
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    # ------------------------------------------------------------------
    # Folder creation
    # ------------------------------------------------------------------

    def test_creates_folder(self):
        new_cert_mod.init_certification("SC-CERT-TEST-0001")
        self.assertTrue((self.tmpdir / "SC-CERT-TEST-0001").is_dir())

    def test_folder_contains_certification_package(self):
        new_cert_mod.init_certification("SC-CERT-TEST-0002")
        pkg_path = self.tmpdir / "SC-CERT-TEST-0002" / "certification_package.json"
        self.assertTrue(pkg_path.exists(), "certification_package.json should exist")

    # ------------------------------------------------------------------
    # Certification ID propagation
    # ------------------------------------------------------------------

    def test_certification_id_is_set(self):
        cert_id = "SC-CERT-TEST-0003"
        new_cert_mod.init_certification(cert_id)
        pkg_path = self.tmpdir / cert_id / "certification_package.json"
        with open(pkg_path, encoding="utf-8") as f:
            pkg = json.load(f)
        self.assertEqual(pkg["certification_id"], cert_id)

    def test_certification_id_overrides_template_placeholder(self):
        """The template has 'CERT-ID-PLACEHOLDER'; init must replace it."""
        cert_id = "SC-CERT-TEST-0004"
        new_cert_mod.init_certification(cert_id)
        pkg_path = self.tmpdir / cert_id / "certification_package.json"
        with open(pkg_path, encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("CERT-ID-PLACEHOLDER", content)
        self.assertIn(cert_id, content)

    # ------------------------------------------------------------------
    # Output is valid JSON
    # ------------------------------------------------------------------

    def test_output_is_valid_json(self):
        cert_id = "SC-CERT-TEST-0005"
        new_cert_mod.init_certification(cert_id)
        pkg_path = self.tmpdir / cert_id / "certification_package.json"
        with open(pkg_path, encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)

    # ------------------------------------------------------------------
    # Duplicate prevention
    # ------------------------------------------------------------------

    def test_duplicate_init_raises_system_exit(self):
        """A second init on the same cert_id must call sys.exit(1)."""
        cert_id = "SC-CERT-TEST-0006"
        new_cert_mod.init_certification(cert_id)
        with self.assertRaises(SystemExit) as ctx:
            new_cert_mod.init_certification(cert_id)
        self.assertEqual(ctx.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
