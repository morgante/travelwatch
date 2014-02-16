import sys
import datetime
from datetime import date
from collections import Counter

sys.path.append("..")
import geo.code as geocode
import geo.reverse as georeverse
import data as db

import retrieve

def convert_date(date):
	return date.strftime("%Y%m%d")

def get_by_state():
	data = db.get_articles()
	aggregated = {}

	if (data is None):
		return aggregated

	for article in data:
		article = clean(article)
		states = []

		for point in article["points"]:
			try:
				print states.append(georeverse.get_state(point))
			except:
				print 'problem with state lookup'

		if (len(states) < 1):
			continue

		state = Counter(states).most_common(1)[0][0]

		if (state in aggregated):
			aggregated[state].append(article)
		else:
			aggregated[state] = [article]

	return aggregated

def fetch(query, pages=1, start=date(2006, 01, 10), end=date.today()):
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

def clean(article):
	points = []

	for position in article["positions"]:
		if ("latitude" not in position):
			continue
		else:
			points.append({
				"latitude": position["latitude"],
				"longitude": position["longitude"]
			})

	article["points"] = points

	return article

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
