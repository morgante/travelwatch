from geopy.geocoders import GoogleV3, Nominatim
import requests
import random
#import foursquare as g

g = Nominatim()

# DONE: ALL THESE METHOS SHOULD TAKE POINTS IN {"latidue": x, "longitude": y} FORM


def change_format(point):
	return str(point.get('latitude'))+", "+str(point.get('longitude'))
	
def get_city(point):
   (new_place, new_point) = g.reverse(change_format(point), exactly_one=True)
   #new_place = "76 Surawong Road, Si Phraya, Bang Rak, Bangkok 10500, Thailand"
   if new_place == None or new_point == None:
       return None

   splitted = new_place.split(',')
   # address it's different for the states
   if splitted[-1] == "USA":
	return splitted[-3]
   else:
	# address needs to be stripped
	# addresses recevied are inconsistent
	remove_address = splitted[-2].lstrip() 
	return remove_address.split(" ")[0]


def get_state(point):

	(new_place, new_point) = g.reverse(change_format(point), exactly_one=True)
 	splited = new_place.split(',')
	print splited[-1]
 #   # address it's different for the states
	if splited[-1] == "USA" or "America" in splited[-1]:
		remove_address = splited[-2].split(" ")
		print remove_address
		if remove_address[0] ==  "":
			return splited[-3]
		return remove_address[0]	
	else:
	#no state
		print "no state"
		return ""
   #return random.choice(['NY', 'VT', 'CA'])


def get_country(point):
   (new_place, new_point) = g.reverse(change_format(point), exactly_one=True)
   splited = new_place.split(',')  
   return splited[-1]
#bad coordinates below  
#print get_state({'latitude': 40.411766, 'longitude': -79.995607}) 
