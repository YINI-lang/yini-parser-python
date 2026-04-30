# src/yini_parser/api/warnings.py

from __future__ import annotations


class YiniParseWarning(Warning):
    """
    Warning raised for non-fatal YINI parse issues.

    A YiniParseWarning represents a problem that was detected while parsing,
    but which does not prevent a result from being produced.

    Typical examples:
    - Duplicate keys ignored in lenient mode.
    - Duplicate sections ignored in lenient mode.
    - Key/section name collisions handled by lenient-mode policy.
    """

    def __init__(
        self,
        message: str,
        line: int | None = None,
        column: int | None = None,
        code: str | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column
        self.code = code

    def __str__(self) -> str:
        location = self._format_location()

        if self.code is not None and location is not None:
            return f"{self.message} [{self.code}] {location}"

        if self.code is not None:
            return f"{self.message} [{self.code}]"

        if location is not None:
            return f"{self.message} {location}"

        return self.message

    def _format_location(self) -> str | None:
        if self.line is not None and self.column is not None:
            return f"(line {self.line}, column {self.column})"

        if self.line is not None:
            return f"(line {self.line})"

        return None
