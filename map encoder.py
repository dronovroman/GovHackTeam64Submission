# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:02:42 2018

@author: Roman
"""
import pandas as pd

overallmarker=''

template= """ 	L.marker([coords]).addTo(mymap).bindPopup("popup text");  """

dtset=pd.read_csv("health.csv")

for index, row in dtset.iterrows():
   lat = str(row[0][1:])
   lon = str(row[1])
   cc=lat+', '+lon
   desc= str(row[3])
   overallmarker += template.replace('coords',cc).replace('popup text',desc) +'\n'
   #print (row[0][1:], row[1], row[3], row[4])
   