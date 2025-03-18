// Template function to create result array of any numeric type
template<typename T>
inline T* createResultArray(const NumpyArrayRef& input, NumpyArrayRef& output, int npy_type) {
    const npy_intp size = input.size();
    npy_intp dims[] = {size};
    PyObject* result_obj = PyArray_SimpleNew(1, dims, npy_type);
    if (!result_obj) {
        throw std::runtime_error("Failed to create output array");
    }
    PyArrayObject* result_arr = reinterpret_cast<PyArrayObject*>(result_obj);
    output = NumpyArrayRef(result_arr);
    return static_cast<T*>(PyArray_DATA(result_arr));
}

// Function to create arrays with arbitrary dimensions
template<typename T>
inline T* createArrayWithShape(NumpyArrayRef& output, const std::vector<npy_intp>& shape, int npy_type) {
    const int ndim = static_cast<int>(shape.size());
    PyObject* result_obj = PyArray_SimpleNew(ndim, shape.data(), npy_type);
    if (!result_obj) {
        throw std::runtime_error("Failed to create array with specified shape");
    }
    PyArrayObject* result_arr = reinterpret_cast<PyArrayObject*>(result_obj);
    output = NumpyArrayRef(result_arr);
    return static_cast<T*>(PyArray_DATA(result_arr));
}
