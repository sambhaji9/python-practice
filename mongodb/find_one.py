import pymongo

# connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# connect to list_database
mydatabase = myclient["mydatabase"]

# connect to collections
mycol = mydatabase["customers"]

print(mycol.find_one())
