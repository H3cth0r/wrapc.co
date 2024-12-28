from wrapcco import Wrapper

wrapper = Wrapper("./Human.h", ["Human"])
print(wrapper.wrapper.program)
