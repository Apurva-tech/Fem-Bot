
import tweepy
import time 
import datetime

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

last_seen = None

while True:

    twt = api.search(q="#crimeagainstwomen OR #StopViolenceAgainstWomen OR #domesticabuse OR #womensupportingwomen OR #endhumantrafficking",
                     count=3, tweet_mode='extended', since_id=last_seen) 
    
    if not twt:
        continue
    
    
    last_seen = twt[-1]._json['id'] - 1
    print(last_seen)
    
    '''for status in tweepy.Cursor(api.user_timeline).items():
       try:
           api.destroy_status(status.id)
       except:
           pass'''
                    
    
    
    
    for s in twt:

       # Reply 
       print(s.id)
       e = datetime.datetime.now()
       sn = s.user.screen_name
       m = "@%s @%s @%s @%s %s:%s:%s" % (sn,"CAREGlobal","FemmeInt", "ngowgwps", e.hour,e.minute,e.second)
       api.update_status(status=m, in_reply_to_status_id = s.id)

       # Retweet 

       try:
           # Add \n escape character to print() to organize tweets
           print('\nTweet by: @' + s.user.screen_name)

           # Retweet tweets as they are found
           s.retweet()
           print('Retweeted the tweet')
       except tweepy.TweepError as e:
           print(e.reason)

       except StopIteration:
           break
       
       
    print("Done!!!")
    
    time.sleep(15)
    
