# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:39:51 2017

@author: ses01816300012
"""

from twython import Twython

ConsumerKey = ''
ConsumerSecret = ''
AccessToken = ''
AccessTokenSecret = ''

twitter = Twython(ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret)

result = twitter.search(q="((Saúde OR SUS) AND (Rio Grande do Sul OR RS) OR (SECRETARIA DE SAÚDE OR SECRETARIA DE SAÚDE DO ESTADO DO RIO GRANDE DO SUL OR SECRETARIA DE SAÚDE DO ESTADO DO RS))",
                        result_type='recent', count=10)


#print(type(result))
#for status in result['statuses']:
#    print("user: {0} text: {1}".format(status["user"]["name"], status["text"]))
    

# Initialize empty list to store tweets: tweets_data
tweets_data = []   
    
    
#df = pd.DataFrame.from_dict(result["data"])
dict_normalized = pd.io.json.json_normalize(result)
df = pd.DataFrame(dict_normalized)

for i in df['statuses']:
    print(i)
    
print(df.keys())
print(type(df['statuses']))