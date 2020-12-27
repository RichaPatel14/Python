import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

list = [
    {"_id": 1, "name": "Richa", "Country: "Canada"},
    {"_id": 2, "name": "Darshil", "Country: "India"}
]
x = mycol.insert_many(list)

if x:
    print("Enter Successfully")
    print(x.inserted_ids)
