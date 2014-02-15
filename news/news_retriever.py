## News Scraper by Nishant Mohanchandra (nm1345@nyu.edu)

## TO DOs
## 1) Figure out how to pull only the headlines
## 2) Discard irrelevant articles ("Arts & Leisure", etc.)

## Do not change this unless you know what you're doing (page request limit & dump location)
PageLimit = 10
DumpFile = "dump.txt"

## Module dependencies
from urllib import *
from pprint import *
import json

## Dictionary of API keys
APIKeys = {
    "NY Times":"a23184e7a28923153d114039b3b92b8e:7:68825444"
    }

## Dictionary of base query strings
QueryStrings = {
    "NY Times":"http://api.nytimes.com/svc/search/v2/articlesearch.json?"
    }

## API Query fields
QueryFields = {
    "q" : "", ## Query term
    "fq" : "", ## Filter query term
    "begin_date" : "20080101", ## YYYYMMDD
    "final_date" : "20081231", ## YYYYMMDD
    "page": "", ## Page number
    "sort" : "", ## Newest | Oldest | (empty; no sort)
    "fl" : "", ## Field list
    "hl" : False, ## Enable highlighting
    "page" : "", ## Page number - filling this in with "2" for example gives you the results of page 2 (10 - 19)
    "facet_field" : "source", ## Facet field list
    "facet_filter" : False, ## Apply any given facet fields
    "callback" : "" ## Give a function name if you want to pass query results to it as input (If you query .JSONP instead of .JSON you need to fill this in)
}

"""
NY Times provides the following fields for fl:

web_url
snippet
lead_paragraph
abstract
print_page
blog
source
multimedia
headline
keywords
pub_date
document_type
news_desk
byline
type_of_material
_id
word_count


NY Times provides the following facet fields:

section_name
document_type
type_of_material
source
day_of_week

More here: http://developer.nytimes.com/docs/read/article_search_api_v2#facets
"""

def main():

    ## Generating the query string to append to the base address
    QUERY_STRING = ""

    ## Function that generates a query string based on the values in QueryFields
    def Generate_QString():
        QUERY_STRING = ""
        for key in QueryFields.keys():
            if QueryFields[key] != "" and QueryFields[key] != False:
                QUERY_STRING = QUERY_STRING + key + "=" + QueryFields[key] + "&"
            else:
                pass
        QUERY_STRING = QUERY_STRING + "api-key=" + APIKeys["NY Times"]
        return QUERY_STRING

    QUERY_STRING = Generate_QString();

    ## Appending API Key information & generating full request
    QUERY = QueryStrings["NY Times"] + QUERY_STRING

    ## Requesting data from news source
    APIRequest = urlopen(QUERY)
    JSONData = json.load(APIRequest)

    ## Finding the total number of pages = (Number of articles / 10) + 1
    TotalPages = (JSONData[u'response'][u'facets'][u'source'][u'total'] / 10) + 1
    QueryFields["facet_field"] = ""

    ## Appending results page by page to a .TXT file
    for i in range(1,TotalPages):
        QueryFields["page"] = str(i)
        QUERY_STRING = Generate_QString();
        QUERY = QueryStrings["NY Times"] + QUERY_STRING
        APIRequest = urlopen(QUERY)
        JSONData = json.load(APIRequest)
        json.dump(JSONData, open(DumpFile,'a'))

        ## BREAK AFTER A FEW PAGES: BE CAREFUL!
        ## MAKE SURE YOUR QUERY ISN'T RETURNING MILLIONS OF RESULTS
        if i == PageLimit:
        break

main()
