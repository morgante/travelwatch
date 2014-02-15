import data as db
import random
from faker import Factory as FakeFactory

fake = FakeFactory.create()

def make_country():
	points = []

	for _ in range(random.randint(10,100)):
		points.append({
			"position": {
				"longitude": float(fake.longitude()),
				"latitude": float(fake.latitude())
			},
			"score": random.randint(1,100)
		})

	score = reduce(lambda x, y: x+y, map(lambda x: x["score"], points))/len(points)

	country = {
		"code": "USA",
		"name": "United States of America",
		"score": score,
		"points": points
	}

	db.insert_country(country)

def make_countries():
	for _ in range(20):
		make_country();

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

def make_alert():
	positions = []

	for _ in range(random.randint(1,4)):
		positions.append({
			"longitude": float(fake.longitude()),
			"latitude": float(fake.latitude())
		})

	data = {
		"provider": "USA",
		"positions": positions,
		"level": random.randint(1,4),
		"text": fake.paragraph(nb_sentences=7, variable_nb_sentences=True),
		"date": fake.date_time()
	}

	db.insert_alert(data)

def make_alerts():	
	for _ in range(10):
		make_alert()

if __name__ == "__main__":
	make_alerts()
	# make_countries()
	# make_articles()