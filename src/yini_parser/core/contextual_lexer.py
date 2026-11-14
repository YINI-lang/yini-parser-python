from antlr4 import InputStream
from antlr4.Token import Token

from ..grammar.generated.YiniLexer import YiniLexer


class ContextualYiniLexer(YiniLexer):
    """Distinguish inline keys named hex from hexadecimal value literals."""

    def __init__(self, input_stream: InputStream) -> None:
        super().__init__(input_stream)
        self._delimiters: list[int] = []
        self._previous_token_type: int | None = None

    def nextToken(self) -> Token:  # noqa: N802
        token = super().nextToken()

        if (
            token.type == self.NUMBER
            and token.text[:4].lower() == "hex:"
            and self._delimiters
            and self._delimiters[-1] == self.OC
            and self._previous_token_type in {self.OC, self.COMMA}
        ):
            # Emit only the key, then let the lexer read the separator and value.
            # Relexing the value preserves decimal fractions and exponent signs.
            self.inputStream.seek(token.start + 3)
            self.column = token.column + 3
            self._hitEOF = False
            token.type = self.KEY
            token.stop = token.start + 2

        if token.type in {self.OC, self.OB}:
            self._delimiters.append(token.type)
        elif token.type in {self.CC, self.CB} and self._delimiters:
            self._delimiters.pop()

        if token.type not in {
            self.NL,
            self.DISABLED_LINE,
            self.FULL_LINE_COMMENT,
            self.SHEBANG,
        }:
            self._previous_token_type = token.type

        return token
