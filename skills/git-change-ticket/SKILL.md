---
name: git-change-ticket
description: Generate a structured git change ticket for created or updated Codex skills in the current repository.
---

# Git Change Ticket

Use this skill when you need a ready-to-paste change ticket for skill work in the current git repository.

## Purpose

Turn local git changes for Codex skills into a concise, reviewable change ticket.

## Instructions

When invoked, do the following:

1. Inspect the current repository state using git.
2. Focus on changes under `skills/`.
3. Identify each affected skill directory.
4. Classify each skill change as:
   - `created`
   - `updated`
   - `deleted`
5. Read only the files needed to summarize the changed skills accurately.
6. Generate a single structured ticket that can be pasted into a PR, issue, or change request.

If relevant supporting files outside `skills/` changed, include them only when they materially explain the skill changes. Typical examples are root `README.md` updates or shared metadata changes.

## Workflow

### Scope Detection

Collect:
- `git status --short`
- staged vs unstaged scope when relevant
- changed paths under `skills/`
- related non-skill files only if they directly support the skill changes

### Skill Analysis

For each changed skill:
- inspect `SKILL.md`
- inspect `prompt.md` if present
- inspect `skill.yaml` if present
- inspect `agents/openai.yaml` or `references/` only when needed to explain the change

Summarize:
- what the skill does
- why it was added or changed
- notable workflow, policy, or packaging changes

### Ticket Output

Use this exact section order:

#### Title

#### Summary

#### Skills Affected

For each skill include:
- skill name
- change type
- short purpose
- notable files changed

#### Implementation Details

Include:
- key workflow or behavior changes
- packaging or metadata changes
- related repo-level documentation changes if applicable

#### Validation

State:
- what was verified
- what was not verified
- whether validation gaps remain

#### Risks / Review Notes

Call out:
- incomplete packaging
- missing validation
- policy or workflow ambiguity
- installation or discoverability gaps

#### Follow-up

List only real next steps. If none, say `None`.

## Rules

- Base the ticket on repository evidence only.
- Do not invent tests, validation, or business context.
- If there are no changed skills under `skills/`, say that no skill ticket is needed.
- Keep the output concise but directly usable.
- Prefer reviewer-oriented language over brainstorming language.
