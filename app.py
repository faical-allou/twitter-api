import psycopg2
import os
import json
import collections
import datetime
import sys
import math
import gc
import tweepy
from models.extractdata import *
from configdatabase import key1, key2, key3, key4


extractdata = extractdata()

auth = tweepy.OAuthHandler(key1,key2)
auth.set_access_token(key3,key4)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        created = status.created_at
        text = status.text
        if status.place is not None:
            place = status.place.country_code
        else:
            place = "unknown location"
        
        if 'trivago' in text.lower():
            keyword = 'trivago'
        elif 'skyscanner' in text.lower():
            keyword = 'skyscanner'
        elif 'tripadvisor' in text.lower():
            keyword = 'tripadvisor'
        elif 'hotelscombined' in text.lower():
            keyword = 'hotelscombined'
        elif 'momondo' in text.lower():
            keyword = 'momondo'
        else:
            keyword = 'unknown'

        extractdata.insert_data(created,text,place, keyword)
        print(created, '\n', text,'\n', place, '\n',keyword)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['trivago', 'skyscanner', 'tripadvisor', 'hotelscombined', 'momondo' ])

