from pymongo import MongoClient

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, using the connection strings
client = MongoClient("mongodb://localhost:27017")

db = client.admin

# issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
