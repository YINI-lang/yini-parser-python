# src/yini_parser/api/errors.py


class YiniParseError(Exception):
    def __init__(
        self, message: str, line: int | None = None, column: int | None = None
    ):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column

    def __str__(self) -> str:
        if self.line is not None and self.column is not None:
            return f"{self.message} (line {self.line}, column {self.column})"
        if self.line is not None:
            return f"{self.message} (line {self.line})"
        return self.message
