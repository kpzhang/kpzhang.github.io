import os
import sys

from bs4 import BeautifulSoup
import requests


def get_contents(url):
    web_base_url = 'http://www.aflcio.org'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    
    # get all link urls
    all_links = []
    all_dates = []
    letters = soup.findAll('div',{'class':'ec_statements'})
    for letter in letters:
        link = letter.find('a').get('href')
        complete_link = web_base_url+link
        all_links.append(complete_link)
        date = letter.find('div',{'id':'legalert_date'}).get_text()
        splits = date.split(',')
        year = str(splits[1].strip())
        month = splits[0].split(' ')[0]
        day = str(splits[0]).split(' ')[1]        
        date_str = month+'-'+day+'-'+year
        all_dates.append(date_str)
        #print complete_link,':',date_str
    
    # create a folder to store output files
    if not os.path.exists('output-2'):
        os.makedirs('output-2')
    
    # get the content for each url link    
    for i in range(len(all_links)):
        link = all_links[i]
        filename = all_dates[i]
        filename_path = os.path.join('output-2',filename)
        fh = open(filename_path,'w')
    
        r = requests.get(link)
        soup = BeautifulSoup(r.text)
        attribute_body = soup.find('div',{'class':'attribute-body'})
        all_p_tags = attribute_body.findAll('p') # get all <p> tags
        for p in all_p_tags:
            text = p.get_text()+'\n'
            fh.write(text.encode('utf-8'))
        fh.close()
        
        
def main():
   base_url = 'http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts'
   for year in range(2015,2017):
       url = base_url+'/(y)/'+str(year)
       get_contents(url) 

if __name__ == '__main__':
    main()