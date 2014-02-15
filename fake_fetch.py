from news import retrieve
from pymongo import MongoClient
import geocode
import data as db

data = retrieve.search(
	    query=None,
            filters=None, # Input here is a list of dictionaries EVEN FOR ONE ELEMENT: ["web_url"], etc.
            begin="20080101",
            end="20081231",
            page=None,
            pages=1,
            sort=None,
            fields=["_id", "web_url", "headline", "keywords"],
            highlight=False,
            facet_field=["source"], # Input here is a list of strings EVEN FOR ONE ELEMENT
            facet_filter=False
	)


#data = [{'lead_paragraph': None, 'headline': u'In Fashion, Fame\u2019s Last Bastion', 'snippet': None, 'url': u'http://www.nytimes.com/2014/02/16/fashion/Fashion-Week-celebrities.html', 'date': None, '_id': u'52fead9438f0d826f8460dfb'}]
#print data
#print data[0]["url"]


for i in data:
   print i
   if i['lead_paragraph'] == None:
	print "rabish"
	
   else:
	article = {
		"positions": [],
		"headline": i['headline'],
		"text": i['lead_paragraph'],
		"keywords": [],
		"date": i['date'] 
	}
   	print "got an article\n"
	db.insert_article(article)
   


