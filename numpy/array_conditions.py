import numpy as np

arr = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("numbers less than 5: ", arr[arr < 5])

five_up = (arr >= 5)
print("numbers greater than equal to 5: ", arr[five_up])

divisible_by_two = arr[arr % 2 == 0]
print("numbers divisible by 2: ", divisible_by_two)