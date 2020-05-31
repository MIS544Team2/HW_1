# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

#Import the necessary packages
from twitter import *
import re


# Variables that contains the user credentials to access Twitter API
ACCESS_TOEKN = '298895919-sZSRQi67wIogm33GPZ3ZuGWjWRlp9aEfa6Teqrbn'
ACEESS_KEY = 'TmmVLRxV2NF9ALVrKsjhYLc1TOmgGvkJJ0sH5dLGWELEG'
CONSUMER_KEY = 'UZyQkQ9ZgRAXV6ivtIur6uped'
CONSUMER_SECRET = 'FzdnjWOPOZsbKnLd9UthNEKr5erLcSc2ZAGPgYtHwLwnCvcrgX'

oauth = OAuth(ACCESS_TOEKN, ACEESS_KEY, CONSUMER_KEY,CONSUMER_SECRET)


# Initiate the connection to Twitter API
psearch = Twitter(auth=oauth)



def pos(query):
    global psearch    
    pos_tweets = psearch.search.tweets(q='@IBM :)', count=100)
#    print(pos_tweets)
    with open('q5_pos.txt', 'a', encoding='utf-8') as f:
        json.dump(pos_tweets, f)
    return

def neg(query):
    global psearch    
    neg_tweets = psearch.search.tweets(q=query, count=100)
#    print(neg_tweets)
    with open('q5_neg.json', 'a', encoding='utf8') as f:
        json.dump(neg_tweets, f)
    return

pos(query = '@IBM :)')
pos(query = '@Microsoft :)')
pos(query = '@generalelectric :)')
pos(query = '@SAP :)')
pos(query = '@Oracle :)')
pos(query = '@exxonmobil :)')
pos(query = '@HP :)')
pos(query = '@Accenture :)')
pos(query = '@FedEx :)')
pos(query = '@Siemens :)')
pos(query = '@Cisco :)')
pos(query = '@jpmorgan :)')
pos(query = '@intel :)')
pos(query = '@UBS :)')
pos(query = '@Boeing :)')
pos(query = '@JohnDeere :)')
pos(query = '@northropgrumman :)')
pos(query = '@Huawei :)')
pos(query = '@CaterpillarInc :)')
pos(query = '@UPS :)')

neg(query = '@IBM :(')
neg(query = '@Microsoft :(')
neg(query = '@generalelectric :(')
neg(query = '@SAP :(')
neg(query = '@Oracle :(')
neg(query = '@exxonmobil :(')
neg(query = '@HP :(')
neg(query = '@Accenture :(')
neg(query = '@FedEx :(')
neg(query = '@Siemens :(')
neg(query = '@Cisco :(')
neg(query = '@jpmorgan :(')
neg(query = '@intel :(')
neg(query = '@UBS :(')
neg(query = '@Boeing :(')
neg(query = '@JohnDeere :(')
neg(query = '@northropgrumman :(')
neg(query = '@Huawei :(')
neg(query = '@CaterpillarInc :(')
neg(query = '@UPS :(')
   
