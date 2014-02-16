import sys

sys.path.append("..")
import geo.code as geocode

import retrieve

def fetch_old(query="crime murder kill", pages=1):
	data = retrieve.search(query, pages=pages, highlight=False )

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

	print article

	normalized = {
		"positions":	headline_positions + headline_positions + text_positions, # headlines are doubly as important
		"headline": 	article["headline"],
		"snippet": 		text,
		"url":			article["url"],
		"date":			article["date"],
		"_id":  		article["_id"]
		# "keywords": keywords, KEYWORDS ARE RUBBISH, DISCARD
	}

	return normalized