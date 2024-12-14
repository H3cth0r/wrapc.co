import sys
sys.path.append('./walkers')
from CPP14Listener import CPP14Listener

class MyCppListener(CPP14Listener):
    def __init__(self):
        print("\n"*4)
    # def enterOpenGuardian(self, ctx):
    #     print(ctx.getText())
    def enterClassContent(self, ctx):
        print(f"{ctx.getText()}\t\t{ctx.getChild(0).__class__.__name__}")
        print("="*30)
    def enterOpenGuardian(self, ctx):
        print(f"{ctx.getText()}")
        for i in range(ctx.getChildCount()):
            print(f"\t->{ctx.getChild(i).getText()}\t\t{ctx.getChild(i).__class__.__name__}")
    # def enterConstructor(self, ctx):
    #     print(ctx.getText())
    # def enterCloseGuardian(self, ctx):
    #     print(ctx.getText())
    # def enterAccessSpecifier(self, ctx):
    #     print(ctx.getText())
    
    def exitClassDefinition(self, ctx):
        print("\n"*5)
    
    def enterMethodDeclaration(self, ctx):
        print(ctx.getText())

    def enterFunctionDefinition(self, ctx):
        print(ctx.getText())
