from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:toor@cluster1.p7ukl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1')
db = client.dbtst1

# doc3 = {
#     'name':'Henny',
#     'age':21
# }

# doc4 = {
#     'name':'Leena',
#     'age':22
# }

# db.urs.insert_one(doc3)
# db.urs.insert_one(doc4)

# all_users = list(db.urs.find({},{'_id':False}))

# print(all_users)
# print(all_users[0])
# print(all_users[0]['name'])

# for ur in all_users:
#     print(ur)

# user = db.urs.find_one({'name':'Sonny'})
# print(user)

# db.urs.update_one({'name':'Henny'},{'$set':{'age':19}})

# user = db.urs.find_one({'name':'Henny'})
# print(user)

# db.urs.delete_one({'name':'Sonny'})

# user = db.urs.find_one({'name':'Sonny'})
# print(user)