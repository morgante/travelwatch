import data as db
import embassy_alerts as emAlerts
from collection import Counter

import twitter_fetch as twitter
import time, datetime

#db.insert('lol', {'hello': 'sir'})

#print db.find_one('lol')

word_list = ["protests", "government"]

TWITTER_DB='twitter_db'

def fetch_twitter():
    names = ['AJEnglish', 'BBCBreaking', 'WSJMidEast', 'AJELive', 'ReutersGulf', 'AlArabiya_Eng', 'RT_com',
         'BreakingNews', 'cnnbrk', 'SkyNewsBreak', 'ABCNewsLive', 'AP']

    cur_date = datetime.datetime.now()
    last_date = datetime.datetime.now() - datetime.timedelta(12)
    step = datetime.timedelta(4)

    while cur_date > last_date:
        tweets = twitter.get_tweets(screen_names=names, start_date=cur_date, 
                                    end_date=cur_date - step)
        cur_date = cur_date - step
        for tweet in tweets:
            db.insert(TWITTER_DB, tweet)
    print 'Done fetching tweets.'

def fetch_embassy_alerts():
    frequencies = []
    for i in range(len(em_alerts)):
        alert_text = em_alerts[i]['alert_text']
        alert_text = alert_text.split(" ",)

if __name__ == "__main__":
    fetch_twitter()

# def main():
# 	start = '20081019'
# 	end = '20091010'

# 	articles = nyt.search(start=start, end=end)

# 	db.save_articles(articles)

# 	twitter = twitter.search(start=start, end=end)

# 	db.save_twitter(twitter)

# main()
