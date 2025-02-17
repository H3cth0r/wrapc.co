from setuptools import setup, Extension
import numpy as np
from extension_template import extract_function_names, generate_extension

module_name = "fast_cpp_caller"
write_to_file = lambda file_path, content: open(file_path, 'w').write(content)

method_test = extract_function_names("./my_library.hpp") 
generated_extension = generate_extension(module_name, "my_library.hpp", method_test)
write_to_file("./extension.cpp", generated_extension)

module = Extension('fast_cpp_caller',
                  sources=['extension.cpp'],
                  include_dirs=[np.get_include()],
                  extra_compile_args=['-std=c++17'])

setup(name='fast_cpp_caller',
      version='1.0',
      ext_modules=[module])
