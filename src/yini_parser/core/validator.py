# src/yini_parser/core/validator.py

from __future__ import annotations

import warnings
from typing import NoReturn

from ..api.errors import YiniParseError
from ..api.warnings import YiniParseWarning


class YiniValidator:
    """
    Handles validation policy for strict and lenient parsing.

    Duplicate keys warn in lenient mode and fail in strict mode.
    Duplicate sections and member/section name collisions fail in both modes.
    """

    def __init__(self, strict: bool = False) -> None:
        self.strict = strict

    def handle_duplicate_key(
        self,
        key: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> bool:
        """
        Handles duplicate keys.

        Returns:
            True  -> caller may keep/replace the value
            False -> caller should ignore the new value
        """
        message = f"Duplicate key {key!r} ignored. The first value is kept."

        if self.strict:
            raise YiniParseError(
                f"Duplicate key {key!r} is not allowed in strict mode.",
                line=line,
                column=column,
            )

        self._warn(
            message,
            line=line,
            column=column,
            code="duplicate-key",
        )

        return False

    def handle_duplicate_section(
        self,
        name: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> NoReturn:
        """Reject duplicate sections in both parsing modes."""
        raise YiniParseError(
            f"Duplicate section {name!r} is not allowed.",
            line=line,
            column=column,
        )

    def handle_key_section_collision(
        self,
        name: str,
        existing_kind: str,
        incoming_kind: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> NoReturn:
        """
        Handles name collisions between keys and sections.

        Example:
            app = "demo"
            ^ app

        or:

            ^ app
            app = "demo"

        Member and section names share one namespace in both modes.
        """
        raise YiniParseError(
            f"Name collision for {name!r}. "
            f"A {existing_kind} with this name already exists, so it cannot "
            f"also be used as a {incoming_kind}.",
            line=line,
            column=column,
        )

    def _warn(
        self,
        message: str,
        *,
        line: int | None = None,
        column: int | None = None,
        code: str | None = None,
    ) -> None:
        warnings.warn(
            YiniParseWarning(
                message,
                line=line,
                column=column,
                code=code,
            ),
            stacklevel=3,
        )
