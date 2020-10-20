import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

print(myclient.list_database_names())
