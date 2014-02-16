from news import retrieve
from pymongo import MongoClient
from geo import code
import data as db



def get_lat_lon(text):

	positions = code.get_geocodes_from_text(text)
	#print "HERE", positions, "\n\n\n\n"
	lat_lon = []
	
	try:
		for i in positions:
			temp = {'latitude': i['latitude'], 
			 	'longitude': i['longitude']}
			
			lat_lon.append(temp)
			#print "==================="
			print lat_lon
			#print "=================="
		return lat_lon
	except:
		#print "\nM\n"
		return lat_lon	

def push_NYT_to_db():

	data = retrieve.search(query = "crime murder kill",pages = 1, highlight=True )
	for i in data[0]:
		
   		if i['lead_paragraph'] == None:
			continue
				
   		else:	
			positions = get_lat_lon(i['lead_paragraph'])
			article = {
					"positions": positions,
					"headline": i['headline'],
					"text": i['lead_paragraph'],
					"date": i['date']}
	
			try:
	    			lstKeywords = []
	    			for j in i['keywords']:
					lstKeywords.append(j['value'])
	   			article['keywords'] = lst_key_words 
					
			except:
	    			article['keywords'] = []

		#print "HERE ", code.get_geocodes_from_text(i['lead_paragraph'])[0]['latitude']
		#db.insert_article(article)
		#print "FINISHED"


push_NYT_to_db()

