# Generated from ./par.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .par import par
else:
    from par import par

# This class defines a complete generic visitor for a parse tree produced by par.

class parVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by par#program.
    def visitProgram(self, ctx:par.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#function.
    def visitFunction(self, ctx:par.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#head.
    def visitHead(self, ctx:par.HeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#function_name.
    def visitFunction_name(self, ctx:par.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#type_parameters.
    def visitType_parameters(self, ctx:par.Type_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#type_params.
    def visitType_params(self, ctx:par.Type_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#arguments.
    def visitArguments(self, ctx:par.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#args.
    def visitArgs(self, ctx:par.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#body.
    def visitBody(self, ctx:par.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#statement.
    def visitStatement(self, ctx:par.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#return_s.
    def visitReturn_s(self, ctx:par.Return_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#assign_s.
    def visitAssign_s(self, ctx:par.Assign_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#init_s.
    def visitInit_s(self, ctx:par.Init_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#if_s.
    def visitIf_s(self, ctx:par.If_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#for_s.
    def visitFor_s(self, ctx:par.For_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#while_s.
    def visitWhile_s(self, ctx:par.While_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#function_call_s.
    def visitFunction_call_s(self, ctx:par.Function_call_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#function_call_args.
    def visitFunction_call_args(self, ctx:par.Function_call_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#arithmetic_s.
    def visitArithmetic_s(self, ctx:par.Arithmetic_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#arithmetic_expr.
    def visitArithmetic_expr(self, ctx:par.Arithmetic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#init_assign_s.
    def visitInit_assign_s(self, ctx:par.Init_assign_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#type.
    def visitType(self, ctx:par.TypeContext):
        return self.visitChildren(ctx)



del par