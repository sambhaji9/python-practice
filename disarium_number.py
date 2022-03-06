import math

def digitsCount(Number):
    length = 0
    while Number != 0:
        length = length + 1
        Number = Number // 10
    return length

def digitsSum(Number):
    Sum = 0
    rem = 0
    length = digitsCount(Number)
    while Number > 0:
        rem = Number % 10
        Sum = Sum + math.pow(rem, length)
        Number = Number // 10
        length = length - 1
    return Sum


minDis = int(input("Enter the Minimum Disarium Number = "))
maxDis = int(input("Enter the Maximum Disarium Number = "))

print("\nThe List of Disarium Numbers from {0} and {1}".format(minDis, maxDis)) 
for i in range(minDis, maxDis):
    Sum = digitsSum(i)

    if Sum == i:
        print(i, end = "   ")