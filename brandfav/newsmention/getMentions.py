#!/usr/bin/python

import os
import sys
import re
import time
import random
from random import randint


import requests
import urllib2
from bs4 import BeautifulSoup


REGEX = r'(\d+)\s*result'

def get_proxy_address():
	pafile = "all_ips.txt"
	pas = []
	fh = open(pafile,'r')
	lines = fh.readlines()
	fh.close()
	for line in lines:
		pas.append(line.strip())

	proxy_address = random.choice(pas)

	return proxy_address


def get_header():
	uafile = "user_agents.txt"
	uas = []
	fh = open(uafile, 'r')
	lines = fh.readlines()
	fh.close()
	for line in lines:
		uas.append(line.strip())

	header = random.choice(uas)

	return header


def extract_results_stat(url):
	proxy_address = get_proxy_address()
	user_agent = get_header()

	headers = {
		'Accept': '*/*',
		'Accept-Encoding': 'gzip,deflate,sdch',
		'Accept-Language': 'en-US',
		'Cache-Control': 'max-age=0',
		'Connection': 'keep-alive',
		'User-Agent': user_agent
	}

	proxies = { 
    	'http': 'http://%s' % (proxy_address)
    }

	search_results = requests.get(url, allow_redirects=True, timeout=10)#headers=headers, proxies=proxies, allow_redirects=True, timeout=10)
	soup = BeautifulSoup(search_results.text)
	result_stats = soup.find(id='resultStats')
	#print result_stats.text

	m = re.match(REGEX, result_stats.text.replace('About ',''))
	number = m.group(1)
	if len(number) > 1:
		number = int(number.replace(',',''))
	else:
		number = int(number)

	return number



def main():
    brands = sys.argv[1]

    fh = open(brands,'r')
    lines = fh.readlines()
    fh.close()

    for i in range(239,274):#len(lines)):
        line = lines[i].strip()
        arr = re.split(',',line)
        keyword = re.sub(r'&|"','',arr[0].strip())
        fid = arr[1].strip()

        val = int(arr[2].strip())
        if val > 0:
            print line
            continue

        news_url = 'https://www.google.co.in/search?q="' + keyword + '"+site:finance.yahoo.com/news&source=lnt&tbs=cdr:1,cd_min:1/1/2016,cd_max:1/1/2015'
        #print news_url
        try:
            result = extract_results_stat(news_url)
            print keyword,',',fid,',',result
        except:
            print keyword,',',fid,', 0'

        time.sleep(randint(1,5))


if __name__ == "__main__":
    main()
