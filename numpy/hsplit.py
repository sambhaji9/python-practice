import numpy as np

x = np.arange(1, 25).reshape(2, 12)
print(x)

print(np.hsplit(x, 3))

print (np.hsplit(x, (3, 4)))