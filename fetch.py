import data as db
import embassy_alerts as emAlerts
from collection import Counter

word_list = ["protests", "government"]

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

em_alerts = emAlerts.get_embassy_alerts()
frequencies = []
for i in range(len(em_alerts)):
   alert_text = em_alerts[i]["alert_text"]
   alert_text = alert_text.split(" ",)  
	   
  

