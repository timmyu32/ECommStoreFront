from flask import Flask, Response, request
import pymongo
import json 
from bson.objectid import ObjectId

app = Flask(__name__)



try:
    mongo = pymongo.MongoClient(host="localhost", port=27017)
    mongo.server_info()
    db = mongo.company
except Exception as e:
    print('Failed to connect to Server')


       
###      CREATE 
@app.route("/users", methods=['POST'])
def create_user():
    # try:
    print(request.json)
    print(request.get_json())

    print(type(request.json))
    input(dir(request))
    user = {
        "name": request.body["name"],
        "lastname": request.form["lastname"]
        }

    dbResponse = db.users.insert_one(user)
    id = dbResponse.inserted_id
    return Response(response= json.dumps({"message": "user created", "id": f"{id}"}), status=200, mimetype="application/json")
    # except Exception as e:
    #     print(e)


###     READ 
@app.route('/users', methods=["GET"])
def read_user():
    try:
        data = list(db.users.find())
        for user in data:
            user['_id'] = str(user['_id'])

        return Response(response= json.dumps(data), status=200, mimetype="application/json")
    except Exception as e:
        print(e)
        return Response(response= json.dumps({"Error": f"{e}"}), status=500, mimetype="application/json")

    
###      UPDATE 
@app.route('/users/<id>', methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"name": request.form["name"]}}
        )
        return Response(response= json.dumps({"message": "user updated"}), status=200, mimetype="application/json")
    except Exception as e:
        print(e)
        return Response( response= json.dumps({"Error": f"{e}"}), status=500, mimetype="application/json")


###      DELEET 
@app.route('/users/<id>', methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(response= json.dumps({"message": f"user deleted id:{id}"}), status=200, mimetype="application/json")
        else:
            return Response(response= json.dumps({"message": f"user not found... id:{id}"}), status=200, mimetype="application/json")
    except Exception as e:
        print(e)
        return Response(response= json.dumps({"Error": f"{e}"}), status=500, mimetype="application/json")


if __name__ == '__main__':
    app.run(port=8000, debug=True)