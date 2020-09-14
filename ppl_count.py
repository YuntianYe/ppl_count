import json
import requests
import pandas as pd
import time

URL = 'https://review.shanghai.nyu.edu/peopleCount2.html'

def get_number(url):
  page = requests.get(url)
  con_s = str(page.content).split(' ')
  for s in con_s:
    if 'NYU' in s:
      result = s 
  res = json.loads(result[:-3]) 
  return res
