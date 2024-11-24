import re
import os
from typing import List, Dict, Any 
import subprocess

class CExtensionGenerator:
    def __init__(self, header_file: str, source_file: str, methods_to_include: List[str]):
        self.header_file = header_file
        self.source_file = source_file
        self.methods_to_include = methods_to_include
        self.function_signatures = {}
        self.type_conversions = {
            'int': ('PyLong_AsLong', 'PyLong_FromLong', 'i'),
            'char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'size_t': ('PyLong_AsSize_t', 'PyLong_FromSize_t', 'n'),
            'uint8_t*': ('PyBytes_AsString', 'PyBytes_FromString', 's'),
            'const char*': ('PyUnicode_AsUTF8', 'PyUnicode_FromString', 's'),
            'FILE*': (None, None, 'O'),  # Special handling required
        }
    def parse_header(self) -> None:
        """ parse the header file to extract function signatures """
        with open(self.header_file, 'r') as f: content = f.read()

        pattern = r'(\w+[\s*]+\w+\s*\([^)]*\))\s*;'
        matches = re.finditer(pattern, content)

        for match in matches:
            func_decl = match.group(1)
            if any(method in func_decl for method in self.methods_to_include):
                self._parse_function_signature(func_decl)

    def _parse_function_signature(self, signature: str) -> None:
        """ parse individual function signature to extract return type and parameters. """
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
                'parameters': params,
        }
    def generate_wrapper_function(self, func_name, str) -> str:
        """ generate python c api wrapper function for a c function """
        sig = self.function_signatures[func_name]
        params = sig['parameters']

        wrapper = f"""
        """
