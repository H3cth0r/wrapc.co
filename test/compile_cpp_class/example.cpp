#include <Python.h>
#include <string>

// First C++ class
class MyClass {
public:
    MyClass(int value) : value(value) {}
    int getValue() const { return value; }
    void setValue(int v) { value = v; }
private:
    int value;
};

// Second C++ class
class AnotherClass {
public:
    AnotherClass(const char* text) : text(text) {}
    const char* getText() const { return text.c_str(); }
    void setText(const char* t) { text = t; }
private:
    std::string text;
};

// Python object structures
typedef struct {
    PyObject_HEAD
    MyClass* cpp_instance;
} PyMyClass;

typedef struct {
    PyObject_HEAD
    AnotherClass* cpp_instance;
} PyAnotherClass;

// Wrapper functions for MyClass
static PyObject* MyClass_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyMyClass* self = (PyMyClass*)type->tp_alloc(type, 0);
    if (self) {
        int value = 0;
        if (!PyArg_ParseTuple(args, "i", &value)) {
            Py_DECREF(self);
            return nullptr;
        }
        self->cpp_instance = new MyClass(value);
    }
    return (PyObject*)self;
}

static void MyClass_dealloc(PyMyClass* self) {
    if (self->cpp_instance) {
        delete self->cpp_instance;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* MyClass_get_value(PyMyClass* self, PyObject* Py_UNUSED(ignored)) {
    return PyLong_FromLong(self->cpp_instance->getValue());
}

static PyObject* MyClass_set_value(PyMyClass* self, PyObject* args) {
    int value;
    if (!PyArg_ParseTuple(args, "i", &value)) {
        return nullptr;
    }
    self->cpp_instance->setValue(value);
    Py_RETURN_NONE;
}

// Wrapper functions for AnotherClass
static PyObject* AnotherClass_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyAnotherClass* self = (PyAnotherClass*)type->tp_alloc(type, 0);
    if (self) {
        const char* text;
        if (!PyArg_ParseTuple(args, "s", &text)) {
            Py_DECREF(self);
            return nullptr;
        }
        self->cpp_instance = new AnotherClass(text);
    }
    return (PyObject*)self;
}

static void AnotherClass_dealloc(PyAnotherClass* self) {
    if (self->cpp_instance) {
        delete self->cpp_instance;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* AnotherClass_get_text(PyAnotherClass* self, PyObject* Py_UNUSED(ignored)) {
    return PyUnicode_FromString(self->cpp_instance->getText());
}

static PyObject* AnotherClass_set_text(PyAnotherClass* self, PyObject* args) {
    const char* text;
    if (!PyArg_ParseTuple(args, "s", &text)) {
        return nullptr;
    }
    self->cpp_instance->setText(text);
    Py_RETURN_NONE;
}

// Method definitions for both classes
static PyMethodDef MyClass_methods[] = {
    {"get_value", (PyCFunction)MyClass_get_value, METH_NOARGS, "Get the value"},
    {"set_value", (PyCFunction)MyClass_set_value, METH_VARARGS, "Set the value"},
    {nullptr}
};

static PyMethodDef AnotherClass_methods[] = {
    {"get_text", (PyCFunction)AnotherClass_get_text, METH_NOARGS, "Get the text"},
    {"set_text", (PyCFunction)AnotherClass_set_text, METH_VARARGS, "Set the text"},
    {nullptr}
};

// Type definitions for both classes
static PyTypeObject MyClassType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "example.MyClass",
    .tp_basicsize = sizeof(PyMyClass),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)MyClass_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "MyClass objects",
    .tp_methods = MyClass_methods,
    .tp_new = MyClass_new,
};

static PyTypeObject AnotherClassType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "example.AnotherClass",
    .tp_basicsize = sizeof(PyAnotherClass),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)AnotherClass_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "AnotherClass objects",
    .tp_methods = AnotherClass_methods,
    .tp_new = AnotherClass_new,
};

// Module definition
static PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",
    "Example module",
    -1,
    nullptr
};

PyMODINIT_FUNC PyInit_example(void) {
    // Initialize both types
    if (PyType_Ready(&MyClassType) < 0) {
        return nullptr;
    }
    if (PyType_Ready(&AnotherClassType) < 0) {
        return nullptr;
    }
    
    PyObject* m = PyModule_Create(&examplemodule);
    if (!m) {
        return nullptr;
    }
    
    // Add both types to the module
    Py_INCREF(&MyClassType);
    if (PyModule_AddObject(m, "MyClass", (PyObject*)&MyClassType) < 0) {
        Py_DECREF(&MyClassType);
        Py_DECREF(m);
        return nullptr;
    }
    
    Py_INCREF(&AnotherClassType);
    if (PyModule_AddObject(m, "AnotherClass", (PyObject*)&AnotherClassType) < 0) {
        Py_DECREF(&AnotherClassType);
        Py_DECREF(&MyClassType);
        Py_DECREF(m);
        return nullptr;
    }
    
    return m;
}
