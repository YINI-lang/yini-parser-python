# src/yini_parser/core/value_decoders.py
from typing import NoReturn

from ..api.errors import YiniParseError

"""
- Parsers reads raw/source text and recognizes its structure as tokens.
- Decoders converts tokens into its runtime value.
"""

_CLASSIC_SIMPLE_ESCAPES = {
    "\\": "\\",
    '"': '"',
    "'": "'",
    "a": "\a",
    "b": "\b",
    "f": "\f",
    "n": "\n",
    "r": "\r",
    "t": "\t",
    "v": "\v",
}


def decode_string_token(
    token_text: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> str:
    """
    Minimal first-pass string decoding.

    Handles:
    - Optional prefixes: R/r and C/c.
    - Single/double quoted strings.
    - Triple-quoted strings.
    - Simple quote stripping.

    Unprefixed strings are treated as raw strings.
    C-prefixed strings decode escape sequences.
    """
    text = token_text

    if not text:
        return ""

    prefix = ""

    if len(text) >= 2 and text[0] in "RrCc" and text[1] in {'"', "'"}:
        prefix = text[0]
        text = text[1:]
    elif len(text) >= 4 and text[0] in "RrCc" and text[1:4] == '"""':
        prefix = text[0]
        text = text[1:]

    # Triple-quoted string.
    if text.startswith('"""') and text.endswith('"""') and len(text) >= 6:
        inner = text[3:-3]

        if prefix in {"C", "c"}:
            return _decode_classic_string(
                inner,
                allow_line_breaks=True,
                line=line,
                column=column,
            )

        _validate_string_content(
            inner,
            allow_line_breaks=True,
            line=line,
            column=column,
        )
        return inner

    # Single-quoted or double-quoted string.
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        inner = text[1:-1]

        # Raw and unprefixed strings: return as-is.
        if prefix in {"", "R", "r"}:
            _validate_string_content(
                inner,
                allow_line_breaks=False,
                line=line,
                column=column,
            )
            return inner

        # Classic strings: decode escapes.
        if prefix in {"C", "c"}:
            return _decode_classic_string(
                inner,
                allow_line_breaks=False,
                line=line,
                column=column,
            )

        return inner

    raise YiniParseError(
        f"Invalid string literal: {token_text!r}",
        line=line,
        column=column,
    )


def parse_number_literal(text, line=None, column=None):
    # text = ctx.getText().strip()
    # line, column = self._ctx_location(ctx)

    try:
        sign = 1
        body = text

        if body.startswith("-"):
            sign = -1
            body = body[1:]
        elif body.startswith("+"):
            body = body[1:]

        lowered = body.lower()

        """
        By spec: hex:FF_AA   // Shall work.
                    hex: FF_AA  // INVALID!
        """
        if lowered.startswith("hex:"):
            cleaned = body.split(":", 1)[1].strip().replace("_", "")
            return sign * int(cleaned, 16)

        if lowered.startswith("0x"):
            return sign * int(body[2:].replace("_", ""), 16)

        if lowered.startswith("0b"):
            return sign * int(body[2:].replace("_", ""), 2)

        if lowered.startswith("%"):
            return sign * int(body[1:].replace("_", ""), 2)

        if lowered.startswith("0o"):
            return sign * int(body[2:].replace("_", ""), 8)

        if lowered.startswith("0z"):
            return sign * _parse_duodecimal(
                body[2:].replace("_", ""),
                line=line,
                column=column,
            )

        decimal_text = text.replace("_", "")

        if any(ch in decimal_text for ch in ".eE"):
            return float(decimal_text)

        return int(decimal_text, 10)

    except YiniParseError:
        raise

    except ValueError:
        raise YiniParseError(
            f"Invalid number literal: {text!r}",
            line=line,
            column=column,
        ) from None


def _decode_classic_string(
    inner: str,
    *,
    allow_line_breaks: bool,
    line: int | None = None,
    column: int | None = None,
) -> str:
    result: list[str] = []
    index = 0

    while index < len(inner):
        char = inner[index]

        if char != "\\":
            _validate_string_content(
                char,
                allow_line_breaks=allow_line_breaks,
                line=line,
                column=column,
            )
            result.append(char)
            index += 1
            continue

        if index + 1 >= len(inner):
            _raise_invalid_escape(
                "Invalid string escape sequence: trailing backslash.",
                line=line,
                column=column,
            )

        escape = inner[index + 1]

        if escape in _CLASSIC_SIMPLE_ESCAPES:
            result.append(_CLASSIC_SIMPLE_ESCAPES[escape])
            index += 2
            continue

        if escape == "o":
            result.append(
                _decode_digits_escape(
                    inner,
                    start=index + 2,
                    length=3,
                    base=8,
                    prefix="\\o",
                    line=line,
                    column=column,
                )
            )
            index += 5
            continue

        if escape == "x":
            result.append(
                _decode_digits_escape(
                    inner,
                    start=index + 2,
                    length=2,
                    base=16,
                    prefix="\\x",
                    line=line,
                    column=column,
                )
            )
            index += 4
            continue

        if escape == "u":
            result.append(
                _decode_digits_escape(
                    inner,
                    start=index + 2,
                    length=4,
                    base=16,
                    prefix="\\u",
                    line=line,
                    column=column,
                )
            )
            index += 6
            continue

        if escape == "U":
            result.append(
                _decode_digits_escape(
                    inner,
                    start=index + 2,
                    length=8,
                    base=16,
                    prefix="\\U",
                    line=line,
                    column=column,
                )
            )
            index += 10
            continue

        _raise_invalid_escape(
            f"Invalid string escape sequence: \\{escape}.",
            line=line,
            column=column,
        )

    return "".join(result)


def _validate_string_content(
    text: str,
    *,
    allow_line_breaks: bool,
    line: int | None = None,
    column: int | None = None,
) -> None:
    for char in text:
        if ord(char) >= 0x20:
            continue

        if allow_line_breaks and char in {"\n", "\r", "\t"}:
            continue

        raise YiniParseError(
            "Invalid string literal: literal control characters are not allowed.",
            line=line,
            column=column,
        )


def _decode_digits_escape(
    text: str,
    *,
    start: int,
    length: int,
    base: int,
    prefix: str,
    line: int | None = None,
    column: int | None = None,
) -> str:
    digits = text[start : start + length]

    if len(digits) != length or not _digits_match_base(digits, base):
        _raise_invalid_escape(
            f"Invalid string escape sequence: {prefix} requires {length} "
            f"base-{base} digit(s).",
            line=line,
            column=column,
        )

    try:
        return chr(int(digits, base))
    except ValueError:
        _raise_invalid_escape(
            f"Invalid string escape sequence: {prefix}{digits}.",
            line=line,
            column=column,
        )


def _digits_match_base(digits: str, base: int) -> bool:
    if base == 8:
        return all("0" <= digit <= "7" for digit in digits)

    if base == 16:
        return all(digit in "0123456789abcdefABCDEF" for digit in digits)

    raise ValueError(f"Unsupported escape base: {base}")


def _raise_invalid_escape(
    message: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> NoReturn:
    raise YiniParseError(
        message,
        line=line,
        column=column,
    )


def _parse_duodecimal(
    text: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> int:
    value = 0

    if not text:
        raise YiniParseError(
            "Invalid duodecimal number: missing digits after '0z'.",
            line=line,
            column=column,
        )

    for ch in text:
        if ch.isdigit():
            digit = int(ch)
        else:
            lowered = ch.lower()

            if lowered in {"a", "x"}:
                digit = 10
            elif lowered in {"b", "e"}:
                digit = 11
            else:
                raise YiniParseError(
                    f"Invalid duodecimal number: {ch!r} is not a valid base-12 digit.",
                    line=line,
                    column=column,
                )

        if digit >= 12:
            raise YiniParseError(
                f"Invalid duodecimal number: {ch!r} is not a valid base-12 digit.",
                line=line,
                column=column,
            )

        value = value * 12 + digit

    return value
