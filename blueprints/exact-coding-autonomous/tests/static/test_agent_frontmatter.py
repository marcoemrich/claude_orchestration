"""Tests that agent definition files have correct frontmatter."""

import pytest

from blueprint_contracts import AGENT_FILES
from conftest import AGENTS_DIR, parse_frontmatter

pytestmark = pytest.mark.static


@pytest.mark.parametrize(
    "agent_name,filename",
    list(AGENT_FILES.items()),
    ids=list(AGENT_FILES.keys()),
)
def test_agent_has_name(agent_name, filename):
    """Frontmatter 'name' must match the contract key exactly.

    SendMessage requires exact name matching; mismatches between
    the registered name and the form agents guess (lowercase
    hyphenated) cause silently dropped messages.
    """
    fm = parse_frontmatter(AGENTS_DIR / filename)
    assert fm.get("name") == agent_name, (
        f"Agent {filename}: expected name {agent_name!r}, got {fm.get('name')!r}"
    )


@pytest.mark.parametrize(
    "agent_name,filename",
    list(AGENT_FILES.items()),
    ids=list(AGENT_FILES.keys()),
)
def test_agent_has_description(agent_name, filename):
    fm = parse_frontmatter(AGENTS_DIR / filename)
    desc = fm.get("description", "")
    assert isinstance(desc, str) and desc.strip(), (
        f"Agent {filename}: description must be a non-empty string"
    )
