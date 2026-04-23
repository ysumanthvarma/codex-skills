---
name: telegram-skill-update
description: Detect newly created Codex skills and send a concise Telegram group update using bot credentials from environment variables
---

# Telegram Skill Update

Use this skill when you want to notify a Telegram group that a new Codex skill was created.

## Purpose

Detect newly created skill packages and send a concise Telegram update using the Bot API.

## Instructions

When invoked, do the following:

1. Inspect the current git state.
2. Focus on newly created skill directories under `skills/`.
3. Read only the files needed to summarize each new skill accurately.
4. Compose a short Telegram message with the skill name and purpose.
5. Check that `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are available.
6. Send only after explicit confirmation unless the user explicitly asked to send now.

## Workflow

### `review`

Read-only phase.

Do the following:
1. Run `git status --short`.
2. Identify new skill directories under `skills/`.
3. Ignore modified-only skills.
4. If no new skills exist, say that no Telegram update is needed.

### `prepare`

Compose the Telegram message.

Do the following:
1. Extract the skill name and short purpose from each new skill.
2. Build a concise message for the target group.
3. Keep the message short and readable.

Preferred message format:

```text
New Codex skill created

- <skill-name>: <short purpose>
```

### `send`

Guarded mutation phase.

Before sending:
1. Check that `TELEGRAM_BOT_TOKEN` is set.
2. Check that `TELEGRAM_CHAT_ID` is set.
3. Show the final message body.
4. Require explicit confirmation before sending unless the user explicitly asked to send now.

Send the message with the Telegram Bot API `sendMessage` endpoint using:
- `chat_id` from `TELEGRAM_CHAT_ID`
- `text` from the prepared message

### `full`

Run:
1. `review`
2. `prepare`
3. `send`

Do not send unless the user explicitly asked to notify the group now.

## Output Format

Use this structure:

### Scope
- new skills detected
- supporting files used

### Telegram Message
- final message text

### Send Status
- `not needed`
- `ready`
- `blocked`
- `sent`

### Blockers
- missing environment variables
- no new skills found
- API send failure

## Rules

- Only notify for newly created skills.
- Do not notify for modified-only skills.
- Do not invent skill descriptions.
- Use repository evidence only.
- Stop if `TELEGRAM_BOT_TOKEN` or `TELEGRAM_CHAT_ID` is missing.
- Keep the Telegram message concise.
