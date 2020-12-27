import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"name": "Darshil"}

mycol.delete_many(myquery)

for x in mycol.find():
    print(x)
