
# old code

import re
import os
from typing import List, Dict, Any

class CExtensionGenerator:
    def __init__(self, header_file: str, source_file: str, methods_to_include: List[str], output_path: str="./"):
        self.header_file = header_file
        self.source_file = source_file
        self.methods_to_include = methods_to_include
        self.function_signatures = {}
        self.type_conversions = {
            'int': ('PyLong_AsLong', 'PyLong_FromLong', 'i'),
            'char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'size_t': ('PyLong_AsSize_t', 'PyLong_FromSize_t', 'n'),
            'uint8_t*': ('PyBytes_AsString', 'PyBytes_FromStringAndSize', 'y#'),
            'const char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'FILE*': (None, None, 'O'),  # Special handling required
            'void': (None, None, None)  # Special handling for void return type
        }
        self.output_path = output_path 

    def parse_header(self) -> None:
        with open(self.header_file, 'r') as f:
            content = f.read()

        # Improved pattern to handle function declarations
        pattern = r'(?:extern\s+)?([a-zA-Z_][a-zA-Z0-9_*\s]+?\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\))\s*;'
        matches = re.finditer(pattern, content)

        for match in matches:
            func_decl = match.group(1)
            if any(method in func_decl for method in self.methods_to_include):
                self._parse_function_signature(func_decl)

    def _parse_function_signature(self, signature: str) -> None:
        parts = signature.split('(')
        ret_and_name = parts[0].strip().split()
        func_name = ret_and_name[-1]
        return_type = ' '.join(ret_and_name[:-1])

        params_str = parts[1].replace(')', '').strip()
        params = []
        if params_str and params_str != 'void':
            for param in params_str.split(','):
                param_parts = param.strip().split()
                param_name = param_parts[-1]
                param_type = ' '.join(param_parts[:-1])
                params.append((param_type, param_name))
        
        self.function_signatures[func_name] = {
            'return_type': return_type,
            'parameters': params
        }

    def _generate_file_handling(self, param_name: str, mode: str = "r") -> str:
        return f"""
    FILE* {param_name}_file = NULL;
    if (PyUnicode_Check({param_name})) {{
        const char* filename = PyUnicode_AsUTF8({param_name});
        {param_name}_file = fopen(filename, "{mode}");
        if (!{param_name}_file) {{
            PyErr_SetString(PyExc_IOError, "Could not open file");
            return NULL;
        }}
    }} else {{
        PyErr_SetString(PyExc_TypeError, "Expected string for filename");
        return NULL;
    }}"""

    def generate_wrapper_function(self, func_name: str) -> str:
        sig = self.function_signatures[func_name]
        params = sig['parameters']
        return_type = sig['return_type']

        # Generate parameter declarations
        param_decls = []
        format_parts = []
        parse_args = []
        
        for param_type, param_name in params:
            if param_type == 'FILE*':
                param_decls.append(f"PyObject* {param_name};")
            elif param_type == 'uint8_t*':
                param_decls.append(f"Py_buffer {param_name}_view;")
                format_parts.append("y*")
                parse_args.append(f"&{param_name}_view")
            else:
                param_decls.append(f"{param_type} {param_name};")
                _, _, format_spec = self.type_conversions.get(param_type, (None, None, 'O'))
                format_parts.append(format_spec)
                parse_args.append(f"&{param_name}")

        # Generate wrapper function
        wrapper = f"""
static PyObject* {func_name}_wrapper(PyObject* self, PyObject* args) {{
    {"    ".join(param_decls)}
    
    if (!PyArg_ParseTuple(args, "{''.join(format_parts)}", {', '.join(parse_args)})) {{
        return NULL;
    }}
"""

        # Add FILE* handling if needed
        file_cleanup = []
        call_args = []
        for param_type, param_name in params:
            if param_type == 'FILE*':
                wrapper += self._generate_file_handling(param_name)
                call_args.append(f"{param_name}_file")
                file_cleanup.append(f"{param_name}_file")
            elif param_type == 'uint8_t*':
                call_args.append(f"{param_name}_view.buf")
            else:
                call_args.append(param_name)

        # Generate function call and return handling
        if return_type == 'void':
            wrapper += f"\n    {func_name}({', '.join(call_args)});\n"
        else:
            wrapper += f"\n    {return_type} result = {func_name}({', '.join(call_args)});\n"

        # Add cleanup
        for file_ptr in file_cleanup:
            wrapper += f"\n    if ({file_ptr}) {{ fclose({file_ptr}); }}"
        
        # Handle return value
        if return_type == 'void':
            wrapper += "\n    Py_RETURN_NONE;"
        elif return_type in self.type_conversions:
            _, to_python, _ = self.type_conversions[return_type]
            if to_python:
                wrapper += f"\n    return {to_python}(result);"
            else:
                wrapper += "\n    Py_RETURN_NONE;"

        wrapper += "\n}"
        return wrapper

    def generate_extension_file(self, output_file: str) -> None:
        method_defs = []
        wrapper_functions = []

        for func_name in self.methods_to_include:
            if func_name in self.function_signatures:
                wrapper_functions.append(self.generate_wrapper_function(func_name))
                method_defs.append(
                    f'    {{"{func_name}", {func_name}_wrapper, METH_VARARGS, '
                    f'"Python wrapper for {func_name}"}},'
                )

        extension_code = f"""#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "{os.path.basename(self.header_file)}"
#include "{os.path.basename(self.source_file)}"

{os.linesep.join(wrapper_functions)}

static PyMethodDef ModuleMethods[] = {{
{os.linesep.join(method_defs)}
    {{NULL, NULL, 0, NULL}}
}};

static struct PyModuleDef moduledef = {{
    PyModuleDef_HEAD_INIT,
    "markdown_extension",
    NULL,
    -1,
    ModuleMethods
}};

PyMODINIT_FUNC PyInit_markdown_extension(void) {{
    return PyModule_Create(&moduledef);
}}"""

        with open(self.output_path + output_file, 'w') as f:
            f.write(extension_code)

def create_extension(header_file: str, source_file: str, methods: List[str], module_name: str, output_path: str="./") -> None:
    """Create a Python C extension from C source and header files."""
    generator = CExtensionGenerator(header_file, source_file, methods, output_path=output_path)
    generator.parse_header()
    generator.generate_extension_file(f"{module_name}_wrapper.c")
