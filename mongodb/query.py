import pymongo

# connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# connect to database
mydatabase = myclient["mydatabase"]

# connect to collection
mycol = mydatabase["customers"]

# query1
myquery = {"address": "Valley 345"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# query2
myquery1 = {"address": {"$gt": "P"}}
mydoc1 = mycol.find(myquery1)

for x1 in mydoc1:
    print(x1)

# query3
myquery2 = {"address": {"$regex": "^S"}}
mydoc2 = mycol.find(myquery2)

for x2 in mydoc2:
    print(x2)