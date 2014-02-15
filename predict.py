import data as db
import geo.names as geonames
import embassies

def main():
	data = embassies.get_alerts()

	for alert in data:
		print (alert["country"], alert["rating"])


if __name__ == "__main__":
    main()