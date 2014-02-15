def get_name_from_code(code):
	code = 'USA' # 3-letter country code
	name = 'United States of America'

	return name

def get_code_from_name(name):
	name = 'United States of America'
	code = 'USA'

	return code

if __name__ == "__main__":
	code = 'UAE'
	if (get_code_from_name(get_name_from_code(code)) == code):
		print 'It works'
	else:
		print 'It is broken'