# src/yini_parser/core/value_decoders.py
from ..api.errors import YiniParseError

"""
- Parsers reads raw/source text and recognizes its structure as tokens.
- Decoders converts tokens into its runtime value.
"""

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
                line=line,
                column=column,
            )

        return inner

    # Single-quoted or double-quoted string.
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        inner = text[1:-1]

        # Raw and unprefixed strings: return as-is.
        if prefix in {"", "R", "r"}:
            return inner

        # Classic strings: decode escapes.
        if prefix in {"C", "c"}:
            return _decode_classic_string(
                inner,
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
    line: int | None = None,
    column: int | None = None,
) -> str:
    try:
        return bytes(inner, "utf-8").decode("unicode_escape")
    except UnicodeDecodeError as exc:
        raise YiniParseError(
            f"Invalid string escape sequence: {exc.reason}.",
            line=line,
            column=column,
        ) from None


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
