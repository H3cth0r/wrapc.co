from typing import List
from .wrapper import Wrapper
from setuptools import Extension as stExtension
import os

def wrapcco_setup(wrappers: List[Wrapper]) -> None:
    for wrapper in wrappers: wrapper.generate()

# Don't forget to add a function to "clean --all"

# class setuptools.Extension(name: str, sources: list[str | PathLike[str]], *args, py_limited_api: bool = False, **kw)

class Extension(Wrapper):
    def __init__(self, header_file: str, source_file: str, methods_to_include: List[str], output_name: str, module_name: str="", output_path: str = "./", *args, **kwargs):
        super().__init__(header_file, source_file, methods_to_include, output_name, output_path)
        self.extension = None 
        self.module_name = module_name
        self.extra_args = args 
        self.extra_kwargs = kwargs 
    def _generate_extension(self):
        self.generate()

        self.extension = stExtension(
            self.module_name + self.output_name, 
            sources=[
                os.path.join(self.output_path, self.output_name + ".c"),
                self.source_file
            ],
            *self.extra_args,
            **self.extra_kwargs
        )
    def __iter__(self):
        if not self.extension: self._generate_extension()
        return iter([self.extension])
