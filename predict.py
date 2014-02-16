import data as db
import geo.names as geonames
import embassies
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
					"score": country["score"] + random.randint(-10, 10) # ha ha ha
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

def main():
	db.db["countries"].drop()

	by_embassies()

if __name__ == "__main__":
    main()