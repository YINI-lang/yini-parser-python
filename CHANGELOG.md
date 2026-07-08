# CHANGELOG

## [Upcoming/Unreleased] 0.2.0 beta 2 - FUTURE
- **Fixed:** The test-suite adapter now writes UTF-8 JSON consistently on Windows.
- **Fixed:** Classic strings now validate YINI escape sequences directly, including invalid octal and Unicode escapes.
- **Fixed:** Literal control characters are rejected in single-line strings while multiline triple-quoted strings still preserve valid formatting.
- **Fixed:** Initial UTF-8 BOMs are still accepted and ignored, but now produce a structured compatibility warning.

## 0.2.0 beta 1 - 2026 June
- **Fixed:** Improved error reporting when a YINI file has broken syntax, including unfinished block comments such as `/* comment`.
- **Fixed:** `#!` lines outside the first line are now safely ignored as comment-like lines.
- **Fixed:** `@yini` markers are now rejected if they appear after real file content. The `@yini` marker belongs at the top of the file.
- **Fixed:** Backticked keys are now handled correctly, and invalid plain keys such as `1key` and `my.key` are rejected.
- **Added:** More tests for keys, comments, parser mode handling, and invalid YINI files.

## 0.1.0a3 - 2026 May
- **Fixed:** Normalized input handling so `load(...)` and `loads(...)` accept YINI documents without a final trailing newline.
- **Improved:** Cleaned up the published Python package contents by excluding tests and development-only project files from the source distribution and wheel.
- **Renamed** handwritten visitor methods to PEP8-style snake_case while preserving ANTLR dispatch aliases.
- **Documented:** Clarified that `yini-parser` uses ANTLR-generated Python parser code, that users do not need Java or the ANTLR generator to use the package, and that the ANTLR generator JAR is not included in the published Python package.
- **Regenerated** the ANTLR-generated Python parser sources from the updated YINI grammar.
- **Updated** the parser visitor to match the latest RC.6 grammar structure.
- **Added** support for `@yini strict` and `@yini lenient` mode declarations, including unknown-mode validation and mode-mismatch diagnostics:
  - `@yini strict` parsed in lenient mode is an error.
  - `@yini lenient` parsed in strict mode is valid but emits a warning.
- Updated strict/lenient validation:
  - Strict mode now rejects empty member values and trailing commas in lists or inline objects.
  - Lenient mode continues to allow empty member values and trailing commas.
  - Strict mode now rejects root-level orphan members outside the single required top-level section.
- Updated inline object handling:
  - `:` remains canonical.
  - `=` is allowed in lenient mode and rejected in strict mode.
  - Inline object values must begin on the same logical line as the separator.
- Updated string concatenation handling:
  - Concatenation must begin with a string literal.
  - Strict mode allows only string literal operands.
  - Lenient mode allows scalar tail operands and converts them to canonical scalar strings.
- Updated section handling:
  - Repeated section markers support levels 1–9.
  - Level 10 and deeper must use numeric shorthand, such as `^10 Section`.
  - `_` separators are supported in repeated marker sequences.
  - Section level jumps are rejected.
- Expanded tests for mode declarations, strict/lenient behavior, inline objects, string concatenation, section depth, and warning diagnostics.
- Updated the quality gate so tests pass with `-W error`, Ruff linting/formatting, and mypy type checking.
- Configured mypy to skip ANTLR-generated parser files.
- **Improved:**: README/Development documentation cleanup.

## 0.1.0a2 - 2026-05-16
- Updated README with links to Python demo applications.
- Added or improved maintainer release documentation.
- No parser behavior changes.

---

**^YINI ≡**  
> YINI is a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, and predictable parsing.

[yini-lang.org](https://yini-lang.org/?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=changelog_footer) · [YINI-lang on GitHub](https://github.com/YINI-lang)  
