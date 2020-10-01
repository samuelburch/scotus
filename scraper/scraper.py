import twint
import time
import datetime
import schedule
import mariadb
import sys

def main():
    print('\ntwint version: ' + twint.__version__)
    tweets = search("realDonaldTrump")
    for tweet in tweets:
        insert_database(cur,tweet)
    
    conn.commit() 
    conn.close()


    #
    #for tweet in tweets:
    #    print ('ID: {}  USERNAME: {}\n\t{}'.format(tweet.id, tweet.username, tweet.tweet))
    #schedule.every().day.do(search)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

try:
    conn = mariadb.connect(
        user="root",
        password="password",
        host="172.17.0.2",
        port=3306,
        database="SCOTUS"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

def insert_database(cur, t):
    try:
        q = (27*'?, ')[:-2]
        cmd=f'insert into tweets(id,conversation_id,datestamp,timestamp,timezone,user_id,username,name,place,    \
        tweet,mentions,urls,photos,replies_count,retweets_count,likes_count,hashtags,cashtags,link,retweet,     \
        quote_url,video,user_rt_id,near,geo,source,retweet_date)                                                \
        VALUES ({q})                \
        on duplicate key update id=id;'

        cur.execute(cmd, (t.id, t.conversation_id, t.datestamp, t.timestamp, t.timezone, t.user_id, t.username,
        t.name, t.place, t.tweet, ', '.join(t.mentions), ', '.join(t.urls), ', '.join(t.photos), t.replies_count,
        t.retweets_count, t.likes_count, ', '.join(t.hashtags), ', '.join(t.cashtags), t.link, t.retweet,
        t.quote_url, t.video, t.user_rt_id, t.near, t.geo, t.source, t.retweet_date))
    except mariadb.Error as e:
        print(f"Error: {e}")


def search(
    username = None, 
    search = None, 
    Location = False, 
    show_hashtags=True, 
    limit = None, 
    filter_retweets = True, 
    min_likes = 0, 
    numdays = 1
    ):

    since = datetime.date.today()-datetime.timedelta(numdays)
    c = twint.Config
    
    c.Username = username
    c.Search = search
    c.Show_hashtags = show_hashtags
    c.Filter_retweets = filter_retweets
    c.Min_likes = min_likes
    c.Since = since.strftime('%Y-%m-%d %H:%M:%S')

    #c.Store_json = True
    c.Store_object = True

    #debug
    #c.Limit = 20
    c.Count = True
    c.Stats = True
    c.Hide_output = True

    twint.run.Search(c)
    tweets = twint.output.tweets_list
    return tweets

    
if __name__ == "__main__":
    main()
