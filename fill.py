import data as db
import geo.names as geonames
import embassies

def fill_embassies():
	print embassies.sync(DEBUG=True)

	return True

def main():
	fill_embassies()

if __name__ == "__main__":
    main()