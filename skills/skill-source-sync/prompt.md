You are syncing upstream source code into local Codex skill `scripts/` folders.

Objectives:
- hydrate missing script code from declared upstream repositories
- keep the sync reproducible
- generate concise, useful per-skill documentation
- preserve user changes unless explicitly told otherwise

Process:
1. Read the manifest.
2. Validate every declared path and repository field.
3. Clone or update upstream sources.
4. Copy only the declared files into the correct `scripts/` folder.
5. Record provenance metadata.
6. Update per-skill documentation.

Documentation requirements for each skill:
- purpose
- upstream repository URL
- branch or ref
- copied paths
- usage instructions
- refresh command
- last synced commit SHA

Safety requirements:
- no unsafe paths
- no destructive cleanup outside the target skill
- no secret material copied from upstream repos
