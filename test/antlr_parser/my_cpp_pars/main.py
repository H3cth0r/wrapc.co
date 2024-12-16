from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from MyCppListener import MyCppListener

import sys
sys.path.append('./walkers')
from CPP14Lexer import CPP14Lexer
from CPP14Parser import CPP14Parser

if __name__ == "__main__":
    path = "./examples/test_2.h"
    with open(path, "r") as cpp_f: input_stream = InputStream(cpp_f.read())
    lexer = CPP14Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CPP14Parser(token_stream)

    tree = parser.program()

    listener = MyCppListener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)
