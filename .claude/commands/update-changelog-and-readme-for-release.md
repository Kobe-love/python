---
name: update-changelog-and-readme-for-release
description: Workflow command scaffold for update-changelog-and-readme-for-release in python.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-changelog-and-readme-for-release

Use this workflow when working on **update-changelog-and-readme-for-release** in `python`.

## Goal

Update the CHANGELOG.md and README.md files to reflect a new release or version, often including compatibility matrix updates and release notes.

## Common Files

- `CHANGELOG.md`
- `README.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Edit CHANGELOG.md with release notes or version changes
- Edit README.md to update compatibility matrix or maintenance status
- Commit both files together
- Merge via pull request

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.