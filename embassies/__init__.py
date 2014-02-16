import sys
sys.path.append("..")
import data as db

import canada
import usa

def get_old():
	return db.get_alerts()

def get_new():
	return sync()["new"]

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