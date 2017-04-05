'''
Created on 5 Apr 2017
@author: brocq18
The following scrapes data from the BBC site on premiership 
football. It outputs the team name and the current points total.
'''
import urllib2 # allows access to url links
from bs4 import BeautifulSoup # used to scrape data from webpages

soup = BeautifulSoup(urllib2.urlopen("http://www.bbc.co.uk/sport/football/tables", "lxml").read()) # reads target url

for row in soup('table', {'class': 'table-stats'})[0].tbody('tr'): # finds table with class = 'table-stats', extracts information contained in the body(tbody) and tags(tr)
    tds = row('td')
    print tds[2].string, tds[10].string # displays team and total points 
