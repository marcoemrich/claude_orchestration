"""Tests that skill files have correct frontmatter.

Skills invoked via Skill({ skill: "<name>" }) require the
frontmatter 'name' field to match the lookup key. The
experiment's measurement pipeline parses these Skill tool
calls — a wrong name silently drops the metric to zero.
"""

import pytest

from blueprint_contracts import SKILL_FILES
from conftest import SKILLS_DIR, parse_frontmatter

pytestmark = pytest.mark.static


@pytest.mark.parametrize(
    "skill_name,relpath",
    list(SKILL_FILES.items()),
    ids=list(SKILL_FILES.keys()),
)
def test_skill_has_name(skill_name, relpath):
    fm = parse_frontmatter(SKILLS_DIR / relpath)
    assert fm.get("name") == skill_name, (
        f"Skill {relpath}: expected name {skill_name!r}, got {fm.get('name')!r}"
    )


@pytest.mark.parametrize(
    "skill_name,relpath",
    list(SKILL_FILES.items()),
    ids=list(SKILL_FILES.keys()),
)
def test_skill_has_description(skill_name, relpath):
    fm = parse_frontmatter(SKILLS_DIR / relpath)
    desc = fm.get("description", "")
    assert isinstance(desc, str) and desc.strip(), (
        f"Skill {relpath}: description must be a non-empty string"
    )


@pytest.mark.parametrize(
    "skill_name,relpath",
    list(SKILL_FILES.items()),
    ids=list(SKILL_FILES.keys()),
)
def test_skill_directory_matches_name(skill_name, relpath):
    """Skill directory name must equal the frontmatter name.

    Claude Code looks up skills by directory name; a mismatch
    between the directory and frontmatter name means the skill
    is unreachable through one of the two lookup paths.
    """
    dirname = relpath.split("/")[0]
    assert dirname == skill_name, (
        f"Skill directory {dirname!r} does not match frontmatter name {skill_name!r}"
    )
