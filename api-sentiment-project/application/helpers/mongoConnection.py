from pymongo import MongoClient

client = MongoClient()
db = client.Aidos

def read_coll(collection,query,client=client):
    res = db[collection].find(query)
    return list(res)

def write_coll(collection, obj,client=client):
    res = db[collection].insert_one(obj)
    return res

def delete_coll(collection, query, client=client):
    res = db[collection].delete_one(query)
    return res


def update_coll(collection, query, update,client=client):
    setting = {"$set":update}
    res = db[collection].update_one(query,setting)
    return res