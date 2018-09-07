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

ssl._create_default_https_context = ssl._create_unverified_context

gn_key="8a575cb0ec28485bb090447fcae5a402"
gn_path="https://newsapi.org/v2/everything?q=flu&sources=google-news-au&apiKey="+gn_key


request = urllib.request.Request(gn_path)


response = urllib.request.urlopen(request)
j = json.loads(re.search(r'{.*}',response.read().decode('utf-8')).group())
