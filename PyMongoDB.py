import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"Country": "India"}
new = {"$set": {"Country": "Canada"}}

mycol.update_one(myquery, new)

for x in mycol.find():
    print(x)
