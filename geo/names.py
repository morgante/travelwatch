from countrycode import countrycode

# Note: Returns name in ALL CAPS
def get_name_from_code(code):
	names = countrycode(codes=[code], origin='iso3c', target='country_name')
        return names[0]

def get_code_from_name(name):
	codes = countrycode(codes=[name], origin='country_name', target='iso3c')
        return codes[0]

if __name__ == "__main__":
	code = 'ARE'
	if (get_code_from_name(get_name_from_code(code)) == code):
		print 'It works'
	else:
		print 'It is broken'
