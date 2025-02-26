#pragma once
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <numeric>
#include <cmath>

int addInts(int a, int b) {
    return a + b;
}

inline int addMoreInts(int a, int b, int c) {
    return a + b + c;
}

void addScalarInPlace(NumpyArrayRef& arr_ref, int scalar) {
    if (arr_ref.dtype() != NPY_DOUBLE) {
        throw std::runtime_error("Expected double-type numpy array");
    }
    
    double* data = arr_ref.data<double>();
    npy_intp size = arr_ref.size();
    
    #pragma omp parallel for
    for(npy_intp i = 0; i < size; ++i) {
        data[i] += scalar;
    }
}
