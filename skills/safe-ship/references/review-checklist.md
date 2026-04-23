# Review Checklist

Use this reference when the main workflow needs more detailed guidance.

## Developer review

Look for:
- missing tests for changed behavior
- API or interface changes without obvious downstream updates
- partial refactors, dead code, stale TODOs, or inconsistent naming
- documentation drift for setup, usage, or architecture

## SRE review

Look for:
- retry, timeout, concurrency, or backoff changes
- config drift or default changes
- logging, metrics, tracing, or alerting regressions
- migration, deployment, rollback, or compatibility risks
- performance regressions or new failure modes

## Security review

Look for:
- secrets, tokens, keys, `.env` files, or private artifacts
- auth or authorization changes
- unsafe shell execution, deserialization, or input handling
- widened network exposure or permission scope
- dependency or supply-chain risk indicators

## Severity

- `blocker`: unsafe to commit or push without change
- `warning`: should be addressed or explicitly accepted
- `note`: useful context but not release-blocking by itself

## Publish block conditions

Block `publish` when:
- secrets or credentials are detected
- unresolved high-severity findings remain
- the repo is in a conflicted, unmerged, or mid-rebase state
- the push targets a protected or default branch without explicit intent
- a `public` repo is missing essential user-facing documentation for the shipped change
