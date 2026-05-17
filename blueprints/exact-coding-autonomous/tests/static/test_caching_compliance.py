"""Tests that the blueprint complies with prompt caching constraints.

Rule files, CLAUDE.md, agent files, and skill files are cached at
session start (level 3). They must not contain dynamic content
that changes between sessions.
"""

import re

import pytest

from blueprint_contracts import (
    DYNAMIC_CONTENT_ALLOWLIST,
    DYNAMIC_CONTENT_PATTERNS,
)
from conftest import AGENTS_DIR, CLAUDE_MD, RULES_DIR, SKILLS_DIR

pytestmark = pytest.mark.static


def _static_files():
    if CLAUDE_MD.exists():
        yield CLAUDE_MD
    if AGENTS_DIR.is_dir():
        yield from sorted(AGENTS_DIR.glob("*.md"))
    if RULES_DIR.is_dir():
        yield from sorted(RULES_DIR.glob("*.md"))
    if SKILLS_DIR.is_dir():
        yield from sorted(SKILLS_DIR.glob("*/SKILL.md"))


def _line_has_dynamic_content(line: str) -> str | None:
    for pattern in DYNAMIC_CONTENT_PATTERNS:
        match = re.search(pattern, line)
        if match:
            for allowed in DYNAMIC_CONTENT_ALLOWLIST:
                if allowed in line:
                    return None
            return match.group(0)
    return None


@pytest.mark.parametrize(
    "filepath",
    list(_static_files()),
    ids=lambda p: str(p.relative_to(p.parents[2])),
)
def test_no_dynamic_content_in_static_files(filepath):
    content = filepath.read_text()
    violations = []
    for i, line in enumerate(content.splitlines(), 1):
        match = _line_has_dynamic_content(line)
        if match:
            violations.append(f"  line {i}: {match!r} in {line.strip()!r}")

    assert not violations, (
        f"Dynamic content found in {filepath.name}:\n" + "\n".join(violations)
    )
