# Generated from ./grammar/v1.0.0-rc.6x/YiniParser.g4 by ANTLR 4.13.2
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
        4,1,40,332,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,3,0,74,8,0,1,0,5,0,77,8,0,10,0,12,0,
        80,9,0,1,0,3,0,83,8,0,1,0,1,0,1,1,1,1,5,1,89,8,1,10,1,12,1,92,9,
        1,1,1,4,1,95,8,1,11,1,12,1,96,3,1,99,8,1,1,2,1,2,5,2,103,8,2,10,
        2,12,2,106,9,2,1,3,1,3,3,3,110,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,120,8,4,1,5,1,5,3,5,124,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,3,8,135,8,8,1,9,1,9,1,9,3,9,140,8,9,1,9,3,9,143,8,9,1,10,1,
        10,3,10,147,8,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,4,13,157,
        8,13,11,13,12,13,158,1,14,1,14,3,14,163,8,14,1,15,1,15,1,15,1,16,
        1,16,1,17,1,17,1,17,3,17,173,8,17,1,18,1,18,1,18,1,18,3,18,179,8,
        18,1,19,1,19,1,19,1,19,3,19,185,8,19,1,20,1,20,4,20,189,8,20,11,
        20,12,20,190,1,21,1,21,5,21,195,8,21,10,21,12,21,198,9,21,1,21,1,
        21,1,22,1,22,1,23,1,23,1,24,1,24,5,24,208,8,24,10,24,12,24,211,9,
        24,1,24,3,24,214,8,24,1,24,5,24,217,8,24,10,24,12,24,220,9,24,1,
        24,1,24,3,24,224,8,24,1,25,1,25,5,25,228,8,25,10,25,12,25,231,9,
        25,1,25,1,25,5,25,235,8,25,10,25,12,25,238,9,25,1,25,5,25,241,8,
        25,10,25,12,25,244,9,25,1,25,5,25,247,8,25,10,25,12,25,250,9,25,
        1,25,3,25,253,8,25,1,26,1,26,1,26,1,26,1,27,1,27,1,28,1,28,5,28,
        263,8,28,10,28,12,28,266,9,28,1,28,3,28,269,8,28,1,28,5,28,272,8,
        28,10,28,12,28,275,9,28,1,28,1,28,3,28,279,8,28,1,29,1,29,5,29,283,
        8,29,10,29,12,29,286,9,29,1,29,1,29,5,29,290,8,29,10,29,12,29,293,
        9,29,1,29,5,29,296,8,29,10,29,12,29,299,9,29,1,29,5,29,302,8,29,
        10,29,12,29,305,9,29,1,29,3,29,308,8,29,1,30,1,30,1,31,1,31,1,32,
        1,32,1,33,1,33,1,34,1,34,1,35,1,35,3,35,322,8,35,1,35,1,35,1,35,
        3,35,327,8,35,1,35,3,35,330,8,35,1,35,0,0,36,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,0,5,2,0,8,10,37,37,2,0,8,10,13,14,2,0,19,19,21,
        21,2,0,31,31,34,35,1,0,8,9,349,0,73,1,0,0,0,2,98,1,0,0,0,4,100,1,
        0,0,0,6,109,1,0,0,0,8,119,1,0,0,0,10,121,1,0,0,0,12,125,1,0,0,0,
        14,127,1,0,0,0,16,134,1,0,0,0,18,142,1,0,0,0,20,144,1,0,0,0,22,150,
        1,0,0,0,24,152,1,0,0,0,26,156,1,0,0,0,28,162,1,0,0,0,30,164,1,0,
        0,0,32,167,1,0,0,0,34,169,1,0,0,0,36,178,1,0,0,0,38,184,1,0,0,0,
        40,186,1,0,0,0,42,192,1,0,0,0,44,201,1,0,0,0,46,203,1,0,0,0,48,223,
        1,0,0,0,50,225,1,0,0,0,52,254,1,0,0,0,54,258,1,0,0,0,56,278,1,0,
        0,0,58,280,1,0,0,0,60,309,1,0,0,0,62,311,1,0,0,0,64,313,1,0,0,0,
        66,315,1,0,0,0,68,317,1,0,0,0,70,321,1,0,0,0,72,74,3,2,1,0,73,72,
        1,0,0,0,73,74,1,0,0,0,74,78,1,0,0,0,75,77,3,8,4,0,76,75,1,0,0,0,
        77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,82,1,0,0,0,80,78,1,
        0,0,0,81,83,3,4,2,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,
        85,5,0,0,1,85,1,1,0,0,0,86,90,5,1,0,0,87,89,3,26,13,0,88,87,1,0,
        0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,99,1,0,0,0,92,90,
        1,0,0,0,93,95,3,26,13,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,
        0,96,97,1,0,0,0,97,99,1,0,0,0,98,86,1,0,0,0,98,94,1,0,0,0,99,3,1,
        0,0,0,100,104,5,5,0,0,101,103,3,6,3,0,102,101,1,0,0,0,103,106,1,
        0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,5,1,0,0,0,106,104,1,0,
        0,0,107,110,3,26,13,0,108,110,3,10,5,0,109,107,1,0,0,0,109,108,1,
        0,0,0,110,7,1,0,0,0,111,120,3,26,13,0,112,120,3,10,5,0,113,120,3,
        12,6,0,114,120,5,6,0,0,115,120,3,14,7,0,116,120,3,30,15,0,117,120,
        3,16,8,0,118,120,3,70,35,0,119,111,1,0,0,0,119,112,1,0,0,0,119,113,
        1,0,0,0,119,114,1,0,0,0,119,115,1,0,0,0,119,116,1,0,0,0,119,117,
        1,0,0,0,119,118,1,0,0,0,120,9,1,0,0,0,121,123,5,35,0,0,122,124,3,
        26,13,0,123,122,1,0,0,0,123,124,1,0,0,0,124,11,1,0,0,0,125,126,5,
        34,0,0,126,13,1,0,0,0,127,128,5,7,0,0,128,15,1,0,0,0,129,135,3,18,
        9,0,130,135,3,24,12,0,131,132,3,68,34,0,132,133,3,28,14,0,133,135,
        1,0,0,0,134,129,1,0,0,0,134,130,1,0,0,0,134,131,1,0,0,0,135,17,1,
        0,0,0,136,143,3,20,10,0,137,139,5,3,0,0,138,140,3,46,23,0,139,138,
        1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,143,3,28,14,0,142,136,
        1,0,0,0,142,137,1,0,0,0,143,19,1,0,0,0,144,146,5,2,0,0,145,147,3,
        22,11,0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,
        3,28,14,0,149,21,1,0,0,0,150,151,5,37,0,0,151,23,1,0,0,0,152,153,
        5,4,0,0,153,154,3,28,14,0,154,25,1,0,0,0,155,157,5,31,0,0,156,155,
        1,0,0,0,157,158,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,27,1,
        0,0,0,160,163,3,26,13,0,161,163,5,0,0,1,162,160,1,0,0,0,162,161,
        1,0,0,0,163,29,1,0,0,0,164,165,3,34,17,0,165,166,3,28,14,0,166,31,
        1,0,0,0,167,168,7,0,0,0,168,33,1,0,0,0,169,170,3,32,16,0,170,172,
        5,19,0,0,171,173,3,36,18,0,172,171,1,0,0,0,172,173,1,0,0,0,173,35,
        1,0,0,0,174,179,3,40,20,0,175,179,3,38,19,0,176,179,3,56,28,0,177,
        179,3,48,24,0,178,174,1,0,0,0,178,175,1,0,0,0,178,176,1,0,0,0,178,
        177,1,0,0,0,179,37,1,0,0,0,180,185,3,64,32,0,181,185,3,46,23,0,182,
        185,3,62,31,0,183,185,3,66,33,0,184,180,1,0,0,0,184,181,1,0,0,0,
        184,182,1,0,0,0,184,183,1,0,0,0,185,39,1,0,0,0,186,188,5,13,0,0,
        187,189,3,42,21,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,1,0,0,
        0,190,191,1,0,0,0,191,41,1,0,0,0,192,196,5,26,0,0,193,195,3,60,30,
        0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,
        0,197,199,1,0,0,0,198,196,1,0,0,0,199,200,3,44,22,0,200,43,1,0,0,
        0,201,202,7,1,0,0,202,45,1,0,0,0,203,204,5,13,0,0,204,47,1,0,0,0,
        205,209,5,24,0,0,206,208,3,60,30,0,207,206,1,0,0,0,208,211,1,0,0,
        0,209,207,1,0,0,0,209,210,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,
        0,212,214,3,50,25,0,213,212,1,0,0,0,213,214,1,0,0,0,214,218,1,0,
        0,0,215,217,3,60,30,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,
        0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,0,221,224,5,
        25,0,0,222,224,5,11,0,0,223,205,1,0,0,0,223,222,1,0,0,0,224,49,1,
        0,0,0,225,242,3,52,26,0,226,228,3,60,30,0,227,226,1,0,0,0,228,231,
        1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,229,
        1,0,0,0,232,236,5,20,0,0,233,235,3,60,30,0,234,233,1,0,0,0,235,238,
        1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,
        1,0,0,0,239,241,3,52,26,0,240,229,1,0,0,0,241,244,1,0,0,0,242,240,
        1,0,0,0,242,243,1,0,0,0,243,252,1,0,0,0,244,242,1,0,0,0,245,247,
        3,60,30,0,246,245,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,
        1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,0,251,253,5,20,0,0,252,248,
        1,0,0,0,252,253,1,0,0,0,253,51,1,0,0,0,254,255,3,32,16,0,255,256,
        3,54,27,0,256,257,3,36,18,0,257,53,1,0,0,0,258,259,7,2,0,0,259,55,
        1,0,0,0,260,264,5,22,0,0,261,263,3,60,30,0,262,261,1,0,0,0,263,266,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,267,269,3,58,29,0,268,267,1,0,0,0,268,269,1,0,0,0,269,273,
        1,0,0,0,270,272,3,60,30,0,271,270,1,0,0,0,272,275,1,0,0,0,273,271,
        1,0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,275,273,1,0,0,0,276,279,
        5,23,0,0,277,279,5,12,0,0,278,260,1,0,0,0,278,277,1,0,0,0,279,57,
        1,0,0,0,280,297,3,36,18,0,281,283,3,60,30,0,282,281,1,0,0,0,283,
        286,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,
        284,1,0,0,0,287,291,5,20,0,0,288,290,3,60,30,0,289,288,1,0,0,0,290,
        293,1,0,0,0,291,289,1,0,0,0,291,292,1,0,0,0,292,294,1,0,0,0,293,
        291,1,0,0,0,294,296,3,36,18,0,295,284,1,0,0,0,296,299,1,0,0,0,297,
        295,1,0,0,0,297,298,1,0,0,0,298,307,1,0,0,0,299,297,1,0,0,0,300,
        302,3,60,30,0,301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,
        304,1,0,0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,308,5,20,0,0,307,
        303,1,0,0,0,307,308,1,0,0,0,308,59,1,0,0,0,309,310,7,3,0,0,310,61,
        1,0,0,0,311,312,5,14,0,0,312,63,1,0,0,0,313,314,5,10,0,0,314,65,
        1,0,0,0,315,316,7,4,0,0,316,67,1,0,0,0,317,318,5,40,0,0,318,69,1,
        0,0,0,319,322,5,39,0,0,320,322,3,36,18,0,321,319,1,0,0,0,321,320,
        1,0,0,0,321,322,1,0,0,0,322,323,1,0,0,0,323,326,5,19,0,0,324,327,
        3,36,18,0,325,327,5,39,0,0,326,324,1,0,0,0,326,325,1,0,0,0,327,329,
        1,0,0,0,328,330,3,26,13,0,329,328,1,0,0,0,329,330,1,0,0,0,330,71,
        1,0,0,0,42,73,78,82,90,96,98,104,109,119,123,134,139,142,146,158,
        162,172,178,184,190,196,209,213,218,223,229,236,242,248,252,264,
        268,273,278,284,291,297,303,307,321,326,329
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
    RULE_line_end = 14
    RULE_assignment = 15
    RULE_identifier = 16
    RULE_member = 17
    RULE_value = 18
    RULE_scalar_value = 19
    RULE_concat_expression = 20
    RULE_concat_tail = 21
    RULE_concat_operand = 22
    RULE_string_literal = 23
    RULE_object_literal = 24
    RULE_object_members = 25
    RULE_object_member = 26
    RULE_object_member_separator = 27
    RULE_list_literal = 28
    RULE_elements = 29
    RULE_multiline_trivia = 30
    RULE_number_literal = 31
    RULE_null_literal = 32
    RULE_boolean_literal = 33
    RULE_bad_meta_text = 34
    RULE_bad_member = 35

    ruleNames =  [ "yini", "prolog", "terminal_stmt", "terminal_trivia", 
                   "stmt", "full_line_comment_stmt", "disabled_line_stmt", 
                   "invalid_section_stmt", "meta_stmt", "directive", "yini_directive", 
                   "yini_mode_declaration", "annotation", "eol", "line_end", 
                   "assignment", "identifier", "member", "value", "scalar_value", 
                   "concat_expression", "concat_tail", "concat_operand", 
                   "string_literal", "object_literal", "object_members", 
                   "object_member", "object_member_separator", "list_literal", 
                   "elements", "multiline_trivia", "number_literal", "null_literal", 
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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 72
                self.prolog()


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1840415014876) != 0):
                self.state = 75
                self.stmt()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 81
                self.terminal_stmt()


            self.state = 84
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(YiniParser.SHEBANG)
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 87
                        self.eol() 
                    self.state = 92
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 93
                        self.eol()

                    else:
                        raise NoViableAltException(self)
                    self.state = 96 
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
            self.state = 100
            self.match(YiniParser.TERMINAL_TOKEN)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==35:
                self.state = 101
                self.terminal_trivia()
                self.state = 106
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
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.eol()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.eol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.full_line_comment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.disabled_line_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(YiniParser.SECTION_HEAD)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.invalid_section_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
                self.meta_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 118
                self.bad_member()
                pass


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
            self.state = 121
            self.match(YiniParser.FULL_LINE_COMMENT)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 122
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
            self.state = 125
            self.match(YiniParser.DISABLED_LINE)
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
            self.state = 127
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


        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.directive()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.annotation()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.bad_meta_text()
                self.state = 132
                self.line_end()
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

        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.yini_directive()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(YiniParser.INCLUDE_TOKEN)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 138
                    self.string_literal()


                self.state = 141
                self.line_end()
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

        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


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
            self.state = 144
            self.match(YiniParser.YINI_TOKEN)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 145
                self.yini_mode_declaration()


            self.state = 148
            self.line_end()
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
            self.state = 150
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

        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


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
            self.state = 152
            self.match(YiniParser.DEPRECATED_TOKEN)
            self.state = 153
            self.line_end()
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
            self.state = 156 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 155
                    self.match(YiniParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 158 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def EOF(self):
            return self.getToken(YiniParser.EOF, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_line_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_end" ):
                return visitor.visitLine_end(self)
            else:
                return visitor.visitChildren(self)




    def line_end(self):

        localctx = YiniParser.Line_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_line_end)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.eol()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(YiniParser.EOF)
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(YiniParser.MemberContext,0)


        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = YiniParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.member()
            self.state = 165
            self.line_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def BOOLEAN_TRUE(self):
            return self.getToken(YiniParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(YiniParser.BOOLEAN_FALSE, 0)

        def NULL(self):
            return self.getToken(YiniParser.NULL, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = YiniParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137438955264) != 0)):
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


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(YiniParser.IdentifierContext,0)


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
        self.enterRule(localctx, 34, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.identifier()
            self.state = 170
            self.match(YiniParser.EQ)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21004032) != 0):
                self.state = 171
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
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.concat_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.scalar_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.list_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
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
        self.enterRule(localctx, 38, self.RULE_scalar_value)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.null_literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.string_literal()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.number_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
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
        self.enterRule(localctx, 40, self.RULE_concat_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(YiniParser.STRING)
            self.state = 188 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 187
                self.concat_tail()
                self.state = 190 
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


        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_concat_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_tail" ):
                return visitor.visitConcat_tail(self)
            else:
                return visitor.visitChildren(self)




    def concat_tail(self):

        localctx = YiniParser.Concat_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_concat_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(YiniParser.PLUS)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                self.state = 193
                self.multiline_trivia()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
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
        self.enterRule(localctx, 44, self.RULE_concat_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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
        self.enterRule(localctx, 46, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


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
        self.enterRule(localctx, 48, self.RULE_object_literal)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(YiniParser.OC)
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 206
                        self.multiline_trivia() 
                    self.state = 211
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 137438955264) != 0):
                    self.state = 212
                    self.object_members()


                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                    self.state = 215
                    self.multiline_trivia()
                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 221
                self.match(YiniParser.CC)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(YiniParser.EMPTY_OBJECT)
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_object_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_members" ):
                return visitor.visitObject_members(self)
            else:
                return visitor.visitChildren(self)




    def object_members(self):

        localctx = YiniParser.Object_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_object_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.object_member()
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                        self.state = 226
                        self.multiline_trivia()
                        self.state = 231
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 232
                    self.match(YiniParser.COMMA)
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                        self.state = 233
                        self.multiline_trivia()
                        self.state = 238
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 239
                    self.object_member() 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                    self.state = 245
                    self.multiline_trivia()
                    self.state = 250
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 251
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

        def identifier(self):
            return self.getTypedRuleContext(YiniParser.IdentifierContext,0)


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
        self.enterRule(localctx, 52, self.RULE_object_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.identifier()
            self.state = 255
            self.object_member_separator()
            self.state = 256
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
        self.enterRule(localctx, 54, self.RULE_object_member_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


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
        self.enterRule(localctx, 56, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(YiniParser.OB)
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 261
                        self.multiline_trivia() 
                    self.state = 266
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21004032) != 0):
                    self.state = 267
                    self.elements()


                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                    self.state = 270
                    self.multiline_trivia()
                    self.state = 275
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 276
                self.match(YiniParser.CB)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(YiniParser.EMPTY_LIST)
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = YiniParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.value()
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 284
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                        self.state = 281
                        self.multiline_trivia()
                        self.state = 286
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 287
                    self.match(YiniParser.COMMA)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                        self.state = 288
                        self.multiline_trivia()
                        self.state = 293
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 294
                    self.value() 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0):
                    self.state = 300
                    self.multiline_trivia()
                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 306
                self.match(YiniParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiline_triviaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(YiniParser.NL, 0)

        def DISABLED_LINE(self):
            return self.getToken(YiniParser.DISABLED_LINE, 0)

        def FULL_LINE_COMMENT(self):
            return self.getToken(YiniParser.FULL_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_multiline_trivia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiline_trivia" ):
                return visitor.visitMultiline_trivia(self)
            else:
                return visitor.visitChildren(self)




    def multiline_trivia(self):

        localctx = YiniParser.Multiline_triviaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_multiline_trivia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 53687091200) != 0)):
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
        self.enterRule(localctx, 62, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self.enterRule(localctx, 64, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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
        self.enterRule(localctx, 66, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
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
        self.enterRule(localctx, 68, self.RULE_bad_meta_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
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
        self.enterRule(localctx, 70, self.RULE_bad_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 319
                self.match(YiniParser.REST)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 22, 24]:
                self.state = 320
                self.value()
                pass
            elif token in [19]:
                pass
            else:
                pass
            self.state = 323
            self.match(YiniParser.EQ)
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 14, 22, 24]:
                self.state = 324
                self.value()
                pass
            elif token in [39]:
                self.state = 325
                self.match(YiniParser.REST)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 328
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





