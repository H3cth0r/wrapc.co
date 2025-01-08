from wrapcco import Wrapper

wrapper = Wrapper(
        header_file="./Human.h", 
        source_file="./Human.cpp",
        to_include=["Human"],
        output_name="human_extension",
        output_path="./",
        language="c++",
)
wrapper.generate()
# print(wrapper.wrapper.program)
