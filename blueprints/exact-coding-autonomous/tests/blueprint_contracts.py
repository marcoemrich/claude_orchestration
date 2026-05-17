"""Single source of truth for exact-coding-autonomous blueprint contracts.

When the blueprint changes, update this file and the tests follow.
"""

# Required directories relative to blueprint root
REQUIRED_DIRECTORIES: list[str] = [
    ".claude",
    ".claude/agents",
    ".claude/rules",
    ".claude/skills",
    ".claude/skills/test-list",
    ".claude/skills/red",
    ".claude/skills/green",
]

# Required files inside .claude/
# NOTE: .claude/CLAUDE.md is intentionally absent in this
# blueprint. The session runs inside an automated evaluation
# framework with no user interaction; the feature spec is
# provided in the initial prompt and tdd.md (auto-loaded
# from .claude/rules/) carries all loop mechanics. A Lead
# CLAUDE.md would have no unique content. See AUDIT.md.
REQUIRED_CLAUDE_FILES: list[str] = [
    "settings.json",
]

# Required files relative to blueprint root
REQUIRED_ROOT_FILES: list[str] = [
    ".claude/agents/refactor.md",
    ".claude/rules/tdd.md",
    ".claude/rules/tdd-experiment-mode.md",
    ".claude/rules/tdd-with-ts-and-vitest.md",
    ".claude/skills/test-list/SKILL.md",
    ".claude/skills/red/SKILL.md",
    ".claude/skills/green/SKILL.md",
]

# Agent definitions — filename must match exactly
AGENT_FILES: dict[str, str] = {
    "refactor": "refactor.md",
}

# Skill definitions — directory name must match the skill's frontmatter name
SKILL_FILES: dict[str, str] = {
    "test-list": "test-list/SKILL.md",
    "red": "red/SKILL.md",
    "green": "green/SKILL.md",
}

# Caching compliance — patterns that indicate dynamic content
DYNAMIC_CONTENT_PATTERNS: list[str] = [
    r"\d{4}-\d{2}-\d{2}",          # dates (YYYY-MM-DD)
    r"\d{2}/\d{2}/\d{4}",          # dates (MM/DD/YYYY)
    r"\d{1,2}:\d{2}:\d{2}",        # timestamps (HH:MM:SS)
    r"counter\s*[:=]\s*\d+",       # counters
    r"version\s*[:=]\s*\d+\.\d+",  # version numbers used as state
]

DYNAMIC_CONTENT_ALLOWLIST: list[str] = [
    "YYYY-MM-DD",
    "HH:MM:SS",
    r"\d{4}-\d{2}-\d{2}",
    r"\d{2}/\d{2}/\d{4}",
    r"\d{1,2}:\d{2}:\d{2}",
    r"version\s*[:=]\s*\d+\.\d+",
]

# Rule file length — see autonomous/tests for rationale
RULE_FILE_LINE_LIMIT: int = 250
RULE_FILE_LENGTH_EXEMPTIONS: set[str] = set()
