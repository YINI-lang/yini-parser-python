# src/yini_parser/core/value_decoders.py
import re
import math
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
    "`": "`",
    "/": "/",
    "0": "\0",
    "?": "?",
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
    Decode raw, escaped, and command string tokens.
    """
    text = token_text

    if not text:
        return ""

    if text.startswith('command"""'):
        return _decode_command_string(text, line=line, column=column)

    prefix = ""

    if len(text) >= 2 and text[0] in "RrCcEe" and text[1] in {'"', "'"}:
        prefix = text[0]
        text = text[1:]

    # Triple-quoted string.
    if text.startswith('"""') and text.endswith('"""') and len(text) >= 6:
        inner = text[3:-3]

        if prefix in {"C", "c", "E", "e"}:
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
        if prefix in {"C", "c", "E", "e"}:
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


def _decode_command_string(
    text: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> str:
    opening = re.match(r'command"""(?:\r\n|\r|\n)', text)
    if opening is None:
        raise YiniParseError(
            "Invalid command string: the opening delimiter must end its line.",
            line=line,
            column=column,
        )

    remainder = text[opening.end() :]
    closing_breaks = list(re.finditer(r"\r\n|\r|\n", remainder))
    if not closing_breaks:
        content = ""
        closing_line = remainder
    else:
        last_break = closing_breaks[-1]
        content = remainder[: last_break.start()]
        closing_line = remainder[last_break.end() :]

    if re.fullmatch(r' *"""', closing_line) is None:
        raise YiniParseError(
            "Invalid command string: the closing delimiter must be alone on its line.",
            line=line,
            column=column,
        )

    _validate_string_content(content, allow_line_breaks=True, line=line, column=column)
    if not content:
        return ""

    parts = re.split(r"(\r\n|\r|\n)", content)
    lines = parts[::2]
    content_breaks = parts[1::2]
    first_nonempty_index = next(
        (index for index, part in enumerate(lines) if part.strip(" ")), None
    )
    indentation = (
        len(lines[first_nonempty_index]) - len(lines[first_nonempty_index].lstrip(" "))
        if first_nonempty_index is not None
        else max(len(part) for part in lines)
    )

    decoded_lines = []
    for index, part in enumerate(lines):
        leading_spaces = len(part) - len(part.lstrip(" "))
        if part.strip(" ") and leading_spaces < indentation:
            raise YiniParseError(
                "Invalid command string: a content line has less than the structural indentation.",
                line=line,
                column=column,
            )
        if (
            first_nonempty_index is not None
            and index < first_nonempty_index
            and leading_spaces > indentation
        ):
            raise YiniParseError(
                "Invalid command string: a space-only line exceeds the structural indentation.",
                line=line,
                column=column,
            )
        decoded_lines.append(part[min(leading_spaces, indentation) :])

    return "".join(
        part + (content_breaks[index] if index < len(content_breaks) else "")
        for index, part in enumerate(decoded_lines)
    )


def normalize_number_literal(
    text: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> str:
    """Normalize from source spelling, then validate the numeric value."""
    unsigned = text.lstrip("+-")
    if unsigned.lower().startswith(("0x", "0b", "0o", "0z", "hex:", "%")):
        parsed_value = parse_number_literal(text, line=line, column=column)
        if parsed_value == 0 and text.startswith("-"):
            return "-0"
        return str(parsed_value)

    normalized = text.replace("_", "").lstrip("+").replace("E", "e")
    normalized = normalized.replace("e+", "e")
    parse_number_literal(text, line=line, column=column)
    return normalized


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
            return _check_integer_range(sign * int(cleaned, 16), text, line, column)

        if lowered.startswith("0x"):
            return _check_integer_range(
                sign * int(body[2:].replace("_", ""), 16), text, line, column
            )

        if lowered.startswith("0b"):
            return _check_integer_range(
                sign * int(body[2:].replace("_", ""), 2), text, line, column
            )

        if lowered.startswith("%"):
            return _check_integer_range(
                sign * int(body[1:].replace("_", ""), 2), text, line, column
            )

        if lowered.startswith("0o"):
            return _check_integer_range(
                sign * int(body[2:].replace("_", ""), 8), text, line, column
            )

        if lowered.startswith("0z"):
            value = sign * _parse_duodecimal(
                body[2:].replace("_", ""),
                line=line,
                column=column,
            )
            return _check_integer_range(value, text, line, column)

        decimal_text = text.replace("_", "")

        if any(ch in decimal_text for ch in ".eE"):
            value = float(decimal_text)
            if not math.isfinite(value):
                raise YiniParseError(
                    f"Floating-point literal overflows binary64: {text!r}",
                    line=line,
                    column=column,
                )
            significand = re.split("[eE]", decimal_text, maxsplit=1)[0]
            if value == 0.0 and any(char in "123456789" for char in significand):
                raise YiniParseError(
                    f"Floating-point literal underflows to zero: {text!r}",
                    line=line,
                    column=column,
                )
            return value

        return _check_integer_range(int(decimal_text, 10), text, line, column)

    except YiniParseError:
        raise

    except ValueError:
        raise YiniParseError(
            f"Invalid number literal: {text!r}",
            line=line,
            column=column,
        ) from None


def _check_integer_range(
    value: int, text: str, line: int | None, column: int | None
) -> int:
    if not -(1 << 63) <= value < (1 << 63):
        raise YiniParseError(
            f"Integer literal is outside the signed 64-bit range: {text!r}",
            line=line,
            column=column,
        )
    return value


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
            digits = re.match(r"[0-7]{1,3}", inner[index + 2 :])
            if digits is None or int(digits.group(), 8) > 0o377:
                _raise_invalid_escape(
                    "Invalid string escape sequence: \\o requires 1 to 3 octal digits in the range 0 to 377.",
                    line=line,
                    column=column,
                )
            next_index = index + 2 + len(digits.group())
            if next_index < len(inner) and inner[next_index] in "89":
                _raise_invalid_escape(
                    "Invalid string escape sequence: octal digits must be in the range 0 to 7.",
                    line=line,
                    column=column,
                )
            result.append(chr(int(digits.group(), 8)))
            index = next_index
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

        if char == "\t" or (allow_line_breaks and char in {"\n", "\r"}):
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
        value = int(digits, base)
        if 0xD800 <= value <= 0xDFFF:
            raise ValueError("Unicode surrogate escape")
        return chr(value)
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
