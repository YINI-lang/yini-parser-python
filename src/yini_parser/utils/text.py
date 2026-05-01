from typing import Any

def normalize_newlines(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("\r\n", "\n").replace("\r", "\n")
    if isinstance(value, list):
        return [normalize_newlines(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize_newlines(v) for k, v in value.items()}
    return value

def strip_whitespaces(txt: str) -> str:
    """
    Remove all whitespace characters from the input string.

    This includes spaces, tabs, newlines, and any other Unicode
    whitespace characters.

    Args:
        text: The input string to process.

    Returns:
        A new string with all whitespace removed.
    """
    return "".join(txt.split())
