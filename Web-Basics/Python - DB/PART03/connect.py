from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:root@cluster0.0vslw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbtest

doc = {
    'name':'Rock',
    'age':25
}

db.users.insert_one(doc)