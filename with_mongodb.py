from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access database and collection
db = client["your_database"]
collection = db["your_collection"]

# Find documents
docs = collection.find()
for doc in docs:
    print(doc)


# Insert Data
collection.insert_one({"name": "Aniket", "age": 21})

# Update Data

collection.update_one({"name": "Aniket"}, {"$set": {"age": 22}})
