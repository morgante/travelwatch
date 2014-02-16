from flask import Flask, request
from flask import render_template
from news import retrieve
import os
import json
import data as db
from bson import Binary, Code
from bson.json_util import dumps as bson_dump
import embassies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/api/alerts/<code>')
def api_advisory(code):
	data = db.get_alerts(query={"country": code.upper()})

	return bson_dump(data)

# This route is for returning country score data, it should eventually mirror the format of /mock/scores
@app.route('/api/scores')
def scores():
	countries = db.get_countries(fields=["code","score"])
	return bson_dump(countries)

# This route is for returning detailed country data
@app.route('/api/countries')
def api_countries():
	countries = db.get_countries()
	return bson_dump(countries)

# This route returns actual
@app.route('/api/countries/<code>')
def api_country(code):
	country = db.get_country({"code": code.upper()})

	return bson_dump(country)

# This route is for returning country score data, it should eventually mirror the format of /mock/scores
@app.route('/mock/scores')
def mock_scores():
	data = [
		{"code": "USA", "name": "United States of America", "score": 19}, # Danger scores are 1-100
		{"code": "FRA", "name": "France", "score": 23},
		{"code": "VEN", "name": "Venezuela", "score": 3},
		{"code": "COL", "name": "Columbia", "score": 60}
	]

	return json.dumps(data)

# This route returns actual
@app.route('/mock/countries/<code>')
def mock_country(code):
	points = [
		{
			"position": {"latitude": 24.4667, "longitude": 54.3667},
			"score": 20, # 1-100
			"force": 10  # 1-100, how much to expand outward
		}
	]

	data =  {
		"code": "USA",
		"name": "United States of America",
		"score": 19,
		"risks": {
			"kidnapping": 5, # 0-100
			"bombing": 2
		},
		"points": points
	}

	return json.dumps(data)

@app.route('/mock/search/', methods=['GET'])
def search_query():
	return retrieve.search(query=request.args.get('query', ''))[0]

if __name__ == '__main__':
  
  if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
  else:
    port = 5000
  
  if ('ENVIRONMENT' in os.environ) and (os.environ['ENVIRONMENT'] == 'dev'):
    app.debug = True
  
  app.run(port=port, host='0.0.0.0')
