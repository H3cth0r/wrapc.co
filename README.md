<div align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="/docs/logo_wrapc_light.svg">
        <img alt="wrapc.co logo" src="/docs/logo_wrapc_dark.svg" width="30%" height="30%">
    </picture>
</div>

---

# WrapC.co ⚡
Hey there! Welcome to **WrapC.co** – your new shortcut to turbocharged Python extensions! 🚀 Born from the fiery forge of developing [Statis.co](https://github.com/H3cth0r/statis.co), our bleeding-edge quantitative finance toolkit, WrapC.co is here to revolutionize how you build Python-C/C++ integrations.

When we first built Statis.co, we brute-forced our way through manual Python-C extensions and Numpy C API integrations. While it worked (and honestly, *crushed* Numpy-python in speed tests 💨), we quickly hit a wall. Endless boilerplate code, argument parsing gymnastics, and setup file headaches sucked the joy out of development. That's when we thought: *"There's gotta be a better way..."* ❄️

Enter **WrapC.co** – the developer experience upgrade you didn't know you needed. We automated the boring bits so you can focus on **writing killer C/C++ code** instead of wrestling with wrapper setup. Now you can seamlessly expose optimized numerical functions, process Numpy arrays at warp speed, and kiss 80% of that boilerplate junk goodbye 🗑️. Same native performance, 10x the developer zen. 🔮

## Installation
### Install from Source
```
git clone https://github.com/H3cth0r/wrapc.co
cd wrapc.co
pip install -e .
```

### Direct Install
```
python3 -m pip install git+https://github.com/H3cth0r/wrapc.co
```

## Documentation
### Requirements
- `Python>=3.9`.
- Extensions should be in `c++17`.
- MacOs and NixOs support.

### Numpy Superpowers 🏗️⚡
Want to crush array operations at C++ speed? Our `NumpyArrayRef` struct is your new best friend – think of it as a nitro boost for Numpy interop 🚀. Nestled in `wrapcco/resources/FunctionWrapper.hpp`, this bad boy gives you two killer features right out the gate:
- `array`: Your direct line to Numpy's array soul
- `owns_data`: Memory management on autopilot ✈️

Check this lightning-round example – we're adding scalars to arrays faster than you can say "zero-copy": 

```cpp
#include <numpy/arrayobject.h>
#include "FunctionWrapper"

NumpyArrayRef addNtoArr(const NumpyArrayRef& a, int nToAdd) {
    // Store array specs ⚙️
    const npy_intp size = a.size();
    double* a_data = a.data<double>();

    // Create output array lightning-fast 🌩️
    npy_intp dims[] = {size};
    PyObject* result_obj = PyArray_SimpleNew(1, dims, NPY_DOUBLE);
    auto* result_arr = reinterpret_cast<PyArrayObject*>(result_obj);
    double* result_data = static_cast<double*>(PyArray_DATA(result_arr));

    // Magic happens here 🎩✨
    for (npy_intp i = 0; i < size; ++i) {
        result_data[i] = a_data[i] + nToAdd;
    }

    return NumpyArrayRef(result_arr);  // Automatic memory VIP treatment 🎟️
}
```

You can even pass a array as reference and modify the array directly.
```cpp
void addScalarInPlace(NumpyArrayRef& arr_ref, int scalar) {
    if (arr_ref.dtype() != NPY_DOUBLE) {
        ...
    }
    
    double* data = arr_ref.data<double>();
    npy_intp size = arr_ref.size();
    
    #pragma omp parallel for
    for(npy_intp i = 0; i < size; ++i) {
        data[i] += scalar;
    }
}
```

Want to compile extensions like an absolute ninja? Grab our header directory with this one-liner:
```py
from wrapcco import get_fw_include
fw_dir = get_fw_include()  # Boom – instant C++ toolkit access 🔧
```

### Examples
For further testing examples, please check this directories:
- [x] Test Wrapper (`test/test_wrapper`)
- [x] Test Wrapper save files (`test/test_wrapper_files`)
- [x] Test Wrapper generate library (`test/test_wrapper_str_code`)
- [x] Test Wrapper generate library with files (`test/test_wrapper_str_code_file`)
- [x] Test Extension and Test Extension save files(`test/test_extension`)
- [x] Test Command Line (`test/test_command_line`)
- [x] Test Command Line save files (`test/test_command_line`)

### Command Line Usage
```sh
python -m wrapcco <library>.hpp --module-name <modulename> --save-script <true/false> --output-path "./"
```
- `<library>`: hpp file containing the library functions.
- `--module-name`: name or your output module executable.
- `--save-script`: choose if you want to generate the `cpp` extension file.

Get examples with
```sh
wrapcco --help-examples
```

## TODO
- Add Piping, to streamline functions
