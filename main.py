DEBUG_MODE = True
DEBUG_FLAG = DEBUG_MODE
from antlr4 import *

from GeneriCVisitor import GeneriCVisitor
from generated.lex import *
from generated.par import *
import subprocess
"""
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
        self.write(ctx.getChild(1).getText())
        for i in range(2,ctx.getChildCount()-1):
            ctx.getChild(i).accept(self)
        self.write(ctx.getChild(ctx.getChildCount()-1).getText())
        self.activeGenericTypes = [] # clean
        return


    # Visit a parse tree produced by par#head.
    def visitHead(self, ctx:par.HeadContext):
        addedTypes = []
        childCount = ctx.getChildCount()
        if(childCount == 6):
            addedTypes.extend(ctx.getChild(2).accept(self))
        self.activeGenericTypes = addedTypes
        return_type = ctx.getChild(0).getText()
        self.writeGeneric(return_type)
        self.write(ctx.getChild(1).getText())
        self.write(ctx.getChild(childCount-3).getText())
        ctx.getChild(childCount-2).accept(self)
        self.write(ctx.getChild(childCount-1).getText())

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


    # Visit a parse tree produced by par#args.
    def visitArgs(self, ctx:par.ArgsContext):
        ctx.getChild(0).accept(self)
        self.write(ctx.getChild(1).getText())
        if(ctx.getChildCount() == 4):
            self.write(ctx.getChild(2).getText())
            ctx.getChild(3).accept(self)
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


    # Visit a parse tree produced by par#type.
    def visitType(self, ctx:par.TypeContext):
        self.writeGeneric(ctx.getText())
        return 
"""
#inputPath = "./test/negative/wrongHelpers.<c>" if DEBUG_FLAG else input("Input path:")
#outputPath = "./test/negative/wrongHelpers.c"  if DEBUG_FLAG else  input("Output path:")

inputPath = "./test/advanced/helpers.<c>" if DEBUG_FLAG else input("Input path:")
outputPath = "./test/advanced/helpers.c"  if DEBUG_FLAG else  input("Output path:")

if DEBUG_FLAG: # remove file so that code generator does not double stuff
    subprocess.run(["rm",outputPath])
    pass

inputStream = InputStream(open(inputPath,"r").read())

lexer = lex(inputStream)
stream = CommonTokenStream(lexer)
parser = par(stream)

tree = parser.program()
visitor = GeneriCVisitor(outputPath)

FAIL_FLAG = False
try:
    visitor.visit(tree)
except:
    FAIL_FLAG = True
    
visitor.end()
if FAIL_FLAG:
    print("FAILED!")
    subprocess.run(["rm",outputPath])    
else:
    print("Done!")
