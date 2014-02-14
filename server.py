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
		{"code": "UAE", "name": "United Arab Emirates", "score": 23} # Violence scores are 1-100
	]

	return json.dumps(data)

if __name__ == '__main__':
  
  if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
  else:
    port = 5000
  
  if ('ENVIRONMENT' in os.environ) and (os.environ['ENVIRONMENT'] == 'dev'):
    app.debug = True
  
  app.run(port=port, host='0.0.0.0')