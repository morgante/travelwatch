## News Scraper by Nishant Mohanchandra (nm1345@nyu.edu)

"""
NYT Article Search API requires the following URI:
http://api.nytimes.com/svc/search/v2/articlesearch.response-format?[q=search term&fq=filter-field:(filter-term)&additional-params=values]&api-key=####
"""

## Module dependencies
from time import sleep
from urllib import *
from pprint import *
import json

## Do not change this unless you know what you're doing (page request limit & dump location)
PageLimit = 10

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
    "page": "", ## Page number - filling this in with "2" for example gives you the results of page 2 (10 - 19)
    "sort" : "", ## Newest | Oldest | (empty; no sort)
    "fl" : "", ## Field list
    "hl" : False, ## Enable highlighting
    "facet_field" : "source", ## Facet field list
    "facet_filter" : False, ## Apply any given facet fields
    "callback" : "" ## Give a function name if you want to pass query results to it as input (If you query .JSONP instead of .JSON you need to fill this in)
}

"""
NY Times provides the following filters for fq:

body	                Multiple tokens
body.search	        Left-edge n-grams

creative_works	                Single token
creative_works.contains	        Multiple tokens

day_of_week	        Single token
document_type	        Case-sensitive exact match

glocations	        Single token
glocations.contains	Multiple tokens

headline	        Multiple tokens
headline.search	        Left-edge n-grams

kicker	                Single token
kicker.contains	        Multiple tokens

news_desk	        Single token
news_desk.contains	Multiple tokens

organizations	        Single token
organizations.contains	Multiple tokens

persons	                Single token
persons.contains	Multiple tokens

pub_date	        Timestamp (YYYY-MM-DD)
pub_year	        Integer
secpg	                Multiple tokens

source	                Single token
source.contains	        Multiple tokens

subject	                Single token
subject.contains	Multiple tokens

section_name	        Single token
section_name.contains	Multiple tokens

type_of_material	        Single token
type_of_material.contains	Multiple tokens

web_url	                Single token (case-sensitive)
word_count	        Integer


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

## The search / scrape function (Default values search all articles in 2008 and returns IDs, URLs, Headlines & Keywords)
def search(
            query=None,
            filters={"news_desk": ["N.Y. / Region","World / Asia Pacific","U.S."], "document_type":["article"]}, # Input here is a list of dictionaries EVEN FOR ONE ELEMENT: ["web_url"], etc.
            begin="20080101",
            end="20090101",
            page=None,
            pages=1,
            sort=None,
            fields=["_id","web_url","lead_paragraph","abstract","headline","keywords","pub_date","word_count","source","document_type","news_desk"],
            highlight=False,
            facet_field=None, # Input here is a list of strings EVEN FOR ONE ELEMENT
            facet_filter=False
	):

    ## Result storage
    result = []

    for source in APIKeys.keys():

        parameters = [query,filters,begin,end,page,pages,sort,fields,highlight,facet_field,facet_filter]
        for i in range (len(parameters)):
            if parameters[i] == None or parameters[i] == False:
                parameters[i] = ""

        ## Filter fields follow special Lucene syntax: http://lucene.apache.org/core/2_9_4/queryparsersyntax.html
        ## Editing parameters[1] - the filter fields - to reflect this

        ## FIGURING OUT FILTERS
        ## INPUT EG: {"news_desk": ["Sports","Foreign"]}
        ## EG: filter-field1:("filter-term1" "filter-term2") AND filter-field2:("filter-term3" "filter-term4")
        ## EG (desired output): &fq=news_desk:("Sports" "Foreign") AND glocations:("NEW YORK CITY")
        if parameters[1] != "":
            FQ_STRING = ""
            for key in parameters[1].keys():
                FQ_STRING = FQ_STRING + key + ":("
                for element in parameters[1][key]:
                    FQ_STRING = FQ_STRING + '"' + element + '" '
                FQ_STRING = FQ_STRING[:-1] + ") AND "
            ## Slice the last " AND" off
            FQ_STRING = FQ_STRING[:-5]
            parameters[1] = FQ_STRING

        ## FIGURING OUT REGULAR FIELDS
        if parameters[7] != "":
            FL_STRING = ""
            for item in parameters[7]:
                FL_STRING = FL_STRING + item + ","
            ## Slice the last "," off
            FL_STRING = FL_STRING[:-1]
            parameters[7] = FL_STRING

        ## FIGURING OUT FACET FIELDS
        if parameters[9] != "":
            FL_STRING = ""
            for item in parameters[9]:
                FL_STRING = FL_STRING + item + ","
            ## Slice the last "," off
            FL_STRING = FL_STRING[:-1]
            parameters[9] = FL_STRING
            
        QueryFields = {
            "q" : parameters[0], ## Query term
            "fq" : parameters[1], ## Filter query term
            "begin_date" : parameters[2], ## YYYYMMDD
            "final_date" : parameters[3], ## YYYYMMDD
            "page": parameters[4], ## Page number
            ## parameters[5] is the limit on page requests!
            "sort" : parameters[6], ## Newest | Oldest | (empty; no sort)
            "fl" : parameters[7], ## Field list
            "hl" : parameters[8], ## Enable highlighting
            "facet_field" : parameters[9], ## Facet field list
            "facet_filter" : parameters[10], ## Apply any given facet fields
            "callback" : "" ## Give a function name if you want to pass query results to it as input (If you query .JSONP instead of .JSON you need to fill this in)
        }

        ## Generating the query string to append to the base address
        QUERY_STRING = ""

        ## Function that generates a query string based on the values in QueryFields
        def Generate_QString(API):
            QUERY_STRING = ""
            for key in QueryFields.keys():
                if QueryFields[key] != "" and QueryFields[key] != False:
                    QUERY_STRING = QUERY_STRING + key + "=" + QueryFields[key] + "&"
                else:
                    pass
            QUERY_STRING = QUERY_STRING + "api-key=" + APIKeys[API]
            return QUERY_STRING

        QUERY_STRING = Generate_QString(source);

        ## Appending API Key information & generating full request
        QUERY = QueryStrings[source] + QUERY_STRING

        # print "Query to API generated: " + QUERY + "\n"

        ## Requesting data from news source
        APIRequest = urlopen(QUERY)
        JSONData = json.load(APIRequest)

        # QueryFields["facet_field"] = ""

        ## Appending results page by page to a list
        for i in range(0,pages):
            QueryFields["page"] = str(i)
            QUERY_STRING = Generate_QString(source);
            QUERY = QueryStrings[source] + QUERY_STRING
            print QUERY_STRING
            APIRequest = urlopen(QUERY)
            JSONData = json.load(APIRequest)
            result.append(handleJSON(JSONData))

            # Sleeping for 0.1s to avoid overloading the NYT API
            sleep(0.1)

            ## BREAK AFTER A FEW PAGES: BE CAREFUL!
            ## MAKE SURE YOUR QUERY ISN'T RETURNING MILLIONS OF RESULTS
            if i == PageLimit:
                break

    return result


## Main function
def main():
    print "Processing query...\n"
    x = search()
    print "Query complete! Results are stored in x.\n"


## Handler for egregiously silly cases
def getValFromDict(d,k):
    if k in d:
        return d[k]
    else:
        return None


## JSON Handler (Thanks Bonnie!)
def handleJSON(raw_json):
    docs = raw_json["response"]["docs"]
    articles = []
    for d in docs:
        headline = getValFromDict(d, "headline")
        try:
            if len(headline) > 0:
                headline = headline["main"]
        except:
            pass
        snippet = getValFromDict(d, "snippet")
        uniq_id = getValFromDict(d, "_id")
        url = getValFromDict(d, "web_url")
        date = getValFromDict(d, "pub_date")
        lead = getValFromDict(d, "lead_paragraph")
        obj = {"headline":headline, "snippet":snippet,
               "lead_paragraph":lead, "_id":uniq_id,
               "url":url, "date":date}
        articles.append(obj)
    return articles

if __name__ == "__main__":
    main()

