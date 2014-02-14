nyuad2014
=========

## Docker
The entire development environment is contained in a Docker container. To get up and running:

1. Install [Docker](https://www.docker.io/gettingstarted/#h_installation).
2.  Clone this repo: ```git clone https://github.com/morgante/travelwatch.git```
3. Go into the travelwatch dir: ```cd travelwatch```
4. Download the Docker image: ```docker pull morgante/travelwatch```
5. Run the Docker container: ```docker run -v /var/code/travelwatch/nyuad:/src -d -t -p 49200:5000 -e ENVIRONMENT='dev' --name travelwatch morgante/travelwatch```
6. Open the app: http://localhost:49200/
7. Make changes to ```server.py``` and they will be reflected live.

## MongoDB
You can connect to the database remotely:

	mongo 128.199.242.243:49155

This database is actually containerized in Docker, so you can run it locally if you want.

	docker pull morgante/tmongo
	docker run -d -p 49155:27017 morgante/tmongo /usr/bin/mongod --smallfiles

### Bonus Hints
If you want to tail the logs for the app, including Python logging output:

	docker logs -f travelwatch

If you want to open an interactive shell of the Docker image (for example, to play with other Python commands):

	docker run -v /var/code/travelwatch/nyuad:/src -t -e ENVIRONMENT='dev' -i --entrypoint="/bin/bash" morgante/travelwatch


If you've changed requirements, you can rebuild locally:

	docker kill travelwatch
	docker rm travelwatch
	docker build -t morgante/travelwatch .
	docker run -v /var/code/travelwatch/nyuad:/src -d -t -p 49200:5000 -e ENVIRONMENT='dev' --name travelwatch morgante/travelwatch

## Machin Learning Pipeline
This is the pipeline for how all our machine learning data will be generated.

1. Fetch the news articles we're going to train on

	python fetch.py

2. Train the model from the data

	python train.py

3. Pull in the model

	import ml
	violence = ml.analyze(data)

## Geocodes

geocode.py is your friend:

```
import geocode
geocode.get_geocodes_from_html('Some <b>HTML</b> goes here, hopefully inlcuding a place like the USA, Egypt, or Boston, MA.')
geocode.get_geocodes_from_url('http://nytimes.com')
geocoe.get_geocodes_from_text('There is no HTML here, but there is a place name! We are in Abu Dhabi, UAE, and I'm from Maryland, USA.')
```
   