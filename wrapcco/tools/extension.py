from setuptools import Extension as stExtension
import numpy as np

"""
Usage:

    module = Extension(name='myextension',
                      sources=['myextension.cpp'],
                      include_dirs=[np.get_include()])

Where:
    - name: full name of the extension.
    - sources: list of source filenames, relative to the distribution root.
    - include_dirs: list of directories to search for C/C++ header files.

"""

class Extension:
    def __init__(self):
        pass
