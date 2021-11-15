from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import os
import sys
import pika
import time

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
delivery_db = cluster.delivery_db
order_db = cluster.order_db
app = Flask(__name__)

time.sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %s" % body)
    cmd = body.decode()

    if cmd[:5] == 'Create':                                       #Delivering Orders
       try:
           order_id = cmd.split(" ")[1]
           query = {
            'order_id': order_id
           }
           newValues = {
                "$set": {
                    'status': 'shipping'
                }
           }
           result = order_db.order.update_one(query, newValues)
           try:
               query = {
              'status': free
               }
               result2 = delivery_db.delivery.find_one(query, {'_id': 0})
               query = {
               'delivery_id': result2['delivery_id']
               }
               newValues = {
                "$set": {
                    'status': 'busy'
                }
               }
               result = order_db.order.update_one(query, newValues)
           except:
                return jsonify({"message": "Cannot change delivery status"}), 404
           if result.modified_count > 0:
               return jsonify({"message": "Order and Delivery Status Update Successfully"}), 202
           elif result.matched_count > 0:
               return jsonify({"message": "Order are already in delivery"}), 409
           else:
               return jsonify({"message": "No such order data"}), 404
            
       except KeyError:  
           return jsonify({'message': 'Key Value are missing'}), 422
       except:
           return jsonify({'message': 'No json body received'}), 400
       time.sleep(30)
                                                                 #After several times, Order is delivered

       try:
          query = {
            'order_id': order_id
          }
          newValues = {
              "$set": {
                    'status': 'delivered'
              }
          }
          result = order_db.order.update_one(query, newValues)
          try:
             query = {
            'status': free
             }
             result2 = delivery_db.delivery.find_one(query, {'_id': 0})
             query = {
             'delivery_id': result2['delivery_id']
             }
             newValues = {
             "$set": {
             'status': 'free'
             }
             }
             result = order_db.order.update_one(query, newValues)
          except:
              return jsonify({"message": "Cannot change delivery status"}), 404
          if result.modified_count > 0:
              return jsonify({"message": "Order and Delivery Status Update Successfully"}), 202
          elif result.matched_count > 0:
              return jsonify({"message": "Order are already in delivery"}), 409
          else:
              return jsonify({"message": "No such order data"}), 404
            
       except KeyError:  
           return jsonify({'message': 'Key Value are missing'}), 422
       except:
           return jsonify({'message': 'No json body received'}), 400     
  #  elif cmd == 'hello':
  #      print("well hello there")
    else:
        print("the message cannot be understand ", body)


    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15005, debug=True)
