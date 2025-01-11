from wrapcco.core.tools import Extension
from setuptools import setup, find_packages

opslib = Extension(
        header_file="./OpsLibs.h", 
        source_file="./OpsLib.cpp",
        to_include=["Point", "calculateAverage"],
        output_name="opslib_extension",
        output_path="./",
        language="c++",
        extra_compile_args=['-std=c++11']
)
setup(
        name="opslib",
        version="0.1.0",
        description="Tool for basic ops",
        ext_modules=list(opslib),
)
