from pymongo import MongoClient
import json

def save_to_mongodb(payload):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sensor"]
    collection = db["sensor_data"]

    collection.insert_one(payload)
    client.close()


def show_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sensor"]
    collection = db["sensor_data"]

    for doc in collection.find({},{"_id":0}):
        print(doc)
    client.close()


def reset_mongodb():
    client = MongoClient("localhost", 27017)
    client.drop_database("sensor_data")  
    print("MongoDB reset complete.")


#reset_mongodb()
#show_mongodb()