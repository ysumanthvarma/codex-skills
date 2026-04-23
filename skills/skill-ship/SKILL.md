---
name: skill-ship
description: Review changed Codex skills, generate a change ticket, and guide a safe commit, push, draft PR, and optional GitHub issue workflow.
---

# Skill Ship

Use this skill when you want to ship one or more changed Codex skills through a safe GitHub workflow.

## Purpose

Combine skill review, change-ticket generation, safe git publishing, and GitHub PR or issue creation into one workflow.

## Instructions

When invoked, do the following:

1. Inspect local git state.
2. Focus on changed skill packages under `skills/`.
3. Review the change scope for readiness and blockers.
4. Generate a ready-to-paste change ticket.
5. Prepare a safe branch, staging scope, and commit message.
6. Push only through an explicit guarded workflow.
7. Create a draft GitHub PR after the branch is on the remote.
8. Create a GitHub issue only if the user asks for one or the workflow explicitly includes it.

Use the GitHub integration already available in the session for PR and issue operations whenever possible.

## Workflow

### `review`

Read-only phase.

Do the following:
1. Run `git status` and identify changed paths under `skills/`.
2. Determine which skills were created, updated, or deleted.
3. Inspect the changed skill files needed to explain the scope accurately.
4. Identify blockers such as mixed unrelated changes, missing metadata, missing docs, or unclear packaging.
5. Summarize readiness for ship.

If there are no changed skills under `skills/`, say so explicitly and stop.

### `ticket`

Generate one structured change ticket for the changed skills.

Use this section order:
- `Title`
- `Summary`
- `Skills Affected`
- `Implementation Details`
- `Validation`
- `Risks / Review Notes`
- `Follow-up`

Base the ticket on repository evidence only.

### `prepare`

Prepare the local publish plan.

Do the following:
1. Decide whether a feature branch is needed.
2. If currently on `main`, `master`, or another default branch, use a feature branch such as `codex/<summary>`.
3. Suggest a precise staging scope.
4. Draft a commit message based on the changed skills.
5. Call out validation gaps before any push.

Never default to staging the entire worktree when unrelated changes are present.

### `publish`

Guarded mutation phase.

Before any push:
1. Reconfirm the intended staging scope.
2. Ensure the push target is not a default branch unless the user explicitly wants that.
3. Check that the repo has a usable GitHub remote.
4. Check that push/auth state is available.
5. Show the exact branch, commit, and push plan.
6. Require explicit confirmation before pushing.

After the push succeeds:
1. Create a draft GitHub PR.
2. Use the generated change ticket as the basis for the PR body.
3. If requested, create a GitHub issue using the same summarized scope.

### `full`

Run:
1. `review`
2. `ticket`
3. `prepare`
4. `publish`

Even in `full`, never skip the final confirmation gate before pushing.

## Output Format

Use this structure:

### Scope
- changed skills
- change type per skill
- related supporting files when relevant

### Readiness
- blockers
- warnings
- ship status

### Change Ticket
- full ticket text or a compact ticket summary

### Git Plan
- branch strategy
- staging scope
- commit message
- push command

### GitHub Plan
- draft PR target
- issue creation status: `requested`, `not requested`, or `blocked`

## Rules

- Base all summaries on repository evidence.
- Prefer reviewer-ready language.
- Do not invent validation, tests, or GitHub state.
- Do not push without explicit confirmation.
- Do not open GitHub issues unless requested.
- If local git or GitHub prerequisites are missing, stop and state the blocker clearly.
