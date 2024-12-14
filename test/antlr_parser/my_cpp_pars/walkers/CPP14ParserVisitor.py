# Generated from CPP14Parser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CPP14Parser import CPP14Parser
else:
    from CPP14Parser import CPP14Parser

# This class defines a complete generic visitor for a parse tree produced by CPP14Parser.

class CPP14ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPP14Parser#cppFile.
    def visitCppFile(self, ctx:CPP14Parser.CppFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#openGuardian.
    def visitOpenGuardian(self, ctx:CPP14Parser.OpenGuardianContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#closeGuardian.
    def visitCloseGuardian(self, ctx:CPP14Parser.CloseGuardianContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#programContent.
    def visitProgramContent(self, ctx:CPP14Parser.ProgramContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#includeStatement.
    def visitIncludeStatement(self, ctx:CPP14Parser.IncludeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classDefinition.
    def visitClassDefinition(self, ctx:CPP14Parser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#className.
    def visitClassName(self, ctx:CPP14Parser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#classContent.
    def visitClassContent(self, ctx:CPP14Parser.ClassContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:CPP14Parser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:CPP14Parser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:CPP14Parser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#returnType.
    def visitReturnType(self, ctx:CPP14Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parameterList.
    def visitParameterList(self, ctx:CPP14Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parameter.
    def visitParameter(self, ctx:CPP14Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#parameterType.
    def visitParameterType(self, ctx:CPP14Parser.ParameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPP14Parser#attributeDeclaration.
    def visitAttributeDeclaration(self, ctx:CPP14Parser.AttributeDeclarationContext):
        return self.visitChildren(ctx)



del CPP14Parser