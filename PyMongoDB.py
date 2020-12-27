import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']


def insert(val):
    x = mycol.insert_one(val)
    print(x.inserted_id)


def find(val):
    for x in mycol.find(val):
        print(x)


def delete(val):
    x = mycol.delete_one(val)
    print(x.deleted_count)


def update(val, nval):
    x = mycol.update_one(val, nval)
    if x:
        print("Successfully Update")


y = input("What you want insert/delete/find/Update: ")
if y.upper() == "INSERT":
    x = 0
    for x in mycol.find({}, {"_id": 1}):
        pass
    x = x['_id'] + 1

    val = {
        "_id": x, "name": input("Enter your name: "), "Country": input("Enter Your Country: ")
    }
    insert(val)
elif y.upper() == "DELETE":
    val = {"name": input("Enter your name: ")}
    delete(val)
elif y.upper() == "FIND":
    val = {"name": input("Enter your name: ")}
    find(val)
elif y.upper() == "UPDATE":
    val = {"name": input("Enter your name: ")}
    nval = {"$set": {"Country": input("Enter your Country: ")}}
    update(val, nval)
else:
    print("Please enter Insert/Delete/Find: ")
