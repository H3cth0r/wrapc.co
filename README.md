<div align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="/docs/logo_wrapc_light.svg">
        <img alt="wrapc.co logo" src="/docs/logo_wrapc_dark.svg" width="30%" height="30%">
    </picture>
</div>

---

Python Library to Wrap C code to python extensions

## TODO
- Create `Extension` method (as setuptools).
- Enable generate extension as command line command.
- Add Piping, to streamline functions

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
