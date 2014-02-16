#f = open('usa_crime_data_2008.csv')
#mapping = {}
#for l in f.readlines()[1:]:
#  s = l.split(',')
#  state = s[0]
#  town = s[1].replace('&',',')
#  pop = s[2]
#  mapping["%s,%s"%(town,state)] = pop

#import pprint
#pprint.pprint(mapping)

def get_town_list():
  f = open('usa_crime_data_2008.csv')
  lst = []
  for l in f.readlines()[1:]:
    lst.append(l.split(',')[1])

#  import pprint
#pprint.pprint(lst)
  return lst
