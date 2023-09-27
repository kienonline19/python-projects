# np.array(args) => ndarray object
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

arr_one = np.array((2, 4, 6, 8.5))

print(arr_one)

# create the 0-D array
arr_two = np.array(56)

print(arr_two)
print(type(arr_two))

# create the 1-D array
print(np.array([1, 2, 3]))

# create the 2-D array
arr_three = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_three)
print(type(arr_three))

# create the 3-D array
arr_four = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_four)

print(arr.ndim)
print(arr_one.ndim)
print(arr_two.ndim)
print(arr_three.ndim)
print(arr_four.ndim)

# create the array with ndmin=5
a = np.array([1, 2, 3, 4, 5], ndmin=5)
print(a)

print('number of dimensions:', a.ndim)
