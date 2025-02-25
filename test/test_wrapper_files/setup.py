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

