from wrapcco.tools import Extension
from setuptools import setup, find_packages
# import time

extension = Extension(
        module_name="testmod.mathfunc",
        filepaths="./testmod/my_library.hpp",
        output_path="./testmod/",
        extra_compile_args=['-std=c++17'],
)
# extension.build()
# time.sleep(20)

setup(
        name="testmod",
        version="0.1.0",
        packages=find_packages(),
        author="h3cth0r",
        author_email="hector.miranda@zentinel.mx",
        description="Test tool with calc",
        ext_modules=list(extension),
) 
