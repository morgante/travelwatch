nyuad2014
=========

Docker
------
The entire development environment is contained in a Docker container. To get up and running:

# Install [Docker](https://www.docker.io/gettingstarted/#h_installation).
# Clone this repo: ```git clone https://github.com/morgante/travelwatch.git```
# Go into the travelwatch dir: ```cd travelwatch```
# Build the Docker image: ```docker build -t morgante/travelwatch .```
# Run the Docker container: ```docker run -v /var/code/travelwatch/nyuad:/src -d -t -p 49200:5000 -e ENVIRONMENT='dev' morgante/travelwatch```
# Open the app: http://localhost:49200/
# Make changes to ```server.py``` and they will be reflected live.