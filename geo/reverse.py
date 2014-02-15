from geopy.geocoders import GoogleV3, Nominatim
import requests
import foursquare as g


def get_city(point):
   (new_place, new_point) = g.reverse(point, exactly_one=True)
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
   (new_place, new_point) = g.reverse(point, exactly_one=True)
   splited = new_place.split(',')
   # address it's different for the states
   if splited[-1] == "USA":
	remove_address = splited[-2].split(" ")
	return remove_address[0]	
   else:
	# no state
	return ""


def get_country(point):
   (new_place, new_point) = g.reverse(point, exactly_one=True)
   splited = new_place.split(',')
  
   return splited[-1]
   
