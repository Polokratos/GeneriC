# Generated from ./par.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .par import par
else:
    from par import par

# This class defines a complete listener for a parse tree produced by par.
class parListener(ParseTreeListener):

    # Enter a parse tree produced by par#program.
    def enterProgram(self, ctx:par.ProgramContext):
        pass

    # Exit a parse tree produced by par#program.
    def exitProgram(self, ctx:par.ProgramContext):
        pass


    # Enter a parse tree produced by par#function.
    def enterFunction(self, ctx:par.FunctionContext):
        pass

    # Exit a parse tree produced by par#function.
    def exitFunction(self, ctx:par.FunctionContext):
        pass


    # Enter a parse tree produced by par#head.
    def enterHead(self, ctx:par.HeadContext):
        pass

    # Exit a parse tree produced by par#head.
    def exitHead(self, ctx:par.HeadContext):
        pass


    # Enter a parse tree produced by par#function_name.
    def enterFunction_name(self, ctx:par.Function_nameContext):
        pass

    # Exit a parse tree produced by par#function_name.
    def exitFunction_name(self, ctx:par.Function_nameContext):
        pass


    # Enter a parse tree produced by par#type_parameters.
    def enterType_parameters(self, ctx:par.Type_parametersContext):
        pass

    # Exit a parse tree produced by par#type_parameters.
    def exitType_parameters(self, ctx:par.Type_parametersContext):
        pass


    # Enter a parse tree produced by par#type_params.
    def enterType_params(self, ctx:par.Type_paramsContext):
        pass

    # Exit a parse tree produced by par#type_params.
    def exitType_params(self, ctx:par.Type_paramsContext):
        pass


    # Enter a parse tree produced by par#arguments.
    def enterArguments(self, ctx:par.ArgumentsContext):
        pass

    # Exit a parse tree produced by par#arguments.
    def exitArguments(self, ctx:par.ArgumentsContext):
        pass


    # Enter a parse tree produced by par#args.
    def enterArgs(self, ctx:par.ArgsContext):
        pass

    # Exit a parse tree produced by par#args.
    def exitArgs(self, ctx:par.ArgsContext):
        pass


    # Enter a parse tree produced by par#body.
    def enterBody(self, ctx:par.BodyContext):
        pass

    # Exit a parse tree produced by par#body.
    def exitBody(self, ctx:par.BodyContext):
        pass


    # Enter a parse tree produced by par#statement.
    def enterStatement(self, ctx:par.StatementContext):
        pass

    # Exit a parse tree produced by par#statement.
    def exitStatement(self, ctx:par.StatementContext):
        pass


    # Enter a parse tree produced by par#return_s.
    def enterReturn_s(self, ctx:par.Return_sContext):
        pass

    # Exit a parse tree produced by par#return_s.
    def exitReturn_s(self, ctx:par.Return_sContext):
        pass


    # Enter a parse tree produced by par#assign_s.
    def enterAssign_s(self, ctx:par.Assign_sContext):
        pass

    # Exit a parse tree produced by par#assign_s.
    def exitAssign_s(self, ctx:par.Assign_sContext):
        pass


    # Enter a parse tree produced by par#init_s.
    def enterInit_s(self, ctx:par.Init_sContext):
        pass

    # Exit a parse tree produced by par#init_s.
    def exitInit_s(self, ctx:par.Init_sContext):
        pass


    # Enter a parse tree produced by par#if_s.
    def enterIf_s(self, ctx:par.If_sContext):
        pass

    # Exit a parse tree produced by par#if_s.
    def exitIf_s(self, ctx:par.If_sContext):
        pass


    # Enter a parse tree produced by par#for_s.
    def enterFor_s(self, ctx:par.For_sContext):
        pass

    # Exit a parse tree produced by par#for_s.
    def exitFor_s(self, ctx:par.For_sContext):
        pass


    # Enter a parse tree produced by par#while_s.
    def enterWhile_s(self, ctx:par.While_sContext):
        pass

    # Exit a parse tree produced by par#while_s.
    def exitWhile_s(self, ctx:par.While_sContext):
        pass


    # Enter a parse tree produced by par#function_call_s.
    def enterFunction_call_s(self, ctx:par.Function_call_sContext):
        pass

    # Exit a parse tree produced by par#function_call_s.
    def exitFunction_call_s(self, ctx:par.Function_call_sContext):
        pass


    # Enter a parse tree produced by par#function_call_args.
    def enterFunction_call_args(self, ctx:par.Function_call_argsContext):
        pass

    # Exit a parse tree produced by par#function_call_args.
    def exitFunction_call_args(self, ctx:par.Function_call_argsContext):
        pass


    # Enter a parse tree produced by par#arithmetic_s.
    def enterArithmetic_s(self, ctx:par.Arithmetic_sContext):
        pass

    # Exit a parse tree produced by par#arithmetic_s.
    def exitArithmetic_s(self, ctx:par.Arithmetic_sContext):
        pass


    # Enter a parse tree produced by par#arithmetic_expr.
    def enterArithmetic_expr(self, ctx:par.Arithmetic_exprContext):
        pass

    # Exit a parse tree produced by par#arithmetic_expr.
    def exitArithmetic_expr(self, ctx:par.Arithmetic_exprContext):
        pass


    # Enter a parse tree produced by par#init_assign_s.
    def enterInit_assign_s(self, ctx:par.Init_assign_sContext):
        pass

    # Exit a parse tree produced by par#init_assign_s.
    def exitInit_assign_s(self, ctx:par.Init_assign_sContext):
        pass


    # Enter a parse tree produced by par#type.
    def enterType(self, ctx:par.TypeContext):
        pass

    # Exit a parse tree produced by par#type.
    def exitType(self, ctx:par.TypeContext):
        pass



del par