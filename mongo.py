import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

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

# Insert a single document (record) into the database.
#Code below works fine. Just commented-out to avoid re-inserting more than once.
#new_doc = {'first': 'douglas', 'last': 'adams', 'dob':'11/03/1952', 'hair_colour': 'grey', 'occupation':'writer', 'nationality': 'english'}
#coll.insert(new_doc)

# Insert multiple documents into the database.
#new_docs = [ {'first': 'terry', 'last': 'pratchett', 'gender': 'm','dob':'28/04/1948', 'hair_colour': 'not much left!', 'occupation':'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'gender': 'm','dob':'20/09/1948', 'hair_colour': 'white', 'occupation':'writer', 'nationality': 'american'}]
#coll.insert_many(new_docs)

# Print out all the documents in our database.
#documents = coll.find()
#for doc in documents:
#    print(doc)

# Print out specific records e.g. where first name is 'douglas'.
#documents = coll.find({'first': 'douglas'})
#for doc in documents:
#    print(doc)

# Delete a specific record.
#coll.remove({'first': 'douglas'})
#documents = coll.find()
#for doc in documents:
#    print(doc)

# Update one record, e.g. set hair colour to 'maroon' on first record where nationality is 'american'.
#coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
#documents = coll.find({'nationality': 'american'})
#for doc in documents:
#    print(doc)

# Update many record, e.g. set hair colour to 'maroon' on first record where nationality is 'american'.
coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
documents = coll.find({'nationality': 'american'})
for doc in documents:
    print(doc)

