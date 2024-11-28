# wrapc.co
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
