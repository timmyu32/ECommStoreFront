from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import pymongo
import json 
from bson.objectid import ObjectId
import copy
import hashlib
import jwt
import time




def isJWTvalid(req):
    authHeader = req.headers.get('Token')
    if (authHeader):
        try:
            decoded = jwt.decode(authHeader, "secret", algorithms=["HS256"])
        except:
            print('Invalid JWT')
            return None
        return req.json['user']
    else:
        return None


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017)
    mongo.server_info()
    db = mongo.shop
    print('CONNECTED TO MONGO SERVER')
except Exception as e:
    print('Failed to connect to Server')


@app.route("/api/user/usertest", methods=['GET',])
def hello_world():
    return "/usertest is successful!"


###############################################################################################
#############################   USER  


#REGISTER USER
@app.route('/api/register', methods=['POST',])
def registerUser():
    try:
        passwrd = request.json["password"]
        passwordBytes = bytes(passwrd, 'utf-8')

        user = {
            "username": request.json["username"],
            "email": request.json["email"],
            "password": hashlib.sha256(passwordBytes).hexdigest(),
            }

        retUser = copy.deepcopy(user)
        dbResponse = db['User'].insert_one(user)
        id = dbResponse.inserted_id
        # print(id)
        return Response(response= json.dumps({"message": "user created", "id": f"{id}", "user": retUser}), status=200, mimetype="application/json")
    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#LOGIN USER
@app.route('/api/login', methods=['POST',])
def loginUser():
    try:
        passwrd = request.json["password"]
        passwordBytes = bytes(passwrd, 'utf-8')
        sha256password  = hashlib.sha256(passwordBytes).hexdigest()
        retUser = db['User'].find_one({"username":request.json["username"]})

        if retUser is None:
            return Response(response= json.dumps("Wrong credentials"), status=401, mimetype="application/json")
        if retUser['password'] != sha256password:
            return Response(response= json.dumps("Wrong Password"), status=401, mimetype="application/json")

        retUser2 = copy.deepcopy(retUser)
        retUser2['_id'] = str(retUser2['_id'])
        id = retUser2['_id']
        del retUser2['password']
        
        payload = {
            "id":id,
            "exp": int(time.time()) + 2*86400
        }
        #CHANGE SECRET KEY!!!
        encoded_jwt = jwt.encode(payload, "secret", algorithm="HS256")

        return Response(response= json.dumps({"message": "user logged in", "id": f"{id}", "user": retUser2, "accessToken":encoded_jwt}), status=200, mimetype="application/json")
    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#CHANGE USER PASSWORD
@app.route('/api/user/<id>', methods=["PUT"])
def modifyUser(id):
    user = isJWTvalid(req=request) 
    print(user)
    if user is not None:
        if user['_id'] == id:
            if (request.json['user']['password']):
                passwrd = request.json['user']["password"]
                passwordBytes = bytes(passwrd, 'utf-8')
                request.json['user']['password'] = hashlib.sha256(passwordBytes).hexdigest()
                
                updatedUser = db['User'].find_one_and_update({'_id': ObjectId(request.json['user']['_id'])}, {'$set': {'password': request.json['user']['password']}})
                # print(updatedUser)
                updatedUser['_id']  = str(updatedUser['_id'])
                id = updatedUser['_id'] 
                del updatedUser['password']
                return Response(response= json.dumps({"message": "user password changed", "id": f"{id}", "user": updatedUser}), status=200, mimetype="application/json")
    else:
        return Response(response= json.dumps("Internal Server Error while changing password"), status=500, mimetype="application/json")

#DELETE USER
@app.route('/api/user/<id>', methods=["DELETE"])
def deleteUser(id):
    '''
    CHANGE SO ONLY ADMIN CAN DELETE USER
    '''
    user = isJWTvalid(req=request) 
    # print(user)
    if user is not None:
        deletedUser = db['User'].delete_one({'_id': ObjectId(request.json['user']['_id'])})
        
        return Response(response= json.dumps({"message": "user deleted", "id": f"{id}"}), status=200, mimetype="application/json")
    else:
        return Response(response= json.dumps("Internal Server Error while trying tp delete password"), status=500, mimetype="application/json")

#GET USER
@app.route('/api/user/<id>', methods=["GET"])
def getUser(id):
    '''
    CHANGE SO ONLY ADMIN CAN GET USER
    '''
    #user = isJWTvalid(req=request) 
    #if user is not None:
    try:
        gotUser = db['User'].find_one({'_id': ObjectId(id)})
        gotUser['_id']  = str(gotUser['_id'])
        del gotUser['password']
        
        return Response(response= json.dumps({"message": "user found", "id": f"{id}", "user": gotUser}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find user ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET ALL USERs
@app.route('/api/users/', methods=["GET"])
def getUAllsers():
    '''
    CHANGE SO ONLY ADMIN CAN GET USER
    '''
    #user = isJWTvalid(req=request) 
    #if user is not None:
    try:
        gotUsers = db['User'].find()
        allUsers = []
        for user in gotUsers:
            user['_id']  = str(user['_id'])
            del user['password']
            allUsers.append(user)
        
        return Response(response= json.dumps({"message": "user found",  "users": allUsers}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find user ERROR: {}".format(e)), status=500, mimetype="application/json")

'''
ADD CREATION TIME STATS TO MAKE AN END POINT THAT ANALYZES
NEW USERS PER TIME PERIOD 
'''

###############################################################################################
#############################   PRODUCT  

#CREATE PRODUCT
@app.route('/api/product/create', methods=['POST',])
def createProduct():
    '''
    CHANGE SO ONLY ADMIN CAN CREATE PRODUCT
    '''
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            newProduct = request.json['product']
            # print(newProduct)
            dbResponse = db['Product'].insert_one(newProduct)
            id = dbResponse.inserted_id
            # print(newProduct)
            newProduct["_id"] = str(newProduct["_id"])
            return Response(response= json.dumps({"message": "product created", "id": f"{id}", "product": newProduct}), status=200, mimetype="application/json")     
        else:
            return Response(response= json.dumps({"message": "user does not have proper credentials"}), status=403, mimetype="application/json")     

    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#MODIFY PRODUCT
@app.route('/api/product/edit/<id>', methods=['PUT',])
def modifyProduct(id):
    '''
    CHANGE SO ONLY ADMIN CAN CREATE PRODUCT
    '''
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            changedProduct = request.json['product']
            changedProduct["_id"] = ObjectId(changedProduct["_id"])

            result = db['Product'].replace_one({'_id': ObjectId(changedProduct["_id"])}, request.json['product'])

            changedProduct["_id"] = str(changedProduct["_id"])

            return Response(response= json.dumps({"message": "product edited", "id": f"{id}", "product": changedProduct}), status=200, mimetype="application/json")     
        else:
            return Response(response= json.dumps({"message": "user does not have proper credentials"}), status=403, mimetype="application/json")     

    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#GET PRODUCT
@app.route('/api/product/<id>', methods=['GET',])
def getProduct(id):
    '''
    CHANGE SO ONLY ADMIN CAN GET PRODUCTs
    '''
    try:
        gotProduct = db['Product'].find_one({'_id': ObjectId(id)})
        gotProduct['_id']  = str(gotProduct['_id'])
        
        return Response(response= json.dumps({"message": "product found", "id": f"{id}", "product": gotProduct}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find product ERROR: {}".format(e)), status=500, mimetype="application/json")

#DELETE PRODUCT
@app.route('/api/product/delete/<id>', methods=['DELETE',])
def deleteProduct(id):
    '''
    CHANGE SO ONLY ADMIN CAN GET PRODUCTs
    '''
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            deletedProduct = db['Product'].delete_one({'_id': ObjectId(id)})
        
        return Response(response= json.dumps({"message": "product deleted", "id": f"{id}"}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find product ERROR: {}".format(e)), status=500, mimetype="application/json")


#GET ALL PRODUCT
@app.route('/api/products/', methods=['GET',])
def getProducts():
    '''
    CHANGE SO ONLY ADMIN CAN GET PRODUCTs
    '''
    try:
        gotProducts = db['Product'].find()
        allProducts = []
        for products in gotProducts:
            products['_id']  = str(products['_id'])
            allProducts.append(products)
        
        return Response(response= json.dumps({"message": "users found",  "products": allProducts}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find user ERROR: {}".format(e)), status=500, mimetype="application/json")

###############################################################################################
#############################   CART  

#CREATE CART
@app.route('/api/cart/create', methods=['POST',])
def createCart():
   
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            newCart = request.json['cart']
            dbResponse = db['Cart'].insert_one(newCart)
            id = dbResponse.inserted_id
            newCart["_id"] = str(newCart["_id"])
            return Response(response= json.dumps({"message": "newCart created", "id": f"{id}", "cart": newCart}), status=200, mimetype="application/json")     
        else:
            return Response(response= json.dumps({"message": "user does not have proper credentials"}), status=403, mimetype="application/json")     

    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#MODIFY CART
@app.route('/api/cart/edit/<id>', methods=['PUT',])
def modifyCart(id):

    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            changedCart = request.json['cart']
            changedCart["_id"] = ObjectId(changedCart["_id"])

            result = db['Cart'].replace_one({'_id': ObjectId(changedCart["_id"])}, request.json['cart'])

            changedCart["_id"] = str(changedCart["_id"])

            return Response(response= json.dumps({"message": "product edited", "id": f"{id}", "cart": changedCart}), status=200, mimetype="application/json")     
        else:
            return Response(response= json.dumps({"message": "user does not have proper credentials"}), status=403, mimetype="application/json")     

    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#DELETE CART
@app.route('/api/cart/delete/<id>', methods=['DELETE',])
def deleteCart(id):
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            deletedCart = db['Cart'].delete_one({'_id': ObjectId(id)})
        
        return Response(response= json.dumps({"message": "cart deleted", "id": f"{id}"}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find product ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET PRODUCT
@app.route('/api/cart/<id>', methods=['GET',])
def getCart(id):

    try:
        gotCart= db['Cart'].find_one({'_id': ObjectId(id)})
        gotCart['_id']  = str(gotCart['_id'])
        
        return Response(response= json.dumps({"message": "cart found", "id": f"{id}", "cart": gotCart}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find product ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET ALL CARTS
@app.route('/api/carts/', methods=['GET',])
def getCarts():

    try:
        gotCarts = db['Cart'].find()
        allCarts = []
        for carts in gotCarts:
            carts['_id']  = str(carts['_id'])
            allCarts.append(carts)
        
        return Response(response= json.dumps({"message": "carts found",  "carts": allCarts}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find user ERROR: {}".format(e)), status=500, mimetype="application/json")


###############################################################################################
#############################   ORDERS  

#CREATE Orders
@app.route('/api/order/create', methods=['POST',])
def createOrders():
   
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            newOrder = request.json['order']
            dbResponse = db['Order'].insert_one(newOrder)
            id = dbResponse.inserted_id
            newOrder["_id"] = str(newOrder["_id"])
            return Response(response= json.dumps({"message": "newOrder created", "id": f"{id}", "cart": newOrder}), status=200, mimetype="application/json")     
        else:
            return Response(response= json.dumps({"message": "user does not have proper credentials"}), status=403, mimetype="application/json")     

    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#MODIFY Orders
@app.route('/api/order/edit/<id>', methods=['PUT',])
def modifyOrders(id):

    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            changedOrder = request.json['order']
            changedOrder["_id"] = ObjectId(changedOrder["_id"])

            result = db['Order'].replace_one({'_id': ObjectId(changedOrder["_id"])}, request.json['order'])

            changedOrder["_id"] = str(changedOrder["_id"])

            return Response(response= json.dumps({"message": "Order edited", "id": f"{id}", "cart": changedOrder}), status=200, mimetype="application/json")     
        else:
            return Response(response= json.dumps({"message": "user does not have proper credentials"}), status=403, mimetype="application/json")     

    except Exception as e:
        print(e)
        return Response(response= json.dumps(e), status=500, mimetype="application/json")

#DELETE Orders
@app.route('/api/order/delete/<id>', methods=['DELETE',])
def deleteOrders(id):
    try:
        user = isJWTvalid(req=request)
        if user is not None: 
            deletedOrder = db['Order'].delete_one({'_id': ObjectId(id)})
        
        return Response(response= json.dumps({"message": "Order deleted", "id": f"{id}"}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find product ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET Orders
@app.route('/api/order/<id>', methods=['GET',])
def getOrders(id):

    try:
        gotOrder= db['Order'].find_one({'_id': ObjectId(id)})
        gotOrder['_id']  = str(gotOrder['_id'])
        
        return Response(response= json.dumps({"message": "order found", "id": f"{id}", "cart": gotOrder}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find product ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET ALL Orders
@app.route('/api/orders/', methods=['GET',])
def getAllOrders():
    try:
        getOrders = db['Cart'].find()
        allOrders = []
        for orders in getOrders:
            orders['_id']  = str(orders['_id'])
            allOrders.append(orders)
        
        return Response(response= json.dumps({"message": "orders found",  "orders": allOrders}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find user ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET CATEGORY ITEMS
@app.route('/api/categories/3', methods=['GET',])
def getCategories():

    try:
        data = db['Data'].find()[0]['data']
        retList = []


        for item in data[3:6]:
            temp = {}
            temp['img'] = item['Images'][0]
            temp['title'] = item['Style'][0]
            retList.append(temp)
        
        return Response(response= json.dumps({"categories": retList}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find categories ERROR: {}".format(e)), status=500, mimetype="application/json")


#GET SLIDER ITEMS
@app.route('/api/slider/3', methods=['GET',])
def getSliderItems():

    try:
        data = db['Data'].find()[0]['data']
        retList = []

        for item in data[3:6]:
            temp = {}
            temp['img'] = item['Images'][0]
            temp['title'] = item['Title']
            temp['desc'] = item['Description']
            temp['bg'] = "f5fafd"

            retList.append(temp)

        return Response(response= json.dumps({"sliderData": retList}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find categories ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET POPULAR PRODUCTS
@app.route('/api/pp/<int:limit>', methods=['GET',])
def getPopularItems(limit):

    try:
        data = db['Data'].find()[0]['data']
        retList = []
        id = 0
        if limit==0:
            for item in data[0::]:
                if item is not None:
                    temp = {}
                    temp['img'] = item['Images'][0]
                    temp['id'] = id
                    id+=1
                    retList.append(temp)
        else:
            for item in data[0:limit]:
                if item is not None:
                    temp = {}
                    temp['img'] = item['Images'][0]
                    temp['id'] = id
                    id+=1
                    retList.append(temp)



        return Response(response= json.dumps({"pp": retList}), status=200, mimetype="application/json")
    except Exception as e:
        return Response(response= json.dumps("Internal Server Error while trying tp find categories ERROR: {}".format(e)), status=500, mimetype="application/json")

#GET POPULAR PRODUCTS
@app.route('/api/product/<int:id>', methods=['GET',])
def Item(id):

    # try:
    data = db['Data'].find()[0]['data']
    retList = []
    temp = {}
    temp['img'] = data[id]['Images'][0]
    temp['title'] =  data[id]['Title']
    temp['desc'] =  data[id]['Description']
    temp['price1'] =  data[id]['OriginalPrice']
    temp['size'] =  data[id]['Size']
    retList.append(temp)

    print(retList)

    return Response(response= json.dumps({"product": retList}), status=200, mimetype="application/json")
    # except Exception as e:
    #     return Response(response= json.dumps("Internal Server Error while trying tp find categories ERROR: {}".format(e)), status=500, mimetype="application/json")

if __name__ == '__main__':
    app.run(port=8000, debug=True)