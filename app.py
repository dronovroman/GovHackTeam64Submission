# -*- coding: utf-8 -*-
"""
Flask app UI
Created on Sat Sep  8 12:34:46 2018

@author: Roman
"""


from flask import Flask, render_template, request, Response, render_template_string, stream_with_context,  send_file
import webbrowser
import urllib.request
import json
import re
import ssl
from bs4 import BeautifulSoup

CAPITALS = ['Sydney', 'Melbourne', 'Brisbane', 'Darwin', 'Hobart', 'Adelaide', 'Perth', 'Canberra']
ssl._create_default_https_context = ssl._create_unverified_context
gn_key="8a575cb0ec28485bb090447fcae5a402"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/start_job", methods=["POST"]) 
def start_job():
    #our main module to render a bunch of google charts...
    #query keyword is passed here from the landing page
    key_word = request.form["keyw"]
    key_word=key_word.lower()
    

#tweeter text analytics based on pre-scraped twees (due to delay in considaration of our twitter API application)
    #SA
    kwd = " "+key_word+" " 
    key_word = urllib.parse.quote(key_word)
    
    
    relevant_tweets_adelaide=''
    t_adelaide=0
    with open("tweeter/Adelaide.txt") as openfile:
        for line in openfile:
            #for part in line.split('.'):
            if kwd in line.strip():
                #print (line)
                relevant_tweets_adelaide += line.strip()
                t_adelaide+=1
                
    # Syd
    relevant_tweets_sydney=''
    t_sydney=0
    with open("tweeter/Sydney.txt") as openfile:
        for line in openfile:
            #for part in line.split('.'):
            if kwd  in line:
                #print (line)
                relevant_tweets_sydney += line.strip()
                t_sydney+=1
                
                    
    # Melbs                
    relevant_tweets_melbourne=''
    t_melbourne=0
    with open("tweeter/Melbourne.txt") as openfile:
        for line in openfile:
            #for part in line.split('.'):
            if kwd in line:
                #print (line)
                relevant_tweets_melbourne += line
                t_melbourne+=1

    # Brisbane                
    relevant_tweets_brisvegas=''
    t_brisvegas=0
    with open("tweeter/Brisbane.txt") as openfile:
        for line in openfile:
            #for part in line.split():
            if kwd in line:
                #print (line)
                relevant_tweets_brisvegas += line
                t_brisvegas+=1
                
    # Darwin                
    relevant_tweets_darwin=''
    t_darwin=0
    with open("tweeter/Darwin.txt") as openfile:
        for line in openfile:
            #for part in line.split():
            if kwd in line:
                #print (line)
                relevant_tweets_darwin += line                
                t_darwin+=1
                

    # Hobart                
    relevant_tweets_hobart=''
    t_hobart=0
    with open("tweeter/Hobart.txt") as openfile:
        for line in openfile:
            #for part in line.split():
            if kwd in line:
                #print (line)
                relevant_tweets_hobart += line                
                t_hobart+=1
                
    
    
    # Perth                
    relevant_tweets_perth=''
    t_perth=0
    with open("tweeter/Perth.txt") as openfile:
        for line in openfile:
            #for part in line.split():
            if kwd in line:
                #print (line)
                relevant_tweets_perth += line                
                t_perth+=1

    
    # Canberra             
    relevant_tweets_canberra=''
    t_canberra=0
    with open("tweeter/Canberra.txt") as openfile:
        for line in openfile:
            #for part in line.split():
            if kwd in line:
                #print (line)
                relevant_tweets_canberra += line    
                t_canberra+=1

    
    
    all_tweets=relevant_tweets_adelaide + relevant_tweets_brisvegas + relevant_tweets_canberra + relevant_tweets_darwin + relevant_tweets_hobart + relevant_tweets_melbourne + relevant_tweets_perth +relevant_tweets_sydney
    #print(len(all_tweets))      
    
    tweeter_string= all_tweets
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    big_goog_string=''
    big_goog_string_rel=''
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
                big_goog_string_rel +=item['title']
    
    tweeter_string = tweeter_string.replace("\r"," ").replace("\n"," ").lower().strip()
    if len(tweeter_string)>1500:
        tweeter_string=tweeter_string[0:1500]        
    google_string_rel = big_goog_string_rel.replace("\r"," ").replace("\n"," ").lower().strip()
    if len(google_string_rel)>1500:
        google_string_rel=google_string_rel[0:1500] 
    #print(key_word)
    print('twitter lengths:', len(tweeter_string))
    print('google lengths:', len(google_string_rel))
    
    print('Tweeter statististics by state: ', t_adelaide, t_brisvegas, t_canberra, t_darwin, t_hobart, t_melbourne, t_perth, t_sydney)
    print('Google news statististics by state: ', g_adelaide, g_brisvegas, g_canberra, g_darwin, g_hobart, g_melbourne, g_perth, g_sydney)    
    #now we have general stats for tweets and news for each state
    vic_t = t_melbourne
    nsw_t = t_sydney
    act_t = t_canberra
    wa_t = t_perth
    tas_t = t_hobart
    qld_t = t_brisvegas
    sa_t = t_adelaide
    nt_t = t_darwin
    
    vic_g = g_melbourne
    nsw_g = g_sydney
    act_g = g_canberra
    wa_g = g_perth
    tas_g = g_hobart
    qld_g = g_brisvegas
    sa_g = g_adelaide
    nt_g = g_darwin 

    
    
    ###
    ###
    ###
    #search query
    data_path="https://data.gov.au/dataset?q="+key_word+"&sort=extras_harvest_portal+asc%2C+score+desc"
    request_data = urllib.request.Request(data_path)
    response_data = urllib.request.urlopen(request_data).read()
    soup_d = BeautifulSoup(response_data)
    name_box = soup_d.find('ul', attrs={'class': "dataset-list unstyled"})    
    nbr=str(name_box).replace('href="/dataset','href="https://data.gov.au/dataset').replace('\n',' ').replace('dataset-list unstyled','list-group').replace('dataset-item','list-group-item').replace('h3','h5').replace('h1','h5')
    
    
    #print(vic_t)
    return render_template('results.html', tweeter_feed = tweeter_string, key_wd = key_word, google_feed = google_string_rel, vic_t=vic_t, nsw_t=nsw_t,act_t=act_t, wa_t=wa_t, tas_t=tas_t,qld_t=qld_t, sa_t=sa_t, nt_t=nt_t, vic_g=vic_g, nsw_g=nsw_g, act_g=act_g, wa_g=wa_g, tas_g=tas_g, qld_g=qld_g, sa_g=sa_g, nt_g=nt_g, ndr=nbr, srcht=key_word)





if __name__ == "__main__":
    urll='http://127.0.0.1:5000/'
    webbrowser.open(urll, new=2, autoraise=True)
    app.run()
