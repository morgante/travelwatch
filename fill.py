import data as db
import geo.names as geonames
import embassies
import sys
import news.retrieve as nyt

def fill_embassies(limit=None):
	print embassies.sync(limit=limit, DEBUG=True)

	return True

def fill_nyt_old(pages=None):
	data = nyt.search(query = "crime murder kill",pages=pages, highlight=True)

	for article in data:
		print article

	# print data

def main():
	type = sys.argv[1]
	n = int(sys.argv[2])

	if (type == 'embassies'):
		fill_embassies(limit=n)
	if (type == 'nyt_old'):
		fill_nyt_old(pages=n)

if __name__ == "__main__":
    main()