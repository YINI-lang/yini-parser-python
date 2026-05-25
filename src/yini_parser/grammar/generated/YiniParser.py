# Generated from ./grammar/v1.0.0-rc.5xxxx/YiniParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,326,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        3,0,68,8,0,1,0,5,0,71,8,0,10,0,12,0,74,9,0,1,0,3,0,77,8,0,1,0,1,
        0,1,1,1,1,5,1,83,8,1,10,1,12,1,86,9,1,1,1,4,1,89,8,1,11,1,12,1,90,
        3,1,93,8,1,1,2,1,2,5,2,97,8,2,10,2,12,2,100,9,2,1,3,1,3,3,3,104,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,114,8,4,1,5,1,5,3,5,118,
        8,5,1,6,1,6,3,6,122,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,131,8,8,
        1,9,1,9,1,9,3,9,136,8,9,1,9,3,9,139,8,9,1,10,1,10,3,10,143,8,10,
        1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,4,13,153,8,13,11,13,12,13,
        154,1,14,1,14,1,14,1,15,1,15,1,15,3,15,163,8,15,1,16,1,16,1,16,1,
        16,3,16,169,8,16,1,17,1,17,1,17,1,17,3,17,175,8,17,1,18,1,18,4,18,
        179,8,18,11,18,12,18,180,1,19,1,19,5,19,185,8,19,10,19,12,19,188,
        9,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,5,22,198,8,22,10,22,
        12,22,201,9,22,1,22,3,22,204,8,22,1,22,5,22,207,8,22,10,22,12,22,
        210,9,22,1,22,1,22,5,22,214,8,22,10,22,12,22,217,9,22,1,22,1,22,
        5,22,221,8,22,10,22,12,22,224,9,22,3,22,226,8,22,1,23,1,23,1,23,
        5,23,231,8,23,10,23,12,23,234,9,23,1,23,5,23,237,8,23,10,23,12,23,
        240,9,23,1,23,3,23,243,8,23,1,24,1,24,1,24,1,24,1,25,1,25,1,26,1,
        26,5,26,253,8,26,10,26,12,26,256,9,26,1,26,3,26,259,8,26,1,26,5,
        26,262,8,26,10,26,12,26,265,9,26,1,26,1,26,5,26,269,8,26,10,26,12,
        26,272,9,26,1,26,1,26,5,26,276,8,26,10,26,12,26,279,9,26,3,26,281,
        8,26,1,27,1,27,5,27,285,8,27,10,27,12,27,288,9,27,1,27,1,27,5,27,
        292,8,27,10,27,12,27,295,9,27,1,27,5,27,298,8,27,10,27,12,27,301,
        9,27,1,27,3,27,304,8,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,
        1,32,1,32,3,32,316,8,32,1,32,1,32,1,32,3,32,321,8,32,1,32,3,32,324,
        8,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,3,2,0,8,10,13,14,
        2,0,19,19,21,21,1,0,8,9,347,0,67,1,0,0,0,2,92,1,0,0,0,4,94,1,0,0,
        0,6,103,1,0,0,0,8,113,1,0,0,0,10,115,1,0,0,0,12,119,1,0,0,0,14,123,
        1,0,0,0,16,130,1,0,0,0,18,138,1,0,0,0,20,140,1,0,0,0,22,146,1,0,
        0,0,24,148,1,0,0,0,26,152,1,0,0,0,28,156,1,0,0,0,30,159,1,0,0,0,
        32,168,1,0,0,0,34,174,1,0,0,0,36,176,1,0,0,0,38,182,1,0,0,0,40,191,
        1,0,0,0,42,193,1,0,0,0,44,225,1,0,0,0,46,227,1,0,0,0,48,244,1,0,
        0,0,50,248,1,0,0,0,52,280,1,0,0,0,54,282,1,0,0,0,56,305,1,0,0,0,
        58,307,1,0,0,0,60,309,1,0,0,0,62,311,1,0,0,0,64,315,1,0,0,0,66,68,
        3,2,1,0,67,66,1,0,0,0,67,68,1,0,0,0,68,72,1,0,0,0,69,71,3,8,4,0,
        70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,76,1,
        0,0,0,74,72,1,0,0,0,75,77,3,4,2,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        78,1,0,0,0,78,79,5,0,0,1,79,1,1,0,0,0,80,84,5,1,0,0,81,83,3,26,13,
        0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,93,
        1,0,0,0,86,84,1,0,0,0,87,89,3,26,13,0,88,87,1,0,0,0,89,90,1,0,0,
        0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,80,1,0,0,0,92,88,
        1,0,0,0,93,3,1,0,0,0,94,98,5,5,0,0,95,97,3,6,3,0,96,95,1,0,0,0,97,
        100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,5,1,0,0,0,100,98,1,0,
        0,0,101,104,3,26,13,0,102,104,3,10,5,0,103,101,1,0,0,0,103,102,1,
        0,0,0,104,7,1,0,0,0,105,114,3,26,13,0,106,114,3,10,5,0,107,114,3,
        12,6,0,108,114,5,6,0,0,109,114,3,14,7,0,110,114,3,28,14,0,111,114,
        3,16,8,0,112,114,3,64,32,0,113,105,1,0,0,0,113,106,1,0,0,0,113,107,
        1,0,0,0,113,108,1,0,0,0,113,109,1,0,0,0,113,110,1,0,0,0,113,111,
        1,0,0,0,113,112,1,0,0,0,114,9,1,0,0,0,115,117,5,35,0,0,116,118,3,
        26,13,0,117,116,1,0,0,0,117,118,1,0,0,0,118,11,1,0,0,0,119,121,5,
        34,0,0,120,122,3,26,13,0,121,120,1,0,0,0,121,122,1,0,0,0,122,13,
        1,0,0,0,123,124,5,7,0,0,124,15,1,0,0,0,125,131,3,18,9,0,126,131,
        3,24,12,0,127,128,3,62,31,0,128,129,3,26,13,0,129,131,1,0,0,0,130,
        125,1,0,0,0,130,126,1,0,0,0,130,127,1,0,0,0,131,17,1,0,0,0,132,139,
        3,20,10,0,133,135,5,3,0,0,134,136,3,42,21,0,135,134,1,0,0,0,135,
        136,1,0,0,0,136,137,1,0,0,0,137,139,3,26,13,0,138,132,1,0,0,0,138,
        133,1,0,0,0,139,19,1,0,0,0,140,142,5,2,0,0,141,143,3,22,11,0,142,
        141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,3,26,13,0,145,
        21,1,0,0,0,146,147,5,37,0,0,147,23,1,0,0,0,148,149,5,4,0,0,149,150,
        3,26,13,0,150,25,1,0,0,0,151,153,5,31,0,0,152,151,1,0,0,0,153,154,
        1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,27,1,0,0,0,156,157,3,
        30,15,0,157,158,3,26,13,0,158,29,1,0,0,0,159,160,5,37,0,0,160,162,
        5,19,0,0,161,163,3,32,16,0,162,161,1,0,0,0,162,163,1,0,0,0,163,31,
        1,0,0,0,164,169,3,36,18,0,165,169,3,34,17,0,166,169,3,52,26,0,167,
        169,3,44,22,0,168,164,1,0,0,0,168,165,1,0,0,0,168,166,1,0,0,0,168,
        167,1,0,0,0,169,33,1,0,0,0,170,175,3,58,29,0,171,175,3,42,21,0,172,
        175,3,56,28,0,173,175,3,60,30,0,174,170,1,0,0,0,174,171,1,0,0,0,
        174,172,1,0,0,0,174,173,1,0,0,0,175,35,1,0,0,0,176,178,5,13,0,0,
        177,179,3,38,19,0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,
        0,180,181,1,0,0,0,181,37,1,0,0,0,182,186,5,26,0,0,183,185,5,31,0,
        0,184,183,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,
        0,187,189,1,0,0,0,188,186,1,0,0,0,189,190,3,40,20,0,190,39,1,0,0,
        0,191,192,7,0,0,0,192,41,1,0,0,0,193,194,5,13,0,0,194,43,1,0,0,0,
        195,199,5,24,0,0,196,198,5,31,0,0,197,196,1,0,0,0,198,201,1,0,0,
        0,199,197,1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,
        0,202,204,3,46,23,0,203,202,1,0,0,0,203,204,1,0,0,0,204,208,1,0,
        0,0,205,207,5,31,0,0,206,205,1,0,0,0,207,210,1,0,0,0,208,206,1,0,
        0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,208,1,0,0,0,211,215,5,25,
        0,0,212,214,5,31,0,0,213,212,1,0,0,0,214,217,1,0,0,0,215,213,1,0,
        0,0,215,216,1,0,0,0,216,226,1,0,0,0,217,215,1,0,0,0,218,222,5,11,
        0,0,219,221,5,31,0,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,
        0,0,222,223,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,225,195,1,0,
        0,0,225,218,1,0,0,0,226,45,1,0,0,0,227,238,3,48,24,0,228,232,5,20,
        0,0,229,231,5,31,0,0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,
        0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,0,235,237,3,48,
        24,0,236,228,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,
        0,0,239,242,1,0,0,0,240,238,1,0,0,0,241,243,5,20,0,0,242,241,1,0,
        0,0,242,243,1,0,0,0,243,47,1,0,0,0,244,245,5,37,0,0,245,246,3,50,
        25,0,246,247,3,32,16,0,247,49,1,0,0,0,248,249,7,1,0,0,249,51,1,0,
        0,0,250,254,5,22,0,0,251,253,5,31,0,0,252,251,1,0,0,0,253,256,1,
        0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,258,1,0,0,0,256,254,1,
        0,0,0,257,259,3,54,27,0,258,257,1,0,0,0,258,259,1,0,0,0,259,263,
        1,0,0,0,260,262,5,31,0,0,261,260,1,0,0,0,262,265,1,0,0,0,263,261,
        1,0,0,0,263,264,1,0,0,0,264,266,1,0,0,0,265,263,1,0,0,0,266,270,
        5,23,0,0,267,269,5,31,0,0,268,267,1,0,0,0,269,272,1,0,0,0,270,268,
        1,0,0,0,270,271,1,0,0,0,271,281,1,0,0,0,272,270,1,0,0,0,273,277,
        5,12,0,0,274,276,5,31,0,0,275,274,1,0,0,0,276,279,1,0,0,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,280,250,
        1,0,0,0,280,273,1,0,0,0,281,53,1,0,0,0,282,299,3,32,16,0,283,285,
        5,31,0,0,284,283,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,
        1,0,0,0,287,289,1,0,0,0,288,286,1,0,0,0,289,293,5,20,0,0,290,292,
        5,31,0,0,291,290,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,
        1,0,0,0,294,296,1,0,0,0,295,293,1,0,0,0,296,298,3,32,16,0,297,286,
        1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,303,
        1,0,0,0,301,299,1,0,0,0,302,304,5,20,0,0,303,302,1,0,0,0,303,304,
        1,0,0,0,304,55,1,0,0,0,305,306,5,14,0,0,306,57,1,0,0,0,307,308,5,
        10,0,0,308,59,1,0,0,0,309,310,7,2,0,0,310,61,1,0,0,0,311,312,5,40,
        0,0,312,63,1,0,0,0,313,316,5,39,0,0,314,316,3,32,16,0,315,313,1,
        0,0,0,315,314,1,0,0,0,315,316,1,0,0,0,316,317,1,0,0,0,317,320,5,
        19,0,0,318,321,3,32,16,0,319,321,5,39,0,0,320,318,1,0,0,0,320,319,
        1,0,0,0,321,323,1,0,0,0,322,324,3,26,13,0,323,322,1,0,0,0,323,324,
        1,0,0,0,324,65,1,0,0,0,43,67,72,76,84,90,92,98,103,113,117,121,130,
        135,138,142,154,162,168,174,180,186,199,203,208,215,222,225,232,
        238,242,254,258,263,270,277,280,286,293,299,303,315,320,323
    ]

class YiniParser ( Parser ):

    grammarFileName = "YiniParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{}'", "'[]'", 
                     "<INVALID>", "<INVALID>", "'^'", "'\\u00A7'", "'>'", 
                     "'<'", "'='", "','", "':'", "'['", "']'", "'{'", "'}'", 
                     "'+'", "'$'", "'%'", "'@'", "';'" ]

    symbolicNames = [ "<INVALID>", "SHEBANG", "YINI_TOKEN", "INCLUDE_TOKEN", 
                      "DEPRECATED_TOKEN", "TERMINAL_TOKEN", "SECTION_HEAD", 
                      "INVALID_SECTION_HEAD", "BOOLEAN_FALSE", "BOOLEAN_TRUE", 
                      "NULL", "EMPTY_OBJECT", "EMPTY_LIST", "STRING", "NUMBER", 
                      "CARET", "SS", "GT", "LT", "EQ", "COMMA", "COLON", 
                      "OB", "CB", "OC", "CC", "PLUS", "DOLLAR", "PC", "AT", 
                      "SEMICOLON", "NL", "WS", "BLOCK_COMMENT", "DISABLED_LINE", 
                      "FULL_LINE_COMMENT", "INLINE_COMMENT", "KEY", "IDENT_INVALID", 
                      "REST", "META_INVALID" ]

    RULE_yini = 0
    RULE_prolog = 1
    RULE_terminal_stmt = 2
    RULE_terminal_trivia = 3
    RULE_stmt = 4
    RULE_full_line_comment_stmt = 5
    RULE_disabled_line_stmt = 6
    RULE_invalid_section_stmt = 7
    RULE_meta_stmt = 8
    RULE_directive = 9
    RULE_yini_directive = 10
    RULE_yini_mode_declaration = 11
    RULE_annotation = 12
    RULE_eol = 13
    RULE_assignment = 14
    RULE_member = 15
    RULE_value = 16
    RULE_scalar_value = 17
    RULE_concat_expression = 18
    RULE_concat_tail = 19
    RULE_concat_operand = 20
    RULE_string_literal = 21
    RULE_object_literal = 22
    RULE_object_members = 23
    RULE_object_member = 24
    RULE_object_member_separator = 25
    RULE_list_literal = 26
    RULE_elements = 27
    RULE_number_literal = 28
    RULE_null_literal = 29
    RULE_boolean_literal = 30
    RULE_bad_meta_text = 31
    RULE_bad_member = 32

    ruleNames =  [ "yini", "prolog", "terminal_stmt", "terminal_trivia", 
                   "stmt", "full_line_comment_stmt", "disabled_line_stmt", 
                   "invalid_section_stmt", "meta_stmt", "directive", "yini_directive", 
                   "yini_mode_declaration", "annotation", "eol", "assignment", 
                   "member", "value", "scalar_value", "concat_expression", 
                   "concat_tail", "concat_operand", "string_literal", "object_literal", 
                   "object_members", "object_member", "object_member_separator", 
                   "list_literal", "elements", "number_literal", "null_literal", 
                   "boolean_literal", "bad_meta_text", "bad_member" ]

    EOF = Token.EOF
    SHEBANG=1
    YINI_TOKEN=2
    INCLUDE_TOKEN=3
    DEPRECATED_TOKEN=4
    TERMINAL_TOKEN=5
    SECTION_HEAD=6
    INVALID_SECTION_HEAD=7
    BOOLEAN_FALSE=8
    BOOLEAN_TRUE=9
    NULL=10
    EMPTY_OBJECT=11
    EMPTY_LIST=12
    STRING=13
    NUMBER=14
    CARET=15
    SS=16
    GT=17
    LT=18
    EQ=19
    COMMA=20
    COLON=21
    OB=22
    CB=23
    OC=24
    CC=25
    PLUS=26
    DOLLAR=27
    PC=28
    AT=29
    SEMICOLON=30
    NL=31
    WS=32
    BLOCK_COMMENT=33
    DISABLED_LINE=34
    FULL_LINE_COMMENT=35
    INLINE_COMMENT=36
    KEY=37
    IDENT_INVALID=38
    REST=39
    META_INVALID=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class YiniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YiniParser.EOF, 0)

        def prolog(self):
            return self.getTypedRuleContext(YiniParser.PrologContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.StmtContext)
            else:
                return self.getTypedRuleContext(YiniParser.StmtContext,i)


        def terminal_stmt(self):
            return self.getTypedRuleContext(YiniParser.Terminal_stmtContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_yini

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini" ):
                return visitor.visitYini(self)
            else:
                return visitor.visitChildren(self)




    def yini(self):

        localctx = YiniParser.YiniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_yini)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 66
                self.prolog()


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1840415014876) != 0):
                self.state = 69
                self.stmt()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 75
                self.terminal_stmt()


            self.state = 78
            self.match(YiniParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrologContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHEBANG(self):
            return self.getToken(YiniParser.SHEBANG, 0)

        def eol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.EolContext)
            else:
                return self.getTypedRuleContext(YiniParser.EolContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_prolog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProlog" ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = YiniParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(YiniParser.SHEBANG)
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 81
                        self.eol() 
                    self.state = 86
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 87
                        self.eol()

                    else:
                        raise NoViableAltException(self)
                    self.state = 90 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terminal_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERMINAL_TOKEN(self):
            return self.getToken(YiniParser.TERMINAL_TOKEN, 0)

        def terminal_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Terminal_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Terminal_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_terminal_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_stmt" ):
                return visitor.visitTerminal_stmt(self)
            else:
                return visitor.visitChildren(self)




    def terminal_stmt(self):

        localctx = YiniParser.Terminal_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_terminal_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(YiniParser.TERMINAL_TOKEN)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==35:
                self.state = 95
                self.terminal_trivia()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terminal_triviaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def full_line_comment_stmt(self):
            return self.getTypedRuleContext(YiniParser.Full_line_comment_stmtContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_terminal_trivia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_trivia" ):
                return visitor.visitTerminal_trivia(self)
            else:
                return visitor.visitChildren(self)




    def terminal_trivia(self):

        localctx = YiniParser.Terminal_triviaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_terminal_trivia)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.eol()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.full_line_comment_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def full_line_comment_stmt(self):
            return self.getTypedRuleContext(YiniParser.Full_line_comment_stmtContext,0)


        def disabled_line_stmt(self):
            return self.getTypedRuleContext(YiniParser.Disabled_line_stmtContext,0)


        def SECTION_HEAD(self):
            return self.getToken(YiniParser.SECTION_HEAD, 0)

        def invalid_section_stmt(self):
            return self.getTypedRuleContext(YiniParser.Invalid_section_stmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(YiniParser.AssignmentContext,0)


        def meta_stmt(self):
            return self.getTypedRuleContext(YiniParser.Meta_stmtContext,0)


        def bad_member(self):
            return self.getTypedRuleContext(YiniParser.Bad_memberContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = YiniParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.eol()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.full_line_comment_stmt()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.disabled_line_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.match(YiniParser.SECTION_HEAD)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.invalid_section_stmt()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.assignment()
                pass
            elif token in [2, 3, 4, 40]:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.meta_stmt()
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 19, 22, 24, 39]:
                self.enterOuterAlt(localctx, 8)
                self.state = 112
                self.bad_member()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_line_comment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FULL_LINE_COMMENT(self):
            return self.getToken(YiniParser.FULL_LINE_COMMENT, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_full_line_comment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_line_comment_stmt" ):
                return visitor.visitFull_line_comment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def full_line_comment_stmt(self):

        localctx = YiniParser.Full_line_comment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_full_line_comment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(YiniParser.FULL_LINE_COMMENT)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 116
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Disabled_line_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISABLED_LINE(self):
            return self.getToken(YiniParser.DISABLED_LINE, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_disabled_line_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisabled_line_stmt" ):
                return visitor.visitDisabled_line_stmt(self)
            else:
                return visitor.visitChildren(self)




    def disabled_line_stmt(self):

        localctx = YiniParser.Disabled_line_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_disabled_line_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(YiniParser.DISABLED_LINE)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 120
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invalid_section_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INVALID_SECTION_HEAD(self):
            return self.getToken(YiniParser.INVALID_SECTION_HEAD, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_invalid_section_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvalid_section_stmt" ):
                return visitor.visitInvalid_section_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invalid_section_stmt(self):

        localctx = YiniParser.Invalid_section_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_invalid_section_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(YiniParser.INVALID_SECTION_HEAD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(YiniParser.DirectiveContext,0)


        def annotation(self):
            return self.getTypedRuleContext(YiniParser.AnnotationContext,0)


        def bad_meta_text(self):
            return self.getTypedRuleContext(YiniParser.Bad_meta_textContext,0)


        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_meta_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_stmt" ):
                return visitor.visitMeta_stmt(self)
            else:
                return visitor.visitChildren(self)




    def meta_stmt(self):

        localctx = YiniParser.Meta_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_meta_stmt)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.directive()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.annotation()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.bad_meta_text()
                self.state = 128
                self.eol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def yini_directive(self):
            return self.getTypedRuleContext(YiniParser.Yini_directiveContext,0)


        def INCLUDE_TOKEN(self):
            return self.getToken(YiniParser.INCLUDE_TOKEN, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(YiniParser.String_literalContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = YiniParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.yini_directive()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(YiniParser.INCLUDE_TOKEN)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 134
                    self.string_literal()


                self.state = 137
                self.eol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Yini_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def YINI_TOKEN(self):
            return self.getToken(YiniParser.YINI_TOKEN, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def yini_mode_declaration(self):
            return self.getTypedRuleContext(YiniParser.Yini_mode_declarationContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_yini_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini_directive" ):
                return visitor.visitYini_directive(self)
            else:
                return visitor.visitChildren(self)




    def yini_directive(self):

        localctx = YiniParser.Yini_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_yini_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(YiniParser.YINI_TOKEN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 141
                self.yini_mode_declaration()


            self.state = 144
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Yini_mode_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_yini_mode_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini_mode_declaration" ):
                return visitor.visitYini_mode_declaration(self)
            else:
                return visitor.visitChildren(self)




    def yini_mode_declaration(self):

        localctx = YiniParser.Yini_mode_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_yini_mode_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(YiniParser.KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEPRECATED_TOKEN(self):
            return self.getToken(YiniParser.DEPRECATED_TOKEN, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_annotation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = YiniParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(YiniParser.DEPRECATED_TOKEN)
            self.state = 149
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_eol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEol" ):
                return visitor.visitEol(self)
            else:
                return visitor.visitChildren(self)




    def eol(self):

        localctx = YiniParser.EolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 151
                    self.match(YiniParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 154 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(YiniParser.MemberContext,0)


        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = YiniParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.member()
            self.state = 157
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def EQ(self):
            return self.getToken(YiniParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(YiniParser.ValueContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = YiniParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(YiniParser.KEY)
            self.state = 160
            self.match(YiniParser.EQ)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21004032) != 0):
                self.state = 161
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat_expression(self):
            return self.getTypedRuleContext(YiniParser.Concat_expressionContext,0)


        def scalar_value(self):
            return self.getTypedRuleContext(YiniParser.Scalar_valueContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(YiniParser.List_literalContext,0)


        def object_literal(self):
            return self.getTypedRuleContext(YiniParser.Object_literalContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = YiniParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_value)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.concat_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.scalar_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.list_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.object_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def null_literal(self):
            return self.getTypedRuleContext(YiniParser.Null_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(YiniParser.String_literalContext,0)


        def number_literal(self):
            return self.getTypedRuleContext(YiniParser.Number_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(YiniParser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_scalar_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_value" ):
                return visitor.visitScalar_value(self)
            else:
                return visitor.visitChildren(self)




    def scalar_value(self):

        localctx = YiniParser.Scalar_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_scalar_value)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.null_literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.string_literal()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.number_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 173
                self.boolean_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def concat_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Concat_tailContext)
            else:
                return self.getTypedRuleContext(YiniParser.Concat_tailContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_concat_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_expression" ):
                return visitor.visitConcat_expression(self)
            else:
                return visitor.visitChildren(self)




    def concat_expression(self):

        localctx = YiniParser.Concat_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_concat_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(YiniParser.STRING)
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.concat_tail()
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==26):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(YiniParser.PLUS, 0)

        def concat_operand(self):
            return self.getTypedRuleContext(YiniParser.Concat_operandContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_concat_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_tail" ):
                return visitor.visitConcat_tail(self)
            else:
                return visitor.visitChildren(self)




    def concat_tail(self):

        localctx = YiniParser.Concat_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concat_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(YiniParser.PLUS)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 183
                self.match(YiniParser.NL)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self.concat_operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_operandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(YiniParser.NUMBER, 0)

        def BOOLEAN_TRUE(self):
            return self.getToken(YiniParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(YiniParser.BOOLEAN_FALSE, 0)

        def NULL(self):
            return self.getToken(YiniParser.NULL, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_concat_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_operand" ):
                return visitor.visitConcat_operand(self)
            else:
                return visitor.visitChildren(self)




    def concat_operand(self):

        localctx = YiniParser.Concat_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_concat_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_string_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = YiniParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(YiniParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OC(self):
            return self.getToken(YiniParser.OC, 0)

        def CC(self):
            return self.getToken(YiniParser.CC, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def object_members(self):
            return self.getTypedRuleContext(YiniParser.Object_membersContext,0)


        def EMPTY_OBJECT(self):
            return self.getToken(YiniParser.EMPTY_OBJECT, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_object_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_literal" ):
                return visitor.visitObject_literal(self)
            else:
                return visitor.visitChildren(self)




    def object_literal(self):

        localctx = YiniParser.Object_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_object_literal)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(YiniParser.OC)
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 196
                        self.match(YiniParser.NL) 
                    self.state = 201
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 202
                    self.object_members()


                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 205
                    self.match(YiniParser.NL)
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 211
                self.match(YiniParser.CC)
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 212
                        self.match(YiniParser.NL) 
                    self.state = 217
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(YiniParser.EMPTY_OBJECT)
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 219
                        self.match(YiniParser.NL) 
                    self.state = 224
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Object_memberContext)
            else:
                return self.getTypedRuleContext(YiniParser.Object_memberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.COMMA)
            else:
                return self.getToken(YiniParser.COMMA, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_object_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_members" ):
                return visitor.visitObject_members(self)
            else:
                return visitor.visitChildren(self)




    def object_members(self):

        localctx = YiniParser.Object_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_object_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.object_member()
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 228
                    self.match(YiniParser.COMMA)
                    self.state = 232
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 229
                        self.match(YiniParser.NL)
                        self.state = 234
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 235
                    self.object_member() 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 241
                self.match(YiniParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def object_member_separator(self):
            return self.getTypedRuleContext(YiniParser.Object_member_separatorContext,0)


        def value(self):
            return self.getTypedRuleContext(YiniParser.ValueContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_object_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_member" ):
                return visitor.visitObject_member(self)
            else:
                return visitor.visitChildren(self)




    def object_member(self):

        localctx = YiniParser.Object_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_object_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(YiniParser.KEY)
            self.state = 245
            self.object_member_separator()
            self.state = 246
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_member_separatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YiniParser.COLON, 0)

        def EQ(self):
            return self.getToken(YiniParser.EQ, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_object_member_separator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_member_separator" ):
                return visitor.visitObject_member_separator(self)
            else:
                return visitor.visitChildren(self)




    def object_member_separator(self):

        localctx = YiniParser.Object_member_separatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_object_member_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==19 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(YiniParser.OB, 0)

        def CB(self):
            return self.getToken(YiniParser.CB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def elements(self):
            return self.getTypedRuleContext(YiniParser.ElementsContext,0)


        def EMPTY_LIST(self):
            return self.getToken(YiniParser.EMPTY_LIST, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = YiniParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(YiniParser.OB)
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 251
                        self.match(YiniParser.NL) 
                    self.state = 256
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21004032) != 0):
                    self.state = 257
                    self.elements()


                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 260
                    self.match(YiniParser.NL)
                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 266
                self.match(YiniParser.CB)
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 267
                        self.match(YiniParser.NL) 
                    self.state = 272
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(YiniParser.EMPTY_LIST)
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 274
                        self.match(YiniParser.NL) 
                    self.state = 279
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.ValueContext)
            else:
                return self.getTypedRuleContext(YiniParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.COMMA)
            else:
                return self.getToken(YiniParser.COMMA, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = YiniParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.value()
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 283
                        self.match(YiniParser.NL)
                        self.state = 288
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 289
                    self.match(YiniParser.COMMA)
                    self.state = 293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 290
                        self.match(YiniParser.NL)
                        self.state = 295
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 296
                    self.value() 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 302
                self.match(YiniParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YiniParser.NUMBER, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_number_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_literal" ):
                return visitor.visitNumber_literal(self)
            else:
                return visitor.visitChildren(self)




    def number_literal(self):

        localctx = YiniParser.Number_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(YiniParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(YiniParser.NULL, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_null_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull_literal" ):
                return visitor.visitNull_literal(self)
            else:
                return visitor.visitChildren(self)




    def null_literal(self):

        localctx = YiniParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(YiniParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_TRUE(self):
            return self.getToken(YiniParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(YiniParser.BOOLEAN_FALSE, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = YiniParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bad_meta_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def META_INVALID(self):
            return self.getToken(YiniParser.META_INVALID, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_bad_meta_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBad_meta_text" ):
                return visitor.visitBad_meta_text(self)
            else:
                return visitor.visitChildren(self)




    def bad_meta_text(self):

        localctx = YiniParser.Bad_meta_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_bad_meta_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(YiniParser.META_INVALID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bad_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(YiniParser.EQ, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.ValueContext)
            else:
                return self.getTypedRuleContext(YiniParser.ValueContext,i)


        def REST(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.REST)
            else:
                return self.getToken(YiniParser.REST, i)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_bad_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBad_member" ):
                return visitor.visitBad_member(self)
            else:
                return visitor.visitChildren(self)




    def bad_member(self):

        localctx = YiniParser.Bad_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_bad_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 313
                self.match(YiniParser.REST)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 22, 24]:
                self.state = 314
                self.value()
                pass
            elif token in [19]:
                pass
            else:
                pass
            self.state = 317
            self.match(YiniParser.EQ)
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 14, 22, 24]:
                self.state = 318
                self.value()
                pass
            elif token in [39]:
                self.state = 319
                self.match(YiniParser.REST)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 322
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





