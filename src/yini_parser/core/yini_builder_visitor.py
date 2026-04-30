"""
Transform / build_model -> visitor converts tree to Python values
"""

from __future__ import annotations

from typing import Any

from ..api.errors import YiniParseError
from ..grammar.generated.YiniParser import YiniParser
from ..grammar.generated.YiniParserVisitor import YiniParserVisitor
from .validator import YiniValidator


class YiniBuilderVisitor(YiniParserVisitor):
    """
    Builds a Python dictionary from the parsed YINI tree.

    Current behavior:
    - Top-level sections become nested dicts.
    - Assignments go into the current section.
    - Lists become Python lists.
    - Inline objects become Python dicts.
    - Booleans become True/False.
    - Null becomes None.
    - Strings become Python str.
    - Numbers become int or float.

    Conflict behavior:
    - lenient mode: first definition wins, later conflicting definitions warn
    - strict mode: conflicting definitions raise YiniParseError
    """

    def __init__(self, strict: bool = False) -> None:
        super().__init__()
        self._root: dict[str, Any] = {}
        self._section_stack: list[dict[str, Any]] = []
        self._section_names: list[str] = []
        self._ignored_section_level: int | None = None
        self._validator = YiniValidator(strict=strict)

    # ------------------------------------------------------------
    # Public/root
    # ------------------------------------------------------------

    def visitYini(self, ctx: YiniParser.YiniContext) -> dict[str, Any]:
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)
        return self._root

    # ------------------------------------------------------------
    # Statements
    # ------------------------------------------------------------

    def visitStmt(self, ctx: YiniParser.StmtContext) -> Any:
        section_token = ctx.SECTION_HEAD()
        if section_token is not None:
            symbol = section_token.getSymbol()
            line = symbol.line
            column = symbol.column + 1  # ANTLR columns are zero-based.

            level, name = self._parse_section_head(
                section_token.getText(),
                line=line,
                column=column,
            )

            # Clear ignore state when a new section at same or shallower level appears.
            if self._ignored_section_level is not None and level <= self._ignored_section_level:
                self._ignored_section_level = None

            self._enter_section_with_parsed(
                level,
                name,
                line=line,
                column=column,
            )
            return None

        # Skip assignments while inside an ignored duplicate/conflicting section block.
        if self._ignored_section_level is not None:
            return None

        assignment_ctx = ctx.assignment()
        if assignment_ctx is not None:
            return self.visit(assignment_ctx)

        return None

    def visitAssignment(self, ctx: YiniParser.AssignmentContext) -> None:
        key, value = self.visit(ctx.member())
        target = self._current_container()

        line = ctx.start.line if ctx.start is not None else None
        column = ctx.start.column + 1 if ctx.start is not None else None

        # Assignment-level key/section collision:
        # if an earlier section already exists with this name, the first definition wins.
        existing = target.get(key)
        if isinstance(existing, dict):
            if not self._validator.handle_key_section_collision(
                name=key,
                existing_kind="section",
                incoming_kind="key",
                line=line,
                column=column,
            ):
                return None

        # Duplicate key:
        if key in target:
            if not self._validator.handle_duplicate_key(
                key,
                line=line,
                column=column,
            ):
                return None

        target[key] = value
        return None

    def visitMember(self, ctx: YiniParser.MemberContext) -> tuple[str, Any]:
        key = ctx.KEY().getText()
        value_ctx = ctx.value()

        # In grammar, empty value is allowed and intended to mean null.
        value = self.visit(value_ctx) if value_ctx is not None else None
        return key, value

    # ------------------------------------------------------------
    # Values
    # ------------------------------------------------------------

    def visitValue(self, ctx: YiniParser.ValueContext) -> Any:
        return self.visitChildren(ctx)

    def visitNull_literal(self, ctx: YiniParser.Null_literalContext) -> None:
        return None

    def visitBoolean_literal(self, ctx: YiniParser.Boolean_literalContext) -> bool:
        text = ctx.getText().strip().lower()
        return text in {"true", "on", "yes"}

    def visitNumber_literal(self, ctx: YiniParser.Number_literalContext) -> int | float:
        text = ctx.getText().strip()
        line = ctx.start.line if ctx.start is not None else None
        column = ctx.start.column + 1 if ctx.start is not None else None

        try:
            lowered = text.lower()

            if lowered.startswith(("0x", "#")):
                cleaned = text[1:] if text.startswith("#") else text[2:]
                return int(cleaned, 16)

            if lowered.startswith("0b"):
                return int(text[2:], 2)

            if lowered.startswith("%"):
                return int(text[1:], 2)

            if lowered.startswith("0o"):
                return int(text[2:], 8)

            if lowered.startswith("0z"):
                return self._parse_duodecimal(text[2:], line=line, column=column)

            if any(ch in text for ch in ".eE"):
                return float(text)

            return int(text, 10)

        except YiniParseError:
            raise

        except ValueError:
            raise YiniParseError(
                f"Invalid number literal: {text!r}",
                line=line,
                column=column,
            ) from None
    
    def visitString_literal(self, ctx: YiniParser.String_literalContext) -> str:
        token = ctx.STRING().getSymbol()
        line = token.line
        column = token.column + 1

        first = self._decode_string_token(
            ctx.STRING().getText(),
            line=line,
            column=column,
        )

        suffix = "".join(self.visit(part) for part in ctx.string_concat())
        return first + suffix


    def visitString_concat(self, ctx: YiniParser.String_concatContext) -> str:
        token = ctx.STRING().getSymbol()
        line = token.line
        column = token.column + 1

        return self._decode_string_token(
            ctx.STRING().getText(),
            line=line,
            column=column,
        )

    def visitList_literal(self, ctx: YiniParser.List_literalContext) -> list[Any]:
        if ctx.EMPTY_LIST() is not None:
            return []

        elements_ctx = ctx.elements()
        if elements_ctx is None:
            return []

        return self.visit(elements_ctx)

    def visitElements(self, ctx: YiniParser.ElementsContext) -> list[Any]:
        return [self.visit(value_ctx) for value_ctx in ctx.value()]

    def visitObject_literal(self, ctx: YiniParser.Object_literalContext) -> dict[str, Any]:
        if ctx.EMPTY_OBJECT() is not None:
            return {}

        object_members_ctx = ctx.object_members()
        if object_members_ctx is None:
            return {}

        return self.visit(object_members_ctx)

    def visitObject_members(self, ctx: YiniParser.Object_membersContext) -> dict[str, Any]:
        result: dict[str, Any] = {}

        for member_ctx in ctx.object_member():
            key, value = self.visit(member_ctx)
            
            line = member_ctx.start.line if member_ctx.start is not None else None
            column = member_ctx.start.column + 1 if member_ctx.start is not None else None

            if key in result:
                if not self._validator.handle_duplicate_key(
                    key,
                    line=line,
                    column=column,
                ):
                    continue

            result[key] = value
        return result

    def visitObject_member(self, ctx: YiniParser.Object_memberContext) -> tuple[str, Any]:
        key = ctx.KEY().getText()
        value = self.visit(ctx.value())
        return key, value

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _current_container(self) -> dict[str, Any]:
        if self._section_stack:
            return self._section_stack[-1]
        return self._root

    # def _enter_section_with_parsed(
    #         self, level: int, name: str
    # ) -> None:
    def _enter_section_with_parsed(
        self,
        level: int,
        name: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> None:
            
        # Root-level section is level 1.
        # level N means nesting depth N.
        while len(self._section_stack) >= level:
            self._section_stack.pop()
            self._section_names.pop()

        parent = self._section_stack[-1] if self._section_stack else self._root
        existing = parent.get(name)

        if existing is None:
            new_section: dict[str, Any] = {}
            parent[name] = new_section
            self._section_stack.append(new_section)
            self._section_names.append(name)
            return

        # Duplicate section name: first definition wins.
        if isinstance(existing, dict):
            if not self._validator.handle_duplicate_section(
                name,
                line=line,
                column=column,
            ):
                self._ignored_section_level = level
                return

            # If validator policy ever changes to allow this.
            self._section_stack.append(existing)
            self._section_names.append(name)
            return

        # Existing scalar/other value, incoming section -> collision.
        if not self._validator.handle_key_section_collision(
            name=name,
            existing_kind="key",
            incoming_kind="section",
            line=line,
            column=column,
        ):
            self._ignored_section_level = level
            return

    def _parse_section_head(
        self,
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

        i = 0
        while i < len(text) and text[i] == marker:
            i += 1

        if i == 1 and i < len(text) and text[i].isdigit():
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
            level = i
            name = text[i:].strip()

        if not name:
            raise YiniParseError(
                f"Missing section name after section marker {marker!r}.",
                line=line,
                column=column,
            )

        return level, self._strip_backticks(name)

    def _strip_backticks(self, text: str) -> str:
        if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
            return text[1:-1]
        return text

    def _decode_string_token(
        self,
        token_text: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> str:
        """
        Minimal first-pass string decoding.

        Handles:
        - Optional prefixes: r, c, h in either case.
        - Single/double quoted strings.
        - Triple-quoted strings.
        - Simple quote stripping.

        This is intentionally conservative for now.
        """
        text = token_text

        if not text:
            return ""

        prefix = ""

        if len(text) >= 2 and text[0] in "RrCcHh" and text[1] in {'"', "'"}:
            prefix = text[0]
            text = text[1:]
        elif len(text) >= 4 and text[0] in "RrCc" and text[1:4] == '"""':
            prefix = text[0]
            text = text[1:]

        # Triple-quoted string.
        if text.startswith('"""') and text.endswith('"""') and len(text) >= 6:
            inner = text[3:-3]

            if prefix in {"C", "c"}:
                return self._decode_classic_string(
                    inner,
                    line=line,
                    column=column,
                )

            return inner

        # Single-quoted or double-quoted string.
        if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
            inner = text[1:-1]

            # Raw, hyper, and unprefixed strings: return as-is.
            if prefix in {"", "R", "r", "H", "h"}:
                return inner

            # Classic strings: decode escapes.
            if prefix in {"C", "c"}:
                return self._decode_classic_string(
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

    def _parse_duodecimal(
        self,
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

    # Helper
    def _decode_classic_string(
        self,
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
