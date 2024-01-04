# Generated from grammar/par.g4 by ANTLR 4.13.1
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
        4,1,13,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,4,1,34,8,1,11,1,12,1,35,1,1,1,1,1,2,1,2,
        1,2,3,2,43,8,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,3,4,58,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,68,8,5,1,6,1,6,
        1,6,3,6,73,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,11,12,
        85,0,25,1,0,0,0,2,30,1,0,0,0,4,39,1,0,0,0,6,48,1,0,0,0,8,57,1,0,
        0,0,10,67,1,0,0,0,12,72,1,0,0,0,14,74,1,0,0,0,16,78,1,0,0,0,18,83,
        1,0,0,0,20,87,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,
        0,0,1,29,1,1,0,0,0,30,31,3,4,2,0,31,33,5,7,0,0,32,34,3,12,6,0,33,
        32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,
        0,37,38,5,8,0,0,38,3,1,0,0,0,39,40,3,20,10,0,40,42,5,11,0,0,41,43,
        3,6,3,0,42,41,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,3,0,0,
        45,46,3,10,5,0,46,47,5,4,0,0,47,5,1,0,0,0,48,49,5,5,0,0,49,50,3,
        8,4,0,50,51,5,6,0,0,51,7,1,0,0,0,52,58,3,20,10,0,53,54,3,20,10,0,
        54,55,5,9,0,0,55,56,3,8,4,0,56,58,1,0,0,0,57,52,1,0,0,0,57,53,1,
        0,0,0,58,9,1,0,0,0,59,60,3,20,10,0,60,61,5,11,0,0,61,68,1,0,0,0,
        62,63,3,20,10,0,63,64,5,11,0,0,64,65,5,9,0,0,65,66,3,10,5,0,66,68,
        1,0,0,0,67,59,1,0,0,0,67,62,1,0,0,0,68,11,1,0,0,0,69,73,3,14,7,0,
        70,73,3,16,8,0,71,73,3,18,9,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,
        1,0,0,0,73,13,1,0,0,0,74,75,5,1,0,0,75,76,5,11,0,0,76,77,5,2,0,0,
        77,15,1,0,0,0,78,79,5,11,0,0,79,80,5,10,0,0,80,81,5,11,0,0,81,82,
        5,2,0,0,82,17,1,0,0,0,83,84,3,20,10,0,84,85,5,11,0,0,85,86,5,2,0,
        0,86,19,1,0,0,0,87,88,7,0,0,0,88,21,1,0,0,0,6,25,35,42,57,67,72
    ]

class par ( Parser ):

    grammarFileName = "par.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "';'", "'('", "')'", "'<'", 
                     "'>'", "'{'", "'}'", "','", "'='" ]

    symbolicNames = [ "<INVALID>", "RETURN", "SEMICOLON", "BRACKET_OR", 
                      "BRACKET_CR", "BRACKET_OS", "BRACKET_CS", "BRACKET_OW", 
                      "BRACKET_CW", "COMMA", "EQUAL", "IDENTIFIER", "TYPE_IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_head = 2
    RULE_type_parameters = 3
    RULE_type_params = 4
    RULE_args = 5
    RULE_statement = 6
    RULE_return_s = 7
    RULE_assign_s = 8
    RULE_init_s = 9
    RULE_type = 10

    ruleNames =  [ "program", "function", "head", "type_parameters", "type_params", 
                   "args", "statement", "return_s", "assign_s", "init_s", 
                   "type" ]

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
    IDENTIFIER=11
    TYPE_IDENTIFIER=12
    WS=13

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




    def program(self):

        localctx = par.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 22
                self.function()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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
            return par.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = par.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.head()
            self.state = 31
            self.match(par.BRACKET_OW)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6146) != 0)):
                    break

            self.state = 37
            self.match(par.BRACKET_CW)
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


        def IDENTIFIER(self):
            return self.getToken(par.IDENTIFIER, 0)

        def BRACKET_OR(self):
            return self.getToken(par.BRACKET_OR, 0)

        def args(self):
            return self.getTypedRuleContext(par.ArgsContext,0)


        def BRACKET_CR(self):
            return self.getToken(par.BRACKET_CR, 0)

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




    def head(self):

        localctx = par.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.type_()
            self.state = 40
            self.match(par.IDENTIFIER)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 41
                self.type_parameters()


            self.state = 44
            self.match(par.BRACKET_OR)
            self.state = 45
            self.args()
            self.state = 46
            self.match(par.BRACKET_CR)
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




    def type_parameters(self):

        localctx = par.Type_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(par.BRACKET_OS)
            self.state = 49
            self.type_params()
            self.state = 50
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




    def type_params(self):

        localctx = par.Type_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_params)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.type_()
                self.state = 54
                self.match(par.COMMA)
                self.state = 55
                self.type_params()
                pass


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


        def IDENTIFIER(self):
            return self.getToken(par.IDENTIFIER, 0)

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




    def args(self):

        localctx = par.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_args)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.type_()
                self.state = 60
                self.match(par.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.type_()
                self.state = 63
                self.match(par.IDENTIFIER)
                self.state = 64
                self.match(par.COMMA)
                self.state = 65
                self.args()
                pass


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


        def assign_s(self):
            return self.getTypedRuleContext(par.Assign_sContext,0)


        def init_s(self):
            return self.getTypedRuleContext(par.Init_sContext,0)


        def getRuleIndex(self):
            return par.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = par.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.return_s()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.assign_s()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.init_s()
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

        def IDENTIFIER(self):
            return self.getToken(par.IDENTIFIER, 0)

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




    def return_s(self):

        localctx = par.Return_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_return_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(par.RETURN)
            self.state = 75
            self.match(par.IDENTIFIER)
            self.state = 76
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(par.IDENTIFIER)
            else:
                return self.getToken(par.IDENTIFIER, i)

        def EQUAL(self):
            return self.getToken(par.EQUAL, 0)

        def SEMICOLON(self):
            return self.getToken(par.SEMICOLON, 0)

        def getRuleIndex(self):
            return par.RULE_assign_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_s" ):
                listener.enterAssign_s(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_s" ):
                listener.exitAssign_s(self)




    def assign_s(self):

        localctx = par.Assign_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(par.IDENTIFIER)
            self.state = 79
            self.match(par.EQUAL)
            self.state = 80
            self.match(par.IDENTIFIER)
            self.state = 81
            self.match(par.SEMICOLON)
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


        def IDENTIFIER(self):
            return self.getToken(par.IDENTIFIER, 0)

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




    def init_s(self):

        localctx = par.Init_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_init_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.type_()
            self.state = 84
            self.match(par.IDENTIFIER)
            self.state = 85
            self.match(par.SEMICOLON)
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

        def TYPE_IDENTIFIER(self):
            return self.getToken(par.TYPE_IDENTIFIER, 0)

        def IDENTIFIER(self):
            return self.getToken(par.IDENTIFIER, 0)

        def getRuleIndex(self):
            return par.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = par.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
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





