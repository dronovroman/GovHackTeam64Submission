# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:13:25 2018

@author: Roman
"""
import urllib.request
import ssl
from bs4 import BeautifulSoup


ssl._create_default_https_context = ssl._create_unverified_context

key_word="cancer"



gn_path="https://data.gov.au/dataset?q="+key_word+"&sort=extras_harvest_portal+asc%2C+score+desc"
request = urllib.request.Request(gn_path)
response = urllib.request.urlopen(request).read()
soup = BeautifulSoup(response)


name_box = soup.find('ul', attrs={'class': "dataset-list unstyled"})


nbr=str(name_box).replace('href="/dataset','href="https://data.gov.au/dataset').replace('\n',' ')
