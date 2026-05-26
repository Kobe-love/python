---
name: automated-client-and-api-code-generation
description: Workflow command scaffold for automated-client-and-api-code-generation in python.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /automated-client-and-api-code-generation

Use this workflow when working on **automated-client-and-api-code-generation** in `python`.

## Goal

Regenerate client and API/model code from upstream sources or OpenAPI specs, updating many files in kubernetes/client/api, kubernetes/client/models, and related files.

## Common Files

- `kubernetes/client/api/*.py`
- `kubernetes/client/models/*.py`
- `kubernetes/.openapi-generator/swagger.json.sha256`
- `kubernetes/README.md`
- `kubernetes/__init__.py`
- `kubernetes/client/__init__.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Run code generation scripts/tools
- Update kubernetes/client/api/*.py and kubernetes/client/models/*.py
- Update kubernetes/.openapi-generator/swagger.json.sha256 and kubernetes/README.md
- Update kubernetes/__init__.py and kubernetes/client/__init__.py
- Update setup.py if needed

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.