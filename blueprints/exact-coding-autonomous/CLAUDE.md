# Blueprint — exact-coding-autonomous

Strict TDD blueprint for Claude Code. Drives the
red-green-refactor cycle as a sequence of Skill calls
(`/test-list`, `/red`, `/green`) plus a refactor subagent
launched after each green. Designed for automated
evaluation: no user interaction, no plan approval gates —
the feature spec arrives in the initial prompt and the
session runs the loop until all tests are implemented.
The Skill and Task calls emitted per cycle are the
measured signal.

## Build and Test

```sh
uv run pytest blueprints/exact-coding-autonomous/tests/ -m static -v
```

## Components

| Path | Purpose |
|---|---|
| `.claude/settings.json` | Permissions (read/write/edit, pnpm, Task, Skill) |
| `.claude/agents/refactor.md` | Refactoring specialist launched as a Task subagent after each green |
| `.claude/rules/tdd.md` | Loop mechanics — which Skill/Task to invoke for each phase, why delegation is required for the metrics |
| `.claude/rules/tdd-experiment-mode.md` | Autonomous-execution rule: no human gates between phases; refactor-subagent prompt template; done-marker |
| `.claude/rules/tdd-with-ts-and-vitest.md` | Tech stack — `.spec.ts` extension, Vitest functions, `pnpm test` |
| `.claude/skills/test-list/SKILL.md` | Skill: writes the initial `it.todo()` list scoped to base functionality |
| `.claude/skills/red/SKILL.md` | Skill: activates one `it.todo()`, records prediction blocks parsed by the measurement pipeline |
| `.claude/skills/green/SKILL.md` | Skill: writes the minimal implementation to turn the active test green |
| `tests/blueprint_contracts.py` | Single source of truth for required files, agents, skills |
| `tests/static/` | File structure, agent/skill frontmatter, rule line length, caching compliance, settings sanity |
| `AUDIT.md` | Audit findings and resolution log |

## Conventions

- Agent files define role only — no workflow coupling, no TDD-phase references in the refactor agent
- Skills (`test-list`, `red`, `green`) live under `.claude/skills/<name>/SKILL.md` and are invoked via `Skill({ skill: "<name>" })` — the measurement pipeline parses these tool calls
- The refactor subagent is launched via `Task({ subagent_type: "refactor", ... })` — isolated context, no memory of red/green
- No Lead `.claude/CLAUDE.md` — the framework supplies the spec in the initial prompt and `tdd.md` auto-loads
- All blueprint files must be fully static — no dates, counters, versions (prompt cache level 3)
- Rule files target under 200 lines — agent adherence degrades beyond that threshold
- Agent and skill `name:` fields use lowercase form — must match the lookup key exactly
- Done marker: `experiment-done.txt` containing the single word `DONE`, written only when all tests pass
- Terminology: "launch" subagents, "invoke" skills

## References

- [Claude Code documentation](https://code.claude.com/docs)
- Micah Martin — Absolute Priority Premise (8th Light blog)
