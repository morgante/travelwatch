
import retrieve

import sys
sys.path.append("..")
from geo import code
import data as db

def get_risk_types():
    terrorism=['terrorist','bombing','terrorism','militants']
    murder=['murder','killed','kill','shot','shoot','knife','death','killer','murderer','homicide']
    rape=['rape','gang rape','rapist','sexual assault']
    weather=['earthquake','cyclone','tsunami','natural disaster', 'hurricane','fire']
    war=['war','conflict','sectarian','violence','chemical weapon','nuclear','ethnic v']

    d = {'terrorism':terrorism,
         'murder':murder,
         'rape':rape,
         'war':war
         }

    return d

# Input: an article w/ headline, text
# Output: a matrix like so...

"""
for each loc in doc:
  freq for a given risk type
"""

def get_risks_for_article(article):
    head_len = len(article['headline'])
    text_len = len(article['text'])

    #locs = code.get_geocodes_from_text(article['headline']) + code.get_geocodes_from_text(article['text'])

    #print locs

    risks = get_risk_types()
    risk_freqs = {}

    for k,v in risks.iteritems():
        hcount = 0
        tcount = 0
        for phrase in v:
            hcount += str.lower(article['headline'].encode('ascii', 'ignore')).count(phrase)
            tcount += str.lower(article['text'].encode('ascii','ignore')).count(phrase)
        print hcount, tcount
        risk_freqs[k] = ((hcount * 2.0) / head_len) + ((tcount * 1.0) / text_len) 

    print risk_freqs
    return risk_freqs

def process_articles_from_db():
    articles = db.find('articles',{})

    locs = {}
    count = 0
    for article in articles:
        print article
        risk_freqs = get_risks_for_article(article)

        a_locs = code.get_geocodes_from_text(article['headline']) + code.get_geocodes_from_text(article['text'])
        for al in a_locs:
            try:
                if not al['placename'] in locs:
                    locs[al['placename']] = risk_freqs
                else:
                    for k,v in risk_freqs.iteritems():
                        locs[al['placename']][k] += v
            except:
                pass
        count += 1
    print locs

    loc_list = [locs[key] for key in locs]
    loc_list.sort(sorter)
    print loc_list

def sorter(a,b):
    return cmp(a['murder'], b['murder'])

def main():
    fake_data = {
        "_id" : "52ffd849bc004d010f5adadd",
	"headline" : "Israeli Forces Kill Palestinian at Gaza Border",
	"positions" : [ ],
	"keywords" : [
		"United States Economy",
		"Women's Rights",
		"Women and Girls",
		"Birth Rates",
		"Income"
	],
	"text" : "GAZA - Israeli forces stationed along the border with Gaza fatally shot one Palestinian man and wounded another on Thursday, according to a Palestinian official.",
	"date" : "2012-12-07T20:55:00Z"}
    process_articles_from_db()
    #get_risks_for_article(fake_data)
  
if __name__ == "__main__":
    main()
