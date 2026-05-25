# CHANGELOG

## 0.1.0a3 - 2026-05-25
- Regenerated the ANTLR-generated Python parser sources from the updated YINI grammar.
- Updated the parser visitor to match the latest RC5/WIP grammar structure.
- Added support for `@yini strict` and `@yini lenient` mode declarations, including mismatch and unknown-mode validation.
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

## 0.1.0a2 - 2026-05-16
- Updated README with links to Python demo applications.
- Added or improved maintainer release documentation.
- No parser behavior changes.

---

**^YINI ≡**  
> YINI is a human-readable, INI-inspired, indentation-insensitive configuration format with clear nested sections, explicit structure, and predictable parsing.

[yini-lang.org](https://yini-lang.org/?utm_source=github&utm_medium=referral&utm_campaign=yini_parser_python&utm_content=changelog_footer) · [YINI-lang on GitHub](https://github.com/YINI-lang)  
