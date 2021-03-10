import os
import sys

from bs4 import BeautifulSoup
import requests


def get_contents(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    
    # get all link urls
    all_links = []
    for link in soup.findAll('a'):
        all_links.append(link.get('href'))
    
    # get all valid links for our tasks
    valid_links = []
    for link in all_links:
        final_url_element = link.split('/')[-1]
        if final_url_element.startswith('index.php?'):
            valid_links.append(link)

    # create a folder to store output files
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # get the content for each valid url link    
    for link in valid_links:
        filename = link.split('=')[-1]+'.txt'
        filename_path = os.path.join('output',filename)
        fh = open(filename_path,'w')
    
        r = requests.get(link)
        soup = BeautifulSoup(r.text)
        all_p_tags = soup.findAll('p') # get all <p> tags
        for p in all_p_tags:
            text = p.get_text()+'\n'
            fh.write(text.encode('utf-8'))
        fh.close()
        
def main():
   presidency_platforms_url = 'http://www.presidency.ucsb.edu/platforms.php'
   get_contents(presidency_platforms_url) 

if __name__ == '__main__':
    main()