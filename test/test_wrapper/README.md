# Test Wrapper class with no generated file

This test is intended to demonstrate that the Wrapper class works correctly. It reads the library files(files with actual functions).
Generate fucntion returns output extension file.

## Procedure
1. Write code:
```py
wrapper = Wrapper.read_file(
        module_name="testmodule",
        filepaths=["./my_library.hpp", "./my_second.hpp"],
)
print(type(wrapper))
output = wrapper.generate("./", False)
print(output)
```
2. Execute main script: `python main.py`
