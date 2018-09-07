# -*- coding: utf-8 -*-
"""
using web url 
https://twitter.com/search?l=en&q=flu%2C%20OR%20sick%2C%20OR%20cold%20near%3A%22barton%2C%20ACT%22%20within%3A15mi&src=typd&lang=en
https://twitter.com/search?l=&q=flu%20OR%20sick%20OR%20cold%20near%3A%22barton%2C%20%20ACT%22%20within%3A15mi&src=typd&lang=en
Created on Sat Sep  8 07:57:09 2018

@author: Roman
"""


from splinter import Browser
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

url="https://twitter.com/search?l=&q=flu%20OR%20sick%20OR%20cold%20near%3A%22barton%2C%20%20ACT%22%20within%3A15mi&src=typd&lang=en"
options = Options()
browser = Browser()
browser.visit(url)
time.sleep(2)
soup = BeautifulSoup(browser.html, 'lxml')

feeds=soup.find('ol', attrs={'class': 'stream-items js-navigable-stream'})

tweets = feeds.find_all('li')

texts= feeds.find_all('p', attrs={'class':'TweetTextSize js-tweet-text tweet-text'})

tt=[]
for tx in texts:
    print(tx.text+'\n')

