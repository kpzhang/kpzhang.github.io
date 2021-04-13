#!/usr/bin/python

import os
import sys
import re

proxy_file = sys.argv[1]
fh = open(proxy_file,'r')
lines = fh.readlines()
fh.close()

for line in lines:
	line = re.sub(r"[\[|\]|u|']",'',line.strip())
	ips = re.split(r'[,\s]+',line)
	for ip in ips:
		print ip