# -*- coding: utf-8 -*-
"""
Tweeter searcher
Created on Sat Sep  8 00:13:23 2018
@author: Roman
"""
import tweepy
#from twitter_authentification import API_KEY, API_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, USR, PASSWD
from twitter_auth import USR, PASSWD


#auth = tweepy.AppAuthHandler? no longer supported
BasicAuthHandler(USR, PASSWD)
api = tweepy.API(auth)
  

query = 'python'
max_tweets = 100
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
