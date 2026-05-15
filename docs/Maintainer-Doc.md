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
```
cd yini-parser-python
```

2. Install the package in editable development mode:
```
task install-dev
```

3. Run the full project check:
```
task check
```

4. Expected result should be something like this:
```
All checks passed!
Success: no issues found
88 passed
```

---

## Clean old build artifacts

Use the project cleanup task:
```
task clean
```

---

## Build the package

Build both the source distribution and wheel:
```
task build
```

---

## Check the built distributions

Run:
```
task check-dist
```

Expected result:
```
PASSED
```

---

## Publishing from GitHub

Releases can also be published from GitHub Actions using PyPI Trusted Publishing.

This is preferred over storing long-lived PyPI API tokens in GitHub secrets.

Basic idea:
1. Configure a Trusted Publisher for the project on PyPI.
2. Add a GitHub Actions release workflow.
3. Trigger the workflow from a version tag, for example `v0.1.0a2`.
4. GitHub builds the package and publishes it to PyPI.

Manual publishing with `twine upload dist/*` is still supported as a fallback.

---

## Publishing manually

Only upload to real PyPI after:
- `task check` passes.
- `task build` succeeds.
- `task check-dist` passes.
- TestPyPI install has been tested successfully.
- Basic import and parsing have been tested in a clean environment.

Upload to real PyPI:
```
python -m twine upload dist/*
```

For the password, paste the real PyPI API token.

After a successful upload, PyPI will show a project URL similar to:
```
https://pypi.org/project/yini-parser/<version>/
```

---

**^YINI ≡**  
> YINI is a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, and predictable parsing.

[yini-lang.org](https://yini-lang.org/?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python) · [YINI-lang on GitHub](https://github.com/YINI-lang)  
