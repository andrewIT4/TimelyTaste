from flask import Flask, jsonify, request
from flask_pymongo import pymongo
from werkzeug.exceptions import HTTPException
import os
import sys

app = Flask(__name__)
# set this configuration key to true for pretty printing
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# specify the URL address by passing the environment variables for connection
client = pymongo.MongoClient('mongodb://' + os.environ['MONGO_USERNAME'] + ':' + os.environ['MONGO_PASSWORD'] + '@' + os.environ['MONGO_SERVER_HOST'] + ':' + os.environ['MONGO_SERVER_PORT'] + '/' , authSource='admin')
# specify the name of database

db = client['cart_service']
cart = db['cart']

# function to check if no records are found or no specified ID is found
def test_empty(data):
    test = list(data)
    if len(test) == 0:
        return 1
    else:
        return 0

@app.route('/cart_api/carts', methods=['GET'])
@app.route('/cart_api/cart/<cart_id>', methods=['GET'])
def get_carts(cart_id=None):
    item = {}
    data = []
    test = test_empty(cart.find())
    # if no records, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    if cart_id == None:
        all_carts = cart.find()
        # format the output for each information and put each of them into a array iteratively 
        for todo in all_carts:
            item = {
                'cart_id' : todo['cart_id'],
                'customer_id' : todo['customer_id'],
                'product_ids' : todo['product_ids'],
            }
            data.append(item)
        # return the sorted data in json format with 200 response
        return jsonify(data), 200
    myquery = { 'cart_id': cart_id }
    # check if no record is found
    test = test_empty(cart.find(myquery))
    # if no record, return error message with 404 response
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    spec_cart = cart.find(myquery)
    # format the output for the information and put it into a array
    for todo in spec_cart:
        item = {
            'cart_id' : todo['cart_id'],
            'customer_id' : todo['customer_id'],
            'product_ids' : todo['product_ids'],
        }
        data.append(item)
    # return the data in json format with 200 response
    return jsonify(data), 200


@app.route('/cart_api/cart', methods=['POST'])
def create_cart():
    content = request.json
    if "cart_id" not in content or "customer_id" not in content or "product_ids" not in content: 
        error = {'error' : 'missing keys of json data'}
        return jsonify(error), 400
    myquery = { 'cart_id': content['cart_id']}
    test = test_empty(cart.find(myquery))
    if test == 1:
        cart.insert_one(content)
        success = {'success' : 'a specified cart is added'}
        return jsonify(success), 201
    error = {'error' : 'order with same cart_id already existed'}
    return jsonify(error), 400
    

@app.route('/cart_api/cart/<cart_id>', methods=['PUT'])
def update_cart(cart_id):
    content = request.json
    if "cart_id" not in content or "customer_id" not in content or "product_ids" not in content: 
        error = {'error' : 'missing keys of json data'}
        return jsonify(error), 400
    if content['cart_id'] != cart_id:
        error = {'error' : 'the student ID entered in endpoint and json object are not the same'}
        return jsonify(error), 400
    myquery = { 'cart_id': cart_id }
    test = test_empty(cart.find(myquery))
    if test == 1:
        cart.insert_one(content)
        success = {'success' : 'a specified cart is added'}
        return jsonify(success), 201
    else:
        cart.find_one_and_update({"cart_id": cart_id}, {"$set": content})
        success = {'success' : 'a specified cart is updated'}
        return jsonify(success), 200


@app.route('/cart_api/cart/<cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    myquery = { 'cart_id': cart_id }
    test = test_empty(cart.find(myquery))
    if test == 1:
        error = {'error' : 'not found'}
        return jsonify(error), 404
    cart.delete_one({'cart_id':cart_id})
    success = {'success' : 'a specified cart is deleted'}
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
    app.run(host="0.0.0.0", port=15001, debug=True)