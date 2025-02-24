headers = lambda library_files: '''
#define PY_SSIZE_T_CLEAN
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <unordered_map>
#include <functional>
#include <vector>
#include <memory>
#include <numeric>
#include <cstring>
#include "FunctionWrapper.hpp"
<library-paths>
'''.replace('<library-paths>', ''.join([f'#include "{lbf}"\n' for lbf in library_files]))

register_handlers = '''
// global registry to store functions
static std::unordered_map<std::string, std::unique_ptr<FunctionWrapperBase>> function_registry;

// function to register C++ functions
template<typename Ret, typename... Args>
void register_function(const std::string& name, Ret(*func)(Args...)) {
    function_registry[name] = std::make_unique<FunctionWrapper<Ret, Args...>>(func);
}
'''

execute_f = '''
// python-callable function to execute registered functions
static PyObject* execute_function(PyObject* self, PyObject* args) {
    const char* func_name;
    PyObject* func_args;

    if (!PyArg_ParseTuple(args, "sO", &func_name, &func_args)) {
        return nullptr;
    }

    auto it = function_registry.find(func_name);
    if (it == function_registry.end()) {
        PyErr_SetString(PyExc_RuntimeError, "Function not found");
        return nullptr;
    }

    return it->second->execute(func_args);
}
'''

template_method = lambda meth_name: '''
static PyObject* <meth-name>F(PyObject* self, PyObject* args) {
    // Get the number of arguments passed
    Py_ssize_t nargs = PyTuple_Size(args);
    
    // Create a new tuple with the actual arguments
    // Note: we dont need to include the function name since its hardcoded
    PyObject* func_args = PyTuple_New(nargs);
    if (!func_args) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to create arguments tuple");
        return nullptr;
    }
    
    // Copy all arguments to the new tuple
    for (Py_ssize_t i = 0; i < nargs; i++) {
        PyObject* item = PyTuple_GetItem(args, i);
        Py_INCREF(item);  // Increment reference count since PyTuple_SetItem steals the reference
        PyTuple_SetItem(func_args, i, item);
    }
    
    // Find and execute the function
    auto it = function_registry.find("<meth-name>");
    if (it == function_registry.end()) {
        Py_DECREF(func_args);
        PyErr_SetString(PyExc_RuntimeError, "Function not found");
        return nullptr;
    }
    
    // Execute the function and clean up
    PyObject* result = it->second->execute(func_args);
    Py_DECREF(func_args);
    return result;
}
'''.replace("<meth-name>", meth_name)
template_methods = lambda method_names: "".join(template_method(meth_name) for meth_name in method_names)

method_def_list = lambda method_names: "\n".join([
        '\t{"<meth-name>", <meth-name>F, METH_VARARGS, "<meth-name> function"},'.replace("<meth-name>", meth_name)
        for meth_name in method_names
])
methods_def = lambda method_names: '''
// module method definitions
static PyMethodDef ModuleMethods[] = {
        {"execute_function", execute_function, METH_VARARGS, "Execute a registered function"},
<method-defs> 
        {nullptr, nullptr, 0, nullptr}
};
'''.replace("<method-defs>", method_def_list(method_names))

module_def = lambda module_name: '''
// module definition structure
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "<module-name>",
    "<module-name> module",
    -1,
    ModuleMethods
};
'''.replace("<module-name>", module_name)

register_functions_f = lambda method_names: "\n".join([f'\tregister_function("{meth_name}", {meth_name});' for meth_name in method_names])
init_module = lambda module_name, method_names: '''
// module initialization function
PyMODINIT_FUNC PyInit_<module-name>(void) {
    import_array();  // initialize NumPy

    PyObject* module = PyModule_Create(&moduledef);
    if (!module) {
        return nullptr;
    }

    // Register all functions during module initialization
    try {
<register-functions>
    } catch (const std::exception& e) {
        PyErr_SetString(PyExc_RuntimeError, 
            ("Failed to register functions: " + std::string(e.what())).c_str());
        Py_DECREF(module);
        return nullptr;
    }

    return module;
}
'''.replace("<register-functions>", register_functions_f(method_names)).replace("<module-name>", module_name.split('.')[-1])

def generate_extension(module_name, library_file_name, method_names):
    output =    headers(library_file_name)
    output +=   register_handlers 
    output +=   execute_f
    output +=   template_methods(method_names)
    output +=   methods_def(method_names)
    output +=   module_def(module_name)
    output +=   init_module(module_name, method_names)
    return output

if __name__ == "__main__":
    method_test = extract_function_names("./my_library.hpp") 
    print(generate_extension("mymodule", "my_library.hpp", method_test))
