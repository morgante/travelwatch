import sys
sys.path.append('..')

import data as db
import word_frequency as wfr

<<<<<<< HEAD
def score_from_crimes(crimes): 
	return 11

=======
def score_from_crimes(crimes):
	return 11; #1-100
>>>>>>> cc6453354a023b3ac90017bc6d44781851b1a751

def get_crimes_by_city(city):

	# db.get_crimes()
	
	cities = {}

	#{
	#	"CITYNAME": {
	#		"city": "CITYNAME",
	#		"crimes": {},
	#		"score": 12
	#	}
	#}

	return 10;

def model_from_all():
    cities ={}

    # Get every single article
    articles = db.get_articles()

    for article in articles:
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
	cities[city][c_Num]=get_crime_by_city(city)
    return cities 
			
