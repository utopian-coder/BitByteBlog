from pymongo import MongoClient
import os

URI = os.environ.get('MONGO_URI')

mongo_client = MongoClient(URI)
