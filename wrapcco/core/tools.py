from setuptools import Extension as stExtension
from typing import List
import os

from wrapcco.core.wrapper import Wrapper

class Extension(Wrapper):
    def __init__(self, header_file: str, source_file: str, to_include: List[str], output_name: str, module_name: str="", output_path: str="./", language: str="c++", *args, **kwargs):
        super().__init__(header_file, source_file, to_include, output_name, output_path, language)
        self.extension = None
        self.module_name = module_name
        self.extra_args = args
        self.extra_kwargs = kwargs
    def _generate_extension(self) -> None:
        self.generate()
        extension_lang = ".cpp" if self.language == "c++" else ".c"
        self.extension = stExtension(
            self.module_name + self.output_name,
            sources=[
                os.path.join(self.output_path, self.output_name+extension_lang),
                self.source_file
            ],
            language=self.language,
            *self.extra_args,
            **self.extra_kwargs
        )
    def __iter__(self) -> stExtension:
        if not self.extension: self._generate_extension()
        return iter([self.extension])
