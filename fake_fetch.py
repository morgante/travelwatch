from news import retrieve
from pymongo import MongoClient
import geocode
import data as db

data = retrieve.search(
	    query = None,
            filters={"news_desk": ["U.S.", "World"], "document_type":["article"]},
            begin="20080101",
            end="20090101",
            page=None,
            pages=1,
            sort=None,
            fields=["_id","web_url","lead_paragraph","abstract","headline","keywords","pub_date","word_count","source","document_type","news_desk"],
            highlight=True,
            facet_field=None, # Input here is a list of strings EVEN FOR ONE ELEMENT
            facet_filter=False
	)

for i in data[0]:
   print i
   if i['lead_paragraph'] == None:
	print "rabish"
	
   else:
	try:
	    article = {
			"positions": [],
			"headline": i['headline'],
			"text": i['lead_paragraph'],
			"keywords": i['keywords']['value'],
			"date": i['date'] 
		}
	    print("keyword is here "+i['keywords']['value'])
	except:
	    article = {
			"positions": [],
			"headline": i['headline'],
			"text": i['lead_paragraph'],
			"keywords": [],
			"date": i['date'] 
		}
   	print "got an article\n"
	db.insert_article(article)
"""
name: which type is it
rank:
value: 
"""
