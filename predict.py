import data as db
import geo.names as geonames
import embassies

def by_embassies():
	countries = []

	for code, country in embassies.get_by_country().iteritems():
		points = [];

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
	by_embassies()

if __name__ == "__main__":
    main()