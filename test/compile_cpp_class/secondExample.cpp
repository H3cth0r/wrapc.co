#include <Python.h>
#include <string>
#include <vector>
#include <memory>

// Base class with virtual functions
class Animal {
public:
    virtual ~Animal() = default;
    virtual std::string speak() const = 0;
    virtual int getAge() const { return age; }
    void setAge(int a) { age = a; }
protected:
    int age = 0;
};

// Derived class
class Dog : public Animal {
public:
    Dog(const std::string& name, int age) : name(name) { setAge(age); }
    std::string speak() const override { return "Woof!"; }
    const std::string& getName() const { return name; }
    
    // Template method
    template<typename T>
    T getAgeInDifferentUnit(T multiplier) const {
        return static_cast<T>(getAge()) * multiplier;
    }
private:
    std::string name;
};

// Python object structure
typedef struct {
    PyObject_HEAD
    std::shared_ptr<Animal> cpp_instance;  // Using smart pointer
} PyAnimal;

// Type checking helper
static bool isDogInstance(const std::shared_ptr<Animal>& ptr) {
    return dynamic_cast<Dog*>(ptr.get()) != nullptr;
}

// Wrapper functions
static PyObject* Animal_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    PyAnimal* self = (PyAnimal*)type->tp_alloc(type, 0);
    if (self) {
        const char* name;
        int age;
        if (!PyArg_ParseTuple(args, "si", &name, &age)) {
            Py_DECREF(self);
            return nullptr;
        }
        // Create a Dog instance (could be extended to create different animals)
        self->cpp_instance = std::make_shared<Dog>(name, age);
    }
    return (PyObject*)self;
}

static void Animal_dealloc(PyAnimal* self) {
    // shared_ptr will handle cleanup automatically
    self->cpp_instance.reset();
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* Animal_speak(PyAnimal* self, PyObject* Py_UNUSED(ignored)) {
    return PyUnicode_FromString(self->cpp_instance->speak().c_str());
}

static PyObject* Animal_get_age(PyAnimal* self, PyObject* Py_UNUSED(ignored)) {
    return PyLong_FromLong(self->cpp_instance->getAge());
}

static PyObject* Animal_get_age_in_months(PyAnimal* self, PyObject* Py_UNUSED(ignored)) {
    if (!isDogInstance(self->cpp_instance)) {
        PyErr_SetString(PyExc_TypeError, "Method only available for Dog instances");
        return nullptr;
    }
    
    auto dog = std::dynamic_pointer_cast<Dog>(self->cpp_instance);
    // Using template method with float multiplier
    float age_in_months = dog->getAgeInDifferentUnit<float>(12.0f);
    return PyFloat_FromDouble(age_in_months);
}

static PyObject* Animal_get_name(PyAnimal* self, PyObject* Py_UNUSED(ignored)) {
    if (!isDogInstance(self->cpp_instance)) {
        PyErr_SetString(PyExc_TypeError, "Method only available for Dog instances");
        return nullptr;
    }
    
    auto dog = std::dynamic_pointer_cast<Dog>(self->cpp_instance);
    return PyUnicode_FromString(dog->getName().c_str());
}

// Method definitions
static PyMethodDef Animal_methods[] = {
    {"speak", (PyCFunction)Animal_speak, METH_NOARGS, "Get the animal's sound"},
    {"get_age", (PyCFunction)Animal_get_age, METH_NOARGS, "Get the animal's age"},
    {"get_age_in_months", (PyCFunction)Animal_get_age_in_months, METH_NOARGS, "Get the dog's age in months"},
    {"get_name", (PyCFunction)Animal_get_name, METH_NOARGS, "Get the dog's name"},
    {nullptr}
};

// Type definition
static PyTypeObject AnimalType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "advanced_example.Animal",
    .tp_basicsize = sizeof(PyAnimal),
    .tp_itemsize = 0,
    .tp_dealloc = (destructor)Animal_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "Animal objects",
    .tp_methods = Animal_methods,
    .tp_new = Animal_new,
};

// Module definition
static PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "advanced_example",
    "Advanced example module",
    -1,
    nullptr
};

PyMODINIT_FUNC PyInit_advanced_example(void) {
    if (PyType_Ready(&AnimalType) < 0) {
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
    
    return m;
}
