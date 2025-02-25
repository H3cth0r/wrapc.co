# Test Wrapper class generating extension file to path

This test is intended to demonstrate that the Wrapper class works correctly, by 
generating extension string and saving to output extension file.

## Procedure
1. Write code:
```py
wrapper = Wrapper.read_file(
        module_name="testmodule",
        filepaths=["./my_library.hpp", "./my_second.hpp"],
)
print(type(wrapper))
output = wrapper.generate("./output", True)
print(output)
```
2. Exexute main script: this generates and saves the extension file: ` python main.py `.
3. Create setup file:
```py
from setuptools import setup, Extension
import numpy as np
from wrapcco import get_fw_include

module = Extension(
    'output.testmodule',
    sources=['./output/testmodule.cpp'],
    include_dirs=[
        './',
        np.get_include(), 
        get_fw_include(), 
    ],
    language='c++',
    extra_compile_args=['-std=c++17']  # Enable C++11 for string support
)

setup(
    name='example',
    version='1.0',
    description='Example module with multiple C++ classes',
    ext_modules=[module]
)
```
4. Run `python setup.py build_ext --inplace`
5. Run test to test correct.
