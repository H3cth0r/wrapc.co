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
- Add a default constructor when class has no constructor.
- Create C grammar wrapper
- Add support for arrays for params and return types.
- Add support for numpy arrays

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

## Current Structure
```
tree -I 'venv|wrapcco\.egg-info|build|__pycache__|*.so'
.
├── docs
│   ├── logo_wrapc_dark.svg
│   ├── logo_wrapc_light.svg
│   └── README.md
├── LICENSE
├── README.md
├── setup.py
├── shell.nix
├── test
│   ├── antlr_parser
│   │   ├── my_cpp_pars
│   │   │   ├── examples
│   │   │   │   ├── test_1.h
│   │   │   │   └── test_2.h
│   │   │   ├── grammars
│   │   │   │   ├── CPP14.g4
│   │   │   │   ├── CPP14Lexer.g4
│   │   │   │   └── CPP14Parser.g4
│   │   │   ├── main.py
│   │   │   ├── MyCppListener.py
│   │   │   └── walkers
│   │   │       ├── CPP14.interp
│   │   │       ├── CPP14Lexer.interp
│   │   │       ├── CPP14Lexer.py
│   │   │       ├── CPP14Lexer.tokens
│   │   │       ├── CPP14Listener.py
│   │   │       ├── CPP14Parser.py
│   │   │       ├── CPP14.tokens
│   │   │       └── CPP14Visitor.py
│   │   └── shell.nix
│   ├── compile_cpp_class
│   │   ├── example.cpp
│   │   ├── example_header.h
│   │   ├── secondExample.cpp
│   │   ├── setup.py
│   │   ├── ThirdDefs.h
│   │   ├── thirdExample.cpp
│   │   └── ThirdImpl.cpp
│   ├── cpp_class
│   │   ├── Human.cpp
│   │   ├── human_extension.cpp
│   │   ├── Human.h
│   │   ├── setup.py
│   │   ├── test_output.py
│   │   └── wrap.py
│   └── cpp_class_n_method
│       ├── OpsLib.cpp
│       ├── opslib_extension.cpp
│       ├── OpsLibs.h
│       └── setup.py
├── test.py
└── wrapcco
    ├── core
    │   ├── __init__.py
    │   ├── tools.py
    │   ├── utils.py
    │   └── wrapper.py
    ├── grammars
    │   └── CPP.g4
    ├── __init__.py
    ├── listeners
    │   ├── cpp_listener.py
    │   └── __init__.py
    ├── walkers
    │   ├── CPP14Lexer.interp
    │   ├── CPP14Lexer.py
    │   ├── CPP14Lexer.tokens
    │   ├── CPP.interp
    │   ├── CPPLexer.interp
    │   ├── CPPLexer.py
    │   ├── CPPLexer.tokens
    │   ├── CPPListener.py
    │   ├── CPPParser.py
    │   ├── CPP.tokens
    │   ├── CPPVisitor.py
    │   └── __init__.py
    └── wrappers
        ├── cpp_wrapper.py
        └── __init__.py

17 directories, 63 files
```

## NEW Structure
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
