# program to check if a number is prime or not

# To take input from the user
num = int(input("Enter the number: "))


# define a flag variable
flag = False

# prime number are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i == 0):
            # if factor is found, set flag to true
            flag = True
            # break out of loop
            break

# check if flag is true
if flag:
    print(num, " is not a prime number")
else:
    print(num, " is a prime number")