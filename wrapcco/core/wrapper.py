from wrapcco.wrappers.cpp_wrapper import ParserHandlerCpp, CppWrapper
from typing import List
import logging

class Wrapper:
    def __init__(self, header_file: str, source_file: str, to_include: List[str], output_name: str, output_path: str="./", language: str="c++"):
        self.header_file = header_file
        self.source_file = source_file
        self.to_include = to_include
        self.output_name =  output_name
        self.language = language 
        self.output_path = output_path
    def _save_extension_file(self) -> None:
        extension_lang = ".cpp" if self.language == "c++" else ".c"
        with open(self.output_path + self.output_name + extension_lang, "w") as file: file.write(self.wrapper.output)
    def generate(self) -> None:
        if "c++" in self.language:
            self.parserHandler = ParserHandlerCpp(self.header_file)
            self.wrapper = CppWrapper(self.parserHandler.program, self.parserHandler.filePath, self.output_name, self.to_include)
        else: logging.error("Language not supported")
        self.wrapper.generate()
        self._save_extension_file()
        print(self.wrapper.output)
