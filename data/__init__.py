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

def find(collection, query={}):
	return db[collection].find(query)

def insert_crime(position, crime):
	insert("crime", {"position": position, "crime": crime});

def insert_crimes(crimes):
	for place in crimes:
		insert_crime(place.position, crime);

def insert_country(country):
	insert("countries", country)

def insert_countries(countries):
	for country in countries:
		insert_country(country)

def get_articles(query={}):
	return find('articles', query)

def test():
	return 'lols'