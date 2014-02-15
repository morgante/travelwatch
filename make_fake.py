import data as db

def make_scores():
	points = [
		{
			"position": {"latitude": 24.4667, "longitude": 54.3667},
			"score": 20, # 1-100
			"force": 10  # 1-100, how much to expand outward
		}
	]

	data =  {
		"code": "USA",
		"name": "United States of America",
		"score": 19,
		"risks": {
			"kidnapping": 5, # 0-100
			"bombing": 2
		},
		"points": points
	}

	db.insert_countries([data])