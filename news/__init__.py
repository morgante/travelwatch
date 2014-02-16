import sys
import datetime
from datetime import date

sys.path.append("..")
import geo.code as geocode
import data as db

import retrieve

def convert_date(date):
	return date.strftime("%Y%m%d")

def get_by_country():
	data = db.get_articles()
	countries = {}

	# print data

	for article in data:
		print article

	

	# if (data is None):
	# 	return countries

	# for alert in data:
	# 	alert = clean_alert(alert)
	# 	if (alert["country"] in countries):
	# 		country = countries[alert["country"]]
	# 	else:
	# 		country = {
	# 			"code": alert["country"],
	# 			"alerts": []
	# 		}

	# 	country["alerts"].append(alert)

	# 	countries[alert["country"]] = country

	# for code, country in countries.iteritems():
	# 	ratings = map(lambda alert: alert["rating"], country["alerts"])
	#  	score = int(float(sum(ratings) / len(ratings)) / 4 * 100)

	#  	country["score"] = score

	return countries

def fetch(query="crime murder kill", pages=1, start=date(2006, 01, 10), end=date.today()):
	data = retrieve.search(query, pages=pages, highlight=False, begin=convert_date(start), end=convert_date(end))

	articles = []

	for article in data:
		articles.append(normalize(article))

	return articles

def get_positions(text):
	try:
		return geocode.get_geocodes_from_text(text)
	except:
		return []


def normalize(article):
	text = ""
	if (article["lead_paragraph"]):
		text += article["lead_paragraph"]
	if (article["snippet"]):
		text += " " + article["snippet"]

	headline_positions = get_positions(article["headline"])
	text_positions = get_positions(text)

	normalized = {
		"positions":	headline_positions + headline_positions + text_positions, # headlines are doubly as important
		"headline": 	article["headline"],
		"snippet": 		text,
		"url":			article["url"],
		"date":			datetime.datetime.strptime(article["date"], "%Y-%m-%dT%H:%M:%SZ"),
		"_id":  		article["_id"]
		# "keywords": keywords, KEYWORDS ARE RUBBISH, DISCARD
	}

	return normalized