from datetime import date

import data as db
import geo.names as geonames
import embassies
import sys
import news

def fill_embassies(limit=None):
	print embassies.sync(limit=limit, DEBUG=True)

	return True

def fill_nyt_old(pages=None, start=date(2008, 01, 01), end=date(2008, 12, 30)):
	oldest = db.db["articles"].find_one(query={
		"date": {"$gt": start, "$lt": end}
		}, sort=[("date", -1)])

	if (oldest is not None):
		start = oldest['date']

	print 'Loading articles since '
	print start

	data = news.fetch(start=start,end=end)

	for article in data:
		try:
			db.insert_article(article)
		except:
			print 'mongo repeat...'

def main():
	type = sys.argv[1]
	n = int(sys.argv[2])

	if (type == 'embassies'):
		fill_embassies(limit=n)
	if (type == 'nyt_old'):
		fill_nyt_old(pages=n)

if __name__ == "__main__":
    main()