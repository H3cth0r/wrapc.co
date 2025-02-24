from __future__ import annotations

from wrapcco import Wrapper
from setuptools import Extension as stExtension
from pathlib import Path
import numpy as np

"""
Usage:

    module = Extension(name='myextension',
                      sources=['myextension.cpp'],
                      include_dirs=[np.get_include()])

Where:
    - name: full name of the extension.
    - sources: list of source filenames, relative to the distribution root.
    - include_dirs: list of directories to search for C/C++ header files.

"""

class Extension(Wrapper):
    def __init__(self, module_name: str, filepaths: List[str], output_path: str, *args, **kwargs):
        wrapper = Wrapper.read_file(module_name, filepaths)
        super().__init__(
                module_name=wrapper.module_name,
                function_names=wrapper.function_names,
                filepaths=wrapper.filepaths,
                tmp_dirs=wrapper.tmp_dirs,
        )
        self.output_path = output_path
        self.extra_args = args
        self.extra_kwargs = kwargs
        self.extension = None
    def build(self): 
        print("Building")
        self.generate(self.output_path)
        print(self.generated_cpps[0])

        import wrapcco
        resources_dir = Path(wrapcco.__file__).parent / 'resources'
        header_dirs = [np.get_include(), str(resources_dir)] + [str(Path(fp).resolve().parent) for fp in self.filepaths]
        print(f"header_dirs: {header_dirs}")

        self.extension = stExtension(
            self.module_name,
            sources=[
                self.generated_cpps[0],
            ],
            include_dirs=header_dirs,
            *self.extra_args,
            **self.extra_kwargs,
        )

    def __iter__(self) -> stExtension: 
        if not self.extension: self.build()
        return iter([self.extension])
