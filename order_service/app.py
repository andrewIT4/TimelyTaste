from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import os
import sys
import datetime
import pika

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
    cluster = MongoClient(CONNECTION_STRING)
    print(cluster.server_info())  # connect to the server and get and print the server info of the mongoDB
# Error message will be printed when unsuccessful to connect to the mongoDB server
# due to incorrect environment variables inserted in the command or the mongoDB server is not available at the moment
except:
    print('Access Failed. One or more environment variables are incorrect or the MongoDB server is down . Please try '
          'again later')
    sys.exit(1)

# Get and initialise the COMP3122Project Database
db = cluster.order_db
app = Flask(__name__)


@app.route('/order_api/orders', methods=['GET'])
def get_orders(order_id=None):
    output = []
    result = list(db.order.find({}, {'_id': 0}).sort("order_id", 1))
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


@app.route('/order_api/orders/<order_id>', methods=['GET'])
def get_orders_by_id(order_id):
    output = []
    query = {"order_id": order_id}
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
@app.route('/order_api/orders/unpaid', methods=['GET'])
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
@app.route('/order_api/orders/shipping', methods=['GET'])
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
@app.route('/order_api/orders/delivered', methods=['GET'])
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
@app.route('/order_api/orders', methods=['POST'])
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
        addMessage("Create "+ str(len(result) + 1 ))
        return jsonify({"message": "Order created Successfully"}), 201
    except KeyError:
        return jsonify({'message': 'Some Key is missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


# update order
@app.route('/order_api/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        query = {
            'order_id': order_id
        }
        newValues = {
            "$set": {
                'menu': data['menu'],
                'drinks': data['drinks'],
                'order_time': datetime.datetime.now()
            }
        }
        result = db.order.update_one(query, newValues)
        if result.modified_count > 0:
            return jsonify({"message": "Order Update Successfully"}), 202
        elif result.matched_count > 0:
            return jsonify({"message": "Menu datas are same"}), 409
        else:
            return jsonify({"message": "No such order data"}), 404
    except KeyError:  # missing student id
        return jsonify({'message': 'Key Value are missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


# update order status
@app.route('/order_api/orders/<order_id>', methods=['PATCH'])
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
            return jsonify({"message": "Order Update Successfully"}), 202
        elif result.matched_count > 0:
            return jsonify({"message": "Order Status is same"}), 409
        else:
            return jsonify({"message": "No such order data"}), 404
    except KeyError:  # missing student id
        return jsonify({'message': 'Key Values are missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


# delete order
@app.route('/order_api/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        query = {
            'order_id': order_id
        }
        result = db.order.delete_one(query)
        if result.deleted_count > 0:
            return jsonify({"message": "order delete Successfully"}), 202
        else:
            return jsonify({"message": "No such order data"}), 404
    except:
        return jsonify({"message": "unknown error"}), 501


def addMessage(cmd):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=cmd,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15004, debug=True)
