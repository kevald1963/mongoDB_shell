import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("MongoDB is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Connect to the database passing in the environment variable set up with the connection string.
conn = mongo_connect(MONGODB_URI)

# Set our collection name on this database.
coll = conn[DBS_NAME][COLLECTION_NAME]

# Print out all the documents in our database.
documents = coll.find()
for doc in documents:
    print(doc)
