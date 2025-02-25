# Test Extension class with no generation of extension file

This test demonstrates compilation of Extension from a library file, without saving the extension `cpp` file.
In case want to save the extension file, just change the `save` argument to true.

## Procedure
1. Write setup file:
```py
from wrapcco.tools import Extension
from setuptools import setup, find_packages

extension = Extension(
        module_name="testmod.mathfunc",
        filepaths="./testmod/my_library.hpp",
        save=False,
        output_path="./testmod/",
        extra_compile_args=['-std=c++17'],
)

setup(
        name="testmod",
        version="0.1.0",
        packages=find_packages(),
        author="h3cth0r",
        author_email="hector.miranda@zentinel.mx",
        description="Test tool with calc",
        ext_modules=list(extension),
) 
```
2. Execute setup file `python setup.py build_ext --inplace`.
3. `.so` will be generated with `None` extension `cpp` file, just by using the library.
