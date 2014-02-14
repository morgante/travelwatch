from alchemyapi import AlchemyAPI
from geopy.geocoders import GoogleV3

def find_geocode(text_loc):
    geolocator = GoogleV3()
    address, (latitude, longitude) = geolocator.geocode(text_loc)
    print(address, latitude, longitude)

def main():
    alchemyapi = AlchemyAPI()
    text = "I'm wondering if it will find a city name, like Abu Dhabi, but I hope so!"
    nytimes = "http://www.nytimes.com/"
    nytimes2 = 'http://www.nytimes.com/2014/02/14/world/asia/on-indian-tea-plantations-low-wages-and-crumbling-homes.html?ref=world'
    good_types = ['StateOrCounty', 'City', 'Country']
    response = alchemyapi.entities('url', nytimes2)
    #print response
    #print response['entities']
    for e in response['entities']:
        if e['type'] in good_types:
            print e['text'], e['type']
            find_geocode(e['text'])

main()

