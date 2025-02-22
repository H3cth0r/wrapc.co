from typing import List
import logging
import re
import _template

"""
Wrapper will read either a file or string(code), parse available 
functions and generate the output code.
- Save generated code.
- Build.

Usage:
    # Read from file
    wrapper = Wrapper.read_file(name="myextension", filepaths="mylibrary.hpp")
    wrapper.generate(build=true, save_output=true)
    # OR
    wrapper.generate_files()
    wrapper.build_inplace()


    # Read from list of files 
    wrapper = Wrapper.read_file(name="myextension", filepaths=["mylibrary.hpp", "anotherlib.hpp"])
    wrapper.generate()

    # Read from string
    wrapper = Wrapper.read(code="...")
"""

class Wrapper:
    def __init__(self, module_name: str, function_names: List[str], filepaths: List[str]):
        """
        Get the code to wrap
        """
        pass

    def generate(self): pass
    def generate_files(self): pass
    def build(self): pass

    @classmethod
    def read_file(cls, name: str, filepaths: List[str])->Wrapper: 
        loaded_functions = []
        if isinstance(filepaths, str): filepaths = [filepaths]
        for filepath in filepaths: loaded_functions += cls._get_functions_from_file(filepath)

    @classmethod
    def read(cls): pass

    @staticmethod
    def _load_file_content(filepath: str)->List[str]:
        try:
            with open(filepath, 'r') as file: return file.readlines()
        except FileNotFoundError as e: 
            logging.error(f"File '{filepath}' not found.", exc_info=True)
            raise
        except PermissionError as e: 
            logging.critical(f"Insufficient permissions to read '{file_path}'. Error: {e}")
            raise
        except Exception as e: 
            logging.exception(f"Unexpected error occurred when processing '{file_path}'")
            raise

    @staticmethod
    def _parse_function_names(lines: List[str])->List[str]:
        function_pattern = re.compile(r'^[\s]*(?:inline\s+)?[a-zA-Z_][a-zA-Z0-9_:<>]*\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*\{')
        function_names = []
        for line in lines:
            match = function_pattern.match(line)
            if match: function_names.append(match.group(1))
        return function_names

    @staticmethod
    def _get_functions_from_file(filepath: str) -> List[str]:
        content = Wrapper._load_file_content(filepath)

        try: return Wrapper._parse_function_names(content)
        except Exception as e:
            logging.exception(f"Unexpected error occurred while parsing '{filepath}'")
            raise

    @staticmethod
    def _generate_extension_file(module_name: str, library_file_names: List[str], function_names: List[str]):
        output =    _template.headers(library_file_names)
        output +=   _template.register_handlers 
        output +=   _template.execute_f
        output +=   _template.template_methods(function_names)
        output +=   _template.methods_def(function_names)
        output +=   _template.module_def(module_name)
        output +=   _template.init_module(module_name, function_names)
        return output
