import numpy as np

arr1 = np.array([[1, 1], [2, 2]])
arr2 = np.array([[3, 3], [4, 4]])

arr3 = np.hstack((arr1, arr2))
print(arr3)