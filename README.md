# Codex Skills

This repository contains reusable Codex skills packaged as simple directories under `skills/`.

## Available Skills

### `brainstormer`

Generates structured solution options for open-ended product and engineering problems.

Use it when you want to:
- restate a problem clearly
- compare multiple implementation approaches
- get a short recommendation with next steps

Path: `skills/brainstormer`

### `safe-ship`

Reviews local git changes from developer, SRE, and security perspectives, then prepares a guarded commit and push workflow.

Modes:
- `review`: read-only analysis of change scope and risks
- `prepare`: suggest commit scope, draft a commit message, and create root `README.md` only if it is missing
- `publish`: run guarded pre-push checks and require explicit confirmation before pushing
- `full`: run `review`, `prepare`, and `publish` in sequence without skipping the final confirmation gate

Key safety behavior:
- classifies findings as `blocker`, `warning`, or `note`
- decides readiness as `not ready`, `ready with caution`, or `ready`
- infers repo posture as `public`, `internal`, or `unknown` and applies stricter standards to public-facing repos
- refuses unsafe publish actions when secrets, protected-branch risk, merge conflicts, rebase state, or unresolved high-severity findings are present
- never overwrites an existing `README.md` automatically
- treats missing `README.md` more strictly for public or reusable repos than for narrowly internal ones

Path: `skills/safe-ship`

## Layout

Each skill follows the same basic structure:

- `SKILL.md`: usage instructions and workflow
- `skill.yaml`: short metadata entry
- `prompt.md`: the behavior prompt used by the skill

Some skills may also include optional supporting directories:

- `agents/`: UI-facing metadata such as `openai.yaml`
- `references/`: detailed guidance loaded only when needed
