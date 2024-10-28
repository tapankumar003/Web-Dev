from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:toor@cluster1.p7ukl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1')
db = client.dbtst1

# db.books.insert_one({
#     'title': 'Harry Potter',
#     'author': 'J.K. Rowling',
#     'rating': 90
# })

# db.books.insert_one({
#     'title': 'The Fisherman and the Fish',
#     'author': 'Joseph Choi',
#     'rating': 10
# })

# db.books.insert_one({
#     'title': 'Fire in the Water',
#     'author': 'Some Dude',
#     'rating': 57
# })


# db.books.update_one(
#     {'title': 'The Fisherman and the Fish'},
#     {'$set': {'author': 'Jimmy Kim'}}
# )



db.books.delete_one({'rating': 90})