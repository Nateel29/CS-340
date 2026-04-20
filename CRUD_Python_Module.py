# Example Python Code to Insert a Document 
### Updated 04/17/2026 by Allan Torres
from pymongo import MongoClient
from pymongo.errors import PyMongoError
 
from bson.objectid import ObjectId 

class AnimalShelterCRUD(object):
 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        #
        # You must edit the password below for your environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(
            f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin"
        )
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            return list(self.collection.find(query))
        else:
            raise Exception("Query must be provided")

    # -----------------------------------------------------------
    # UPDATE — Modify document(s) in the collection
    # -----------------------------------------------------------
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Error updating document:", e)
                return 0
        else:
            raise Exception("Query and new_values must be provided")

    # -----------------------------------------------------------
    # DELETE — Remove document(s) from the collection
    # -----------------------------------------------------------
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Error deleting document:", e)
                return 0
        else:
            raise Exception("Query must be provided")
