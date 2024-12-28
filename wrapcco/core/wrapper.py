from wrapcco.wrappers.cpp_wrapper import ParserHandlerCpp, CppWrapper

class Wrapper:
    def __init__(self, def_path, to_parse=[], lang="cpp"):
        self.def_path = def_path
        if "cpp" in lang:
            self.parserHandler = ParserHandlerCpp(def_path)
            self.wrapper = CppWrapper(self.parserHandler.program, to_parse)
        else: print("lang not supported")
        self.wrapper.generate()
        print(self.wrapper.output)
