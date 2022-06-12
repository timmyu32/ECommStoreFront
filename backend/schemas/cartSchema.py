from flask import Flask, Response, request
import pymongo
from pymongo.errors import CollectionInvalid
import json 
from bson.objectid import ObjectId


app = Flask(__name__)

db = pymongo.MongoClient(host="localhost", port=27017)['shop']

cart_schema = {
    "userID": {
        "type": "string",
        'required': True,

    },
    "products": {
        "type": "array",
    }
}


collection = 'Cart'
validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
required = []
unique = []

for field_key in cart_schema:
    field = cart_schema[field_key]
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




