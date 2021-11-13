from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import os
import sys
import datetime

app = Flask(__name__)
# set this configuration key to true for pretty printing
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# specify the URL address by passing the environment variables for connection
username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
hostAddress = os.getenv('MONGO_SERVER_HOST')
port = os.getenv('MONGO_SERVER_PORT')

client = CONNECTION_STRING = f'mongodb://{username}:{password}@{hostAddress}:{port}'
# specify the name of database
try:
    db = MongoClient['order_service']
    cart = db['cart']
    order = db['order']
except:
    print('Access Failed. One or more environment variables are incorrect or the MongoDB server is down . Please try '
          'again later')
    sys.exit(1)


@app.route('/orders', methods=['GET'])
@app.route('/order/<order_id>', methods=['GET'])
def get_orders(order_id=None):
    output = []
    query = {} if order_id is None else {"order": order_id}
    result = list(db.order.find(query, {'_id': 0}).sort("order_id", 1))
    # If the list is not empty
    if len(result) > 0:
        for x in result:
            print(x, flush=True)
            output.append(x)
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'order not found'}), 404


# get the orders unbilled
@app.route('/orders/unpaid', methods=['GET'])
def get_unpaid_orders():
    output = []
    query = {"status": "unpaid"}
    result = list(db.order.find(query, {'_id': 0}).sort("order_id", 1))
    # If the list is not empty
    if len(result) > 0:
        for x in result:
            print(x, flush=True)
            output.append(x)
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'order not found'}), 404


# get the orders unshipped
@app.route('/orders/shipping', methods=['GET'])
def get_unshipped_orders():
    output = []
    query = {"status": "shipping"}
    result = list(db.order.find(query, {'_id': 0}).sort("order_id", 1))
    # If the list is not empty
    if len(result) > 0:
        for x in result:
            print(x, flush=True)
            output.append(x)
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'order not found'}), 404


# get the orders delivered
@app.route('/orders/delivered', methods=['GET'])
def get_delivered_orders():
    output = []
    query = {"status": "delivered"}
    result = list(db.order.find(query, {'_id': 0}).sort("order_id", 1))
    # If the list is not empty
    if len(result) > 0:
        for x in result:
            print(x, flush=True)
            output.append(x)
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'order not found'}), 404


# create order
@app.route('/order', methods=['POST'])
def create_order():
    try:
        data = request.json

        result = list(db.order.find({}, {'_id': 0}).sort("order_id", 1))
        query = {
            'order_id': len(result) + 1,
            'username': data['username'],
            'store_id': data['store_id'],
            'status': 'unpaid',
            'menu': data['menu'],
            'drinks': data['drinks'],
            'order_time': datetime.datetime.now()
        }
        db.order.insert_one(query)
        return jsonify({"message", "Order created Successfully"}), 201
    except KeyError:
        return jsonify({'message': 'Some Key is missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


# update order
@app.route('/order/<order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        query = {
            'order_id': order_id
        }
        newValues = {
            "$set": {
                'menus': data['menus'],
                'drinks': data['drinks'],
                'order_time': datetime.datetime.now()
            }
        }
        result = db.order.update_one(query, newValues)

        if result.modified_count > 0:
            return jsonify({"message", "Order Update Successfully"}), 202
        else:
            return jsonify({"message", "No such order data"}), 404
    except KeyError:  # missing student id
        return jsonify({'message': 'Order id is missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


# update order status
@app.route('/order/<order_id>', methods=['PATCH'])
def update_order_status(order_id):
    try:
        data = request.json
        query = {
            'order_id': order_id
        }
        newValues = {
            "$set": {
                'status': data['status'],
                'update_time': datetime.datetime.now()
            }
        }
        result = db.order.update_one(query, newValues)

        if result.modified_count > 0:
            return jsonify({"message", "Order Update Successfully"}), 202
        else:
            return jsonify({"message", "No such order data"}), 404
    except KeyError:  # missing student id
        return jsonify({'message': 'Order id is missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


# delete order
@app.route('/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        query = {
            'order_id': order_id
        }
        result = db.order.delete_one(query)
        if result.count > 0:
            return jsonify({"message", "order delete Successfully"}), 202
        else:
            return jsonify({"message", "No such order data"}), 404
    except:
        return jsonify({"message": "unknown error"}), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000, debug=True)