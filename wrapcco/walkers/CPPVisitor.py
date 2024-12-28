# Generated from CPP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CPPParser import CPPParser
else:
    from CPPParser import CPPParser

# This class defines a complete generic visitor for a parse tree produced by CPPParser.

class CPPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPPParser#program.
    def visitProgram(self, ctx:CPPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#openGuardian.
    def visitOpenGuardian(self, ctx:CPPParser.OpenGuardianContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#closeGuardian.
    def visitCloseGuardian(self, ctx:CPPParser.CloseGuardianContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#programContent.
    def visitProgramContent(self, ctx:CPPParser.ProgramContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#includeStatement.
    def visitIncludeStatement(self, ctx:CPPParser.IncludeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#classDefinition.
    def visitClassDefinition(self, ctx:CPPParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#className.
    def visitClassName(self, ctx:CPPParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#classDerivation.
    def visitClassDerivation(self, ctx:CPPParser.ClassDerivationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#derivedClassName.
    def visitDerivedClassName(self, ctx:CPPParser.DerivedClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#classContent.
    def visitClassContent(self, ctx:CPPParser.ClassContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:CPPParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:CPPParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#templateStatement.
    def visitTemplateStatement(self, ctx:CPPParser.TemplateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#methodReturnType.
    def visitMethodReturnType(self, ctx:CPPParser.MethodReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#methodName.
    def visitMethodName(self, ctx:CPPParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:CPPParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#destructorDeclaration.
    def visitDestructorDeclaration(self, ctx:CPPParser.DestructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CPPParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#functionReturnType.
    def visitFunctionReturnType(self, ctx:CPPParser.FunctionReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#parameterType.
    def visitParameterType(self, ctx:CPPParser.ParameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:CPPParser.AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#returnType.
    def visitReturnType(self, ctx:CPPParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#undefinedReturnType.
    def visitUndefinedReturnType(self, ctx:CPPParser.UndefinedReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#parameterList.
    def visitParameterList(self, ctx:CPPParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPParser#parameter.
    def visitParameter(self, ctx:CPPParser.ParameterContext):
        return self.visitChildren(ctx)



del CPPParser