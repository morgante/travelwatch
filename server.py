from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

if __name__ == '__main__':
  
  if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
  else:
    port = 5000
  
  if ('ENVIRONMENT' in os.environ) and (os.environ['ENVIRONMENT'] == 'dev'):
    app.debug = True
  
  app.run(port=port, host='0.0.0.0')