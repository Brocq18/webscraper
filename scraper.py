'''
Created on 5 Apr 2017
@author: brocq18
The following scrapes data from the BBC site on premiership 
football. It outputs the team name and the current points total.
'''
import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen("http://www.bbc.co.uk/sport/football/tables", "lxml").read())

for row in soup('table', {'class': 'table-stats'})[0].tbody('tr'):
    tds = row('td')
    print tds[2].string, tds[10].string # displays team and total points
    