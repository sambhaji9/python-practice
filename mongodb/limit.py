import pymongo

# connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# connect to database
mydatabase = myclient["mydatabase"]

# connect to collection
mycol = mydatabase["customers"]

myresult = mycol.find().sort("name").limit(5)

# print the result
for x in myresult:
    print(x)
