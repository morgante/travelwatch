from pymongo import MongoClient
import os

if ('DB_PORT_27017_TCP_ADDR' in os.environ):
	ip = os.environ['DB_PORT_27017_TCP_ADDR']
else:
	ip = '128.199.242.243'

if ('DB_PORT_27017_TCP_PORT' in os.environ):
	port = int(os.environ['DB_PORT_27017_TCP_PORT'])
else:
	port = 49210

if (os.environ['ENVIRONMENT'] == 'prod'):
	db_name = 'production'
else:
	db_name = 'development'

client = MongoClient(ip, port)
db = client[db_name]

def insert(collection, data):
	db[collection].insert(data)

def find_one(collection, query={}, fields=None):
	return db[collection].find_one(query, fields=fields)

def find(collection, query={}, fields=None):
	return db[collection].find(query, fields=fields)

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

def get_country(query={}, fields=None):
	return find_one('countries', query, fields=fields)

def get_countries(query={}, fields=None):
	return find('countries', query, fields=fields)

def insert_article(data):
	insert("articles", data)

def get_articles(query={}):
	return find('articles', query)

def insert_alert(data):
	insert("alerts", data)

def get_alert(query={}):
	return find_one('alerts', query)

def get_alerts(query={}):
	return find('alerts', query)

def test():
	return 'lols'