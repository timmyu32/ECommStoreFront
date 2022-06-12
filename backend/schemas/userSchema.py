from flask import Flask, Response, request
import pymongo
from pymongo.errors import CollectionInvalid
import json 
from bson.objectid import ObjectId


app = Flask(__name__)


# try:
#     client = pymongo.MongoClient(host="localhost", port=27017)
#     client.server_info()
#     mydb = client.prototypeShop
#     userCollection = mydb.User
#     print('CONNECTED TO MONGO SERVER')
#     userSchema = {

#     }

#     #userCollection.insert_many(user_schema)

# except Exception as e:
#     print('Failed to connect to Server')



db = pymongo.MongoClient(host="localhost", port=27017)['shop']

user_schema = {
    "username": {
        "type": "string",
        'required': True,
        "unique": True,
    },
    "email": {
        "type": "string",
        'required': True,
        "unique": True,
    },
    "password": {
       "type": "string",
        'required': True,
    },
    "isAdmin": {
        "type": "boolean"
    }
}


collection = 'User'
validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
required = []
unique = []

for field_key in user_schema:
    field = user_schema[field_key]
    properties = {'bsonType': field['type']}
    minimum = field.get('minlength')

    if type(minimum) == int:
        properties['minimum'] = minimum

    if field.get('required') is True: required.append(field_key)
    if field.get('unique') is True: unique.append(field_key)


    validator['$jsonSchema']['properties'][field_key] = properties

if len(required) > 0:
    validator['$jsonSchema']['required'] = required
if len(unique) > 0:
    validator['$jsonSchema']['unique'] = unique

query = [('collMod', collection),
         ('validator', validator)]

try:
    db.create_collection(collection)
except Exception as e:
    print(e)




