import numpy as np

arr = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

five_up = (arr > 5) | (arr == 5)
print("numbers greater than equal to 5: ", five_up)

arr1 = np.nonzero(arr < 5)
print(arr1)
