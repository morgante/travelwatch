
import pycountry

def article_to_country_codes(article):
    h = article['headline']
    t = article['snippet']
    country_names = [c.name for c in pycountry.countries]
    country_codes = [c.numeric for c in pycountry.countries]

    codes = []
    for i in range(len(country_names)):
        if country_names[i] in h or country_names[i] in t:
            codes.append(country_codes[i])
    return codes

