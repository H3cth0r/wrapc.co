import sys
sys.path.append('./walkers')
from CPP14ParserListener import CPP14ParserListener

class MyCppListener(CPP14ParserListener):
    def __init__(self): pass

    # Class Definition methods
    def enterClassSpecifier(self, ctx): print(ctx.getText())
    # def enterClassHead(self, ctx): print(ctx.getText())
    def enterClassHeadName(self, ctx): 
        # print(ctx.getText())
        py_obj_struct = f"""
typedef struct {{
    PyObject_HEAD
    {ctx.getText()}* cpp_instance;
}} Py{ctx.getText()};
        """
        print(py_obj_struct)
    def exitClassSpecifier(self, ctx): 
        print("="*30)
