"""Shared fixtures for exact-coding-autonomous blueprint tests."""

import sys
from pathlib import Path

import yaml

_tests_dir = str(Path(__file__).parent)
if _tests_dir not in sys.path:
    sys.path.insert(0, _tests_dir)

BLUEPRINT_ROOT = Path(__file__).parent.parent
REPO_ROOT = BLUEPRINT_ROOT.parent.parent

CLAUDE_DIR = BLUEPRINT_ROOT / ".claude"
AGENTS_DIR = CLAUDE_DIR / "agents"
RULES_DIR = CLAUDE_DIR / "rules"
SKILLS_DIR = CLAUDE_DIR / "skills"
SETTINGS_FILE = CLAUDE_DIR / "settings.json"
CLAUDE_MD = CLAUDE_DIR / "CLAUDE.md"


def parse_frontmatter(filepath: Path) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    text = filepath.read_text()
    if not text.startswith("---"):
        return {}
    end = text.index("---", 3)
    yaml_text = text[3:end].strip()
    return yaml.safe_load(yaml_text) or {}
