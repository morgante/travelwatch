import data as db
import geo.names as geonames
import embassies
import sys

def fill_embassies(limit=None):
	print embassies.sync(limit=limit, DEBUG=True)

	return True

def main():
	type = sys.argv[1]
	n = int(sys.argv[2])

	if (type == 'embassies'):
		fill_embassies(limit=n)

if __name__ == "__main__":
    main()