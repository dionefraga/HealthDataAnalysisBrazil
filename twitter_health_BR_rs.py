# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:37:04 2017

@author: ses01816300012
"""

# Import packages
import tweepy, json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")
        #self.file_name = "tweets.txt"

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        #with open(self.file_name, 'w') as file:
        #   file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
print(stream.filter(track=['AbraSUS', 'SUSRS', 'RSSUS', 'Saúde']))
#PROCURAR POR FILTROS DE HASHTAGS


#read twitter file
# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
#print(tweets_data[0].keys())
#print(tweets_data[0].values())


df = pd.DataFrame(tweets_data, columns=['text','lang'])
#print(df['text'])



import re

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


# Initialize list to store tweet counts
[saude, sus, rs] = [0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    saude += word_in_text('#AbraSUS', row['text'])
    sus += word_in_text('#SUSRS', row['text'])
    rs += word_in_text('#RSSUS', row['text'])


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['abrasus', 'susrs', 'rssus']

# Plot histogram
ax = sns.barplot(cd, [saude,sus,rs])
ax.set(ylabel="count")
plt.show()


    
    
