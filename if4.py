''' In this program,
    we check if the number is positive or negative or zero and
    display an appropriate message '''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("Positive number")
else:
    print("Negative number")