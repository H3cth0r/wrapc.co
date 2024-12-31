from wrapcco.core.tools import Extension
from setuptools import setup, find_packages

human_extension = Extension(
        header_file="./Human.h", 
        source_file="./Human.cpp",
        to_include=["Human"],
        output_name="human_extension",
        output_path="./",
        language="c++",
        extra_compile_args=['-std=c++11']
)
setup(
        name="human",
        version="0.1.0",
        description="Tool to parse Markdown to HTML.",
        ext_modules=list(human_extension),
)
