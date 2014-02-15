from flask import Flask
from flask import render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

# This route is for returning country score data, it should eventually mirror the format of /mock/scores
@app.route('/api/scores')
def scores():
	return 'not implemented'

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

# This route is for returning detailed country data
@app.route('/mock/country/<code>')
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

if __name__ == '__main__':
  
  if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
  else:
    port = 5000
  
  if ('ENVIRONMENT' in os.environ) and (os.environ['ENVIRONMENT'] == 'dev'):
    app.debug = True
  
  app.run(port=port, host='0.0.0.0')
