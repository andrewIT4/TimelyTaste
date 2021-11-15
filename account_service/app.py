from flask import Flask, request, jsonify, abort
import pymongo
import json
import os
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
jwt = JWTManager()

#  set JWT secretkey
app.config['JWT_SECRET_KEY'] = 'TimelyTaste'
jwt.init_app(app)

# Make connection to MongoDB with the Environment Variables
username = os.environ.get('MONGO_USERNAME')
password = os.environ.get('MONGO_PASSWORD')
hostname = os.environ.get('MONGO_SERVER_HOST')
hostname = hostname.replace("\'", "")
port = os.environ.get('MONGO_SERVER_PORT')
port = port.replace("\'", "")
connStr = 'mongodb://%s:%s@%s:%s/' % (username, password, hostname, port)

conn = pymongo.MongoClient(connStr)
user_account = conn["user_account"]
customer = user_account['customer']


@app.route('/account_api/accounts', methods=['GET'])
def get_account():
    output = []
    result = list(customer.find({}, {'_id': 0}).sort("username", 1))
    # If the list is not empty
    if len(result) > 0:
        for x in result:
            print(x, flush=True)
            output.append(x)
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'not found'}), 404


@app.route('/account_api/accounts/<username>', methods=['GET'])
def get_account_by_username(username):
    output = []
    query = {'username': username}
    result = list(customer.find(query, {'_id': 0}).sort("username", 1))
    if len(result) > 0:
        for x in result:
            print(x, flush=True)
            output.append(x)
        # Convert the list of records into json format and return
        return jsonify(result), 200
    else:  # If the list is empty
        # Convert the error message into json format and return
        return jsonify({'error': 'not found'}), 404


@app.route('/account_api/accounts/<username>', methods=['PUT'])
def update_customer(username):
    try:
        data = request.json
        query = {
            'username': username
        }
        newValues = {
            "$set": {
                'firstname': data['firstname'],
                'lastname': data['lastname'],
                'location': data['location'],
                'credit_no': data['credit_no'],
                'role': data['role']
            }
        }
        result = customer.update_one(query, newValues)
        if result.modified_count > 0:
            return jsonify({"message": "Customer Updated Successfully"}), 202
        elif result.matched_count > 0:
            return jsonify({"message": "Customer datas are same"}), 409
        else:
            return jsonify({"message": "No such customer data"}), 404
    except KeyError:  # missing student id
        return jsonify({'message': 'Keys Value are missing'}), 422
    except:
        return jsonify({'message': 'No json body received'}), 400


@app.route('/account_api/accounts/<username>', methods=['DELETE'])
def delete_customer(username):
    try:
        query = {
            'username': username
        }
        result = customer.delete_many(query)
        if result.deleted_count > 0:
            return jsonify({"message": "Account delete Successfully"}), 200
        else:
            return jsonify({"message": "No such account data"}), 404
    except:
        return jsonify({"message": "unknown error"}), 501



@app.route('/account_api/login', methods=['POST'])
# @jwt_required
def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    user_found = customer.find_one({"username": username})  # query by specified username
    print(user_found)
    if user_found:  # user exists
        if password == user_found["password"]:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401


@app.route('/account_api/signup', methods=['POST'])
def signup():
    data = request.json
    username = data["username"]
    password = data["password"]
    user_found = customer.find_one({"username": username})  # query by specified username
    if user_found:  # user exists
        if password == user_found["password"]:
            return jsonify({"msg": "Account already exists"}), 401
    try:
        acct = {"username": username, "password": password}
        customer.insert_one(acct)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    except:
        abort(405)


@app.errorhandler(405)
def error_405(error):
    response = dict(error="Error")
    return jsonify(response), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15001, debug=True)
