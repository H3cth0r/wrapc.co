<div align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="/docs/logo_wrapc_light.svg">
        <img alt="wrapc.co logo" src="/docs/logo_wrapc_dark.svg" width="30%" height="30%">
    </picture>
</div>

---

Python Library to Wrap C code to python extensions

### Install from source
```
pip install -e .
```

### Basic usage


```
python -m wrapcco header.h source.c output_name
# or
wrapcco header.h source.c output_name
```

```
# Using python -m
python -m wrapcco header.h source.c output_name --methods function1 function2 function3

# Using the installed command
wrapcco header.h source.c output_name --methods function1 function2 function3
```

Or:
```
wrapcco --help-examples
```

### To Distribute
```
pip install build twine
python -m build
twine upload dist/*
```

## TODO
- Fix wrapper generator
    - There are syntax errors stile.
    - add functions wrapping
    - Add a default constructor when class has no constructor.
    - Fix typing, to manage spaces between pointers and references.
- Create C grammar wrapper


## NOTES
Don't forget that this the setup file should also include
the implementation.

**Important build commands**
```
python setup.py build_ext --inplace
```

Generate walkers
```
antlr4 -Dlanguage=Python3 *.g4 -visitor -o ../walkers/
```

NEW Structure
```
wrapcco/
├── wrapcco/
│   ├── __init__.py             # Initialize the module, handle imports
│   ├── core/
│   │   ├── __init__.py         # Core module initialization
│   │   ├── wrapper.py          # General wrapper class and logic
│   │   ├── utils.py            # Utility functions for common tasks
│   ├── parsers/
│   │   ├── __init__.py         # Parser module initialization
│   │   ├── base_parser.py      # Common parser logic
│   │   ├── c_parser.py         # C-specific parser logic
│   │   ├── cpp_parser.py       # C++-specific parser logic
│   ├── grammars/               # ANTLR grammar files
│   │   ├── C.g4               # ANTLR grammar for C
│   │   ├── CPP.g4             # ANTLR grammar for C++
│   ├── walkers/
│   │   ├── __init__.py         # Walkers module initialization
│   │   ├── base_walker.py      # Base walker for traversing parse trees
│   │   ├── c_walker.py         # C-specific walker logic
│   │   ├── cpp_walker.py       # C++-specific walker logic
│   ├── listeners/
│   │   ├── __init__.py         # Listeners module initialization
│   │   ├── base_listener.py    # Base listener for ANTLR
│   │   ├── c_listener.py       # C-specific listener logic
│   │   ├── cpp_listener.py     # C++-specific listener logic
│   ├── output/                 # Directory for generated Python extensions
│       └── (empty)             # Empty, for dynamically created files
├── tests/
│   ├── __init__.py             # Initialize tests
│   ├── test_wrapper.py         # Tests for the general wrapper
│   ├── test_parsers.py         # Tests for parsers
│   ├── test_walkers.py         # Tests for walkers
│   ├── test_listeners.py       # Tests for listeners
├── examples/
│   ├── example_c.c             # Example C code to wrap
│   ├── example_cpp.cpp         # Example C++ code to wrap
├── README.md                   # Documentation for the module
├── setup.py                    # Packaging and installation
├── pyproject.toml              # Build system configuration
├── requirements.txt            # Dependencies list
└── .gitignore                  # Git ignore file
```
