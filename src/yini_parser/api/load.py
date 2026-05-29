# src/yini_parser/api/load.py
from __future__ import annotations

from pathlib import Path
from typing import Any

from antlr4 import CommonTokenStream, InputStream

from yini_parser.api.errors import YiniParseError

from ..core.yini_builder_visitor import YiniBuilderVisitor
from ..grammar.generated.YiniLexer import YiniLexer
from ..grammar.generated.YiniParser import YiniParser


def loads(text: str, strict: bool = False) -> dict[str, Any]:
    """
    Parse YINI text and return the resulting Python dictionary.
    """

    text = _ensure_final_newline(text)
    input_stream = InputStream(text)

    return _parse_input_stream(input_stream, strict=strict)


def load(path: str | Path, strict: bool = False) -> dict[str, Any]:
    """
    Parse a YINI file from disk and return the resulting Python dictionary.
    """

    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    text = _ensure_final_newline(text)
    input_stream = InputStream(text)

    return _parse_input_stream(input_stream, strict=strict)


def _parse_input_stream(
    input_stream: InputStream | FileStream, strict: bool
) -> dict[str, Any]:
    lexer = YiniLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = YiniParser(stream)

    tree = parser.yini()

    if parser.getNumberOfSyntaxErrors() > 0:
        #        raise ValueError(f"Failed to parse YINI input: {parser.getNumberOfSyntaxErrors()} syntax error(s).")
        raise YiniParseError(
            f"Failed to parse YINI input: {parser.getNumberOfSyntaxErrors()} syntax error(s)."
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
