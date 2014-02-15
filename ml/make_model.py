import sys
sys.path.append('..')

import data as db
import word_frequency as wfr
import geo.reverse as gr
import train
import numpy
def score_from_crimes(crimes): 
    w1 = 2*crimes['violent crime']/48430
    w2 = 3*crimes['murder and nonnegligent manslaughter']/523
    w3 = 2.5*crimes['forcible rape']/1038
    w4 = 2*crimes['robbery']/22186
    w5 = 1.5*crimes['aggravated assault']/24831
    w6 = crimes['property crime']/149989
    w7 = crimes['burglary']/26947
    w8 = crimes['larceny/theft']/117682
    w9 = crimes['motor vehicle theft']/22623
    weightedSum = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9
    if weightedSum == 0:
        return 0
    # My justification: (so i can make fun of myself for this later)
    # Looks hacky, but fleshed this out in excel and it works
    # Data looks somewhat exponential=>log the weighted data
    # weights based on Importance*#occurances/MAXoccurances
    # The -5 and /(-10) put it in a reasonable decimal scale
    # The 1- Inverted the percentage to represent risk instead of "safety"
    # /0.8 to level out the percentages across the 1.0 range
    normalized = (1 - ((numpy.log10(weightedSum)-5)/(-10)))/0.8
    return normalized


def get_crimes_by_city():

    cursor = db.get_crimes()
	
    cNUM = {}
    
    for entry in cursor:
        lat = entry['position']['latitude']
        lon = entry['position']['longitude']
        city = gr.get_city((lon,lat))
	cNUM[city] = score_from_crimes(entry["crimes"])
	
    return cNUM


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
	print article["position"]

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
			
