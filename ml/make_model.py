import data as db
import word_frequency as wfr

def get_crimes_by_city():
	return [{
		"city": "Abu Dhabi, UAE",
		"score": 32
	}]

def get_keywords_by_city():
    cities ={}

    # Get every single article
    articles = db.get_articles()

    for article in articles():
	##unsure of the exact notation for this part
	#############################
	hl=article["headline"]
	txt=article["txt"]
	kw=article["keywords"]
        city=get_city_from_position(article["position"])
   	##############################

	##currently using equal weighting
	wf1=wfr.normalize(wfr.get_frequency(hl))
	wf2=wfr.normalize(wfr.get_frequency(h2))
	wf3=wfr.normalize(wfr.get_frequency(h3))
	wf=wfr.normalize(wfr.add(wfr.add(wf1,wf2),w3))

	if city in cities.keys():
	    cities[city]=wfr.add(cities[city][0],wf)
	else:
	    cities[city]=wfr
    
    for city in cities:
	##normalize after all articles have been updated
	cities[city]=wfr.normalize(cities[city])
        #have to append a cNum to each city

    return cities 


def train():
	crimes = get_crimes_by_city()
	keywords = get_keywords_by_city()

	# TRAIN THE MODEL YAY