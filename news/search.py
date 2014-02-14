
def search(
	query=None,
	filter=None,
	begin="20080101",
	end="20081231",
	page=None,
	pages=10,
	limit=100,
	sort=None,
	fields=["web_url", "headline", "keywords"],
	highlight=False,
	facet_field="source",
	facet_filter=False
	):
		
		# ALWAYS return id
		return [{"id":"4fd3a2548eb7c8105d8ea27e", "web_url": "http://google.com", "headline": "Man bites dog", "keywords": ["man", "dog"]}]; # Actually return stories here


if __name__ == "__main__":
	# Do testing in here
	print 'hello'
	print search()