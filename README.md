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

### `ticket-generator`

Generates a structured change ticket for created, updated, or deleted Codex skills.

Use it when you want to turn a set of skill-related git changes into a reviewer-ready ticket.

Path: `skills/ticket-generator`

### `skill-ship`

Reviews changed Codex skills, generates a change ticket, and guides a safe commit, push, draft PR, and optional GitHub issue workflow.

Use it when you want to ship skill changes through GitHub with a guarded workflow.

Path: `skills/skill-ship`

### `skill-factory`

Scaffolds new Codex skills, generates missing `README.md` files, and prepares a repo for git initialization and publish.

Use it when you want to create a new skill repo or add new skills to an existing repo.

Path: `skills/skill-factory`

### `telegram-skill-update`

Detects newly created Codex skills and sends a concise Telegram group update using bot credentials from environment variables.

Use it when you want to notify a Telegram group after a new skill is created.

Path: `skills/telegram-skill-update`

### `skill-source-sync`

Syncs upstream code repositories into skill `scripts/` folders and generates provenance-aware documentation.

Use it when you want to:
- hydrate missing `scripts/` content for copied local skills
- keep upstream source provenance attached to synced files
- generate per-skill README content from a single manifest

Path: `skills/skill-source-sync`

## Layout

Each skill follows the same basic structure:

- `SKILL.md`: usage instructions and workflow
- `skill.yaml`: short metadata entry
- `prompt.md`: the behavior prompt used by the skill

Some skills may also include optional supporting directories:

- `agents/`: UI-facing metadata such as `openai.yaml`
- `references/`: detailed guidance loaded only when needed
