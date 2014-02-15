# DOCKER-VERSION 0.8.0
FROM		shykes/pybuilder

# Need python-dev
RUN 		apt-get install -y python-dev
RUN 		apt-get install -y build-essential

# Scikit-learn 
RUN 		apt-get install -y python-numpy python-setuptools python-scipy
RUN 		apt-get install -y libatlas-dev libatlas3-base
RUN 		pip install -U scikit-learn

# NLTK
RUN			pip install pyyaml nltk
RUN 		python -c "import nltk; [nltk.download(p) for p in ['maxent_ne_chunker', 'punkt', 'words', 'maxent_treebank_pos_tagger']]"

# Mongo
RUN 		apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN 		echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
RUN 		apt-get update
RUN 		apt-get install mongodb-10gen

# Pips
RUN 		cd /src; pip install flask
RUN 		cd /src; pip install geopy
RUN 		cd /src; pip install beautifulsoup4
RUN 		cd /src; pip install python-twitter
RUN 		cd /src; pip install pymongo
RUN 		cd /src; pip install fake-factory
RUN 		cd /src; pip install countrycode

# Dev tools
RUN 		apt-get install -y vim

# Add source
ADD 		. /src

# Pip installer
# RUN 		cd /src; pip install -r requirements.txt

# Expose port
EXPOSE 		5000

# Run it
WORKDIR		/src

ENTRYPOINT ["/bin/bash"]