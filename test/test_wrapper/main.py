from wrapcco import Wrapper

if __name__ == "__main__":
    wrapper = Wrapper.read_file(
            module_name="testmodule",
            filepaths=["./my_library.hpp", "./my_second.hpp"],
    )
    print(type(wrapper))

    wrapper.generate_files("./", True)
