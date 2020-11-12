
import tweepy
import time 
import datetime



CONSUMER_KEY = 'Hjmxs0Zpy0UvCWBcnE5ncizGO'
CONSUMER_SECRET = 'yxx8xhZ4jGImNxPwYD5bPaV70Qkj1VncGcmN4QsZrXv6ar4snl'
ACCESS_KEY = '1326213244441120768-DdXA1e2hRYhFG2In959mqYyyrIzv9y'
ACCESS_SECRET = 'OA5mBk6nsILZ8RwTwuZnFURGqWAMtrMJs4Zz7soSMGys5'




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
       m = "@%s @%s @%s @%s please take notice %s:%s:%s" % (sn,"BeingSanch","DurgaIndia1", "NCWIndia", e.hour,e.minute,e.second)
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
    
