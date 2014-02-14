# DOCKER-VERSION 0.8.0
FROM		shykes/pybuilder

# Need python-dev
RUN 		apt-get install -y python-dev
RUN 		apt-get install -y build-essential

# Scikit-learn dependencies
RUN 		apt-get install -y python-numpy python-setuptools python-scipy
RUN 		apt-get install -y libatlas-dev libatlas3-base

# Scikit-learn
RUN 		pip install -U scikit-learn

# Geocode
RUN 		pip install -U geopy
#RUN 		cd geocoding
#RUN 		python alchemyapi.py 22c297c6c8d199f88b09cedd9ca91e8f0c112fc2
#RUN 		cd ..

# Scraping
RUN 		pip install beautifulsoup4

# Pips
RUN 		cd /src; pip install flask

# Add source
ADD 		. /src

# Pip installer
RUN 		cd /src; pip install -r requirements.txt

# Expose port
EXPOSE 		5000

# Run it
WORKDIR		/src

ENTRYPOINT ["python", "server.py"]
