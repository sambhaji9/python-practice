class MyClass:
    variable = 'blah'

    def printMessage(self):
        print("This is printMessage from inside the class")

myobjectx = MyClass()
print(myobjectx.variable)
myobjectx.printMessage()