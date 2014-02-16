def gen_map():
  lines = open('usa_crime_data_2008.csv').readlines()
  mapping = {}
  for l in lines[1:]: #throw out the title line
    mapping[l.split(",")[0]] = 0
  
  for l in lines[1:]: # ''
    split = l.split(",")
    state = split[0]
    pop = split[2]
    mapping[state]+=int(pop)

  return mapping

def getPop(state):
  m = gen_map()
  try: 
    return m[state.strip().upper()]
  except:
    return m["ALABAMA"]
