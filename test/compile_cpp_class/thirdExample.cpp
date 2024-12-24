#include <Python.h>
#include "ThirdDefs.h"

typedef struct {
    PyObject_HEAD
    Animal* cpp_instance;
} PyAnimal;
            
typedef struct {
    PyObject_HEAD
    Dog* cpp_instance;
} PyDog;
            
static PyObject* Animal_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyAnimal* self = (PyAnimal*)type->tp_alloc(type, 0);
    if (self) {
        ;
        if (!PyArg_ParseTuple(args, "", )) {
            Py_DECREF(self);
            return nullptr;
        }
        
        try {
            self->cpp_instance = new Animal();
        } catch (const std::exception& e) {
            PyErr_SetString(PyExc_RuntimeError, e.what());
            Py_DECREF(self);
            return nullptr;
        }
    }
    return (PyObject*)self;
}

static void (_class.className)_dealloc(PyAnimal* self) {
    if (self->cpp_instance) {
        delete self->cpp_instance;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}
        
static PyObject* Animal_speak(PyAnimal* self, PyObject* args) {
        
    auto result = self->cpp_instance->speak();
    return PyUnicode_FromString(result.c_str());
            }

static PyObject* Animal_getAge(PyAnimal* self, PyObject* args) {
        
    auto result = self->cpp_instance->getAge();
    return PyLong_FromLong(result);
            }

static PyObject* Animal_setAge(PyAnimal* self, PyObject* args) {
        
    int a;
    if (!PyArg_ParseTuple(args, "i", & a)) {
        return nullptr;
    }
    
            
    self->cpp_instance->setAge(a);
    Py_RETURN_NONE;
            }

static PyMethodDef Animal_methods[] = {
    {"speak", (PyCFunction)Animal_speak, METH_NOARGS, "Execute speak"},
    {"getAge", (PyCFunction)Animal_getAge, METH_NOARGS, "Execute getAge"},
    {"setAge", (PyCFunction)Animal_setAge, METH_VARARGS, "Execute setAge"},
    {NULL, NULL, 0, NULL}
};
        
static PyTypeObject AnimalType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "example.Animal",
    .tp_basicsize = sizeof(PyAnimal),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)Animal_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "Animal objects",
    .tp_methods = Animal_methods,
    .tp_new = Animal_new,
};
        
static PyObject* Dog_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyDog* self = (PyDog*)type->tp_alloc(type, 0);
    if (self) {
        const char* name_str, int age;
        if (!PyArg_ParseTuple(args, "si", & name_str, & age)) {
            Py_DECREF(self);
            return nullptr;
        }
        std::string name(name_str);
        try {
            self->cpp_instance = new Dog(name, age);
        } catch (const std::exception& e) {
            PyErr_SetString(PyExc_RuntimeError, e.what());
            Py_DECREF(self);
            return nullptr;
        }
    }
    return (PyObject*)self;
}

static void (_class.className)_dealloc(PyDog* self) {
    if (self->cpp_instance) {
        delete self->cpp_instance;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}
        
static PyObject* Dog_speak(PyDog* self, PyObject* args) {
        
    auto result = self->cpp_instance->speak();
    return PyUnicode_FromString(result.c_str());
            }

static PyObject* Dog_getName(PyDog* self, PyObject* args) {
        
    auto result = self->cpp_instance->getName();
    return None(result.c_str());
            }

static PyObject* Dog_getAgeInDifferentUnit(PyDog* self, PyObject* args) {
        
    T multiplier;
    if (!PyArg_ParseTuple(args, "O", & multiplier)) {
        return nullptr;
    }
    
            
    auto result = self->cpp_instance->getAgeInDifferentUnit(multiplier);
    return None(result);
            }

static PyMethodDef Dog_methods[] = {
    {"speak", (PyCFunction)Dog_speak, METH_NOARGS, "Execute speak"},
    {"getName", (PyCFunction)Dog_getName, METH_NOARGS, "Execute getName"},
    {"getAgeInDifferentUnit", (PyCFunction)Dog_getAgeInDifferentUnit, METH_VARARGS, "Execute getAgeInDifferentUnit"},
    {NULL, NULL, 0, NULL}
};
        
static PyTypeObject DogType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "example.Dog",
    .tp_basicsize = sizeof(PyDog),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)Dog_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "Dog objects",
    .tp_methods = Dog_methods,
    .tp_new = Dog_new,
};
        
static PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",
    "Example module",
    -1,
    nullptr
};

PyMODINIT_FUNC PyInit_example(void) {
        
    if (PyType_Ready(&AnimalType) < 0) {
        return nullptr;
    }
            
    if (PyType_Ready(&DogType) < 0) {
        return nullptr;
    }
            
    PyObject* m = PyModule_Create(&examplemodule);
    if (!m) {
        return nullptr;
    }
        
    Py_INCREF(&AnimalType);
    if (PyModule_AddObject(m, "Animal", (PyObject*)&AnimalType) < 0) {
        Py_DECREF(&AnimalType);
        Py_DECREF(m);
        return nullptr;
    }
            
    Py_INCREF(&DogType);
    if (PyModule_AddObject(m, "Dog", (PyObject*)&DogType) < 0) {
        Py_DECREF(&DogType);
        Py_DECREF(m);
        return nullptr;
    }
            
    return m;
}
