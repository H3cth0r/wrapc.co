
#include <Python.h>
#include "./Human.h"
        
typedef struct {
    PyObject_HEAD
    Human* cpp_instance;
} PyHuman;
            
static PyObject* Human_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyHuman* self = (PyHuman*)type->tp_alloc(type, 0);
    if (self) {
        const char* name_str; int age; double height; double weight;
        
        if (!PyArg_ParseTuple(args, "sidd", & name_str, & age, & height, & weight)) {
            Py_DECREF(self);
            return nullptr;
        }
            
        std::string name(name_str);
        try {
            self->cpp_instance = new Human(name, age, height, weight);
        } catch (const std::exception& e) {
            PyErr_SetString(PyExc_RuntimeError, e.what());
            Py_DECREF(self);
            return nullptr;
        }
    }
    return (PyObject*)self;
}

static void Human_dealloc(PyHuman* self) {
    if (self->cpp_instance) {
        delete self->cpp_instance;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}
        
static PyObject* Human_getName(PyHuman* self, PyObject* args) {
        
    auto result = self->cpp_instance->getName();
    return PyUnicode_FromString(result.c_str());
            }

static PyObject* Human_getAge(PyHuman* self, PyObject* args) {
        
    auto result = self->cpp_instance->getAge();
    return PyLong_FromLong(result);
            }

static PyObject* Human_getHeight(PyHuman* self, PyObject* args) {
        
    auto result = self->cpp_instance->getHeight();
    return PyFloat_FromDouble(result);
            }

static PyObject* Human_getWeight(PyHuman* self, PyObject* args) {
        
    auto result = self->cpp_instance->getWeight();
    return PyFloat_FromDouble(result);
            }

static PyObject* Human_setName(PyHuman* self, PyObject* args) {
        
    const char* name_str;
    if (!PyArg_ParseTuple(args, "s", & name_str)) {
        return nullptr;
    }
    std::string name(name_str);
            
    self->cpp_instance->setName(name);
    Py_RETURN_NONE;
            }

static PyObject* Human_setAge(PyHuman* self, PyObject* args) {
        
    int age;
    if (!PyArg_ParseTuple(args, "i", & age)) {
        return nullptr;
    }
    
            
    self->cpp_instance->setAge(age);
    Py_RETURN_NONE;
            }

static PyObject* Human_setHeight(PyHuman* self, PyObject* args) {
        
    double height;
    if (!PyArg_ParseTuple(args, "d", & height)) {
        return nullptr;
    }
    
            
    self->cpp_instance->setHeight(height);
    Py_RETURN_NONE;
            }

static PyObject* Human_setWeight(PyHuman* self, PyObject* args) {
        
    double weight;
    if (!PyArg_ParseTuple(args, "d", & weight)) {
        return nullptr;
    }
    
            
    self->cpp_instance->setWeight(weight);
    Py_RETURN_NONE;
            }

static PyObject* Human_calculateBMI(PyHuman* self, PyObject* args) {
        
    auto result = self->cpp_instance->calculateBMI();
    return PyFloat_FromDouble(result);
            }

static PyMethodDef Human_methods[] = {
    {"getName", (PyCFunction)Human_getName, METH_NOARGS, "Execute getName"},
    {"getAge", (PyCFunction)Human_getAge, METH_NOARGS, "Execute getAge"},
    {"getHeight", (PyCFunction)Human_getHeight, METH_NOARGS, "Execute getHeight"},
    {"getWeight", (PyCFunction)Human_getWeight, METH_NOARGS, "Execute getWeight"},
    {"setName", (PyCFunction)Human_setName, METH_VARARGS, "Execute setName"},
    {"setAge", (PyCFunction)Human_setAge, METH_VARARGS, "Execute setAge"},
    {"setHeight", (PyCFunction)Human_setHeight, METH_VARARGS, "Execute setHeight"},
    {"setWeight", (PyCFunction)Human_setWeight, METH_VARARGS, "Execute setWeight"},
    {"calculateBMI", (PyCFunction)Human_calculateBMI, METH_NOARGS, "Execute calculateBMI"},
    {NULL, NULL, 0, NULL}
};
        
static PyTypeObject HumanType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "human_extension.Human",
    .tp_basicsize = sizeof(PyHuman),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)Human_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "Human objects",
    .tp_methods = Human_methods,
    .tp_new = Human_new,
};
        
static PyModuleDef human_extensionmodule = {
    PyModuleDef_HEAD_INIT,
    "human_extension",
    "human_extension module",
    -1,
    nullptr
};

PyMODINIT_FUNC PyInit_human_extension(void) {
        
    if (PyType_Ready(&HumanType) < 0) {
        return nullptr;
    }
            
    PyObject* m = PyModule_Create(&human_extensionmodule);
    if (!m) {
        return nullptr;
    }
        
    Py_INCREF(&HumanType);
    if (PyModule_AddObject(m, "Human", (PyObject*)&HumanType) < 0) {
        Py_DECREF(&HumanType);
        Py_DECREF(m);
        return nullptr;
    }
            
    return m;
}
        