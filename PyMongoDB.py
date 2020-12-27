import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

list = [
    {"name": "Richa", "Country: "Canada"},
    {"name": "Darshil", "Country: "India"}
]
x = mycol.insert_many(list)

if x:
    print("Enter Successfully")
