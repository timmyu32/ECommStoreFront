import pymongo


try:
    mongo = pymongo.MongoClient(host="localhost", port=27017)
    mongo.server_info()
    db = mongo.shop
    print('CONNECTED TO MONGO SERVER')
except Exception as e:
    print('Failed to connect to Server')

data = db['Data'].find()[0]['data']
retList = []


for item in data[0:3]:
    # print(item)
    temp = {}
    temp['img'] = item['Images'][0]
    temp['title'] = item['Style'][0]
    retList.append(temp)

print(retList)