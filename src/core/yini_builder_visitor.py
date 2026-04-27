"""
transform / build_model -> visitor converts tree to Python values
"""

# src/core/VisitorInterp.py
from __future__ import annotations

from decimal import Decimal
from typing import Any

from grammar.generated.YiniParser import YiniParser
from grammar.generated.YiniParserVisitor import YiniParserVisitor


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

    Notes:
    - This is a first practical version, not the final strict/lenient validator.
    - Repeated keys currently overwrite earlier values.
    """

    def __init__(self) -> None:
        super().__init__()
        self._root: dict[str, Any] = {}
        self._section_stack: list[dict[str, Any]] = []
        self._section_names: list[str] = []

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
            self._enter_section(section_token.getText())
            return None

        assignment_ctx = ctx.assignment()
        if assignment_ctx is not None:
            return self.visit(assignment_ctx)

        return None

    def visitAssignment(self, ctx: YiniParser.AssignmentContext) -> None:
        key, value = self.visit(ctx.member())
        target = self._current_container()
        target[key] = value
        return None

    def visitMember(self, ctx: YiniParser.MemberContext) -> tuple[str, Any]:
        key = ctx.KEY().getText()
        value_ctx = ctx.value()

        # In your grammar, empty value is allowed and intended to mean null
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
            return self._parse_duodecimal(text[2:])

        if any(ch in text for ch in ".eE"):
            return float(text)

        return int(text, 10)

    def visitString_literal(self, ctx: YiniParser.String_literalContext) -> str:
        first = self._decode_string_token(ctx.STRING().getText())
        suffix = "".join(self.visit(part) for part in ctx.string_concat())
        return first + suffix

    def visitString_concat(self, ctx: YiniParser.String_concatContext) -> str:
        return self._decode_string_token(ctx.STRING().getText())

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

    def _enter_section(self, raw_text: str) -> None:
        level, name = self._parse_section_head(raw_text)

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
        elif isinstance(existing, dict):
            new_section = existing
        else:
            raise ValueError(f"Section name conflicts with non-object value: {name!r}")

        self._section_stack.append(new_section)
        self._section_names.append(name)

    def _parse_section_head(self, raw_text: str) -> tuple[int, str]:
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
            raise ValueError("Empty section header")

        marker = text[0]

        if marker not in {"^", "<", "§"}:
            raise ValueError(f"Invalid section marker: {marker!r}")

        i = 0
        while i < len(text) and text[i] == marker:
            i += 1

        if i == 1 and i < len(text) and text[i].isdigit():
            j = i
            while j < len(text) and text[j].isdigit():
                j += 1
            level = int(text[i:j])
            name = text[j:].strip()
        else:
            level = i
            name = text[i:].strip()

        if not name:
            raise ValueError(f"Missing section name in header: {raw_text!r}")

        return level, self._strip_backticks(name)

    def _strip_backticks(self, text: str) -> str:
        if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
            return text[1:-1]
        return text

    def _decode_string_token(self, token_text: str) -> str:
        """
        Minimal first-pass string decoding.

        Handles:
        - optional prefixes: r, c, h in either case
        - single/double quoted strings
        - triple-quoted strings
        - simple quote stripping

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

        # Triple-quoted
        if text.startswith('"""') and text.endswith('"""') and len(text) >= 6:
            inner = text[3:-3]
            if prefix in {"C", "c"}:
                return bytes(inner, "utf-8").decode("unicode_escape")
            return inner

        # Single-quoted or double-quoted
#        if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
#            inner = text[1:-1]
#
#            # Raw / hyper: return as-is
#            if prefix in {"R", "r", "H", "h"}:
#                return inner
#
#            # Classic or unprefixed: decode simple escapes for now
#            return bytes(inner, "utf-8").decode("unicode_escape")
        # Single-quoted or double-quoted
        if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
            inner = text[1:-1]

            # Raw, hyper, and unprefixed strings: return as-is
            if prefix in {"", "R", "r", "H", "h"}:
                return inner

            # Classic strings: decode escapes
            if prefix in {"C", "c"}:
                return bytes(inner, "utf-8").decode("unicode_escape")

            return inner

        return text

    def _parse_duodecimal(self, text: str) -> int:
        value = 0
        for ch in text:
            if ch.isdigit():
                digit = int(ch)
            else:
                lowered = ch.lower()
                if lowered == "a" or lowered == "x":
                    digit = 10
                elif lowered == "b" or lowered == "e":
                    digit = 11
                else:
                    raise ValueError(f"Invalid duodecimal digit: {ch!r}")
            if digit >= 12:
                raise ValueError(f"Invalid duodecimal digit: {ch!r}")
            value = value * 12 + digit
        return value
