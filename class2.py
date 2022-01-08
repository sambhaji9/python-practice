class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append( trick )

d = Dog("Fido")
e = Dog("Sheru")

# print(d.kind)
# print(d.name)

# print(e.kind)
# print(e.name)

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)
print(e.tricks)