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


pos_tweets=[]
neg_tweets=[]
# searching queries
queries_pos = [ '@IBM :)','@Microsoft :)','@generalelectric :)','@SAP :)','@Oracle :)','@exxonmobil :)','@HP :)','@Accenture :)','@FedEx :)','@Siemens :)','@Cisco :)','@jpmorgan :)','@intel :)','@UBS :)','@Boeing :)','@JohnDeere :)','@northropgrumman :)','@Huawei :)','@CaterpillarInc :)','@UPS :)']
queries_neg = [ '@IBM :(','@Microsoft :(','@generalelectric :(','@SAP :(','@Oracle :(','@exxonmobil :(','@HP :(','@Accenture :(','@FedEx :(','@Siemens :(','@Cisco :(','@jpmorgan :(','@intel :(','@UBS :(','@Boeing :(','@JohnDeere :(','@northropgrumman :(','@Huawei :(','@CaterpillarInc :(','@UPS :(']

# Search and Save tweets in json file
for query in queries_pos:
    pos_search = psearch.search.tweets(q= query, count=100)
    pos_tweets.extend(pos_search['statuses'])

with open('q5_pos.txt', 'w', encoding='utf8') as f:
    json.dump(pos_tweets, f, ensure_ascii=False)


for query in queries_neg:
    neg_search = psearch.search.tweets(q= query, count=100)
    neg_tweets.extend(neg_search['statuses'])

with open('q5_neg.txt', 'w', encoding='utf8') as f:
    json.dump(neg_tweets, f, ensure_ascii=False)

