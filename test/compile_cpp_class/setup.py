from setuptools import setup, Extension

module = Extension(
    'example',
    sources=['thirdExample.cpp', 'ThirdImpl.cpp'],
    language='c++',
    extra_compile_args=['-std=c++11']  # Enable C++11 for string support
)

setup(
    name='example',
    version='1.0',
    description='Example module with multiple C++ classes',
    ext_modules=[module]
)

