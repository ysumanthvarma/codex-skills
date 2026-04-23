---
name: safe-ship
description: Review git repo changes from developer, SRE, and security perspectives, then prepare a safe commit and push workflow.
---

# Safe Ship

Use this skill when you need to inspect local git changes before committing or pushing.

The skill works in four modes:

1. `review`
2. `prepare`
3. `publish`
4. `full`

Default to `review` if the user does not specify a mode.

## Goals

1. Review changes from developer, SRE, and security perspectives.
2. Infer whether the repository should be treated as public-facing or internal.
3. Identify blockers before changes are committed or pushed.
4. Prepare a safe commit scope and commit message.
5. Push only through an explicit guarded workflow.

## Workflow

### `review`

Read-only phase.

Do the following:
1. Inspect git status, staged vs unstaged changes, current branch, and changed files.
2. Infer repo posture as `public`, `internal`, or `unknown` and state the evidence.
3. Summarize the change scope.
4. Review from developer, SRE, and security perspectives.
5. Classify findings as `blocker`, `warning`, or `note`.
6. Decide readiness as `not ready`, `ready with caution`, or `ready`.
7. Check whether root `README.md` exists and report its status.

For review criteria and posture heuristics:
- Read [references/review-checklist.md](references/review-checklist.md) when you need the detailed review rubric.
- Read [references/repo-posture.md](references/repo-posture.md) when posture is unclear or documentation severity depends on repo type.

### `prepare`

Mutation phase for low-risk repo hygiene and commit preparation.

Do the following:
1. Start with the `review` output.
2. Suggest commit scope.
Include:
- which files should be included
- which files should be excluded
- whether unrelated changes should be split
3. Draft a commit message using the actual scope.
4. If root `README.md` is missing, create a minimal factual `README.md`.
5. If `README.md` exists, do not overwrite it automatically.
6. If existing docs appear stale, flag them for review instead of rewriting them unless the user explicitly asks.

When generating a missing `README.md`, keep it conservative and evidence-based. Use this baseline structure:

```md
# <Project Name>

## Overview

## Requirements

## Setup

## Usage

## Development

## Structure
```

Only include sections that can be supported by repository evidence. Do not invent features, commands, or architecture details.

If documentation shape depends on repo posture, read [references/repo-posture.md](references/repo-posture.md).

### `publish`

Guarded publish phase.

Before any push:
1. Re-run readiness checks.
2. Check for merge conflicts, rebase/cherry-pick state, and unmerged paths.
3. Check current branch and warn on default or protected branch targets such as `main` or `master`.
4. Check whether the branch is ahead or behind its remote.
5. Raise the validation bar for `public` repos. Prefer to run obvious tests, lint, or build checks when the repo exposes them.
6. For `internal` repos, run validation that is proportionate to the repo risk and available evidence.
7. Show the exact commit and push commands before running them.
8. Require explicit confirmation before any push.

For block conditions and push thresholds, read [references/review-checklist.md](references/review-checklist.md).

### `full`

Run `review`, then `prepare`, then `publish`.

Even in `full`, never skip the final push confirmation gate.

## Output Format

Use this structure:

### Scope
- changed files and high-level summary
- repo posture: `public`, `internal`, or `unknown`
- posture evidence

### Developer Findings
- list findings with severity

### SRE Findings
- list findings with severity

### Security Findings
- list findings with severity

### Documentation
- report whether `README.md` exists
- if missing, state whether one was created in `prepare`
- state whether current documentation is sufficient for the inferred repo posture

### Readiness
- `not ready`, `ready with caution`, or `ready`

### Commit Plan
- files to include
- files to exclude
- suggested commit message

### Publish Plan
- pre-push checks
- exact next command

## Safety Rules

1. Never auto-stage all files by default when unrelated or risky files are present.
2. Never commit or push secrets, credentials, `.env` files, private keys, or obviously sensitive artifacts.
3. Never rewrite user-authored documentation unless explicitly asked.
4. Treat public-facing changes more strictly than internal-only changes when deciding readiness.
5. Prefer suggesting commands over executing risky ones.
6. If the repo state is ambiguous, state the assumption and keep the workflow conservative.

## Typical Triggers

Use this skill when the user asks to:
- review local repo changes before committing
- sanity check a branch before push
- prepare a clean commit from mixed local changes
- assess change risk from developer, SRE, and security perspectives
- apply stricter release hygiene to public repositories than to internal ones
- create a missing `README.md` as part of safe commit preparation
