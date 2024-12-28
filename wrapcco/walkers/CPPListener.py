# Generated from CPP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CPPParser import CPPParser
else:
    from CPPParser import CPPParser

# This class defines a complete listener for a parse tree produced by CPPParser.
class CPPListener(ParseTreeListener):

    # Enter a parse tree produced by CPPParser#program.
    def enterProgram(self, ctx:CPPParser.ProgramContext):
        pass

    # Exit a parse tree produced by CPPParser#program.
    def exitProgram(self, ctx:CPPParser.ProgramContext):
        pass


    # Enter a parse tree produced by CPPParser#openGuardian.
    def enterOpenGuardian(self, ctx:CPPParser.OpenGuardianContext):
        pass

    # Exit a parse tree produced by CPPParser#openGuardian.
    def exitOpenGuardian(self, ctx:CPPParser.OpenGuardianContext):
        pass


    # Enter a parse tree produced by CPPParser#closeGuardian.
    def enterCloseGuardian(self, ctx:CPPParser.CloseGuardianContext):
        pass

    # Exit a parse tree produced by CPPParser#closeGuardian.
    def exitCloseGuardian(self, ctx:CPPParser.CloseGuardianContext):
        pass


    # Enter a parse tree produced by CPPParser#programContent.
    def enterProgramContent(self, ctx:CPPParser.ProgramContentContext):
        pass

    # Exit a parse tree produced by CPPParser#programContent.
    def exitProgramContent(self, ctx:CPPParser.ProgramContentContext):
        pass


    # Enter a parse tree produced by CPPParser#includeStatement.
    def enterIncludeStatement(self, ctx:CPPParser.IncludeStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#includeStatement.
    def exitIncludeStatement(self, ctx:CPPParser.IncludeStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#classDefinition.
    def enterClassDefinition(self, ctx:CPPParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#classDefinition.
    def exitClassDefinition(self, ctx:CPPParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#className.
    def enterClassName(self, ctx:CPPParser.ClassNameContext):
        pass

    # Exit a parse tree produced by CPPParser#className.
    def exitClassName(self, ctx:CPPParser.ClassNameContext):
        pass


    # Enter a parse tree produced by CPPParser#classDerivation.
    def enterClassDerivation(self, ctx:CPPParser.ClassDerivationContext):
        pass

    # Exit a parse tree produced by CPPParser#classDerivation.
    def exitClassDerivation(self, ctx:CPPParser.ClassDerivationContext):
        pass


    # Enter a parse tree produced by CPPParser#derivedClassName.
    def enterDerivedClassName(self, ctx:CPPParser.DerivedClassNameContext):
        pass

    # Exit a parse tree produced by CPPParser#derivedClassName.
    def exitDerivedClassName(self, ctx:CPPParser.DerivedClassNameContext):
        pass


    # Enter a parse tree produced by CPPParser#classContent.
    def enterClassContent(self, ctx:CPPParser.ClassContentContext):
        pass

    # Exit a parse tree produced by CPPParser#classContent.
    def exitClassContent(self, ctx:CPPParser.ClassContentContext):
        pass


    # Enter a parse tree produced by CPPParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:CPPParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by CPPParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:CPPParser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by CPPParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:CPPParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:CPPParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#templateStatement.
    def enterTemplateStatement(self, ctx:CPPParser.TemplateStatementContext):
        pass

    # Exit a parse tree produced by CPPParser#templateStatement.
    def exitTemplateStatement(self, ctx:CPPParser.TemplateStatementContext):
        pass


    # Enter a parse tree produced by CPPParser#methodReturnType.
    def enterMethodReturnType(self, ctx:CPPParser.MethodReturnTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#methodReturnType.
    def exitMethodReturnType(self, ctx:CPPParser.MethodReturnTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#methodName.
    def enterMethodName(self, ctx:CPPParser.MethodNameContext):
        pass

    # Exit a parse tree produced by CPPParser#methodName.
    def exitMethodName(self, ctx:CPPParser.MethodNameContext):
        pass


    # Enter a parse tree produced by CPPParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:CPPParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:CPPParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#destructorDeclaration.
    def enterDestructorDeclaration(self, ctx:CPPParser.DestructorDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#destructorDeclaration.
    def exitDestructorDeclaration(self, ctx:CPPParser.DestructorDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CPPParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CPPParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CPPParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CPPParser#functionReturnType.
    def enterFunctionReturnType(self, ctx:CPPParser.FunctionReturnTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#functionReturnType.
    def exitFunctionReturnType(self, ctx:CPPParser.FunctionReturnTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#parameterType.
    def enterParameterType(self, ctx:CPPParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#parameterType.
    def exitParameterType(self, ctx:CPPParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:CPPParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by CPPParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:CPPParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by CPPParser#returnType.
    def enterReturnType(self, ctx:CPPParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#returnType.
    def exitReturnType(self, ctx:CPPParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#undefinedReturnType.
    def enterUndefinedReturnType(self, ctx:CPPParser.UndefinedReturnTypeContext):
        pass

    # Exit a parse tree produced by CPPParser#undefinedReturnType.
    def exitUndefinedReturnType(self, ctx:CPPParser.UndefinedReturnTypeContext):
        pass


    # Enter a parse tree produced by CPPParser#parameterList.
    def enterParameterList(self, ctx:CPPParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CPPParser#parameterList.
    def exitParameterList(self, ctx:CPPParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CPPParser#parameter.
    def enterParameter(self, ctx:CPPParser.ParameterContext):
        pass

    # Exit a parse tree produced by CPPParser#parameter.
    def exitParameter(self, ctx:CPPParser.ParameterContext):
        pass



del CPPParser