
#include <Python.h>
#include "./OpsLibs.h"
        
typedef struct {
    PyObject_HEAD
    Point* cpp_instance;
} PyPoint;
            
static PyObject* Point_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyPoint* self = (PyPoint*)type->tp_alloc(type, 0);
    if (self) {
        int x; int y; const char* name_str;
        
        if (!PyArg_ParseTuple(args, "iis", & x, & y, & name_str)) {
            Py_DECREF(self);
            return nullptr;
        }
            
        std::string name(name_str);
        try {
            self->cpp_instance = new Point(x, y, name);
        } catch (const std::exception& e) {
            PyErr_SetString(PyExc_RuntimeError, e.what());
            Py_DECREF(self);
            return nullptr;
        }
    }
    return (PyObject*)self;
}

static void Point_dealloc(PyPoint* self) {
    if (self->cpp_instance) {
        delete self->cpp_instance;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}
        
static PyObject* Point_getX(PyPoint* self, PyObject* args) {
        
    auto result = self->cpp_instance->getX();
    return PyLong_FromLong(result);
            }

static PyObject* Point_getY(PyPoint* self, PyObject* args) {
        
    auto result = self->cpp_instance->getY();
    return PyLong_FromLong(result);
            }

static PyObject* Point_moveOnXBy(PyPoint* self, PyObject* args) {
        
    int x;
    if (!PyArg_ParseTuple(args, "i", & x)) {
        return nullptr;
    }
    
            
    self->cpp_instance->moveOnXBy(x);
    Py_RETURN_NONE;
            }

static PyObject* Point_moveOnYBy(PyPoint* self, PyObject* args) {
        
    int y;
    if (!PyArg_ParseTuple(args, "i", & y)) {
        return nullptr;
    }
    
            
    self->cpp_instance->moveOnYBy(y);
    Py_RETURN_NONE;
            }

static PyMethodDef Point_methods[] = {
    {"getX", (PyCFunction)Point_getX, METH_NOARGS, "Execute getX"},
    {"getY", (PyCFunction)Point_getY, METH_NOARGS, "Execute getY"},
    {"moveOnXBy", (PyCFunction)Point_moveOnXBy, METH_VARARGS, "Execute moveOnXBy"},
    {"moveOnYBy", (PyCFunction)Point_moveOnYBy, METH_VARARGS, "Execute moveOnYBy"},
    {NULL, NULL, 0, NULL}
};
        
static PyTypeObject PointType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "opslib_extension.Point",
    .tp_basicsize = sizeof(PyPoint),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)Point_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "Point objects",
    .tp_methods = Point_methods,
    .tp_new = Point_new,
};
        
static PyModuleDef opslib_extensionmodule = {
    PyModuleDef_HEAD_INIT,
    "opslib_extension",
    "opslib_extension module",
    -1,
    nullptr
};

PyMODINIT_FUNC PyInit_opslib_extension(void) {
        
    if (PyType_Ready(&PointType) < 0) {
        return nullptr;
    }
            
    PyObject* m = PyModule_Create(&opslib_extensionmodule);
    if (!m) {
        return nullptr;
    }
        
    Py_INCREF(&PointType);
    if (PyModule_AddObject(m, "Point", (PyObject*)&PointType) < 0) {
        Py_DECREF(&PointType);
        Py_DECREF(m);
        return nullptr;
    }
            
    return m;
}
        