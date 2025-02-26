import numpy as np
from testmod.mathfunc import addInts, addScalarInPlace

result = addInts(5, 3)
print(result)


arr = np.array([1., 2., 3.], dtype=np.float64)
print(arr)
addScalarInPlace(arr, 5)
print(arr)
