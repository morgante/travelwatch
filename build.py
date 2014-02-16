import sys

import data as db
import news
from news import risks
from ml import words

def get_news():
	cdata = news.get_by_state()

	for code, articles in cdata.iteritems():
		# ratings = map(lambda alert: alert["rating"], country["alerts"])
	 	# score = int(float(sum(ratings) / len(ratings)) / 4 * 100)

	 	# country["score"] = score

		for article in articles:
			# print article
			# print article
			print words.frequencies(article["snippet"])

	# print cdata

def main():
	get_news()

if __name__ == "__main__":
    main()