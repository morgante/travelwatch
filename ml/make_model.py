import sys
sys.path.append('..')

import data as db
import word_frequency as wfr
import geo.reverse as gr
def score_from_crimes(crimes): 
	return 11

def score_from_crimes(crimes):
	return 11; #1-100

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
	txt=article["text"]
	kw=article["keywords"]
        if len(article["positions"]) < 1:
            continue

        point = (article["positions"]["latitude"], article["positions"]["longitude"])
        city=gr.get_city(point)
        if city == None:
            continue
   	##############################

	##currently using equal weighting
	wf1=wfr.normalize(wfr.get_frequency(hl))
	wf2=wfr.normalize(wfr.get_frequency(txt))
	wf3=wfr.normalize(wfr.get_frequency(kw))
	wf=wfr.normalize(wfr.add(wfr.add(wf1,wf2),wf3))

	if city in cities.keys():
	    cities[city]=wfr.add(cities[city],wf)
	else:
	    cities[city]=wf
    
    for city in cities:
	##normalize after all articles have been updated
	cities[city]=wfr.normalize(cities[city])
        #have to append a cNum to each city
	cities[city]["c_Num"]=get_crimes_by_city(city)
        print cities[city]
    return cities 
			
