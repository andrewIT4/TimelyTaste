from flask import Flask,request,jsonify, abort
import pymongo
import json
import os
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)
jwt = JWTManager()

#  set JWT secretkey
app.config['JWT_SECRET_KEY'] = 'TimelyTaste'
jwt.init_app(app)

#Make connection to MongoDB with the Environment Variables 
username=os.environ.get('MONGO_USERNAME')
password = os.environ.get('MONGO_PASSWORD')
hostname = os.environ.get('MONGO_SERVER_HOST')
hostname = hostname.replace("\'", "")
port = os.environ.get('MONGO_SERVER_PORT')
port = port.replace("\'", "")
connStr ='mongodb://%s:%s@%s:%s/' % (username, password, hostname, port)

conn =  pymongo.MongoClient(connStr)
user_account = conn["user_account"]
customer = user_account['customer']

@app.route('/login', methods=['POST'])
#@jwt_required
def login():
    data = request.json
    username = data["username"]
    password = data["password"] 
    user_found = customer.find_one({"username": username})  # query by specified username
    print(user_found)
    if user_found:  # user exists
        if password == user_found["password"]:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
@app.route('/signup', methods=['POST'])
def signup(): 
    data = request.json
    username = data["username"]
    password = data["password"]
    user_found = customer.find_one({"username": username})  # query by specified username
    if user_found:  # user exists
        if password == user_found["password"]:
           return jsonify({"msg": "Account already exists"}), 401
    try:
       acct = {"username": username,"password": password}
       customer.insert_one(acct)
       access_token = create_access_token(identity=username)
       return jsonify(access_token=access_token)
    except:
       abort(405)
     
@app.errorhandler(405)
def error_405(error):
    response = dict(error="Error")
    return jsonify(response), 405

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=15000, debug=True)
