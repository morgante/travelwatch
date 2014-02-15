import data as db

def get_crimes_by_city():
	return [{
		"city": "Abu Dhabi, UAE",
		"score": 32
	}]

def get_keywords_by_city():
    cities = {}

    # Get every single article
    articles = db.get_articles()

    for article in articles():
 	print article["keywords"]

	word_frequencies = {
	    "murder": 1,
	    "bombing": 3
	}
	# city = get_city_from_position(article["position"])
    city = "Abu Dhabi, UAE"

    if (city in cities):
	cities
    else:
			
