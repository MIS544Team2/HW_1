try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import *

# Variables that contains the user credentials to access Twitter API
ACCESS_TOEKN = '298895919-sZSRQi67wIogm33GPZ3ZuGWjWRlp9aEfa6Teqrbn'
ACEESS_KEY = 'TmmVLRxV2NF9ALVrKsjhYLc1TOmgGvkJJ0sH5dLGWELEG'
CONSUMER_KEY = 'UZyQkQ9ZgRAXV6ivtIur6uped'
CONSUMER_SECRET = 'FzdnjWOPOZsbKnLd9UthNEKr5erLcSc2ZAGPgYtHwLwnCvcrgX'

oauth = OAuth(ACCESS_TOEKN, ACEESS_KEY, CONSUMER_KEY,CONSUMER_SECRET)

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re

# Create tracklist with the words that will be searched for
tracklist = ['@IBM']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 10

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)



# Handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOEKN, ACEESS_KEY)
stream = Stream(auth, l)
stream.filter(track=tracklist)
    
