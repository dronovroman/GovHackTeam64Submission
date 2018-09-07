# -*- coding: utf-8 -*-
"""
scraper based on Twitter Search https://github.com/ckoepp/TwitterSearch
Created on Sat Sep  8 07:36:29 2018

@author: Roman
"""

from TwitterSearch import *
try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['Guttenberg', 'Doktorarbeit']) 
    tso.set_language('au') 
    tso.set_include_entities(False)

    ts = TwitterSearch(
        consumer_key = 'aaabbb',
        consumer_secret = 'cccddd',
        access_token = '111222',
        access_token_secret = '333444'
     )

    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: 
    print(e)