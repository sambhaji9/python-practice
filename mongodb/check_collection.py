import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]

collist = mydb.list_collection_names()
print(collist)

if "customers" in collist:
    print("The collection exists.")
else:
    print("The collection do not exists.")