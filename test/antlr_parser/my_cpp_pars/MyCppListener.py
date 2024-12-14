import sys
sys.path.append('./walkers')
from CPP14ParserListener import CPP14ParserListener

class MyCppListener(CPP14ParserListener):
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
