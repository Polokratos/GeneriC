from generated.parVisitor import parVisitor
from generated.lex import *
from generated.par import *
class GeneriCVisitor(parVisitor):
    
    def __init__(self, outputPath):
        file = open(outputPath,"w")
        self.write = lambda txt : file.write(txt + " ")
        self.end = file.close
        self.activeGenericTypes = []

    def replaceIfGeneric(self,val):
        if(val.replace("*","") in self.activeGenericTypes):
            return "void*"+("*"*val.count("*"))
        return val

    def writeGeneric(self,val):
        self.write(self.replaceIfGeneric(val))
    
    # Visit a parse tree produced by par#program.
    def visitProgram(self, ctx:par.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#function.
    def visitFunction(self, ctx:par.FunctionContext):
        self.write("\n")
        ctx.getChild(0).accept(self)
        ctx.getChild(1).accept(self)
        self.activeGenericTypes = [] # clean
        return


    # Visit a parse tree produced by par#head.
    def visitHead(self, ctx:par.HeadContext):
        addedTypes = []
        childCount = ctx.getChildCount()
        if(childCount == 4):
            addedTypes.extend(ctx.getChild(2).accept(self))
        self.activeGenericTypes = addedTypes
        return_type = ctx.getChild(0).getText()
        self.writeGeneric(return_type)
        ctx.getChild(1).accept(self)
        ctx.getChild(ctx.getChildCount()-1).accept(self)
        return


    # Visit a parse tree produced by par#function_name.
    def visitFunction_name(self, ctx:par.Function_nameContext):
        self.write(ctx.getText())
        return 


    # Visit a parse tree produced by par#type_parameters.
    def visitType_parameters(self, ctx:par.Type_parametersContext):
        typesList = ctx.getChild(1).accept(self)
        return typesList


    # Visit a parse tree produced by par#type_params.
    def visitType_params(self, ctx:par.Type_paramsContext):
        typesList = []
        typesList.append(ctx.getChild(0).getText())
        if(ctx.getChildCount() == 3):
            typesList.extend(ctx.getChild(2).accept(self))
        return typesList


    # Visit a parse tree produced by par#arguments.
    def visitArguments(self, ctx:par.ArgumentsContext):
        self.write("(")
        ctx.getChild(1).accept(self)
        self.write(")")
        return


    # Visit a parse tree produced by par#args.
    def visitArgs(self, ctx:par.ArgsContext):
        ctx.getChild(0).accept(self)
        self.write(ctx.getChild(1).getText())
        if(ctx.getChildCount() == 4):
            self.write(ctx.getChild(2).getText())
            ctx.getChild(3).accept(self)
        return


    # Visit a parse tree produced by par#body.
    def visitBody(self, ctx:par.BodyContext):
        self.write(ctx.getChild(0).getText())
        for i in range(1,ctx.getChildCount()-1):
            ctx.getChild(i).accept(self)
        self.write(ctx.getChild(ctx.getChildCount()-1).getText())
        return


    # Visit a parse tree produced by par#statement.
    def visitStatement(self, ctx:par.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by par#return_s.
    def visitReturn_s(self, ctx:par.Return_sContext):
        for child in ctx.getChildren():
            self.writeGeneric(child.getText())
        return 


    # Visit a parse tree produced by par#assign_s.
    def visitAssign_s(self, ctx:par.Assign_sContext):
        for child in ctx.getChildren():
            self.writeGeneric(child.getText())
        return


    # Visit a parse tree produced by par#init_s.
    def visitInit_s(self, ctx:par.Init_sContext):
        for child in ctx.getChildren():
            self.writeGeneric(child.getText())
        return


    # Visit a parse tree produced by par#if_s.
    def visitIf_s(self, ctx:par.If_sContext):
        self.write(ctx.getChild(0).getText())
        self.write(ctx.getChild(1).getText())
        ctx.getChild(2).accept(self)
        self.write(ctx.getChild(3).getText())
        ctx.getChild(4).accept(self)


    # Visit a parse tree produced by par#for_s.
    def visitFor_s(self, ctx:par.For_sContext):
        self.write(ctx.getChild(0).getText())
        self.write(ctx.getChild(1).getText())
        ctx.getChild(2).accept(self)
        ctx.getChild(3).accept(self)
        self.write(ctx.getChild(4).getText())
        self.write(ctx.getChild(5).getText())
        self.write(ctx.getChild(6).getText())
        self.write(ctx.getChild(7).getText())
        ctx.getChild(8).accept(self)


    # Visit a parse tree produced by par#while_s.
    def visitWhile_s(self, ctx:par.While_sContext):
        self.write(ctx.getChild(0).getText())
        self.write(ctx.getChild(1).getText())
        ctx.getChild(2).accept(self)
        self.write(ctx.getChild(3).getText())
        ctx.getChild(4).accept(self)
        return


    # Visit a parse tree produced by par#function_call_s.
    def visitFunction_call_s(self, ctx:par.Function_call_sContext):
        self.write(ctx.getChild(0).getText())
        l = ctx.getChildCount()
        self.write(ctx.getChild(l-4).getText())
        ctx.getChild(l-3).accept(self)
        self.write(ctx.getChild(l-2).getText())
        self.write(ctx.getChild(l-1).getText())
        return
    
    def visitFunction_call_args(self, ctx:par.Function_call_argsContext):
        self.write(ctx.getChild(0).getText())
        if(ctx.getChildCount() == 1): 
            return
        self.write(ctx.getChild(1).getText())
        ctx.getChild(2).accept(self)
        return


    # Visit a parse tree produced by par#arithmetic_s.
    def visitArithmetic_s(self, ctx:par.Arithmetic_sContext):
        for child in ctx.getChildren():
            self.writeGeneric(child.getText())
        return


    # Visit a parse tree produced by par#arithmetic_expr.
    def visitArithmetic_expr(self, ctx:par.Arithmetic_exprContext):
        for child in ctx.getChildren():
            self.writeGeneric(child.getText())
        return


    # Visit a parse tree produced by par#init_assign_s.
    def visitInit_assign_s(self, ctx:par.Init_assign_sContext):
        self.writeGeneric(ctx.getChild(0).getText())
        self.write(ctx.getChild(1).getText())
        self.write(ctx.getChild(2).getText())
        if(ctx.getChildCount() == 5):
            self.write(ctx.getChild(3).getText())
            self.write(ctx.getChild(4).getText())
        else:
            ctx.getChild(3).accept(self)
        return
        


    # Visit a parse tree produced by par#type.
    def visitType(self, ctx:par.TypeContext):
        self.writeGeneric(ctx.getText())