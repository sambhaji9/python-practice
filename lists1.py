fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))
print(fruits.index("banana"))
# print(fruits.index("tangerine"))

print(fruits.index("banana", 4))

fruits.reverse()
print(fruits)

fruits.append("grapes")
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)