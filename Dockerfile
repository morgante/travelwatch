# DOCKER-VERSION 0.8.0
FROM		shykes/pybuilder

# Need python-dev
RUN 		apt-get install -y python-dev
RUN 		apt-get install -y build-essential

RUN 		apt-get install -y vim

# Scikit-learn dependencies
RUN 		apt-get install -y python-numpy python-setuptools python-scipy
RUN 		apt-get install -y libatlas-dev libatlas3-base

# Scikit-learn
RUN 		pip install -U scikit-learn


# Pips
RUN 		cd /src; pip install flask
RUN 		cd /src; pip install geopy
RUN 		cd /src; pip install beautifulsoup4
RUN 		cd /src; pip install python-twitter
RUN 		cd /src; pip install pymongo
RUN		cd /src; pip install pyyaml nltk

# Add source
ADD 		. /src

# Pip installer
RUN 		cd /src; pip install -r requirements.txt

# Expose port
EXPOSE 		5000

# Run it
WORKDIR		/src

RUN 		python nltk_downloads.py

ENTRYPOINT ["python", "server.py"]
