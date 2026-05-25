# src/yini_parser/utils/antlr.py
from typing import Any


def ctx_location(ctx: Any) -> tuple[int | None, int | None]:
    token = getattr(ctx, "start", None)
    if token is None:
        return None, None
    return token.line, token.column + 1
