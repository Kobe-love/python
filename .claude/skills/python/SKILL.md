```markdown
# python Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill teaches you the key development patterns, coding conventions, and collaborative workflows used in the `python` repository. The codebase is Python-based, with no specific framework detected, and focuses on maintainable, modular code. It features automated code generation, regular documentation updates, and robust example management. The repository follows clear conventions for file naming, imports, exports, and testing, and uses a set of repeatable workflows to streamline contributions and releases.

## Coding Conventions

- **File Naming:**  
  All files use `snake_case` for consistency and readability.
  ```
  # Good
  my_module.py
  api_client.py

  # Bad
  MyModule.py
  apiClient.py
  ```

- **Import Style:**  
  Relative imports are preferred within packages.
  ```python
  # In kubernetes/client/api/v1_api.py
  from ..models import v1_pod
  ```

- **Export Style:**  
  Named exports are used; modules explicitly define what is exported.
  ```python
  # In __init__.py
  from .api_client import ApiClient
  __all__ = ["ApiClient"]
  ```

- **Commit Messages:**  
  Freeform, concise messages (~46 characters on average), no enforced prefix.

## Workflows

### Update Changelog and README for Release
**Trigger:** When preparing or finalizing a new release or version update  
**Command:** `/release-update`

1. Edit `CHANGELOG.md` with release notes or version changes.
2. Edit `README.md` to update the compatibility matrix or maintenance status.
3. Commit both files together.
4. Merge via pull request.

**Example:**
```sh
# Edit files
git add CHANGELOG.md README.md
git commit -m "Update changelog and README for v1.2.3"
git push
# Open a pull request
```

---

### Automated Client and API Code Generation
**Trigger:** When upstream API changes or new OpenAPI specs are released  
**Command:** `/regenerate-client`

1. Run code generation scripts/tools.
2. Update `kubernetes/client/api/*.py` and `kubernetes/client/models/*.py`.
3. Update `kubernetes/.openapi-generator/swagger.json.sha256` and `kubernetes/README.md`.
4. Update `kubernetes/__init__.py` and `kubernetes/client/__init__.py`.
5. Update `setup.py` if needed.
6. Commit all generated files together.
7. Merge via pull request.

**Example:**
```sh
# Run codegen tool (example)
python scripts/generate_client.py
git add kubernetes/client/api/ kubernetes/client/models/ \
        kubernetes/.openapi-generator/swagger.json.sha256 \
        kubernetes/README.md kubernetes/__init__.py \
        kubernetes/client/__init__.py setup.py
git commit -m "Regenerate client and models for API v1.23"
git push
# Open a pull request
```

---

### Update GitHub Actions Workflows Dependencies
**Trigger:** When a new version of a GitHub Action dependency is released or security updates are needed  
**Command:** `/update-actions`

1. Edit `.github/workflows/*.yaml` to update action versions.
2. Commit all affected workflow files together.
3. Merge via pull request (often via Dependabot).

**Example:**
```yaml
# In .github/workflows/test.yaml
- uses: actions/setup-python@v4  # Bump to latest
```
```sh
git add .github/workflows/
git commit -m "Update GitHub Actions dependencies"
git push
# Open a pull request
```

---

### Add or Update Examples
**Trigger:** When demonstrating new features or improving documentation/examples  
**Command:** `/add-example`

1. Create or update Python scripts in `examples/`.
2. Create or update YAML files in `examples/` or subdirectories.
3. Commit related files together.
4. Merge via pull request.

**Example:**
```sh
# Add a new example
cp my_new_example.py examples/
git add examples/my_new_example.py
git commit -m "Add example for new feature X"
git push
# Open a pull request
```

## Testing Patterns

- **Framework:** Unknown (not explicitly detected).
- **File Pattern:** Test files match `*.test.*` (e.g., `foo.test.py`).
- **Example:**
  ```
  tests/
    test_api.test.py
    test_models.test.py
  ```
- Tests are likely run using standard Python test runners (e.g., `pytest` or `unittest`), but check project documentation for specifics.

## Commands

| Command           | Purpose                                                      |
|-------------------|--------------------------------------------------------------|
| /release-update   | Update CHANGELOG and README for a new release                |
| /regenerate-client| Regenerate client and API/model code from upstream specs     |
| /update-actions   | Update GitHub Actions workflow dependencies                  |
| /add-example      | Add or update example scripts or YAML manifests              |
```