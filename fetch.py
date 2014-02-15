import data as db


db.insert('lol', {'hello': 'sir'})

print db.find_one('lol')

# def main():
# 	start = '20081019'
# 	end = '20091010'

# 	articles = nyt.search(start=start, end=end)

# 	db.save_articles(articles)

# 	twitter = twitter.search(start=start, end=end)

# 	db.save_twitter(twitter)

# main()