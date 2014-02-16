import sys

sys.path.append("..")

import data as db
import news
from news import risks

import words

def get_news():
	cdata = news.get_by_country()

	print cdata

def main():
	get_news()

if __name__ == "__main__":
    main()