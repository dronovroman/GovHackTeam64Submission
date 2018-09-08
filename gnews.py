# -*- coding: utf-8 -*-
"""
News glugin based on https://newsapi.org/
Google search - canberra times
Created on Sat Sep  8 00:42:27 2018

@author: Roman
"""

import urllib.request
import json
import re
import ssl

big_goog_string=''
bd=[]
cl=[]
ssl._create_default_https_context = ssl._create_unverified_context
CAPITALS = ['Sydney', 'Melbourne', 'Brisbane', 'Darwin', 'Hobart', 'Adelaide', 'Perth', 'Canberra']
gn_key="8a575cb0ec28485bb090447fcae5a402"
key_word = 'cancer'

for city in CAPITALS:
    gn_path="https://newsapi.org/v2/everything?q=" +key_word+"&q="+ city + "&sources=google-news-au&apiKey="+gn_key
    request = urllib.request.Request(gn_path)
    response = urllib.request.urlopen(request)
    j = json.loads(re.search(r'{.*}',response.read().decode('utf-8')).group())
    bd.append(j)
    cl.append(city)
    
    
   

for j in bd:
    for item in j['articles']:
        print(item['title']+'\n')
        big_goog_string +=item['title']
        
        
        
        
big_goog_string=''
bd=[]
cl=[]   
g_adelaide=0;
g_brisvegas=0
g_canberra=0
g_darwin=0
g_hobart=0
g_melbourne=0
g_perth=0
g_sydney=0

for city in CAPITALS:
    gn_path="https://newsapi.org/v2/everything?q=" +key_word+"&q="+ city + "&sources=google-news-au&apiKey="+gn_key
    request1 = urllib.request.Request(gn_path)
    response = urllib.request.urlopen(request1)
    j = json.loads(re.search(r'{.*}',response.read().decode('utf-8')).group())
    bd.append(j)
    cl.append(city)
    for j in bd:
        for item in j['articles']:
            #print(item['title']+'\n')
            big_goog_string +=item['title']
            if key_word in item['title']:
                if city== 'Adelaide':
                    g_adelaide +=1;
                if city== 'Darwin':
                    g_darwin +=1;
                if city== 'Brisbane':
                    g_brisvegas +=1;
                if city== 'Canberra':
                    g_canberra +=1;
                if city== 'Hobart':
                    g_hobart +=1;
                if city== 'Melbourne':
                    g_melbourne +=1;
                if city== 'Perth':
                    g_perth +=1;
                if city== 'Sydney':
                    g_sydney +=1;        
        
        
        