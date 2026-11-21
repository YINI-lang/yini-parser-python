# yini-parser-python

The official Python parser for **YINI**, a configuration format inspired by INI.
YINI supports nested sections, comments, and values such as numbers, booleans,
lists, and objects. Section markers define the nesting, so indentation is optional.

Useful links:
- [Try YINI in Playground](https://yini-lang.org/playground/?utm_source=github&utm_campaign=yini_parser_python&utm_content=readme_useful_links&utm_medium=referral)
- [yini-parser on GitHub](https://github.com/YINI-lang/yini-parser-python)
- [Report an Issue or give Feedback](https://github.com/YINI-lang/yini-parser-python/issues)

[![YINI Test Suite](https://github.com/YINI-lang/yini-parser-python/actions/workflows/yini-test-suite.yml/badge.svg)](https://github.com/YINI-lang/yini-parser-python/actions/workflows/yini-test-suite.yml)
[![PyPI version](https://img.shields.io/pypi/v/yini-parser)](https://pypi.org/project/yini-parser/)
[![Python versions](https://img.shields.io/pypi/pyversions/yini-parser)](https://pypi.org/project/yini-parser/)

Requires **Python 3.10 or newer**. This parser is a release candidate and targets
**YINI Specification 1.0.0 RC7**. See the [changelog](CHANGELOG.md) for release details.

---

## Installation

Install from PyPI, allowing prerelease versions:

```bash
python -m pip install --pre yini-parser
```

The [--pre option](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-pre)
lets pip select release candidates and other prereleases.
To upgrade an existing installation, add `--upgrade`.

The package name is `yini-parser`; the Python import name is `yini_parser`:

```python
import yini_parser
```

---

## Quick start

Save this configuration as `config.yini`:

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

Load it in Python:

```python
from yini_parser import load

data = load("config.yini")

print(data["App"]["name"])  # Demo App
print(data["App"]["Server"]["port"])  # 8080
```

The result is a Python dictionary. Here is the same data shown as JSON:

```json
{
  "App": {
    "name": "Demo App",
    "version": 1.2,
    "features": ["search", "logs"],
    "debug": false,
    "pageSize": 25,
    "Server": {
      "host": "localhost",
      "port": 8080,
      "useTLS": false
    }
  }
}
```

To parse text directly, use `loads`:

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

## API

| Function | Input | Result |
| --- | --- | --- |
| `load(path, strict=False)` | A UTF-8 file, given as a string path or `pathlib.Path`. | A Python dictionary. |
| `loads(text, strict=False)` | A string containing YINI text. | A Python dictionary. |

Sections and inline objects become dictionaries. Lists become Python lists;
strings, numbers, and booleans become the corresponding Python types. YINI `null`
becomes `None`.

Invalid YINI raises `YiniParseError`. Catch it to report a parse error:

```python
from yini_parser import YiniParseError, load

try:
    data = load("config.yini")
except YiniParseError as error:
    print(f"Could not parse config.yini: {error}")
```

The error message includes a line and column when available. File access and
UTF-8 decoding errors use Python's standard exceptions.

## Strict and lenient parsing

Both functions use lenient mode by default. Pass `strict=True` to apply the
strict rules. A strict document needs exactly one top-level section and a final
`/END` marker:

```python
from yini_parser import loads

data = loads('^ App\nname = "Demo App"\n/END\n', strict=True)
```

Some common differences are:

| Rule | Lenient mode | Strict mode |
| --- | --- | --- |
| `/END` marker | Optional. | Required. |
| Members outside an explicit section | Allowed at the document root. | Rejected. |
| Empty member value after `=` | Becomes `None` with a warning. | Rejected. |
| Duplicate key | Keeps the first value and warns. | Rejected. |
| Trailing comma in a list or inline object | Allowed. | Rejected. |
| Inline object separator | `:` or `=`. | `:` only. |

An explicit `@yini strict` declaration is rejected in lenient mode. An
`@yini lenient` declaration produces a warning in strict mode, and all strict
validation rules still apply. Duplicate sections under the same parent are
errors in both modes. A declaration does not switch the parser's mode.

Warnings use Python's standard `warnings` system and the `YiniParseWarning`
category, available from `yini_parser.api`. Mixed line endings and a shebang
(`#!`) outside the start of the first line produce warnings in lenient mode and
errors in strict mode. The `@include` directive is reserved and is rejected in
both modes.

The deprecated `%` binary prefix remains valid in both modes and produces a
warning recommending `0b` instead.

Inside backticked keys and section names, write `\\` for one literal backslash.

See the [YINI specification and documentation](https://yini-lang.org/refs/specification?utm_source=github&utm_campaign=yini_parser_python&utm_content=readme&utm_medium=referral).

---

## Examples

This repository includes three runnable examples in [examples/](examples/).

Each Python script reads a `.yini` file beside it, so you can compare the input
with the code that loads it.

After cloning this repository, install the package locally:

```sh
python -m pip install -e .
```

Then run the examples from the repository root:
```sh
python examples/example1.py
python examples/example2.py
python examples/example3.py
```

What they show:
- [example1.py](examples/example1.py) reads `basic.yini` and prints basic app settings.
- [example2.py](examples/example2.py) reads `nested.yini` and shows nested sections as dictionaries.
- [example3.py](examples/example3.py) reads `application.yini`, checks required fields, and prints a configuration report.

More YINI syntax examples are available on the [YINI examples page](https://yini-lang.org/learn-yini/examples/?utm_source=github&utm_campaign=yini_parser_python&utm_content=readme&utm_medium=referral).

Runnable example projects are available in the [YINI demo apps repository](https://github.com/YINI-lang/yini-demo-apps/tree/main/python):
- [Python basic demo](https://github.com/YINI-lang/yini-demo-apps/tree/main/python/basic)
- [Python medium demo](https://github.com/YINI-lang/yini-demo-apps/tree/main/python/medium)

---

## Why YINI?

YINI is designed for configuration files that people read and edit by hand.

Compared with common configuration formats:
- **INI:** YINI defines nested sections and value types such as numbers and lists.
- **JSON:** YINI supports comments and does not require quotes around simple keys.
- **YAML:** YINI does not use indentation to define structure.
- **TOML:** YINI uses explicit section markers for hierarchy instead of dotted table names.

<details>
<summary>Compare the same configuration in YINI, JSON, YAML, and TOML</summary>

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
- Section markers `^` define the nesting. Indentation is optional.
- Strings can use either `'` or `"`.
- `E`/`e` strings interpret escapes such as `\n`; `C`/`c` remain valid, deprecated aliases.
- `command"""` starts a multiline literal that removes structural indentation and preserves line breaks.
- Source line endings in triple-quoted and command strings become LF (`\n`) in both modes. Characters produced by escape sequences retain their exact values.

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

</details>

The format and parser are release candidates. Pin the package version and test
your application's configuration files before using it in production. If your
tools already require JSON, YAML, or TOML, using that format may be a better fit.

---

## Parser implementation

The package includes Python parser code generated by ANTLR, a tool that turns
grammar rules into parser code. You only need Python to use the package. Java
and the ANTLR generator are needed only by maintainers who regenerate the parser.

---

## Feedback and bug reports

If you find a problem, [open an issue on GitHub](https://github.com/YINI-lang/yini-parser-python/issues).

When reporting parser behavior, it is helpful to include:
- The YINI input that caused the issue.
- The expected result.
- The actual result or error message.
- The installed `yini-parser` version.
- The Python version used.
- Whether you used strict or lenient mode.

---

## Development

From a local checkout, install the development dependencies:

```bash
python -m pip install -e ".[dev]"
```

If you use Task, the equivalent command is:

```bash
task install-dev
```

Run the full project check:

```bash
task check
```

This runs:
- The test suite with warnings treated as errors.
- Ruff lint checks.
- Ruff formatting checks.
- mypy type checking.

You can also run the tests directly:

```bash
python -m pytest -v -W error
```

The generated parser is included, so normal development does not need Java.
Grammar updates are maintained separately; `task antlr` is a maintainer task
that requires Windows, Java, and the vendored ANTLR JAR.

See [Development setup](docs/Development-Setup.md) and the
[Maintainer guide](docs/Maintainer-Doc.md) for more details.

---

## Testing and stability

The local tests cover the loading API, values, nested sections, strict and
lenient rules, warnings, and error handling.

The parser also passes all 542 cases in
[`yini-test-suite`](https://github.com/YINI-lang/yini-test-suite) `0.4.0rc1`,
the shared test suite for YINI Specification 1.0.0 RC7. These tests check both
strict and lenient parsing. CI runs this pinned suite on pull requests and
pushes to `main`, and before publishing a release.

Passing these tests helps check compatibility with the specification. Test the
configuration files your application uses as well.

---

## Links

- [YINI Cheat Sheet](https://yini-lang.org/refs/yini-cheat-sheet/?utm_source=github&utm_campaign=yini_parser_python&utm_content=readme_links&utm_medium=referral)
- [YINI Specification](https://yini-lang.org/refs/specification/?utm_source=github&utm_campaign=yini_parser_python&utm_content=readme_links&utm_medium=referral)
- [YINI Demo Apps](https://github.com/YINI-lang/yini-demo-apps)

---

## License

Licensed under [Apache License 2.0](LICENSE).

---

**^YINI ≡**  
> YINI is a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, and predictable parsing.
> 
> It has a formal specification and a defined grammar.

[yini-lang.org](https://yini-lang.org/?utm_source=github&utm_campaign=yini_parser_python&utm_content=readme_footer&utm_medium=referral) · [YINI-lang on GitHub](https://github.com/YINI-lang)  
