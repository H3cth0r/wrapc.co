import sys
from dataclasses import dataclass, field
from typing import List
# import pprint
sys.path.append('./walkers')
from CPP14Listener import CPP14Listener

@dataclass
class Param:
    paramType: str = ""
    paramName: str = ""
@dataclass
class Method:
    accessSpecifier: str = ""
    methodName: str = ""
    params: List[Param] = field(default_factory=list)
    returnType: str = ""
@dataclass
class Constructor:
    params: List[Param] = field(default_factory=list)
@dataclass
class Attribute:
    accessSpecifier: str = ""
    attrType: str = ""
    attrName: str = ""
@dataclass
class ClassDef:
    className: str = ""
    constructors: List[Constructor] = field(default_factory=list)
    methods: List[Method] = field(default_factory=list)
    attributes: List[Attribute] = field(default_factory=list)

@dataclass
class Function:
    returnType: str = ""
    functionName: str = ""
    params: List[Param] = field(default_factory=list)

@dataclass
class Program:
    classes: List[ClassDef] = field(default_factory=list)
    functions: List[Function] = field(default_factory=list)

class MyCppListener(CPP14Listener):
    def __init__(self):
        self.inProgramContent = ""
        self.accessSpecifier = 'private'
        self.method = None
        self.constructor = None
        self.attribute = None
        self.function = None
        print("\n"*2)
        self.program = Program()

    # Enter class defintion
    def enterClassDefinition(self, ctx):
        self.inProgramContent = "class"
        self.classDef = ClassDef()
        self.classDef.className = ctx.getChild(1).getText()

    def enterAccessSpecifier(self, ctx):
        self.accessSpecifier = ctx.getChild(0).getText()

    def enterConstructorDeclaration(self, ctx): self.constructor = Constructor()
    def exitConstructorDeclaration(self, ctx): 
        self.classDef.constructors.append(self.constructor)
        self.constructor = None

    def enterMethodDeclaration(self, ctx):
        self.method = Method()
        self.method.accessSpecifier = self.accessSpecifier
    def enterMethodName(self, ctx): self.method.methodName = ctx.getText()
    def enterMethodReturnType(self, ctx): 
        RT = ctx.getChild(0)
        for i in range(RT.getChildCount()):
            txt = RT.getChild(i).getText()
            self.method.returnType += txt if RT.getChildCount()-1 == i else txt + " "
    def enterParameter(self, ctx):
        param = Param()
        for i in range(ctx.getChildCount()):
            txt = ctx.getChild(i).getText()
            if i == ctx.getChildCount()-1: param.paramName += txt
            else: param.paramType += txt if ctx.getChildCount()-2 == i else txt + " "
        if self.method: self.method.params.append(param)
        elif self.constructor: self.constructor.params.append(param)
        elif self.function: self.function.params.append(param)
    def exitMethodDeclaration(self, ctx): 
        self.classDef.methods.append(self.method)
        self.method = None

    def enterAttributeDeclaration(self, ctx):
        self.attribute = Attribute()
        self.attribute.accessSpecifier = self.accessSpecifier
        self.attribute.attrType = ctx.getChild(0).getText()
        self.attribute.attrName = ctx.getChild(1).getText()
    def exitAttributeDeclaration(self, ctx):
        self.classDef.attributes.append(self.attribute)
        self.attribute = None

    def exitClassDefinition(self, ctx):
        # print(self.classDef)
        # pprint.pp(self.classDef)
        self.program.classes.append(self.classDef)
    # Exit class defintion

    def enterFunctionDefinition(self, ctx):
        self.function = Function()
        self.function.functionName = ctx.getChild(1).getText()
    def enterFunctionReturnType(self, ctx):
        RT = ctx.getChild(0)
        for i in range(ctx.getChildCount()):
            txt = RT.getChild(i).getText()
            self.function.returnType += txt if RT.getChildCount()-1 == i else txt + " "
    def exitFunctionDefinition(self, ctx):
        self.program.functions.append(self.function)
        self.function = None

    def exitProgram(self, ctx):
        # pprint.pp(self.program)
        pass

