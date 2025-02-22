
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <numpy/arrayobject.h>
#include <unordered_map>
#include <functional>
#include <vector>
#include <memory>
#include <numeric>
#include <cstring>
#include "FunctionWrapper.hpp"
#include "my_library.hpp"
#include "my_second.hpp"


// global registry to store functions
static std::unordered_map<std::string, std::unique_ptr<FunctionWrapperBase>> function_registry;

// function to register C++ functions
template<typename Ret, typename... Args>
void register_function(const std::string& name, Ret(*func)(Args...)) {
    function_registry[name] = std::make_unique<FunctionWrapper<Ret, Args...>>(func);
}

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

static PyObject* addIntsF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("addInts");
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

static PyObject* addMoreIntsF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("addMoreInts");
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

static PyObject* addArraysF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("addArrays");
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

static PyObject* multiplyArraysF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("multiplyArrays");
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

static PyObject* scaleArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("scaleArray");
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

static PyObject* dotProductF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("dotProduct");
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

static PyObject* expArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("expArray");
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

static PyObject* logArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("logArray");
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

static PyObject* sumArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("sumArray");
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

static PyObject* meanArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("meanArray");
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

static PyObject* maxArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("maxArray");
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

static PyObject* minArrayF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("minArray");
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

static PyObject* linspaceF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("linspace");
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

static PyObject* arangeF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("arange");
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

static PyObject* prodIntsF(PyObject* self, PyObject* args) {
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
    auto it = function_registry.find("prodInts");
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

// module method definitions
static PyMethodDef ModuleMethods[] = {
        {"execute_function", execute_function, METH_VARARGS, "Execute a registered function"},
	{"addInts", addIntsF, METH_VARARGS, "addInts function"},
	{"addMoreInts", addMoreIntsF, METH_VARARGS, "addMoreInts function"},
	{"addArrays", addArraysF, METH_VARARGS, "addArrays function"},
	{"multiplyArrays", multiplyArraysF, METH_VARARGS, "multiplyArrays function"},
	{"scaleArray", scaleArrayF, METH_VARARGS, "scaleArray function"},
	{"dotProduct", dotProductF, METH_VARARGS, "dotProduct function"},
	{"expArray", expArrayF, METH_VARARGS, "expArray function"},
	{"logArray", logArrayF, METH_VARARGS, "logArray function"},
	{"sumArray", sumArrayF, METH_VARARGS, "sumArray function"},
	{"meanArray", meanArrayF, METH_VARARGS, "meanArray function"},
	{"maxArray", maxArrayF, METH_VARARGS, "maxArray function"},
	{"minArray", minArrayF, METH_VARARGS, "minArray function"},
	{"linspace", linspaceF, METH_VARARGS, "linspace function"},
	{"arange", arangeF, METH_VARARGS, "arange function"},
	{"prodInts", prodIntsF, METH_VARARGS, "prodInts function"}, 
        {nullptr, nullptr, 0, nullptr}
};

// module definition structure
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "testmodule",
    "testmodule module",
    -1,
    ModuleMethods
};

// module initialization function
PyMODINIT_FUNC PyInit_testmodule(void) {
    import_array();  // initialize NumPy

    PyObject* module = PyModule_Create(&moduledef);
    if (!module) {
        return nullptr;
    }

    // Register all functions during module initialization
    try {
	register_function("addInts", addInts);
	register_function("addMoreInts", addMoreInts);
	register_function("addArrays", addArrays);
	register_function("multiplyArrays", multiplyArrays);
	register_function("scaleArray", scaleArray);
	register_function("dotProduct", dotProduct);
	register_function("expArray", expArray);
	register_function("logArray", logArray);
	register_function("sumArray", sumArray);
	register_function("meanArray", meanArray);
	register_function("maxArray", maxArray);
	register_function("minArray", minArray);
	register_function("linspace", linspace);
	register_function("arange", arange);
	register_function("prodInts", prodInts);
    } catch (const std::exception& e) {
        PyErr_SetString(PyExc_RuntimeError, 
            ("Failed to register functions: " + std::string(e.what())).c_str());
        Py_DECREF(module);
        return nullptr;
    }

    return module;
}
