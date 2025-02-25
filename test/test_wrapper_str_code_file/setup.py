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

