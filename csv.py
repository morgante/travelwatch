import pprint
from geo.code import find_geocode
import data as db

# Fills in the State for towns/cities lacking that data
def get_entries():
  csv = open('usa_crime_data_2008.csv').readlines()
  for line_no in xrange(len(csv)):
    split = csv[line_no].split(',')
    if not split[0]:
      csv[line_no] = csv[line_no - 1].split(',')[0] + csv[line_no]

  lines = [l for l in csv if not l=='\n']

  entries = []

  for line in lines[1:]: # [1:] to ignore column title
  #Commas in town names were replaced with '&' for CSV, revert back
    geo = find_geocode("%s,%s"%(values[1].replace('&',','),values[0]))
    
    ## Cached results return differently than noncached:
    if "points" in geo:
      lon = geo['points'][0]['longitude']
      lat = geo['points'][0]['latitude']
    else:
      lon = geo['longitude']
      lat = geo['latitude']    
    ## Based on DB Schema
    try:
      entry = { 
              'position' : { 'longitude': lon,
                             'latitude': lat },
              'crimes' : {
                         'violent crime': int(values[3]),
                         'murder and nonnegligent manslaughter': int(values[4]),
                         'forcible rape': int(values[5]),
                         'robbery': int(values[6]),
                         'aggravated assault': int(values[7]),
                         'property crime': int(values[8]),
                         'burglary': int(values[9]),
                         'larceny/theft': int(values[10]),
                         'motor vehicle theft': int(values[11])
                         }
              }
      #db.insert_crime(entry['position'], entry['crimes'])
      #pprint.pprint(entry)
      entries.append(entry)
    except Exception as e:
      ## Signals bad entry as noted by footnotes in spreadsheet
      print "Entry discarded, see footnotes 3,5 in spreadsheet"
      print e, values[0], values[1]
  return entries

def upload_entries():
  entries = get_entries()
  db.insert_crimes(entries)

