import data as db
import random
from faker import Factory as FakeFactory

fake = FakeFactory.create()

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

def make_article():
	data = {
		"positions": [],
		"headline": fake.sentence(nb_words=6, variable_nb_words=True),
		"text": fake.paragraph(nb_sentences=7, variable_nb_sentences=True),
		"keywords": [],
		"date": fake.date_time()
	}

	for _ in range(random.randint(3,7)):
		word = fake.word()

		if (not word in data["keywords"]):
			data["keywords"].append(word)

	for _ in range(random.randint(1,4)):
		data["positions"].append({
				"longitude": float(fake.longitude()),
				"latitude": float(fake.latitude())
			})

	db.insert_article(data)

def make_articles():	
	for _ in range(10):
		make_article()


if __name__ == "__main__":
	make_articles()