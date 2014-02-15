from geopy.geocoders import GoogleV3

g = GoogleV3()
#point has to be a string
point = "13.7278956, 100.5241235"
(new_place, new_point) = g.reverse(point, exactly_one=True)

print new_place
