import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"Country": "Canada"}

for x in mycol.find(myquery):
    print(x)

