from alchemyapi import AlchemyAPI
from geopy.geocoders import GoogleV3, OpenMapQuest
import nltk_ner
from bs4 import BeautifulSoup as BS
import data as db

DEBUG=True
LAT_LONG_DB='lat-long-db'

def get_geocodes_from_text(text):
    return get_geocodes('text', text)

def get_geocodes_from_url(url):
    return get_geocodes('url', url)

def get_geocodes_from_html(html):
    return get_geocodes('html', html)

def get_geocodes(src_type, src, api_type='n'):
    locs = []
    geocodes = []

    if api_type == 'a':
        locs = get_locs_from_alchemy(src_type, src)
    else:
        locs = get_locs_from_nltk(src)

    for l in locs:
        geocodes.append(find_geocode(l))

    if DEBUG:
        print geocodes

    return geocodes

def get_locs_from_nltk(txt):
    clean = BS(txt).text
    return nltk_ner.extract_entities(clean)

def get_locs_from_alchemy(src_type, src):
    alchemyapi = AlchemyAPI()
    good_types = ['StateOrCounty', 'City', 'Country']

    try:
        response = alchemyapi.entities(src_type, src)
    except:
        return None

    locs = []
    for e in response['entities']:
        if e['type'] in good_types:
            if DEBUG:
                print e['text'], e['type']
            locs.append(e['text'])

    return locs

def find_geocode(text_loc):

    cached = db.find_one(LAT_LONG_DB, {"placename":text_loc})
    if cached != None:
        print 'got cached! ', cached
        return cached

    try:
        #geolocator = GoogleV3(secret_key='D0SLwabec9DkZtLLwmNwDeU3',
        #                      client_id='924851581047.apps.googleusercontent.com')
        geolocator = OpenMapQuest()
        address, (latitude, longitude) = geolocator.geocode(text_loc)
        mydict = {"placename": address, "longitude": longitude, "latitude": latitude}
        print mydict
        db.insert(LAT_LONG_DB, mydict)
        return mydict

    except Exception, err:
        print Exception, err
        return None

def main():
    #alchemyapi = AlchemyAPI()
    text = "It's great to be at NYU Abu Dhabi! Going home to Princeton NJ on Monday though..."
    nytimes = "http://www.nytimes.com/"
    nytimes2 = 'http://www.nytimes.com/2014/02/14/world/asia/on-indian-tea-plantations-low-wages-and-crumbling-homes.html?ref=world'
    html = "My name is <b>Bonnie</b> and I am from <h2>Ocean City MD</h2>"
    get_geocodes_from_html(html)
    get_geocodes_from_url(nytimes2)
    get_geocodes_from_text(text)
    #good_types = ['StateOrCounty', 'City', 'Country']
    #response = alchemyapi.entities('url', nytimes2)
    #print response
    #print response['entities']
    #for e in response['entities']:
    #    if e['type'] in good_types:
    #        print e['text'], e['type']
    #        find_geocode(e['text'])

if __name__ == "__main__":
    main()

