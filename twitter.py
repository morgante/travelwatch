import twitter,time,datetime
import geocode

print time.time()
print datetime.datetime.now()

api = twitter.Api(consumer_key='B50F3gDc5Cno0tegLCAg',
                      consumer_secret='8Za4gCQOiejidwTFx7jtUFj3IRNVlFwbpAMQsq8SBxo',
                      access_token_key='18345495-DpGYvrRy7W0GMFAk0DuFmyt9xZOwY4ceha79Ygz38',
                      access_token_secret='QXCPHzWnrJQEYephcUiAuNyMFLEpXxD39qX7e3gveezZ7')


names = ['AJEnglish', 'BBCBreaking', 'WSJMidEast', 'AJELive', 'ReutersGulf', 'AlArabiya_Eng', 'RT_com',
         'BreakingNews', 'cnnbrk', 'SkyNewsBreak', 'ABCNewsLive', 'AP']
test_names=['AJEnglish']

DEBUG=True

def get_datetime_for_status(s):
    delta = time.time() - s.created_at_in_seconds
    post_date = datetime.datetime.now() - datetime.timedelta(0, delta)
    return post_date

# Gives a very rough id for a date. Granularity tuning using step var.
def find_id_for_date(goal_date, username):
    #print goal_date, username
    oldest_id = None
    oldest_time = None
    step=50
    while oldest_time == None or oldest_time > goal_date:
        if oldest_id == None:
            statuses = api.GetUserTimeline(screen_name=username, count=step)
        else:
            statuses = api.GetUserTimeline(screen_name=username, count=step, max_id=oldest_id)
            
        s = statuses[len(statuses) - 1]
        delta = time.time() - s.created_at_in_seconds
        post_date = datetime.datetime.now() - datetime.timedelta(0, delta)

        if oldest_time == None or post_date < oldest_time:
            oldest_time = post_date
            oldest_id = s.id

        if post_date > goal_date:
            #print post_date
            continue

    if DEBUG:
        print oldest_id, oldest_time
    return oldest_id

def get_tweets(screen_names=test_names, start_date=datetime.datetime.now(), 
               end_date=datetime.datetime.now() - datetime.timedelta(2)):

    tweets = []

    print 'Start date, end date: ', start_date, end_date

    for name in screen_names:
        if DEBUG:
            print name
        end_id = find_id_for_date(end_date, name)
        start_id = find_id_for_date(start_date, name)

        print 'end_id, start_id: ', end_id, start_id

        statuses = []
        
        working_id = end_id
        while working_id < start_id:
            q = api.GetUserTimeline(screen_name=name, count=100, since_id=working_id)
            statuses = statuses + q
            working_id = q[0].id

        for s in statuses:
            tweets.append({"status":s.text, "time": get_datetime_for_status(s), "user":name})
            if DEBUG:
                try:
                    print str(s.text), get_datetime_for_status(s)
                except:
                    pass
    return tweets


if __name__ == "__main__":
    tweets = get_tweets()
    print tweets
