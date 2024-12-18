from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from MyCppListener import MyCppListener

from dataclasses import dataclass 

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
        self.program =  program
        self.output = """"""
        self.type_conversions = {
            'int': ('PyLong_AsLong', 'PyLong_FromLong', 'i'),
            'char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'size_t': ('PyLong_AsSize_t', 'PyLong_FromSize_t', 'n'),
            'uint8_t*': ('PyBytes_AsString', 'PyBytes_FromStringAndSize', 'y#'),
            'const char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'FILE*': (None, None, 'O'),
            'void': (None, None, None),
            'std::string': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'const std::string&': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's')
        }
    def _get_type_format(self, param_type: str) -> str:
        """return format character for PyArg_ParseTuple"""
        return self.type_conversions.get(param_type, (None, None, 'O'))[2]
    def _get_type_converter(self, param_type: str, to_python: bool = True) -> str:
        """return appropiate type converter function"""
        converters =  self.type_conversions.get(param_type, (None, None, None))
        return converters[1] if to_python else converters[0]
    def _generate_param_parsing(self, params: List) -> Tuple[str, str]:
        """generate parameter parsing code and format string for PyArg_ParseTuple"""
        format_str = ""
        parse_vars = []
        parse_code = []

        for param in params:
            format_char = self._get_type_format(param.paramType)
            if format_char:
                format_str += format_char
                if "std::string" in param.paramType:
                    parse_vars.append(f"const char* {param.paramName}_str")
                    parse_code.append(f"std::string {param.paramName}({param.paramName}_str);")
                else: parse_vars.append(f"{param.paramType} {param.paramName}")
        return format_str, ", ".join(parse_vars), "\n            ".join(parse_code)
    def _generateObjectStructures(self):
        for _class in self.program.classes:
            self.output += f"""
typedef struct {{
    PyObject_HEAD
    {_class.className}* cpp_instance;
}} Py{_class.className};
            """
    def _generateConstructor(self, _class):
        format_str, parse_vars, parse_code = self._generate_param_parsing(_class.constructors[0].params)
        self.output += f"""
static PyObject* {_class.className}_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {{
    Py{_class.className}* self = (Py{_class.className}*)type->tp_alloc(type, 0);
    if (self) {{
        {parse_vars};
        if (!PyArg_ParseTuple(args, "{format_str}", {parse_vars})) {{
            Py_DECREF(self);
            return nullptr;
        }}
        {parse_code}
        try {{
            self->cpp_instance = new {_class.className}({", ".join(p.paramName for p in _class.constructors[0].params)});
        }} catch (const std::exception& e) {{
            PyErr_SetString(PyExc_RuntimeError, e.what());
            Py_DECREF(self);
            return nullptr;
        }}
    }}
    return (PyObject*)self;
}}

static void (_class.className)_dealloc(Py{_class.className}* self) {{
    if (self->cpp_instance) {{
        delete self->cpp_instance;
    }}
    Py_TYPE(self)->tp_free((PyObject*)self);
}}
        """
    def _generateMethod(self, _class, method): 
        format_str, parse_vars, parse_code = self._generate_param_parsing(method.params)
        converter = self._get_type_converter(method.returnType, to_python=True)
        self.output += f"""
static PyObject* {_class.className}_{method.methodName}(Py{_class.className}* self, PyObject* args) {{
        """

if __name__ == "__main__":
    path = "./examples/test_2.h"
    parserHandler = ParserHandler(path)
    pprint.pp(parserHandler.program)
    extensionGenerator =  ExtensionGenerator(parserHandler.program)
    extensionGenerator.generate()
    print(extensionGenerator.output)
