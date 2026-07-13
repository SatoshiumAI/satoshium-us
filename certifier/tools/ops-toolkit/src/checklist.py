"""
checklist.py — Release checklist logic for Satoshium certification artifact groups.
"""
from pathlib import Path
from typing import List, Tuple

from .models import EXPECTED_ARTIFACTS, PLACEHOLDER_MARKERS


class ChecklistResult:
    def __init__(self) -> None:
        self.present: List[str] = []
        self.missing: List[str] = []
        self.placeholder_warnings: List[Tuple[str, List[str]]] = []

    @property
    def is_complete(self) -> bool:
        return len(self.missing) == 0 and len(self.placeholder_warnings) == 0

    def summary(self) -> str:
        lines = []
        total = len(EXPECTED_ARTIFACTS)
        present_count = len(self.present)

        lines.append(f"Release Checklist — {present_count}/{total} artifacts present")
        lines.append("=" * 50)

        lines.append("\n✅  Present artifacts:")
        if self.present:
            for name in self.present:
                lines.append(f"  [x] {name}")
        else:
            lines.append("  (none)")

        lines.append("\n❌  Missing artifacts:")
        if self.missing:
            for name in self.missing:
                lines.append(f"  [ ] {name}")
        else:
            lines.append("  (none — all artifacts present)")

        if self.placeholder_warnings:
            lines.append("\n⚠   Artifacts with unfilled placeholders:")
            for fname, markers in self.placeholder_warnings:
                lines.append(f"  {fname}:")
                for m in markers:
                    lines.append(f"    • {m}")

        lines.append("")
        if self.is_complete:
            lines.append("🟢  Release check PASSED — all artifacts present and no placeholders found.")
        else:
            lines.append("🔴  Release check FAILED — address the items above before release.")

        return "\n".join(lines)


def check_for_placeholders(filepath: Path) -> List[str]:
    """Return a list of placeholder markers found in the given file."""
    found = []
    try:
        text = filepath.read_text(encoding="utf-8")
        for marker in PLACEHOLDER_MARKERS:
            occurrences = text.count(marker)
            if occurrences > 0:
                found.append(f"{marker!r} appears {occurrences}x")
    except Exception:
        pass
    return found


def run_checklist(cert_dir: str) -> ChecklistResult:
    result = ChecklistResult()
    base = Path(cert_dir)

    for artifact_name in EXPECTED_ARTIFACTS:
        artifact_path = base / artifact_name
        if artifact_path.exists():
            result.present.append(artifact_name)
            placeholders = check_for_placeholders(artifact_path)
            if placeholders:
                result.placeholder_warnings.append((artifact_name, placeholders))
        else:
            result.missing.append(artifact_name)

    return result
