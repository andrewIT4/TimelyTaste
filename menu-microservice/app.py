from flask import Flask, jsonify
from pymongo import MongoClient
import os
import sys

# username = os.getenv('MONGO_USERNAME')
# password = os.getenv('MONGO_PASSWORD')
# hostAddress = os.getenv('MONGO_SERVER_HOST')
# port = os.getenv('MONGO_SERVER_PORT')

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

# Get and initialise the COMP3122Project Database
db = cluster.COMP3122Project
app = Flask(__name__)