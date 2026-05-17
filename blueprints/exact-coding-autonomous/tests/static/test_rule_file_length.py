"""Rule files must stay within the recommended line limit."""

import pytest

from blueprint_contracts import RULE_FILE_LENGTH_EXEMPTIONS, RULE_FILE_LINE_LIMIT
from conftest import RULES_DIR

pytestmark = pytest.mark.static

TARGET_LINES = 200


def _rule_files():
    if RULES_DIR.is_dir():
        yield from sorted(RULES_DIR.glob("*.md"))


@pytest.mark.parametrize(
    "filepath",
    list(_rule_files()),
    ids=lambda p: p.name,
)
def test_rule_file_within_line_limit(filepath):
    if filepath.name in RULE_FILE_LENGTH_EXEMPTIONS:
        pytest.skip(f"{filepath.name} is exempt (known tech debt — needs split)")
    line_count = len(filepath.read_text().splitlines())
    assert line_count <= RULE_FILE_LINE_LIMIT, (
        f"{filepath.name} has {line_count} lines "
        f"(limit: {RULE_FILE_LINE_LIMIT}, target: {TARGET_LINES}). "
        f"Split into focused files — long rule files degrade agent adherence."
    )
