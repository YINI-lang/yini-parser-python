# Generated from ./grammar/v1.0.0-rc.5/YiniParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .YiniParser import YiniParser
else:
    from YiniParser import YiniParser

# This class defines a complete generic visitor for a parse tree produced by YiniParser.

class YiniParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YiniParser#yini.
    def visitYini(self, ctx:YiniParser.YiniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#prolog.
    def visitProlog(self, ctx:YiniParser.PrologContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#terminal_stmt.
    def visitTerminal_stmt(self, ctx:YiniParser.Terminal_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#stmt.
    def visitStmt(self, ctx:YiniParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#invalid_section_stmt.
    def visitInvalid_section_stmt(self, ctx:YiniParser.Invalid_section_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#meta_stmt.
    def visitMeta_stmt(self, ctx:YiniParser.Meta_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#directive.
    def visitDirective(self, ctx:YiniParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#annotation.
    def visitAnnotation(self, ctx:YiniParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#eol.
    def visitEol(self, ctx:YiniParser.EolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#assignment.
    def visitAssignment(self, ctx:YiniParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#member.
    def visitMember(self, ctx:YiniParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#value.
    def visitValue(self, ctx:YiniParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#object_literal.
    def visitObject_literal(self, ctx:YiniParser.Object_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#object_members.
    def visitObject_members(self, ctx:YiniParser.Object_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#object_member.
    def visitObject_member(self, ctx:YiniParser.Object_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#list_literal.
    def visitList_literal(self, ctx:YiniParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#elements.
    def visitElements(self, ctx:YiniParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#number_literal.
    def visitNumber_literal(self, ctx:YiniParser.Number_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#null_literal.
    def visitNull_literal(self, ctx:YiniParser.Null_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#string_literal.
    def visitString_literal(self, ctx:YiniParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#string_concat.
    def visitString_concat(self, ctx:YiniParser.String_concatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#boolean_literal.
    def visitBoolean_literal(self, ctx:YiniParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#bad_meta_text.
    def visitBad_meta_text(self, ctx:YiniParser.Bad_meta_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YiniParser#bad_member.
    def visitBad_member(self, ctx:YiniParser.Bad_memberContext):
        return self.visitChildren(ctx)



del YiniParser