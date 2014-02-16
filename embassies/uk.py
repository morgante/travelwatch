# -*- coding: utf-8 -*-
## UK Embassy scraper by Nishant Mohanchandra (nm1345@nyu.edu)

## Module dependencies
from bs4 import BeautifulSoup as BS
from datetime import datetime
import urllib2
import string
import time
import re

import sys
sys.path.append("..")
import geo.names as geonames


# Number of countries to scrape
LIMIT = 225

def get_alerts():

    """
    Adopting Bonnie's rankings for safety: 1 is safest; 4 is most dangerous
    """

    ## The first number is the danger score & the second number is how many times it appears
    advisory_phrases = {'advise against all': [4,0],
                        'all but essential': [3,0],
                        'low threat from terrorism': [2,0],
                        'Most visits are trouble-free': [1,0],
                        'Most visits are trouble free': [1,0]}
    
    stem_url = "https://www.gov.uk/"
    url = "https://www.gov.uk/foreign-travel-advice"

    ## Using beautiful soup to organize the webpage
    page = urllib2.urlopen(url)
    soup = BS(page.read())

    ## Lists for alerts and country pages
    gathered_alerts = []
    country_pages = []

    ## Zoning in on each country page
    rows = (soup.find("div", {"id": "wrapper"})).find_all("li")
    raw_data = []
    country_codes = []
    country_codes_final = []

    ## Chucking stuff from the li that isn't needed
    for row in rows:
        cells = str(row.find_all("a"))
        if len(cells) < 1:
            continue
        raw_data.append(cells)

    ## Chucking stuff from the a href tag that isn't needed
    for i in range(len(raw_data)):
        raw_data[i] = raw_data[i][11:-5]
        raw_data[i] = raw_data[i].split('"')[0]
    raw_data = raw_data[2:]

    ## Scraping area names
    for element in raw_data:
        country_codes.append(element[22:])

    ## Removing shitty hyphens from country names
    for element in country_codes:
        country_codes_final.append(geonames.get_code_from_name(element.replace("-"," ")))

    ## Dealing with some horrible shitty individual cases
    for i in range(len(country_codes_final)):
        if len(country_codes_final[i]) > 3:
            if country_codes_final[i] == "bonaire st eustatius saba":
                country_codes_final[i] = "BES"
            elif country_codes_final[i] == "british antarctic territory":
                country_codes_final[i] = "ATB"
            elif country_codes_final[i] == "kosovo":
                country_codes_final[i] = "SCG"
            elif country_codes_final[i] == "south korea":
                country_codes_final[i] = "KOR"
            elif country_codes_final[i] == "st maarten":
                country_codes_final[i] = "SXM"
            ## If this code ever executes, fuck you, British Embassy
            else:
                country_codes_final[i] = "XXX"

    ## Scraping all the individual country data
    for i in range(LIMIT):

        try:
            country_webpage = urllib2.urlopen(stem_url+raw_data[i]).read()
            country_pages.append(country_webpage)
            country_soup = BS(country_webpage)
            country_soup = country_soup.find("div", {"id": "wrapper"}).find_all("p")
            country_paragraphs = []
            timestamp_paragraphs = []
            timestamp = ""

            timestamp_soup = BS(country_webpage)
            timestamp_soup = timestamp_soup.find("div", {"id": "wrapper"}).find_all("ul")

            ## Finding the fucking timestamp
            for x in timestamp_soup:
                timestamp_paragraphs.append(str(x))
            for element in timestamp_paragraphs:
                if element.find("Update") != -1:
                    timestamp = element.split("div")[4]
                
            ## Getting a list of page paragraphs
            for x in country_soup:
                country_paragraphs.append(str(x))

            ## Throwing some crap on the page out    
            country_paragraphs = country_paragraphs[4:-4]

            ## Throwing <strong> paras out (only titles) & stripping <p> tags for what remains
            to_delete = []
            for j in range(len(country_paragraphs)):
                if country_paragraphs[j].find("<strong>") != -1:
                    country_paragraphs[j] = ""
                else:
                    country_paragraphs[j] = country_paragraphs[j][3:-4]
                    
            ## Joining list elements into one string for the advisory (newline delimited) then converting into Unicode UTF-8
            country_paragraphs = '\n'.join(country_paragraphs)
            country_paragraphs = unicode(country_paragraphs, "utf-8")

            ## . . ._... THE POWER OF PYTHON . . ._...
            ## (Substring occurence counting)
            for key in advisory_phrases.keys():
                advisory_phrases[key][1] = len([m.start() for m in re.finditer(key, country_pages[0])])
                # print key, advisory_phrases[key][1]

            # Generating the rating (whichever indicator shows up the most gets to rate the country
            rating = -1
            max_score = -1
            for key in advisory_phrases.keys():
                if max_score < advisory_phrases[key][1]:
                    max_score = advisory_phrases[key][1]
                    rating = advisory_phrases[key][0]

            # "Most visits are trouble-free" and "Most visits are trouble free" override the rating
            if advisory_phrases["Most visits are trouble-free"][1] > 0 or advisory_phrases["Most visits are trouble free"][1] > 0:
                rating = 1
                
            # Can't decide? The country is "safe"
            elif rating == -1:
                rating = 1

            else:
                pass
            
            # FUCKING TIMESTAMP FORMATTING
            timestamp = timestamp.split("<")[0][2:]

            months = {"January":"Jan",
                      "February":"Feb",
                      "March":"Mar",
                      "April":"Apr",
                      "June":"Jun",
                      "July":"Jul",
                      "August":"Aug",
                      "September":"Sep",
                      "October":"Oct",
                      "November":"Nov",
                      "December":"Dec"}
            
            timestamp = timestamp.split(" ")
            timestamp[1] = months[timestamp[1]]
            timestamp = " ".join(timestamp)
            timestamp = timestamp[:-4] + timestamp[-2:]
            print timestamp
            
            date = time.strptime(timestamp, "%d %b %y")
            date = datetime.fromtimestamp(time.mktime(date))

            gathered_alerts.append({'date': date, 'country': country_codes_final[i], 'rating': rating, 'advisory': country_paragraphs, 'provider': 'GBR'})

        except:
            pass

    """
    
    for element in gathered_alerts:
        print element
        print

    """
    
    return gathered_alerts


"""
Sample Dictionary:

{'date': datetime.datetime(2013, 8, 12, 12, 3, 59),
'country': 'AFG',
'rating': 4,

'advisory': u" \nAFGHANISTAN - AVOID ALL TRAVEL\n
Foreign Affairs, Trade and Development Canada advises against all travel to Afghanistan, due to the unstable security situation, ongoing insurgency, terrorist attacks,
the risk of kidnapping and a high crime rate. If you choose to travel to Afghanistan despite this warning, you are taking a serious risk.
We strongly recommend that Canadians register with the Registration of Canadians Abroad (ROCA) service and include personal and professional contact details.
If you are already in Afghanistan, you should leave. The Embassy of Canada in Afghanistan's ability to provide consular and other support throughout the country
is very limited.\n",

'provider': 'CAN'}
"""

def main():
    alerts = get_alerts()

if __name__ == "__main__":
    main()

