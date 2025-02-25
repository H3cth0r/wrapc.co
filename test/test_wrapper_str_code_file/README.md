# Test Wrapper read python string lib and generate extension

## Procedure
1. Write code:
```py
from wrapcco import Wrapper

if __name__ == "__main__":
    input_code = '''
#pragma once
int addInts(int a, int b) {
    return a + b;
}

inline int addMoreInts(int a, int b, int c) {
    return a + b + c;
}
    '''

    wrapper = Wrapper.read(
            module_name="testmodule",
            code=input_code,
            lib_output_dir="./output/includir",
            save_lib=True
    )
    print(type(wrapper))

    output = wrapper.generate("./output", True)
    print(output)
```
2. Execute `main.py` script: this generates and saves library and then saves the extension file.
3. Create setup file:
```py
from setuptools import setup, Extension
import numpy as np
import wrapcco as wo

module = Extension(
    'output.testmodule',
    sources=['./output/testmodule.cpp'],
    include_dirs=[
        './output/includir/',
        np.get_include(), 
        wo.get_fw_include(), 
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
