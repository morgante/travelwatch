import data as db
import geo.names as geonames
import embassies
import random
import news

import ml
from ml import words
from ml import normalize
from ml import train as modeler
import random

def by_embassies():
	countries = []

	for code, country in embassies.get_by_country().iteritems():
		points = [];

		for alert in country["alerts"]:
			for point in alert["points"]:
				points.append({
					"position": {
						"longitude": point["latitude"],
						"latitude": point["longitude"]
					},
					"score": country["score"] + random.randint(-40, 40) # ha ha ha
				})

		doc = {
			"code": code,
			"name": geonames.get_name_from_code(code),
			"score": country["score"],
			"points": points
		}

		countries.append(doc)

	for country in countries:
		db.insert_country(country)

	print "Inserted country data"

def get_news():
	cdata = news.get_by_state()
	fdata = {}

	for code, articles in cdata.iteritems():
		keywords = words.frequencies()

		for article in articles:
			for word, freq in words.frequencies(article["snippet"]).iteritems():
				keywords[word] += freq

		fdata[code] = keywords

	return fdata

def by_news():

    for (code, ndata) in get_news().iteritems():
        row = normalize.row({
            "news": ndata
        })


        print ml.predict(row)


def main():
	# db.db["countries"].drop()
	
	by_embassies()
	
	# by_news()

if __name__ == "__main__":
    main()