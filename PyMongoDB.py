import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

dict = {
    "name": "Richa",
    "Country: "Canada",
}
x = mycol.insert_one(dict)

if x:
    print("Enter Successfully")
