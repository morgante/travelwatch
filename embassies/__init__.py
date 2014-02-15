import sys
sys.path.append("..")
import data as db

import canada
import usa

def get_alerts():
	return db.get_alerts()

def sync():
	alerts = {
		"old": [],
		"new": []
	}

	us_alerts = usa.get_alerts(limit=2)
	ca_alerts = canada.get_alerts(limit=2)

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