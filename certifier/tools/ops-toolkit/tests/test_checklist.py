"""
test_checklist.py — Tests for src/checklist.py

Verifies that:
  - An empty directory reports all artifacts as missing
  - A directory with all 13 artifacts passes the checklist
  - A directory missing some artifacts reports exactly those as missing
  - Files containing PLACEHOLDER markers are flagged in placeholder_warnings
  - Files without placeholders do not appear in placeholder_warnings
  - is_complete is True only when nothing is missing and no placeholders exist
  - The complete fixture passes check_release (integration)
  - The incomplete fixture fails check_release (integration)
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.checklist import run_checklist, check_for_placeholders  # noqa: E402
from src.models import EXPECTED_ARTIFACTS                         # noqa: E402

# Paths to committed test fixtures
FIXTURE_COMPLETE   = REPO_ROOT / "tests" / "fixtures" / "complete-certification"
FIXTURE_INCOMPLETE = REPO_ROOT / "tests" / "fixtures" / "incomplete-certification"


def _touch(directory: Path, filename: str, content: str = "clean content") -> None:
    """Write a file in directory with the given content."""
    (directory / filename).write_text(content, encoding="utf-8")


def _create_all_artifacts(directory: Path, with_placeholders: bool = False) -> None:
    """Populate directory with all 13 expected artifact files."""
    content = "PLACEHOLDER content" if with_placeholders else "clean content"
    for name in EXPECTED_ARTIFACTS:
        _touch(directory, name, content)


class TestChecklistEmptyDirectory(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_all_artifacts_missing_in_empty_dir(self):
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(sorted(result.missing), sorted(EXPECTED_ARTIFACTS))

    def test_no_artifacts_present_in_empty_dir(self):
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(result.present, [])

    def test_is_not_complete_in_empty_dir(self):
        result = run_checklist(str(self.tmpdir))
        self.assertFalse(result.is_complete)

    def test_missing_count_equals_total_artifacts(self):
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(len(result.missing), len(EXPECTED_ARTIFACTS))


class TestChecklistAllPresent(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        _create_all_artifacts(self.tmpdir, with_placeholders=False)

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_all_artifacts_present(self):
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(sorted(result.present), sorted(EXPECTED_ARTIFACTS))

    def test_none_missing_when_all_present(self):
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(result.missing, [])

    def test_is_complete_when_all_present_and_clean(self):
        result = run_checklist(str(self.tmpdir))
        self.assertTrue(result.is_complete)

    def test_no_placeholder_warnings_when_clean(self):
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(result.placeholder_warnings, [])


class TestChecklistPartiallyPresent(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_reports_exactly_the_missing_artifacts(self):
        present = ["certification_package.json", "scr.md", "scrd.html"]
        for name in present:
            _touch(self.tmpdir, name)
        result = run_checklist(str(self.tmpdir))
        expected_missing = [a for a in EXPECTED_ARTIFACTS if a not in present]
        self.assertEqual(sorted(result.missing), sorted(expected_missing))

    def test_present_list_matches_files_created(self):
        present = ["certification_package.json", "evidence_inventory.json"]
        for name in present:
            _touch(self.tmpdir, name)
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(sorted(result.present), sorted(present))

    def test_is_not_complete_when_some_missing(self):
        _touch(self.tmpdir, "certification_package.json")
        result = run_checklist(str(self.tmpdir))
        self.assertFalse(result.is_complete)


class TestChecklistPlaceholderDetection(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_placeholder_in_file_is_flagged(self):
        _create_all_artifacts(self.tmpdir, with_placeholders=False)
        _touch(self.tmpdir, "sreg_stub.json", '{"key": "SREG-ID-PLACEHOLDER"}')
        result = run_checklist(str(self.tmpdir))
        flagged_names = [fname for fname, _ in result.placeholder_warnings]
        self.assertIn("sreg_stub.json", flagged_names)

    def test_clean_files_are_not_flagged(self):
        _create_all_artifacts(self.tmpdir, with_placeholders=False)
        result = run_checklist(str(self.tmpdir))
        self.assertEqual(result.placeholder_warnings, [])

    def test_placeholder_in_file_makes_checklist_incomplete(self):
        _create_all_artifacts(self.tmpdir, with_placeholders=True)
        result = run_checklist(str(self.tmpdir))
        self.assertFalse(result.is_complete)

    def test_yyyy_mm_dd_marker_is_detected(self):
        _create_all_artifacts(self.tmpdir, with_placeholders=False)
        _touch(self.tmpdir, "anch_stub.json", '{"date": "YYYY-MM-DD"}')
        result = run_checklist(str(self.tmpdir))
        flagged_names = [fname for fname, _ in result.placeholder_warnings]
        self.assertIn("anch_stub.json", flagged_names)

    def test_placeholder_occurrence_count_reported(self):
        _create_all_artifacts(self.tmpdir, with_placeholders=False)
        _touch(
            self.tmpdir,
            "satr_stub.json",
            "PLACEHOLDER PLACEHOLDER PLACEHOLDER"
        )
        result = run_checklist(str(self.tmpdir))
        flagged = {fname: markers for fname, markers in result.placeholder_warnings}
        self.assertIn("satr_stub.json", flagged)
        self.assertTrue(
            any("3x" in m for m in flagged["satr_stub.json"]),
            msg=f"Expected 3x occurrence count, got: {flagged['satr_stub.json']}"
        )


class TestCheckForPlaceholders(unittest.TestCase):
    """Unit tests for the check_for_placeholders helper."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_no_placeholders_returns_empty_list(self):
        f = self.tmpdir / "clean.txt"
        f.write_text("all good here", encoding="utf-8")
        self.assertEqual(check_for_placeholders(f), [])

    def test_single_placeholder_detected(self):
        f = self.tmpdir / "dirty.txt"
        f.write_text("PLACEHOLDER", encoding="utf-8")
        found = check_for_placeholders(f)
        self.assertTrue(len(found) > 0)

    def test_multiple_different_markers_all_detected(self):
        f = self.tmpdir / "multi.txt"
        f.write_text("PLACEHOLDER and YYYY-MM-DD", encoding="utf-8")
        found = check_for_placeholders(f)
        self.assertEqual(len(found), 2)


class TestChecklistSummaryOutput(unittest.TestCase):

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_summary_contains_pass_message_when_complete(self):
        _create_all_artifacts(self.tmpdir, with_placeholders=False)
        result = run_checklist(str(self.tmpdir))
        self.assertIn("PASSED", result.summary())

    def test_summary_contains_fail_message_when_incomplete(self):
        result = run_checklist(str(self.tmpdir))
        self.assertIn("FAILED", result.summary())

    def test_summary_shows_artifact_counts(self):
        _touch(self.tmpdir, "certification_package.json")
        result = run_checklist(str(self.tmpdir))
        summary = result.summary()
        self.assertIn("1/", summary)


# ---------------------------------------------------------------------------
# Fixture-based integration tests
#
# These tests run against committed fixture directories and verify the exact
# pass/fail outcomes that the GitHub Actions workflow also asserts.
# If a fixture is corrupted or placeholder content is accidentally removed,
# these tests catch it before CI runs.
# ---------------------------------------------------------------------------

class TestChecklistCompleteFixture(unittest.TestCase):
    """
    The complete fixture must pass check_release with no missing files
    and no placeholder warnings.  This is the same assertion as the
    'Release check — complete fixture must PASS (exit 0)' CI step.
    """

    def setUp(self):
        self.assertTrue(
            FIXTURE_COMPLETE.exists(),
            f"Complete fixture directory not found: {FIXTURE_COMPLETE}"
        )

    def test_complete_fixture_is_complete(self):
        result = run_checklist(str(FIXTURE_COMPLETE))
        self.assertTrue(
            result.is_complete,
            msg=(
                "Complete fixture failed check_release.\n"
                + result.summary()
            )
        )

    def test_complete_fixture_has_no_missing_files(self):
        result = run_checklist(str(FIXTURE_COMPLETE))
        self.assertEqual(
            result.missing, [],
            msg=f"Unexpected missing files in complete fixture: {result.missing}"
        )

    def test_complete_fixture_has_no_placeholder_warnings(self):
        result = run_checklist(str(FIXTURE_COMPLETE))
        self.assertEqual(
            result.placeholder_warnings, [],
            msg=(
                "Placeholder markers found in complete fixture — "
                "all fields must be filled:\n"
                + "\n".join(
                    f"  {fname}: {markers}"
                    for fname, markers in result.placeholder_warnings
                )
            )
        )

    def test_complete_fixture_has_all_13_artifacts_present(self):
        result = run_checklist(str(FIXTURE_COMPLETE))
        self.assertEqual(
            sorted(result.present),
            sorted(EXPECTED_ARTIFACTS),
            msg="Complete fixture does not have all 13 expected artifacts present."
        )


class TestChecklistIncompleteFixture(unittest.TestCase):
    """
    The incomplete fixture must fail check_release due to missing files
    and placeholder markers.  This is the same assertion as the
    'Release check — incomplete fixture must FAIL (exit 1)' CI step.
    """

    def setUp(self):
        self.assertTrue(
            FIXTURE_INCOMPLETE.exists(),
            f"Incomplete fixture directory not found: {FIXTURE_INCOMPLETE}"
        )

    def test_incomplete_fixture_is_not_complete(self):
        result = run_checklist(str(FIXTURE_INCOMPLETE))
        self.assertFalse(
            result.is_complete,
            msg="Incomplete fixture unexpectedly passed check_release — it should fail."
        )

    def test_incomplete_fixture_has_missing_files(self):
        result = run_checklist(str(FIXTURE_INCOMPLETE))
        self.assertGreater(
            len(result.missing), 0,
            msg="Incomplete fixture should have missing artifact files."
        )

    def test_incomplete_fixture_missing_at_least_10_files(self):
        """The fixture provides only 2 of 13 artifacts; 11 must be missing."""
        result = run_checklist(str(FIXTURE_INCOMPLETE))
        self.assertGreaterEqual(
            len(result.missing), 10,
            msg=(
                f"Expected at least 10 missing files in incomplete fixture, "
                f"got {len(result.missing)}: {result.missing}"
            )
        )

    def test_incomplete_fixture_has_placeholder_warnings(self):
        result = run_checklist(str(FIXTURE_INCOMPLETE))
        self.assertGreater(
            len(result.placeholder_warnings), 0,
            msg="Incomplete fixture should have placeholder markers in at least one file."
        )

    def test_incomplete_fixture_certification_package_has_placeholders(self):
        """certification_package.json must contain placeholder markers."""
        result = run_checklist(str(FIXTURE_INCOMPLETE))
        flagged_names = [fname for fname, _ in result.placeholder_warnings]
        self.assertIn(
            "certification_package.json",
            flagged_names,
            msg="certification_package.json in incomplete fixture should have placeholder markers."
        )


if __name__ == "__main__":
    unittest.main()
