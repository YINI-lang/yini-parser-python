# src/yini_parser/core/section_headers.py
from ..api.errors import YiniParseError
from ..utils.text import strip_backticks

def parse_section_head(
    raw_text: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> tuple[int, str]:
    """
    Parses a SECTION_HEAD token text like:
        "^ App\\n"
        "^^ Server\\n"
        "^7 DeepSection\\n"

    Returns:
        (level, name)
    """

    text = raw_text.strip()
    text = text.splitlines()[0].strip()
    text = _strip_section_tail_comment(text)

    if not text:
        raise YiniParseError(
            "Invalid section header: the header is empty.",
            line=line,
            column=column,
        )

    marker = text[0]

    if marker not in {"^", "<", "§"}:
        raise YiniParseError(
            f"Invalid section header: {marker!r} is not a valid section marker. "
            "Use one of: '^', '<', or '§'.",
            line=line,
            column=column,
        )

    # Numeric shorthand form, for example: ^7 SectionName.
    if len(text) >= 2 and text[1].isdigit():
        i = 1
        j = i

        while j < len(text) and text[j].isdigit():
            j += 1

        level_text = text[i:j]

        try:
            level = int(level_text)
        except ValueError:
            raise YiniParseError(
                f"Invalid section level: {level_text!r} is not a valid number.",
                line=line,
                column=column,
            ) from None

        name = text[j:].strip()

    else:
        # Repeated/basic form, for example:
        #   ^^ Section
        #   ^_^ Section
        #   ^_^_^ Section
        i = 0
        level = 0
        expecting_marker = True

        while i < len(text):
            ch = text[i]

            if ch == marker:
                level += 1
                expecting_marker = False
                i += 1
                continue

            if ch == "_" and not expecting_marker:
                if i + 1 < len(text) and text[i + 1] == marker:
                    expecting_marker = True
                    i += 1
                    continue

            break

        name = text[i:].strip()

    if not name:
        raise YiniParseError(
            f"Missing section name after section marker {marker!r}.",
            line=line,
            column=column,
        )

    return level, strip_backticks(name)


def _strip_section_tail_comment(text: str) -> str:
    in_single = False
    in_double = False
    in_backtick = False

    i = 0
    while i < len(text):
        ch = text[i]

        if ch == "`" and not in_single and not in_double:
            in_backtick = not in_backtick
            i += 1
            continue

        if ch == "'" and not in_double and not in_backtick:
            in_single = not in_single
            i += 1
            continue

        if ch == '"' and not in_single and not in_backtick:
            in_double = not in_double
            i += 1
            continue

        if not in_single and not in_double and not in_backtick:
            if ch == "#":
                return text[:i].rstrip()

            if ch == "/" and i + 1 < len(text) and text[i + 1] == "/":
                return text[:i].rstrip()

        i += 1

    return text.rstrip()
