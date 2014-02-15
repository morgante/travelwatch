from alchemyapi import AlchemyAPI
from geopy.geocoders import GoogleV3


def get_geocodes_from_text(text):
    return get_geocodes('text', text)

def get_geocodes_from_url(url):
    return get_geocodes('url', url)

def get_geocodes_from_html(html):
    return get_geocodes('html', html)

def get_geocodes(src_type, src):
    alchemyapi = AlchemyAPI()
    good_types = ['StateOrCounty', 'City', 'Country']
    response = alchemyapi.entities(src_type, src)
    geocodes = []
    for e in response['entities']:
        if e['type'] in good_types:
            print e['text'], e['type']
            geocodes.append(find_geocode(e['text']))
    print geocodes
    return geocodes

def find_geocode(text_loc):
    geolocator = GoogleV3()
    address, (latitude, longitude) = geolocator.geocode(text_loc)
    return (address, latitude, longitude)

def main():
    #alchemyapi = AlchemyAPI()
    text = "I'm wondering if it will find a city name, like Abu Dhabi, but I hope so!"
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

