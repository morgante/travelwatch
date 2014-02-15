from bs4 import BeautifulSoup as BS
import urllib2
import time
from datetime import datetime

DEBUG=True

def get_embassy_alerts():
    stem_url = "http://travel.state.gov"
    warnings_url = "http://travel.state.gov/content/passports/english/alertswarnings.html"
    page = urllib2.urlopen(warnings_url)
    soup = BS(page.read())

    alert_dicts = []

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
        alert_dict = {"country": country, "rating": rating,  "date":alert_time}

        adv_url = stem_url + link['href']

        print "Opening URL: ", adv_url
        page = urllib2.urlopen(adv_url)
        soup = BS(page.read())
        text = soup.find("div", {'class' : 'content_par'})
        paras = text.findAll("p")
        # Trim last 3 paragraphs b/c they contain extraneous info
        paras = paras[:len(paras) - 3]        
        alert_dict['advisory'] = ''.join([p.text for p in paras])
        alert_dicts.append(alert_dict)
        if DEBUG:
            try:
                print alert_dict
            except:
                pass

    if DEBUG:
        try:
            print alert_dicts
        except:
            pass

    return alert_dicts

def main():
    get_embassy_alerts()

if __name__ == "__main__":
    main()
