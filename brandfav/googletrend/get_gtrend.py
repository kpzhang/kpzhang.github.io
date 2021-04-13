#!/usr/bin/python

import os
import sys
import re
import json
import time
from random import randint

from pytrends.request import TrendReq

google_username = 'YOUR GMAIL'
google_password = 'YOUR PASSWORD'

pt = TrendReq(google_username,google_password,custom_useragent=None)

brands = sys.argv[1]
start = int(sys.argv[2])

fh = open(brands,'r')
lines = fh.readlines()
fh.close()

#print "facebook page name,GoogleTrend"
for i in range(start,len(lines)):
    arr = lines[i].strip().split(',')
    fname = arr[0].strip()
    fname = re.sub(r'\W+',' ',fname)
    fid = arr[1].strip()

    pt = TrendReq(google_username,google_password,custom_useragent=None)

    trend_payload = {'q':fname, 'date':'01/2015 12m'} 
    try:
        response = pt.trend(trend_payload,return_type='json')
        weeks = response['table']['rows']
        total = 0
        for k in range(len(weeks)):
            week = weeks[k]
            val = week['c'][1]['v']
            total += float(val)
        avg = total/len(weeks)

        print fid,",",avg
        time.sleep(randint(10,12))
    except:
        print fid,", 0"
        time.sleep(10)
