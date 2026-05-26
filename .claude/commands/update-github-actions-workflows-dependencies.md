---
name: update-github-actions-workflows-dependencies
description: Workflow command scaffold for update-github-actions-workflows-dependencies in python.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-github-actions-workflows-dependencies

Use this workflow when working on **update-github-actions-workflows-dependencies** in `python`.

## Goal

Update GitHub Actions workflow files to bump versions of actions (e.g., setup-python, checkout, codecov-action) across multiple workflow YAMLs.

## Common Files

- `.github/workflows/e2e-master.yaml`
- `.github/workflows/e2e-release-*.yaml`
- `.github/workflows/test.yaml`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Edit .github/workflows/*.yaml to update action versions
- Commit all affected workflow files together
- Merge via pull request (often via Dependabot)

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.