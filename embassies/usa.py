from bs4 import BeautifulSoup as BS
import urllib2
import time
from datetime import datetime

import sys
sys.path.append("..")
import geo.names as geonames
import geo.code as geocode

def get_alerts(limit=None, DEBUG=False):
    stem_url = "http://travel.state.gov"
    warnings_url = "http://travel.state.gov/content/passports/english/alertswarnings.html"
    page = urllib2.urlopen(warnings_url)
    soup = BS(page.read())

    alert_dicts = []

    print ('limit', limit)    

    rows = soup.find("table").find("tbody").find_all("tr")        
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 1:
            continue
        notice_type = cells[0].get('class')[0]

        # Grab time, save it as a datetime obj
        time_thingy = time.strptime(cells[1].text, "%B %d, %Y")
        alert_time = datetime.fromtimestamp(time.mktime(time_thingy))

        link = cells[2].find('a')
        country = link.contents[0].split(' ')
        country = ' '.join(country[:len(country)-2])
        country = country.strip()
        
        rating = 4
        if notice_type == 'alert':
            rating = 2

        try:
            code = geonames.get_code_from_name(country)
        except:
            continue

        alert_dict = {"provider": "USA", "country": code, "rating": rating,  "date":alert_time}

        adv_url = stem_url + link['href']

        if(DEBUG):
            print "Opening URL: ", adv_url

        page = urllib2.urlopen(adv_url)
        soup = BS(page.read())
        text = soup.find("div", {'class' : 'content_par'})
        paras = text.findAll("p")
        # Trim last 3 paragraphs b/c they contain extraneous info
        paras = paras[:len(paras) - 3]        
        alert_dict['advisory'] = ''.join([p.text for p in paras])
        alert_dicts.append(alert_dict)

        try:
            alert_dict["positions"] = geocode.get_geocodes_from_text(alert_dict['advisory'])
        except:
            alert_dict["positions"] = []

        if DEBUG:
            try:
                print alert_dict
            except:
                pass

        if (limit is not None and len(alert_dicts) >= limit):
            break;

    if DEBUG:
        try:
            print alert_dicts
        except:
            pass

    return alert_dicts

def main():
    get_alerts()

if __name__ == "__main__":
    main()
