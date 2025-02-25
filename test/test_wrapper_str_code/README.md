# Test Wrapper read python string lib

## Procedure
1. Write code: `save_lib` will enable generate library file.
```py
from wrapcco import Wrapper

if __name__ == "__main__":
    input_code = '''
#pragma once
int addInts(int a, int b) {
    return a + b;
}

inline int addMoreInts(int a, int b, int c) {
    return a + b + c;
}
    '''

    wrapper = Wrapper.read(
            module_name="testmodule",
            code=input_code,
            lib_output_dir="./",
            save_lib=True
    )
    print(type(wrapper))

    output = wrapper.generate("./", False)
    print(output)
```
2. Execute `python main.py`. Will generate library file and show extension string.
