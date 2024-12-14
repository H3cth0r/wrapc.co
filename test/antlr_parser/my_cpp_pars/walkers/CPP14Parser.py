# Generated from CPP14Parser.g4 by ANTLR 4.13.1
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
        4,1,31,154,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,3,0,
        41,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,3,3,55,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,1,4,1,4,1,
        5,1,5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,5,1,5,3,5,81,8,5,1,6,
        1,6,1,7,1,7,1,7,1,7,3,7,89,8,7,1,8,1,8,1,8,1,9,1,9,1,9,3,9,97,8,
        9,1,9,1,9,1,9,1,10,3,10,103,8,10,1,10,1,10,1,10,1,10,3,10,109,8,
        10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,119,8,12,10,12,12,
        12,122,9,12,1,13,3,13,125,8,13,1,13,1,13,1,13,1,13,3,13,131,8,13,
        1,13,1,13,1,13,1,13,1,13,3,13,138,8,13,1,13,1,13,1,13,1,13,3,13,
        144,8,13,1,14,1,14,3,14,148,8,14,1,15,1,15,1,15,1,15,1,15,0,0,16,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,0,3,5,2,0,2,2,25,
        25,156,0,32,1,0,0,0,2,42,1,0,0,0,4,49,1,0,0,0,6,54,1,0,0,0,8,56,
        1,0,0,0,10,69,1,0,0,0,12,82,1,0,0,0,14,88,1,0,0,0,16,90,1,0,0,0,
        18,93,1,0,0,0,20,102,1,0,0,0,22,113,1,0,0,0,24,115,1,0,0,0,26,143,
        1,0,0,0,28,147,1,0,0,0,30,149,1,0,0,0,32,36,3,2,1,0,33,35,3,6,3,
        0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,40,
        1,0,0,0,38,36,1,0,0,0,39,41,3,4,2,0,40,39,1,0,0,0,40,41,1,0,0,0,
        41,1,1,0,0,0,42,43,5,20,0,0,43,44,5,6,0,0,44,45,5,26,0,0,45,46,5,
        20,0,0,46,47,5,7,0,0,47,48,5,26,0,0,48,3,1,0,0,0,49,50,5,20,0,0,
        50,51,5,8,0,0,51,5,1,0,0,0,52,55,3,8,4,0,53,55,3,10,5,0,54,52,1,
        0,0,0,54,53,1,0,0,0,55,7,1,0,0,0,56,57,5,20,0,0,57,58,5,9,0,0,58,
        59,5,14,0,0,59,64,5,27,0,0,60,61,5,18,0,0,61,63,5,27,0,0,62,60,1,
        0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,
        64,1,0,0,0,67,68,5,15,0,0,68,9,1,0,0,0,69,70,5,1,0,0,70,71,3,12,
        6,0,71,75,5,10,0,0,72,74,3,14,7,0,73,72,1,0,0,0,74,77,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,80,5,11,
        0,0,79,81,5,16,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,11,1,0,0,0,82,
        83,5,27,0,0,83,13,1,0,0,0,84,89,3,16,8,0,85,89,3,18,9,0,86,89,3,
        20,10,0,87,89,3,30,15,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,
        0,88,87,1,0,0,0,89,15,1,0,0,0,90,91,7,0,0,0,91,92,5,17,0,0,92,17,
        1,0,0,0,93,94,3,12,6,0,94,96,5,12,0,0,95,97,3,24,12,0,96,95,1,0,
        0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,13,0,0,99,100,5,16,0,0,100,
        19,1,0,0,0,101,103,5,21,0,0,102,101,1,0,0,0,102,103,1,0,0,0,103,
        104,1,0,0,0,104,105,3,22,11,0,105,106,5,27,0,0,106,108,5,12,0,0,
        107,109,3,24,12,0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,
        0,110,111,5,13,0,0,111,112,5,16,0,0,112,21,1,0,0,0,113,114,7,1,0,
        0,114,23,1,0,0,0,115,120,3,26,13,0,116,117,5,19,0,0,117,119,3,26,
        13,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,
        0,0,121,25,1,0,0,0,122,120,1,0,0,0,123,125,5,22,0,0,124,123,1,0,
        0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,127,3,28,14,0,127,128,5,
        27,0,0,128,144,1,0,0,0,129,131,5,22,0,0,130,129,1,0,0,0,130,131,
        1,0,0,0,131,132,1,0,0,0,132,133,3,28,14,0,133,134,5,23,0,0,134,135,
        5,27,0,0,135,144,1,0,0,0,136,138,5,22,0,0,137,136,1,0,0,0,137,138,
        1,0,0,0,138,139,1,0,0,0,139,140,3,28,14,0,140,141,5,24,0,0,141,142,
        5,27,0,0,142,144,1,0,0,0,143,124,1,0,0,0,143,130,1,0,0,0,143,137,
        1,0,0,0,144,27,1,0,0,0,145,148,5,25,0,0,146,148,3,12,6,0,147,145,
        1,0,0,0,147,146,1,0,0,0,148,29,1,0,0,0,149,150,5,25,0,0,150,151,
        5,27,0,0,151,152,5,16,0,0,152,31,1,0,0,0,16,36,40,54,64,75,80,88,
        96,102,108,120,124,130,137,143,147
    ]

class CPP14Parser ( Parser ):

    grammarFileName = "CPP14Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'void'", "'public'", "'protected'", 
                     "'private'", "'ifndef'", "'define'", "'endif'", "'include'", 
                     "'{'", "'}'", "'('", "')'", "'<'", "'>'", "';'", "':'", 
                     "'::'", "','", "'#'", "'static'", "'const'", "'&'", 
                     "'*'" ]

    symbolicNames = [ "<INVALID>", "Class", "Void", "PublicAccess", "ProtectedAccess", 
                      "PrivateAccess", "Ifndef", "Define", "Endif", "Include", 
                      "LeftBrace", "RightBrace", "LeftPar", "RightPar", 
                      "LeftChevron", "RightChevron", "Semi", "Colon", "DoubleColon", 
                      "Comma", "Hash", "Static", "Const", "Ampersand", "Star", 
                      "Type", "MacroIdentifier", "Identifier", "Whitespace", 
                      "Newline", "BlockComment", "LineComment" ]

    RULE_cppFile = 0
    RULE_openGuardian = 1
    RULE_closeGuardian = 2
    RULE_programContent = 3
    RULE_includeStatement = 4
    RULE_classDefinition = 5
    RULE_className = 6
    RULE_classContent = 7
    RULE_accessSpecifier = 8
    RULE_constructorDeclaration = 9
    RULE_methodDeclaration = 10
    RULE_returnType = 11
    RULE_parameterList = 12
    RULE_parameter = 13
    RULE_parameterType = 14
    RULE_attributeDeclaration = 15

    ruleNames =  [ "cppFile", "openGuardian", "closeGuardian", "programContent", 
                   "includeStatement", "classDefinition", "className", "classContent", 
                   "accessSpecifier", "constructorDeclaration", "methodDeclaration", 
                   "returnType", "parameterList", "parameter", "parameterType", 
                   "attributeDeclaration" ]

    EOF = Token.EOF
    Class=1
    Void=2
    PublicAccess=3
    ProtectedAccess=4
    PrivateAccess=5
    Ifndef=6
    Define=7
    Endif=8
    Include=9
    LeftBrace=10
    RightBrace=11
    LeftPar=12
    RightPar=13
    LeftChevron=14
    RightChevron=15
    Semi=16
    Colon=17
    DoubleColon=18
    Comma=19
    Hash=20
    Static=21
    Const=22
    Ampersand=23
    Star=24
    Type=25
    MacroIdentifier=26
    Identifier=27
    Whitespace=28
    Newline=29
    BlockComment=30
    LineComment=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CppFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def openGuardian(self):
            return self.getTypedRuleContext(CPP14Parser.OpenGuardianContext,0)


        def programContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPP14Parser.ProgramContentContext)
            else:
                return self.getTypedRuleContext(CPP14Parser.ProgramContentContext,i)


        def closeGuardian(self):
            return self.getTypedRuleContext(CPP14Parser.CloseGuardianContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_cppFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCppFile" ):
                listener.enterCppFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCppFile" ):
                listener.exitCppFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCppFile" ):
                return visitor.visitCppFile(self)
            else:
                return visitor.visitChildren(self)




    def cppFile(self):

        localctx = CPP14Parser.CppFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cppFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.openGuardian()
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 33
                    self.programContent() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 39
                self.closeGuardian()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenGuardianContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Hash(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.Hash)
            else:
                return self.getToken(CPP14Parser.Hash, i)

        def Ifndef(self):
            return self.getToken(CPP14Parser.Ifndef, 0)

        def MacroIdentifier(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.MacroIdentifier)
            else:
                return self.getToken(CPP14Parser.MacroIdentifier, i)

        def Define(self):
            return self.getToken(CPP14Parser.Define, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_openGuardian

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpenGuardian" ):
                listener.enterOpenGuardian(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpenGuardian" ):
                listener.exitOpenGuardian(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpenGuardian" ):
                return visitor.visitOpenGuardian(self)
            else:
                return visitor.visitChildren(self)




    def openGuardian(self):

        localctx = CPP14Parser.OpenGuardianContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_openGuardian)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(CPP14Parser.Hash)
            self.state = 43
            self.match(CPP14Parser.Ifndef)
            self.state = 44
            self.match(CPP14Parser.MacroIdentifier)
            self.state = 45
            self.match(CPP14Parser.Hash)
            self.state = 46
            self.match(CPP14Parser.Define)
            self.state = 47
            self.match(CPP14Parser.MacroIdentifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseGuardianContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Hash(self):
            return self.getToken(CPP14Parser.Hash, 0)

        def Endif(self):
            return self.getToken(CPP14Parser.Endif, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_closeGuardian

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloseGuardian" ):
                listener.enterCloseGuardian(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloseGuardian" ):
                listener.exitCloseGuardian(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCloseGuardian" ):
                return visitor.visitCloseGuardian(self)
            else:
                return visitor.visitChildren(self)




    def closeGuardian(self):

        localctx = CPP14Parser.CloseGuardianContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_closeGuardian)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CPP14Parser.Hash)
            self.state = 50
            self.match(CPP14Parser.Endif)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def includeStatement(self):
            return self.getTypedRuleContext(CPP14Parser.IncludeStatementContext,0)


        def classDefinition(self):
            return self.getTypedRuleContext(CPP14Parser.ClassDefinitionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_programContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramContent" ):
                listener.enterProgramContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramContent" ):
                listener.exitProgramContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramContent" ):
                return visitor.visitProgramContent(self)
            else:
                return visitor.visitChildren(self)




    def programContent(self):

        localctx = CPP14Parser.ProgramContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_programContent)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.includeStatement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.classDefinition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Hash(self):
            return self.getToken(CPP14Parser.Hash, 0)

        def Include(self):
            return self.getToken(CPP14Parser.Include, 0)

        def LeftChevron(self):
            return self.getToken(CPP14Parser.LeftChevron, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.Identifier)
            else:
                return self.getToken(CPP14Parser.Identifier, i)

        def RightChevron(self):
            return self.getToken(CPP14Parser.RightChevron, 0)

        def DoubleColon(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.DoubleColon)
            else:
                return self.getToken(CPP14Parser.DoubleColon, i)

        def getRuleIndex(self):
            return CPP14Parser.RULE_includeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeStatement" ):
                listener.enterIncludeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeStatement" ):
                listener.exitIncludeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludeStatement" ):
                return visitor.visitIncludeStatement(self)
            else:
                return visitor.visitChildren(self)




    def includeStatement(self):

        localctx = CPP14Parser.IncludeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_includeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(CPP14Parser.Hash)
            self.state = 57
            self.match(CPP14Parser.Include)
            self.state = 58
            self.match(CPP14Parser.LeftChevron)
            self.state = 59
            self.match(CPP14Parser.Identifier)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 60
                self.match(CPP14Parser.DoubleColon)
                self.state = 61
                self.match(CPP14Parser.Identifier)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(CPP14Parser.RightChevron)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(CPP14Parser.Class, 0)

        def className(self):
            return self.getTypedRuleContext(CPP14Parser.ClassNameContext,0)


        def LeftBrace(self):
            return self.getToken(CPP14Parser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(CPP14Parser.RightBrace, 0)

        def classContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPP14Parser.ClassContentContext)
            else:
                return self.getTypedRuleContext(CPP14Parser.ClassContentContext,i)


        def Semi(self):
            return self.getToken(CPP14Parser.Semi, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefinition" ):
                return visitor.visitClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classDefinition(self):

        localctx = CPP14Parser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(CPP14Parser.Class)
            self.state = 70
            self.className()
            self.state = 71
            self.match(CPP14Parser.LeftBrace)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 169869372) != 0):
                self.state = 72
                self.classContent()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(CPP14Parser.RightBrace)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 79
                self.match(CPP14Parser.Semi)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_className

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassName" ):
                listener.enterClassName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassName" ):
                listener.exitClassName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassName" ):
                return visitor.visitClassName(self)
            else:
                return visitor.visitChildren(self)




    def className(self):

        localctx = CPP14Parser.ClassNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessSpecifier(self):
            return self.getTypedRuleContext(CPP14Parser.AccessSpecifierContext,0)


        def constructorDeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.ConstructorDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.MethodDeclarationContext,0)


        def attributeDeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.AttributeDeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_classContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassContent" ):
                listener.enterClassContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassContent" ):
                listener.exitClassContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassContent" ):
                return visitor.visitClassContent(self)
            else:
                return visitor.visitChildren(self)




    def classContent(self):

        localctx = CPP14Parser.ClassContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classContent)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.accessSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.constructorDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.methodDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.attributeDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Colon(self):
            return self.getToken(CPP14Parser.Colon, 0)

        def PublicAccess(self):
            return self.getToken(CPP14Parser.PublicAccess, 0)

        def ProtectedAccess(self):
            return self.getToken(CPP14Parser.ProtectedAccess, 0)

        def PrivateAccess(self):
            return self.getToken(CPP14Parser.PrivateAccess, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_accessSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessSpecifier" ):
                listener.enterAccessSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessSpecifier" ):
                listener.exitAccessSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessSpecifier" ):
                return visitor.visitAccessSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def accessSpecifier(self):

        localctx = CPP14Parser.AccessSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_accessSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 91
            self.match(CPP14Parser.Colon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(CPP14Parser.ClassNameContext,0)


        def LeftPar(self):
            return self.getToken(CPP14Parser.LeftPar, 0)

        def RightPar(self):
            return self.getToken(CPP14Parser.RightPar, 0)

        def Semi(self):
            return self.getToken(CPP14Parser.Semi, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_constructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclaration" ):
                listener.enterConstructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclaration" ):
                listener.exitConstructorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDeclaration" ):
                return visitor.visitConstructorDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constructorDeclaration(self):

        localctx = CPP14Parser.ConstructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.className()
            self.state = 94
            self.match(CPP14Parser.LeftPar)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 171966464) != 0):
                self.state = 95
                self.parameterList()


            self.state = 98
            self.match(CPP14Parser.RightPar)
            self.state = 99
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(CPP14Parser.ReturnTypeContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def LeftPar(self):
            return self.getToken(CPP14Parser.LeftPar, 0)

        def RightPar(self):
            return self.getToken(CPP14Parser.RightPar, 0)

        def Semi(self):
            return self.getToken(CPP14Parser.Semi, 0)

        def Static(self):
            return self.getToken(CPP14Parser.Static, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = CPP14Parser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 101
                self.match(CPP14Parser.Static)


            self.state = 104
            self.returnType()
            self.state = 105
            self.match(CPP14Parser.Identifier)
            self.state = 106
            self.match(CPP14Parser.LeftPar)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 171966464) != 0):
                self.state = 107
                self.parameterList()


            self.state = 110
            self.match(CPP14Parser.RightPar)
            self.state = 111
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(CPP14Parser.Type, 0)

        def Void(self):
            return self.getToken(CPP14Parser.Void, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_returnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnType" ):
                listener.enterReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnType" ):
                listener.exitReturnType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = CPP14Parser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==2 or _la==25):
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


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPP14Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(CPP14Parser.ParameterContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.Comma)
            else:
                return self.getToken(CPP14Parser.Comma, i)

        def getRuleIndex(self):
            return CPP14Parser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = CPP14Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.parameter()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 116
                self.match(CPP14Parser.Comma)
                self.state = 117
                self.parameter()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterType(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterTypeContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def Const(self):
            return self.getToken(CPP14Parser.Const, 0)

        def Ampersand(self):
            return self.getToken(CPP14Parser.Ampersand, 0)

        def Star(self):
            return self.getToken(CPP14Parser.Star, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = CPP14Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 123
                    self.match(CPP14Parser.Const)


                self.state = 126
                self.parameterType()
                self.state = 127
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 129
                    self.match(CPP14Parser.Const)


                self.state = 132
                self.parameterType()
                self.state = 133
                self.match(CPP14Parser.Ampersand)
                self.state = 134
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 136
                    self.match(CPP14Parser.Const)


                self.state = 139
                self.parameterType()
                self.state = 140
                self.match(CPP14Parser.Star)
                self.state = 141
                self.match(CPP14Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(CPP14Parser.Type, 0)

        def className(self):
            return self.getTypedRuleContext(CPP14Parser.ClassNameContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_parameterType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterType" ):
                listener.enterParameterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterType" ):
                listener.exitParameterType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterType" ):
                return visitor.visitParameterType(self)
            else:
                return visitor.visitChildren(self)




    def parameterType(self):

        localctx = CPP14Parser.ParameterTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameterType)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(CPP14Parser.Type)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.className()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(CPP14Parser.Type, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def Semi(self):
            return self.getToken(CPP14Parser.Semi, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_attributeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeDeclaration" ):
                listener.enterAttributeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeDeclaration" ):
                listener.exitAttributeDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclaration" ):
                return visitor.visitAttributeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def attributeDeclaration(self):

        localctx = CPP14Parser.AttributeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attributeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(CPP14Parser.Type)
            self.state = 150
            self.match(CPP14Parser.Identifier)
            self.state = 151
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





