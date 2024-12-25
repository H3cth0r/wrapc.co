from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from MyCppListener import MyCppListener, Constructor

from typing import List, Dict, Optional, Tuple

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
        self.output = """
        #include <Python.h>
        """
        self.type_conversions = {
            'int': ('PyLong_AsLong', 'PyLong_FromLong', 'i'),
            'char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'size_t': ('PyLong_AsSize_t', 'PyLong_FromSize_t', 'n'),
            'uint8_t*': ('PyBytes_AsString', 'PyBytes_FromStringAndSize', 'y#'),
            'const char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'FILE*': (None, None, 'O'),
            'void': (None, None, None),
            'std::string': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'const std::string &': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's')
        }
        self.classes_to_parse = ["Dog"]
    def _get_type_format(self, param_type: str) -> str:
        """return format character for PyArg_ParseTuple"""
        return self.type_conversions.get(param_type, (None, None, 'O'))[2]
    def _get_type_converter(self, param_type: str, to_python: bool = True) -> str:
        """return appropiate type converter function"""
        converters =  self.type_conversions.get(param_type, (None, None, None))
        to_convert = converters[1] if to_python else converters[0]
        return to_convert if to_convert is not None else ""
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
    def _generate_args_param_parsing(self, params: List) -> Tuple[str, str]:
        """generate parameter parsing code and format string for PyArg_ParseTuple"""
        format_str = ""
        parse_vars = []
        parse_code = []
        parse_PyArgs = []

        for param in params:
            format_char = self._get_type_format(param.paramType)
            if format_char:
                format_str += format_char
                if "std::string" in param.paramType:
                    parse_vars.append(f"const char* {param.paramName}_str")
                    parse_PyArgs.append(f"& {param.paramName}_str")
                    parse_code.append(f"std::string {param.paramName}({param.paramName}_str);")
                else: 
                    parse_vars.append(f"{param.paramType} {param.paramName}")
                    parse_PyArgs.append(f"& {param.paramName}")
        return format_str, "; ".join(parse_vars), "\n            ".join(parse_code), ", ".join(parse_PyArgs)
    def _generateObjectStructures(self):
        for _class in self.program.classes:
            self.output += f"""
typedef struct {{
    PyObject_HEAD
    {_class.className}* cpp_instance;
}} Py{_class.className};
            """
    def _generateConstructor(self, _class):
        format_str, parse_vars, parse_code, parse_PyArgs = self._generate_args_param_parsing(_class.constructors[0].params)
        args_part = ""
        if parse_PyArgs != "":
            args_part = f"""
        if (!PyArg_ParseTuple(args, "{format_str}", {parse_PyArgs})) {{
            Py_DECREF(self);
            return nullptr;
        }}
            """
        parse_vars = parse_vars + ";" if parse_vars!= "" else parse_vars
        self.output += f"""
static PyObject* {_class.className}_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {{
    Py{_class.className}* self = (Py{_class.className}*)type->tp_alloc(type, 0);
    if (self) {{
        {parse_vars}
        {args_part}
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

static void {_class.className}_dealloc(Py{_class.className}* self) {{
    if (self->cpp_instance) {{
        delete self->cpp_instance;
    }}
    Py_TYPE(self)->tp_free((PyObject*)self);
}}
        """
    def _generateMethod(self, _class, method): 
        format_str, parse_vars, parse_code, parse_PyArgs= self._generate_args_param_parsing(method.params)
        print("return type: " + method.returnType + "\tmethod: " + method.methodName)
        converter = self._get_type_converter(method.returnType, to_python=True)
        self.output += f"""
static PyObject* {_class.className}_{method.methodName}(Py{_class.className}* self, PyObject* args) {{
        """
        if method.params: 
            self.output += f"""
    {parse_vars};
    if (!PyArg_ParseTuple(args, "{format_str}", {parse_PyArgs})) {{
        return nullptr;
    }}
    {parse_code}
            """
        if method.returnType == "void":
            self.output += f"""
    self->cpp_instance->{method.methodName}({", ".join(p.paramName for p in method.params)});
    Py_RETURN_NONE;
            """
        else:
            self.output += f"""
    auto result = self->cpp_instance->{method.methodName}({", ".join(p.paramName for p in method.params)});
    return {converter}(result{"" if "std::string" not in method.returnType else ".c_str()"});
            """
        self.output += "}\n"

    def _generateMethods(self, _class):
        method_defs = []
        for method in _class.methods:
            self._generateMethod(_class, method)
            method_defs.append(
                f'{{"{method.methodName}", '
                f'(PyCFunction){_class.className}_{method.methodName}, '
                f'{"METH_VARARGS" if method.params else "METH_NOARGS"}, '
                f'"Execute {method.methodName}"}}'
            )
        
        method_list = ",\n    ".join(method_defs)
        self.output += f"""
static PyMethodDef {_class.className}_methods[] = {{
    {method_list},
    {{NULL, NULL, 0, NULL}}
}};
        """
    def _generateTypeObject(self, _class):
        self.output += f"""
static PyTypeObject {_class.className}Type = {{
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "example.{_class.className}",
    .tp_basicsize = sizeof(Py{_class.className}),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor){_class.className}_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "{_class.className} objects",
    .tp_methods = {_class.className}_methods,
    .tp_new = {_class.className}_new,
}};
        """
    def generate(self):
        self._generateObjectStructures()

        for _class in self.program.classes:
            if _class.className not in self.classes_to_parse: continue
            if _class.constructors: self._generateConstructor(_class)
            else:
                _class.constructors.append(Constructor())
                self._generateConstructor(_class)
            self._generateMethods(_class)
            self._generateTypeObject(_class)
        self._generateModuleInit()

    def _generateModuleInit(self):
        self.output += """
static PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",
    "Example module",
    -1,
    nullptr
};

PyMODINIT_FUNC PyInit_example(void) {
        """
        for _class in self.program.classes:
            if _class.className not in self.classes_to_parse: continue
            self.output += f"""
    if (PyType_Ready(&{_class.className}Type) < 0) {{
        return nullptr;
    }}
            """
        self.output += """
    PyObject* m = PyModule_Create(&examplemodule);
    if (!m) {
        return nullptr;
    }
        """
        for _class in self.program.classes:
            if _class.className not in self.classes_to_parse: continue
            self.output += f"""
    Py_INCREF(&{_class.className}Type);
    if (PyModule_AddObject(m, "{_class.className}", (PyObject*)&{_class.className}Type) < 0) {{
        Py_DECREF(&{_class.className}Type);
        Py_DECREF(m);
        return nullptr;
    }}
            """
        self.output += """
    return m;
}
        """

if __name__ == "__main__":
    path = "./examples/test_2.h"
    parserHandler = ParserHandler(path)
    pprint.pp(parserHandler.program)
    extensionGenerator =  ExtensionGenerator(parserHandler.program)
    extensionGenerator.generate()
    print(extensionGenerator.output)
