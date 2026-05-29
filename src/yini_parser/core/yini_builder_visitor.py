"""
Transform / build_model -> visitor converts tree to Python values
"""

# src/yini_parser/core/yini_builder_visitor.py
from __future__ import annotations

import warnings
from typing import Any

from ..api.errors import YiniParseError
from ..api.warnings import YiniParseWarning
from ..grammar.generated.YiniParser import YiniParser
from ..grammar.generated.YiniParserVisitor import YiniParserVisitor
from ..utils.antlr import ctx_location

from .section_headers import parse_section_head
from .value_decoders import decode_string_token, parse_number_literal
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
        self._strict = strict
        self._root: dict[str, Any] = {}
        self._section_stack: list[dict[str, Any]] = []
        self._section_names: list[str] = []
        self._ignored_section_level: int | None = None
        self._top_level_section_count = 0
        self._validator = YiniValidator(strict=strict)
        # self._root_member_count = 0

    # ------------------------------------------------------------
    # Public/root
    # ------------------------------------------------------------

    def visit_yini(self, ctx: YiniParser.YiniContext) -> dict[str, Any]:
        for stmt_ctx in ctx.stmt():
            self.visit(stmt_ctx)

        if self._strict:
            if self._top_level_section_count != 1:
                raise YiniParseError(
                    "Strict mode requires exactly one explicit top-level section."
                )

            if ctx.terminal_stmt() is None:
                raise YiniParseError(
                    "Strict mode requires exactly one document terminator."
                )
        else:
            if not self._root:
                self._add_warning(
                    "empty-document: The document contains no meaningful YINI content.",
                    code="empty-document",
                )

        return self._root

    # ------------------------------------------------------------
    # Statements
    # ------------------------------------------------------------

    def visit_stmt(self, ctx: YiniParser.StmtContext) -> Any:
        section_token = ctx.SECTION_HEAD()
        if section_token is not None:
            symbol = section_token.getSymbol()
            line = symbol.line
            column = symbol.column + 1

            level, name = parse_section_head(
                section_token.getText(),
                line=line,
                column=column,
            )

            # If we are inside an ignored duplicate/conflicting section block,
            # skip deeper nested sections too. Resume only at same or shallower level.
            if self._ignored_section_level is not None:
                if level > self._ignored_section_level:
                    return None
                self._ignored_section_level = None

            if self._strict and level == 1:
                self._top_level_section_count += 1
                if self._top_level_section_count > 1:
                    raise YiniParseError(
                        "Strict mode allows exactly one explicit top-level section.",
                        line=line,
                        column=column,
                    )

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

        meta_ctx = ctx.meta_stmt()
        if meta_ctx is not None:
            return self.visit(meta_ctx)

        invalid_section_ctx = ctx.invalid_section_stmt()
        if invalid_section_ctx is not None:
            return self.visit(invalid_section_ctx)

        assignment_ctx = ctx.assignment()
        if assignment_ctx is not None:
            return self.visit(assignment_ctx)

        bad_member_ctx = ctx.bad_member()
        if bad_member_ctx is not None:
            return self.visit(bad_member_ctx)

        return None

    def visit_meta_stmt(self, ctx: YiniParser.Meta_stmtContext) -> None:
        """
        Handles metadata-level statements.

        A meta statement can be:
        - A valid directive, such as `@yini`, `@yini strict`, or `@include`.
        - A valid annotation, currently recognized but ignored.
        - Invalid metadata text, which must raise a parse error.
        """

        directive_ctx = ctx.directive()
        if directive_ctx is not None:
            return self.visit(directive_ctx)

        annotation_ctx = ctx.annotation()
        if annotation_ctx is not None:
            return self.visit(annotation_ctx)

        bad_meta_ctx = ctx.bad_meta_text()
        if bad_meta_ctx is not None:
            return self.visit(bad_meta_ctx)

        return None

    def visit_directive(self, ctx: YiniParser.DirectiveContext) -> None:
        yini_directive_ctx = ctx.yini_directive()
        if yini_directive_ctx is not None:
            return self.visit(yini_directive_ctx)

        # @include is reserved/recognized but has no runtime behavior yet.
        if ctx.INCLUDE_TOKEN() is not None:
            return None

        return None

    def visit_yini_directive(self, ctx: YiniParser.Yini_directiveContext) -> None:
        mode_ctx = ctx.yini_mode_declaration()

        # Plain @yini is valid and declares no mode.
        if mode_ctx is None:
            return None

        return self.visit(mode_ctx)

    def visit_yini_mode_declaration(
        self,
        ctx: YiniParser.Yini_mode_declarationContext,
    ) -> None:
        mode = ctx.KEY().getText().strip().lower()
        line, column = ctx_location(ctx)

        if mode not in {"strict", "lenient"}:
            raise YiniParseError(
                f"Invalid @yini mode: {mode!r}. Expected 'strict' or 'lenient'.",
                line=line,
                column=column,
            )

        if mode == "strict" and not self._strict:
            raise YiniParseError(
                "This document declares '@yini strict', but the parser is running in lenient mode.",
                line=line,
                column=column,
            )

        if mode == "lenient" and self._strict:
            self._add_warning(
                "This document declares '@yini lenient', but the parser is running in strict mode.",
                line=line,
                column=column,
                code="YINI_MODE_MISMATCH",
            )
            return None

        return None

    def visit_annotation(self, ctx: YiniParser.AnnotationContext) -> None:
        """
        Handles metadata annotations.

        Annotations are recognized syntax, but they currently do not affect the
        parsed data model. They are ignored by this builder for now.
        """

        return None

    def visit_bad_meta_text(self, ctx: YiniParser.Bad_meta_textContext) -> None:
        line, column = ctx_location(ctx)
        raise YiniParseError(
            f"Invalid YINI directive or metadata statement: {ctx.getText()!r}",
            line=line,
            column=column,
        )

    def visit_invalid_section_stmt(
        self, ctx: YiniParser.Invalid_section_stmtContext
    ) -> None:
        line, column = ctx_location(ctx)
        raise YiniParseError(
            f"Invalid section statement: {ctx.getText()!r}",
            line=line,
            column=column,
        )

    def visit_bad_member(self, ctx: YiniParser.Bad_memberContext) -> None:
        line, column = ctx_location(ctx)
        raise YiniParseError(
            f"Invalid member statement: {ctx.getText()!r}",
            line=line,
            column=column,
        )

    def visit_assignment(self, ctx: YiniParser.AssignmentContext) -> None:
        key, value = self.visit(ctx.member())
        target = self._current_container()

        line = ctx.start.line if ctx.start is not None else None
        column = ctx.start.column + 1 if ctx.start is not None else None

        if self._strict and target is self._root:
            raise YiniParseError(
                "Top-level members are not allowed in strict mode.",
                line=line,
                column=column,
            )

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

    def visit_member(self, ctx: YiniParser.MemberContext) -> tuple[str, Any]:
        key = ctx.KEY().getText()
        value_ctx = ctx.value()

        if value_ctx is None:
            if self._strict:
                line, column = ctx_location(ctx)
                raise YiniParseError(
                    "Strict mode does not allow empty member values. Use 'null' explicitly.",
                    line=line,
                    column=column,
                )
            return key, None

        value = self.visit(value_ctx)
        return key, value

    # ------------------------------------------------------------
    # Values
    # ------------------------------------------------------------

    def visit_value(self, ctx: YiniParser.ValueContext) -> Any:
        concat_ctx = getattr(ctx, "concat_expression", lambda: None)()
        if concat_ctx is not None:
            return self.visit(concat_ctx)

        scalar_ctx = getattr(ctx, "scalar_value", lambda: None)()
        if scalar_ctx is not None:
            return self.visit(scalar_ctx)

        list_ctx = getattr(ctx, "list_literal", lambda: None)()
        if list_ctx is not None:
            return self.visit(list_ctx)

        object_ctx = getattr(ctx, "object_literal", lambda: None)()
        if object_ctx is not None:
            return self.visit(object_ctx)

        return None

    def visit_scalar_value(self, ctx: YiniParser.Scalar_valueContext) -> Any:
        string_ctx = getattr(ctx, "string_literal", lambda: None)()
        if string_ctx is not None:
            return self.visit(string_ctx)

        number_ctx = getattr(ctx, "number_literal", lambda: None)()
        if number_ctx is not None:
            return self.visit(number_ctx)

        null_ctx = getattr(ctx, "null_literal", lambda: None)()
        if null_ctx is not None:
            return self.visit(null_ctx)

        boolean_ctx = getattr(ctx, "boolean_literal", lambda: None)()
        if boolean_ctx is not None:
            return self.visit(boolean_ctx)

        return self.visitChildren(ctx)

    def visit_concat_expression(self, ctx: YiniParser.Concat_expressionContext) -> str:
        operands = []

        first_token = ctx.STRING()

        if first_token is None:
            line, column = ctx_location(ctx)
            raise YiniParseError(
                "Invalid concatenation expression: a concatenation expression must begin with a string literal.",
                line=line,
                column=column,
            )

        line, column = ctx_location(ctx)

        operands.append(
            decode_string_token(
                first_token.getText(),
                line=line,
                column=column,
            )
        )

        for tail_ctx in ctx.concat_tail():
            operands.append(self.visit(tail_ctx))

        if self._strict:
            for operand in operands:
                if not isinstance(operand, str):
                    line, column = ctx_location(ctx)
                    raise YiniParseError(
                        "Invalid strict-mode concatenation expression: all concatenation operands must be string literals.",
                        line=line,
                        column=column,
                    )

        return "".join(self._stringify_concat_operand(operand) for operand in operands)

    def visit_concat_tail(self, ctx: YiniParser.Concat_tailContext) -> str:
        return self.visit(ctx.concat_operand())

    def visit_concat_operand(self, ctx: YiniParser.Concat_operandContext) -> str:
        line, column = ctx_location(ctx)

        string_token = ctx.STRING()
        if string_token is not None:
            return decode_string_token(
                string_token.getText(),
                line=line,
                column=column,
            )

        if self._strict:
            raise YiniParseError(
                "Strict mode only allows string literals in string concatenation.",
                line=line,
                column=column,
            )

        number_token = ctx.NUMBER()
        if number_token is not None:
            value = parse_number_literal(
                number_token.getText(),
                line=line,
                column=column,
            )
            return self._number_to_canonical_string(value)

        true_token = ctx.BOOLEAN_TRUE()
        if true_token is not None:
            return "true"

        false_token = ctx.BOOLEAN_FALSE()
        if false_token is not None:
            return "false"

        null_token = ctx.NULL()
        if null_token is not None:
            return "null"

        raise YiniParseError(
            "Invalid string concatenation operand.",
            line=line,
            column=column,
        )

    def visit_string_literal(self, ctx: YiniParser.String_literalContext) -> str:
        line, column = ctx_location(ctx)
        return decode_string_token(
            ctx.getText(),
            line=line,
            column=column,
        )

    def visit_null_literal(self, ctx: YiniParser.Null_literalContext) -> None:
        return None

    def visit_boolean_literal(self, ctx: YiniParser.Boolean_literalContext) -> bool:
        text = ctx.getText().strip().lower()
        return text in {"true", "on", "yes"}

    def visit_number_literal(
        self, ctx: YiniParser.Number_literalContext
    ) -> int | float:
        line, column = ctx_location(ctx)
        return parse_number_literal(
            ctx.getText().strip(),
            line=line,
            column=column,
        )

    def visit_list_literal(self, ctx: YiniParser.List_literalContext) -> list[Any]:
        if ctx.EMPTY_LIST() is not None:
            return []

        elements_ctx = ctx.elements()
        if elements_ctx is None:
            return []

        return self.visit(elements_ctx)

    def visit_elements(self, ctx: YiniParser.ElementsContext) -> list[Any]:
        if self._strict and self._elements_has_trailing_comma(ctx):
            line, column = self._last_comma_location(ctx)
            raise YiniParseError(
                "Trailing commas in lists are not allowed in strict mode.",
                line=line,
                column=column,
            )

        return [self.visit(value_ctx) for value_ctx in ctx.value()]

    def visit_object_literal(
        self, ctx: YiniParser.Object_literalContext
    ) -> dict[str, Any]:
        if ctx.EMPTY_OBJECT() is not None:
            return {}

        object_members_ctx = ctx.object_members()
        if object_members_ctx is None:
            return {}

        return self.visit(object_members_ctx)

    def visit_object_members(
        self, ctx: YiniParser.Object_membersContext
    ) -> dict[str, Any]:
        if self._strict and self._object_members_has_trailing_comma(ctx):
            line, column = self._last_comma_location(ctx)
            raise YiniParseError(
                "Trailing commas in inline objects are not allowed in strict mode.",
                line=line,
                column=column,
            )

        result: dict[str, Any] = {}

        for member_ctx in ctx.object_member():
            key, value = self.visit(member_ctx)

            line = member_ctx.start.line if member_ctx.start is not None else None
            column = (
                member_ctx.start.column + 1 if member_ctx.start is not None else None
            )

            if key in result:
                if not self._validator.handle_duplicate_key(
                    key,
                    line=line,
                    column=column,
                ):
                    continue

            result[key] = value

        return result

    def visit_object_member(
        self, ctx: YiniParser.Object_memberContext
    ) -> tuple[str, Any]:
        """
        - Lenient mode allows `=`.
        - Strict mode rejects `=` inside inline objects.
        - The canonical inline object member separator remains `:`.
        """

        key = ctx.KEY().getText()
        value = self.visit(ctx.value())

        separator_ctx = ctx.object_member_separator()
        separator = (
            separator_ctx.getText().strip() if separator_ctx is not None else ":"
        )

        if self._strict and separator == "=":
            line, column = ctx_location(separator_ctx or ctx)
            raise YiniParseError(
                "Inline object members must use ':' in strict mode.",
                line=line,
                column=column,
            )

        return key, value

    # ANTLR's generated parser dispatches to these exact method names.
    visitYini = visit_yini
    visitStmt = visit_stmt
    visitMeta_stmt = visit_meta_stmt
    visitDirective = visit_directive
    visitYini_directive = visit_yini_directive
    visitYini_mode_declaration = visit_yini_mode_declaration
    visitAnnotation = visit_annotation
    visitBad_meta_text = visit_bad_meta_text
    visitInvalid_section_stmt = visit_invalid_section_stmt
    visitBad_member = visit_bad_member
    visitAssignment = visit_assignment
    visitMember = visit_member
    visitValue = visit_value
    visitScalar_value = visit_scalar_value
    visitConcat_expression = visit_concat_expression
    visitConcat_tail = visit_concat_tail
    visitConcat_operand = visit_concat_operand
    visitString_literal = visit_string_literal
    visitNull_literal = visit_null_literal
    visitBoolean_literal = visit_boolean_literal
    visitNumber_literal = visit_number_literal
    visitList_literal = visit_list_literal
    visitElements = visit_elements
    visitObject_literal = visit_object_literal
    visitObject_members = visit_object_members
    visitObject_member = visit_object_member

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _current_container(self) -> dict[str, Any]:
        if self._section_stack:
            return self._section_stack[-1]
        return self._root

    def _enter_section_with_parsed(
        self,
        level: int,
        name: str,
        *,
        line: int | None = None,
        column: int | None = None,
    ) -> None:

        # Root-level section is level 1.
        # Level N means nesting depth N.
        current_depth = len(self._section_stack)

        if level > current_depth + 1:
            raise YiniParseError(
                f"Section level jumps are not allowed. Expected level {current_depth + 1}, got level {level}.",
                line=line,
                column=column,
            )

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

    def _number_to_canonical_string(self, value: int | float) -> str:
        if isinstance(value, bool):
            # Defensive only; bool is a subclass of int in Python.
            return "true" if value else "false"

        if isinstance(value, int):
            return str(value)

        if isinstance(value, float):
            # Reasonable first version. You can refine later if needed.
            return str(value)

        return str(value)

    # def _has_trailing_comma(self, ctx: Any) -> bool:
    #     """
    #     Returns True when a list/object member sequence ends with a comma.

    #     This relies on the generated grammar shape where:
    #     - ctx.COMMA() returns all comma tokens.
    #     - ctx.value() or ctx.object_member() returns real elements/members only.
    #     - A trailing comma means there are at least as many commas as values/members.
    #     """

    #     commas = ctx.COMMA()

    #     if hasattr(ctx, "value"):
    #         items = ctx.value()
    #     elif hasattr(ctx, "object_member"):
    #         items = ctx.object_member()
    #     else:
    #         return False

    #     return len(commas) >= len(items)

    def _last_comma_location(self, ctx: Any) -> tuple[int | None, int | None]:
        commas = ctx.COMMA()

        if not commas:
            return None, None

        symbol = commas[-1].getSymbol()
        return symbol.line, symbol.column + 1

    def _elements_has_trailing_comma(self, ctx: YiniParser.ElementsContext) -> bool:
        return len(ctx.COMMA()) >= len(ctx.value())

    def _object_members_has_trailing_comma(
        self,
        ctx: YiniParser.Object_membersContext,
    ) -> bool:
        return len(ctx.COMMA()) >= len(ctx.object_member())

    def _stringify_concat_operand(self, value: Any) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"

        if value is None:
            return "null"

        return str(value)

    def _add_warning(
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
            stacklevel=2,
        )
