# Generated from ./par.g4 by ANTLR 4.13.1
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
        4,1,18,209,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,1,
        1,1,2,1,2,1,2,3,2,59,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,3,5,74,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,88,8,7,1,8,1,8,5,8,92,8,8,10,8,12,8,95,9,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,108,8,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,122,8,11,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        3,16,152,8,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,
        163,8,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,171,8,18,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,186,8,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,205,8,20,1,21,1,21,1,21,0,0,22,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,1,0,14,
        15,209,0,47,1,0,0,0,2,52,1,0,0,0,4,55,1,0,0,0,6,62,1,0,0,0,8,64,
        1,0,0,0,10,73,1,0,0,0,12,75,1,0,0,0,14,87,1,0,0,0,16,89,1,0,0,0,
        18,107,1,0,0,0,20,109,1,0,0,0,22,121,1,0,0,0,24,123,1,0,0,0,26,127,
        1,0,0,0,28,133,1,0,0,0,30,143,1,0,0,0,32,149,1,0,0,0,34,162,1,0,
        0,0,36,170,1,0,0,0,38,185,1,0,0,0,40,204,1,0,0,0,42,206,1,0,0,0,
        44,46,3,2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,
        0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,
        53,3,4,2,0,53,54,3,16,8,0,54,3,1,0,0,0,55,56,3,42,21,0,56,58,3,6,
        3,0,57,59,3,8,4,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,
        3,12,6,0,61,5,1,0,0,0,62,63,5,16,0,0,63,7,1,0,0,0,64,65,5,5,0,0,
        65,66,3,10,5,0,66,67,5,6,0,0,67,9,1,0,0,0,68,74,3,42,21,0,69,70,
        3,42,21,0,70,71,5,9,0,0,71,72,3,10,5,0,72,74,1,0,0,0,73,68,1,0,0,
        0,73,69,1,0,0,0,74,11,1,0,0,0,75,76,5,3,0,0,76,77,3,14,7,0,77,78,
        5,4,0,0,78,13,1,0,0,0,79,80,3,42,21,0,80,81,5,16,0,0,81,88,1,0,0,
        0,82,83,3,42,21,0,83,84,5,16,0,0,84,85,5,9,0,0,85,86,3,14,7,0,86,
        88,1,0,0,0,87,79,1,0,0,0,87,82,1,0,0,0,88,15,1,0,0,0,89,93,5,7,0,
        0,90,92,3,18,9,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,
        1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,8,0,0,97,17,1,0,0,0,
        98,108,3,20,10,0,99,108,3,40,20,0,100,108,3,22,11,0,101,108,3,24,
        12,0,102,108,3,26,13,0,103,108,3,28,14,0,104,108,3,30,15,0,105,108,
        3,32,16,0,106,108,3,36,18,0,107,98,1,0,0,0,107,99,1,0,0,0,107,100,
        1,0,0,0,107,101,1,0,0,0,107,102,1,0,0,0,107,103,1,0,0,0,107,104,
        1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,108,19,1,0,0,0,109,110,5,
        1,0,0,110,111,5,16,0,0,111,112,5,2,0,0,112,21,1,0,0,0,113,114,5,
        16,0,0,114,115,5,10,0,0,115,116,5,16,0,0,116,122,5,2,0,0,117,118,
        5,16,0,0,118,119,5,10,0,0,119,120,5,17,0,0,120,122,5,2,0,0,121,113,
        1,0,0,0,121,117,1,0,0,0,122,23,1,0,0,0,123,124,3,42,21,0,124,125,
        5,16,0,0,125,126,5,2,0,0,126,25,1,0,0,0,127,128,5,11,0,0,128,129,
        5,3,0,0,129,130,3,38,19,0,130,131,5,4,0,0,131,132,3,16,8,0,132,27,
        1,0,0,0,133,134,5,12,0,0,134,135,5,3,0,0,135,136,3,18,9,0,136,137,
        3,38,19,0,137,138,5,2,0,0,138,139,5,16,0,0,139,140,7,0,0,0,140,141,
        5,4,0,0,141,142,3,16,8,0,142,29,1,0,0,0,143,144,5,13,0,0,144,145,
        5,3,0,0,145,146,3,38,19,0,146,147,5,4,0,0,147,148,3,16,8,0,148,31,
        1,0,0,0,149,151,5,16,0,0,150,152,3,8,4,0,151,150,1,0,0,0,151,152,
        1,0,0,0,152,153,1,0,0,0,153,154,5,3,0,0,154,155,3,34,17,0,155,156,
        5,4,0,0,156,157,5,2,0,0,157,33,1,0,0,0,158,163,5,16,0,0,159,160,
        5,16,0,0,160,161,5,9,0,0,161,163,3,34,17,0,162,158,1,0,0,0,162,159,
        1,0,0,0,163,35,1,0,0,0,164,165,5,16,0,0,165,166,5,14,0,0,166,171,
        5,2,0,0,167,168,5,16,0,0,168,169,5,15,0,0,169,171,5,2,0,0,170,164,
        1,0,0,0,170,167,1,0,0,0,171,37,1,0,0,0,172,186,5,16,0,0,173,174,
        5,16,0,0,174,175,5,6,0,0,175,186,5,16,0,0,176,177,5,16,0,0,177,178,
        5,5,0,0,178,186,5,16,0,0,179,180,5,16,0,0,180,181,5,6,0,0,181,186,
        5,17,0,0,182,183,5,16,0,0,183,184,5,5,0,0,184,186,5,17,0,0,185,172,
        1,0,0,0,185,173,1,0,0,0,185,176,1,0,0,0,185,179,1,0,0,0,185,182,
        1,0,0,0,186,39,1,0,0,0,187,188,3,42,21,0,188,189,5,16,0,0,189,190,
        5,10,0,0,190,191,5,16,0,0,191,192,5,2,0,0,192,205,1,0,0,0,193,194,
        3,42,21,0,194,195,5,16,0,0,195,196,5,10,0,0,196,197,5,17,0,0,197,
        198,5,2,0,0,198,205,1,0,0,0,199,200,3,42,21,0,200,201,5,16,0,0,201,
        202,5,10,0,0,202,203,3,32,16,0,203,205,1,0,0,0,204,187,1,0,0,0,204,
        193,1,0,0,0,204,199,1,0,0,0,205,41,1,0,0,0,206,207,5,16,0,0,207,
        43,1,0,0,0,12,47,58,73,87,93,107,121,151,162,170,185,204
    ]

class par ( Parser ):

    grammarFileName = "par.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "';'", "'('", "')'", "'<'", 
                     "'>'", "'{'", "'}'", "','", "'='", "'if'", "'for'", 
                     "'while'", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "RETURN", "SEMICOLON", "BRACKET_OR", 
                      "BRACKET_CR", "BRACKET_OS", "BRACKET_CS", "BRACKET_OW", 
                      "BRACKET_CW", "COMMA", "EQUAL", "IF", "FOR", "WHILE", 
                      "INCREMENT", "DECREMENT", "LVALUE", "CONSTANT", "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_head = 2
    RULE_function_name = 3
    RULE_type_parameters = 4
    RULE_type_params = 5
    RULE_arguments = 6
    RULE_args = 7
    RULE_body = 8
    RULE_statement = 9
    RULE_return_s = 10
    RULE_assign_s = 11
    RULE_init_s = 12
    RULE_if_s = 13
    RULE_for_s = 14
    RULE_while_s = 15
    RULE_function_call_s = 16
    RULE_function_call_args = 17
    RULE_arithmetic_s = 18
    RULE_arithmetic_expr = 19
    RULE_init_assign_s = 20
    RULE_type = 21

    ruleNames =  [ "program", "function", "head", "function_name", "type_parameters", 
                   "type_params", "arguments", "args", "body", "statement", 
                   "return_s", "assign_s", "init_s", "if_s", "for_s", "while_s", 
                   "function_call_s", "function_call_args", "arithmetic_s", 
                   "arithmetic_expr", "init_assign_s", "type" ]

    EOF = Token.EOF
    RETURN=1
    SEMICOLON=2
    BRACKET_OR=3
    BRACKET_CR=4
    BRACKET_OS=5
    BRACKET_CS=6
    BRACKET_OW=7
    BRACKET_CW=8
    COMMA=9
    EQUAL=10
    IF=11
    FOR=12
    WHILE=13
    INCREMENT=14
    DECREMENT=15
    LVALUE=16
    CONSTANT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(par.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(par.FunctionContext)
            else:
                return self.getTypedRuleContext(par.FunctionContext,i)


        def getRuleIndex(self):
            return par.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = par.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 44
                self.function()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(par.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(par.HeadContext,0)


        def body(self):
            return self.getTypedRuleContext(par.BodyContext,0)


        def getRuleIndex(self):
            return par.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = par.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.head()
            self.state = 53
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(par.TypeContext,0)


        def function_name(self):
            return self.getTypedRuleContext(par.Function_nameContext,0)


        def arguments(self):
            return self.getTypedRuleContext(par.ArgumentsContext,0)


        def type_parameters(self):
            return self.getTypedRuleContext(par.Type_parametersContext,0)


        def getRuleIndex(self):
            return par.RULE_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHead" ):
                return visitor.visitHead(self)
            else:
                return visitor.visitChildren(self)




    def head(self):

        localctx = par.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.type_()
            self.state = 56
            self.function_name()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 57
                self.type_parameters()


            self.state = 60
            self.arguments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def getRuleIndex(self):
            return par.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_name" ):
                return visitor.visitFunction_name(self)
            else:
                return visitor.visitChildren(self)




    def function_name(self):

        localctx = par.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(par.LVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_OS(self):
            return self.getToken(par.BRACKET_OS, 0)

        def type_params(self):
            return self.getTypedRuleContext(par.Type_paramsContext,0)


        def BRACKET_CS(self):
            return self.getToken(par.BRACKET_CS, 0)

        def getRuleIndex(self):
            return par.RULE_type_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_parameters" ):
                listener.enterType_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_parameters" ):
                listener.exitType_parameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_parameters" ):
                return visitor.visitType_parameters(self)
            else:
                return visitor.visitChildren(self)




    def type_parameters(self):

        localctx = par.Type_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(par.BRACKET_OS)
            self.state = 65
            self.type_params()
            self.state = 66
            self.match(par.BRACKET_CS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(par.TypeContext,0)


        def COMMA(self):
            return self.getToken(par.COMMA, 0)

        def type_params(self):
            return self.getTypedRuleContext(par.Type_paramsContext,0)


        def getRuleIndex(self):
            return par.RULE_type_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_params" ):
                listener.enterType_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_params" ):
                listener.exitType_params(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_params" ):
                return visitor.visitType_params(self)
            else:
                return visitor.visitChildren(self)




    def type_params(self):

        localctx = par.Type_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_params)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.type_()
                self.state = 70
                self.match(par.COMMA)
                self.state = 71
                self.type_params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_OR(self):
            return self.getToken(par.BRACKET_OR, 0)

        def args(self):
            return self.getTypedRuleContext(par.ArgsContext,0)


        def BRACKET_CR(self):
            return self.getToken(par.BRACKET_CR, 0)

        def getRuleIndex(self):
            return par.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = par.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(par.BRACKET_OR)
            self.state = 76
            self.args()
            self.state = 77
            self.match(par.BRACKET_CR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(par.TypeContext,0)


        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def COMMA(self):
            return self.getToken(par.COMMA, 0)

        def args(self):
            return self.getTypedRuleContext(par.ArgsContext,0)


        def getRuleIndex(self):
            return par.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = par.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.type_()
                self.state = 80
                self.match(par.LVALUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.type_()
                self.state = 83
                self.match(par.LVALUE)
                self.state = 84
                self.match(par.COMMA)
                self.state = 85
                self.args()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_OW(self):
            return self.getToken(par.BRACKET_OW, 0)

        def BRACKET_CW(self):
            return self.getToken(par.BRACKET_CW, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(par.StatementContext)
            else:
                return self.getTypedRuleContext(par.StatementContext,i)


        def getRuleIndex(self):
            return par.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = par.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(par.BRACKET_OW)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 79874) != 0):
                self.state = 90
                self.statement()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(par.BRACKET_CW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_s(self):
            return self.getTypedRuleContext(par.Return_sContext,0)


        def init_assign_s(self):
            return self.getTypedRuleContext(par.Init_assign_sContext,0)


        def assign_s(self):
            return self.getTypedRuleContext(par.Assign_sContext,0)


        def init_s(self):
            return self.getTypedRuleContext(par.Init_sContext,0)


        def if_s(self):
            return self.getTypedRuleContext(par.If_sContext,0)


        def for_s(self):
            return self.getTypedRuleContext(par.For_sContext,0)


        def while_s(self):
            return self.getTypedRuleContext(par.While_sContext,0)


        def function_call_s(self):
            return self.getTypedRuleContext(par.Function_call_sContext,0)


        def arithmetic_s(self):
            return self.getTypedRuleContext(par.Arithmetic_sContext,0)


        def getRuleIndex(self):
            return par.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = par.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.return_s()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.init_assign_s()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.assign_s()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.init_s()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.if_s()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.for_s()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                self.while_s()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 105
                self.function_call_s()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 106
                self.arithmetic_s()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(par.RETURN, 0)

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def getRuleIndex(self):
            return par.RULE_return_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_s" ):
                listener.enterReturn_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_s" ):
                listener.exitReturn_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_s" ):
                return visitor.visitReturn_s(self)
            else:
                return visitor.visitChildren(self)




    def return_s(self):

        localctx = par.Return_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(par.RETURN)
            self.state = 110
            self.match(par.LVALUE)
            self.state = 111
            self.match(par.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self, i:int=None):
            if i is None:
                return self.getTokens(par.LVALUE)
            else:
                return self.getToken(par.LVALUE, i)

        def EQUAL(self):
            return self.getToken(par.EQUAL, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def CONSTANT(self):
            return self.getToken(par.CONSTANT, 0)

        def getRuleIndex(self):
            return par.RULE_assign_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_s" ):
                listener.enterAssign_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_s" ):
                listener.exitAssign_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_s" ):
                return visitor.visitAssign_s(self)
            else:
                return visitor.visitChildren(self)




    def assign_s(self):

        localctx = par.Assign_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assign_s)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(par.LVALUE)
                self.state = 114
                self.match(par.EQUAL)
                self.state = 115
                self.match(par.LVALUE)
                self.state = 116
                self.match(par.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(par.LVALUE)
                self.state = 118
                self.match(par.EQUAL)
                self.state = 119
                self.match(par.CONSTANT)
                self.state = 120
                self.match(par.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(par.TypeContext,0)


        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def getRuleIndex(self):
            return par.RULE_init_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit_s" ):
                listener.enterInit_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit_s" ):
                listener.exitInit_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_s" ):
                return visitor.visitInit_s(self)
            else:
                return visitor.visitChildren(self)




    def init_s(self):

        localctx = par.Init_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_init_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.type_()
            self.state = 124
            self.match(par.LVALUE)
            self.state = 125
            self.match(par.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(par.IF, 0)

        def BRACKET_OR(self):
            return self.getToken(par.BRACKET_OR, 0)

        def arithmetic_expr(self):
            return self.getTypedRuleContext(par.Arithmetic_exprContext,0)


        def BRACKET_CR(self):
            return self.getToken(par.BRACKET_CR, 0)

        def body(self):
            return self.getTypedRuleContext(par.BodyContext,0)


        def getRuleIndex(self):
            return par.RULE_if_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_s" ):
                listener.enterIf_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_s" ):
                listener.exitIf_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_s" ):
                return visitor.visitIf_s(self)
            else:
                return visitor.visitChildren(self)




    def if_s(self):

        localctx = par.If_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(par.IF)
            self.state = 128
            self.match(par.BRACKET_OR)
            self.state = 129
            self.arithmetic_expr()
            self.state = 130
            self.match(par.BRACKET_CR)
            self.state = 131
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(par.FOR, 0)

        def BRACKET_OR(self):
            return self.getToken(par.BRACKET_OR, 0)

        def statement(self):
            return self.getTypedRuleContext(par.StatementContext,0)


        def arithmetic_expr(self):
            return self.getTypedRuleContext(par.Arithmetic_exprContext,0)


        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def BRACKET_CR(self):
            return self.getToken(par.BRACKET_CR, 0)

        def body(self):
            return self.getTypedRuleContext(par.BodyContext,0)


        def INCREMENT(self):
            return self.getToken(par.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(par.DECREMENT, 0)

        def getRuleIndex(self):
            return par.RULE_for_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_s" ):
                listener.enterFor_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_s" ):
                listener.exitFor_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_s" ):
                return visitor.visitFor_s(self)
            else:
                return visitor.visitChildren(self)




    def for_s(self):

        localctx = par.For_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(par.FOR)
            self.state = 134
            self.match(par.BRACKET_OR)
            self.state = 135
            self.statement()
            self.state = 136
            self.arithmetic_expr()
            self.state = 137
            self.match(par.SEMICOLON)
            self.state = 138
            self.match(par.LVALUE)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 140
            self.match(par.BRACKET_CR)
            self.state = 141
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(par.WHILE, 0)

        def BRACKET_OR(self):
            return self.getToken(par.BRACKET_OR, 0)

        def arithmetic_expr(self):
            return self.getTypedRuleContext(par.Arithmetic_exprContext,0)


        def BRACKET_CR(self):
            return self.getToken(par.BRACKET_CR, 0)

        def body(self):
            return self.getTypedRuleContext(par.BodyContext,0)


        def getRuleIndex(self):
            return par.RULE_while_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_s" ):
                listener.enterWhile_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_s" ):
                listener.exitWhile_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_s" ):
                return visitor.visitWhile_s(self)
            else:
                return visitor.visitChildren(self)




    def while_s(self):

        localctx = par.While_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(par.WHILE)
            self.state = 144
            self.match(par.BRACKET_OR)
            self.state = 145
            self.arithmetic_expr()
            self.state = 146
            self.match(par.BRACKET_CR)
            self.state = 147
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def BRACKET_OR(self):
            return self.getToken(par.BRACKET_OR, 0)

        def function_call_args(self):
            return self.getTypedRuleContext(par.Function_call_argsContext,0)


        def BRACKET_CR(self):
            return self.getToken(par.BRACKET_CR, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def type_parameters(self):
            return self.getTypedRuleContext(par.Type_parametersContext,0)


        def getRuleIndex(self):
            return par.RULE_function_call_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_s" ):
                listener.enterFunction_call_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_s" ):
                listener.exitFunction_call_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_s" ):
                return visitor.visitFunction_call_s(self)
            else:
                return visitor.visitChildren(self)




    def function_call_s(self):

        localctx = par.Function_call_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_call_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(par.LVALUE)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 150
                self.type_parameters()


            self.state = 153
            self.match(par.BRACKET_OR)
            self.state = 154
            self.function_call_args()
            self.state = 155
            self.match(par.BRACKET_CR)
            self.state = 156
            self.match(par.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def COMMA(self):
            return self.getToken(par.COMMA, 0)

        def function_call_args(self):
            return self.getTypedRuleContext(par.Function_call_argsContext,0)


        def getRuleIndex(self):
            return par.RULE_function_call_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_args" ):
                listener.enterFunction_call_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_args" ):
                listener.exitFunction_call_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_args" ):
                return visitor.visitFunction_call_args(self)
            else:
                return visitor.visitChildren(self)




    def function_call_args(self):

        localctx = par.Function_call_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_call_args)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(par.LVALUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(par.LVALUE)
                self.state = 160
                self.match(par.COMMA)
                self.state = 161
                self.function_call_args()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def INCREMENT(self):
            return self.getToken(par.INCREMENT, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def DECREMENT(self):
            return self.getToken(par.DECREMENT, 0)

        def getRuleIndex(self):
            return par.RULE_arithmetic_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_s" ):
                listener.enterArithmetic_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_s" ):
                listener.exitArithmetic_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_s" ):
                return visitor.visitArithmetic_s(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_s(self):

        localctx = par.Arithmetic_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arithmetic_s)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(par.LVALUE)
                self.state = 165
                self.match(par.INCREMENT)
                self.state = 166
                self.match(par.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(par.LVALUE)
                self.state = 168
                self.match(par.DECREMENT)
                self.state = 169
                self.match(par.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self, i:int=None):
            if i is None:
                return self.getTokens(par.LVALUE)
            else:
                return self.getToken(par.LVALUE, i)

        def BRACKET_CS(self):
            return self.getToken(par.BRACKET_CS, 0)

        def BRACKET_OS(self):
            return self.getToken(par.BRACKET_OS, 0)

        def CONSTANT(self):
            return self.getToken(par.CONSTANT, 0)

        def getRuleIndex(self):
            return par.RULE_arithmetic_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expr" ):
                listener.enterArithmetic_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expr" ):
                listener.exitArithmetic_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expr" ):
                return visitor.visitArithmetic_expr(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_expr(self):

        localctx = par.Arithmetic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arithmetic_expr)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(par.LVALUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(par.LVALUE)
                self.state = 174
                self.match(par.BRACKET_CS)
                self.state = 175
                self.match(par.LVALUE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(par.LVALUE)
                self.state = 177
                self.match(par.BRACKET_OS)
                self.state = 178
                self.match(par.LVALUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.match(par.LVALUE)
                self.state = 180
                self.match(par.BRACKET_CS)
                self.state = 181
                self.match(par.CONSTANT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(par.LVALUE)
                self.state = 183
                self.match(par.BRACKET_OS)
                self.state = 184
                self.match(par.CONSTANT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_assign_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(par.TypeContext,0)


        def LVALUE(self, i:int=None):
            if i is None:
                return self.getTokens(par.LVALUE)
            else:
                return self.getToken(par.LVALUE, i)

        def EQUAL(self):
            return self.getToken(par.EQUAL, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def CONSTANT(self):
            return self.getToken(par.CONSTANT, 0)

        def function_call_s(self):
            return self.getTypedRuleContext(par.Function_call_sContext,0)


        def getRuleIndex(self):
            return par.RULE_init_assign_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit_assign_s" ):
                listener.enterInit_assign_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit_assign_s" ):
                listener.exitInit_assign_s(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_assign_s" ):
                return visitor.visitInit_assign_s(self)
            else:
                return visitor.visitChildren(self)




    def init_assign_s(self):

        localctx = par.Init_assign_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_init_assign_s)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.type_()
                self.state = 188
                self.match(par.LVALUE)
                self.state = 189
                self.match(par.EQUAL)
                self.state = 190
                self.match(par.LVALUE)
                self.state = 191
                self.match(par.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.type_()
                self.state = 194
                self.match(par.LVALUE)
                self.state = 195
                self.match(par.EQUAL)
                self.state = 196
                self.match(par.CONSTANT)
                self.state = 197
                self.match(par.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.type_()
                self.state = 200
                self.match(par.LVALUE)
                self.state = 201
                self.match(par.EQUAL)
                self.state = 202
                self.function_call_s()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LVALUE(self):
            return self.getToken(par.LVALUE, 0)

        def getRuleIndex(self):
            return par.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = par.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(par.LVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





