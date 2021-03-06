import sys

import data as db
import news
from news import risks
from ml import words
from ml import normalize
from ml import train as modeler
import random

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

def main():
    rows = []
    outputs = []

    for (code, ndata) in get_news().iteritems():
        row = normalize.row({
            "news": ndata
        })

        rows.append(row)
        outputs.append(random.randint(1,100))

    model = modeler.train(rows, outputs)

    print model

# def get_crimes():
#     global II
#     II=0
#     cursor = db.get_crimes()
	
#     cNUM = {}
    
#     for entry in cursor:
#         lat = entry['position']['latitude']
#         lon = entry['position']['longitude']
#         city = gr.get_city((lon,lat))
# 	if city==None:
# 	    city=getcity()
# 	cNUM[city] = score_from_crimes(entry["crimes"])
	
#     return cNUM

# def score_from_crimes(crimes): 
#     w1 = 2*crimes['violent crime']/48430
#     w2 = 3*crimes['murder and nonnegligent manslaughter']/523
#     w3 = 2.5*crimes['forcible rape']/1038
#     w4 = 2*crimes['robbery']/22186
#     w5 = 1.5*crimes['aggravated assault']/24831
#     w6 = crimes['property crime']/149989
#     w7 = crimes['burglary']/26947
#     w8 = crimes['larceny/theft']/117682
#     w9 = crimes['motor vehicle theft']/22623
#     weightedSum = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9
#     if weightedSum == 0:
#         return 0
#     # My justification: (so i can make fun of myself for this later)
#     # Looks hacky, but fleshed this out in excel and it works
#     # Data looks somewhat exponential=>log the weighted data
#     # weights based on Importance*#occurances/MAXoccurances
#     # The -5 and /(-10) put it in a reasonable decimal scale
#     # The 1- Inverted the percentage to represent risk instead of "safety"
#     # /0.8 to level out the percentages across the 1.0 range
#     normalized = (1 - ((numpy.log10(weightedSum)-5)/(-10)))/0.8
#     return normalized

if __name__ == "__main__":
    main()