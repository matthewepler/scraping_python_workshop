# Scraper for www.deadlists.com
# Matthew Epler, 2016 
# matthewepler@gmail.com


from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

baseURL = "http://deadlists.com/deadlists/yearresults.asp?KEY=1967"
html = urlopen(baseURL)
bs = BeautifulSoup(html, 'lxml')
print(bs.prettify());
