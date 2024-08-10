#!/usr/local/bin/python 

#*** DO NOT EDIT - GENERATED FROM services.ipynb ****

import os, json
from  mangorest.mango import webapi
from geoapp.utils import read_csv, readfile

BASE = "/opt/data/data/stocks/data"

#--------------------------------------------------------------------------------------------------------    
DEFAULT_FILE = f'{BASE}/stocks.csv'
@webapi("/stocks/getsymbols")
def getsymbols(request, user="", **kwargs):
    file = f'{BASE}/{user}/stocks.csv'
    if (not user or not os.path.exists(file)):
        file = DEFAULT_FILE

    df, ret = read_csv(file)
    return ret 
#--------------------------------------------------------------------------------------------------------    
@webapi("/stocks/getDetails")
def getdetails(request, q="dow_jones", duration="all", user="", **kwargs):
    symbol = q
    csv     = f'{BASE}/{symbol}/daily.csv'
    csv_aug = f'{BASE}/{symbol}/daily_aug.csv'

    if os.path.exists(csv_aug):
        csv = csv_aug
    elif ( not os.path.exists(csv  )):
        csv   = f'{BASE}/dow_jones/daily.csv'

    news    = f'{BASE}/{symbol}/news.html'
    stats1  = f'{BASE}/{symbol}/summary.json'
    stats2  = f'{BASE}/{symbol}/fundamentals.json'

    if (not os.path.exists(news  )): news  = f'{BASE}/dow_jones/news.html'
    if (not os.path.exists(stats1)): stats1= f'{BASE}/dow_jones/summary.json'

    s1 = json.loads(readfile(stats1, "{}"))
    s2 = json.loads(readfile(stats2, "{}"))
    s2.update(s1)

    print(f"Symbol Details :{csv} - {news} {stats1}")

    df, ret = read_csv(csv)
    ret['news'] = readfile(news, "")
    ret['stats']= json.dumps(s2)

    return ret
