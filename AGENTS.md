# AGENTS.md

> AI agent instructions for this repository.
> Read this before making any changes to the codebase.
> If any instruction in this file is unclear, ambiguous, or conflicts with the repository state, stop and ask the human maintainer before proceeding.

See also: [Shared AI agent instructions for the YINI project family](../AGENTS.md)

## Project Overview

- **Name:** yini-parser-python
- **Package name:** yini-parser
- **Import name:** `yini_parser`
- **Language/runtime:** Python 3.10+
- **Package manager:** pip, using `pyproject.toml` and editable installs
- **Task runner:** Task (`Taskfile.yml`)
- **Framework/stack:** setuptools package, ANTLR4-generated parser, pytest, Ruff, mypy
- **Monorepo:** No
- **Status:** Alpha package for early testing and integration

This repository contains the official Python parser for YINI, an INI-inspired,
indentation-insensitive configuration format with explicit nested sections and
deterministic parsing.

## Repository Structure

```text
.
+-- src/
|   +-- yini_parser/               # Main package
|   |   +-- api/                   # Public load/loads API, errors, warnings
|   |   +-- core/                  # Parser visitor, value decoding, validation
|   |   +-- grammar/generated/     # ANTLR-generated Python sources
|   |   +-- utils/                 # Small internal utilities
|   +-- main.py                    # Sample CLI-style entrypoint
|   +-- dev.py                     # Development entrypoint
+-- grammar/v1.0.0-rc.6/           # Source ANTLR grammar files
+-- libs/antlr4/                   # Vendored ANTLR generator JAR and license
+-- tests/                         # pytest suite and golden smoke fixtures
+-- tests/fixtures/smoke-fixtures/ # .yini inputs paired with expected .json
+-- sample/                        # Small sample YINI/JSON files and images
+-- tools/                         # Adapter and project tooling scripts
+-- docs/                          # Development and maintainer documentation
+-- .github/workflows/             # Test and publish workflows
+-- pyproject.toml                 # Package metadata and tool configuration
+-- Taskfile.yml                   # Local development commands
+-- README.md                      # Human-facing project overview
```

## Commands

Install the package locally:

```bash
python -m pip install -e .
```

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Equivalent Task commands:

```bash
task install
task install-dev
```

Run the test suite with warnings treated as errors:

```bash
task test
```

Run one focused test file:

```bash
python -m pytest -v -W error tests/test_values.py
```

Run tests without promoting warnings to errors:

```bash
task test-relaxed
```

Run lint, formatting check, and type checking:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy
```

Run the full project check:

```bash
task check
```

Build distributions:

```bash
python -m build
task build
```

Run adapter checks:

```bash
task test-adapter
task test-adapter-strict
```

Regenerate ANTLR parser sources, only when grammar changes require it:

```bash
task antlr
```

`task antlr` is Windows-only in the current Taskfile and requires Java plus
`libs/antlr4/antlr4-4.13.2-complete.jar`.

## Required Checks

Before considering a change complete, run the smallest relevant checks first.

For documentation-only changes:

```bash
python -m pytest -v -W error tests/test_load.py
```

This may be skipped for pure instruction-file edits if no code, examples, or
user-facing behavior changed. Say clearly what was validated instead.

For focused parser or API changes:

```bash
python -m pytest -v -W error tests/<relevant-test-file>.py
```

For parsing behavior changes:

```bash
python -m pytest -v -W error
python -m ruff check .
python -m ruff format --check .
python -m mypy
```

For larger changes, release work, grammar changes, or public API changes:

```bash
task check
python -m build
python -m twine check dist/*
```

If a required check cannot be run, explain why and describe what was validated
instead.

## Code Style

Follow the existing style of the repository.

General rules:
- Prefer clear, simple, maintainable code.
- Prefer small, focused changes.
- Do not rewrite unrelated code.
- Do not reformat files unnecessarily.
- Keep public APIs stable unless the task explicitly asks for an API change.
- Add or update tests when behavior changes.
- Prefer explicit, readable logic over clever or overly compact code.
- Preserve existing naming conventions, file layout, and architectural patterns.
- Keep runtime code compatible with Python 3.10 and newer.
- Use the standard library before adding dependencies.
- Keep public exports in `src/yini_parser/__init__.py` intentional and minimal.

Ruff excludes `src/yini_parser/grammar/generated/`. Do not make style-only edits
to generated ANTLR files.

## Testing

When changing behavior:
- Add or update focused tests near the affected behavior.
- Keep tests deterministic.
- Do not remove failing tests. Fix the issue or clearly report why the test is failing.
- Preserve strict-mode and lenient-mode separation in tests.
- Cover warning behavior when a lenient parse accepts something strict mode rejects.
- Add or update golden smoke fixtures when fixture-backed parsing behavior changes.
- Avoid broad fixture updates unless the behavior change intentionally affects them.

The smoke fixtures pair `.smoke.yini` inputs with `.smoke.json` expected output
under `tests/fixtures/smoke-fixtures/`.

## Parser And Grammar Guidance

YINI values clarity, readability, predictability, explicit structure, and
deterministic parsing.

When changing parser behavior:
- Make behavior match the current YINI specification.
- Prefer precise diagnostics over vague errors.
- Keep syntax examples human-readable.
- Avoid implicit or magical behavior.
- Preserve the difference between strict mode and lenient mode.
- Be careful with duplicate keys, repeated sections, key/section collisions,
  comments, ignored lines, inline objects, string concatenation, and mode
  declarations.

ANTLR source grammar files live in `grammar/v1.0.0-rc.6/`. Generated Python
parser files live in `src/yini_parser/grammar/generated/`.

Do not hand-edit generated files unless the task is specifically about generated
output and the maintainer accepts that regeneration is not available. Prefer
changing the grammar and running `task antlr`.

## Documentation Guidance

Update documentation when a change affects:
- public APIs,
- command-line usage,
- configuration,
- installation,
- examples,
- parser behavior visible to users.

Keep documentation concise and consistent with the existing tone. The README is
user-facing; `docs/Development-Setup.md` and `docs/Maintainer-Doc.md` are for
contributors and maintainers.

## Dependency Policy

Do not add new runtime dependencies unless clearly necessary.

Before adding a dependency, prefer:
1. Existing project utilities.
2. Standard library functionality.
3. Small local helper functions.

If a new dependency is necessary, explain why it is justified.

The current runtime dependency is pinned:

```text
antlr4-python3-runtime==4.13.2
```

Keep the ANTLR runtime version aligned with the vendored generator JAR unless
the maintainer explicitly chooses a version change.

## Safety and Scope Boundaries

### Always Do

- Run tests before submitting any change.
- Match the code patterns in the file you are editing.
- Keep changes focused - one concern per PR.
- When editing Markdown files, if a line introduces a bulleted list and ends with a colon (`:`), place the first bullet immediately on the next line. Do not insert a blank line between the introductory line and the first bullet.

### Ask First

- Before adding a new dependency.
- Before changing the public API or exported types.
- Before modifying CI/CD configuration.
- Before refactoring shared utilities used across multiple modules.

### Never Do

Do not modify:
- secrets,
- credentials,
- private keys,
- `.env` files,
- generated files unless generation is part of the requested task,
- vendored dependencies,
- lockfiles unless dependency changes require it,
- unrelated formatting or whitespace.

Do not perform destructive operations such as:
- deleting large parts of the repository,
- resetting history,
- force-pushing,
- creating releases,
- publishing packages.

Do not create commits, tags, branches, or releases unless explicitly requested.

Release publishing is handled through `.github/workflows/publish-to-pypi.yml`
using PyPI Trusted Publishing. Do not trigger or alter publishing workflows
unless the maintainer asks for release work.

## Project-Specific Notes

- The public loading API is `load`, `loads`, and `YiniParseError`.
- The package is alpha; still avoid unnecessary public API churn.
- Generated parser files are included so package users do not need Java or the
  ANTLR generator.
- Java is only needed by maintainers regenerating parser sources.
- Prefer Taskfile commands when available because CI and docs use them.
- When changing examples, keep YINI syntax readable and explicit.
- When changing diagnostics, prefer messages that help users locate and fix the
  specific parse issue.
