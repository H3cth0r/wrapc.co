from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from MyCppListener import MyCppListener

import pprint
import sys
sys.path.append('./walkers')
from CPP14Lexer import CPP14Lexer
from CPP14Parser import CPP14Parser

class ParserHandler:
    def __init__(self, filePath):
        self.filePath = filePath
        with open(filePath, "r") as fileContent: inputStream = InputStream(fileContent.read()) 
        lexer = CPP14Lexer(inputStream)
        tokenStream = CommonTokenStream(lexer)
        parser = CPP14Parser(tokenStream)
        tree = parser.program()
        self.listener = MyCppListener()
        walker = ParseTreeWalker()
        walker.walk(self.listener, tree)
        self.program = self.listener.program

class ExtensionGenerator:
    def __init__(self, program):
        self.program = program
        self.output = """"""
        self.type_conversions = {
            'int':          ('PyLong_AsLong', 'PyLong_FromLong', 'i'),
            'char*':        ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'size_t':       ('PyLong_AsSize_t', 'PyLong_FromSize_t', 'n'),
            'uint8_t*':     ('PyBytes_AsString', 'PyBytes_FromStringAndSize', 'y#'),
            'const char*':  ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'FILE*':        (None, None, 'O'),
            'void':         (None, None, None)

            # Cpp type conversion
            'std::string':        ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
        }
    def _generateObjectStructures(self):
        for _class in self.program.classes:
            self.output += f"""
typedef struct {{
    PyObject_HEAD
    {_class.className}* cpp_instance;
}} Py{_class.className};
            """
    def _generateWrapperMethods(self):
        for _class in self.program.classes:
            self._generateInitMethod(_class)

    def _generateInitMethod(self, _class):
        self.output += """
static PyObject* {_class.className}_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {{
    Py{_class.className}* self = (Py{_class.className}*)type->tp_alloc(type, 0);
    if (self) {
    }
}}
        """


    def generate(self):
        self._generateObjectStructures()
        self._generateWrapperMethods()

if __name__ == "__main__":
    path = "./examples/test_2.h"
    parserHandler = ParserHandler(path)
    pprint.pp(parserHandler.program)
    extensionGenerator =  ExtensionGenerator(parserHandler.program)
    extensionGenerator.generate()
    print(extensionGenerator.output)
