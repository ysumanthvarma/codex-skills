---
name: skill-source-sync
description: Sync upstream code repositories into skill scripts folders and generate provenance-aware documentation.
---

# Skill Source Sync

Sync missing code for local Codex skills from upstream repositories into each skill's `scripts/` folder.

## Purpose

Provide a repeatable workflow to hydrate missing `scripts/` content for copied skills and keep source provenance documented.

## Inputs

- target skill name, or `all`
- manifest file path

## Workflow

1. Read the source manifest.
2. Validate repository URL, branch, source path, and destination path.
3. Clone or update the upstream repository in a temporary working location.
4. Copy the declared source files into `skills/<skill>/scripts/`.
5. Write provenance metadata with upstream URL, branch, and commit SHA.
6. Generate or refresh `skills/<skill>/README.md`.
7. Report copied files, skipped files, and validation failures.
8. Run the sync implementation from `scripts/sync-skill-sources.py`.

## Rules

- Never write outside `skills/<skill>/scripts/`.
- Never delete user-authored files unless explicitly asked.
- Fail on unsafe paths such as `..` or absolute destination overrides.
- Prefer copying only declared source paths instead of a full repository.
- Preserve executable permissions when relevant.
- Require documentation fields before syncing a skill.

## Output

For each synced skill, produce:
- copied file list
- upstream repo URL
- upstream commit SHA
- documentation status
- any validation errors
