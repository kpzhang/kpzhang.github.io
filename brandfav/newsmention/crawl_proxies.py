# -*- coding: utf-8 -*-

import logging
import urllib2
import requests
import html5lib
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


# browser info
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# database info
username = 'root'
password = '123456'
host = 'localhost'
dbase = 'doctorinfo'



def get_soup(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'html5lib')
    return soup

def get_html(url):
    request = urllib2.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36")
    html = urllib2.urlopen(request)
    return html.read()

def fetch_kxdaili(page):

    # www.kxdaili.com

    proxies = []
    try:
        url = "http://www.kxdaili.com/dailiip/1/%d.html" % page
        soup = get_soup(url)
        table_tag = soup.find("table", attrs={"class": "segment"})
        trs = table_tag.tbody.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            ip = tds[0].text
            port = tds[1].text
            latency = tds[4].text.split(" ")[0]
            if float(latency) < 0.5:
                proxy = "%s:%s" % (ip, port)
                proxies.append(proxy)
    except Exception as error:
        print(error)
    print('1',proxies)
    return proxies


def img2port(img_url):

    code = img_url.split("=")[-1]
    if code.find("AO0OO0O") > 0:
        return 80
    else:
        return None


def fetch_mimvp():

    # http: // proxy.mimvp.com / free.php

    proxies = []
    try:
        url = "http://proxy.mimvp.com/free.php?proxy=in_hp"
        soup = get_soup(url)
        table = soup.find("div", attrs={"id": "list"}).table
        tds = table.tbody.find_all("td")
        for i in range(0, len(tds), 10):
            id = tds[i].text
            ip = tds[i + 1].text
            port = img2port(tds[i + 2].img["src"])
            response_time = tds[i + 7]["title"][:-1]
            transport_time = tds[i + 8]["title"][:-1]
            if port is not None and float(response_time) < 1:
                proxy = "%s:%s" % (ip, port)
                proxies.append(proxy)
    except Exception as error:
        print(error)
    print('2', proxies)
    return proxies


def fetch_xici():

    # http://www.xicidaili.com/nn/

    proxies = []
    try:
        url = "http://www.xicidaili.com/nn/"
        soup = get_soup(url)
        table = soup.find("table", attrs={"id": "ip_list"})
        trs = table.find_all("tr")
        for i in range(1, len(trs)):
            tr = trs[i]
            tds = tr.find_all("td")
            ip = tds[1].text
            port = tds[2].text
            proxies.append("%s:%s" % (ip, port))
    except Exception as error:
        print(error)
    print('3', proxies)
    return proxies


# the ping time is too long
def fetch_ip181():

    #http://www.ip181.com/

    proxies = []
    try:
        url = "http://www.ip181.com/"
        soup = get_soup(url)
        table = soup.find("table")
        trs = table.find_all("tr")
        for i in range(1, len(trs)):
            tds = trs[i].find_all("td")
            ip = tds[0].text
            port = tds[1].text
            latency = tds[4].text[:-2]
            if float(latency) < 1:
                proxies.append("%s:%s" % (ip, port))
    except Exception as error:
        print(error)
    print('4', proxies)
    return proxies


def fetch_httpdaili():

    # http://www.httpdaili.com/mfdl/

    proxies = []
    try:
        url = "http://www.httpdaili.com/mfdl/"
        soup = get_soup(url)
        table = soup.find("div", attrs={"kb-item-wrap11"}).table
        trs = table.find_all("tr")
        for i in range(1, len(trs)):
            try:
                tds = trs[i].find_all("td")
                ip = tds[0].text
                port = tds[1].text

                proxies.append("%s:%s" % (ip, port))
            except:
                pass
    except Exception as error:
        print(error)
    print('4', proxies)
    return proxies


def fetch_66ip():

    # http://www.66ip.cn/

    proxies = []
    try:
        # change getnum to set numbers of proxies
        url = "http://www.66ip.cn/nmtq.php?getnum=10&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip"
        content = get_html(url)
        urls = content.split("</script>")[2].split("<br/>")
        for u in urls:
            if u.strip():
                if len(u.strip()) <= 20:
                    proxies.append(u.strip())

    except Exception as error:
        print(error)
    print('5', proxies)
    return proxies


def check(proxy):

    proxies = {
        'http': 'http://%s' % (proxy)
    }
    url = 'https://www.google.com/search?q=google'
    try:
        wb_data = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        if len(wb_data.text) > 30000:
            #print(proxy)
            return True
        else:
            print('fail')
            return False
    except Exception:
        return False


def fetch_all(endpage=2):

    proxies = []

    for i in range(1, endpage):
        proxies.append(fetch_kxdaili(i))
    proxies.append(fetch_mimvp())
    proxies.append(fetch_xici())
    # proxies += fetch_ip181()
    proxies.append(fetch_httpdaili())
    proxies.append(fetch_66ip())

    for p in proxies:
        if check(p):
            print p



fetch_all()