from flask import Flask, jsonify, request
from flask_pymongo import pymongo
from pymongo import errors
from werkzeug.exceptions import HTTPException
import os
import sys

app = Flask(__name__)
# set this configuration key to true for pretty printing
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# specify the URL address by passing the environment variables for connection
client = pymongo.MongoClient('mongodb://' + os.environ['MONGO_USERNAME'] + ':' + os.environ['MONGO_PASSWORD'] + '@' + os.environ['MONGO_SERVER_HOST'] + ':' + os.environ['MONGO_SERVER_PORT'] + '/' , authSource='admin')
# specify the name of database
db = client['order_service']
order = db['order']

try:
   client.admin.command('ismaster')
except errors.PyMongoError as err:
   print('Server not available: %s' % err)
   exit()

# function to check if no records are found or no specified ID is found
def test_empty(data):
    test = list(data)
    if len(test) == 0:
        return 1
    else:
        return 0


@app.route('/order_api/orders', methods=['GET'])
@app.route('/order_api/order/<order_id>', methods=['GET'])
def get_orders(order_id=None):
    item = {}
    data = []
    test = test_empty(order.find())
    # if no records, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    if order_id == None:
        all_orders = order.find()
        # format the output for each information and put each of them into a array iteratively 
        for todo in all_orders:
            item = {
                'order_id' : todo['order_id'],
                'cart_id' : todo['cart_id'],
                'status' : todo['status'],
            }
            data.append(item)
        # return the sorted data in json format with 200 response
        return jsonify(data), 200
    myquery = { 'order_id': order_id }
    # check if no record is found
    test = test_empty(order.find(myquery))
    # if no record, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    spec_order = order.find(myquery)
    # format the output for the information and put it into a array
    for todo in spec_order:
        item = {
            'order_id' : todo['order_id'],
            'cart_id' : todo['cart_id'],
            'status' : todo['status'],
        }
        data.append(item)
    # return the data in json format with 200 response
    return jsonify(data), 200


# get the orders unbilled
@app.route('/order_api/orders/unbilled', methods=['GET'])
def get_unbilled_orders():
    item = {}
    data = []
    test = test_empty(order.find())
    # if no records, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    myquery = { 'status': "unbilled" }
    spec_order = order.find(myquery)
    # format the output for the information and put it into a array
    for todo in spec_order:
        item = {
            'order_id' : todo['order_id'],
            'cart_id' : todo['cart_id'],
            'status' : todo['status'],
        }
        data.append(item)
    # return the data in json format with 200 response
    return jsonify(data), 200


# get the orders unshipped
@app.route('/order_api/orders/unshipped', methods=['GET'])
def get_unshipped_orders():
    item = {}
    data = []
    test = test_empty(order.find())
    # if no records, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    myquery = { 'status': "billed" }
    spec_order = order.find(myquery)
    # format the output for the information and put it into a array
    for todo in spec_order:
        item = {
            'order_id' : todo['order_id'],
            'cart_id' : todo['cart_id'],
            'status' : todo['status'],
        }
        data.append(item)
    # return the data in json format with 200 response
    return jsonify(data), 200


# get the orders shipping
@app.route('/order_api/orders/shipping', methods=['GET'])
def get_shipping_orders():
    item = {}
    data = []
    test = test_empty(order.find())
    # if no records, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    myquery = { 'status': "shipping" }
    spec_order = order.find(myquery)
    # format the output for the information and put it into a array
    for todo in spec_order:
        item = {
            'order_id' : todo['order_id'],
            'cart_id' : todo['cart_id'],
            'status' : todo['status'],
        }
        data.append(item)
    # return the data in json format with 200 response
    return jsonify(data), 200


# get the orders delivered
@app.route('/order_api/orders/delivered', methods=['GET'])
def get_delivered_orders():
    item = {}
    data = []
    test = test_empty(order.find())
    # if no records, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    myquery = { 'status': "delivered" }
    spec_order = order.find(myquery)
    # format the output for the information and put it into a array
    for todo in spec_order:
        item = {
            'order_id' : todo['order_id'],
            'cart_id' : todo['cart_id'],
            'status' : todo['status'],
        }
        data.append(item)
    # return the data in json format with 200 response
    return jsonify(data), 200

# create order
@app.route('/order_api/order', methods=['POST'])
def create_order():
    content = request.json
    if "order_id" not in content or "cart_id" not in content or "status" not in content: 
        error = {'error' : 'missing keys of json data'}
        return jsonify(error), 400
    myquery = { 'order_id': content['order_id']}
    test = test_empty(order.find(myquery))
    if test == 1:
        order.insert_one(content)
        success = {'success' : 'a specified order is added'}
        return jsonify(success), 201
    error = {'error' : 'order with same order_id already existed'}
    return jsonify(error), 400


# update order
@app.route('/order_api/order/<order_id>', methods=['PUT'])
def update_order(order_id):
    content = request.json
    if "order_id" not in content or "cart_id" not in content or "status" not in content: 
        error = {'error' : 'missing keys of json data'}
        return jsonify(error), 400
    if content['order_id'] != order_id:
        error = {'error' : 'the student ID entered in endpoint and json object are not the same'}
        return jsonify(error), 400
    myquery = { 'order_id': order_id }
    test = test_empty(order.find(myquery))
    if test == 1:
        order.insert_one(content)
        success = {'success' : 'a specified order is added'}
        return jsonify(success), 201
    else:
        order.find_one_and_update({"order_id": order_id}, {"$set": content})
        success = {'success' : 'a specified order is updated'}
        return jsonify(success), 200


# delete order
@app.route('/order_api/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    myquery = { 'order_id': order_id }
    test = test_empty(order.find(myquery))
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    order.delete_one({'order_id':order_id})
    success = {'success' : 'a specified order is deleted'}
    return jsonify(success), 200


@app.errorhandler(Exception)
# handle 500 and global errors
def handle_exception(e):
    code = 500
    if ":" in str(e):
        temp, message = str(e).split(': ', 1)
    else:
         message = str(e)
    if isinstance(e, HTTPException):
        code = e.code
    error = {'error' : message}
    return jsonify(error), code

@app.errorhandler(405)
# handle 405 errors
def method_not_allowed(e):
    error = {'error': 'the method is not allowed'}
    return jsonify(error), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000, debug=True)