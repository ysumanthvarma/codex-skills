---
name: skill-factory
description: Scaffold new Codex skills in a git repo, generate required README.md files, and guide git init, commit, push, and publish steps.
---

# Skill Factory

Use this skill when you want to create a new Codex skill repository or add new skills to an existing repository.

## Purpose

Turn a skill idea into a repo-ready scaffold with documentation, git setup, and publish planning.

## Instructions

When invoked, do the following:

1. Restate the requested repo and skill scope.
2. Identify missing inputs only when they block creation.
3. Propose the repo layout and approval gate.
4. After approval, create the requested skill files and any required `README.md` files.
5. If the target is a new repo, initialize git and prepare the first commit.
6. If a GitHub remote exists, prepare the push and draft PR workflow.
7. If Telegram notification is requested, prepare the message body for the Telegram update skill.

## Workflow

### `plan`

Read-only phase.

Do the following:
1. Inspect the requested skill idea and target path.
2. Determine whether the target is a new repo or an existing repo.
3. List the files that will be created.
4. Identify any blocking inputs.
5. Return a concise approval-ready plan.

### `scaffold`

Mutation phase for file creation.

Do the following:
1. Create the target repository directory if it does not exist.
2. Create the root `README.md` if it is missing.
3. Create each requested skill directory under `skills/`.
4. Write the required files for each skill:
   - `SKILL.md`
   - `skill.yaml`
   - `prompt.md`
   - `agents/openai.yaml` when the skill should appear in the UI
5. Add `references/` only when a skill needs extra policy or template content.

### `publish`

Guarded git phase.

Before any push:
1. Initialize git if the target is a new repo.
2. Check branch state and remote availability.
3. Prepare the commit scope.
4. Require explicit confirmation before pushing.
5. Open a draft PR only after a successful push when GitHub is available.

### `full`

Run:
1. `plan`
2. `scaffold`
3. `publish`

Do not skip the approval gate before file creation or the confirmation gate before push.

## Output Format

Use this structure:

### Scope
- requested repo or skill scope
- target path or repo state
- blocking inputs

### Repo Plan
- new repo or existing repo
- files to create
- README plan

### Skill Plan
- skill names
- generated files per skill
- any optional references or metadata

### Git Plan
- git init status
- branch plan
- commit plan
- push plan

### Notification Plan
- Telegram handoff status
- message summary if requested

## Rules

- Do not create files before approval when plan-first flow is requested.
- Do not overwrite existing `README.md` files unless explicitly asked.
- Do not push without explicit confirmation.
- Stop if GitHub remote or auth is missing.
- Base all output on repository evidence or the requested inputs.
