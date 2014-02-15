from bs4 import BeautifulSoup as BS
import urllib2
import geocode

stem_url = "http://travel.state.gov"
warnings_url = "http://travel.state.gov/content/passports/english/alertswarnings.html"
page = urllib2.urlopen(warnings_url)
soup = BS(page.read())

gathered_alerts = []

rows = soup.find("table").find("tbody").find_all("tr")        
for row in rows:
    cells = row.find_all("td")
    if len(cells) < 1:
        print 'it is the header'
        continue
    notice_type = cells[0].get('class')[0]
    link = cells[2].find('a')
    #print notice_type, stem_url + link['href']
    gathered_alerts.append((notice_type, stem_url + link['href']))

print gathered_alerts

for alert in gathered_alerts:
    kind, url = alert
    print "Opening URL: ", url
    page = urllib2.urlopen(url)
    soup = BS(page.read())
    text = soup.find("div", {'class' : 'content_par'})
    paras = text.findAll("p")
    # Trim last 3 paragraphs b/c they contain extraneous info
    paras = paras[:len(paras) - 3]
    for para in paras:
        locs = geocode.get_geocodes_from_html(para)
        for loc in locs:
            if not str(loc[0]) == u'United States':
                print loc
    print '=========================='

