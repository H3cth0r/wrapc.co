from wrapcco import Wrapper

if __name__ == "__main__":
    # wrapper = Wrapper.read_file(
    #         module_name="testmodule",
    #         filepaths=["./my_library.hpp", "./my_second.hpp"],
    # )
    # print(type(wrapper))
    #
    # wrapper.generate("./", True)

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
