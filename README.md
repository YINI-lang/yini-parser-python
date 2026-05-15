# yini-parser-python

The official Python parser for **YINI** (by the YINI-lang project) — a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, comments, and predictable parsing.  

> **Status:** Alpha.  
> This parser is intended for early testing and integration. The public API and edge-case behavior may still change before `1.0.0`.

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
```
import yini_parser
```

---

## Quick Start

Example YINI file:

```yini
// A small, practical YINI config.

// The App section starts here.
^ App
name = "Demo App"
version = 1.2
features = ["search", "logs"]
debug = false    // on/off, yes/no would work too.
pageSize = 25

    // Another section, nested under App.
    ^^ Server
    host = "localhost"
    port = 8080    # Can comment with # too.
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

## Development

For local development:

```bash
python -m pip install -e ".[dev]"
```

or, if using the project Taskfile:

```bash
task install-dev
```

---

## Tests

The `tests/` directory contains a focused implementation-local test suite, including:
- Tests for the public API.
- Key semantic tests.
- Smoke/golden tests.
- Parser behavior tests for comments, values, sections, strict mode, conflicts, inline objects, and string concatenation.

Run the test suite with:

```bash
python -m pytest -v
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
