import data as db
import geo.names as geonames
import embassies
from ml import normalize

def main():
	data = embassies.get_old()

	for alert in data:
		print (alert["country"], alert["rating"])


if __name__ == "__main__":
    main()