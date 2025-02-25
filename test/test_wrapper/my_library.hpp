#pragma once
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <numeric>
#include <cmath>
#include <omp.h>

int addInts(int a, int b) {
    return a + b;
}

inline int addMoreInts(int a, int b, int c) {
    return a + b + c;
}

inline NumpyArrayRef addArrays(const NumpyArrayRef& a, const NumpyArrayRef& b) {
    // Check if arrays have the same size
    if (a.size() != b.size()) {
        throw std::runtime_error("Arrays must have the same size");
    }
    
    // Store common array size
    const npy_intp size = a.size();
    
    // Get array data
    double* a_data = a.data<double>();
    double* b_data = b.data<double>();
    
    // Create output array with the same shape as input
    npy_intp dims[] = {size};
    PyObject* result_obj = PyArray_SimpleNew(1, dims, NPY_DOUBLE);
    if (!result_obj) {
        throw std::runtime_error("Failed to create output array");
    }
    
    PyArrayObject* result_arr = reinterpret_cast<PyArrayObject*>(result_obj);
    double* result_data = static_cast<double*>(PyArray_DATA(result_arr));
    
    // Perform addition directly on the array data using OpenMP
    // #pragma omp parallel for
    for (npy_intp i = 0; i < size; ++i) {
        result_data[i] = a_data[i] + b_data[i];
    }
    
    // Return the new array (NumpyArrayRef will manage the reference)
    return NumpyArrayRef(result_arr);
}
