phonebook = {}
phonebook["sambhaji"] = 9890233414
phonebook["sadhana"] = 9370100212

print(phonebook)

phonebook1 = {
    "sambhaji": 9890233414,
    "sadhana": 9370100212,
    "satyam": 9265456587
}
print(phonebook1)

for name, value in phonebook.items():
    print("Phone number of %s is %d" % (name, value))

del phonebook1["satyam"]
print(phonebook1)