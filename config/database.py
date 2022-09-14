from pymongo import MongoClient


client = MongoClient("mongodb+srv://bhavyam9133:<password>@cluster0.b9zdd78.mongodb.net/?retryWrites=true&w=majority")
db = client.test

#db = client.test

db = client.todo_app

collection_name = db["todos_app"]
