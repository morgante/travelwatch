from bs4 import BeautifulSoup as BS
import urllib2
import time
from datetime import datetime
import geocode

DEBUG=True

def get_embassy_alerts():
    stem_url = "http://travel.state.gov"
    warnings_url = "http://travel.state.gov/content/passports/english/alertswarnings.html"
    page = urllib2.urlopen(warnings_url)
    soup = BS(page.read())

    gathered_alerts = []

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
        gathered_alerts.append((notice_type, alert_time, stem_url + link['href']))

    alerts_dicts = []

    for alert in gathered_alerts:
        kind, alert_time, url = alert
        alert_dict = {"kind": kind, "url":url, "date":alert_time}

        if DEBUG:
            print "Opening URL: ", url
        page = urllib2.urlopen(url)
        soup = BS(page.read())
        text = soup.find("div", {'class' : 'content_par'})
        paras = text.findAll("p")
        # Trim last 3 paragraphs b/c they contain extraneous info
        paras = paras[:len(paras) - 3]
        
        alert_dict['alert_text'] = ''.join([p.text for p in paras])
        geocodes = []

        for para in paras:
            locs = geocode.get_geocodes_from_html(para)
            for loc in locs:
                if loc == None or len(loc) < 1:
                    continue
                if not str(loc[0]) == u'United States':
                    geocodes.append(loc)

        alert_dict['geocodes'] = geocodes
        if DEBUG:
            try:
                print alert_dict
            except:
                pass
        alerts_dicts.append(alert_dict)

    if DEBUG:
        try:
            print alerts_dicts
        except:
            pass

    return alerts_dicts

def main():
    get_embassy_alerts()

if __name__ == "__main__":
    main()
