import re
import os
from typing import List

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

    def parse_header(self) -> None:
        function_pattern = re.compile(
            r"""
            ^\s*                                 # Optional leading whitespace
            ([\w\s\*&]+?)                        # Return type (including pointers and references)
            \s+                                  # Whitespace before function name
            (\w+)                                # Function name
            \s*                                  # Optional whitespace
            \(\s*                                # Opening parenthesis with optional whitespace
            ([^)]*)                              # Parameter list (everything up to closing parenthesis)
            \s*\)\s*;                            # Closing parenthesis and semicolon
            """, re.VERBOSE | re.MULTILINE
        )
        param_pattern = re.compile(
            r"""
            ([\w\s\*&]+)                         # Parameter type (including pointers and references)
            \s+                                  # Whitespace
            (\w+)                                # Parameter name
            """, re.VERBOSE
        )
