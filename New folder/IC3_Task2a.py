import urllib.request
from bs4 import BeautifulSoup
import os
import pandas as pd

link ='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
hi = urllib.request.urlopen(link)
parsedCode = BeautifulSoup(urllib.request.urlopen(link),"html.parser")
print(parsedCode.prettify())
print(parsedCode.title)
aTags = parsedCode.find_all('a')
print(aTags)
for i in aTags:
    print(i.get('href'))