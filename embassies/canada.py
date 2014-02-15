# Canadian embassies
from bs4 import BeautifulSoup as BS
import urllib2
import time, datetime
from datetime import datetime

DEBUG=True

def get_alerts():

    """
    Rankings for safety: 1 is safest; 4 is most dangerous
    """
    advisory_phrases = {'AVOID ALL TRAVEL':4,
                        'AVOID NON-ESSENTIAL TRAVEL': 3,
                        'Exercise a high degree of caution':2,
                        'Exercise normal security precautions':1}
    stem_url = "http://travel.gc.ca/"
    url = "http://travel.gc.ca/travelling/advisories"
    page = urllib2.urlopen(url)
    soup = BS(page.read())

    gathered_alerts = []

    rows = soup.find("table", {"id": "reportlist"}).find("tbody").find_all("tr")
    print len(rows)
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 1:
            continue
        link = cells[1].find('a')
        country_name = link.contents[0]
        country_url = stem_url + link['href']

        advisory_rating = -1
        for phrase in advisory_phrases:
            if phrase in cells[2].text:
                advisory_rating = advisory_phrases[phrase]
                break

        date = time.strptime(cells[3].text, "%Y-%m-%d %H:%M:%SZ")
        date = datetime.fromtimestamp(time.mktime(date))
        country_dict = {"country":country_name,
                        "rating":advisory_rating,
                        "date":date}
        c_page = urllib2.urlopen(country_url)
        c_soup = BS(c_page.read())
        adv_text = c_soup.find("div", {"class":"AdvisoryContainer"}).text
        country_dict['advisory'] = adv_text
        print country_dict
        gathered_alerts.append(country_dict)

    return gathered_alerts

def main():
    alerts = get_alerts()

if __name__ == "__main__":
    main()
