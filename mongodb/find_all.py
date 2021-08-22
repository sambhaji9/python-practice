import pymongo

# connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# connect to database
mydatabase = myclient["mydatabase"]

# connect to collection
mycol = mydatabase["customers"]

for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)
