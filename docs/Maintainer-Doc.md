# Maintainer Documentation

This document describes the maintainer workflow for building, checking, and publishing new releases of `yini-parser-python`.

The package is published on PyPI as:

```text
yini-parser
```

The import package name is:
```python
import yini_parser
```

---

## Release checklist

Before publishing a new release, make sure that:
- The version number has been updated in pyproject.toml.
- The changelog or release notes have been updated, if applicable.
- The README is accurate for the current release.
- The package builds successfully.
- The package metadata passes twine check.
- The package has been tested in a clean virtual environment.
- The final package has been uploaded to real PyPI.

---

## Version numbering

The package version is defined in `pyproject.toml`:

For Python-compatible pre-release versions:
```
0.1.0a1
0.1.0a2
0.1.0a3
```

For release candidates:
```
0.1.0rc1
0.1.0rc2
```

For stable releases:
```
0.1.0
1.0.0
```

---

### PyPI versions are immutable

Important: Once a version has been uploaded to PyPI, the same version cannot be uploaded again. If a fix is needed, bump the version number.

---

## Local preparation

1. Start from the project root:

```bash
cd yini-parser-python
```

2. Install the package in editable development mode:

```bash
task install-dev
```

3. Run the full project check:

```bash
task check
```

4. Expected result should be something like this:

```text
All checks passed!
Success: no issues found
88 passed
```

---

## Option A - Publish manually from your machine

Use this option when you want to build and upload the package directly from your local machine.

From the repo root, install or update the build tools:

```bash
python -m pip install --upgrade build twine
```

Clean old builds.

In Command Prompt:

```bat
rmdir /s /q dist build
```

In PowerShell:

```powershell
Remove-Item -Recurse -Force dist, build -ErrorAction SilentlyContinue
```

Build both the source distribution and wheel:

```bash
python -m build
```

Check the package metadata:

```bash
python -m twine check dist/*
```

Upload to PyPI:

```bash
python -m twine upload dist/*
```

When prompted, use:

```text
Username: __token__
Password: <your PyPI API token>
```

The token should come from PyPI. Prefer a project-scoped API token for `yini-parser` if the project already exists.

After a successful upload, PyPI will show a project URL similar to:

```text
https://pypi.org/project/yini-parser/<version>/
```

---

## Option B - Publish through GitHub Actions with a PyPI token

Use this option when publishing a GitHub release should build and upload the package automatically.

Add a workflow such as `.github/workflows/publish.yml`:

```yaml
name: Publish Python package

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest

    permissions:
      contents: read

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install build tools
        run: python -m pip install --upgrade build twine

      - name: Build package
        run: python -m build

      - name: Check package
        run: python -m twine check dist/*

      - name: Publish to PyPI
        run: python -m twine upload dist/*
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
```

Then add the token to GitHub:

1. Go to the repository on GitHub.
2. Open `Settings -> Secrets and variables -> Actions`.
3. Choose `New repository secret`.
4. Add a secret named `PYPI_API_TOKEN`.
5. Paste the PyPI token as the secret value.

After this is configured, drafting and publishing a GitHub release should trigger the workflow.

---

## Better modern option - PyPI Trusted Publishing

Trusted Publishing is the cleaner modern approach. It lets GitHub Actions publish with OpenID Connect (OIDC), instead of storing a long-lived PyPI API token in GitHub secrets.

With this flow, GitHub Actions sends an OIDC token to PyPI. PyPI checks that token against the trusted publisher configuration and exchanges it for a short-lived API token.

Add a workflow such as `.github/workflows/publish.yml`:

```yaml
name: Publish Python package

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install build
        run: python -m pip install --upgrade build

      - name: Build package
        run: python -m build

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
```

This only works after configuring the trusted publisher on PyPI. PyPI requires a trusted publisher to be configured for the associated platform before publishing through it.

For this project, configure PyPI with approximately:

```text
Owner: YINI-lang or your GitHub username
Repository: yini-parser-python
Workflow name: publish.yml
Environment: optional, only if the workflow uses one
```

The workflow filename must match exactly. For example, if PyPI says `publish.yml`, the file should be `.github/workflows/publish.yml`.

---

## Final release gate

Only upload to real PyPI after:
- `task check` passes.
- `python -m build` succeeds.
- `python -m twine check dist/*` passes.
- The package has been tested in a clean virtual environment.
- Basic import and parsing have been tested from the built package.

---

**^YINI ≡**  
> YINI is a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, and predictable parsing.

[yini-lang.org](https://yini-lang.org/?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python) · [YINI-lang on GitHub](https://github.com/YINI-lang)  
