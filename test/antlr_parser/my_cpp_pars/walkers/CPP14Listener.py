# Generated from CPP14.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CPP14Parser import CPP14Parser
else:
    from CPP14Parser import CPP14Parser

# This class defines a complete listener for a parse tree produced by CPP14Parser.
class CPP14Listener(ParseTreeListener):

    # Enter a parse tree produced by CPP14Parser#program.
    def enterProgram(self, ctx:CPP14Parser.ProgramContext):
        pass

    # Exit a parse tree produced by CPP14Parser#program.
    def exitProgram(self, ctx:CPP14Parser.ProgramContext):
        pass


    # Enter a parse tree produced by CPP14Parser#openGuardian.
    def enterOpenGuardian(self, ctx:CPP14Parser.OpenGuardianContext):
        pass

    # Exit a parse tree produced by CPP14Parser#openGuardian.
    def exitOpenGuardian(self, ctx:CPP14Parser.OpenGuardianContext):
        pass


    # Enter a parse tree produced by CPP14Parser#closeGuardian.
    def enterCloseGuardian(self, ctx:CPP14Parser.CloseGuardianContext):
        pass

    # Exit a parse tree produced by CPP14Parser#closeGuardian.
    def exitCloseGuardian(self, ctx:CPP14Parser.CloseGuardianContext):
        pass


    # Enter a parse tree produced by CPP14Parser#programContent.
    def enterProgramContent(self, ctx:CPP14Parser.ProgramContentContext):
        pass

    # Exit a parse tree produced by CPP14Parser#programContent.
    def exitProgramContent(self, ctx:CPP14Parser.ProgramContentContext):
        pass


    # Enter a parse tree produced by CPP14Parser#includeStatement.
    def enterIncludeStatement(self, ctx:CPP14Parser.IncludeStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#includeStatement.
    def exitIncludeStatement(self, ctx:CPP14Parser.IncludeStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classDefinition.
    def enterClassDefinition(self, ctx:CPP14Parser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classDefinition.
    def exitClassDefinition(self, ctx:CPP14Parser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#className.
    def enterClassName(self, ctx:CPP14Parser.ClassNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#className.
    def exitClassName(self, ctx:CPP14Parser.ClassNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classContent.
    def enterClassContent(self, ctx:CPP14Parser.ClassContentContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classContent.
    def exitClassContent(self, ctx:CPP14Parser.ClassContentContext):
        pass


    # Enter a parse tree produced by CPP14Parser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:CPP14Parser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:CPP14Parser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:CPP14Parser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:CPP14Parser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#methodReturnType.
    def enterMethodReturnType(self, ctx:CPP14Parser.MethodReturnTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#methodReturnType.
    def exitMethodReturnType(self, ctx:CPP14Parser.MethodReturnTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#methodName.
    def enterMethodName(self, ctx:CPP14Parser.MethodNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#methodName.
    def exitMethodName(self, ctx:CPP14Parser.MethodNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:CPP14Parser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:CPP14Parser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#functionReturnType.
    def enterFunctionReturnType(self, ctx:CPP14Parser.FunctionReturnTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionReturnType.
    def exitFunctionReturnType(self, ctx:CPP14Parser.FunctionReturnTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parameterType.
    def enterParameterType(self, ctx:CPP14Parser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterType.
    def exitParameterType(self, ctx:CPP14Parser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:CPP14Parser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:CPP14Parser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#returnType.
    def enterReturnType(self, ctx:CPP14Parser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#returnType.
    def exitReturnType(self, ctx:CPP14Parser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#undefinedReturnType.
    def enterUndefinedReturnType(self, ctx:CPP14Parser.UndefinedReturnTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#undefinedReturnType.
    def exitUndefinedReturnType(self, ctx:CPP14Parser.UndefinedReturnTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parameterList.
    def enterParameterList(self, ctx:CPP14Parser.ParameterListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterList.
    def exitParameterList(self, ctx:CPP14Parser.ParameterListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parameter.
    def enterParameter(self, ctx:CPP14Parser.ParameterContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameter.
    def exitParameter(self, ctx:CPP14Parser.ParameterContext):
        pass



del CPP14Parser