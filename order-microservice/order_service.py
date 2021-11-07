from flask import Flask, jsonify, request, abort
from flask_pymongo import pymongo
import os
import sys

app = Flask(__name__)
# set this configuration key to true for pretty printing
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# specify the URL address by passing the environment variables for connection
client = pymongo.MongoClient('mongodb://' + os.environ['MONGO_USERNAME'] + ':' + os.environ['MONGO_PASSWORD'] + '@' + os.environ['MONGO_SERVER_HOST'] + ':' + os.environ['MONGO_SERVER_PORT'] + '/' , authSource='admin')
# specify the name of database
db = client['order_service']
cart = db['cart']
order = db['order']

@app.route('/orders', methods=['GET'])
@app.route('/order/<order_id>', methods=['GET'])
def get_orders(order_id=None):

    return 1


# get the orders unbilled
@app.route('/orders/unbilled', methods=['GET'])
def get_unbilled_orders():

    return 1


# get the orders unshipped
@app.route('/orders/unshipped', methods=['GET'])
def get_unshipped_orders():

    return 1


# get the orders delivered
@app.route('/orders/delivered', methods=['GET'])
def get_delivered_orders():

    return 1


# create order
@app.route('/order', methods=['POST'])
def create_order():

    return 1


# update order
@app.route('/order/<order_id>', methods=['PUT'])
def update_order(order_id):

    return 1


# delete order
@app.route('/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):

    return 1


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000, debug=True)