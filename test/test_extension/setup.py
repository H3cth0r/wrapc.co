from wrapcco.tools import Extension
import time

if __name__ == "__main__":
    extension = Extension(
            module_name="mathfunc",
            filepaths="./testmod/my_library.hpp",
            output_path="./testmod/",
            extra_compile_args=["-std=c99"],
    )
    extension.build()
    time.sleep(20)
