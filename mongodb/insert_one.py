import pymongo

# connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# connect to database
mydb = myclient["mydatabase"]

# connect to collection
mycol = mydb["customers"]

mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)

print(x.inserted_id)