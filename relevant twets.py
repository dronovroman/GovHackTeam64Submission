# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:33:58 2018

@author: Roman
"""

key_word='cancer'
#######################


#SA
relevant_tweets_adelaide=''
t_adelaide=0
with open("tweeter/Adelaide.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_adelaide += line
                t_adelaide+=1
                
# Syd
relevant_tweets_sydney=''
t_sydney=0
with open("tweeter/Sydney.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_sydney += line
                t_sydney+=1
                
                
# Melbs                
relevant_tweets_melbourne=''
t_melbourne=0
with open("tweeter/Melbourne.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_melbourne += line
                t_melbourne+=1

# Brisbane                
relevant_tweets_brisvegas=''
t_brisvegas=0
with open("tweeter/Brisbane.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_brisvegas += line
                t_brisvegas+=1
                
# Darwin                
relevant_tweets_darwin=''
t_darwin=0
with open("tweeter/Darwin.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_darwin += line                
                t_darwin+=1
                

# Hobart                
relevant_tweets_hobart=''
t_hobart=0
with open("tweeter/Hobart.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_hobart += line                
                t_hobart+=1
                


# Perth                
relevant_tweets_perth=''
t_perth=0
with open("tweeter/Perth.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_perth += line                
                t_perth+=1


# Canberra             
relevant_tweets_canberra=''
t_canberra=0
with open("tweeter/Canberra.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if key_word in part:
                print (line)
                relevant_tweets_canberra += line    
                t_canberra+=1



all_tweets=relevant_tweets_adelaide + relevant_tweets_brisvegas + relevant_tweets_canberra + relevant_tweets_darwin + relevant_tweets_hobart + relevant_tweets_melbourne + relevant_tweets_perth +relevant_tweets_sydney
print(len(all_tweets))                