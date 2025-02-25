from __future__ import annotations

from typing import List
import logging
import tempfile
import shutil
import re
import os
from wrapcco.core import _template

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
    def __init__(self, module_name: str, function_names: List[str], filepaths: List[str], tmp_dirs: List[str] | None = None):
        """
        Get the code to wrap
        """
        self.module_name    = module_name
        self.function_names = function_names 
        # self.filepaths      = [os.path.abspath(p) for p in filepaths]
        self.filepaths      = filepaths 
        self.filenames      = [ filename.split("/")[-1] for filename in filepaths]

        # track directories/files needing cleanup
        self.tmp_dirs       = tmp_dirs or []

        # paths for generated cpp files
        self.generated_cpps: List[str] = []

        print(self.filepaths)
        print(self.filenames)

    def __del__(self):
        for d in list(set(self.tmp_dirs)):
            try: shutil.rmtree(d)
            except Exception as e: logging.warning(f"Failed deleting {d}: {e}")

    def generate(self, output_path: str|None=None, save: bool=False) -> str:
        extension_file = self._generate_extension_file(self.module_name, self.filenames, self.function_names)

        if save == False:
            tmp_dir = tempfile.mkdtemp(prefix=f"{self.module_name}_ext_")
            os.makedirs(tmp_dir, exist_ok=True)
            out_cpp = os.path.join(tmp_dir, f"{self.module_name}.cpp")
            print(f"out_cpp: {out_cpp}")
            try:
                with open(out_cpp, 'w', encoding='utf-8') as f_out: f_out.write(extension_file)
                # logging.info(f"Saved temporal CPP at {out_cpp}")
                self.generated_cpps.append(out_cpp)
                self.tmp_dirs.append(os.path.dirname(out_cpp))
            except IOError as e:
                logging.error(f"Failed saving temporal CPP:{e}")
                raise
        else:
            if not output_path: raise ValueError("Must provide `output_path` when saving.")
            out_fp = os.path.join(output_path, f"{self.module_name}.cpp")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            try:
                with open(out_fp, 'w', encoding='utf-8') as f_out: f_out.write(extension_file)
                self.generated_cpps.append(out_fp)
            except IOError as e:
                logging.error(f"Failed saving temporal CPP:{e}")
                raise
        return extension_file

    # TODO build is done in Extension
    # def build(self): pass

    @classmethod
    def read_file(cls, module_name: str, filepaths: List[str])->Wrapper: 
        function_names = []
        if isinstance(filepaths, str): filepaths = [filepaths]
        for filepath in filepaths: function_names += cls._get_functions_from_file(filepath)
        print(function_names)
        return cls(module_name=module_name, function_names=function_names, filepaths=filepaths)

    @classmethod
    def read(cls, module_name: str, code: str, lib_output_dir: str | None=None, save_lib: bool=False)->Wrapper:
        content_lines = code.splitlines(True)
        try: function_names = cls._parse_function_names(content_lines)
        except Exception as e:
            logging.exception(f"Unexpected error occurred while parsing provided code")
            raise
        
        hdr_filename = f"{module_name}_library.hpp"
        fp_list = []
        tmps = []

        if save_lib:
            lib_outdir = lib_output_dir or os.getcwd()
            os.makedirs(lib_outdir, exist_ok=True)
            hdr_fullpath = os.path.join(lib_outdir, hdr_filename)
            with open(hdr_fullpath, 'w') as f_out: f_out.write(code)
            fp_list=[hdr_fullpath]
        else:
            tmp_dir = tempfile.mkdtemp(prefix=f"{module_name}_lib_")
            tmps.append(tmp_dir)
            hdr_fullpath=os.path.join(tmp_dir, hdr_filename)
            with open(hdr_fullpath, 'w') as f_out: f_out.write(code)
            fp_list=[hdr_fullpath]

        return cls(module_name=module_name, function_names=function_names, filepaths=fp_list, tmp_dirs=tmps)

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
