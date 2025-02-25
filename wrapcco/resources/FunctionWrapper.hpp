#include <stdexcept>
#include <numpy/arrayobject.h>

// Add a new type to handle numpy arrays directly
struct NumpyArrayRef {
    PyArrayObject* array;
    bool owns_data;  // Whether this object should decrement the reference on destruction
    
    // Constructor that takes ownership
    explicit NumpyArrayRef(PyArrayObject* arr, bool take_ownership = true) 
        : array(arr), owns_data(take_ownership) {
        if (take_ownership) {
            Py_INCREF(arr);
        }
    }
    
    // Destructor to handle reference counting
    ~NumpyArrayRef() {
        if (owns_data && array) {
            Py_DECREF(array);
        }
    }
    
    // No copy constructor - prevent accidental copying
    NumpyArrayRef(const NumpyArrayRef&) = delete;
    NumpyArrayRef& operator=(const NumpyArrayRef&) = delete;
    
    // Move constructor and assignment
    NumpyArrayRef(NumpyArrayRef&& other) noexcept
        : array(other.array), owns_data(other.owns_data) {
        other.array = nullptr;
        other.owns_data = false;
    }
    
    NumpyArrayRef& operator=(NumpyArrayRef&& other) noexcept {
        if (this != &other) {
            if (owns_data && array) {
                Py_DECREF(array);
            }
            array = other.array;
            owns_data = other.owns_data;
            other.array = nullptr;
            other.owns_data = false;
        }
        return *this;
    }
    
    // Helper methods to access data
    template<typename T>
    T* data() const {
        return static_cast<T*>(PyArray_DATA(array));
    }
    
    int ndim() const {
        return PyArray_NDIM(array);
    }
    
    npy_intp size() const {
        return PyArray_SIZE(array);
    }
    
    npy_intp* shape() const {
        return PyArray_DIMS(array);
    }
    
    npy_intp* strides() const {
        return PyArray_STRIDES(array);
    }
    
    int dtype() const {
        return PyArray_TYPE(array);
    }
};

// function wrapper base class
class FunctionWrapperBase {
public:
    virtual PyObject* execute(PyObject* args) = 0;
    virtual ~FunctionWrapperBase() = default;
};

// template class for handling different function signatures
template<typename Ret, typename... Args>
class FunctionWrapper : public FunctionWrapperBase {
private:
    std::function<Ret(Args...)> func;
    
    // helper to convert Python objects to C++ types
    template<typename T>
    T convert_arg(PyObject* obj) {
        using U = std::decay_t<T>;
        if constexpr (std::is_same_v<U, int>) {
            return PyLong_AsLong(obj);
        } else if constexpr (std::is_same_v<U, double>) {
            return PyFloat_AsDouble(obj);
        } else if constexpr (std::is_same_v<U, std::vector<double>>) {
            // Keep this for backward compatibility
            if (!PyArray_Check(obj)) {
                throw std::runtime_error("Expected numpy array");
            }
            
            PyArrayObject* arr_cont = reinterpret_cast<PyArrayObject*>(
                PyArray_ContiguousFromAny(obj, NPY_DOUBLE, 1, 1));
            
            if (!arr_cont) {
                throw std::runtime_error("Could not convert array to contiguous double array");
            }
            
            npy_intp size = PyArray_SIZE(arr_cont);
            double* data = static_cast<double*>(PyArray_DATA(arr_cont));
            std::vector<double> result(data, data + size);
            
            Py_DECREF(arr_cont);
            return result;
        } else if constexpr (std::is_same_v<U, NumpyArrayRef>) {
            // For direct NumPy array handling
            if (!PyArray_Check(obj)) {
                throw std::runtime_error("Expected numpy array");
            }
            
            // Ensure the array is contiguous and has the right type
            // Note: This doesn't copy data if the array is already contiguous and of the right type
            PyArrayObject* arr_cont = reinterpret_cast<PyArrayObject*>(
                PyArray_FromAny(obj, nullptr, 0, 0, 
                                NPY_ARRAY_C_CONTIGUOUS | NPY_ARRAY_ENSUREARRAY, 
                                nullptr));
            
            if (!arr_cont) {
                throw std::runtime_error("Could not ensure array is contiguous");
            }
            
            return NumpyArrayRef(arr_cont, true);  // true means take ownership
        }
        throw std::runtime_error("Unsupported type conversion");
    }

    // helper to convert C++ return types to Python objects
    template<typename T>
    PyObject* convert_return(const T& value) {
        if constexpr (std::is_same_v<T, int>) {
            return PyLong_FromLong(value);
        } else if constexpr (std::is_same_v<T, double>) {
            return PyFloat_FromDouble(value);
        } else if constexpr (std::is_same_v<T, std::vector<double>>) {
            npy_intp dims[] = {static_cast<npy_intp>(value.size())};
            PyObject* arr = PyArray_SimpleNew(1, dims, NPY_DOUBLE);
            if (!arr) {
                throw std::runtime_error("Failed to create numpy array");
            }
            memcpy(PyArray_DATA(reinterpret_cast<PyArrayObject*>(arr)), 
                   value.data(), value.size() * sizeof(double));
            return arr;
        } else if constexpr (std::is_same_v<T, NumpyArrayRef>) {
            // For returning NumPy arrays directly
            Py_INCREF(value.array);  // Increase reference count for the returned value
            return reinterpret_cast<PyObject*>(value.array);
        }
        throw std::runtime_error("Unsupported return type conversion");
    }

    // helper to get argument at index
    template<size_t I>
    auto get_arg(PyObject* args) {
        using ArgType = typename std::tuple_element<I, std::tuple<Args...>>::type;
        // Remove both reference and const qualifiers.
        return convert_arg<std::remove_cv_t<std::remove_reference_t<ArgType>>>(PyTuple_GetItem(args, I));
    }

    // helper to build argument tuple
    template<size_t... I>
    auto build_args(PyObject* args, std::index_sequence<I...>) {
        return std::make_tuple(get_arg<I>(args)...);
    }

public:
    FunctionWrapper(std::function<Ret(Args...)> f) : func(f) {}

    PyObject* execute(PyObject* args) override {
        if (!PyTuple_Check(args)) {
            PyErr_SetString(PyExc_TypeError, "Arguments must be a tuple");
            return nullptr;
        }

        if (PyTuple_Size(args) != sizeof...(Args)) {
            PyErr_SetString(PyExc_TypeError, "Wrong number of arguments");
            return nullptr;
        }

        try {
            auto tuple_args = build_args(args, std::index_sequence_for<Args...>{});
            if constexpr (std::is_void_v<Ret>) {
                std::apply(func, tuple_args);
                Py_RETURN_NONE;
            } else {
                auto result = std::apply(func, tuple_args);
                return convert_return(result);
            }
        } catch (const std::exception& e) {
            PyErr_SetString(PyExc_RuntimeError, e.what());
            return nullptr;
        }
    }
};
