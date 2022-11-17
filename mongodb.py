import pymongo

client = pymongo.MongoClient("mongodb+srv://Bhavik104:Bha301095vik@bhavik.z4hoewi.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d= {
   "name": "bhavik",
   "email":"bhaviksheth104@gmail.com",
    "surname" : "Sheth"
}

db1 = client['mongotest']
coll = db1["test"]
coll.insert_one(d)