from array import array
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

array3 = np.concatenate((a, b))

print(array3)