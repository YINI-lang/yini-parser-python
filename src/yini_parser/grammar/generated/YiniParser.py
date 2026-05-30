# Generated from ./grammar/v1.0.0-rc.6/YiniParser.g4 by ANTLR 4.13.2
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
        4,1,40,324,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        3,0,68,8,0,1,0,5,0,71,8,0,10,0,12,0,74,9,0,1,0,3,0,77,8,0,1,0,1,
        0,1,1,1,1,5,1,83,8,1,10,1,12,1,86,9,1,1,1,4,1,89,8,1,11,1,12,1,90,
        3,1,93,8,1,1,2,1,2,5,2,97,8,2,10,2,12,2,100,9,2,1,3,1,3,3,3,104,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,114,8,4,1,5,1,5,3,5,118,
        8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,129,8,8,1,9,1,9,1,9,
        3,9,134,8,9,1,9,3,9,137,8,9,1,10,1,10,3,10,141,8,10,1,10,1,10,1,
        11,1,11,1,12,1,12,1,12,1,13,4,13,151,8,13,11,13,12,13,152,1,14,1,
        14,1,14,1,15,1,15,1,15,3,15,161,8,15,1,16,1,16,1,16,1,16,3,16,167,
        8,16,1,17,1,17,1,17,1,17,3,17,173,8,17,1,18,1,18,4,18,177,8,18,11,
        18,12,18,178,1,19,1,19,5,19,183,8,19,10,19,12,19,186,9,19,1,19,1,
        19,1,20,1,20,1,21,1,21,1,22,1,22,5,22,196,8,22,10,22,12,22,199,9,
        22,1,22,3,22,202,8,22,1,22,5,22,205,8,22,10,22,12,22,208,9,22,1,
        22,1,22,5,22,212,8,22,10,22,12,22,215,9,22,1,22,1,22,5,22,219,8,
        22,10,22,12,22,222,9,22,3,22,224,8,22,1,23,1,23,1,23,5,23,229,8,
        23,10,23,12,23,232,9,23,1,23,5,23,235,8,23,10,23,12,23,238,9,23,
        1,23,3,23,241,8,23,1,24,1,24,1,24,1,24,1,25,1,25,1,26,1,26,5,26,
        251,8,26,10,26,12,26,254,9,26,1,26,3,26,257,8,26,1,26,5,26,260,8,
        26,10,26,12,26,263,9,26,1,26,1,26,5,26,267,8,26,10,26,12,26,270,
        9,26,1,26,1,26,5,26,274,8,26,10,26,12,26,277,9,26,3,26,279,8,26,
        1,27,1,27,5,27,283,8,27,10,27,12,27,286,9,27,1,27,1,27,5,27,290,
        8,27,10,27,12,27,293,9,27,1,27,5,27,296,8,27,10,27,12,27,299,9,27,
        1,27,3,27,302,8,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,
        1,32,3,32,314,8,32,1,32,1,32,1,32,3,32,319,8,32,1,32,3,32,322,8,
        32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,3,2,0,8,10,13,14,
        2,0,19,19,21,21,1,0,8,9,344,0,67,1,0,0,0,2,92,1,0,0,0,4,94,1,0,0,
        0,6,103,1,0,0,0,8,113,1,0,0,0,10,115,1,0,0,0,12,119,1,0,0,0,14,121,
        1,0,0,0,16,128,1,0,0,0,18,136,1,0,0,0,20,138,1,0,0,0,22,144,1,0,
        0,0,24,146,1,0,0,0,26,150,1,0,0,0,28,154,1,0,0,0,30,157,1,0,0,0,
        32,166,1,0,0,0,34,172,1,0,0,0,36,174,1,0,0,0,38,180,1,0,0,0,40,189,
        1,0,0,0,42,191,1,0,0,0,44,223,1,0,0,0,46,225,1,0,0,0,48,242,1,0,
        0,0,50,246,1,0,0,0,52,278,1,0,0,0,54,280,1,0,0,0,56,303,1,0,0,0,
        58,305,1,0,0,0,60,307,1,0,0,0,62,309,1,0,0,0,64,313,1,0,0,0,66,68,
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
        26,13,0,117,116,1,0,0,0,117,118,1,0,0,0,118,11,1,0,0,0,119,120,5,
        34,0,0,120,13,1,0,0,0,121,122,5,7,0,0,122,15,1,0,0,0,123,129,3,18,
        9,0,124,129,3,24,12,0,125,126,3,62,31,0,126,127,3,26,13,0,127,129,
        1,0,0,0,128,123,1,0,0,0,128,124,1,0,0,0,128,125,1,0,0,0,129,17,1,
        0,0,0,130,137,3,20,10,0,131,133,5,3,0,0,132,134,3,42,21,0,133,132,
        1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,137,3,26,13,0,136,130,
        1,0,0,0,136,131,1,0,0,0,137,19,1,0,0,0,138,140,5,2,0,0,139,141,3,
        22,11,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,143,
        3,26,13,0,143,21,1,0,0,0,144,145,5,37,0,0,145,23,1,0,0,0,146,147,
        5,4,0,0,147,148,3,26,13,0,148,25,1,0,0,0,149,151,5,31,0,0,150,149,
        1,0,0,0,151,152,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,27,1,
        0,0,0,154,155,3,30,15,0,155,156,3,26,13,0,156,29,1,0,0,0,157,158,
        5,37,0,0,158,160,5,19,0,0,159,161,3,32,16,0,160,159,1,0,0,0,160,
        161,1,0,0,0,161,31,1,0,0,0,162,167,3,36,18,0,163,167,3,34,17,0,164,
        167,3,52,26,0,165,167,3,44,22,0,166,162,1,0,0,0,166,163,1,0,0,0,
        166,164,1,0,0,0,166,165,1,0,0,0,167,33,1,0,0,0,168,173,3,58,29,0,
        169,173,3,42,21,0,170,173,3,56,28,0,171,173,3,60,30,0,172,168,1,
        0,0,0,172,169,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,35,1,0,
        0,0,174,176,5,13,0,0,175,177,3,38,19,0,176,175,1,0,0,0,177,178,1,
        0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,37,1,0,0,0,180,184,5,26,
        0,0,181,183,5,31,0,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,
        0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,188,3,40,
        20,0,188,39,1,0,0,0,189,190,7,0,0,0,190,41,1,0,0,0,191,192,5,13,
        0,0,192,43,1,0,0,0,193,197,5,24,0,0,194,196,5,31,0,0,195,194,1,0,
        0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,201,1,0,
        0,0,199,197,1,0,0,0,200,202,3,46,23,0,201,200,1,0,0,0,201,202,1,
        0,0,0,202,206,1,0,0,0,203,205,5,31,0,0,204,203,1,0,0,0,205,208,1,
        0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,206,1,
        0,0,0,209,213,5,25,0,0,210,212,5,31,0,0,211,210,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,224,1,0,0,0,215,213,
        1,0,0,0,216,220,5,11,0,0,217,219,5,31,0,0,218,217,1,0,0,0,219,222,
        1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,224,1,0,0,0,222,220,
        1,0,0,0,223,193,1,0,0,0,223,216,1,0,0,0,224,45,1,0,0,0,225,236,3,
        48,24,0,226,230,5,20,0,0,227,229,5,31,0,0,228,227,1,0,0,0,229,232,
        1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,233,1,0,0,0,232,230,
        1,0,0,0,233,235,3,48,24,0,234,226,1,0,0,0,235,238,1,0,0,0,236,234,
        1,0,0,0,236,237,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,239,241,
        5,20,0,0,240,239,1,0,0,0,240,241,1,0,0,0,241,47,1,0,0,0,242,243,
        5,37,0,0,243,244,3,50,25,0,244,245,3,32,16,0,245,49,1,0,0,0,246,
        247,7,1,0,0,247,51,1,0,0,0,248,252,5,22,0,0,249,251,5,31,0,0,250,
        249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,
        256,1,0,0,0,254,252,1,0,0,0,255,257,3,54,27,0,256,255,1,0,0,0,256,
        257,1,0,0,0,257,261,1,0,0,0,258,260,5,31,0,0,259,258,1,0,0,0,260,
        263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,264,1,0,0,0,263,
        261,1,0,0,0,264,268,5,23,0,0,265,267,5,31,0,0,266,265,1,0,0,0,267,
        270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,279,1,0,0,0,270,
        268,1,0,0,0,271,275,5,12,0,0,272,274,5,31,0,0,273,272,1,0,0,0,274,
        277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,279,1,0,0,0,277,
        275,1,0,0,0,278,248,1,0,0,0,278,271,1,0,0,0,279,53,1,0,0,0,280,297,
        3,32,16,0,281,283,5,31,0,0,282,281,1,0,0,0,283,286,1,0,0,0,284,282,
        1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,284,1,0,0,0,287,291,
        5,20,0,0,288,290,5,31,0,0,289,288,1,0,0,0,290,293,1,0,0,0,291,289,
        1,0,0,0,291,292,1,0,0,0,292,294,1,0,0,0,293,291,1,0,0,0,294,296,
        3,32,16,0,295,284,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,
        1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,300,302,5,20,0,0,301,300,
        1,0,0,0,301,302,1,0,0,0,302,55,1,0,0,0,303,304,5,14,0,0,304,57,1,
        0,0,0,305,306,5,10,0,0,306,59,1,0,0,0,307,308,7,2,0,0,308,61,1,0,
        0,0,309,310,5,40,0,0,310,63,1,0,0,0,311,314,5,39,0,0,312,314,3,32,
        16,0,313,311,1,0,0,0,313,312,1,0,0,0,313,314,1,0,0,0,314,315,1,0,
        0,0,315,318,5,19,0,0,316,319,3,32,16,0,317,319,5,39,0,0,318,316,
        1,0,0,0,318,317,1,0,0,0,319,321,1,0,0,0,320,322,3,26,13,0,321,320,
        1,0,0,0,321,322,1,0,0,0,322,65,1,0,0,0,42,67,72,76,84,90,92,98,103,
        113,117,128,133,136,140,152,160,166,172,178,184,197,201,206,213,
        220,223,230,236,240,252,256,261,268,275,278,284,291,297,301,313,
        318,321
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
            self.state = 121
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
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.directive()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.annotation()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.bad_meta_text()
                self.state = 126
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
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.yini_directive()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(YiniParser.INCLUDE_TOKEN)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 132
                    self.string_literal()


                self.state = 135
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
            self.state = 138
            self.match(YiniParser.YINI_TOKEN)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 139
                self.yini_mode_declaration()


            self.state = 142
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
            self.state = 144
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
            self.state = 146
            self.match(YiniParser.DEPRECATED_TOKEN)
            self.state = 147
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
            self.state = 150 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 149
                    self.match(YiniParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 152 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 154
            self.member()
            self.state = 155
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
            self.state = 157
            self.match(YiniParser.KEY)
            self.state = 158
            self.match(YiniParser.EQ)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21004032) != 0):
                self.state = 159
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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.concat_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.scalar_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.list_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.null_literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.string_literal()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.number_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
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
            self.state = 174
            self.match(YiniParser.STRING)
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 175
                self.concat_tail()
                self.state = 178 
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
            self.state = 180
            self.match(YiniParser.PLUS)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 181
                self.match(YiniParser.NL)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
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
            self.state = 189
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
            self.state = 191
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
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(YiniParser.OC)
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 194
                        self.match(YiniParser.NL) 
                    self.state = 199
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 200
                    self.object_members()


                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 203
                    self.match(YiniParser.NL)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 209
                self.match(YiniParser.CC)
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 210
                        self.match(YiniParser.NL) 
                    self.state = 215
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(YiniParser.EMPTY_OBJECT)
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 217
                        self.match(YiniParser.NL) 
                    self.state = 222
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.state = 225
            self.object_member()
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 226
                    self.match(YiniParser.COMMA)
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 227
                        self.match(YiniParser.NL)
                        self.state = 232
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 233
                    self.object_member() 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 239
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
            self.state = 242
            self.match(YiniParser.KEY)
            self.state = 243
            self.object_member_separator()
            self.state = 244
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
            self.state = 246
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
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(YiniParser.OB)
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 249
                        self.match(YiniParser.NL) 
                    self.state = 254
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21004032) != 0):
                    self.state = 255
                    self.elements()


                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 258
                    self.match(YiniParser.NL)
                    self.state = 263
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 264
                self.match(YiniParser.CB)
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 265
                        self.match(YiniParser.NL) 
                    self.state = 270
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(YiniParser.EMPTY_LIST)
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 272
                        self.match(YiniParser.NL) 
                    self.state = 277
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 280
            self.value()
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 284
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 281
                        self.match(YiniParser.NL)
                        self.state = 286
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 287
                    self.match(YiniParser.COMMA)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==31:
                        self.state = 288
                        self.match(YiniParser.NL)
                        self.state = 293
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 294
                    self.value() 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 300
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
            self.state = 303
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
            self.state = 305
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
            self.state = 307
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
            self.state = 309
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
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 311
                self.match(YiniParser.REST)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 22, 24]:
                self.state = 312
                self.value()
                pass
            elif token in [19]:
                pass
            else:
                pass
            self.state = 315
            self.match(YiniParser.EQ)
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 14, 22, 24]:
                self.state = 316
                self.value()
                pass
            elif token in [39]:
                self.state = 317
                self.match(YiniParser.REST)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 320
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





