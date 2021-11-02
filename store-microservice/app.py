from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import os
import sys

username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
hostAddress = os.getenv('MONGO_SERVER_HOST')
port = os.getenv('MONGO_SERVER_PORT')

# Application will print error message and exit when one of the environment variables is not inserted in the
# execution command
if username is None or password is None or hostAddress is None or port is None:
    print("One of more environment variables is not provided in the execution command\nThe Application will exit now.")
    sys.exit(1)

CONNECTION_STRING = f'mongodb://{username}:{password}@{hostAddress}:{port}'

try:
    cluster = MongoClient(CONNECTION_STRING)
    print(cluster.server_info())  # connect to the server and get and print the server info of the mongoDB
# Error message will be printed when unsuccessful to connect to the mongoDB server
# due to incorrect environment variables inserted in the command or the mongoDB server is not available at the moment
except:
    print('Access Failed. One or more environment variables are incorrect or the MongoDB server is down . Please try '
          'again later')
    sys.exit(1)

# Get and initialise the store_db Database
db = cluster.store_db
app = Flask(__name__)


def storesResultToList(stores):
    result = []  # initialise empty result list
    # Convert the query result records into a single object and append into the result list one by one
    for s in stores:
        result.append({'store_id': s['store_id'],
                       'store_name': s['store_name']
                       })
    return result


@app.route('/stores', methods=['GET'])
def get_stores():
    stores = db.store.find({}, {'_id': 0}).sort("store_id", 1)
    result = storesResultToList(stores)

    # If the list is not empty
    if len(result) > 0:
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'not found'}), 404


@app.route('/stores/<store_id>)', methods=['GET'])
def get_stores(store_id):
    query = {'store_id': store_id}
    stores = db.store.find(query, {'_id': 0}).sort("store_id", 1)
    result = storesResultToList(stores)

    # If the list is not empty
    if len(result) > 0:
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'not found'}), 404


@app.route('/stores', methods=['POST'])
def create_store():
    data = request.json
    store = data.find_one({"store_id": data})  # query by specified username
    if store:  # user exists
        return jsonify({"msg": "Store already exists"}), 401
    try:
        query = {
            'store_id': data['store_id'],
            'store_name': data['store_name']
        }
        db.store.insert_one(query)
        return jsonify({"message", "Store created Successfully"}), 201
    except:
        abort(405)


@app.route('/stores/<store_id>', methods=['PUT'])
def update_store(store_id):
    data = request.json
    query = {
        'store_id': store_id
    }
    newValues = {
        "$set": {
            'store_name': data['store_name']
        }
    }
    result = db.store.update_one(query,newValues)
    if result.modified_count > 0:
        return jsonify({"message", "Store delete Successfully"}), 202
    else:
        return jsonify({"message", "No such store data"}), 404


@app.route('/stores/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    query = {
        'store_id': store_id
    }
    result = db.store.delete_one(query)
    if result.count > 0:
        return jsonify({"message", "Store delete Successfully"}), 202
    else:
        return jsonify({"message", "No such store data"}), 404


@app.errorhandler(405)
def error_405(error):
    response = dict(error="Error")
    return jsonify(response), 405