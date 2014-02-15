from embassies import *
import data as db
import geo.names as geonames

def get_alerts():
	alerts = {
		"old": [],
		"new": []
	}

	us_alerts = usa.get_alerts(limit=2)

	# for alert in us_alerts:
	# 	alert["source"] = "USA"

	# 	existing = db.get_alert({"source": "USA", "date": alert["date"]})

	# 	if (existing is None or alert["date"] > existing["date"]):
	# 		alerts["new"].append(alert)

	return alerts

def main():
	data = get_alerts()

	# print geonames.get_code_from_name("Canada")

	# print data


if __name__ == "__main__":
    main()