import numpy as np
arr1 = np.array([1,2,3,5,5])
arr2 = np.array([1,6,3,4,5])
print(arr1)
print(arr2)
print(np.greater(arr2, arr1))  # compare arr2 with arr1
print(np.greater(arr1, arr2))  # compare arr1 with arr2

print(np.less(arr1, arr2))
print(np.less(arr2, arr1))

print(np.less_equal(arr1, arr2))
print(np.less_equal(arr2, arr1))

print(np.greater_equal(arr1, arr2))
print(np.greater_equal(arr2, arr1))
