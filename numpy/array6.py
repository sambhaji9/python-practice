import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(np.concatenate((x, y), axis = 0))