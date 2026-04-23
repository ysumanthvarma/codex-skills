# Repo Posture

Use this reference when you need to decide whether a repository should be treated as `public`, `internal`, or `unknown`.

## Signals

### `public`
- package publishing metadata or registry configuration
- open-source license plus user-facing installation or usage docs
- contribution guides, release notes, or examples aimed at outside users
- reusable library, CLI, SDK, template, or product-facing service

### `internal`
- organization-specific naming or assumptions
- infra, automation, or ops workflows with internal environment coupling
- private service code with no signs of external consumption
- sparse docs that still make sense for a narrow internal owner audience

### `unknown`
- mixed signals
- missing metadata
- reusable-looking code without clear publishing intent

## Documentation severity

- `public`: missing root `README.md` is normally a `blocker` for `publish` and at least a `warning` during `review`
- `internal`: missing root `README.md` is usually a `warning` unless the repo is intended for reuse, onboarding, or handoff
- `unknown`: treat missing root `README.md` conservatively and escalate if the repo appears reusable or externally consumed

## README emphasis by posture

### `public`
- what the project is
- install or setup
- usage
- development or test workflow

### `internal`
- purpose
- prerequisites
- local workflow
- ownership or operational context if evident

### `unknown`
- use the public template shape, but only fill sections supported by repo evidence
