import pymongo

# connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# connect to list_database
mydatabase = myclient["mydatabase"]

# connect to collections
mycol = mydatabase["customers"]

# ascending sort
mydoc = mycol.find().sort("name")

print("\n")
print("Sorting in ascending order")
for x in mydoc:
    print(x)

# descending sort
mydoc1 = mycol.find().sort("name", -1)

print("\n")
print("Sorting in descending order")
for x1 in mydoc1:
    print(x1)