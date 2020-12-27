import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"Country": {"$gt": "C"}}

for x in mycol.find(myquery):
    print(x)

