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

@app.route('/carts', methods=['GET'])
@app.route('/cart/<cart_id>', methods=['GET'])
def get_carts(cart_id=None):
    try:
       all_carts=[]
       if cart_id==None:
          for c in cart.find({},{"_id": 0}).sort("entity_id", 1):
              all_carts.append(c)
          return json.dumps(all_carts, sort_keys=True), 200
       else:
          for c in cart.find({"entity_id": cart_id},{"_id": 0}).sort("entity_id", 1):
              all_carts.append(c)
          return json.dumps(all_carts, sort_keys=True), 200
#Error Handling if no student records are found      
    except:
        abort(404)


@app.route('/cart', methods=['POST'])
def create_cart():

    return 1


@app.route('/carts', methods=['POST'])
def create_carts():

    return 1


@app.route('/cart/<cart_id>', methods=['PUT'])
def update_cart(cart_id):

    return 1


@app.route('/cart/<cart_id>', methods=['DELETE'])
def delete_cart(cart_id):

    return 1


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15001, debug=True)
