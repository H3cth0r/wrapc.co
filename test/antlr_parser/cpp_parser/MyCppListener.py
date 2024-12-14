import sys
from dataclasses import dataclass, field
from typing import List
sys.path.append('./walkers')
from CPP14ParserListener import CPP14ParserListener

@dataclass
class ParamDef:
    paramName: str
    paramType: str
@dataclass
class ClassMethod:
    methodName: str
    returnType: str
@dataclass
class Attribute:
    attributeType: str 
    attributeName: str
@dataclass
class ClassDef:
    className: str = "default name"
    constructors:   List[ClassMethod]   = field(default_factory=list)
    methods:        List[ClassMethod]   = field(default_factory=list)
    attributes:     List[Attribute]     = field(default_factory=list)

def iterate(baseNode, level=0):
    try:
        levelIndent = "  "*level
        print(f"{levelIndent}-> {baseNode.__class__.__name__}\t\t{baseNode.getText()}")
    except: return
    for i in range(baseNode.getChildCount()):
        iterate(baseNode.getChild(i), level+1)
    
class MyCppListener(CPP14ParserListener):
    def __init__(self): 
        self.classes = []
        self.functions = []

    def enterClassSpecifier(self, ctx): 
        self.currentClass = ClassDef()
        self.inClassDef = True
        print(ctx.getText())

    # def enterClassHead(self, ctx): print(ctx.getText())

    def enterClassHeadName(self, ctx): 
        self.currentClass.className = ctx.getText()
        print(ctx.getText())

    # def enterMemberSpecification(self, ctx): print(ctx.getText())
    # def enterMemberdeclaration(self, ctx): print(ctx.getText())
    def enterMemberdeclaration(self, ctx): 
        # print(ctx.getChild(0).__class__.__name__)
        pass
    # def enter
    def enterEmptyDefinition(self, ctx): 
        print("---")
        # print(f"-> {ctx.__class__.__name__}\t\t{ctx.getText()}")
        # for i in range(ctx.getChildCount()-1):
        #     print(f"\t-> {ctx.getChild(i).__class__.__name__}\t\t{ctx.getChild(i).getText()}")
        #     if ctx.getChildCount() == 0: continue
        #     for j in range(ctx.getChildCount()):
        #         try:
        #             print(f"\t\t-> {ctx.getChild(i).getChild(j).__class__.__name__}\t\t{ctx.getChild(i).getChild(j).getText()}")
        #         except: continue
        # print(ctx.getChildCount())
        iterate(ctx)
    
    def exitClassHeadName(self, ctx):
        print(self.currentClass)
        self.inClassDef = False
        self.classes.append(self.currentClass)

    def exitClassSpecifier(self, ctx): print("="*30)
