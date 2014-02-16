import sys
sys.path.append("..")
import data as db

import canada
import usa

def get_by_country():
	data = get_old()
	countries = {}

	if (data is None):
		return countries

	for alert in data:
		alert = clean_alert(alert)
		if (alert["country"] in countries):
			country = countries[alert["country"]]
		else:
			country = {
				"code": alert["country"],
				"alerts": []
			}

		country["alerts"].append(alert)

		countries[alert["country"]] = country

	for code, country in countries.iteritems():
		ratings = map(lambda alert: alert["rating"], country["alerts"])
	 	score = int(float(sum(ratings) / len(ratings)) / 4 * 100)

	 	country["score"] = score

	return countries

def get_old():
	return db.get_alerts()

def get_new():
	return sync()["new"]

def clean_alert(alert):
	points = []

	for position in alert["positions"]:
		if ("latitude" not in position):
			continue
		if (("placename" in position) and (alert["country"] is not "USA") and (position["placename"] is "United States")):
			continue
		else:
			points.append({
				"latitude": position["latitude"],
				"longitude": position["longitude"]
			})

	alert["points"] = points

	return alert

def sync(limit=None, DEBUG=False):
	alerts = {
		"old": [],
		"new": []
	}

	us_alerts = usa.get_alerts(limit)
	ca_alerts = canada.get_alerts(limit)

	all_alerts = us_alerts + ca_alerts

	for alert in all_alerts:
		existing = db.get_alert({"provider": alert["provider"], "date": alert["date"]})

		if (existing is None or alert["date"] > existing["date"]):
			db.insert_alert(alert)
			alerts["new"].append(alert)
		else:
			alerts["old"].append(alert)

	return alerts

__all__ = ["canada", "usa"]