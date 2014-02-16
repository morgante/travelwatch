from geopy.geocoders import GoogleV3, Nominatim
import requests
import random
#import foursquare as g

g = Nominatim()

# TODO: ALL THESE METHOS SHOULD TAKE POINTS IN {"latidue": x, "longitude": y} FORM


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
<<<<<<< HEAD
   
=======
   return random.choice(['NY', 'VT', 'CA'])

 #   (new_place, new_point) = g.reverse(point, exactly_one=True)
 #   splited = new_place.split(',')
 #   # address it's different for the states
 #   if splited[-1] == "USA":
	# remove_address = splited[-2].split(" ")
	# return remove_address[0]	
 #   else:
	# # no state
	# return ""
>>>>>>> a36e58e2be902a0f1cfd48e7f95de0c27cae5199


def get_country(point):
   (new_place, new_point) = g.reverse(change_format(point), exactly_one=True)
   splited = new_place.split(',')  
   return splited[-1]
  
#print change_format({'latitude': 123, 'longitude':5678}) 
