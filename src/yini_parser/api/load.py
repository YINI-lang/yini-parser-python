# src/yini_parser/api/load.py
from __future__ import annotations

from pathlib import Path
from typing import Any
import re
import warnings

from antlr4 import CommonTokenStream, InputStream, Token
from antlr4.error.ErrorListener import ErrorListener

from yini_parser.api.errors import YiniParseError
from yini_parser.api.warnings import YiniParseWarning

from ..core.yini_builder_visitor import YiniBuilderVisitor
from ..grammar.generated.YiniLexer import YiniLexer
from ..grammar.generated.YiniParser import YiniParser


def loads(text: str, strict: bool = False) -> dict[str, Any]:
    """
    Parse YINI text and return the resulting Python dictionary.
    """

    text = _normalize_leading_bom(text, strict=strict)
    _validate_document_text(text, strict=strict)
    text = _ensure_final_newline(text)
    input_stream = InputStream(text)

    return _parse_input_stream(input_stream, strict=strict)


def load(path: str | Path, strict: bool = False) -> dict[str, Any]:
    """
    Parse a YINI file from disk and return the resulting Python dictionary.
    """

    file_path = Path(path)
    with file_path.open("r", encoding="utf-8", newline="") as source:
        text = source.read()
    text = _normalize_leading_bom(text, strict=strict)
    _validate_document_text(text, strict=strict)
    text = _ensure_final_newline(text)
    input_stream = InputStream(text)

    return _parse_input_stream(input_stream, strict=strict)


def _parse_input_stream(input_stream: InputStream, strict: bool) -> dict[str, Any]:
    lexer = YiniLexer(input_stream)
    lexer_errors = _SyntaxErrorCollector()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_errors)

    stream = CommonTokenStream(lexer)
    _normalize_shebang_comment_tokens(stream)
    _validate_command_closing_lines(stream, input_stream)

    parser = YiniParser(stream)
    parser_errors = _SyntaxErrorCollector()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_errors)

    tree = parser.yini()

    syntax_errors = lexer_errors.errors + parser_errors.errors
    if syntax_errors:
        line, column, message = syntax_errors[0]
        raise YiniParseError(
            f"Failed to parse YINI input: {len(syntax_errors)} syntax error(s). "
            f"First error: {message}",
            line=line,
            column=column,
        )

    visitor = YiniBuilderVisitor(strict=strict)
    result = visitor.visit(tree)

    if not isinstance(result, dict):
        raise TypeError(
            f"Expected parsed result to be a dict, got {type(result).__name__}."
        )

    return result


def _ensure_final_newline(text: str) -> str:
    if text and not text.endswith(("\n", "\r")):
        return text + "\n"

    return text


def _validate_document_text(text: str, *, strict: bool) -> None:
    if not strict:
        return

    if re.match(r"[ \t]+#!", text):
        raise YiniParseError(
            "A shebang must start at column 1; leading whitespace is invalid in strict mode.",
            line=1,
            column=1,
        )

    first_ending = None
    for line_number, ending in enumerate(re.finditer(r"\r\n|\r|\n", text), start=1):
        if first_ending is None:
            first_ending = ending.group()
        elif ending.group() != first_ending:
            raise YiniParseError(
                "Mixed line endings are not allowed in strict mode.",
                line=line_number,
                column=ending.start()
                - max(
                    text.rfind("\r", 0, ending.start()),
                    text.rfind("\n", 0, ending.start()),
                ),
            )


def _normalize_leading_bom(text: str, *, strict: bool) -> str:
    if not text.startswith("\ufeff"):
        return text

    if not strict:
        warnings.warn(
            YiniParseWarning(
                "UTF-8 BOM found at the start of the YINI document; ignoring BOM.",
                line=1,
                column=1,
                code="BOM",
            ),
            stacklevel=2,
        )

    return text[1:]


class _SyntaxErrorCollector(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
        self.errors: list[tuple[int, int, str]] = []

    def syntaxError(  # noqa: N802
        self,
        recognizer: Any,
        offendingSymbol: Any,
        line: int,
        column: int,
        msg: str,
        e: Exception | None,
    ) -> None:
        self.errors.append((line, column + 1, msg))


def _normalize_shebang_comment_tokens(stream: CommonTokenStream) -> None:
    """
    Keep a leading shebang available to the prolog rule, but treat later
    shebang-looking lines as ordinary ignored line content.
    """

    stream.fill()

    seen_meaningful_token = False

    for token in stream.tokens:
        if token.type == Token.EOF:
            continue

        if token.type == YiniLexer.NL:
            continue

        if token.type == YiniLexer.SHEBANG:
            if seen_meaningful_token:
                token.type = YiniLexer.NL
            else:
                seen_meaningful_token = True
            continue

        seen_meaningful_token = True

    stream.seek(0)


def _validate_command_closing_lines(
    stream: CommonTokenStream, input_stream: InputStream
) -> None:
    source = input_stream.strdata
    for token in stream.tokens:
        if token.type != YiniLexer.STRING or not token.text.startswith('command"""'):
            continue

        after_closing = token.stop + 1
        if after_closing >= len(source) or source[after_closing] in "\r\n":
            continue

        token_text = token.text
        line_breaks = (
            token_text.count("\r") + token_text.count("\n") - token_text.count("\r\n")
        )
        last_break = max(token_text.rfind("\r"), token_text.rfind("\n"))
        raise YiniParseError(
            "Invalid command string: the closing delimiter must end its line.",
            line=token.line + line_breaks,
            column=len(token_text[last_break + 1 :]) + 1,
        )
