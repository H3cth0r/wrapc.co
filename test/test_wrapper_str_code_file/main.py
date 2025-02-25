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
            lib_output_dir="./output/includir",
            save_lib=True
    )
    print(type(wrapper))

    output = wrapper.generate("./output", True)
    print(output)
