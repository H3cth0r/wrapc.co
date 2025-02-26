# Testing command line compile

The intentantion of this test is to showcase how to compile or generate output from command line.

## Basic Usage:
```py
python -m wrapcco <library>.hpp --module-name <modulename> --save-script <true/false> --output-path "./"
```

## Procedure
1. Compile not saving `cpp`
```
wrapcco my_library.hpp --module-name mymodtest
```
2. Reset directory:
```
rm -r build/
rm mymodtest.*
```
3. Compile saving `cpp`.
```
wrapcco my_library.hpp --module-name output.mymodtest --save-script true --output-path ./output/
```
