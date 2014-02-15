import requests

import sys
sys.path.append("..")

import data as db
payload = {'client_secret': 'DSTVFBTFZD4SD0CZBFXQKLZCIDSF2H25PEQ1OBDYCJFQCTGH',
               'client_id': 'MR2F2BFWBS0YK5BATB5OMTDF4MD4ESHAYCNU1UUQGT2ZRSOB', 'v': 20140202}

FSQ_DB='foursquare-db'

def get_geocode(txt):
    cached = db.find_one(FSQ_DB, {"query":txt})
    if cached != None:
        print 'Found cached result for ', txt
        mydict = {'placename':cached['placename'],
                  'longitude':cached['points'][0][0],
                  'latitude':cached['points'][0][1]}
        return mydict

    payload['query'] = txt
    r = requests.get("http://api.foursquare.com/v2/geo/geocode", params=payload)
    #print r.json()
    try:
       ans = r.json()['response']['geocode']['interpretations']['items'][0]
    except:
       return {}

    pos = ans['feature']['geometry']['center']
    lat = pos['lat']
    lng = pos['lng']
    name = ans['feature']['name']

    mydict = {'query':txt, 'placename':name, 'points':[(lng, lat)]}
    db.insert(FSQ_DB, mydict)

    return mydict


def reverse(point, exactly_one=True):
    # returns (new_place, new_point)
    cached = db.find_one(FSQ_DB, {"points": {"$in":[point] }})
    if cached != None:
        print 'OMG found a cached copy for point ', point
        return (cached['placename'], cached['points'][0])

    (lng, lat) = point
    payload['query'] = ''
    payload['ll'] = str(lat) + ',' + str(lng)

    r = requests.get("http://api.foursquare.com/v2/venues/search", params=payload)
    loc = r.json()['response']['venues'][0]['location']

    name = loc['city']
    new_point = (loc['lng'], loc['lat'])

    name_cached = db.find_one(FSQ_DB, {'placename':name})
    if name_cached != None:
        name_cached['points'].append(new_point)
        db[FSQ_DB].update({"points":name_cached["points"]})
    else:
        name_cached = {'placename':name, 'points':[new_point]}
        db.insert(FSQ_DB, name_cached)
    return (name, new_point)


