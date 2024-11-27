import re
import os
from typing import List
import json

class CExtensionGenerator:
    def __init__(self, header_file: str, source_file: str, methods_to_include: List[str], output_name: str, output_path: str="./"):
        self.header_file = header_file
        self.source_file = source_file
        self.methods_to_include = methods_to_include
        self.output_name = output_name 
        self.output_path = output_path
        self.type_conversions = {
            'int':          ('PyLong_AsLong', 'PyLong_FromLong', 'i'),
            'char*':        ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'size_t':       ('PyLong_AsSize_t', 'PyLong_FromSize_t', 'n'),
            'uint8_t*':     ('PyBytes_AsString', 'PyBytes_FromStringAndSize', 'y#'),
            'const char*':  ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'FILE*':        (None, None, 'O'),
            'void':         (None, None, None)
        }
        self.manual_parsing = False

    def parse_header(self) -> None:
        with open(self.header_file, 'r') as file: header_content = file.read()

        self.functions = {}

        header_content = '\n'.join(line for line in header_content.splitlines() if not line.strip().startswith('#'))

        func_pattern = re.compile(
            r"(?P<return_type>(?:[\w\*\s]+?))\s+"  # Return type (includes pointers and spaces)
            r"(?P<name>\w+)"                      # Function name
            r"\s*\((?P<params>[^)]*)\)"           # Parameter list
            r"\s*;"                               # End of declaration
        )

        param_pattern = re.compile(
            r"(?P<param_type>(?:const\s+)?[\w\*\s]+?)\s+(?P<param_name>\w+)"  # Parameter type (handles const and pointers)
        )

        matches = func_pattern.findall(header_content)

        for match in matches:
            return_type = match[0].strip()
            name = match[1]
            param_list = match[2]
            if name not in self.methods_to_include: continue

            params = []
            if param_list.strip():
                for param in param_list.split(','):
                    param_match = param_pattern.search(param.strip())
                    if param_match:
                        param_type = param_match.group('param_type').strip()
                        param_name = param_match.group('param_name').strip()
                        params.append((param_type, param_name))
            self.functions[name] = {
                    "return_type": return_type,
                    "params": params,
            }

        print(json.dumps(self.functions, indent=4))

    def generate_c_extention_functions(self):
        self.c_functions = []

        for func_name, details in self.functions.items():
            return_type = details["return_type"]
            params = details["params"]

            variable_declarations = []
            input_parsing = []
            c_arguments = []
            format_specifiers = []
            return_conversion = self.type_conversions.get(return_type, (None, None, None))[1]

            # Process each parameter
            for param_type, param_name in params:
                type_conversion = self.type_conversions.get(param_type)
                if not type_conversion: raise ValueError(f"Unsupported type: {param_type}")
                parse_func, _, specifier = type_conversion

                # Declare variables
                variable_declarations.append(f"{param_type} {param_name};")
                if parse_func: input_parsing.append(f"{param_name} = {parse_func}(args[{len(c_arguments)}]);")
                else: input_parsing.append(f"{param_type} {param_name}; /* Custom parsing may be needed */")
                c_arguments.append(param_name)
                format_specifiers.append(specifier)

            # Build PyArg_ParseTuple arguments
            if self.manual_parsing: parse_func = "\n    ".join(input_parsing)
            else:
                format_string = ''.join(format_specifiers)
                parse_arguments_code = f"""
    if (!PyArg_ParseTuple(args, "{format_string}", {", ".join(f"&{arg}" for arg in c_arguments)})) {{
        return NULL;
    }}
                """

            # Construct the function call
            if return_type == "void":
                function_call = f"{func_name}({', '.join(c_arguments)});"
                return_statement = "Py_RETURN_NONE;"
            else:
                function_call = f"{return_type} result = {func_name}({', '.join(c_arguments)});"
                if return_conversion: return_statement = f"return {return_conversion}(result);"
                else: return_statement = "return Py_None;"

            # Generate the function definition
            function_code = f"""
static PyObject* py_{func_name}(PyObject* self, PyObject* args) {{
    {''.join(variable_declarations).strip()}
    {parse_arguments_code.strip()}
    {function_call.strip()}
    {return_statement.strip()}
}}
            """
            print(function_code)
            self.c_functions.append(function_code)

    def generate_c_extension(self):
        method_table = ",\n     ".join([
            f'{{"{func_name}", py_{func_name}, METH_VARARGS, "Wrapper for {func_name}"}}'
            for func_name in self.functions.keys()
        ])
        self.c_extension_code = f"""
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "{os.path.basename(self.header_file)}"

{''.join(self.c_functions)}

static PyMethodDef module_methods[] = {{
    {method_table},
    {{NULL, NULL, 0, NULL}}
}};

static struct PyModuleDef moduledef = {{
    PyModuleDef_HEAD_INIT,
    "{self.output_name}",
    "Python C Extension",
    -1,
    module_methods
}};

PyMODINIT_FUNC PyInit_{self.output_name}(void) {{
    return PyModule_Create(&moduledef);
}}
        """
        print("="*30)
        print(self.c_extension_code)

    def save_extension_file(self): 
        with open(self.output_path + self.output_name + ".c", 'w') as file: file.write( self.c_extension_code)
