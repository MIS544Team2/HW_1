try:
    import json
except ImportError:
    import simplejson as json

import json
import pandas as pd
import re
import nltk
from string import punctuation
from nltk.tokenize import word_tokenize
# nltk.download('stopwords')
from nltk.corpus import stopwords
import random

#--------Import positive dataset retrieved from Q5 and write in data frame
data = json.load(open('q5_pos.txt'))
file = json.dumps(data)
pos_tweets = json.loads(file)

#for tweet in pos_tweets:
#    print(tweet['text'])
tweet_df=[] 
for tweet in pos_tweets:
    tweet_df.append(tweet["text"])

tweet_df_pos = pd.DataFrame(data=tweet_df, columns =["Tweets"]) 
#tweet_df_pos.head()

#--------Import negative dataset retrieved from Q5 and write in data frame
data = json.load(open('q5_neg.txt'))
file = json.dumps(data)
neg_tweets = json.loads(file)

#for tweet in neg_tweets:
#    print(tweet['text'])

# Pre-processing Tweets in the Data Sets
tweet_df=[] 
for tweet in neg_tweets:
    tweet_df.append(tweet["text"])
tweet_df_neg = pd.DataFrame(data=tweet_df, columns =["Tweets"]) 
# tweet_df_neg.head()

#-------- Pre-processing Tweets in the Data Sets
def cleanTxt(tweet):
    tweet = tweet.lower() # convert text to lower-case
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
    tweet = re.sub('@[A-Za-z0–9]+', '', tweet) #Removing @mentions
    tweet = re.sub('RT[\s]+', '', tweet) # Removing RT
    tweet = re.sub('RT[\s]+', '', tweet) # Removing RT
    tweet = re.sub('https?:\/\/\S+', '', tweet) # Removing hyperlink
    return tweet

tweet_df_pos["Tweets"] = tweet_df_pos["Tweets"].apply(cleanTxt)
tweet_df_pos["Category"]='pos'
tweet_df_neg["Tweets"] = tweet_df_neg["Tweets"].apply(cleanTxt)
tweet_df_neg["Category"]='neg'


doc_pos = [(list(word_tokenize(field)), category)
for category in tweet_df_pos['Category']
for field in tweet_df_pos['Tweets']]

doc_neg = [(list(word_tokenize(field)), category)
for category in tweet_df_neg['Category']
for field in tweet_df_neg['Tweets']]

document = doc_pos + doc_neg

random.shuffle(document)
#-------- Randomly split data into trainset and testset

#train_pos=tweet_df_pos.sample(frac=0.9, random_state=0)
#test_pos=tweet_df_pos.drop(train_pos.index)
#train_neg= tweet_df_neg.sample(frac=0.9, random_state=0)
#test_neg= tweet_df_neg.drop(train_neg.index)

#-------- Extract tokens and remove stopwords in Train sets
stop_words=set(stopwords.words('english') + list(punctuation) + ['AT_USER','URL'])
def tweet_prep(tweets):
    # Extract all words in the training set and break into token features 
    all_tokens=[]
    for tweet in tweets['Tweets']: 
        text_tokens = word_tokenize(tweet)
        tokens=[word for word in text_tokens if not word in stop_words]
        all_tokens.extend(tokens)
    return all_tokens

tokens_pos=tweet_prep(tweet_df_pos)
tokens_neg=tweet_prep(tweet_df_neg)
tokens_all=tokens_pos + tokens_neg
# Get a list of distict words with its frequency as a key
all_words=nltk.FreqDist(tokens_all)
token_features= all_words.keys()


#-------- Build up feature vector

def extract_features(doc):
    words=set(doc)
    features ={}
    for w in token_features:
        features[w] = (w in words)
    return features

featuresets = [(extract_features(tweet), category) for (rev, category) in document]



training_set= featuresets[:1500]
testing_set= featuresets[500:]


classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)


