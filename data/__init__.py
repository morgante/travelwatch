from pymongo import MongoClient
import os

if ('DB_PORT_27017_TCP_ADDR' in os.environ):
	ip = os.environ['DB_PORT_27017_TCP_ADDR']
else:
	ip = '128.199.242.243'

if ('DB_PORT_27017_TCP_PORT' in os.environ):
	port = int(os.environ['DB_PORT_27017_TCP_PORT'])
else:
	port = 49155

if (os.environ['ENVIRONMENT'] == 'prod'):
	db_name = 'production'
else:
	db_name = 'development'

client = MongoClient(ip, port)
db = client[db_name]

def insert(collection, data):
	db[collection].insert(data)

def find_one(collection, query={}):
	return db[collection].find_one(query)

def test():
	return 'lols'