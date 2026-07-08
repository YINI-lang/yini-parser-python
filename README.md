# yini-parser-python

The official Python parser for **YINI** (by the YINI-lang project) — a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, comments, and predictable parsing.  

[![YINI Test Suite](https://github.com/YINI-lang/yini-parser-python/actions/workflows/yini-test-suite.yml/badge.svg)](https://github.com/YINI-lang/yini-parser-python/actions/workflows/yini-test-suite.yml)

> **Status:** Beta.  
> This parser is intended for early testing and integration. The public API and edge-case behavior may still change before `1.0.0`.

## Project links

- [YINI homepage](https://yini-lang.org?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=readme_project_links)
- [YINI specification](https://yini-lang.org/refs/specification?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=readme_project_links)
- [GitHub repository](https://github.com/YINI-lang/yini-parser-python)
- [Bug reports and issues](https://github.com/YINI-lang/yini-parser-python/issues)

---

## Installation

Install from PyPI:

```bash
pip install yini-parser
```

The package name on PyPI is:
```
yini-parser
```

The Python import name is:
```python
import yini_parser
```

---

## Copy-paste test

Test the package in under one minute.

Parse a YINI string:

```python
from yini_parser import loads

data = loads("""
^ Application
name = "demo"

^^ Server
port = 8080
""")

print(data)
```

Expected output:

```python
{'Application': {'name': 'demo', 'Server': {'port': 8080}}}
```

---

## Quick Start

Example lenient-mode (default) YINI file:

```ini
// A small, practical YINI config.

// The App section starts here.
^ App
name = "Demo App"
version = 1.2
features = ["search", "logs"]
debug = false    // off/no would work too.
pageSize = 25

    // Nested under App. Indentation is optional and used for readability.
    ^^ Server
    host = "localhost"
    port = 8080    # YINI also supports # comments.
    useTLS = off
```

Parse a YINI file:

```python
from yini_parser import load

data = load("sample/basic.yini")

print(data["App"]["name"])  # Demo App
print(data["App"]["Server"]["port"])  # 8080
```

Parse a YINI string:

```python
from yini_parser import loads

data = loads("""
^ App
name = "Demo App"
version = 1.2
debug = false
""")

print(data["App"]["name"])  # Demo App
```

Use `load(...)` to parse a file and `loads(...)` to parse a string.

See the [YINI specification and documentation](https://yini-lang.org/refs/specification?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=readme).

---

## Examples

Runnable example projects are available in the [YINI demo apps repository](https://github.com/YINI-lang/yini-demo-apps/tree/main/python).

The Python examples show how to install `yini-parser`, load `.yini` files, and access parsed configuration data in small practical scripts.

- [Python basic demo](https://github.com/YINI-lang/yini-demo-apps/tree/main/python/basic)
- [Python medium demo](https://github.com/YINI-lang/yini-demo-apps/tree/main/python/medium)

---

## Why YINI?

YINI is intended for configuration files where human readability, explicit structure, and predictable parsing are more important than minimal syntax or maximum flexibility.

Compared with common configuration formats:
- **INI:** YINI supports clearer nested sections and typed values.
- **JSON:** YINI supports comments and is easier to edit by hand.
- **YAML:** YINI does not use indentation to define structure.
- **TOML:** YINI uses explicit section markers for hierarchy instead of dotted table names.

The same small configuration can be written in several formats:

### YINI
```ini
^ Application
name = 'demo'
environment = 'dev'

^^ Server
host = 'localhost'
ports = [8080, 8081]

^^^ TLS
enabled = true
mode = 'optional'
```

- `Application` contains the top-level application settings.
- `Server` is nested under `Application`.
- `TLS` is nested under `Server`.
- The section markers `^` make the nesting explicit. Indentation is optional and not required for structure.
- Strings can use either `'` or `"`.

### JSON
```json
{
  "Application": {
    "name": "demo",
    "environment": "dev",
    "Server": {
      "host": "localhost",
      "ports": [8080, 8081],
      "TLS": {
        "enabled": true,
        "mode": "optional"
      }
    }
  }
}
```

### YAML
```yaml
Application:
  name: demo
  environment: dev
  Server:
    host: localhost
    ports:
      - 8080
      - 8081
    TLS:
      enabled: true
      mode: optional
```

### TOML
```toml
[Application]
name = "demo"
environment = "dev"

[Application.Server]
host = "localhost"
ports = [8080, 8081]

[Application.Server.TLS]
enabled = true
mode = "optional"
```

YINI may not be the right choice when you need mature ecosystem support, existing schema tooling, or maximum compatibility with infrastructure that already expects JSON, YAML, or TOML. The format and parser are still beta-stage and best suited for testing, experiments, and early integration feedback.

---

## Parser implementation

`yini-parser` uses Python parser code generated by ANTLR.

The generated Python parser files are included in the package. Users do **not** need Java or the ANTLR generator tool to install or use `yini-parser`.

The package depends on `antlr4-python3-runtime` because the generated lexer and parser use the ANTLR Python runtime while parsing.

The ANTLR generator JAR is only needed by maintainers when regenerating parser sources from the grammar, and it is not included in the published Python package.

---

## Feedback and bug reports

If you find a problem, please open an issue on GitHub:

- [Report a bug or issue](https://github.com/YINI-lang/yini-parser-python/issues)

When reporting parser behavior, it is helpful to include:
- The YINI input that caused the issue.
- The expected result.
- The actual result or error message.
- The installed `yini-parser` version.
- The Python version used.

---

## Development

For local development:

```bash
python -m pip install -e ".[dev]"
```

or, if using the project Taskfile:

```bash
task install-dev
```

Generate the ANTLR parser sources:

```bash
task antlr
```

Run the full project check:

```bash
task check
```

This runs:
- The test suite with warnings treated as errors,
- Ruff lint checks,
- Ruff formatting checks,
- mypy type checking.

---

## Tests

The `tests/` directory contains a focused implementation-local test suite, including tests for:
- The public loading API.
- Values, numbers, strings, lists, and inline objects, including lenient `=` separators and strict `:` enforcement.
- Sections, nested sections, section depth, and section marker separators.
- Strict and lenient parser behavior.
- `@yini strict` and `@yini lenient` mode declarations.
- Duplicate keys, repeated sections, and key/section collisions.
- String concatenation.
- Comments, ignored lines, smoke fixtures, and warning/error behavior.

Run the test suite with:

```bash
python -m pytest -v -W error
```

or, if using the project Taskfile:

```bash
task test
```

Run the full project check with:

```bash
task check
```

---

## 🧪 Testing and Stability

This parser is covered by smoke, integration, and regression tests.

It has also been run against the shared external
[`yini-test-suite`](https://github.com/YINI-lang/yini-test-suite) conformance suite
for YINI Specification 1.0.0 RC 6.

Current conformance result:
- 360 passed
- 0 failed
- Lenient and strict modes covered
- Smoke and golden test suites covered

---

## Links

- [YINI specification](https://yini-lang.org/refs/specification?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=readme)
- [YINI homepage](https://yini-lang.org?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=readme)
- [YINI-lang on GitHub](https://github.com/YINI-lang)
- [yini-parser on PyPI](https://pypi.org/project/yini-parser/)


---

**^YINI ≡**  
> YINI is a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, and predictable parsing.
> 
> It has a formal specification and a defined grammar.

[yini-lang.org](https://yini-lang.org/?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=readme_footer) · [YINI-lang on GitHub](https://github.com/YINI-lang)  
